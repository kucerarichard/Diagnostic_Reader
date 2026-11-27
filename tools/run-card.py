#!/usr/bin/env python3
"""Start a run card for a run directory, filled from the build manifests on disk.

`build-manifest.json` records the condition: the request as parsed, every file with its
sha256, the specimen's sha256, the token estimate, the prompt's sha256. It deliberately
records no timestamp, so that identical inputs produce an identical manifest.

That leaves out everything about the run as opposed to the condition: the command, the date,
the repository state, which model executed the prompt, and what that model was told beyond
the prompt. Suite section 5 asks for those. This writes them into a RUN-CARD.md beside the
manifests, filling what it can read and leaving the rest as marked blanks for the operator.

    python tools/run-card.py runs/2026-11-28-my-run
    python tools/run-card.py runs/2026-11-28-my-run --force

A run directory holds one subdirectory per task, each with a build-manifest.json. Blanks are
written as TODO lines; a card with TODO left in it is an incomplete record, not a finished
one.

Standard library only, Python 3.9 or later, same as the dr package.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path


def git(*args, default="unknown"):
    try:
        out = subprocess.run(("git",) + args, capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or default
    except Exception:
        return default


def manifests(run_dir: Path):
    found = []
    for mp in sorted(run_dir.glob("*/build-manifest.json")):
        try:
            found.append((mp.parent.name, json.loads(mp.read_text(encoding="utf-8"))))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"WARN  {mp}: {exc}", file=sys.stderr)
    return found


def prompt_sha(m: dict) -> str:
    if m.get("parts"):
        return m["parts"][0].get("sha256", "")[:16]
    ps = m.get("prompt_sha256") or {}
    return next(iter(ps.values()), "")[:16]


def command_for(task: str, m: dict, out: str = "") -> str:
    """Reconstruct the command from the parsed request. Close, not guaranteed verbatim."""
    r = m.get("request", {})
    parts = ["python -m dr", r.get("task", task)]
    if r.get("task") == "triangulate":
        parts = ["python -m dr", "read", "--triangulate"]
    if r.get("voices"):
        parts += ["--voices"] + list(r["voices"])
    if r.get("verdict"):
        parts += ["--verdict", r["verdict"]]
    for sp in m.get("specimens", []):
        parts += ["--specimen", sp.get("path", "?").replace("\\", "/")]
    if r.get("extensions"):
        parts += ["--extensions"] + list(r["extensions"])
    if r.get("withhold"):
        parts += ["--withhold"] + list(r["withhold"])
    snap = m.get("snapshot", "")
    if snap and snap not in (".",):
        parts += ["--framework", snap]
    if out:
        parts += ["--out", out]
    return " ".join(parts)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--force", action="store_true", help="overwrite an existing card")
    a = ap.parse_args(argv)

    if not a.run_dir.is_dir():
        print(f"ERROR: no such directory: {a.run_dir}", file=sys.stderr); return 2
    card = a.run_dir / "RUN-CARD.md"
    if card.exists() and not a.force:
        print(f"ERROR: {card} exists; pass --force to overwrite", file=sys.stderr); return 2
    found = manifests(a.run_dir)
    if not found:
        print(f"ERROR: no */build-manifest.json under {a.run_dir}", file=sys.stderr); return 2

    L = [f"# Run card: {a.run_dir.name}", "",
         "Filled from the build manifests. Lines marked TODO are the operator's; a card with",
         "TODO left in it is an incomplete record.", "", "## Environment", "",
         "| | |", "|---|---|",
         f"| Run ID | `{a.run_dir.name}` |",
         f"| Date | {date.today().isoformat()} |",
         f"| Repository | commit `{git('rev-parse', '--short', 'HEAD')}` |",
         f"| Working tree | {'clean' if not git('status','--porcelain',default='') else 'DIRTY at compile time'} |",
         f"| Compiler | dr {found[0][1].get('generator_version','?')} |", ""]

    for task, m in found:
        snap = m.get("snapshot", "?")
        L += [f"## {task}", "",
              "```", command_for(task, m, f"{a.run_dir.as_posix()}/{task}"), "```", "",
              "| | |", "|---|---|",
              f"| Request line | `{m.get('request_line','?')}` |",
              f"| Framework | `{snap}` |",
              f"| Files | {len(m.get('files', []))} |",
              f"| Characters | {m.get('prompt_chars', 0):,} |",
              f"| Token estimate | {m.get('token_estimate', 0):,} |",
              f"| Prompt sha256 | `{prompt_sha(m)}` |", ""]
        if m.get("withheld"):
            L += [f"Withheld: {', '.join('`'+w+'`' for w in m['withheld'])}", ""]
        L += ["Load set:", ""]
        for f in m.get("files", []):
            L.append(f"- `{f['name']}` {f.get('version','')} `{f.get('sha256','')[:16]}`")
        L += ["", "TODO which model executed this prompt, and how it was delivered.",
              "TODO what the model was told beyond the prompt. This is part of the condition",
              "     and is recorded nowhere else.", "",
              "TODO what fired, what stood down, and what the output reports as switched off.", ""]

    for task, m in found:
        for sp in m.get("specimens", []):
            L += ["## Specimen", "", "| | |", "|---|---|",
                  f"| Path | `{sp.get('path','?')}` |",
                  f"| sha256 | `{sp.get('sha256','')[:16]}` |"]
            for k, v in (sp.get("card") or {}).items():
                L.append(f"| {k} | {v} |")
            L += ["", "TODO anything about the specimen the card cannot carry: how it was",
                  "     supplied, what was normalized, and whether the copyright status",
                  "     constrains the output.", ""]
            break
        break

    L += ["## Checks run by the operator after the fact", "",
          "TODO what was verified by hand rather than taken from the executor's report.", "",
          "## Limitations", "",
          "TODO fidelity limits, absent files, anything the run could not establish.", ""]

    card.write_text("\n".join(L), encoding="utf-8", newline="\n")
    todos = sum(1 for line in L if line.lstrip().startswith("TODO"))
    print(f"wrote {card} from {len(found)} manifest(s); {todos} TODO lines for you to fill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
