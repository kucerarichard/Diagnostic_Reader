# Diagnostic Reader Regression Suite

Test definitions for the regression suite, compiled into reader prompts by `dr regress`. This directory holds no runtime module. The framework files are read from the repository root (or a snapshot you name), and nothing here calls a model.

The cases live under `regression/tests/R*/`. That is a different directory from `tests/` at the repository root, which holds the compiler's own unit tests and is run with `python -m unittest`; the two share a word and nothing else. A regression case is a condition for a language model; a unit test is an assertion about the `dr` package. See `tests/README.md` for the latter.

```
python -m dr regress --cases R1 --out run-R1
```

`regression/generate_prompts.py` forwards to the same command for scripts that still call it.

## Contents

| Path | Holds |
|---|---|
| `regression/tests/<R-ID>/manifest.json` | the condition: a `request` block the compiler resolves into a load set, an `expect` block, and the pinned specimen |
| `regression/tests/<R-ID>/target-prompt.md` | Reader instructions for the case |
| `regression/tests/<R-ID>/specimen.txt` | the frozen transcription; its sha256 is pinned in the manifest. R9 has none by design |
| `regression/tests/R11/account.txt` | the poet's account the DATUM reading measures the specimen against; pinned like the specimen |
| `regression-suite-v*.md`, `prompt-regime-v*.md` | control documents: scoring, procedure, test cards. Reference for the operator, not read by the compiler |
| `tools/` | scripts for a hand-run: the Tier 1 snapshot builder and the wrapper cutter. See `tools/README.md` |

## Output

`dr regress` writes two files:

| File | Contents |
|---|---|
| `reader-prompt.md` | per case: target instructions, a reader-facing manifest (no scoring material), the LOAD SET table, every framework file in the condition, the specimen with its card, the LOAD SET repeated with withheld files named, and the operator request line |
| `build-manifest.json` | selected cases, the reader model label, per-case request line, load set with sha256 per file, withheld list, specimen sha256, token estimate, and the prompt's sha256 |

Suite v0.7 removed the independent evaluator and the LLM adjudicator. One role is compiled; the operator reads the artifact against the case manifest and the criteria on its card in `prompt-regime`, Part II.

A working convention, one directory per run:

```
python -m dr regress --cases R1 --out runs/2026-11-24-R1-<model>
#   paste reader-prompt.md into the Reader; save its output as runs/.../reader-output.md
#   note which model you pasted into beside it; the prompt does not record it, by design
```

The directory then holds the condition (`build-manifest.json`, with every hash), the output, and the prompt. Commit the manifest and the output; the `.gitignore` drops the prompt files from `runs/`, since they regenerate from the manifest and each is several megabytes. The first thing to read in any `reader-output.md` is its loading report against the case's repeated LOAD SET.

For a run that does not mean pasting several hundred kilobytes by hand, see `tools/README.md`: the framework is attached as files and only the wrapper is pasted, which is about 3 percent of the prompt.

## Case manifests

The `request` block takes the same fields as the `dr` command line, so a case is a request the compiler resolves:

```json
"request": {
  "task": "triangulate",
  "voices": ["ASSAY", "PLUMB"],
  "extensions": ["provenance"],
  "withhold": ["2-harris-voice-module"]
},
"expect": {
  "loaded": ["1-rother-voice-module", "11-provenance-grading-extension"],
  "absent": ["2-harris-voice-module"]
}
```

`withhold` is the fault-injection hook: the stem is removed from the plan and listed under WITHHELD FILES in every role prompt. `expect` pins stems that must and must not be in the resolved plan, so a case that depends on a file being present or absent fails at compile time, with the plan printed, instead of in a model run. The specimen's pinned sha256 is checked on every compile; an edited transcription refuses to compile.

The load set is derived, never listed by hand. `python -m dr regress --explain --cases R10-C` prints it with the reason for each file.

## Conditions

| Case | Request | Framework set |
|---|---|---|
| R1, R2, R4 | `sidecar`, ASSAY | boot, kernel, `0c`, `7`, `1` (~222k tokens) |
| R3 | `triangulate` ASSAY and PLUMB, PLUMB closes | adds `2` (~355k) |
| R5 | `triangulate` ASSAY and RETICLE | adds `3-perloff` (~327k) |
| R6 | `triangulate` ASSAY and PLUMB | adds `2` (~355k) |
| R7 | `triangulate` ASSAY and TARE | adds `3-kowit` (~269k) |
| R8 | `sidecar` ASSAY, VISE verdict riding ASSAY, `11` loaded | adds `4`, `11` (~310k) |
| R9 | `scan canon A for apostrophe`, no specimen | boot, kernel, `0c`, `7` (~63k) |
| R10-A to D | `triangulate` ASSAY and PLUMB with `11`, one stem withheld | the R10 base less the withheld file |
| R11 | `datum`, The Raven against Poe's "The Philosophy of Composition" | boot, kernel, `0c`, `11`, `5` (~159k) |

Every voice and both modes are now under test somewhere: ASSAY throughout, PLUMB in R3, R6, and R10, RETICLE in R5, TARE in R7, DATUM in R11, VISE in R8, and JIG only implicitly, since the suite's corpus holds finished canonical poems and the workshop wants a draft. The dial file is the one extension no case loads; it rides the workshop.

The R10 base loads `11-provenance-grading-extension` explicitly so that R10-C has something to withhold; DATUM is not loaded there, because The Tyger carries no account for it to measure. R11 is the DATUM case: Poe's essay is the one text in the corpus that gives the voice a record, and it is a famously disputed one. The account is held at P2 and the target is scored on measuring it against the page, not on agreeing with received opinion about the essay.

Where a case names voices, whether a voice fires on the specimen is the test and not the premise; a justified stand-down passes.

R9 changed in this revision from an image-scan test to the canon-scan test the suite's section 12 defines. The harness is text only. The prompt regime's R9 card was rewritten to match; the suite's card was already right.

## Looking around the cases

Nothing here has been run. There is no baseline, no leaderboard, and no order you are supposed
to go in. A case is a question someone found interesting enough to freeze, and freezing it is
most of the work; running it is cheap and optional. Browse with the compiler, which consults no
model:

```
python -m dr list tests                                    the fourteen cases with their titles
python -m dr regress --explain --cases R9                  what R9 loads, and why each file is there
python -m dr regress --explain --cases R3 R6               two cases that load the same six files
```

Sizes below are Tier 1, the voice-module headers without their corpora, which is what
`regression/tools/make-tier1-snapshot.py` builds. Tier 3 is roughly three times larger and is
the condition the manifests pin.

### The Tyger, four ways

**R1** (72k, 5 files) asks the plainest question in the suite: given five files, does the
apparatus say which five it used? The trap is that the boot's Module Registry lists sixteen
modules whatever the condition, so a model that confuses an inventory with a load set will
report eleven files it never saw. Everything else in the suite depends on this one working.

**R2** (72k, 5 files) is the same five files and the same poem, asking instead whether devices
get named before they get interpreted. The device inventory holds 192 entries across seven
categories; the question is whether the reading reaches for one that fires on the page or one
that sounds right.

**R10-A to R10-D** (63k to 82k, 6 files) take The Tyger apart by removing one file at a time
from a two-voice triangulation. These are the most interesting cases in the suite and the
least like literary criticism. Each asks whether the apparatus notices an absence and switches
a procedure off, or quietly rebuilds the missing file from memory.

- **R10-A** withholds the designation layer. Narrower than it looks: the kernel's own Voice
  Slot Matrix still names all five designations, so a verdict labelled ASSAY remains possible.
  What actually goes missing is the leak-tier procedure and the calibration-collision rule, and
  the case is scored on whether that split gets reported.
- **R10-B** withholds the device inventory, leaving the kernel's Device Inventory Lite. Does the
  reading say so, or improvise an inventory and imply compliance?
- **R10-C** withholds the provenance-grading extension. Two things are absent here, which is the
  point: the extension itself, and DATUM, whose module this condition never loads although the
  boot and the designation layer both name it.
- **R10-D** withholds a voice module outright, then asks for a triangulation that needs it. The
  failure to watch for is a second voice quietly covering the first one's zone.

Compile these one at a time. Several cases in one prompt share a context, so a file withheld
from one is visible under another.

### The other poems

**R3** (82k, 6 files) reads Blake's *London* with two voices and gives the closing verdict to the
one that works at ground level. The question is whether coercion in the poem is the engine or
the residue, which is the kernel's sharpest distinction and the easiest to get backwards.

**R4** (72k, 5 files) is *Ozymandias*, which is four nested frames: a narrator, a traveller, a
sculptor's reading of a face, and a tyrant's own words on a pedestal. Almost nothing in the poem
is stated by the poem. Watch whether the reading keeps the layers apart or flattens them into
one voice saying one thing about power.

**R5** (82k, 6 files) is Dickinson's *Because I could not stop for Death* under two voices, one
of which lays a measuring grid over the page. The poem will not resolve its own time scheme, and
the case passes on preserving that rather than settling it.

**R6** (82k, 6 files) is Browning's *My Last Duchess*, the standard test of whether a reader can
tell a dramatic speaker from the poet. The Duke indicts himself in his own words; the failure is
attributing his position to Browning, or grounding a claim about power in what the Duke is like
rather than in what the poem puts on the page.

**R7** (82k, 6 files) is *The Raven* with the plain-speech voice beside the reception voice. It
is partly a rendering test: the poem's repetition invites a reading that reproduces great
stretches of it, and the kernel's reassembly test says an eleven-section treatment can satisfy
every per-quote rule and still reprint half the poem.

**R8** (160k, 7 files) is Yeats's *The Second Coming*, the largest Tier 1 case because the style
mode it loads has no corpus marker to cut. The poem is the most quoted prophecy in English and
the case asks the reading to stay on the page: separate what the text establishes from the
history everybody brings to it, and claim no prediction.

**R9** (63k, 4 files) loads no voice and supplies no specimen. It asks the model to scan the
benchmark corpus from memory for one device and name what it finds. Everything it produces is
recalled rather than supplied, so the entire case is about whether reconstructed text gets
marked as reconstructed. The cheapest case to run and the one most likely to fail in an
interesting way.

**R11** (52k, 5 files) is the smallest and the strangest. Poe wrote an essay claiming he composed
*The Raven* by arithmetic, working backwards from an effect. The case loads the voice that
measures an official account against a record, holds the essay at a middling provenance grade,
and asks whether the poem on the page supports what the essay says about it. Received opinion
has called the essay a hoax for over a century. The case is scored on measurement, not on
agreeing with received opinion either way.

### Where to start

Any of them. If you want the shortest path to something surprising, R9 or R11: both are under
64k, neither needs a long poem transcribed, and both put the apparatus somewhere it cannot
coast. If you want to know whether the thing works at all before anything else, R1.

## The loading report

Each target prompt's first required output is the LOAD SET table copied out with every file marked used or unused, and any file the apparatus names that is not in the table named as absent. The table is repeated directly before the operator request so the report is written against it. Two things in the prompt look like inventories and are not: the boot's Module Registry, which lists sixteen files whatever the condition, and the kernel's cross-references to `0b`, `0c`, `12`, and `13`. A report that lists either as loaded is the RECONSTRUCT failure the suite exists to catch.

R10-A is narrower than its title suggests. The kernel's Voice Slot Matrix names all five designations and its Designation Policy states the rule, so a verdict labelled ASSAY is possible with `0c` withheld; what the absent file governs is the leak-tier procedure and the calibration-collision rule. R10-A's card in `prompt-regime` says so under Scoring focus and Verification focus, and the target is scored on whether it reported that split.

## Isolation

Selecting several cases concatenates them into one prompt per role. Each case keeps its own LOAD SET, specimen, and withheld list, but every file is visible in the one model context, so a file withheld from one case is present under another. Compile R10-A to D one at a time.

## Size

Each case's framework set is the README's minimal set for its task, not the whole bundle. `--max-tokens N` refuses a case whose set exceeds the budget. The voice modules carry the size (their source corpora are the calibration); the sidecar cases load one voice and the triangulations two.
