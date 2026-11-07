"""Turn a Request into a load plan.

Steps, in order: task minimal set, requested voices, modes, features and
plugins; include and exclude overrides; withhold as fault injection; closure
over hard dependencies; version floors against the snapshot; boot load order;
size and token estimate against a budget. Every file in the plan carries the
reason it is there.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

from .registry import Registry, RegistryError, version_ge
from .request import Request, collision_warnings
from .snapshot import Snapshot

DEFAULT_CHARS_PER_TOKEN = 4.0
BOOT_STEM = "0-poetics-boot-hollow"


class ResolveError(ValueError):
    pass


@dataclass
class PlannedFile:
    stem: str
    name: str
    version: Optional[str]
    size: int
    sha256: str
    load_step: Optional[int]
    type: str
    designation: Optional[str]
    reasons: List[str]


@dataclass
class LoadPlan:
    request: Request
    request_line: str
    files: List[PlannedFile]
    withheld: List[str]                 # stems removed as fault injection
    excluded: List[str]                 # stems removed by --exclude
    missing: List[str]                  # stems wanted but absent from the snapshot
    full_monty_state: str               # absent | present | multi
    plugins: List[str]
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    chars_per_token: float = DEFAULT_CHARS_PER_TOKEN
    max_tokens: Optional[int] = None

    @property
    def total_bytes(self) -> int:
        return sum(f.size for f in self.files)

    @property
    def token_estimate(self) -> int:
        return int(self.total_bytes / self.chars_per_token)

    @property
    def over_budget(self) -> bool:
        return self.max_tokens is not None and self.token_estimate > self.max_tokens

    @property
    def ok(self) -> bool:
        return not self.errors and not self.over_budget

    def stems(self) -> List[str]:
        return [f.stem for f in self.files]


def resolve(req: Request, reg: Registry, snap: Snapshot, request_line: str,
            max_tokens: Optional[int] = None,
            chars_per_token: float = DEFAULT_CHARS_PER_TOKEN) -> LoadPlan:
    reasons: Dict[str, List[str]] = {}
    warnings: List[str] = []
    errors: List[str] = []

    def want(stem: str, why: str) -> None:
        reasons.setdefault(stem, [])
        if why not in reasons[stem]:
            reasons[stem].append(why)

    task = reg.tasks[req.task]
    if not req.no_boot:
        want(BOOT_STEM, "entry point")
    for stem in task.modules:
        want(stem, f"task {task.label}")

    # voices and modes
    for v in req.voices:
        want(reg.voice_module(v), f"voice {v}")
    if req.vise:
        want(reg.modes["VISE"]["module"], f"VISE, {req.spine} spine")
    if req.task == "workshop":
        want(reg.modes["JIG"]["module"], "JIG workshop")

    # features implied by flags
    def feature(name: str, why: str) -> None:
        for stem in reg.features[name]["modules"]:
            want(stem, why)

    if req.found:
        feature("found-text", f"kind {req.kind} is not poem; 8 loads by default")
    if req.hermetic:
        feature("hermetic", "Hermetic chamber reading, Section H")
    if req.battery:
        feature("battery", "Full battery report")
    if req.task == "workshop" and req.wants_dials():
        feature("dial-trials", "dial trial or dial overlay requested")
    for ext in req.extensions:
        key = ext.strip().lower()
        if key in reg.features:
            feature(key, f"--extensions {ext}")
        else:
            try:
                want(reg.resolve_stem(ext), f"--extensions {ext}")
            except RegistryError as exc:
                errors.append(str(exc))

    # plugins: private and opt-in
    plugin_stems: List[str] = []
    for p in req.plugins:
        try:
            stem = reg.plugin_stem(p)
        except RegistryError as exc:
            errors.append(str(exc))
            continue
        plugin_stems.append(stem)
        want(stem, f"--plugins {p}")
    for stem in plugin_stems:
        m = reg.modules[stem]
        hits = [d for d in m.collides_with if d in req.voices or (d == "JIG" and req.task == "workshop")]
        if hits:
            warnings.append(f"plugin {m.handle} is a calibration collision for {', '.join(hits)}; "
                            "expect a jurisdiction stand-down on its specimen")

    warnings.extend(collision_warnings(req, reg))

    # includes
    for inc in req.include:
        try:
            want(reg.resolve_stem(inc), f"--include {inc}")
        except RegistryError as exc:
            errors.append(str(exc))

    # closure over hard dependencies
    changed = True
    while changed:
        changed = False
        for stem in list(reasons):
            for dep in reg.modules[stem].requires:
                if dep not in reasons:
                    want(dep, f"required by {stem}")
                    changed = True

    # withhold (fault injection) and exclude
    withheld: List[str] = []
    for w in req.withhold:
        try:
            stem = reg.resolve_stem(w)
        except RegistryError as exc:
            errors.append(str(exc))
            continue
        if stem in reasons:
            reasons.pop(stem)
        withheld.append(stem)
    excluded: List[str] = []
    for x in req.exclude:
        try:
            stem = reg.resolve_stem(x)
        except RegistryError as exc:
            errors.append(str(exc))
            continue
        if stem in reasons:
            reasons.pop(stem)
            excluded.append(stem)
    for stem in withheld + excluded:
        dependents = [s for s in reasons if stem in reg.modules[s].requires]
        if dependents:
            kind = "withheld" if stem in withheld else "excluded"
            warnings.append(f"{stem} is {kind} but {', '.join(dependents)} depend on it; "
                            "the apparatus should switch those off rather than rebuild the file")
    if "0c-voice-designations" in withheld + excluded and any(
            reg.modules[s].type == "voice" for s in reasons):
        warnings.append("0c-voice-designations is absent with voice modules loaded; "
                        "the boot warns every voice will label output with its source's name")

    # non-loadable files
    for stem in list(reasons):
        if not reg.modules[stem].loadable:
            errors.append(f"{stem} is never loaded (apparatus note); drop it from the request")

    # resolve against the snapshot
    files: List[PlannedFile] = []
    missing: List[str] = []
    for stem in reg.in_load_order(list(reasons)):
        ff = snap.get(stem)
        if ff is None:
            missing.append(stem)
            continue
        m = reg.modules[stem]
        files.append(PlannedFile(stem=stem, name=ff.name, version=ff.version, size=ff.size,
                                 sha256=ff.sha256, load_step=m.load_step, type=m.type,
                                 designation=m.designation, reasons=reasons[stem]))
    for stem in missing:
        errors.append(f"{stem} is needed ({'; '.join(reasons[stem])}) but is not in the snapshot")

    # version floors
    present = {f.stem: f.version for f in files}
    for f in files:
        for dep, floor in reg.modules[f.stem].floors.items():
            have = present.get(dep)
            if have is None:
                continue  # missing dependency already reported, or not loaded
            if not version_ge(have, floor):
                errors.append(f"{f.stem} needs {dep} {floor} or later; snapshot has {have}")

    # duplicate releases
    for f in files:
        if f.stem in snap.duplicates:
            warnings.append(f"{f.stem}: more than one release on disk ({', '.join(snap.duplicates[f.stem])}); "
                            f"using {f.name}")

    plugins_loaded = [s for s in present if reg.modules[s].type == "plugin"]
    state = "absent" if not plugins_loaded else ("present" if len(plugins_loaded) == 1 else "multi")

    plan = LoadPlan(request=req, request_line=request_line, files=files, withheld=withheld,
                    excluded=excluded, missing=missing, full_monty_state=state,
                    plugins=plugins_loaded, warnings=warnings, errors=errors,
                    chars_per_token=chars_per_token, max_tokens=max_tokens)
    if plan.over_budget:
        plan.errors.append(f"estimated {plan.token_estimate:,} tokens exceeds --max-tokens {max_tokens:,}")
    return plan
