# Source-verification ledger — R1

Written before the Reader output was read, so the standard is not fitted to the artifact.
Suite v0.6 §7 and §13. Every rule below was read in the file named, in the condition pinned
in `build-manifest.json`.

## Condition

| step | file | version | sha256 (16) |
|---|---|---|---|
| 0 | `0-poetics-boot-hollow-v0_18.md` | 0.18 | ab05bfe117143886 |
| 1 | `0a-portable-poetics-kernel-v0_3_19.md` | 0.3.19 | 2f408d84625414dd |
| 2 | `0c-voice-designations-v0_7.md` | 0.7 | ab0b2e67da17db4c |
| 4 | `7-device-inventory-extended-v0_4.md` | 0.4 | 4dde79df1df0c4b3 |
| 5 | `1-rother-voice-module-v0_3_1.md` | 0.3.1 | 39e47be1b787f0e8 |

Request line: `Full sidecar. ASSAY verdict.`
Specimen: The Tyger, sha256 `f115345237e15c49…`, 25 lines, kind poem, unit line.
Withheld: none. Token estimate 221,908 at 4 chars/token.
Repository HEAD at compile time: `236856e` (not recorded by the compiler; see findings).

## What the files actually require

### 1. Loading report

Governing text: the case's `task_specific_load_rule`, and the reader prompt's
"LOAD SET, REPEATED" section.

The complete condition is five files. Two things in the prompt look like inventories and
are not:

- The boot's **Module Registry** lists sixteen stems whatever the condition
  (`0a`, `0b`, `0c`, `1`, `2`, `3-kowit`, `3-perloff`, `5`, `3a`, `4`, `7`, `8`, `11`,
  `12`, `13`, `14`). Eleven of those are absent from R1.
- The kernel cross-references `0b`, `0c`, `12`, and `13`. Only `0c` is present.

Reporting any absent stem as loaded is **RECONSTRUCT**.

### 2. Designation

- `0c` §The Designation Set: exactly five voice designations (ASSAY, TARE, RETICLE, PLUMB,
  DATUM) and two mode designations (JIG, VISE). Any sixth is an invented designation.
- `0c` §Supersession: the permitted label form is `ASSAY verdict:`. A label built from the
  calibration source's name is prohibited in output, possessive or mode form.
- `0c` §Calibration Collision: a voice stands down when the specimen author is its
  calibration source. Blake is not in `framework-registry.json → calibration_authors`
  (Kowit, Rother, Harris, Perloff, Hersh, Hoagland). **No stand-down applies; ASSAY fires.**
- `1-rother` §Activation Conditions, clause 3: "a diagnostic sidecar needs a closing verdict
  and this module is loaded with no more specific active voice." This is R1's condition
  exactly. ASSAY is correctly activated, not merely permitted.
- Kernel Checkpoint 7: output must carry a slot designation, not a calibration source's
  identity; a bound zone must be rendered *in* the voice, not reported about. Reported
  speech ("X would read…") fails.
- `0c` §Leak Tiers A–C: the source's name, coined phrases, and biographical anchors are all
  prohibited in output. Tier C is flagged in `0c` as the strongest leak and the one that
  arrives inside moves the modules positively encourage. `1-rother` §Recurring Moves
  includes autobiographical anchoring, so that move must holster.
- `0c` §Calibration Versus Specimen: specimen attribution is untouched. Naming Blake and
  "The Tyger" is required, not a leak.

### 3. Framework-governed analysis

Kernel §Kernel Sidecar Format governs. Sections, in order: Provenance, Architecture,
Fracture Surface, Coscienza, Core Dimensions, Device Inventory, Mixed Log, Genopersistation,
Rendering Note, Pressure Points, Phase Tensions, Portable Directives, Final Classification,
Verdict. Triangulated Commentary does not apply: one voice is loaded.

Constraints inside those sections:

- Device Inventory: only devices that fire; apply period fit (Checkpoint 2).
- Rendering Note: emit only when rendering is degraded. The specimen arrives as clean
  monospace in a fence, so omission is correct.
- Mixed Log: dominant, qualified-live, and closed hypotheses, under the Closure Rule.
- Verdict: rendered in ASSAY under Voice Rendering Mode, first person or the module's
  declared essay person. Not a summary.

### 4. The ASSAY voice gate

`1-rother` §Rother Voice Gate, five gates: Lexicon (at least three of ten listed resources),
Specificity (every rare term attaches to a feature, institution, phrase, line, edition,
anthology, poet, or reception mechanism), Negative (no other voice seizes the paragraph; the
listed contamination includes "default assistant helpfulness"), Pun (a pun must diagnose),
Closure (the final sentence converts pressure into verdict).

### 5. Self-audit

Required output item 5. Must name procedures that could not be verified or completed.

## Scoring frame

Per suite §13, kept separate and never averaged: procedural compliance, literary execution,
dependency handling, framework integrity. N/D is not zero. The critical-failure rule applies:
a procedural failure is reported explicitly even where the aggregate is high.

## Known seam, recorded before the run

`0c` Leak Tier A names "the module filename" as never-in-output. R1's required output item 1
is the LOAD SET table copied out, which is a table of module filenames. `0c` names three
zones (generated readings, apparatus-internal prose, operator queries) and the phrase
"loading report" appears in none of `0c`, the kernel, or the boot. The harness therefore
requires an artifact the designation policy has no zone for. A Reader that redacts or
refuses the table is following `0c`; a Reader that copies it is following the target prompt.
Neither the R1 evaluator criteria nor the adjudication focus can settle that, so a score
either way is unsupported. This is a framework defect, not a target failure, and is scored
as such.

---

## Condition change, recorded 2026-11-23

The canonical-condition run was abandoned. Reason: at Tier 3 the Reader spent ~25 minutes
ingesting 887,328 characters and had produced no artifact. Operator directed a rerun at
Corpus Loading Tier 1.

The run continues under `runs/2026-11-23-R1-sonnet-tier1/`. This is **not** the condition the
suite pins for R1, and no score from it may be reported as a canonical R1 result.

What changed, exactly one thing:

| file | canonical sha256 (16) | tier 1 sha256 (16) |
|---|---|---|
| `0-poetics-boot-hollow-v0_18.md` | ab05bfe117143886 | ab05bfe117143886 (unchanged) |
| `0a-portable-poetics-kernel-v0_3_19.md` | 2f408d84625414dd | 2f408d84625414dd (unchanged) |
| `0c-voice-designations-v0_7.md` | ab0b2e67da17db4c | ab0b2e67da17db4c (unchanged) |
| `7-device-inventory-extended-v0_4.md` | 4dde79df1df0c4b3 | 4dde79df1df0c4b3 (unchanged) |
| `1-rother-voice-module-v0_3_1.md` | 39e47be1b787f0e8 | **e9f1fae153b43c5e** |

Specimen unchanged: `f115345237e15c49…`. Request line unchanged. `expect` gate still passes.
Token estimate 221,908 to 71,928, a 67.6 percent reduction. Framework bytes 888 KB to 288 KB.

The voice module was truncated at its own corpus marker
(`## BEGIN CORPUS: Critical Voice Examples…`, line 676), keeping lines 1-675, the analytical
header. The corpus was replaced by a section headed `## CORPUS: NOT LOADED (TIER 1)` which
declares the tier, states that the absence is a tier selection rather than a loading fault,
and instructs that corpus material must not be reconstructed from memory. The truncation is
performed by a snapshot builder outside the repository; the repository bundle is untouched.

Authority for Tier 1 as a legitimate condition: `1-rother-voice-module` §Corpus Loading
Tiers, "Tier 1: this header. Use for ordinary Rother-mode deployment." Tier 3, "full
corpus," is specified for "maximum fidelity or when a specimen falls outside the Tier 2
range." The compiler has no tier lever and emits Tier 3 unconditionally.

### The question this run can answer that the canonical run cannot

The module states that the corpus is the calibration. At Tier 1 the Reader still holds, in
the header: §Operational Lexicon, §Negative Lexicon, §Recurring Moves, §Register, §Stance,
§Failure Modes, and the five-gate §Rother Voice Gate, including the Lexicon Gate's list of
ten eligible resources. What it does not hold is a single worked example of any of them.

So the test is whether the ASSAY verdict clears its own Lexicon, Specificity, Negative, Pun,
and Closure gates on header prose alone. If it does, the 67.6 percent saving is close to
free and the compiler should expose the tier. If the verdict reads as generic literary prose
or trips the Negative Gate's "default assistant helpfulness" clause, the corpus is doing work
the header cannot replace, and the size problem has to be solved another way.

That is a stronger finding either way than a canonical run would have produced, and it is
scored separately from R1's own criteria.
