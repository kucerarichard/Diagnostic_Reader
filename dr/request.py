"""The operator's request, normalized from CLI flags.

A Request records what was asked. resolve.py turns it into a load plan, and
compile (Phase 2) turns it into a prompt. `render_request_line` writes the
request as the plain-language form the README documents, so the model sees
the same trigger a chat operator would type.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .registry import Registry, RegistryError


@dataclass
class Request:
    task: str                                   # key in registry.tasks
    voices: List[str] = field(default_factory=list)
    verdict: Optional[str] = None               # voice that closes
    counter_voices: List[str] = field(default_factory=list)
    vise: bool = False
    spine: Optional[str] = None                 # voice VISE rides
    kind: str = "poem"
    unit: Optional[str] = None
    hermetic: bool = False
    battery: bool = False
    account: bool = False                       # DATUM: an account is supplied
    extensions: List[str] = field(default_factory=list)   # feature names or stems
    plugins: List[str] = field(default_factory=list)      # plugin handles or stems
    # workshop
    rewrites: Optional[bool] = None             # None = default (two trials)
    rewrite_under: List[str] = field(default_factory=list)
    ars_poetica: bool = False
    dial_trial: Optional[str] = None            # "" means unnamed dial trial
    rewrite_at: List[str] = field(default_factory=list)   # dial:setting
    no_dial_trials: bool = False
    contrast_at: Optional[str] = None
    feedback_bridge: bool = False
    # scan
    scan_source: Optional[str] = None           # canon | supplied
    scan_category: Optional[str] = None
    scan_devices: List[str] = field(default_factory=list)
    scan_or: bool = False
    # specimens (text only)
    specimens: List[str] = field(default_factory=list)
    title: Optional[str] = None
    author: Optional[str] = None
    date: Optional[str] = None
    edition: Optional[str] = None
    provenance: Optional[str] = None
    copyright: Optional[str] = None
    found_by: Optional[str] = None
    account_path: Optional[str] = None          # DATUM: file holding the poet's account
    corpus: List[str] = field(default_factory=list)       # scan supplied
    # overrides
    include: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)
    withhold: List[str] = field(default_factory=list)
    no_boot: bool = False
    ask: Optional[str] = None                   # free-text passthrough

    # ---- derived ---------------------------------------------------------

    @property
    def found(self) -> bool:
        return self.kind != "poem"

    def wants_dials(self) -> bool:
        if self.no_dial_trials:
            return False
        return self.dial_trial is not None or bool(self.rewrite_at)


def normalize(req: Request, reg: Registry) -> Request:
    """Fill defaults and validate names. Raises RegistryError on a bad name."""
    if req.task not in reg.tasks:
        raise RegistryError(f"unknown task {req.task!r}; tasks are {', '.join(reg.tasks)}")
    req.voices = [v.upper() for v in req.voices]
    req.counter_voices = [v.upper() for v in req.counter_voices]
    for v in req.voices + req.counter_voices + [x for x in (req.verdict, req.spine) if x]:
        reg.voice_module(v)
    if req.verdict:
        req.verdict = req.verdict.upper()
    if req.spine:
        req.spine = req.spine.upper()
    if req.kind not in reg.kinds:
        raise RegistryError(f"unknown kind {req.kind!r}; kinds are {', '.join(reg.kinds)}")
    if req.unit is None:
        req.unit = reg.kind_default_unit.get(req.kind, "line")
    if req.unit not in reg.units:
        raise RegistryError(f"unknown unit {req.unit!r}; units are {', '.join(reg.units)}")

    task = reg.tasks[req.task]
    if not req.voices and task.default_voices:
        req.voices = list(task.default_voices)
    if req.task == "triangulate" and len(req.voices) < task.min_voices:
        raise RegistryError(
            "triangulate needs at least two voices; pass --voices, e.g. --voices ASSAY PLUMB "
            f"(voices are {', '.join(reg.voices)})")
    if req.task == "datum" and "DATUM" not in req.voices:
        req.voices.insert(0, "DATUM")
    if req.vise and not req.spine:
        req.spine = req.verdict or (req.voices[0] if req.voices else reg.modes["VISE"]["default_spine"])
    if req.spine and req.spine not in req.voices:
        req.voices.append(req.spine)
    if req.verdict and req.verdict not in req.voices:
        req.voices.append(req.verdict)
    for v in req.counter_voices:
        if v not in req.voices:
            req.voices.append(v)
    if req.scan_source and req.scan_source not in ("canon", "supplied"):
        raise RegistryError("scan source must be canon or supplied")
    if req.task == "scan" and not req.scan_source:
        raise RegistryError("scan needs a source: canon or supplied. The apparatus never substitutes one for the other.")
    if req.task == "scan" and not req.scan_devices:
        raise RegistryError("scan needs at least one device (--devices)")
    if req.account_path:
        req.account = True
    return req


def collision_warnings(req: Request, reg: Registry) -> List[str]:
    """A specimen by a calibration author makes its voice or mode stand down."""
    if not req.author:
        return []
    out = []
    for name, spec in reg.calibration_authors.items():
        if name.lower() in req.author.lower():
            hits = [d for d in spec["stands_down"]
                    if d in req.voices or (d == "JIG" and req.task == "workshop")
                    or (d == "dial-trials" and req.task == "workshop" and req.wants_dials())]
            if hits:
                out.append(f"specimen author {req.author!r} calibrates {', '.join(hits)}; "
                           "expect a jurisdiction stand-down (recorded without stated cause)")
    return out


def render_request_line(req: Request, reg: Registry) -> str:
    """The operator request as plain language the kernel and modules recognize."""
    parts: List[str] = []
    t = req.task
    if t == "quick-read":
        parts.append("Quick read.")
    elif t == "sidecar":
        parts.append("Full sidecar.")
        if len(req.voices) == 1:
            parts.append(f"{req.voices[0]} verdict.")
    elif t == "triangulate":
        if req.voices:
            parts.append(f"Triangulate {_and_list(req.voices)}.")
        else:
            parts.append("Triangulate this.")
    elif t == "datum":
        parts.append("DATUM verdict on the poem and its note." if req.account
                     else "DATUM verdict.")
    elif t == "poetics-scan":
        parts.append("Poetics scan.")
    elif t == "scan":
        cat = f" {req.scan_category}" if req.scan_category else ""
        joiner = " or " if req.scan_or else " and "
        parts.append(f"Scan {req.scan_source}{cat} for {joiner.join(req.scan_devices)}")
    elif t == "workshop":
        parts.append("workshop this specimen" if not req.found else f"jig as {req.kind}")
    elif t == "extract":
        parts.append("extract confinement")

    if req.found and t not in ("workshop", "scan", "extract"):
        parts.append(f"Read as found. Kind: {req.kind}. Unit: {req.unit}.")
    if req.task in ("sidecar", "triangulate") and req.verdict and len(req.voices) > 1:
        parts.append(f"{req.verdict} closes.")
    for v in req.counter_voices:
        parts.append(f"Add {v} as counter-voice.")
    if req.vise:
        parts.append(f"VISE verdict, {req.spine} spine.")
    if req.hermetic:
        parts.append("Run the Hermetic chamber reading.")
    if req.battery:
        parts.append("Full battery report.")

    if t == "workshop":
        if req.rewrites is False:
            parts.append("no rewrites")
        elif req.rewrites:
            parts.append("confinement rewrites")
        for ru in req.rewrite_under:
            parts.append(f"rewrite under {ru}")
        if req.ars_poetica:
            parts.append("+ ars poetica")
        if req.no_dial_trials:
            parts.append("no dial trials")
        elif req.dial_trial is not None:
            parts.append("dial trial" if req.dial_trial == "" else f"dial trial: {req.dial_trial}")
        for ra in req.rewrite_at:
            dial, _, setting = ra.partition(":")
            parts.append(f"rewrite at {dial.strip()}: {setting.strip()}" if setting else f"rewrite at {dial.strip()}")
        if req.contrast_at:
            parts.append(f"contrast at: {req.contrast_at}")
        if req.feedback_bridge:
            parts.append("feedback bridge")
    if req.ask:
        parts.append(req.ask.strip())
    # Reading requests read as sentences; workshop and scan commands are one per line,
    # the way the README lists them.
    joiner = "\n" if t in ("workshop", "scan", "extract") else " "
    return joiner.join(parts)


def _and_list(items: List[str]) -> str:
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]
