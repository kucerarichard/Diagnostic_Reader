"""Read a framework snapshot (directory or ZIP) and resolve stems to files.

The kernel's File Reference Rule: a reference names the unversioned stem, the
file name carries the version, and the operator resolves the stem against what
is on disk. This module is that operator.
"""
from __future__ import annotations

import hashlib
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional

from .registry import Registry, RegistryError, parse_version

KERNEL_PREFIX = "0a-portable-poetics-kernel"

# file name:  <stem>-v0_3_19.md   or   <stem>-v0.2.md   or   <stem>.md
_FILENAME_RE = re.compile(r"^(?P<stem>.+?)(?:-v(?P<ver>\d+(?:[._]\d+)*))?\.md$", re.IGNORECASE)

# version lines seen in the bundle, in priority order
_HEADER_PATTERNS = [
    re.compile(r"^\s*Module version:\s*v?(\d+(?:\.\d+)*)", re.M | re.I),
    re.compile(r"^\s*Plugin version:\s*v?(\d+(?:\.\d+)*)", re.M | re.I),
    re.compile(r"^\s*\**Version\**:?\s*\**\s*v?(\d+(?:\.\d+)*)", re.M | re.I),
    re.compile(r"^## Revision Note \(v(\d+(?:\.\d+)*)\)", re.M),
]
_HEADER_SCAN_CHARS = 4000


class SnapshotError(ValueError):
    pass


@dataclass
class FrameworkFile:
    name: str                  # file name as on disk, e.g. 0a-portable-poetics-kernel-v0_3_19.md
    stem: str                  # unversioned stem
    filename_version: Optional[str]
    header_version: Optional[str]
    size: int
    sha256: str
    _read: object = field(repr=False, default=None)

    @property
    def version(self) -> Optional[str]:
        """Header wins; the file name is the fallback. Lint reports disagreement."""
        return self.header_version or self.filename_version

    def read_bytes(self) -> bytes:
        return self._read()

    def read_text(self) -> str:
        """Decoded text with line endings normalized to LF. The sha256 is of the raw bytes."""
        return self.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


@dataclass
class Snapshot:
    source: Path
    root: str                       # subdirectory inside a zip, or "" for a directory
    files: Dict[str, FrameworkFile]  # by stem
    by_name: Dict[str, FrameworkFile]
    duplicates: Dict[str, List[str]]  # stem -> file names, when more than one release is present
    skipped: List[str]               # markdown files not treated as framework files
    is_zip: bool

    def get(self, stem: str) -> Optional[FrameworkFile]:
        return self.files.get(stem)

    def require(self, stem: str) -> FrameworkFile:
        f = self.files.get(stem)
        if f is None:
            raise SnapshotError(f"{stem} is not in the snapshot at {self.source}")
        return f

    def version_of(self, stem: str) -> Optional[str]:
        f = self.files.get(stem)
        return f.version if f else None


def split_filename(name: str) -> tuple:
    m = _FILENAME_RE.match(name)
    if not m:
        return name, None
    ver = m.group("ver")
    return m.group("stem"), (ver.replace("_", ".") if ver else None)


def header_version(text: str) -> Optional[str]:
    head = text[:_HEADER_SCAN_CHARS]
    for pat in _HEADER_PATTERNS:
        m = pat.search(head)
        if m:
            try:
                parse_version(m.group(1))
            except RegistryError:
                continue
            return m.group(1).rstrip(".")
    return None


def _is_runtime_candidate(relpath: PurePosixPath, registry: Registry) -> bool:
    if relpath.suffix.lower() != ".md":
        return False
    if any(part in registry.non_runtime_dirs for part in relpath.parts[:-1]):
        return False
    if relpath.name in registry.non_runtime_files:
        return False
    return True


def _find_root(names: List[str]) -> str:
    """Pick the directory that holds the kernel, so a zip with one top folder works."""
    for n in names:
        p = PurePosixPath(n)
        if p.name.startswith(KERNEL_PREFIX):
            return str(p.parent) if str(p.parent) != "." else ""
    raise SnapshotError("no portable kernel file found in the snapshot")


def load_snapshot(source: Path, registry: Registry) -> Snapshot:
    source = Path(source).resolve()
    if not source.exists():
        raise SnapshotError(f"snapshot does not exist: {source}")

    entries: List[tuple] = []  # (relative posix path, read callable)
    is_zip = source.is_file()
    if is_zip:
        # Read the archive eagerly and close it. A handle held open for lazy reads
        # blocks deleting or replacing the file on Windows, and the bundle is a few MB.
        try:
            with zipfile.ZipFile(source, "r") as zf:
                names = [i.filename for i in zf.infolist() if not i.is_dir()]
                root = _find_root(names)
                for n in names:
                    p = PurePosixPath(n)
                    rel_parent = str(p.parent) if str(p.parent) != "." else ""
                    if root and not (rel_parent == root or rel_parent.startswith(root + "/")):
                        continue
                    if p.suffix.lower() != ".md":
                        continue
                    rel = PurePosixPath(n[len(root) + 1:]) if root else p
                    data = zf.read(n)
                    entries.append((rel, (lambda data=data: data)))
        except zipfile.BadZipFile as exc:
            raise SnapshotError(f"{source} is neither a directory nor a ZIP") from exc
    else:
        root = ""
        for path in sorted(source.rglob("*.md")):
            rel = PurePosixPath(path.relative_to(source).as_posix())
            entries.append((rel, (lambda path=path: path.read_bytes())))

    files: Dict[str, FrameworkFile] = {}
    by_name: Dict[str, FrameworkFile] = {}
    duplicates: Dict[str, List[str]] = {}
    skipped: List[str] = []
    for rel, read in sorted(entries, key=lambda e: str(e[0])):
        if not _is_runtime_candidate(rel, registry):
            if rel.suffix.lower() == ".md":
                skipped.append(str(rel))
            continue
        if len(rel.parts) != 1:
            skipped.append(str(rel))
            continue
        data = read()
        stem, fver = split_filename(rel.name)
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            skipped.append(str(rel))
            continue
        ff = FrameworkFile(
            name=rel.name, stem=stem, filename_version=fver,
            header_version=header_version(text), size=len(data),
            sha256=hashlib.sha256(data).hexdigest(), _read=read,
        )
        by_name[ff.name] = ff
        if stem in files:
            duplicates.setdefault(stem, [files[stem].name]).append(ff.name)
            # keep the higher version on disk as the resolution
            if _newer(ff, files[stem]):
                files[stem] = ff
        else:
            files[stem] = ff
    if KERNEL_PREFIX not in files:
        raise SnapshotError(f"no portable kernel in {source}")
    return Snapshot(source=source, root=root, files=files, by_name=by_name,
                    duplicates=duplicates, skipped=skipped, is_zip=is_zip)


def _newer(a: FrameworkFile, b: FrameworkFile) -> bool:
    try:
        return parse_version(a.version or "0") > parse_version(b.version or "0")
    except RegistryError:
        return a.name > b.name
