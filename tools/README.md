# tools

Scripts that run beside the compiler. Standard library only, Python 3.9 or later, like `dr`.
None of them calls a model. The regression harness has its own in `regression/tools/`.

| Script | Does |
|---|---|
| `run-card.py` | starts a RUN-CARD.md for a run directory, filled from the build manifests |
| `martino-transcribe.py` | Tool 1 of `15-martino-extraction`: letters to notes |

## run-card.py

```
python tools/run-card.py runs/2026-11-28-my-run
python tools/run-card.py runs/2026-11-28-my-run --force
```

`build-manifest.json` records the condition and nothing about the run. That is deliberate:
it carries no timestamp so that identical inputs produce an identical manifest. What it
therefore cannot carry is the command, the date, the repository state, which model executed
the prompt, and what that model was told beyond the prompt. Suite section 5 asks for all of
those, and without them a run is not reproducible by anyone who was not in the room.

The script fills what it can read from the manifests, including a reconstruction of the
command from the parsed request, and writes the rest as TODO lines. A card with TODO left in
it is an incomplete record.

The reconstructed command is close, not guaranteed verbatim. It is built from the request as
the compiler parsed it, so a flag that left no trace in the request does not come back.

The field most worth filling by hand is what the executor was told beyond the prompt. When a
prompt is handed to an agent rather than pasted into a chat, the surrounding instructions are
part of the condition, and they are recorded nowhere else at all.

Worked examples: `runs/2026-11-27-slab/RUN-CARD.md` and
`runs/2026-11-27-couriers/RUN-CARD.md`, both written by hand before this script existed.

## martino-transcribe.py

```
python tools/martino-transcribe.py COLTRANE TENOR --compact
python tools/martino-transcribe.py "Dare frame thy fearful symmetry" --tonic C
python tools/martino-transcribe.py --file path/to/specimen.txt --max-lines 4
```

The letter-scale mapping from `15-martino-extraction`, Tool 1. Maps the twenty-six letters
onto the seven natural notes, cycling, so a word has a pitch sequence. `--tonic` chooses
which natural note is degree 1 and defaults to A, the source's own setting; moving it picks a
mode, moves the wrap, and changes the contour, while the notes stay where they are.

It generates material, not findings. The mapping reads spelling, and English spelling is not
sound, so the output is not how a line sounds. The extraction's Tool 1 states what it can and
cannot show, and the failure mode to watch is treating a landing-note mismatch as a rhyme
finding when it is a spelling finding.
