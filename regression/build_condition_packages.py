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
    specimen = manifest.get("specimen", {})
    specimen_path = test_dir / specimen.get("path", "specimen.txt")
    if not specimen_path.exists() or (specimen.get("status", "").startswith("BLOCKED")):
        print(f"SKIP {tid}: required specimen missing or blocked ({specimen.get('path', 'specimen.txt')})")
        continue
    expected_hash = specimen.get("sha256")
    if expected_hash and expected_hash != "REQUIRED: scan not supplied" and sha256(specimen_path) != expected_hash:
        raise RuntimeError(f"{tid}: specimen SHA-256 mismatch for {specimen_path}")
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
        # Only this test's run controls go to the target.
        for name in ["manifest.json", "target-prompt.md", "specimen.txt", "specimen.png"]:
            p = test_dir / name
            if p.exists():
                z.write(p, name)
    with zipfile.ZipFile(outpath) as z:
        packaged = z.namelist()
        missing = [f for f in withheld if any(Path(n).name == f for n in packaged)]
        if missing:
            raise RuntimeError(f"{tid}: withheld file(s) present in package: {missing}")
    print(f"{outpath.name}\t{outpath.stat().st_size}\tsha256={sha256(outpath)}")
print("NOTE: R9 is skipped until its scan specimen is supplied. Other specimens are frozen user-supplied transcriptions; bibliographic editions remain unverified.")
