\
#!/usr/bin/env python3
"""Build isolated target-condition ZIPs from this repository snapshot.

Run from the repository root:
  python regression/build_condition_packages.py

The script excludes test-control documents and all other regression folders from
runtime packages. It includes only the selected condition's manifest, target
prompt, and specimen. For R10, it removes the explicitly withheld file and
verifies that it is absent from the resulting ZIP.
"""
from pathlib import Path
import json, zipfile, hashlib

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "regression"
OUT = REG / "packages"
OUT.mkdir(exist_ok=True)
EXCLUDE = {
    "regression-suite-v0_5.md",
    "prompt-regime-v0_1.md",
    "regression/regression-suite-v0_5.md",
    "regression/prompt-regime-v0_1.md",
    "diagnostic-reader-regression-suite-v0_5.md",
    "diagnostic-reader-prompt-regime-v0_1.md",
    "README.md",
    "session-record-2026-10-08.md",
}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

for test_dir in sorted((REG / "tests").iterdir()):
    if not test_dir.is_dir():
        continue
    manifest_path = test_dir / "manifest.json"
    if not manifest_path.exists():
        continue
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    tid = manifest["test_id"]
    withheld = set(manifest.get("withheld_files", []))
    outpath = OUT / f"target-{tid}.zip"
    with zipfile.ZipFile(outpath, "w", zipfile.ZIP_DEFLATED) as z:
        # Runtime apparatus files only; regression controls are not runtime modules.
        for p in sorted(ROOT.rglob("*")):
            if not p.is_file() or REG in p.parents:
                continue
            if p.name in EXCLUDE or p.name in withheld:
                continue
            z.write(p, p.relative_to(ROOT).as_posix())
        # Include the exact test-control documents for auditability.
        # These are controls/reference documents, not Diagnostic Reader runtime modules.
        for name in ["regression-suite-v0_5.md", "prompt-regime-v0_1.md"]:
            p = REG / name
            if not p.exists():
                raise FileNotFoundError(f"Required regression control document missing: {p}")
            z.write(p, f"regression/{name}")
        # Only this test's run controls go to the package root.
        for name in ["manifest.json", "target-prompt.md", "specimen.txt", "specimen.png"]:
            p = test_dir / name
            if p.exists():
                z.write(p, name)
    with zipfile.ZipFile(outpath) as z:
        packaged = z.namelist()
        required_controls = {
            "regression/regression-suite-v0_5.md",
            "regression/prompt-regime-v0_1.md",
        }
        missing_controls = sorted(required_controls - set(packaged))
        if missing_controls:
            raise RuntimeError(f"{tid}: missing control document(s): {missing_controls}")
        missing = [f for f in withheld if any(Path(n).name == f for n in packaged)]
        if missing:
            raise RuntimeError(f"{tid}: withheld file(s) present in package: {missing}")
    print(f"{outpath.name}\t{outpath.stat().st_size}\tsha256={sha256(outpath)}")
print("NOTE: packages were built from the current framework snapshot and the supplied specimen files. Verify specimen source/hash metadata in each manifest before treating runs as scored benchmark results.")
