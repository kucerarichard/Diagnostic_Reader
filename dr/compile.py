"""Write the prompt a load plan describes.

Output is one Markdown file (or several parts, split at file boundaries)
plus build-manifest.json. The prompt holds, in order: a header with the
load set and any withheld files, every planned framework file fenced and
labeled, the specimen card and text, and the operator request line. That is
the order a chat operator produces by uploading files and then typing the
request, so the model meets the same shape.

Text only. A specimen that is not UTF-8 text is an error.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import __version__
from .registry import Registry
from .request import Request
from .resolve import LoadPlan
from .snapshot import Snapshot

RULE = "=" * 88
SPECIMEN_META_KEYS = ("title", "author", "date", "edition", "kind", "unit", "provenance", "copyright", "found by")
_META_LINE = re.compile(r"^(title|author|date|edition|kind|unit|provenance|copyright|found by):\s*(.*)$", re.I)


class CompileError(ValueError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fence(text: str, language: str = "text") -> str:
    """A fence longer than any backtick run in the payload."""
    runs = [len(x) for x in re.findall(r"`+", text)]
    ticks = "`" * max(3, (max(runs) + 1) if runs else 3)
    return f"{ticks}{language}\n{text.rstrip()}\n{ticks}\n"


def section(title: str, body: str) -> str:
    return f"\n{RULE}\n{title}\n{RULE}\n\n{body.rstrip()}\n"


# ---- specimens ----------------------------------------------------------------

@dataclass
class Specimen:
    path: str
    text: str
    sha256: str
    meta: Dict[str, str] = field(default_factory=dict)
    role: str = "specimen"          # specimen | account | corpus

    def units(self, unit: str) -> int:
        body = self.text.strip("\n")
        if unit in ("paragraph", "fragment", "speech"):
            return len([p for p in re.split(r"\n\s*\n", body) if p.strip()])
        if unit == "sentence":
            return len([s for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()])
        return len([l for l in body.split("\n") if l.strip()])


def read_text_file(path: Path, label: str) -> str:
    if str(path) == "-":
        data = sys.stdin.buffer.read()
    else:
        if not path.is_file():
            raise CompileError(f"{label} not found: {path}")
        data = path.read_bytes()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise CompileError(f"{label} {path} is not UTF-8 text. The compiler takes text specimens only.") from exc


def split_meta(text: str) -> Tuple[Dict[str, str], str]:
    """Optional header block: `Key: value` lines, then a blank line, then the text.
    Keys are the specimen card fields. Anything else at the top is text."""
    lines = text.split("\n")
    meta: Dict[str, str] = {}
    i = 0
    while i < len(lines):
        m = _META_LINE.match(lines[i].strip())
        if not m:
            break
        meta[m.group(1).lower()] = m.group(2).strip()
        i += 1
    if meta and i < len(lines) and lines[i].strip() == "":
        return meta, "\n".join(lines[i + 1:])
    return {}, text


def load_specimen(path: Path, role: str, overrides: Dict[str, str]) -> Specimen:
    raw = read_text_file(path, role)
    meta, body = split_meta(raw)
    for k, v in overrides.items():
        if v:
            meta[k] = v
    return Specimen(path=str(path), text=body, sha256=sha256(raw.encode("utf-8")), meta=meta, role=role)


def specimen_card(sp: Specimen, req: Request, index: int, total: int, prefix: str = "") -> str:
    m = sp.meta
    title = m.get("title") or Path(sp.path).stem
    kind = m.get("kind", req.kind)
    unit = m.get("unit", req.unit or "line")
    rows: List[Tuple[str, str]] = []
    if req.task == "workshop":
        # Defaults follow the workshop card: a poem with no author named is the user's
        # own draft; found text with no author named is a third party's, status unknown.
        if kind == "poem":
            author = m.get("author", "the user")
            provenance = m.get("provenance", "the user's own draft" if author == "the user" else "unknown")
        else:
            author = m.get("author", "unknown")
            provenance = m.get("provenance", "found")
        copyright_ = m.get("copyright", "the user's" if provenance == "the user's own draft" else "unknown")
        rows += [("Author", author), ("Provenance", provenance), ("Copyright", copyright_),
                 ("Kind", kind), ("Unit", unit)]
        if kind != "poem":
            rows.append(("Found by", m.get("found by", "the user")))
        rows.append(("Length", f"{sp.units(unit)} {unit}s"))
    else:
        rows += [("Title", title)]
        if m.get("author"):
            rows.append(("Author", m["author"]))
        if m.get("date"):
            rows.append(("Date", m["date"]))
        if m.get("edition"):
            rows.append(("Edition or source", m["edition"]))
        if m.get("copyright"):
            rows.append(("Source status", m["copyright"]))
        rows += [("Kind", kind), ("Unit", unit), ("Length", f"{sp.units(unit)} {unit}s")]
    width = max(len(k) for k, _ in rows) + 1
    card = "\n".join(f"{(k + ':').ljust(width)} {v}" for k, v in rows)
    label = "SPECIMEN" if total == 1 else f"SPECIMEN {index} OF {total}"
    return section(f"{prefix}{label}: {title} (sha256 {sp.sha256[:16]})",
                   fence(card, "text") + "\n" + fence(sp.text, "text"))


# ---- prompt -------------------------------------------------------------------

def _load_table(plan: LoadPlan) -> str:
    lines = [f"{'step':4s} {'file':50s} {'version':8s} {'sha256':16s}"]
    for f in plan.files:
        step = "-" if f.load_step is None else str(f.load_step)
        lines.append(f"{step:4s} {f.name:50s} {f.version or '?':8s} {f.sha256[:16]}")
    return "\n".join(lines)


def header(plan: LoadPlan, reg: Registry, specimens: List[Specimen]) -> str:
    task = reg.tasks[plan.request.task]
    out = "# DIAGNOSTIC READER: COMPILED PROMPT\n\n"
    out += f"Generator: dr {__version__}\nTask: {task.label}\n"
    if plan.request.voices:
        out += f"Voices: {', '.join(plan.request.voices)}\n"
    out += f"Full Monty State: {plan.full_monty_state}"
    out += f" ({', '.join(plan.plugins)})\n" if plan.plugins else "\n"
    out += (
        "\nThe compiler performed the load step. The framework files below are the complete "
        "file set for this request, in the boot's load order; treat each as loaded from the "
        "point it appears. Resolve every cross-reference against this set, not against memory "
        "of other releases. Where a procedure needs a file that is not in the set, say so and "
        "switch that procedure off rather than rebuild the file's contents. The specimen and "
        "the operator request follow the framework files.\n"
    )
    out += section("LOAD SET", fence(_load_table(plan), "text"))
    if plan.withheld:
        out += section("WITHHELD FILES",
                       "These files are intentionally absent from this run. Procedures that depend on "
                       "them switch off; record the gap and do not reconstruct them:\n"
                       + "\n".join(f"- `{s}`" for s in plan.withheld))
    if plan.excluded:
        out += section("EXCLUDED FILES", "Removed by the operator:\n" + "\n".join(f"- `{s}`" for s in plan.excluded))
    return out


def framework_sections(plan: LoadPlan, snap: Snapshot) -> List[Tuple[str, str]]:
    """(stem, section text) per planned file."""
    out = []
    for f in plan.files:
        text = snap.require(f.stem).read_text()
        title = f"FRAMEWORK FILE {f.load_step if f.load_step is not None else '-'}: {f.name}"
        if f.designation:
            title += f" ({f.designation})"
        out.append((f.stem, section(title, fence(text, "markdown"))))
    return out


def tail(plan: LoadPlan, req: Request, specimens: List[Specimen]) -> str:
    out = ""
    main = [s for s in specimens if s.role == "specimen"]
    for i, sp in enumerate(main, 1):
        out += specimen_card(sp, req, i, len(main))
    for sp in (s for s in specimens if s.role == "account"):
        out += section(f"ACCOUNT: the poet's account of the specimen, held at P2 (sha256 {sp.sha256[:16]})",
                       fence(sp.text, "text"))
    corpus = [s for s in specimens if s.role == "corpus"]
    for i, sp in enumerate(corpus, 1):
        title = sp.meta.get("title") or Path(sp.path).name
        out += section(f"SUPPLIED CORPUS {i} OF {len(corpus)}: {title} (sha256 {sp.sha256[:16]})",
                       fence(sp.text, "text"))
    out += section("LOAD SET, REPEATED",
                   "The complete file set for this prompt, as at the top. A file the apparatus names that is "
                   "not in this table is absent from this run.\n\n" + fence(_load_table(plan), "text")
                   + ("\nWithheld from this run: " + ", ".join(f"`{w}`" for w in plan.withheld) + "\n"
                      if plan.withheld else ""))
    out += section("OPERATOR REQUEST", plan.request_line)
    return out


# ---- assembly and output ------------------------------------------------------

@dataclass
class Build:
    parts: List[Tuple[str, str]]        # (file name, content)
    manifest: dict


def build(plan: LoadPlan, reg: Registry, snap: Snapshot, specimens: List[Specimen],
          part_size: Optional[int] = None) -> Build:
    if not plan.ok:
        raise CompileError("plan has errors; run with --explain to see them")
    if plan.request.task not in ("scan",) and not any(s.role == "specimen" for s in specimens):
        raise CompileError("no specimen: pass --specimen FILE (text only; '-' reads stdin)")
    if plan.request.task == "scan" and plan.request.scan_source == "supplied" \
            and not any(s.role == "corpus" for s in specimens):
        raise CompileError("scan supplied needs --corpus FILE")

    head = header(plan, reg, specimens)
    files = framework_sections(plan, snap)
    end = tail(plan, plan.request, specimens)

    blocks: List[Tuple[str, str]] = [("header", head)] + files + [("tail", end)]
    if part_size is None:
        parts = [("prompt.md", "".join(b for _, b in blocks))]
    else:
        parts = _split(blocks, part_size)

    manifest = {
        "generator": "dr",
        "generator_version": __version__,
        "request": _request_dict(plan.request),
        "request_line": plan.request_line,
        "task": reg.tasks[plan.request.task].label,
        "snapshot": str(snap.source),
        "snapshot_sha256": sha256(snap.source.read_bytes()) if snap.is_zip else None,
        "files": [{"step": f.load_step, "stem": f.stem, "name": f.name, "version": f.version,
                   "size": f.size, "sha256": f.sha256, "reasons": f.reasons} for f in plan.files],
        "withheld": plan.withheld,
        "excluded": plan.excluded,
        "full_monty_state": plan.full_monty_state,
        "plugins": plan.plugins,
        "specimens": [{"role": s.role, "path": s.path, "sha256": s.sha256, "meta": s.meta} for s in specimens],
        "framework_bytes": plan.total_bytes,
        "prompt_chars": sum(len(c) for _, c in parts),
        "token_estimate": int(sum(len(c) for _, c in parts) / plan.chars_per_token),
        "chars_per_token": plan.chars_per_token,
        "max_tokens": plan.max_tokens,
        "parts": [{"name": n, "chars": len(c), "sha256": sha256(c.encode("utf-8"))} for n, c in parts],
        "warnings": plan.warnings,
    }
    return Build(parts=parts, manifest=manifest)


def _split(blocks: List[Tuple[str, str]], part_size: int) -> List[Tuple[str, str]]:
    groups: List[List[str]] = [[]]
    sizes = [0]
    for _, text in blocks:
        if sizes[-1] and sizes[-1] + len(text) > part_size:
            groups.append([])
            sizes.append(0)
        groups[-1].append(text)
        sizes[-1] += len(text)
    n = len(groups)
    parts = []
    for i, g in enumerate(groups, 1):
        note = (f"<!-- dr: part {i} of {n}. Paste every part into one context, in order, before "
                f"the model answers. -->\n\n")
        parts.append((f"prompt-part{i}of{n}.md", note + "".join(g)))
    return parts


def _request_dict(req: Request) -> dict:
    from dataclasses import asdict
    d = asdict(req)
    for k in ("specimens", "corpus"):
        if k in d:
            d[k] = [str(p) for p in d[k]]
    if d.get("account_path") is not None:
        d["account_path"] = str(d["account_path"])
    return d


def write(build_: Build, out_dir: Path) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for name, content in build_.parts:
        p = out_dir / name
        p.write_text(content, encoding="utf-8", newline="\n")
        written.append(p)
    mp = out_dir / "build-manifest.json"
    mp.write_text(json.dumps(build_.manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                  encoding="utf-8")
    written.append(mp)
    return written
