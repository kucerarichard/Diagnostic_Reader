# dr: Diagnostic Reader prompt compiler

`dr` turns an operator request into the set of framework files a model needs, in the boot's load order, with the request written as the plain-language form the kernel recognizes. It replaces the chat-shell practice of uploading framework files by hand and typing "workshop this specimen" into the context. The regression harness in `regression/` is one consumer of the same loader.

Standard library only. Python 3.9 or later. Run it from the repository root as `python -m dr`. Specimens are text; the compiler takes no images.

```
$ python -m dr read --specimen tyger.txt --title "The Tyger" --author "William Blake" --date 1794 --out run-tyger
Wrote 2 files to run-tyger
  prompt.md: 880,839 chars; sha256 b515bd39c3f0a8b4
  build-manifest.json
Request line: Full sidecar. ASSAY verdict.
~220,209 tokens at 4 chars/token; 5 framework files; Full Monty State absent
```

`prompt.md` is the one thing you paste into a chat model.

## Why a compiler

The full framework is 5.4 MB, about 1.3 million tokens, which no model context holds. The README's minimal sets by task are what make a run possible, and until now they lived only in prose:

```
$ python -m dr explain read --quick
...
Total: 167 KB across 3 files; ~41,705 tokens at 4 chars/token

$ python -m dr explain workshop --dial-trial
...
Total: 1.58 MB across 8 files; ~396,182 tokens at 4 chars/token
```

The resolver computes those sets from `framework-registry.json`, closes them over hard dependencies (DATUM pulls `11`, the battery pulls `7`), checks version floors against the files on disk, and records why every file is present.

## Commands

### read, workshop, scan, extract

Compile a prompt into `--out` (default `compiled-run/`). The output is `prompt.md`, or `prompt-partNofM.md` with `--part-size`, plus `build-manifest.json`.

The prompt holds, in order:

1. A header: generator version, task, voices, Full Monty State, and a notice that the compiler performed the load step and the model should treat the files that follow as loaded and switch off any procedure whose file is absent.
2. The load set as a table: step, file, version, sha256.
3. Withheld and excluded files, when any.
4. Every framework file, fenced and labeled with its load step, name, and designation.
5. The specimen card and the specimen text, fenced, with the specimen's sha256.
6. The account (DATUM) or supplied corpus (scan), when given.
7. The load set again, as a short table with any withheld files named, so the model's loading report is written next to the inventory rather than from memory of a table 300k tokens back.
8. The operator request line.

That is the order a chat operator produces by uploading files and then typing the request. The request line is rendered in the plain-language form the README documents, so the model meets the same trigger:

```
========================================================================================
OPERATOR REQUEST
========================================================================================

Triangulate ASSAY and PLUMB. PLUMB closes.
```

A plan with errors or over budget writes nothing and exits 1. A bad request or a missing or non-text specimen exits 2.

### Specimens

`--specimen FILE` is required for every task except `scan canon`. It takes a UTF-8 text file, or `-` for stdin, and repeats for more than one specimen. A file may open with a header block that fills the card:

```
Title: Kitchen, 6 a.m.
Author: the user
Provenance: the user's own draft
Copyright: the user's

The kettle clicks before the light does.
...
```

Keys are `title`, `author`, `date`, `edition`, `kind`, `unit`, `provenance`, `copyright`, `found by`. A blank line ends the block; a file without one is all text. The flags `--title`, `--author`, `--date`, `--edition`, `--provenance`, `--copyright`, `--found-by` override the block for a single specimen; with several specimens, use the blocks.

The card follows the workshop's Supplied Specimen Card for `workshop` and the sidecar's Provenance field otherwise. Defaults: a poem with no author is the user's own draft under the user's copyright; found text with no author is a third party's, status unknown. `Length` is counted in the declared unit (lines, bars, sentences, speeches, paragraphs, fragments).

`--account FILE` on a DATUM read embeds the poet's account as a separate section held at P2. `--corpus FILE` on `scan supplied` embeds each corpus file.

### explain

Shows the load plan for a request and writes nothing.

```
$ python -m dr explain read --triangulate --voices ASSAY PLUMB --verdict PLUMB
Request:       triangulate; voices ASSAY, PLUMB; verdict PLUMB
Request line:  Triangulate ASSAY and PLUMB. PLUMB closes.
Snapshot:      /path/to/Diagnostic_Reader

step file                                             version      size  why
0    0-poetics-boot-hollow-v0_18.md                   0.18        19 KB  entry point
1    0a-portable-poetics-kernel-v0_3_19.md            0.3.19     126 KB  task Triangulated reading
2    0c-voice-designations-v0_7.md                    0.7         22 KB  task Triangulated reading
4    7-device-inventory-extended-v0_4.md              0.4         85 KB  task Triangulated reading
5    1-rother-voice-module-v0_3_1.md                  0.3.1      635 KB  voice ASSAY
5    2-harris-voice-module-v0_3_1.md                  0.3.1      532 KB  voice PLUMB

Full Monty State: absent
Total: 1.42 MB across 6 files; ~354,855 tokens at 4 chars/token
Plan OK.
```

The `step` column is the boot's load order. `why` is the chain that put the file in the plan, so a file nobody asked for still explains itself:

```
4    11-provenance-grading-extension-v0_1.md          0.1          8 KB  required by 5-hersh-voice-module
```

`explain` takes every flag the compile commands take, and every compile command takes `--explain`. Exit code 0 is a plan that compiles; 1 is a plan with errors or over budget; 2 is a bad request.

### read

```
python -m dr explain read [--quick | --sidecar | --triangulate | --datum | --poetics-scan-only]
    [--voices ASSAY PLUMB ...] [--verdict VOICE] [--counter-voice VOICE]
    [--vise] [--spine VOICE] [--hermetic] [--battery] [--account [FILE]]
    [--kind KIND] [--unit UNIT] ...
```

`--sidecar` is the default and loads ASSAY when no voice is named. `--triangulate` needs two or more voices and refuses to guess them, since the choice decides the load size. `--datum` loads `0a 0c 11 5` and takes `--account FILE`. A `--kind` other than `poem` loads `8-frye-extraction` by default, per the kernel's Found Text Compatibility, and sets the unit from the kind unless `--unit` says otherwise.

### workshop

```
python -m dr explain workshop [--kind KIND] [--provenance TEXT] [--copyright TEXT]
    [--rewrites | --no-rewrites] [--rewrite-under CONFINEMENT] [--ars-poetica]
    [--dial-trial [DIAL] | --no-dial-trials] [--rewrite-at DIAL:SETTING]
    [--contrast-at DEVICE] [--feedback-bridge] ...
```

Loads `0a 0c 3-kowit 3a 12 7`. `--dial-trial` or `--rewrite-at` adds `13`. Each workshop command renders on its own line in the request, the way the README lists them:

```
Request line:  workshop this specimen
               rewrite under axis: upward
               + ars poetica
               dial trial: idiom density
```

### scan

```
python -m dr explain scan canon|supplied [--category A] --devices DEVICE [DEVICE ...] [--or] [--corpus FILE]
```

The source flag is positional and required. The apparatus never substitutes one source for the other, so neither does the compiler. Devices are conjunctive unless `--or`.

### Shared flags

| Flag | Effect |
|---|---|
| `--specimen FILE` | specimen text file; repeatable; `-` for stdin |
| `--title`, `--author`, `--date`, `--edition`, `--provenance`, `--copyright`, `--found-by` | card fields; override a header block |
| `--extensions EXT ...` | features or stems: `frye`, `casanova`, `monadology`, `attridge-staten`, `compartmentalization`, `battery`, or `9`, `14`, `7a` |
| `--plugins PLUGIN ...` | full monty plugins by handle (`"Snow Crust"`) or stem. Private and opt-in; Full Monty State is `absent` until one is named |
| `--slot-registry` | load `0b` |
| `--include`, `--exclude STEM ...` | force a module in or out; exclusions are recorded |
| `--withhold STEM ...` | fault injection: remove a module and record it as withheld. The R10 tests are this flag |
| `--no-boot` | omit `0-poetics-boot-hollow` |
| `--max-tokens N` | fail when the estimate exceeds N; nothing is written |
| `--chars-per-token F` | estimate divisor, default 4 |
| `--part-size CHARS` | split the prompt into parts under this size, at file boundaries, for upload limits |
| `--out DIR` | output directory, default `compiled-run` |
| `--ask TEXT` | free text appended to the request line, for anything the grammar lacks |
| `--explain` | print the plan instead of compiling |
| `--json` | machine-readable output |
| `--framework PATH` | snapshot directory or ZIP; default `$DR_FRAMEWORK`, else the repo root |

Stems accept shorthand: `7`, `7a`, `0c`, `3-kowit`.

### regress

```
python -m dr regress --cases R1 R10-A [--out DIR] [--reader-model X] [--evaluator-model Y] [--adjudicator-model Z]
    [--reader-output FILE] [--evaluator-output FILE] [--max-tokens N] [--explain] [--regression-dir DIR]
```

Compiles regression cases into `reader-prompt.md`, `evaluator-prompt.md`, `adjudicator-prompt.md`, and `build-manifest.json`. Each case's `manifest.json` carries a `request` block in the same fields as the command line, so the load set is resolved, never listed; `withhold` is the fault-injection hook and `expect` pins what must and must not be in the plan. The specimen's sha256 is checked against its pin. See `regression/README.md` for the case format and the conditions.

```
$ python -m dr regress --cases R10-D --out run-R10-D
Wrote 4 files to run-R10-D for R10-D
  reader-prompt.md: 896,101 chars; sha256 976d10cead37c967
  evaluator-prompt.md: 986,223 chars; sha256 c42e0033eadaa479
  adjudicator-prompt.md: 986,925 chars; sha256 04c73acea77ba274
  build-manifest.json
  R10-D: 6 files, ~223,905 tokens; Triangulate ASSAY and PLUMB.; withheld 2-harris-voice-module
```

`--explain` prints each case's plan and writes nothing. `regression/generate_prompts.py` forwards to this command.

### lint

Checks `framework-registry.json` against the boot's Module Registry and Plugin Registry, the files on disk, each file's version line against its file name, and every version floor, then loads every regression case through the resolver. On the current bundle it reproduces the README's Registry Gaps section, plus two notes on R10-A's deliberate fault:

```
$ python -m dr lint
INFO  disk: 0d-apparatus-provenance is in framework-registry.json but not on disk
WARN  boot: 7a-nom-function-battery is on disk and loadable but the boot's Module Registry does not list it (known Registry Gap)
WARN  boot: 9-casanova-extraction is on disk and loadable but the boot's Module Registry does not list it (known Registry Gap)
WARN  boot: 10-monadology-foundations is on disk and loadable but the boot's Module Registry does not list it (known Registry Gap)
WARN  boot: compartmentalization-engine is on disk and loadable but the boot's Module Registry does not list it (known Registry Gap)
WARN  boot: boot's plugin registry gives Small Branch as full-monty-santos-small-branch-example; the file on disk is full-monty-santos-small-branch-v0.2.md (known Registry Gap)
WARN  boot: plugin Gilson (full-monty-gilson-coscienza-plugin) is on disk but not in the boot's Plugin Registry

INFO  regression: R10-A: 0c-voice-designations is withheld but 1-rother-voice-module, 2-harris-voice-module depend on it; ...
INFO  regression: R10-A: 0c-voice-designations is absent with voice modules loaded; ...

29 framework files; 0 errors, 6 warnings, 3 notes
```

Exit code 1 on any error. A header version that disagrees with the file name is an error, because kernel 0.3.12 once shipped under a 0.3.12 file name with a 0.3.11 version line.

### list

```
python -m dr list modules | tasks | voices | modes | plugins | features | kinds | tests
python -m dr list devices [--category A] [--find apostrophe]
python -m dr list categories
python -m dr list confinements [--axis inward] [--handle "Snow Crust"] [--class primitive] [--imposed-by TEXT]
python -m dr list dials
python -m dr list directives
```

`devices`, `categories`, `confinements`, `dials`, and `directives` parse the catalog files on disk, so they report the snapshot you point at. `tests` reads `regression/tests/*/manifest.json`.

```
$ python -m dr list categories
category  name                                  devices
A         Deictic and Scalar Devices            24
B         Sonic and Prosodic Devices            30
C         Syntactic and Sentence Devices        30
D         Figural and Rhetorical Devices        33
E         Structural and Compositional Devices  33
F         Visual and Typographic Devices        20
G         Pragmatic and Ethical Devices         22
```

## Tests

```
python -m unittest discover -s tests
```

77 tests, standard library only, under a second. They read the framework files in the repository root, so counts and load sets pinned in them move when the bundle does; that is the point.

| Group | Pins |
|---|---|
| Registry, snapshot | floor semantics, stem shorthand, version headers, ZIP with a top folder, duplicate releases |
| Resolver | each task's set, closure, found text, dials, load order, withhold, plugins, collisions, budget, floors |
| Request lines | every documented form renders as the README shows it |
| Catalogs | 192 devices by category, 194 confinements (57 composites, 137 primitives, axis split 13/17/12/15), 9 dials, 21 directives |
| Compile | section order, fence escaping, card defaults, account and corpus sections, splitting, text-only, over budget writes nothing, identical hashes |
| Regress | every case loads, fault-injection shapes, R9 as text, the sha pin, the `expect` gate, role prompt contents, embedded outputs |
| Golden | `tests/golden.json`: the load set and request line for each task and each regression case |
| Drift | the framework README's Files tables and minimal-sets table agree with the disk and the registry; the registry's own schema; every source parses as Python 3.9 |
| Robustness | help renders for every subcommand, non-ASCII specimens round-trip, backtick runs of any length fence correctly, the `generate_prompts.py` shim forwards, explain and compile agree |

`tests/golden.json` is the one file a deliberate change updates. After editing `framework-registry.json`, a case manifest, or a request form, run `python tests/update_golden.py`, read the diff, and commit it with the change. A golden failure with no such edit behind it means a task or case loads something different from what it loaded before, and that is what the test is for.

`dr lint` carries the README drift check too, as `readme` findings, so the check runs where the operator runs lint and not only in the suite.

## framework-registry.json

The dependency table. The boot stays the human-readable inventory; this file is its machine mirror, and `lint` keeps the two from drifting. Edit it when a module, voice, task, or dependency changes.

| Key | Holds |
|---|---|
| `modules` | one entry per stem: `type`, `load_step` (the boot's eight steps), `requires` (hard dependencies), `floors` (version floors on other stems), `designation`, `loadable`, plugin `handle` and `collides_with` |
| `voices` | designation to module, with the fires and holds-silent conditions from the README |
| `modes` | VISE and JIG |
| `features` | requestable capabilities (`battery`, `dial-trials`, `found-text`) to the modules they need |
| `tasks` | the README's minimal sets by task, with default voices |
| `kinds`, `units`, `kind_default_unit` | the kernel's found-text declarations |
| `non_runtime_files`, `non_runtime_dirs` | what the snapshot loader skips |
| `calibration_authors` | author name to the voices and modes that stand down for that author's specimen; `--author` is checked against it and a match warns |

A floor compares by the digits it states: `0.3` is satisfied by `0.3.19`, per the kernel's File Reference Rule.

## build-manifest.json

Written beside the prompt. It records the generator version, the request as parsed, the request line, the snapshot path (and its sha256 when a ZIP), every framework file with step, version, size, sha256, and the reasons it was loaded, the withheld and excluded lists, Full Monty State and plugins, each specimen with its sha256 and card fields, the character count and token estimate, and the sha256 of each prompt part. No timestamps: identical inputs produce identical output and identical hashes.

## Budget

The voice modules are the bulk of any plan; 95 percent of each one is its source corpus, which is the calibration and stays. A compact mode that stripped revision notes was measured at 0.7 percent of the bundle and was not built. The lever is which voices you load: `explain` shows the cost of each, and `--max-tokens` refuses a plan that will not fit.

## Snapshots

`--framework` takes a directory or a ZIP. A ZIP may hold the files under one top-level folder; the loader finds the folder that holds the kernel. Files are resolved by unversioned stem; when two releases of one stem are present the higher version wins and `lint` reports the pair. Each file's version comes from its header line (`Version:`, `Module version:`, `## Revision Note (vX)`), with the file name as fallback.

## Layout

```
dr/
  framework-registry.json   the dependency table
  registry.py               loads the table; version comparison
  snapshot.py               directory or ZIP; stem resolution; version headers
  request.py                the Request model; request-line rendering; author collisions
  resolve.py                Request -> LoadPlan
  compile.py                LoadPlan + specimens -> prompt parts and build manifest
  regress.py                regression cases -> reader, evaluator, adjudicator prompts
  catalog.py                parsers for 7, 12, 13, the kernel's directives, and regression manifests
  lint.py                   consistency checks
  cli.py                    argument grammar and output
tests/                      the compiler's unit tests (not the regression cases, which are regression/tests/R*/)
  test_dr.py                python -m unittest discover -s tests
  golden.json               pinned load sets and request lines
  update_golden.py          regenerates golden.json after a deliberate change
  README.md                 what the suite covers and when to update the golden file
```

## History

Phase 1: registry, snapshot, resolver, catalog parsers, `explain`, `lint`, `list`. Phase 2: `compile`, text specimens with header blocks, accounts and corpora, splitting, the build manifest. Phase 3: `regress` on top of the same loader, v2 case manifests with `request` and `expect`, R9 as a text canon scan. The original `regression/generate_prompts.py` embedded all 29 files in every case (about 5.4 MB per prompt); the sidecar cases now load five files and the triangulations six.
