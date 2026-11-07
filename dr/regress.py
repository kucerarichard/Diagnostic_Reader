"""Compile regression cases into reader, evaluator, and adjudicator prompts.

A case directory under regression/tests/<R-ID>/ holds manifest.json,
target-prompt.md, evaluator-prompt.md, adjudicator-prompt.md, and usually
specimen.txt. The manifest's `request` block is the same request the CLI
takes (task, voices, extensions, withhold, ...); the resolver computes the
load set from it. `withhold` is the fault-injection hook. `expect` pins
which stems must and must not end up in the plan, so a test that depends
on a file being present or absent fails at compile time instead of in a
model run.

The reader prompt per case is the target instructions, a reader-facing
manifest, and the compiled prompt (load set, framework files, specimen,
request line). The evaluator and adjudicator prompts carry the control
documents, the full manifest, the same framework files and specimen, and
a slot for the reader output (and evaluator report). No model is called.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Dict, List, Optional

from . import __version__
from .compile import (CompileError, Specimen, fence, load_specimen, section, sha256,
                      specimen_card)
from .registry import Registry, RegistryError
from .request import Request, normalize, render_request_line
from .resolve import LoadPlan, resolve
from .snapshot import Snapshot

CASE_RE = re.compile(r"^R\d+(?:-[A-Z])?$")
ROLES = ("reader", "evaluator", "adjudicator")
READER_MANIFEST_KEYS = (
    "schema_version", "test_id", "title", "condition", "canonical_work", "corpus_id",
    "test_card", "primary_question", "request", "task_specific_load_rule", "specimen", "account",
)
_REQUEST_FIELDS = {f.name for f in fields(Request)}


class RegressionError(ValueError):
    pass


@dataclass
class Case:
    id: str
    dir: Path
    manifest: dict
    request: Request
    request_line: str
    plan: LoadPlan
    specimen: Optional[Specimen]
    account: Optional[Specimen]          # DATUM: the poet's account, pinned like the specimen
    target_prompt: str
    evaluator_prompt: str
    adjudicator_prompt: str
    expect_errors: List[str]

    @property
    def ok(self) -> bool:
        return self.plan.ok and not self.expect_errors


# ---- loading ------------------------------------------------------------------

def _read(path: Path, label: str) -> str:
    if not path.is_file():
        raise RegressionError(f"{label} missing: {path}")
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").rstrip() + "\n"


def find_control(reg_dir: Path, stem: str) -> Path:
    """Resolve a control document by unversioned stem, e.g. regression-suite -> regression-suite-v0_5.md."""
    hits = sorted(reg_dir.glob(f"{stem}*.md"))
    if not hits:
        raise RegressionError(f"no {stem}*.md in {reg_dir}")
    return hits[-1]


def request_from_manifest(manifest: dict, case_id: str) -> Request:
    spec = manifest.get("request")
    if not isinstance(spec, dict) or "task" not in spec:
        raise RegressionError(f"{case_id}: manifest needs a request block with a task "
                              "(schema_version 2.0; run the v1 manifests through the migration note in regression/README.md)")
    unknown = set(spec) - _REQUEST_FIELDS
    if unknown:
        raise RegressionError(f"{case_id}: unknown request fields {sorted(unknown)}")
    return Request(**spec)


def load_case(reg_dir: Path, case_id: str, reg: Registry, snap: Snapshot,
              max_tokens: Optional[int] = None) -> Case:
    case_dir = reg_dir / "tests" / case_id
    if not case_dir.is_dir():
        raise RegressionError(f"no such case: {case_dir}")
    manifest = json.loads(_read(case_dir / "manifest.json", f"{case_id} manifest"))
    if manifest.get("test_id") != case_id:
        raise RegressionError(f"{case_id}: manifest test_id is {manifest.get('test_id')!r}")

    try:
        req = normalize(request_from_manifest(manifest, case_id), reg)
    except (RegistryError, TypeError) as exc:
        raise RegressionError(f"{case_id}: {exc}") from exc
    line = render_request_line(req, reg)
    plan = resolve(req, reg, snap, line, max_tokens=max_tokens)

    # specimen: text only; scan canon supplies none by design
    specimen: Optional[Specimen] = None
    sp_meta = manifest.get("specimen") or {}
    if sp_meta.get("path"):
        status = str(sp_meta.get("status", "")).upper()
        if "BLOCKED" in status or "REQUIRED" in status:
            raise RegressionError(f"{case_id}: specimen is not ready: {sp_meta.get('status')}")
        try:
            specimen = load_specimen(case_dir / sp_meta["path"], "specimen", {
                "title": sp_meta.get("work_title"), "author": sp_meta.get("author_attribution"),
                "edition": sp_meta.get("edition_or_source"), "copyright": sp_meta.get("source_status"),
            })
        except CompileError as exc:
            raise RegressionError(f"{case_id}: {exc}") from exc
        pinned = sp_meta.get("sha256")
        if pinned and pinned != specimen.sha256:
            raise RegressionError(f"{case_id}: specimen sha256 {specimen.sha256[:16]} does not match "
                                  f"the pinned {pinned[:16]}; the transcription is frozen")
    elif req.task != "scan":
        raise RegressionError(f"{case_id}: manifest has no specimen.path and the task is not scan")

    # account: a second text the DATUM reading measures the specimen against
    account: Optional[Specimen] = None
    ac_meta = manifest.get("account") or {}
    if ac_meta.get("path"):
        try:
            account = load_specimen(case_dir / ac_meta["path"], "account",
                                    {"title": ac_meta.get("title"), "author": ac_meta.get("author")})
        except CompileError as exc:
            raise RegressionError(f"{case_id}: account: {exc}") from exc
        pinned = ac_meta.get("sha256")
        if pinned and pinned != account.sha256:
            raise RegressionError(f"{case_id}: account sha256 {account.sha256[:16]} does not match "
                                  f"the pinned {pinned[:16]}; the transcription is frozen")
        if not req.account:
            req.account = True
            line = render_request_line(req, reg)
            plan = resolve(req, reg, snap, line, max_tokens=max_tokens)
    elif req.task == "datum" or req.account:
        raise RegressionError(f"{case_id}: a DATUM reading needs account.path in the manifest")

    # expectations
    expect = manifest.get("expect") or {}
    errors: List[str] = []
    loaded = set(plan.stems())
    for stem in expect.get("loaded", []):
        if stem not in loaded:
            errors.append(f"{case_id}: expected {stem} loaded; plan has {sorted(loaded)}")
    for stem in expect.get("absent", []):
        if stem in loaded:
            errors.append(f"{case_id}: expected {stem} absent; it is in the plan")
    for stem in req.withhold:
        if stem not in plan.withheld:
            errors.append(f"{case_id}: withhold {stem} did not resolve")

    adj = _read(case_dir / "adjudicator-prompt.md", f"{case_id} adjudicator prompt")
    return Case(
        id=case_id, dir=case_dir, manifest=manifest, request=req, request_line=line, plan=plan,
        specimen=specimen,
        account=account,
        target_prompt=_read(case_dir / "target-prompt.md", f"{case_id} target prompt"),
        evaluator_prompt=_read(case_dir / "evaluator-prompt.md", f"{case_id} evaluator prompt"),
        adjudicator_prompt=adj,
        expect_errors=errors,
    )


# ---- prompt assembly ----------------------------------------------------------

def reader_manifest(manifest: dict) -> dict:
    """Operational facts only; no scoring, evaluator, or adjudicator material."""
    return {k: manifest[k] for k in READER_MANIFEST_KEYS if k in manifest}


def _load_table(plan: LoadPlan) -> str:
    lines = [f"{'step':4s} {'file':50s} {'version':8s} {'sha256':16s}"]
    for f in plan.files:
        step = "-" if f.load_step is None else str(f.load_step)
        lines.append(f"{step:4s} {f.name:50s} {f.version or '?':8s} {f.sha256[:16]}")
    return "\n".join(lines)


def condition_sections(case: Case, snap: Snapshot) -> str:
    """Load set, withheld list, framework files, specimen, request line. Shared by all three roles."""
    c, plan = case.id, case.plan
    out = section(f"{c}: LOAD SET", fence(_load_table(plan), "text"))
    if plan.withheld:
        out += section(f"{c}: WITHHELD FILES",
                       "Intentionally absent from this condition. Procedures that depend on them switch "
                       "off; the gap is recorded and nothing is reconstructed:\n"
                       + "\n".join(f"- `{s}`" for s in plan.withheld))
    for f in plan.files:
        title = f"{c}: FRAMEWORK FILE {f.load_step if f.load_step is not None else '-'}: {f.name}"
        if f.designation:
            title += f" ({f.designation})"
        out += section(title, fence(snap.require(f.stem).read_text(), "markdown"))
    if case.specimen is not None:
        out += specimen_card(case.specimen, case.request, 1, 1, prefix=f"{c}: ")
    else:
        out += section(f"{c}: SPECIMEN", "No specimen text is supplied for this condition. "
                       "A canon scan names its own specimen from the model's knowledge, under Scan Mode's rules.")
    if case.account is not None:
        title = case.account.meta.get("title", "the poet's account")
        out += section(f"{c}: ACCOUNT: {title}, the poet's account of the specimen, held at P2 "
                       f"(sha256 {case.account.sha256[:16]})",
                       "The account is a claim about the specimen and not evidence about it; the record "
                       "is the specimen's own text and whatever the account itself documents.\n\n"
                       + fence(case.account.text, "text"))
    out += section(f"{c}: LOAD SET, REPEATED",
                   f"The complete file set for {c}, as at the top of the case. A file the apparatus names "
                   "that is not in this table is absent from this condition; the loading report names it as "
                   "absent, not as used.\n\n" + fence(_load_table(plan), "text")
                   + ("\nWithheld from this condition: " + ", ".join(f"`{w}`" for w in plan.withheld) + "\n"
                      if plan.withheld else ""))
    out += section(f"{c}: OPERATOR REQUEST", case.request_line)
    return out


def build_prompts(cases: List[Case], snap: Snapshot, suite: str, regime: str,
                  evaluator_master: str, adjudicator_master: str,
                  reader_output: Optional[str], evaluator_output: Optional[str],
                  models: Dict[str, str]) -> Dict[str, str]:
    ids = ", ".join(c.id for c in cases)
    multi = len(cases) > 1
    isolation = (
        "This prompt holds more than one case. Each case's own LOAD SET is its complete file set; a file "
        "that appears under another case is not available to this one, however visible it is in context. "
        if multi else "")

    reader = (
        "# DIAGNOSTIC READER: REGRESSION READER PROMPT\n\n"
        f"Generator: dr {__version__}\nSelected cases: {ids}\nReader model: {models['reader']}\n\n"
        "You are the Reader, the test subject. For each case, the compiler has performed the load step: the "
        "framework files under that case's LOAD SET are the complete file set for that condition, in the "
        "boot's load order. Treat each as loaded from the point it appears, resolve cross-references against "
        "that set and not against memory of other releases, and where a procedure needs a file that is not "
        f"in the set, say so and switch the procedure off rather than rebuild it. {isolation}"
        "Do not consult evaluator or adjudicator materials. Do not grade yourself. Label each case's output "
        "with its test ID and keep the outputs separate.\n"
    )
    evaluator = (
        "# INDEPENDENT EVALUATOR: REGRESSION EVALUATOR PROMPT\n\n"
        f"Generator: dr {__version__}\nSelected cases: {ids}\nEvaluator model: {models['evaluator']}\n\n"
        "You are the independent evaluator, not the Reader and not the adjudicator. Evaluate each case "
        "separately against the control documents and the exact condition shown under its LOAD SET. Do not "
        "treat the Reader's self-audit as independent evidence. Distinguish Pass, Partial, Fail, and N/D "
        "exactly as the suite defines. Cite the supplied source text.\n"
    ) + section("SHARED EVALUATOR INSTRUCTIONS", evaluator_master) \
      + section("CANONICAL REGRESSION SUITE", suite) \
      + section("CANONICAL PROMPT REGIME", regime)
    adjudicator = (
        "# INDEPENDENT ADJUDICATOR: REGRESSION ADJUDICATOR PROMPT\n\n"
        f"Generator: dr {__version__}\nSelected cases: {ids}\nAdjudicator model: {models['adjudicator']}\n\n"
        "You are the independent adjudicator. Audit the evaluator and independently inspect the Reader "
        "artifact against the supplied files. The evaluator is not authoritative. For every criterion, "
        "uphold, revise, overturn, or mark N/D with evidence. Identify missed failures and distinguish "
        "framework defects from execution or load failures. Recommend only justified changes, and produce "
        "one consolidated verdict and prioritized recommendations after all cases.\n"
    ) + section("SHARED ADJUDICATOR INSTRUCTIONS", adjudicator_master) \
      + section("CANONICAL REGRESSION SUITE", suite) \
      + section("CANONICAL PROMPT REGIME", regime)

    for case in cases:
        full = json.dumps(case.manifest, ensure_ascii=False, indent=2, sort_keys=True)
        rdr = json.dumps(reader_manifest(case.manifest), ensure_ascii=False, indent=2, sort_keys=True)
        cond = condition_sections(case, snap)
        reader += section(f"{case.id}: TARGET INSTRUCTIONS", case.target_prompt)
        reader += section(f"{case.id}: CONDITION MANIFEST (reader-facing)", fence(rdr, "json"))
        reader += cond
        evaluator += section(f"{case.id}: EVALUATOR CASE INSTRUCTIONS", case.evaluator_prompt)
        evaluator += section(f"{case.id}: FULL TEST MANIFEST", fence(full, "json"))
        evaluator += cond
        adjudicator += section(f"{case.id}: ADJUDICATOR CASE INSTRUCTIONS", case.adjudicator_prompt)
        adjudicator += section(f"{case.id}: FULL TEST MANIFEST", fence(full, "json"))
        adjudicator += cond

    slot_reader = ("[PASTE THE COMPLETE RAW READER OUTPUT HERE. Preserve test IDs; do not summarize.]\n")
    slot_eval = ("[PASTE THE COMPLETE INDEPENDENT EVALUATOR REPORT HERE. Preserve all criteria, "
                 "evidence, scores, and N/D entries.]\n")
    evaluator += section("RAW READER OUTPUT", reader_output or slot_reader)
    adjudicator += section("RAW READER OUTPUT", reader_output or slot_reader)
    adjudicator += section("INDEPENDENT EVALUATOR REPORT", evaluator_output or slot_eval)

    return {"reader-prompt.md": reader.rstrip() + "\n",
            "evaluator-prompt.md": evaluator.rstrip() + "\n",
            "adjudicator-prompt.md": adjudicator.rstrip() + "\n"}


def build_manifest(cases: List[Case], prompts: Dict[str, str], snap: Snapshot, models: Dict[str, str],
                   reader_output: Optional[str], evaluator_output: Optional[str]) -> dict:
    return {
        "generator": "dr regress",
        "generator_version": __version__,
        "selected_cases": [c.id for c in cases],
        "model_assignments": models,
        "snapshot": str(snap.source),
        "snapshot_sha256": sha256(snap.source.read_bytes()) if snap.is_zip else None,
        "cases": {
            c.id: {
                "request": {k: v for k, v in c.manifest["request"].items()},
                "request_line": c.request_line,
                "files": [{"step": f.load_step, "name": f.name, "version": f.version, "sha256": f.sha256,
                           "reasons": f.reasons} for f in c.plan.files],
                "withheld": c.plan.withheld,
                "full_monty_state": c.plan.full_monty_state,
                "specimen_sha256": c.specimen.sha256 if c.specimen else None,
                "account_sha256": c.account.sha256 if c.account else None,
                "framework_bytes": c.plan.total_bytes,
                "token_estimate": c.plan.token_estimate,
                "warnings": c.plan.warnings,
            } for c in cases
        },
        "prompt_sha256": {n: sha256(t.encode("utf-8")) for n, t in prompts.items()},
        "prompt_chars": {n: len(t) for n, t in prompts.items()},
        "multi_case_context_warning": (
            "A multi-case prompt shares one model context. Each case's LOAD SET defines its condition, but "
            "files included for another case are visible. Compile one case at a time for strict isolation, "
            "especially R10."
        ) if len(cases) > 1 else "Single-case prompt: no cross-case context exposure.",
        "handoff_slots": {
            "evaluator": "reader output embedded" if reader_output else "paste reader output at the marked slot",
            "adjudicator_reader": "reader output embedded" if reader_output else "paste reader output at the marked slot",
            "adjudicator_evaluator": "evaluator report embedded" if evaluator_output else "paste evaluator report at the marked slot",
        },
    }


# ---- entry ----------------------------------------------------------------------

def compile_cases(case_ids: List[str], reg_dir: Path, reg: Registry, snap: Snapshot,
                  models: Dict[str, str], reader_output: Optional[str] = None,
                  evaluator_output: Optional[str] = None, max_tokens: Optional[int] = None):
    """Returns (cases, prompts, build_manifest). Raises RegressionError when any case cannot compile."""
    ids = [c.upper() for c in case_ids]
    if len(set(ids)) != len(ids):
        raise RegressionError("duplicate case IDs")
    bad = [c for c in ids if not CASE_RE.fullmatch(c)]
    if bad:
        raise RegressionError(f"invalid case ID(s): {', '.join(bad)}")
    cases = [load_case(reg_dir, c, reg, snap, max_tokens=max_tokens) for c in ids]
    problems = [e for c in cases for e in c.plan.errors + c.expect_errors]
    if problems:
        raise RegressionError("cannot compile:\n  " + "\n  ".join(problems))
    suite = _read(find_control(reg_dir, "regression-suite"), "regression suite")
    regime = _read(find_control(reg_dir, "prompt-regime"), "prompt regime")
    ev = _read(reg_dir / "prompts" / "evaluator-master.md", "evaluator master")
    ad = _read(reg_dir / "prompts" / "adjudicator-master.md", "adjudicator master")
    prompts = build_prompts(cases, snap, suite, regime, ev, ad, reader_output, evaluator_output, models)
    manifest = build_manifest(cases, prompts, snap, models, reader_output, evaluator_output)
    return cases, prompts, manifest


def write(out_dir: Path, prompts: Dict[str, str], manifest: dict) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for name, content in prompts.items():
        p = out_dir / name
        p.write_text(content, encoding="utf-8", newline="\n")
        written.append(p)
    mp = out_dir / "build-manifest.json"
    mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    written.append(mp)
    return written
