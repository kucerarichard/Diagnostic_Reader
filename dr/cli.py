"""Command line for the Diagnostic Reader compiler.

    python -m dr explain read --triangulate --voices ASSAY PLUMB --verdict PLUMB
    python -m dr lint
    python -m dr list devices --category A

read, workshop, scan, and extract compile a prompt into --out. Every one of
them takes --explain to print the plan instead.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path
from typing import List, Optional

from . import __version__
from .catalog import (categories, confinements, devices, dials, directives, filter_confinements,
                      find_device, regression_tests)
from .compile import CompileError, Specimen, build, load_specimen, write
from .lint import lint
from .regress import RegressionError, compile_cases
from .regress import write as write_regression
from .registry import Registry, RegistryError, load_registry
from .request import Request, normalize, render_request_line
from .resolve import DEFAULT_CHARS_PER_TOKEN, LoadPlan, ResolveError, resolve
from .snapshot import Snapshot, SnapshotError, load_snapshot

COMPILE_COMMANDS = ("read", "workshop", "scan", "extract")


# ---- argument grammar ---------------------------------------------------------

def _default_framework() -> Path:
    env = os.environ.get("DR_FRAMEWORK")
    if env:
        return Path(env)
    return Path(__file__).resolve().parent.parent


def add_global(p: argparse.ArgumentParser, top: bool = True) -> None:
    """Global flags. They are accepted before or after the subcommand; on a
    subparser the defaults are suppressed so they only apply when given."""
    kw = {} if top else {"default": argparse.SUPPRESS}
    p.add_argument("--framework", type=Path, **({"default": None} if top else kw),
                   help="framework snapshot: directory or ZIP (default: $DR_FRAMEWORK or the repo root)")
    p.add_argument("--registry", type=Path, **({"default": None} if top else kw),
                   help="alternate framework-registry.json")
    p.add_argument("--json", action="store_true", **kw, help="machine-readable output")


def add_shared_compile(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("specimen")
    g.add_argument("--specimen", type=Path, action="append", default=[], metavar="FILE",
                   help="specimen text file; repeatable; '-' reads stdin. A header block of "
                        "'Key: value' lines (title, author, date, edition, kind, unit, provenance, "
                        "copyright) followed by a blank line is read as the card")
    g.add_argument("--title")
    g.add_argument("--author")
    g.add_argument("--date")
    g.add_argument("--edition")
    g.add_argument("--kind", default="poem", help="what the specimen presents itself as (default poem)")
    g.add_argument("--unit", default=None, help="what an address counts (default from kind)")
    g.add_argument("--provenance", help="the user's own draft / posted for critique at X / published in Y / public domain")
    g.add_argument("--copyright", help="source status: the user's / in copyright / public domain / unknown")
    g.add_argument("--found-by", help="for found text: the user / named third party / a named procedure")

    g = p.add_argument_group("modules")
    g.add_argument("--extensions", nargs="+", default=[], metavar="EXT",
                   help="features or stems: frye casanova monadology attridge-staten compartmentalization battery 7a 9 14 ...")
    g.add_argument("--plugins", nargs="+", default=[], metavar="PLUGIN",
                   help="full monty plugins by handle or stem; private and opt-in (Full Monty State defaults to absent)")
    g.add_argument("--slot-registry", action="store_true", help="load 0b-voice-slot-registry")
    g.add_argument("--include", nargs="+", default=[], metavar="STEM", help="force a module in")
    g.add_argument("--exclude", nargs="+", default=[], metavar="STEM", help="force a module out (recorded)")
    g.add_argument("--withhold", nargs="+", default=[], metavar="STEM",
                   help="fault injection: remove a module and record it as withheld")
    g.add_argument("--no-boot", action="store_true", help="omit 0-poetics-boot-hollow")

    g = p.add_argument_group("budget and output")
    g.add_argument("--max-tokens", type=int, default=None, help="fail when the estimate exceeds this")
    g.add_argument("--chars-per-token", type=float, default=DEFAULT_CHARS_PER_TOKEN)
    g.add_argument("--part-size", type=int, default=None, metavar="CHARS",
                   help="split the prompt into parts under this many characters, at file boundaries")
    g.add_argument("--out", type=Path, default=Path("compiled-run"), help="output directory (default compiled-run)")

    p.add_argument("--ask", metavar="TEXT", help="free-text operator request appended to the request line")
    p.add_argument("--explain", action="store_true", help="print the load plan instead of compiling")


def add_read(p: argparse.ArgumentParser) -> None:
    m = p.add_mutually_exclusive_group()
    m.add_argument("--quick", action="store_true", help="minimal runtime: 0a and 0c")
    m.add_argument("--sidecar", action="store_true", help="full diagnostic (default)")
    m.add_argument("--triangulate", action="store_true", help="sidecar with commentary from two or more voices")
    m.add_argument("--datum", action="store_true", help="record-against-account reading: 0a 0c 11 5")
    m.add_argument("--poetics-scan-only", action="store_true", help="the Poetics Scan alone, then stop")
    p.add_argument("--voices", nargs="+", default=[], metavar="VOICE", help="ASSAY PLUMB TARE RETICLE DATUM")
    p.add_argument("--verdict", metavar="VOICE", help="voice that closes")
    p.add_argument("--counter-voice", action="append", default=[], metavar="VOICE",
                   help="add a voice in a zone another voice holds; repeatable")
    p.add_argument("--vise", action="store_true", help="VISE verdict (loads 4-gonzo-mode)")
    p.add_argument("--spine", metavar="VOICE", help="voice VISE rides (default: verdict voice, else first voice)")
    p.add_argument("--hermetic", action="store_true", help="Section H chamber reading")
    p.add_argument("--battery", action="store_true", help="Full battery report (loads 7a)")
    p.add_argument("--account", type=Path, default=None, metavar="FILE",
                   help="text file holding the poet's account, for DATUM")
    add_shared_compile(p)


def add_workshop(p: argparse.ArgumentParser) -> None:
    p.add_argument("--voices", nargs="+", default=[], metavar="VOICE", help="extra voices beside TARE")
    r = p.add_mutually_exclusive_group()
    r.add_argument("--rewrites", action="store_true", help="confinement rewrites (two trials)")
    r.add_argument("--no-rewrites", action="store_true")
    p.add_argument("--rewrite-under", action="append", default=[], metavar="CONFINEMENT",
                   help="e.g. 'withheld case + flat predicate', 'axis: upward', 'handle: Snow Crust'")
    p.add_argument("--ars-poetica", action="store_true", help="+ ars poetica overlay")
    d = p.add_mutually_exclusive_group()
    d.add_argument("--dial-trial", nargs="?", const="", default=None, metavar="DIAL",
                   help="dial trial; name a dial or let the reasoning path choose (loads 13)")
    d.add_argument("--no-dial-trials", action="store_true")
    p.add_argument("--rewrite-at", action="append", default=[], metavar="DIAL:SETTING",
                   help="e.g. 'diction altitude:high' (loads 13)")
    p.add_argument("--contrast-at", metavar="DEVICE", help="Function Bay named contrast trial")
    p.add_argument("--feedback-bridge", action="store_true", help="section 13, what one peer can say in the thread")
    add_shared_compile(p)


def add_scan(p: argparse.ArgumentParser) -> None:
    p.add_argument("source", choices=["canon", "supplied"], help="canon from the model's knowledge, or a supplied corpus")
    p.add_argument("--category", metavar="A-H", help="device Category letter or name")
    p.add_argument("--devices", nargs="+", required=True, metavar="DEVICE")
    p.add_argument("--or", dest="scan_or", action="store_true", help="any device, instead of all (conjunctive default)")
    p.add_argument("--corpus", type=Path, action="append", default=[], metavar="FILE", help="supplied corpus files")
    add_shared_compile(p)


def add_extract(p: argparse.ArgumentParser) -> None:
    add_shared_compile(p)


ADDERS = {"read": add_read, "workshop": add_workshop, "scan": add_scan, "extract": add_extract}


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="dr", description="Diagnostic Reader prompt compiler")
    ap.add_argument("--version", action="version", version=f"dr {__version__}")
    add_global(ap)
    sub = ap.add_subparsers(dest="command", required=True)

    for name, adder in ADDERS.items():
        p = sub.add_parser(name, help=f"compile a {name} prompt")
        adder(p)
        add_global(p, top=False)

    ex = sub.add_parser("explain", help="show the load plan for a request without writing anything")
    exsub = ex.add_subparsers(dest="explain_command", required=True)
    for name, adder in ADDERS.items():
        p = exsub.add_parser(name)
        adder(p)
        add_global(p, top=False)

    rg = sub.add_parser("regress", help="compile regression cases into reader, evaluator, and adjudicator prompts")
    rg.add_argument("--cases", nargs="+", required=True, metavar="R-ID", help="e.g. R1 R3 R10-A")
    rg.add_argument("--regression-dir", type=Path, default=None, help="default <framework>/regression")
    rg.add_argument("--out", type=Path, default=Path("compiled-regression"))
    rg.add_argument("--reader-output", type=Path, help="raw Reader output to embed in the evaluator and adjudicator prompts")
    rg.add_argument("--evaluator-output", type=Path, help="evaluator report to embed in the adjudicator prompt")
    rg.add_argument("--reader-model", default="X (not specified)")
    rg.add_argument("--evaluator-model", default="Y (not specified)")
    rg.add_argument("--adjudicator-model", default="Z (not specified)")
    rg.add_argument("--max-tokens", type=int, default=None, help="per-case budget on the framework set")
    rg.add_argument("--explain", action="store_true", help="show each case's load plan and write nothing")
    add_global(rg, top=False)

    li = sub.add_parser("lint", help="check framework-registry.json against the boot, the disk, and the regression manifests")
    add_global(li, top=False)

    ls = sub.add_parser("list", help="list what the canon can be scanned or asked for")
    add_global(ls, top=False)
    ls.add_argument("what", choices=["modules", "tasks", "voices", "modes", "plugins", "features",
                                     "devices", "categories", "confinements", "dials", "directives",
                                     "kinds", "tests"])
    ls.add_argument("--category", metavar="A-G", help="devices: one Category")
    ls.add_argument("--find", metavar="TEXT", help="devices: substring match on the device name")
    ls.add_argument("--axis", choices=["upward", "sideways", "inward", "outward"], help="confinements")
    ls.add_argument("--handle", metavar="HANDLE", help="confinements: specimen handle substring")
    ls.add_argument("--class", dest="klass", choices=["composite", "primitive"], help="confinements")
    ls.add_argument("--imposed-by", metavar="TEXT", help="confinements: substring on imposed by")
    return ap


# ---- request assembly -----------------------------------------------------------

def request_from_args(cmd: str, a: argparse.Namespace) -> Request:
    if cmd == "read":
        if a.quick:
            task = "quick-read"
        elif a.triangulate:
            task = "triangulate"
        elif a.datum:
            task = "datum"
        elif a.poetics_scan_only:
            task = "poetics-scan"
        else:
            task = "sidecar"
        req = Request(task=task, voices=a.voices, verdict=a.verdict, counter_voices=a.counter_voice,
                      vise=a.vise, spine=a.spine, hermetic=a.hermetic, battery=a.battery,
                      account=a.account is not None,
                      account_path=str(a.account) if a.account else None)
    elif cmd == "workshop":
        req = Request(task="workshop", voices=a.voices,
                      rewrites=True if a.rewrites else (False if a.no_rewrites else None),
                      rewrite_under=a.rewrite_under, ars_poetica=a.ars_poetica,
                      dial_trial=a.dial_trial, rewrite_at=a.rewrite_at, no_dial_trials=a.no_dial_trials,
                      contrast_at=a.contrast_at, feedback_bridge=a.feedback_bridge)
    elif cmd == "scan":
        req = Request(task="scan", scan_source=a.source, scan_category=a.category,
                      scan_devices=a.devices, scan_or=a.scan_or, corpus=[str(c) for c in a.corpus])
    else:
        req = Request(task="extract")
    req.kind = a.kind
    req.unit = a.unit
    req.specimens = [str(x) for x in a.specimen]
    req.title, req.author, req.date, req.edition = a.title, a.author, a.date, a.edition
    req.provenance, req.copyright, req.found_by = a.provenance, a.copyright, a.found_by
    req.extensions = list(a.extensions)
    if a.slot_registry:
        req.extensions.append("slot-registry")
    req.plugins = list(a.plugins)
    req.include, req.exclude, req.withhold = list(a.include), list(a.exclude), list(a.withhold)
    req.no_boot = a.no_boot
    req.ask = a.ask
    return req


# ---- output -----------------------------------------------------------------------

def _fmt_size(n: int) -> str:
    return f"{n / 1e6:.2f} MB" if n >= 1e6 else f"{n / 1e3:.0f} KB"


def print_plan(plan: LoadPlan, snap: Snapshot, a: argparse.Namespace) -> None:
    req = plan.request
    print(f"Request:       {req.task}" + (f"; voices {', '.join(req.voices)}" if req.voices else "")
          + (f"; verdict {req.verdict}" if req.verdict else "")
          + (f"; kind {req.kind}, unit {req.unit}" if req.found else ""))
    lines = plan.request_line.splitlines() or [""]
    print(f"Request line:  {lines[0]}")
    for extra in lines[1:]:
        print(f"               {extra}")
    print(f"Snapshot:      {snap.source}" + (f" (zip, root {snap.root or '/'})" if snap.is_zip else ""))
    if req.specimens:
        print("Specimens:     " + ", ".join(req.specimens))
    if req.account_path:
        print(f"Account:       {req.account_path}")
    if req.corpus:
        print("Corpus:        " + ", ".join(req.corpus))
    print()
    print(f"{'step':4s} {'file':48s} {'version':8s} {'size':>8s}  why")
    for f in plan.files:
        step = "-" if f.load_step is None else str(f.load_step)
        why = "; ".join(f.reasons)
        print(f"{step:4s} {f.name:48s} {f.version or '?':8s} {_fmt_size(f.size):>8s}  {why}")
    print()
    print(f"Full Monty State: {plan.full_monty_state}" + (f" ({', '.join(plan.plugins)})" if plan.plugins else ""))
    if plan.withheld:
        print(f"Withheld (fault injection): {', '.join(plan.withheld)}")
    if plan.excluded:
        print(f"Excluded: {', '.join(plan.excluded)}")
    budget = f"; budget {plan.max_tokens:,}" if plan.max_tokens else ""
    print(f"Total: {_fmt_size(plan.total_bytes)} across {len(plan.files)} files; "
          f"~{plan.token_estimate:,} tokens at {plan.chars_per_token:g} chars/token{budget}")
    for w in plan.warnings:
        print(f"WARN  {w}")
    for e in plan.errors:
        print(f"ERROR {e}")
    if plan.ok:
        print("Plan OK.")


def plan_to_json(plan: LoadPlan, snap: Snapshot) -> dict:
    return {
        "request": asdict(plan.request),
        "request_line": plan.request_line,
        "snapshot": str(snap.source),
        "files": [asdict(f) for f in plan.files],
        "withheld": plan.withheld,
        "excluded": plan.excluded,
        "missing": plan.missing,
        "full_monty_state": plan.full_monty_state,
        "plugins": plan.plugins,
        "total_bytes": plan.total_bytes,
        "token_estimate": plan.token_estimate,
        "max_tokens": plan.max_tokens,
        "warnings": plan.warnings,
        "errors": plan.errors,
        "ok": plan.ok,
    }


def _table(rows: List[dict], cols: List[str], widths: Optional[List[int]] = None) -> None:
    if not rows:
        print("(none)")
        return
    widths = widths or [max(len(c), max(len(str(r.get(c, ""))) for r in rows)) for c in cols]
    widths = [min(w, 60) for w in widths]
    print("  ".join(c.ljust(w) for c, w in zip(cols, widths)))
    for r in rows:
        print("  ".join(str(r.get(c, ""))[:w].ljust(w) for c, w in zip(cols, widths)))


def do_list(a: argparse.Namespace, reg: Registry, snap: Snapshot, framework: Path) -> int:
    what = a.what
    rows: List[dict]
    if what == "modules":
        rows = []
        for m in reg.in_load_order([s for s in reg.modules if reg.modules[s].loadable or snap.get(s)]):
            ff = snap.get(m)
            mm = reg.modules[m]
            rows.append({"step": "-" if mm.load_step is None else mm.load_step, "stem": m,
                         "version": (ff.version if ff else "absent"), "type": mm.type,
                         "designation": mm.designation or "", "requires": ", ".join(mm.requires),
                         "size": _fmt_size(ff.size) if ff else "", "role": mm.role})
        cols = ["step", "stem", "version", "type", "designation", "requires", "size", "role"]
    elif what == "tasks":
        rows = [{"task": t.name, "label": t.label, "modules": ", ".join(t.modules),
                 "default voices": ", ".join(t.default_voices) or ("2+ required" if t.min_voices else "")}
                for t in reg.tasks.values()]
        cols = ["task", "label", "default voices", "modules"]
    elif what == "voices":
        rows = [{"designation": d, "module": v["module"], "unit": v["unit"], "fires when": v["fires"],
                 "holds silent when": v["silent"]} for d, v in reg.voices.items()]
        cols = ["designation", "module", "unit", "fires when", "holds silent when"]
    elif what == "modes":
        rows = [{"designation": d, "module": v["module"], "rides": v["rides"]} for d, v in reg.modes.items()]
        cols = ["designation", "module", "rides"]
    elif what == "plugins":
        rows = [{"handle": m.handle, "stem": m.stem, "on disk": "yes" if snap.get(m.stem) else "no",
                 "collides with": ", ".join(m.collides_with), "calibration": m.role} for m in reg.plugins()]
        cols = ["handle", "stem", "on disk", "collides with", "calibration"]
    elif what == "features":
        rows = [{"feature": k, "modules": ", ".join(v["modules"]), "note": v.get("note", "")}
                for k, v in reg.features.items()]
        cols = ["feature", "modules", "note"]
    elif what == "devices":
        rows = find_device(snap, a.find) if a.find else devices(snap)
        if a.category:
            rows = [d for d in rows if d["category"].lower() == a.category.lower() or
                    a.category.lower() in d["category_name"].lower()]
        cols = ["category", "device", "definition"]
    elif what == "categories":
        rows = categories(snap)
        cols = ["category", "name", "devices"]
    elif what == "confinements":
        rows = filter_confinements(confinements(snap), axis=a.axis, handle=a.handle,
                                   klass=a.klass, imposed_by=a.imposed_by)
        cols = ["id", "class", "name", "handle", "axis", "imposed by"]
    elif what == "dials":
        rows = dials(snap)
        cols = ["id", "name", "status", "checks", "couplings"]
    elif what == "directives":
        rows = directives(snap)
        cols = ["name", "class", "prompt"]
    elif what == "kinds":
        rows = [{"kind": k, "default unit": reg.kind_default_unit.get(k, "")} for k in reg.kinds]
        cols = ["kind", "default unit"]
    else:  # tests
        rows = regression_tests(framework / "regression")
        cols = ["id", "title", "request", "withheld", "specimen"]
        for r in rows:
            r["withheld"] = ", ".join(r.get("withheld", []))
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        _table(rows, cols)
        print(f"\n{len(rows)} {what}")
    return 0


# ---- main -------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    try:
        return _main(argv)
    except BrokenPipeError:
        # Output was piped into something that stopped reading (head, more). Not an error.
        try:
            sys.stdout.close()
        except OSError:
            pass
        return 0


def _main(argv: Optional[List[str]]) -> int:
    ap = build_parser()
    a = ap.parse_args(argv)
    framework = (a.framework or _default_framework()).resolve()
    try:
        reg = load_registry(a.registry)
        snap = load_snapshot(framework, reg)
    except (RegistryError, SnapshotError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if a.command == "lint":
        findings = lint(reg, snap, framework / "regression")
        if a.json:
            print(json.dumps([asdict(f) for f in findings], indent=2))
        else:
            for f in findings:
                print(f)
            errs = sum(1 for f in findings if f.level == "error")
            warns = sum(1 for f in findings if f.level == "warn")
            print(f"\n{len(snap.files)} framework files; {errs} errors, {warns} warnings, "
                  f"{len(findings) - errs - warns} notes")
        return 1 if any(f.level == "error" for f in findings) else 0

    if a.command == "list":
        try:
            return do_list(a, reg, snap, framework)
        except SnapshotError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

    if a.command == "regress":
        return do_regress(a, reg, snap, framework)

    cmd = a.explain_command if a.command == "explain" else a.command
    explaining = a.command == "explain" or a.explain
    try:
        req = normalize(request_from_args(cmd, a), reg)
        line = render_request_line(req, reg)
        plan = resolve(req, reg, snap, line, max_tokens=a.max_tokens, chars_per_token=a.chars_per_token)
    except (RegistryError, ResolveError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if explaining:
        if a.json:
            print(json.dumps(plan_to_json(plan, snap), ensure_ascii=False, indent=2))
        else:
            print_plan(plan, snap, a)
        return 0 if plan.ok else 1

    if not plan.ok:
        print_plan(plan, snap, a)
        print("\nNothing written.", file=sys.stderr)
        return 1
    try:
        specimens = load_specimens(req)
        b = build(plan, reg, snap, specimens, part_size=a.part_size)
        written = write(b, a.out)
    except (CompileError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({"written": [str(p) for p in written], "manifest": b.manifest}, ensure_ascii=False, indent=2))
    else:
        m = b.manifest
        print(f"Wrote {len(written)} files to {a.out}")
        for part in m["parts"]:
            print(f"  {part['name']}: {part['chars']:,} chars; sha256 {part['sha256'][:16]}")
        print(f"  build-manifest.json")
        print(f"Request line: {plan.request_line.splitlines()[0]}" + (" ..." if "\n" in plan.request_line else ""))
        print(f"~{m['token_estimate']:,} tokens at {m['chars_per_token']:g} chars/token; "
              f"{len(m['files'])} framework files; Full Monty State {m['full_monty_state']}")
        for w in m["warnings"]:
            print(f"WARN  {w}")
    return 0


def do_regress(a: argparse.Namespace, reg: Registry, snap: Snapshot, framework: Path) -> int:
    reg_dir = (a.regression_dir or framework / "regression").resolve()
    if snap.is_zip and a.regression_dir is None:
        print("ERROR: with a ZIP snapshot, pass --regression-dir", file=sys.stderr)
        return 2
    models = {"reader": a.reader_model, "evaluator": a.evaluator_model, "adjudicator": a.adjudicator_model}
    try:
        ro = a.reader_output.read_text(encoding="utf-8") if a.reader_output else None
        eo = a.evaluator_output.read_text(encoding="utf-8") if a.evaluator_output else None
        if a.explain:
            from .regress import load_case
            code = 0
            for cid in a.cases:
                case = load_case(reg_dir, cid.upper(), reg, snap, max_tokens=a.max_tokens)
                print(f"##### {case.id}: {case.manifest.get('title', '')}")
                print_plan(case.plan, snap, a)
                for e in case.expect_errors:
                    print(f"ERROR {e}")
                print()
                code = code or (0 if case.ok else 1)
            return code
        cases, prompts, manifest = compile_cases(a.cases, reg_dir, reg, snap, models, ro, eo, a.max_tokens)
        written = write_regression(a.out, prompts, manifest)
    except (RegressionError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({"written": [str(p) for p in written], "manifest": manifest}, ensure_ascii=False, indent=2))
        return 0
    print(f"Wrote {len(written)} files to {a.out} for {', '.join(c.id for c in cases)}")
    for name, content in prompts.items():
        print(f"  {name}: {len(content):,} chars; sha256 {manifest['prompt_sha256'][name][:16]}")
    print("  build-manifest.json")
    for c in cases:
        print(f"  {c.id}: {len(c.plan.files)} files, ~{c.plan.token_estimate:,} tokens; {c.request_line.splitlines()[0]}"
              + (f"; withheld {', '.join(c.plan.withheld)}" if c.plan.withheld else ""))
        for w in c.plan.warnings:
            print(f"    WARN {w}")
    if len(cases) > 1:
        print("WARNING: multi-case prompts share one context; compile one case for strict isolation.", file=sys.stderr)
    return 0


def load_specimens(req: Request) -> List[Specimen]:
    overrides = {"title": req.title, "author": req.author, "date": req.date, "edition": req.edition,
                 "provenance": req.provenance, "copyright": req.copyright, "found by": req.found_by}
    if len(req.specimens) > 1 and any(overrides.values()):
        raise CompileError("with more than one specimen, put the card fields in each file's header "
                           "block instead of --title/--author/...")
    out: List[Specimen] = []
    for sp in req.specimens:
        out.append(load_specimen(Path(sp), "specimen", overrides))
    if req.account_path:
        out.append(load_specimen(Path(req.account_path), "account", {}))
    for c in req.corpus:
        out.append(load_specimen(Path(c), "corpus", {}))
    return out
