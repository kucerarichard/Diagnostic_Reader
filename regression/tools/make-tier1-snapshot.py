#!/usr/bin/env python3
"""Build a Tier 1 framework snapshot: voice module headers, no corpora.

Each voice module defines its own corpus loading tiers and names Tier 1, the analytical
header alone, as the ordinary deployment tier. The compiler has no tier lever and emits
Tier 3, the full corpus, for every run. This script writes a snapshot directory holding
every framework file with each voice module truncated at its own corpus marker, so
`dr --framework <snapshot>` compiles a Tier 1 condition.

    python regression/tools/make-tier1-snapshot.py
    python -m dr regress --cases R1 --framework tier1-snapshot --regression-dir regression

The second command needs --regression-dir, because --framework also relocates the case
lookup and the snapshot holds no regression directory.

Truncation applies to the five voice modules only. 4-gonzo-mode carries no corpus marker
and is copied whole, which is why R8 stays the largest case at Tier 1.

A Tier 1 condition is not the condition the suite pins. Each voice module's sha256
changes, so a Tier 1 run is a separate operating profile and its scores are not canonical
results for a case. Suite section 2 calls such a profile a compact configuration for
lower-capability models and requires it to be documented as empirically supported rather
than assumed interchangeable with the full configuration.

Standard library only, Python 3.9 or later, same as the dr package.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

# stem prefix -> the line its corpus begins at. Matched with startswith on a stripped line.
# Every file here declares its own tiers and names Tier 1 as the header alone. The workshop
# puts it plainest: "The tiering is a cost rule. Do not load the full corpus when the header
# carries the task."
CORPUS_MARKERS = {
    "1-rother-voice-module": "## BEGIN CORPUS:",
    "2-harris-voice-module": "## CORPUS —",
    "3-kowit-voice-module": "## Kowit Corpus.",
    "3-perloff-voice-module": "### MARJ OVERVIEW:",
    "5-hersh-voice-module": "## CORPUS —",
    "3a-workshop": "## Corpus Boundary",
    "4-gonzo-mode": "## Corpus Boundary",
}

NOTICE = """## CORPUS: NOT LOADED (TIER 1)

Corpus Loading Tier 1 is in force for this run: this module's analytical header only. The
module's own Corpus Loading Tiers section names Tier 1 the ordinary deployment tier. The
corpus below the marker is withheld by tier selection, not missing through a loading
fault, and its absence is the declared condition.

The module states that the corpus is the calibration. Any operation whose procedure needs
corpus passages runs at header fidelity only. Report that limitation. Do not reconstruct
corpus material from memory.

Withheld at this marker: `{marker}` and everything below it.
"""


def truncate(path: Path, marker: str) -> tuple:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    lines = text.split("\n")
    idx = next((i for i, line in enumerate(lines) if line.startswith(marker)), None)
    if idx is None:
        return (None, len(lines))
    kept = lines[:idx]
    path.write_text("\n".join(kept) + "\n" + NOTICE.format(marker=marker), encoding="utf-8")
    return (idx, len(lines))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--framework", type=Path, default=Path("."),
                    help="source bundle to copy from (default: the current directory)")
    ap.add_argument("--out", type=Path, default=Path("tier1-snapshot"),
                    help="snapshot directory to write (default: tier1-snapshot)")
    a = ap.parse_args(argv)

    src, dst = a.framework.resolve(), a.out.resolve()
    # Match by stem, never by versioned filename: the boot's version moves.
    if not any(src.glob("0-poetics-boot-hollow*.md")) or not any(src.glob("0a-portable-poetics-kernel*.md")):
        print(f"ERROR: {src} does not look like a framework bundle", file=sys.stderr)
        return 2
    if dst == src:
        print("ERROR: --out would overwrite the source bundle", file=sys.stderr)
        return 2

    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    copied = 0
    for f in sorted(src.glob("*.md")):
        shutil.copy2(f, dst / f.name)
        copied += 1

    print(f"copied {copied} markdown files to {dst}")
    missing = []
    for f in sorted(dst.glob("*.md")):
        stem = next((s for s in CORPUS_MARKERS if f.name.startswith(s)), None)
        if stem is None:
            continue
        idx, total = truncate(f, CORPUS_MARKERS[stem])
        if idx is None:
            missing.append(f.name)
            print(f"  WARN {f.name}: marker {CORPUS_MARKERS[stem]!r} not found; copied whole")
        else:
            print(f"  {f.name}: kept {idx} header lines of {total}")
    if missing:
        print("\nA missing marker means that module shipped a renamed corpus heading.",
              file=sys.stderr)
        print("Check the heading and update CORPUS_MARKERS before trusting the snapshot.",
              file=sys.stderr)
        return 1
    print(f"\nTier 1 snapshot ready. Compile against it with:\n"
          f"  python -m dr regress --cases R9 --framework {a.out} --regression-dir regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
