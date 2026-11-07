"""Check that the registry JSON, the boot, the files on disk, and the regression
manifests agree. Findings are reported, never repaired.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from .registry import Registry, RegistryError, parse_version
from .snapshot import Snapshot

_BOOT_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([0-9][0-9.]*)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")
_PLUGIN_LINE = re.compile(r"^- (.+?): `([^`]+)`\.")


@dataclass
class Finding:
    level: str      # error | warn | info
    check: str
    message: str

    def __str__(self) -> str:
        return f"{self.level.upper():5s} {self.check}: {self.message}"


def _boot_registry(snap: Snapshot, reg: Registry) -> dict:
    boot = snap.get(reg.raw["mirrors"]["boot_stem"])
    if boot is None:
        return {}
    rows = {}
    for line in boot.read_text().splitlines():
        m = _BOOT_ROW.match(line)
        if m:
            rows[m.group(1)] = {"version": m.group(2), "type": m.group(3), "designation": m.group(4)}
    return rows


def _boot_plugins(snap: Snapshot, reg: Registry) -> dict:
    boot = snap.get(reg.raw["mirrors"]["boot_stem"])
    if boot is None:
        return {}
    out = {}
    in_section = False
    for line in boot.read_text().splitlines():
        if line.startswith("## Plugin Registry"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            m = _PLUGIN_LINE.match(line)
            if m:
                out[m.group(1)] = m.group(2)
    return out


def lint(reg: Registry, snap: Snapshot, regression_dir: Optional[Path] = None) -> List[Finding]:
    f: List[Finding] = []

    # 1. every registered module resolves to a file, or is marked optional
    for m in reg.modules.values():
        if snap.get(m.stem) is None:
            level = "info" if m.optional_on_disk else ("warn" if not m.loadable else "error")
            f.append(Finding(level, "disk", f"{m.stem} is in framework-registry.json but not on disk"))

    # 2. files on disk the registry does not know
    for stem, ff in snap.files.items():
        if stem not in reg.modules:
            f.append(Finding("warn", "registry", f"{ff.name} is on disk but not in framework-registry.json"))
    for stem, names in snap.duplicates.items():
        f.append(Finding("warn", "disk", f"{stem} has more than one release on disk: {', '.join(names)}"))

    # 3. header version vs filename version
    for ff in snap.files.values():
        if ff.header_version and ff.filename_version and ff.header_version != ff.filename_version:
            f.append(Finding("error", "version", f"{ff.name}: header says {ff.header_version}, file name says {ff.filename_version}"))
        elif not ff.header_version and not ff.filename_version:
            f.append(Finding("info", "version", f"{ff.name}: no version line and no version in the file name"))
        elif not ff.header_version:
            f.append(Finding("info", "version", f"{ff.name}: no version line; using the file name's {ff.filename_version}"))

    # 4. boot Module Registry vs disk
    boot_rows = _boot_registry(snap, reg)
    if not boot_rows:
        f.append(Finding("error", "boot", "could not read the boot's Module Registry table"))
    for stem, row in boot_rows.items():
        ff = snap.get(stem)
        if ff is None:
            f.append(Finding("error", "boot", f"boot registers {stem} {row['version']} but it is not on disk"))
            continue
        if ff.version and ff.version != row["version"]:
            f.append(Finding("error", "boot", f"boot registers {stem} at {row['version']}; disk has {ff.version}"))
        m = reg.modules.get(stem)
        if m and m.designation and row["designation"] != m.designation:
            f.append(Finding("error", "boot", f"boot gives {stem} designation {row['designation']}; registry JSON says {m.designation}"))
        if m is None:
            f.append(Finding("warn", "boot", f"boot registers {stem} but framework-registry.json does not"))
    for m in reg.modules.values():
        if m.loadable and m.type not in ("boot", "plugin") and m.stem not in boot_rows and snap.get(m.stem):
            f.append(Finding("warn", "boot", f"{m.stem} is on disk and loadable but the boot's Module Registry does not list it (known Registry Gap)"))

    # 5. boot Plugin Registry vs disk
    boot_plugins = _boot_plugins(snap, reg)
    for handle, stem in boot_plugins.items():
        if snap.get(stem) is None:
            alias = next((m.stem for m in reg.plugins() if m.boot_alias == stem), None)
            msg = f"boot's plugin registry gives {handle} as {stem}; "
            msg += f"the file on disk is {snap.get(alias).name}" if alias and snap.get(alias) else "no file on disk matches"
            f.append(Finding("warn", "boot", msg + " (known Registry Gap)"))
    for m in reg.plugins():
        if m.handle not in boot_plugins and snap.get(m.stem):
            f.append(Finding("warn", "boot", f"plugin {m.handle} ({m.stem}) is on disk but not in the boot's Plugin Registry"))

    # 6. mirrors line
    boot_ff = snap.get(reg.raw["mirrors"]["boot_stem"])
    if boot_ff and boot_ff.version != reg.raw["mirrors"]["boot_version"]:
        f.append(Finding("warn", "registry", f"framework-registry.json mirrors boot {reg.raw['mirrors']['boot_version']}; disk has {boot_ff.version}. Review the mirror after the boot's changes"))

    # 7. floors satisfiable with what is on disk
    for m in reg.modules.values():
        for dep, floor in m.floors.items():
            have = snap.version_of(dep)
            if have is None:
                continue
            try:
                ok = parse_version(have)[: len(parse_version(floor))] >= parse_version(floor)
            except RegistryError:
                ok = False
            if not ok:
                f.append(Finding("error", "floor", f"{m.stem} needs {dep} {floor}; disk has {have}"))

    # 8. README tables agree with the disk and the registry
    f.extend(_lint_readme(reg, snap))

    # 9. every regression case loads: request resolves, specimen matches its pin, expectations hold
    if regression_dir and (Path(regression_dir) / "tests").is_dir():
        from .regress import RegressionError, load_case
        for case_dir in sorted((Path(regression_dir) / "tests").iterdir()):
            if not (case_dir / "manifest.json").is_file():
                continue
            try:
                case = load_case(Path(regression_dir), case_dir.name, reg, snap)
            except RegressionError as exc:
                f.append(Finding("error", "regression", str(exc)))
                continue
            for e in case.plan.errors + case.expect_errors:
                f.append(Finding("error", "regression", e))
            for w in case.plan.warnings:
                f.append(Finding("info", "regression", f"{case.id}: {w}"))

    return f


_README_FILE_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([0-9][0-9.]*)\s*\|")
_README_TASK_ROW = re.compile(r"^\|\s*([^|`]+?)\s*\|\s*([^|]*)\|")
_SHORTHAND = re.compile(r"`([0-9][0-9a-z-]*|compartmentalization-engine)`")


def _lint_readme(reg: Registry, snap: Snapshot) -> List[Finding]:
    """The framework README's Files tables and minimal-sets table are prose copies of
    what the disk and framework-registry.json hold. Report where they disagree."""
    out: List[Finding] = []
    readme = snap.source / reg.raw["mirrors"]["readme"] if not snap.is_zip else None
    if readme is None or not readme.is_file():
        return out
    text = readme.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    in_tasks = False
    for line in text.splitlines():
        m = _README_FILE_ROW.match(line)
        if m and m.group(1) in reg.modules:
            ff = snap.get(m.group(1))
            if ff and ff.version and ff.version != m.group(2):
                out.append(Finding("warn", "readme", f"README lists {m.group(1)} at {m.group(2)}; disk has {ff.version}"))
            continue
        if line.startswith("| Task |"):
            in_tasks = True
            continue
        if in_tasks:
            if not line.startswith("|"):
                in_tasks = False
                continue
            m = _README_TASK_ROW.match(line)
            if not m:
                continue
            label = m.group(1).strip()
            task = next((t for t in reg.tasks.values() if t.label.lower() == label.lower()), None)
            if task is None:
                continue
            listed = set()
            for sh in _SHORTHAND.findall(m.group(2)):
                try:
                    listed.add(reg.resolve_stem(sh))
                except RegistryError:
                    out.append(Finding("warn", "readme", f"README task {label!r} names unknown module `{sh}`"))
            registered = {s for s in task.modules if reg.modules[s].type != "boot"}
            if listed != registered:
                out.append(Finding("warn", "readme",
                                   f"README task {label!r} lists {sorted(listed)}; registry task {task.name} has {sorted(registered)}"))
    return out
