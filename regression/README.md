# Diagnostic Reader Regression Suite

Test definitions for the regression suite, compiled into role prompts by `dr regress`. This directory holds no runtime module. The framework files are read from the repository root (or a snapshot you name), and nothing here calls a model.

The cases live under `regression/tests/R*/`. That is a different directory from `tests/` at the repository root, which holds the compiler's own unit tests and is run with `python -m unittest`; the two share a word and nothing else. A regression case is a condition for a language model; a unit test is an assertion about the `dr` package. See `tests/README.md` for the latter.

```
python -m dr regress --cases R1 --reader-model "Model X" --evaluator-model "Model Y" --adjudicator-model "Model Z" --out run-R1
```

`regression/generate_prompts.py` forwards to the same command for scripts that still call it.

## Contents

| Path | Holds |
|---|---|
| `regression/tests/<R-ID>/manifest.json` | the condition: a `request` block the compiler resolves into a load set, an `expect` block, and the pinned specimen |
| `regression/tests/<R-ID>/target-prompt.md` | Reader instructions for the case |
| `regression/tests/<R-ID>/evaluator-prompt.md`, `adjudicator-prompt.md` | role-specific case instructions |
| `regression/tests/<R-ID>/specimen.txt` | the frozen transcription; its sha256 is pinned in the manifest. R9 has none by design |
| `regression/tests/R11/account.txt` | the poet's account the DATUM reading measures the specimen against; pinned like the specimen |
| `regression-suite-v*.md`, `prompt-regime-v*.md` | control documents: scoring, procedure, test cards. Not runtime modules |
| `prompts/evaluator-master.md`, `prompts/adjudicator-master.md` | shared role instructions |

## Output

`dr regress` writes four files:

| File | Contents |
|---|---|
| `reader-prompt.md` | per case: target instructions, a reader-facing manifest (no scoring material), the LOAD SET table, every framework file in the condition, the specimen with its card, the LOAD SET repeated with withheld files named, and the operator request line |
| `evaluator-prompt.md` | evaluator master, the two control documents, then per case: evaluator instructions, the full manifest, the same LOAD SET, files and specimen, and a slot for the raw Reader output |
| `adjudicator-prompt.md` | the same with adjudicator instructions and a second slot for the evaluator report |
| `build-manifest.json` | selected cases, model labels, per-case request line, load set with sha256 per file, withheld list, specimen sha256, token estimate, and the sha256 of each prompt |

After the Reader run, paste its complete raw output into the marked slot in `evaluator-prompt.md`, or recompile with `--reader-output reader-output.md`. After evaluation, paste the evaluator report into `adjudicator-prompt.md`, or recompile with `--reader-output ... --evaluator-output ...`.

A working convention, one directory per run:

```
python -m dr regress --cases R1 --reader-model "<model>" --out runs/2026-11-08-R1-<model>
#   paste reader-prompt.md into the Reader; save its output as runs/.../reader-output.md
python -m dr regress --cases R1 --reader-model "<model>" --evaluator-model "<model>"     --reader-output runs/2026-11-08-R1-<model>/reader-output.md --out runs/2026-11-08-R1-<model>
#   paste evaluator-prompt.md into the evaluator; save as runs/.../evaluator-report.md
python -m dr regress --cases R1 --reader-model "<model>" --evaluator-model "<model>" --adjudicator-model "<model>"     --reader-output runs/.../reader-output.md --evaluator-output runs/.../evaluator-report.md --out runs/2026-11-08-R1-<model>
#   paste adjudicator-prompt.md into the adjudicator; save as runs/.../adjudicator-report.md
```

The directory then holds the condition (`build-manifest.json`, with every hash), the three outputs, and the prompts. Commit the manifest and the outputs; the `.gitignore` drops the prompt files from `runs/`, since they regenerate from the manifest and each set is several megabytes. The first thing to read in any `reader-output.md` is its loading report against the case's repeated LOAD SET.

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

## The loading report

Each target prompt's first required output is the LOAD SET table copied out with every file marked used or unused, and any file the apparatus names that is not in the table named as absent. The table is repeated directly before the operator request so the report is written against it. Two things in the prompt look like inventories and are not: the boot's Module Registry, which lists sixteen files whatever the condition, and the kernel's cross-references to `0b`, `0c`, `12`, and `13`. A report that lists either as loaded is the RECONSTRUCT failure the suite exists to catch.

R10-A is narrower than its title suggests. The kernel's Voice Slot Matrix names all five designations and its Designation Policy states the rule, so a verdict labelled ASSAY is possible with `0c` withheld; what the absent file governs is the leak-tier procedure and the calibration-collision rule. The evaluator and adjudicator prompts for R10-A say so, and the target is scored on whether it reported that split.

## Isolation

Selecting several cases concatenates them into one prompt per role. Each case keeps its own LOAD SET, specimen, and withheld list, but every file is visible in the one model context, so a file withheld from one case is present under another. Compile R10-A to D one at a time.

## Size

Each case's framework set is the README's minimal set for its task, not the whole bundle. `--max-tokens N` refuses a case whose set exceeds the budget. The voice modules carry the size (their source corpora are the calibration); the sidecar cases load one voice and the triangulations two.
