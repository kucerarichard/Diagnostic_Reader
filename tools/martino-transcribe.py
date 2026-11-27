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
# The source sets A as 1: "the entire alphabet now became the A-minor scale." That is a
# choice, not a property of the letters. The seven natural notes are one set; which of them
# is called 1 picks a mode, moves the wrap, and changes the contour. --tonic exposes it.
PITCH_CLASS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
MODE = {"C": "Ionian (major)", "D": "Dorian", "E": "Phrygian", "F": "Lydian",
        "G": "Mixolydian", "A": "Aeolian (natural minor)", "B": "Locrian"}


def scale_of(tonic: str):
    """The seven naturals in order from the tonic."""
    i = NATURALS.index(tonic)
    return [NATURALS[(i + k) % 7] for k in range(7)]


def degree_names(tonic: str):
    """Roman numeral per degree, cased by the quality of the triad built on it."""
    sc = scale_of(tonic)
    names = {}
    for d in range(7):
        root, third, fifth = (PITCH_CLASS[sc[(d + k) % 7]] for k in (0, 2, 4))
        t, f = (third - root) % 12, (fifth - root) % 12
        num = "i ii iii iv v vi vii".split()[d]
        if (t, f) == (4, 7):
            names[d + 1] = num.upper()
        elif (t, f) == (3, 6):
            names[d + 1] = num + "o"   # diminished, in ASCII so any console renders it
        else:
            names[d + 1] = num
    return names


def note_of(ch: str) -> str:
    return NATURALS[(ord(ch.upper()) - 65) % 7]


def transcribe(text: str, tonic: str = "A"):
    """[(letter, note, degree)] for the alphabetic characters, degrees against tonic."""
    off = NATURALS.index(tonic)
    return [(c, note_of(c), ((ord(c.upper()) - 65) % 7 - off) % 7 + 1)
            for c in text if c.isalpha()]


def contour(degrees) -> str:
    """Up, down, repeat, one character per step.

    Relative to the tonic: the step from degree 7 to degree 1 prints as a fall because the
    scale is numbered as a line, and moving the tonic moves that wrap. Nothing here
    constrains register. The same degrees voice as steps or as sevenths depending on where
    the player puts each note, and that is the player's decision.
    """
    out = []
    for a, b in zip(degrees, degrees[1:]):
        out.append("=" if b == a else ("/" if b > a else "\\"))
    return "".join(out)


def staff(rows, tonic: str, width: int = 72) -> str:
    """A rough seven-line plot, highest degree at the top."""
    cells = rows[:width]
    sc, names = scale_of(tonic), degree_names(tonic)
    lines = []
    for deg in range(7, 0, -1):
        row = "".join("o" if d == deg else "." for _, _, d in cells)
        lines.append(f"  {sc[deg-1]} {names[deg]:>4} |{row}")
    lines.append("        " + " " + "".join(c.upper() for c, _, _ in cells))
    return "\n".join(lines)


def report(label: str, text: str, compact: bool, tonic: str = "A") -> None:
    rows = transcribe(text, tonic)
    if not rows:
        print(f"{label}: no letters"); return
    notes = [n for _, n, _ in rows]
    degs = [d for _, _, d in rows]
    if compact:
        print(f"  {label:<34} {' '.join(notes)}")
        return
    names = degree_names(tonic)
    print(f"\n{label}")
    print(f"  letters   {len(rows)}")
    print(f"  notes     {' '.join(notes)}")
    print(f"  degrees   {' '.join(str(d) for d in degs)}")
    print(f"  tonic     {tonic} is 1, so the mode is {MODE[tonic]}")
    print(f"  contour   {contour(degs)}")
    print(f"  span      {max(degs) - min(degs) + 1} of 7")
    print(f"  lands on  {notes[-1]} ({names[degs[-1]]})"
          + ("   the tonic" if degs[-1] == 1 else "   not the tonic"))
    if len(rows) <= 72:
        print(staff(rows, tonic))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("text", nargs="*", help="words or a line, quoted")
    ap.add_argument("--file", type=Path, help="transcribe a text file line by line")
    ap.add_argument("--compact", action="store_true", help="one line of notes per input")
    ap.add_argument("--tonic", default="A", type=lambda s: s.strip().upper(),
                    choices=list(NATURALS),
                    help="which natural note is degree 1 (default A, the source's choice). "
                         "Moving it picks a mode, moves the wrap, and changes the contour; "
                         "the notes themselves do not move")
    ap.add_argument("--max-lines", type=int, default=12, help="with --file (default 12)")
    a = ap.parse_args(argv)

    if not a.text and not a.file:
        ap.print_help(); return 2

    if a.file:
        if not a.file.is_file():
            print(f"ERROR: no such file: {a.file}", file=sys.stderr); return 2
        lines = [l.strip() for l in a.file.read_text(encoding="utf-8").splitlines() if l.strip()]
        for line in lines[:a.max_lines]:
            report(line, line, a.compact or len(lines) > 1, a.tonic)
        if len(lines) > a.max_lines:
            print(f"\n  ... {len(lines) - a.max_lines} more lines; raise --max-lines")
    for t in a.text:
        report(t, t, a.compact, a.tonic)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
