"""Load framework-registry.json, the machine mirror of the boot's registry.

The JSON file is data the operator edits. This module only gives it types and
a few lookups. Nothing here reads the framework files; see snapshot.py.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REGISTRY_PATH = Path(__file__).resolve().parent / "framework-registry.json"

_VERSION_RE = re.compile(r"^\d+(?:\.\d+)*$")


class RegistryError(ValueError):
    pass


def parse_version(text: str) -> Tuple[int, ...]:
    """'0.3.16' -> (0, 3, 16). Trailing punctuation is tolerated; anything else fails."""
    text = text.strip().lstrip("vV").rstrip(".")
    if not _VERSION_RE.match(text):
        raise RegistryError(f"not a version: {text!r}")
    return tuple(int(p) for p in text.split("."))


def version_ge(have: str, floor: str) -> bool:
    """True when `have` satisfies a floor. Floors compare by the digits they state:
    0.3 is satisfied by 0.3.1 and 0.3.19, per the kernel's File Reference Rule."""
    h, f = parse_version(have), parse_version(floor)
    h = h + (0,) * (len(f) - len(h))
    return h[: len(f)] >= f


@dataclass
class Module:
    stem: str
    type: str
    load_step: Optional[int]
    loadable: bool = True
    designation: Optional[str] = None
    handle: Optional[str] = None
    requires: List[str] = field(default_factory=list)
    floors: Dict[str, str] = field(default_factory=dict)
    role: str = ""
    note: str = ""
    boot_alias: Optional[str] = None
    collides_with: List[str] = field(default_factory=list)
    optional_on_disk: bool = False


@dataclass
class Task:
    name: str
    label: str
    modules: List[str]
    default_voices: List[str] = field(default_factory=list)
    min_voices: int = 0


@dataclass
class Registry:
    raw: dict
    modules: Dict[str, Module]
    voices: Dict[str, dict]
    modes: Dict[str, dict]
    features: Dict[str, dict]
    tasks: Dict[str, Task]
    kinds: List[str]
    units: List[str]
    kind_default_unit: Dict[str, str]
    non_runtime_files: List[str]
    non_runtime_dirs: List[str]
    calibration_authors: Dict[str, dict]
    path: Path

    # ---- lookups -------------------------------------------------------

    def voice_module(self, designation: str) -> str:
        d = designation.upper()
        if d not in self.voices:
            raise RegistryError(f"unknown voice {designation!r}; voices are {', '.join(self.voices)}")
        return self.voices[d]["module"]

    def designation_of(self, stem: str) -> Optional[str]:
        m = self.modules.get(stem)
        return m.designation if m else None

    def plugin_stem(self, name: str) -> str:
        """Accept a plugin handle ('Snow Crust'), a stem, or the boot's alias."""
        key = name.strip().lower()
        for m in self.modules.values():
            if m.type != "plugin":
                continue
            if key in {m.stem.lower(), (m.handle or "").lower(), (m.boot_alias or "").lower()}:
                return m.stem
        plugins = ", ".join(f"{m.handle} ({m.stem})" for m in self.modules.values() if m.type == "plugin")
        raise RegistryError(f"unknown plugin {name!r}; plugins are {plugins}")

    def resolve_stem(self, name: str) -> str:
        """Accept a stem or an identifier shorthand such as '7', '7a', '3-kowit', '0c'."""
        key = name.strip().lower()
        if key in self.modules:
            return key
        for stem in self.modules:
            if stem.lower().startswith(key + "-") or stem.lower() == key:
                return stem
        # bare identifier like "7" must match the leading token exactly
        for stem in self.modules:
            lead = stem.split("-", 1)[0].lower()
            if lead == key:
                return stem
        raise RegistryError(f"unknown module {name!r}")

    def plugins(self) -> List[Module]:
        return [m for m in self.modules.values() if m.type == "plugin"]

    def in_load_order(self, stems: List[str]) -> List[str]:
        order = {stem: i for i, stem in enumerate(self.modules)}
        return sorted(
            stems,
            key=lambda s: (
                self.modules[s].load_step if self.modules[s].load_step is not None else 99,
                order.get(s, 999),
            ),
        )


def load_registry(path: Optional[Path] = None) -> Registry:
    path = Path(path) if path else REGISTRY_PATH
    raw = json.loads(path.read_text(encoding="utf-8"))
    modules: Dict[str, Module] = {}
    for stem, spec in raw["modules"].items():
        modules[stem] = Module(
            stem=stem,
            type=spec["type"],
            load_step=spec.get("load_step"),
            loadable=spec.get("loadable", True),
            designation=spec.get("designation"),
            handle=spec.get("handle"),
            requires=list(spec.get("requires", [])),
            floors=dict(spec.get("floors", {})),
            role=spec.get("role", ""),
            note=spec.get("note", ""),
            boot_alias=spec.get("boot_alias"),
            collides_with=list(spec.get("collides_with", [])),
            optional_on_disk=spec.get("optional_on_disk", False),
        )
    tasks = {
        name: Task(
            name=name,
            label=spec["label"],
            modules=list(spec["modules"]),
            default_voices=list(spec.get("default_voices", [])),
            min_voices=int(spec.get("min_voices", 0)),
        )
        for name, spec in raw["tasks"].items()
    }
    reg = Registry(
        raw=raw,
        modules=modules,
        voices=raw["voices"],
        modes=raw["modes"],
        features=raw["features"],
        tasks=tasks,
        kinds=list(raw["kinds"]),
        units=list(raw["units"]),
        kind_default_unit=dict(raw["kind_default_unit"]),
        non_runtime_files=list(raw.get("non_runtime_files", [])),
        non_runtime_dirs=list(raw.get("non_runtime_dirs", [])),
        calibration_authors=dict(raw.get("calibration_authors", {})),
        path=path,
    )
    _check_internal_consistency(reg)
    return reg


def _check_internal_consistency(reg: Registry) -> None:
    """Every stem the JSON refers to must be a module the JSON declares."""
    problems: List[str] = []
    for m in reg.modules.values():
        for dep in m.requires:
            if dep not in reg.modules:
                problems.append(f"{m.stem} requires unknown module {dep}")
        for dep in m.floors:
            if dep not in reg.modules:
                problems.append(f"{m.stem} has a floor on unknown module {dep}")
    for name, v in reg.voices.items():
        if v["module"] not in reg.modules:
            problems.append(f"voice {name} maps to unknown module {v['module']}")
        elif reg.modules[v["module"]].designation != name:
            problems.append(f"voice {name} maps to {v['module']} whose designation is {reg.modules[v['module']].designation}")
    for name, v in reg.modes.items():
        if v["module"] not in reg.modules:
            problems.append(f"mode {name} maps to unknown module {v['module']}")
    for name, f in reg.features.items():
        for stem in f["modules"]:
            if stem not in reg.modules:
                problems.append(f"feature {name} names unknown module {stem}")
    for t in reg.tasks.values():
        for stem in t.modules:
            if stem not in reg.modules:
                problems.append(f"task {t.name} names unknown module {stem}")
        for v in t.default_voices:
            if v not in reg.voices:
                problems.append(f"task {t.name} names unknown voice {v}")
    for kind in reg.kind_default_unit:
        if kind not in reg.kinds:
            problems.append(f"kind_default_unit names unknown kind {kind}")
    if problems:
        raise RegistryError("framework-registry.json is inconsistent:\n  " + "\n  ".join(problems))
