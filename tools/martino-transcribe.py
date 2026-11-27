#!/usr/bin/env python3
"""Tool 1 of 15-martino-extraction: letter-scale transcription.

Maps the twenty-six letters onto the seven natural notes, cycling, so that the alphabet
becomes the A-minor scale: A to G, then H begins again at A. Twenty-six letters make three
full passes of seven with five left over. A word then has a pitch sequence.

    python tools/martino-transcribe.py "Tyger Tyger burning bright"
    python tools/martino-transcribe.py --file regression/tests/R1/specimen.txt
    python tools/martino-transcribe.py COLTRANE TENOR --compact

This generates material, not findings. The mapping reads spelling, and English spelling is
not sound, so the output is not how the line sounds and no claim about the line's music
follows from it. Its use is to hand an ear a second object derived by a rule that does not
know what the poem means. See the extraction's Tool 1, "What It Can and Cannot Show".

Standard library only, Python 3.9 or later, same as the dr package.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

NATURALS = "ABCDEFG"
# Degrees are read against A minor, so A is 1. Martino: "the entire alphabet now became
# the A-minor scale."
DEGREE_NAME = {1: "i", 2: "ii", 3: "III", 4: "iv", 5: "v", 6: "VI", 7: "VII"}


def note_of(ch: str) -> str:
    return NATURALS[(ord(ch.upper()) - 65) % 7]


def transcribe(text: str):
    """[(letter, note, degree)] for the alphabetic characters in text."""
    return [(c, note_of(c), (ord(c.upper()) - 65) % 7 + 1) for c in text if c.isalpha()]


def contour(degrees) -> str:
    """Up, down, repeat, one character per step."""
    out = []
    for a, b in zip(degrees, degrees[1:]):
        out.append("=" if b == a else ("/" if b > a else "\\"))
    return "".join(out)


def staff(rows, width: int = 72) -> str:
    """A rough seven-line plot, highest degree at the top."""
    cells = rows[:width]
    lines = []
    for deg in range(7, 0, -1):
        row = "".join("o" if d == deg else "." for _, _, d in cells)
        lines.append(f"  {NATURALS[deg-1]} {DEGREE_NAME[deg]:>3} |{row}")
    lines.append("       " + " " + "".join(c.upper() for c, _, _ in cells))
    return "\n".join(lines)


def report(label: str, text: str, compact: bool) -> None:
    rows = transcribe(text)
    if not rows:
        print(f"{label}: no letters"); return
    notes = [n for _, n, _ in rows]
    degs = [d for _, _, d in rows]
    if compact:
        print(f"  {label:<34} {' '.join(notes)}")
        return
    print(f"\n{label}")
    print(f"  letters   {len(rows)}")
    print(f"  notes     {' '.join(notes)}")
    print(f"  degrees   {' '.join(str(d) for d in degs)}   (against A minor; A is i)")
    print(f"  contour   {contour(degs)}")
    print(f"  span      {max(degs) - min(degs) + 1} of 7")
    print(f"  lands on  {notes[-1]} ({DEGREE_NAME[degs[-1]]})"
          + ("   the tonic" if degs[-1] == 1 else "   not the tonic"))
    if len(rows) <= 72:
        print(staff(rows))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("text", nargs="*", help="words or a line, quoted")
    ap.add_argument("--file", type=Path, help="transcribe a text file line by line")
    ap.add_argument("--compact", action="store_true", help="one line of notes per input")
    ap.add_argument("--max-lines", type=int, default=12, help="with --file (default 12)")
    a = ap.parse_args(argv)

    if not a.text and not a.file:
        ap.print_help(); return 2

    if a.file:
        if not a.file.is_file():
            print(f"ERROR: no such file: {a.file}", file=sys.stderr); return 2
        lines = [l.strip() for l in a.file.read_text(encoding="utf-8").splitlines() if l.strip()]
        for line in lines[:a.max_lines]:
            report(line, line, a.compact or len(lines) > 1)
        if len(lines) > a.max_lines:
            print(f"\n  ... {len(lines) - a.max_lines} more lines; raise --max-lines")
    for t in a.text:
        report(t, t, a.compact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
