"""Tests for the dr package. Run from the repo root:

    python -m unittest discover -s tests -v

They read the framework files in the repo root, so counts pinned here
(192 devices, 194 confinements, 9 dials, 21 directives) move when the
catalogs do. That is the point.
"""
from __future__ import annotations

import ast
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from dr import catalog, cli
from dr.compile import CompileError, Specimen, build, load_specimen, split_meta, write
from dr.lint import lint
from dr.regress import RegressionError, compile_cases, load_case, reader_manifest
from dr.regress import write as write_regression
from dr.registry import RegistryError, load_registry, version_ge
from dr.request import Request, normalize, render_request_line
from dr.resolve import resolve
from dr.snapshot import header_version, load_snapshot, split_filename

ROOT = Path(__file__).resolve().parent.parent
REG = load_registry()
SNAP = load_snapshot(ROOT, REG)


def plan_for(**kw):
    max_tokens = kw.pop("max_tokens", None)
    req = normalize(Request(**kw), REG)
    return resolve(req, REG, SNAP, render_request_line(req, REG), max_tokens=max_tokens)


class RegistryTests(unittest.TestCase):
    def test_version_floor_semantics(self):
        self.assertTrue(version_ge("0.3.19", "0.3"))
        self.assertTrue(version_ge("0.3.16", "0.3.16"))
        self.assertFalse(version_ge("0.3.15", "0.3.16"))
        self.assertTrue(version_ge("0.4", "0.3.16"))
        self.assertTrue(version_ge("1.0", "0.9.9"))

    def test_lookups(self):
        self.assertEqual(REG.voice_module("plumb"), "2-harris-voice-module")
        self.assertEqual(REG.resolve_stem("7"), "7-device-inventory-extended")
        self.assertEqual(REG.resolve_stem("7a"), "7a-nom-function-battery")
        self.assertEqual(REG.resolve_stem("3-kowit"), "3-kowit-voice-module")
        self.assertEqual(REG.plugin_stem("Snow Crust"), "full-monty-snowcrust-example")
        self.assertEqual(REG.plugin_stem("full-monty-santos-small-branch-example"),
                         "full-monty-santos-small-branch")
        with self.assertRaises(RegistryError):
            REG.voice_module("MUSE")

    def test_every_voice_has_a_module_on_disk(self):
        for v in REG.voices.values():
            self.assertIsNotNone(SNAP.get(v["module"]), v["module"])


class SnapshotTests(unittest.TestCase):
    def test_split_filename(self):
        self.assertEqual(split_filename("0a-portable-poetics-kernel-v0_3_19.md"),
                         ("0a-portable-poetics-kernel", "0.3.19"))
        self.assertEqual(split_filename("full-monty-santos-small-branch-v0.2.md"),
                         ("full-monty-santos-small-branch", "0.2"))
        self.assertEqual(split_filename("full-monty-snowcrust-example.md"),
                         ("full-monty-snowcrust-example", None))

    def test_header_version_patterns(self):
        self.assertEqual(header_version("# X\n\nVersion: 0.18\n"), "0.18")
        self.assertEqual(header_version("# X\n## Module Manifest\nModule version: v0.3.1\n"), "0.3.1")
        self.assertEqual(header_version("# X\nVersion 0.2. Derived from\n"), "0.2")
        self.assertEqual(header_version("# X\n## Revision Note (v0.2)\n"), "0.2")
        self.assertIsNone(header_version("# X\nno version here\n"))

    def test_versions_resolved(self):
        self.assertEqual(SNAP.version_of("0a-portable-poetics-kernel"), "0.3.19")
        self.assertEqual(SNAP.version_of("2-harris-voice-module"), "0.3.1")
        self.assertEqual(SNAP.version_of("12-confinement-inventory"), "0.16")
        self.assertEqual(len(SNAP.files), 29)
        self.assertIn("README.md", SNAP.skipped)
        self.assertNotIn("regression/README.md", SNAP.by_name)

    def test_zip_with_top_folder(self):
        with tempfile.TemporaryDirectory() as td:
            zpath = Path(td) / "snap.zip"
            with zipfile.ZipFile(zpath, "w") as zf:
                for f in ROOT.glob("*.md"):
                    zf.write(f, f"Some Folder/{f.name}")
                zf.writestr("Some Folder/regression/README.md", "not runtime")
            snap = load_snapshot(zpath, REG)
            self.assertEqual(snap.root, "Some Folder")
            self.assertEqual(len(snap.files), 29)
            self.assertEqual(snap.get("0c-voice-designations").read_text()[:7], "# VOICE")

    def test_duplicate_release_picks_newer(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for f in ROOT.glob("*.md"):
                shutil.copy(f, d / f.name)
            (d / "8-frye-extraction-v0_5.md").write_text("# FRYE\nVersion: 0.5\n", encoding="utf-8")
            snap = load_snapshot(d, REG)
            self.assertEqual(snap.version_of("8-frye-extraction"), "0.6")
            self.assertIn("8-frye-extraction", snap.duplicates)


class ResolveTests(unittest.TestCase):
    def test_quick_read_minimal_set(self):
        p = plan_for(task="quick-read")
        self.assertEqual(p.stems(), ["0-poetics-boot-hollow", "0a-portable-poetics-kernel", "0c-voice-designations"])
        self.assertTrue(p.ok)

    def test_sidecar_defaults_to_assay(self):
        p = plan_for(task="sidecar")
        self.assertIn("1-rother-voice-module", p.stems())
        self.assertIn("7-device-inventory-extended", p.stems())

    def test_triangulate_needs_two_voices(self):
        with self.assertRaises(RegistryError):
            plan_for(task="triangulate")
        p = plan_for(task="triangulate", voices=["ASSAY", "PLUMB"])
        self.assertTrue(p.ok)

    def test_datum_pulls_11_through_closure(self):
        p = plan_for(task="sidecar", voices=["DATUM"])
        self.assertIn("11-provenance-grading-extension", p.stems())
        reasons = {f.stem: f.reasons for f in p.files}
        self.assertIn("required by 5-hersh-voice-module", reasons["11-provenance-grading-extension"])

    def test_workshop_set_and_dials(self):
        p = plan_for(task="workshop")
        self.assertEqual(set(p.stems()), {
            "0-poetics-boot-hollow", "0a-portable-poetics-kernel", "0c-voice-designations",
            "7-device-inventory-extended", "12-confinement-inventory", "3-kowit-voice-module", "3a-workshop"})
        self.assertNotIn("13-speaker-dials", p.stems())
        p = plan_for(task="workshop", dial_trial="")
        self.assertIn("13-speaker-dials", p.stems())
        p = plan_for(task="workshop", dial_trial="idiom density", no_dial_trials=True)
        self.assertNotIn("13-speaker-dials", p.stems())

    def test_found_text_loads_8(self):
        p = plan_for(task="sidecar", kind="news report")
        self.assertIn("8-frye-extraction", p.stems())
        self.assertEqual(p.request.unit, "paragraph")
        self.assertNotIn("8-frye-extraction", plan_for(task="sidecar").stems())

    def test_battery_requires_7(self):
        p = plan_for(task="quick-read", battery=True)
        self.assertIn("7a-nom-function-battery", p.stems())
        self.assertIn("7-device-inventory-extended", p.stems())

    def test_load_order(self):
        p = plan_for(task="workshop", voices=["TARE", "PLUMB"], dial_trial="", plugins=["Snow Crust"])
        steps = [f.load_step for f in p.files]
        self.assertEqual(steps, sorted(steps))
        self.assertEqual(p.files[-1].type, "plugin")

    def test_withhold_is_recorded_and_warns(self):
        p = plan_for(task="datum", account=True, withhold=["11"])
        self.assertEqual(p.withheld, ["11-provenance-grading-extension"])
        self.assertNotIn("11-provenance-grading-extension", p.stems())
        self.assertTrue(any("5-hersh-voice-module depend" in w for w in p.warnings))
        self.assertTrue(p.ok)  # fault injection is a valid plan

    def test_withhold_0c_warns_about_labels(self):
        p = plan_for(task="sidecar", withhold=["0c"])
        self.assertTrue(any("label output with its source" in w for w in p.warnings))

    def test_plugins_opt_in_and_state(self):
        self.assertEqual(plan_for(task="sidecar").full_monty_state, "absent")
        self.assertEqual(plan_for(task="sidecar", plugins=["Snow Crust"]).full_monty_state, "present")
        self.assertEqual(plan_for(task="sidecar", plugins=["Snow Crust", "Gilson"]).full_monty_state, "multi")

    def test_collision_warning(self):
        p = plan_for(task="workshop", plugins=["Kowit Hell"])
        self.assertTrue(any("calibration collision" in w for w in p.warnings))

    def test_non_loadable_is_an_error(self):
        p = plan_for(task="quick-read", include=["voice-volitional-map"])
        self.assertFalse(p.ok)

    def test_budget(self):
        p = plan_for(task="triangulate", voices=["ASSAY", "PLUMB"], max_tokens=100_000)
        self.assertTrue(p.over_budget)
        self.assertFalse(p.ok)
        self.assertTrue(plan_for(task="quick-read", max_tokens=100_000).ok)

    def test_floor_violation_detected(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for f in ROOT.glob("*.md"):
                if not f.name.startswith("0a-portable-poetics-kernel"):
                    shutil.copy(f, d / f.name)
            (d / "0a-portable-poetics-kernel-v0_3_15.md").write_text("# Portable Poetics Kernel\nVersion: 0.3.15\n", encoding="utf-8")
            snap = load_snapshot(d, REG)
            req = normalize(Request(task="workshop", dial_trial=""), REG)
            p = resolve(req, REG, snap, "")
            self.assertTrue(any("needs 0a-portable-poetics-kernel 0.3.19" in e for e in p.errors))
            self.assertTrue(any("13-speaker-dials needs 0a-portable-poetics-kernel 0.3.16" in e for e in p.errors))

    def test_deterministic(self):
        a = plan_for(task="workshop", voices=["TARE"], dial_trial="x", plugins=["Gilson"])
        b = plan_for(task="workshop", voices=["TARE"], dial_trial="x", plugins=["Gilson"])
        self.assertEqual([(f.stem, f.sha256) for f in a.files], [(f.stem, f.sha256) for f in b.files])


class RequestLineTests(unittest.TestCase):
    def line(self, **kw):
        return render_request_line(normalize(Request(**kw), REG), REG)

    def test_reading_forms(self):
        self.assertEqual(self.line(task="quick-read"), "Quick read.")
        self.assertEqual(self.line(task="sidecar"), "Full sidecar. ASSAY verdict.")
        self.assertEqual(self.line(task="triangulate", voices=["PLUMB", "DATUM"], verdict="PLUMB"),
                         "Triangulate PLUMB and DATUM. PLUMB closes.")
        self.assertEqual(self.line(task="sidecar", voices=["ASSAY"], counter_voices=["TARE"]),
                         "Full sidecar. Add TARE as counter-voice.")
        self.assertEqual(self.line(task="sidecar", voices=["PLUMB"], vise=True),
                         "Full sidecar. PLUMB verdict. VISE verdict, PLUMB spine.")
        self.assertEqual(self.line(task="datum", account=True), "DATUM verdict on the poem and its note.")
        self.assertEqual(self.line(task="poetics-scan"), "Poetics scan.")
        self.assertEqual(self.line(task="sidecar", kind="label"),
                         "Full sidecar. ASSAY verdict. Read as found. Kind: label. Unit: line.")

    def test_scan_forms(self):
        self.assertEqual(self.line(task="scan", scan_source="canon", scan_category="A", scan_devices=["apostrophe"]),
                         "Scan canon A for apostrophe")
        self.assertEqual(self.line(task="scan", scan_source="supplied", scan_devices=["caesura", "enjambment"], scan_or=True),
                         "Scan supplied for caesura or enjambment")
        with self.assertRaises(RegistryError):
            self.line(task="scan", scan_devices=["caesura"])  # no source flag

    def test_workshop_forms(self):
        self.assertEqual(self.line(task="workshop"), "workshop this specimen")
        self.assertEqual(self.line(task="workshop", kind="news report"), "jig as news report")
        self.assertEqual(self.line(task="workshop", rewrite_under=["axis: upward"], ars_poetica=True,
                                   dial_trial="idiom density", rewrite_at=["diction altitude:high"],
                                   contrast_at="caesura", feedback_bridge=True, ask="keep it short").split("\n"),
                         ["workshop this specimen", "rewrite under axis: upward", "+ ars poetica",
                          "dial trial: idiom density", "rewrite at diction altitude: high",
                          "contrast at: caesura", "feedback bridge", "keep it short"])
        self.assertEqual(self.line(task="workshop", rewrites=False, no_dial_trials=True).split("\n"),
                         ["workshop this specimen", "no rewrites", "no dial trials"])


class CatalogTests(unittest.TestCase):
    def test_device_counts(self):
        cats = {c["category"]: c["devices"] for c in catalog.categories(SNAP)}
        self.assertEqual(cats, {"A": 24, "B": 30, "C": 30, "D": 33, "E": 33, "F": 20, "G": 22})
        self.assertEqual(len(catalog.devices(SNAP)), 192)
        self.assertEqual(catalog.find_device(SNAP, "apostrophe")[0]["category"], "A")

    def test_confinements(self):
        rows = catalog.confinements(SNAP)
        self.assertEqual(len(rows), 194)
        self.assertEqual(sum(r["class"] == "composite" for r in rows), 57)
        self.assertEqual(sum(r["class"] == "primitive" for r in rows), 137)
        by_axis = {a: len(catalog.filter_confinements(rows, axis=a, klass="composite"))
                   for a in ("upward", "sideways", "inward", "outward")}
        self.assertEqual(by_axis, {"upward": 13, "sideways": 17, "inward": 12, "outward": 15})
        ap = catalog.filter_confinements(rows, handle="Apple-Picking")
        self.assertIn("cf-ap-04", [r["id"] for r in ap])

    def test_dials(self):
        d = catalog.dials(SNAP)
        self.assertEqual([x["id"] for x in d], [f"sd-0{i}" for i in range(1, 10)])
        self.assertEqual(sum(x["status"] == "established" for x in d), 4)
        self.assertEqual(d[1]["checks"], "open-or-corner, gating")

    def test_directives(self):
        d = catalog.directives(SNAP)
        self.assertEqual(len(d), 21)
        self.assertEqual(d[0]["name"], "Floor-Origin Hypothesis")
        self.assertTrue(d[0]["prompt"].startswith("Where does the poem claim legitimacy"))
        self.assertEqual(d[-1]["name"], "Access-Asymmetry Mode")

    def test_regression_tests(self):
        t = catalog.regression_tests(ROOT / "regression")
        self.assertEqual(len(t), 14)
        self.assertEqual([x for x in t if x["id"] == "R10-A"][0]["withheld"], ["0c-voice-designations"])
        self.assertEqual([x for x in t if x["id"] == "R9"][0]["specimen"], "(none)")


class LintTests(unittest.TestCase):
    def test_lint_on_bundle(self):
        findings = lint(REG, SNAP, ROOT / "regression")
        self.assertFalse([f for f in findings if f.level == "error"], [str(f) for f in findings])
        msgs = " ".join(f.message for f in findings)
        # the README's Registry Gaps, reproduced
        self.assertIn("7a-nom-function-battery", msgs)
        self.assertIn("full-monty-santos-small-branch-example", msgs)

    def test_lint_catches_header_filename_disagreement(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for f in ROOT.glob("*.md"):
                shutil.copy(f, d / f.name)
            (d / "8-frye-extraction-v0_6.md").write_text("# FRYE\nVersion: 0.5\n", encoding="utf-8")
            snap = load_snapshot(d, REG)
            errs = [f for f in lint(REG, snap) if f.level == "error"]
            self.assertTrue(any("header says 0.5, file name says 0.6" in f.message for f in errs))


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli.main(["--framework", str(ROOT), *argv])
        return code, out.getvalue(), err.getvalue()

    def test_explain_json(self):
        code, out, _ = self.run_cli("explain", "read", "--triangulate", "--voices", "ASSAY", "PLUMB", "--json")
        self.assertEqual(code, 0)
        d = json.loads(out)
        self.assertEqual(d["request_line"], "Triangulate ASSAY and PLUMB.")
        self.assertIn("2-harris-voice-module", [f["stem"] for f in d["files"]])

    def test_global_flag_after_subcommand(self):
        code, out, _ = self.run_cli("list", "categories", "--json")
        self.assertEqual(code, 0)
        self.assertEqual(len(json.loads(out)), 7)

    def test_bad_voice_exits_2(self):
        code, _, err = self.run_cli("explain", "read", "--voices", "MUSE")
        self.assertEqual(code, 2)
        self.assertIn("unknown voice", err)

    def test_over_budget_exits_1(self):
        code, out, _ = self.run_cli("explain", "read", "--max-tokens", "1000")
        self.assertEqual(code, 1)
        self.assertIn("exceeds --max-tokens", out)

    def test_compile_needs_specimen(self):
        code, _, err = self.run_cli("read", "--quick", "--out", str(self.tmp / "none"))
        self.assertEqual(code, 2)
        self.assertIn("no specimen", err)
        self.assertFalse((self.tmp / "none").exists())

    def test_lint(self):
        code, out, _ = self.run_cli("lint")
        self.assertEqual(code, 0)
        self.assertIn("0 errors", out)


DRAFT = """Title: Kitchen, 6 a.m.
Author: the user

The kettle clicks before the light does.
I count the spoons back into the drawer.

Outside the bin lorry takes the week.
"""

TYGER = ROOT / "regression" / "tests" / "R1" / "specimen.txt"


class CompileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.draft = self.tmp / "draft.txt"
        self.draft.write_text(DRAFT, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def compile(self, specimens=None, **kw):
        plan = plan_for(**kw)
        return build(plan, REG, SNAP, specimens or [], part_size=kw.get("part_size"))

    def test_split_meta(self):
        meta, body = split_meta(DRAFT)
        self.assertEqual(meta, {"title": "Kitchen, 6 a.m.", "author": "the user"})
        self.assertTrue(body.startswith("The kettle"))
        self.assertEqual(split_meta("just text\nno header\n"), ({}, "just text\nno header\n"))
        self.assertEqual(split_meta("Title: x\nno blank line after\n"), ({}, "Title: x\nno blank line after\n"))

    def test_text_only(self):
        bad = self.tmp / "img.png"
        bad.write_bytes(bytes([0x89, 0x50, 0x4E, 0x47, 0, 0xFF]))
        with self.assertRaises(CompileError):
            load_specimen(bad, "specimen", {})
        with self.assertRaises(CompileError):
            load_specimen(self.tmp / "missing.txt", "specimen", {})

    def test_prompt_shape(self):
        sp = load_specimen(TYGER, "specimen", {"title": "The Tyger", "author": "William Blake"})
        b = self.compile([sp], task="quick-read")
        self.assertEqual([n for n, _ in b.parts], ["prompt.md"])
        text = b.parts[0][1]
        order = [text.index(x) for x in ("LOAD SET", "FRAMEWORK FILE 1: 0a-portable", "FRAMEWORK FILE 2: 0c-voice",
                                          "SPECIMEN: The Tyger", "Tyger! Tyger!", "LOAD SET, REPEATED",
                                          "OPERATOR REQUEST", "Quick read.")]
        self.assertEqual(order, sorted(order))
        kernel_row = [f for f in b.manifest["files"] if f["stem"] == "0a-portable-poetics-kernel"][0]
        self.assertEqual(text.count(kernel_row["sha256"][:16]), 2)  # top table and the repeat
        self.assertNotIn("\r", text)
        self.assertIn(f"sha256 {sp.sha256[:16]}", text)
        self.assertEqual(sp.sha256, "f115345237e15c49116904ea7f3bde94ccf6688012c325e0c828132e351777cb")
        self.assertEqual(b.manifest["specimens"][0]["meta"]["author"], "William Blake")
        self.assertEqual(len(b.manifest["files"]), 3)

    def test_fence_longer_than_payload_runs(self):
        sp = Specimen(path="x", text="a ```` b", sha256="0" * 64, meta={"title": "t"})
        text = self.compile([sp], task="quick-read").parts[0][1]
        self.assertIn("`````text\na ```` b\n`````", text)

    def test_workshop_card_defaults(self):
        sp = load_specimen(self.draft, "specimen", {})
        text = self.compile([sp], task="workshop").parts[0][1]
        self.assertIn("Provenance: the user's own draft", text)
        self.assertIn("Copyright:  the user's", text)
        self.assertIn("Length:     3 lines", text)
        report = self.tmp / "r.txt"
        report.write_text("Title: Bridge\n\nPara one.\n\nPara two.\n", encoding="utf-8")
        sp = load_specimen(report, "specimen", {})
        text = self.compile([sp], task="workshop", kind="news report").parts[0][1]
        self.assertIn("Author:     unknown", text)
        self.assertIn("Copyright:  unknown", text)
        self.assertIn("Found by:   the user", text)
        self.assertIn("Length:     2 paragraphs", text)
        self.assertIn("jig as news report", text)

    def test_account_and_corpus_sections(self):
        acct = self.tmp / "a.txt"
        acct.write_text("Author's note: written in one sitting.", encoding="utf-8")
        sps = [load_specimen(self.draft, "specimen", {}), load_specimen(acct, "account", {})]
        text = self.compile(sps, task="datum", account=True).parts[0][1]
        self.assertIn("ACCOUNT: the poet's account", text)
        self.assertLess(text.index("SPECIMEN:"), text.index("ACCOUNT:"))
        self.assertLess(text.index("ACCOUNT:"), text.index("OPERATOR REQUEST"))
        corp = [load_specimen(self.draft, "corpus", {})]
        text = self.compile(corp, task="scan", scan_source="supplied", scan_devices=["caesura"]).parts[0][1]
        self.assertIn("SUPPLIED CORPUS 1 OF 1", text)
        with self.assertRaises(CompileError):
            self.compile([], task="scan", scan_source="supplied", scan_devices=["caesura"])
        self.compile([], task="scan", scan_source="canon", scan_devices=["caesura"])  # canon needs no text

    def test_split_at_file_boundaries(self):
        sp = load_specimen(self.draft, "specimen", {})
        plan = plan_for(task="quick-read")
        b = build(plan, REG, SNAP, [sp], part_size=60_000)
        names = [n for n, _ in b.parts]
        self.assertEqual(names, ["prompt-part1of3.md", "prompt-part2of3.md", "prompt-part3of3.md"])
        joined = "".join(c for _, c in b.parts)
        self.assertEqual(joined.count("FRAMEWORK FILE"), 3)
        for _, c in b.parts:
            self.assertTrue(c.startswith("<!-- dr: part"))
        self.assertEqual(b.manifest["parts"][0]["sha256"], b.manifest["parts"][0]["sha256"])

    def test_refuses_bad_plan(self):
        sp = load_specimen(self.draft, "specimen", {})
        plan = plan_for(task="sidecar", max_tokens=1000)
        with self.assertRaises(CompileError):
            build(plan, REG, SNAP, [sp])

    def test_deterministic_output(self):
        sp = load_specimen(self.draft, "specimen", {})
        a = self.compile([sp], task="quick-read").manifest["parts"][0]["sha256"]
        b = self.compile([sp], task="quick-read").manifest["parts"][0]["sha256"]
        self.assertEqual(a, b)

    def test_write(self):
        sp = load_specimen(self.draft, "specimen", {})
        b = self.compile([sp], task="quick-read")
        written = write(b, self.tmp / "out")
        self.assertEqual([p.name for p in written], ["prompt.md", "build-manifest.json"])
        m = json.loads((self.tmp / "out" / "build-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(m["request_line"], "Quick read.")
        self.assertEqual(m["generator_version"], cli.__version__)


class CliCompileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "draft.txt").write_text(DRAFT, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli.main(["--framework", str(ROOT), *argv])
        return code, out.getvalue(), err.getvalue()

    def test_end_to_end(self):
        code, out, err = self.run_cli("read", "--quick", "--specimen", str(self.tmp / "draft.txt"),
                                      "--copyright", "the user's", "--out", str(self.tmp / "run"))
        self.assertEqual(code, 0, err)
        self.assertIn("Wrote 2 files", out)
        prompt = (self.tmp / "run" / "prompt.md").read_text(encoding="utf-8")
        self.assertRegex(prompt, r"Source status: +the user's")
        self.assertTrue(prompt.rstrip().endswith("Quick read."))

    def test_author_collision_warning_in_output(self):
        code, out, _ = self.run_cli("workshop", "--specimen", str(self.tmp / "draft.txt"), "--author", "Steve Kowit",
                                    "--out", str(self.tmp / "run"))
        self.assertEqual(code, 0)
        self.assertIn("calibrates TARE, JIG", out)

    def test_over_budget_writes_nothing(self):
        code, _, err = self.run_cli("read", "--specimen", str(self.tmp / "draft.txt"), "--max-tokens", "1000",
                                    "--out", str(self.tmp / "run"))
        self.assertEqual(code, 1)
        self.assertIn("Nothing written", err)
        self.assertFalse((self.tmp / "run").exists())

    def test_multi_specimen_metadata_conflict(self):
        code, _, err = self.run_cli("read", "--quick", "--specimen", str(self.tmp / "draft.txt"),
                                    "--specimen", str(TYGER), "--title", "x", "--out", str(self.tmp / "run"))
        self.assertEqual(code, 2)
        self.assertIn("header block", err)


REG_DIR = ROOT / "regression"
MODELS = {"reader": "X", "evaluator": "Y", "adjudicator": "Z"}


class RegressTests(unittest.TestCase):
    def test_every_case_loads(self):
        for d in sorted((REG_DIR / "tests").iterdir()):
            case = load_case(REG_DIR, d.name, REG, SNAP)
            self.assertTrue(case.ok, (d.name, case.plan.errors, case.expect_errors))

    def test_fault_injection_cases(self):
        c = load_case(REG_DIR, "R10-D", REG, SNAP)
        self.assertEqual(c.plan.withheld, ["2-harris-voice-module"])
        self.assertNotIn("2-harris-voice-module", c.plan.stems())
        self.assertIn("1-rother-voice-module", c.plan.stems())
        c = load_case(REG_DIR, "R10-C", REG, SNAP)
        self.assertNotIn("11-provenance-grading-extension", c.plan.stems())
        self.assertIn("2-harris-voice-module", c.plan.stems())

    def test_r9_is_a_text_canon_scan(self):
        c = load_case(REG_DIR, "R9", REG, SNAP)
        self.assertIsNone(c.specimen)
        self.assertEqual(c.request_line, "Scan canon A for apostrophe")
        self.assertEqual(set(c.plan.stems()), {"0-poetics-boot-hollow", "0a-portable-poetics-kernel",
                                              "0c-voice-designations", "7-device-inventory-extended"})
        self.assertFalse((REG_DIR / "tests" / "R9" / "specimen.png").exists())

    def test_voice_and_mode_coverage(self):
        """Every voice and both modes are loaded by at least one case."""
        loaded = set()
        for d in sorted((REG_DIR / "tests").iterdir()):
            if (d / "manifest.json").is_file():
                loaded |= set(load_case(REG_DIR, d.name, REG, SNAP).plan.stems())
        for v in REG.voices.values():
            self.assertIn(v["module"], loaded, v["module"])
        self.assertIn(REG.modes["VISE"]["module"], loaded)

    def test_r11_account(self):
        c = load_case(REG_DIR, "R11", REG, SNAP)
        self.assertIsNotNone(c.account)
        self.assertEqual(c.account.sha256, c.manifest["account"]["sha256"])
        self.assertEqual(c.specimen.sha256, load_case(REG_DIR, "R7", REG, SNAP).specimen.sha256)
        self.assertIn("5-hersh-voice-module", c.plan.stems())
        self.assertNotIn("7-device-inventory-extended", c.plan.stems())
        _, prompts, man = compile_cases(["R11"], REG_DIR, REG, SNAP, MODELS)
        r = prompts["reader-prompt.md"]
        self.assertIn("R11: ACCOUNT: The Philosophy of Composition", r)
        self.assertIn("Charles Dickens, in a note now lying before me", r)
        self.assertLess(r.index("R11: SPECIMEN:"), r.index("R11: ACCOUNT:"))
        self.assertLess(r.index("R11: ACCOUNT:"), r.index("R11: LOAD SET, REPEATED"))
        self.assertEqual(man["cases"]["R11"]["account_sha256"], c.account.sha256)
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "regression"
            shutil.copytree(REG_DIR, d)
            (d / "tests" / "R11" / "account.txt").write_text("tampered", encoding="utf-8")
            with self.assertRaises(RegressionError):
                load_case(d, "R11", REG, SNAP)

    def test_specimen_pin(self):
        c = load_case(REG_DIR, "R1", REG, SNAP)
        self.assertEqual(c.specimen.sha256, c.manifest["specimen"]["sha256"])
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "regression"
            shutil.copytree(REG_DIR, d)
            (d / "tests" / "R1" / "specimen.txt").write_text("tampered", encoding="utf-8")
            with self.assertRaises(RegressionError) as cm:
                load_case(d, "R1", REG, SNAP)
            self.assertIn("frozen", str(cm.exception))

    def test_expect_gate(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "regression"
            shutil.copytree(REG_DIR, d)
            mp = d / "tests" / "R2" / "manifest.json"
            m = json.loads(mp.read_text(encoding="utf-8"))
            m["request"]["withhold"] = ["7-device-inventory-extended"]
            mp.write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")
            c = load_case(d, "R2", REG, SNAP)
            self.assertFalse(c.ok)
            self.assertTrue(any("expected 7-device-inventory-extended loaded" in e for e in c.expect_errors))
            with self.assertRaises(RegressionError):
                compile_cases(["R2"], d, REG, SNAP, MODELS)

    def test_reader_manifest_hides_scoring(self):
        c = load_case(REG_DIR, "R1", REG, SNAP)
        rm = reader_manifest(c.manifest)
        self.assertIn("request", rm)
        self.assertNotIn("scoring", rm)
        self.assertNotIn("evaluator", rm)
        self.assertNotIn("expect", rm)

    def test_role_prompts(self):
        cases, prompts, man = compile_cases(["R10-A"], REG_DIR, REG, SNAP, MODELS)
        self.assertEqual(sorted(prompts), ["adjudicator-prompt.md", "evaluator-prompt.md", "reader-prompt.md"])
        r, e, a = prompts["reader-prompt.md"], prompts["evaluator-prompt.md"], prompts["adjudicator-prompt.md"]
        for t in (r, e, a):
            self.assertIn("R10-A: WITHHELD FILES", t)
            self.assertIn("- `0c-voice-designations`", t)
            self.assertIn("R10-A: LOAD SET, REPEATED", t)
            self.assertIn("Withheld from this condition: `0c-voice-designations`", t)
            self.assertLess(t.index("R10-A: LOAD SET, REPEATED"), t.index("R10-A: OPERATOR REQUEST"))
            self.assertNotIn("FRAMEWORK FILE 2: 0c-voice-designations", t)
            self.assertIn("R10-A: SPECIMEN: The Tyger", t)
            self.assertIn("R10-A: OPERATOR REQUEST", t)
            self.assertNotIn("\r", t)
        self.assertNotIn("CANONICAL REGRESSION SUITE", r)
        self.assertNotIn("scoring", r.split("R10-A: LOAD SET")[0].split("CONDITION MANIFEST")[1])
        self.assertIn("CANONICAL REGRESSION SUITE", e)
        self.assertIn("RAW READER OUTPUT", e)
        self.assertNotIn("INDEPENDENT EVALUATOR REPORT", e)
        self.assertIn("INDEPENDENT EVALUATOR REPORT", a)
        self.assertIn("[PASTE THE COMPLETE RAW READER OUTPUT HERE", a)
        self.assertEqual(man["cases"]["R10-A"]["withheld"], ["0c-voice-designations"])
        self.assertEqual(man["multi_case_context_warning"], "Single-case prompt: no cross-case context exposure.")

    def test_outputs_embedded(self):
        _, prompts, man = compile_cases(["R1"], REG_DIR, REG, SNAP, MODELS,
                                        reader_output="READER SAYS X", evaluator_output="EVAL SAYS Y")
        self.assertIn("READER SAYS X", prompts["evaluator-prompt.md"])
        self.assertIn("EVAL SAYS Y", prompts["adjudicator-prompt.md"])
        self.assertNotIn("[PASTE", prompts["adjudicator-prompt.md"])
        self.assertEqual(man["handoff_slots"]["evaluator"], "reader output embedded")

    def test_multi_case_and_determinism(self):
        _, p1, m1 = compile_cases(["R1", "R3"], REG_DIR, REG, SNAP, MODELS)
        _, p2, m2 = compile_cases(["R1", "R3"], REG_DIR, REG, SNAP, MODELS)
        self.assertEqual(m1["prompt_sha256"], m2["prompt_sha256"])
        self.assertIn("more than one case", p1["reader-prompt.md"])
        with self.assertRaises(RegressionError):
            compile_cases(["R1", "R1"], REG_DIR, REG, SNAP, MODELS)
        with self.assertRaises(RegressionError):
            compile_cases(["R99"], REG_DIR, REG, SNAP, MODELS)

    def test_write(self):
        with tempfile.TemporaryDirectory() as td:
            _, prompts, man = compile_cases(["R9"], REG_DIR, REG, SNAP, MODELS)
            written = write_regression(Path(td), prompts, man)
            self.assertEqual([p.name for p in written],
                             ["reader-prompt.md", "evaluator-prompt.md", "adjudicator-prompt.md", "build-manifest.json"])

    def test_cli_regress(self):
        out, err = io.StringIO(), io.StringIO()
        with tempfile.TemporaryDirectory() as td:
            with redirect_stdout(out), redirect_stderr(err):
                code = cli.main(["--framework", str(ROOT), "regress", "--cases", "R9", "--out", td])
            self.assertEqual(code, 0, err.getvalue())
            self.assertIn("Scan canon A for apostrophe", out.getvalue())
            with redirect_stdout(out), redirect_stderr(err):
                code = cli.main(["--framework", str(ROOT), "regress", "--explain", "--cases", "R10-B"])
            self.assertEqual(code, 0)
            self.assertIn("Withheld (fault injection): 7-device-inventory-extended", out.getvalue())


class GoldenTests(unittest.TestCase):
    """Pinned load sets. A change here is a change to what a task or a case loads;
    review it, then run tests/update_golden.py."""

    def setUp(self):
        self.golden = json.loads((ROOT / "tests" / "golden.json").read_text(encoding="utf-8"))

    def test_task_load_sets(self):
        sys.path.insert(0, str(ROOT / "tests"))
        from update_golden import TASK_PROBES
        for name, kw in TASK_PROBES.items():
            req = normalize(Request(task=name, **kw), REG)
            line = render_request_line(req, REG)
            plan = resolve(req, REG, SNAP, line)
            self.assertEqual({"request_line": line, "stems": plan.stems()}, self.golden["tasks"][name], name)

    def test_regression_case_load_sets(self):
        seen = set()
        for d in sorted((REG_DIR / "tests").iterdir()):
            if not (d / "manifest.json").is_file():
                continue
            c = load_case(REG_DIR, d.name, REG, SNAP)
            seen.add(c.id)
            self.assertEqual({"request_line": c.request_line, "stems": c.plan.stems(), "withheld": c.plan.withheld},
                             self.golden["regression_cases"][c.id], c.id)
        self.assertEqual(seen, set(self.golden["regression_cases"]))


class DriftTests(unittest.TestCase):
    def test_readme_agrees_with_disk_and_registry(self):
        findings = [f for f in lint(REG, SNAP) if f.check == "readme"]
        self.assertEqual(findings, [], [str(f) for f in findings])

    def test_readme_check_fires(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for f in ROOT.glob("*.md"):
                shutil.copy(f, d / f.name)
            t = (d / "README.md").read_text(encoding="utf-8")
            t = t.replace("| `0c-voice-designations` | 0.7 |", "| `0c-voice-designations` | 0.6 |")
            t = t.replace("| Quick reading | `0a`, `0c` |", "| Quick reading | `0a`, `0c`, `7` |")
            (d / "README.md").write_text(t, encoding="utf-8")
            msgs = [f.message for f in lint(REG, load_snapshot(d, REG)) if f.check == "readme"]
            self.assertTrue(any("0c-voice-designations at 0.6" in m for m in msgs), msgs)
            self.assertTrue(any("task 'Quick reading'" in m for m in msgs), msgs)

    def test_registry_schema(self):
        raw = REG.raw
        for stem, spec in raw["modules"].items():
            self.assertIn("type", spec, stem)
            self.assertIn("load_step", spec, stem)
            self.assertIn("loadable", spec, stem)
            if spec["type"] == "plugin":
                self.assertIn("handle", spec, stem)
                self.assertEqual(spec["load_step"], 7, stem)
            if spec["type"] == "voice":
                self.assertIn("designation", spec, stem)
                self.assertIn("0c-voice-designations", spec.get("requires", []), stem)
        for t in REG.tasks.values():
            for stem in t.modules:
                self.assertTrue(REG.modules[stem].loadable, (t.name, stem))
        self.assertEqual(set(REG.voices), {"ASSAY", "PLUMB", "TARE", "RETICLE", "DATUM"})
        self.assertEqual(set(REG.modes), {"VISE", "JIG"})

    def test_sources_parse_as_python39(self):
        for f in list((ROOT / "dr").glob("*.py")) + list((ROOT / "tests").glob("*.py")) \
                + [ROOT / "regression" / "generate_prompts.py"]:
            ast.parse(f.read_text(encoding="utf-8"), filename=str(f), feature_version=(3, 9))


class RobustnessTests(unittest.TestCase):
    def test_help_renders_for_every_subcommand(self):
        for argv in (["--help"], ["read", "--help"], ["workshop", "--help"], ["scan", "--help"],
                     ["extract", "--help"], ["explain", "read", "--help"], ["list", "--help"],
                     ["lint", "--help"], ["regress", "--help"]):
            out = io.StringIO()
            with redirect_stdout(out), self.assertRaises(SystemExit) as cm:
                cli.main(argv)
            self.assertEqual(cm.exception.code, 0, argv)
            self.assertIn("usage:", out.getvalue())

    def test_non_ascii_round_trip(self):
        text = "Title: Bánh trôi nước\nAuthor: Hồ Xuân Hương\n\nThân em vừa trắng lại vừa tròn\n"
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "sp.txt"
            f.write_text(text, encoding="utf-8")
            sp = load_specimen(f, "specimen", {})
            self.assertEqual(sp.meta["author"], "Hồ Xuân Hương")
            b = build(plan_for(task="quick-read"), REG, SNAP, [sp])
            prompt = b.parts[0][1]
            self.assertIn("Thân em vừa trắng lại vừa tròn", prompt)
            self.assertRegex(prompt, r"Author: +Hồ Xuân Hương")
            written = write(b, Path(td) / "out")
            self.assertIn("Hồ Xuân Hương", written[0].read_text(encoding="utf-8"))

    def test_catalog_text_keeps_diacritics(self):
        self.assertTrue(any("Nôm" in d["definition"] or "Nôm" in d["device"] for d in catalog.devices(SNAP)))

    def test_fence_escaping_at_every_run_length(self):
        from dr.compile import fence
        for n in range(1, 8):
            payload = "a " + "`" * n + " b"
            out = fence(payload)
            opener = out.split("\n", 1)[0]
            ticks = len(opener) - len(opener.lstrip("`"))
            self.assertGreater(ticks, n)
            self.assertTrue(out.rstrip().endswith("`" * ticks))

    def test_shim_forwards_to_regress(self):
        with tempfile.TemporaryDirectory() as td:
            r = subprocess.run([sys.executable, str(ROOT / "regression" / "generate_prompts.py"),
                                "--cases", "R9", "--out", td, "--framework", str(ROOT)],
                               capture_output=True, text=True, cwd=td)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((Path(td) / "reader-prompt.md").is_file())

    def test_explain_matches_compile(self):
        """The plan explain prints is the plan compile embeds."""
        out = io.StringIO()
        with redirect_stdout(out):
            cli.main(["--framework", str(ROOT), "explain", "workshop", "--dial-trial", "--json"])
        explained = [f["stem"] for f in json.loads(out.getvalue())["files"]]
        plan = plan_for(task="workshop", dial_trial="")
        self.assertEqual(explained, plan.stems())


if __name__ == "__main__":
    unittest.main()
