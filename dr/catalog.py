"""Parse the catalogs the `list` commands read.

Each parser reads one framework file from the snapshot and returns plain
dicts. The parsers depend on the markdown shapes those files use today;
tests/test_catalog.py pins the counts so a format change shows up.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional

from .snapshot import Snapshot

DEVICE_STEM = "7-device-inventory-extended"
CONFINEMENT_STEM = "12-confinement-inventory"
DIAL_STEM = "13-speaker-dials"
KERNEL_STEM = "0a-portable-poetics-kernel"

_CATEGORY_HEADING = re.compile(r"^## ([A-G])\. (.+?)\s*$")
_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")
_STRIP_MD = re.compile(r"[*_`]")


def _cells(line: str) -> List[str]:
    m = _TABLE_ROW.match(line.rstrip())
    if not m:
        return []
    return [c.strip() for c in m.group(1).split("|")]


def _is_separator(cells: List[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c) for c in cells)


def _plain(text: str) -> str:
    return _STRIP_MD.sub("", text).strip()


# ---- devices ----------------------------------------------------------------

def devices(snap: Snapshot) -> List[dict]:
    """Rows of the Category A to G tables: category letter and name, device, definition."""
    text = snap.require(DEVICE_STEM).read_text()
    out: List[dict] = []
    cat_letter = cat_name = None
    in_table = False
    for line in text.splitlines():
        h = _CATEGORY_HEADING.match(line)
        if h:
            cat_letter, cat_name = h.group(1), h.group(2)
            in_table = False
            continue
        if line.startswith("## "):
            cat_letter = None
            continue
        if cat_letter is None:
            continue
        cells = _cells(line)
        if not cells:
            in_table = False
            continue
        if _is_separator(cells):
            in_table = True
            continue
        if not in_table:
            continue  # header row
        if len(cells) < 2:
            continue
        out.append({
            "category": cat_letter,
            "category_name": cat_name,
            "device": _plain(cells[0]),
            "definition": _plain(cells[1]),
            "example": _plain(cells[2]) if len(cells) > 2 else "",
        })
    return out


def categories(snap: Snapshot) -> List[dict]:
    counts: Dict[str, dict] = {}
    for d in devices(snap):
        c = counts.setdefault(d["category"], {"category": d["category"], "name": d["category_name"], "devices": 0})
        c["devices"] += 1
    return [counts[k] for k in sorted(counts)]


def find_device(snap: Snapshot, name: str) -> List[dict]:
    key = name.strip().lower()
    return [d for d in devices(snap) if key in d["device"].lower()]


# ---- confinements -----------------------------------------------------------

def confinements(snap: Snapshot) -> List[dict]:
    """Rows of the two index tables (composites and primitives) in 12."""
    text = snap.require(CONFINEMENT_STEM).read_text()
    out: List[dict] = []
    section: Optional[str] = None
    header: List[str] = []
    for line in text.splitlines():
        if line.startswith("## Index: Composites"):
            section, header = "composite", []
            continue
        if line.startswith("## Index: Primitives"):
            section, header = "primitive", []
            continue
        if line.startswith("## "):
            section = None
            continue
        if section is None:
            continue
        cells = _cells(line)
        if not cells:
            continue
        if _is_separator(cells):
            continue
        if not header:
            header = [c.lower() for c in cells]
            continue
        if not cells[0].startswith("cf-"):
            continue
        row = {"class": section}
        for k, v in zip(header, cells):
            row[k] = _plain(v)
        out.append(row)
    return out


def filter_confinements(rows: List[dict], axis: Optional[str] = None, handle: Optional[str] = None,
                        klass: Optional[str] = None, imposed_by: Optional[str] = None) -> List[dict]:
    def ok(r: dict) -> bool:
        if axis and r.get("axis", "").lower() != axis.lower():
            return False
        if handle and handle.lower() not in r.get("handle", "").lower():
            return False
        if klass and r.get("class") != klass:
            return False
        if imposed_by and imposed_by.lower() not in r.get("imposed by", "").lower():
            return False
        return True
    return [r for r in rows if ok(r)]


# ---- dials ------------------------------------------------------------------

_DIAL_HEADING = re.compile(r"^### (sd-\d\d) (.+?)\s*$")
_FIELD_LINE = re.compile(r"^\*\*(Range|Couplings|Device|Checks|Holds fixed)\.\*\*\s*(.*)$")


def dials(snap: Snapshot) -> List[dict]:
    text = snap.require(DIAL_STEM).read_text()
    out: List[dict] = []
    cur: Optional[dict] = None
    in_block = False
    for line in text.splitlines():
        h = _DIAL_HEADING.match(line)
        if h:
            cur = {"id": h.group(1), "name": h.group(2), "status": "", "scale": "", "zero_point": "",
                   "checks": "", "range": "", "couplings": "", "device": ""}
            out.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("## "):
            cur = None
            continue
        if line.strip().startswith("```"):
            in_block = not in_block
            continue
        if in_block:
            for part in line.split("|"):
                k, _, v = part.partition(":")
                k, v = k.strip().lower().replace(" ", "_"), v.strip()
                if k in cur and v:
                    cur[k] = v
            continue
        f = _FIELD_LINE.match(line)
        if f:
            key = f.group(1).lower().replace(" ", "_")
            if not cur.get(key):  # the fenced block's value wins over the prose field
                cur[key] = f.group(2).strip()
    return out


# ---- directives -------------------------------------------------------------

def directives(snap: Snapshot) -> List[dict]:
    """### headings under the kernel's Portable Calibration Directives and V0.3 Supplemental Directives."""
    text = snap.require(KERNEL_STEM).read_text()
    out: List[dict] = []
    section: Optional[str] = None
    pending: Optional[dict] = None
    want_prompt = False
    for line in text.splitlines():
        if line.startswith("## Portable Calibration Directives"):
            section = "portable"
            continue
        if line.startswith("## V0.3 Supplemental Directives"):
            section = "supplemental"
            continue
        if line.startswith("## "):
            section = None
            pending = None
            continue
        if section and line.startswith("### "):
            pending = {"name": line[4:].strip(), "class": section, "prompt": ""}
            out.append(pending)
            want_prompt = False
            continue
        if pending is None:
            continue
        if line.strip() == "Prompt:":
            want_prompt = True
            continue
        if want_prompt and line.startswith(">") and not pending["prompt"]:
            pending["prompt"] = line.lstrip("> ").strip()
            want_prompt = False
    # the supplemental section also holds two rules that are not directives
    return [d for d in out if d["class"] == "portable" or d["name"] in
            ("Captive Attention Mechanism", "Access-Asymmetry Mode")]


# ---- regression tests -------------------------------------------------------

def regression_tests(regression_dir: Path) -> List[dict]:
    out: List[dict] = []
    tests_dir = Path(regression_dir) / "tests"
    if not tests_dir.is_dir():
        return out
    for mf in sorted(tests_dir.glob("*/manifest.json")):
        try:
            m = json.loads(mf.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            out.append({"id": mf.parent.name, "error": str(exc)})
            continue
        req = m.get("request") or {}
        summary = req.get("task", "")
        if req.get("voices"):
            summary += " " + "+".join(req["voices"])
        if req.get("scan_devices"):
            summary += f" {req.get('scan_source', '')} {' '.join(req['scan_devices'])}"
        if req.get("vise"):
            summary += " +VISE"
        if req.get("account"):
            summary += " +account"
        if req.get("extensions"):
            summary += " ext:" + ",".join(req["extensions"])
        out.append({
            "id": m.get("test_id", mf.parent.name),
            "title": m.get("title", ""),
            "condition": m.get("condition", ""),
            "work": m.get("canonical_work", ""),
            "request": summary,
            "withheld": req.get("withhold", m.get("withheld_files", [])),
            "specimen": (m.get("specimen") or {}).get("path", "") or "(none)",
            "status": (m.get("specimen") or {}).get("status", ""),
        })
    return out
