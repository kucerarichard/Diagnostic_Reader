#!/usr/bin/env python3
"""Rewrite tests/golden.json from the current registry, bundle, and regression cases.

Run it after a deliberate change to framework-registry.json, a case manifest,
or a request form, then review the diff before committing. The golden file
pins, per task, the default load set and request line, and per regression
case the load set, withheld list, and request line. It does not pin file
hashes or prompt text, which change with every framework release.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dr.regress import load_case  # noqa: E402
from dr.registry import load_registry  # noqa: E402
from dr.request import Request, normalize, render_request_line  # noqa: E402
from dr.resolve import resolve  # noqa: E402
from dr.snapshot import load_snapshot  # noqa: E402

TASK_PROBES = {
    "quick-read": {},
    "sidecar": {},
    "triangulate": {"voices": ["ASSAY", "PLUMB"]},
    "datum": {"account": True},
    "scan": {"scan_source": "canon", "scan_category": "A", "scan_devices": ["apostrophe"]},
    "workshop": {},
    "poetics-scan": {"kind": "label"},
    "extract": {},
}


def build() -> dict:
    reg = load_registry()
    snap = load_snapshot(ROOT, reg)
    tasks = {}
    for name, kw in TASK_PROBES.items():
        req = normalize(Request(task=name, **kw), reg)
        line = render_request_line(req, reg)
        plan = resolve(req, reg, snap, line)
        tasks[name] = {"request_line": line, "stems": plan.stems()}
    cases = {}
    for d in sorted((ROOT / "regression" / "tests").iterdir()):
        if (d / "manifest.json").is_file():
            c = load_case(ROOT / "regression", d.name, reg, snap)
            cases[c.id] = {"request_line": c.request_line, "stems": c.plan.stems(), "withheld": c.plan.withheld}
    return {"tasks": tasks, "regression_cases": cases}


if __name__ == "__main__":
    out = ROOT / "tests" / "golden.json"
    out.write_text(json.dumps(build(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out}")
