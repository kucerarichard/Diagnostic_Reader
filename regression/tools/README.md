# regression/tools

Two scripts for running a case by hand in a chat shell, and the procedure that uses them.
Neither calls a model. Standard library only, Python 3.9 or later, like the `dr` package.

| Script | Does |
|---|---|
| `make-tier1-snapshot.py` | copies the bundle with each voice module cut at its corpus marker, giving a Tier 1 framework to compile against |
| `cut-wrapper.py` | strips the framework files out of a compiled reader prompt, leaving the 3 percent you have to paste |

## Why

A compiled reader prompt is about 97 percent framework files. Chat shells take file
attachments, so the framework can be uploaded instead of pasted, and attaching five files
costs five clicks. For R1 that is 294,310 characters pasted against 9,528.

| Case | Compiled prompt | Wrapper | Attachments |
|---|---|---|---|
| R9 | 258,612 | 8,791 | 4 |
| R1 | 294,310 | 9,528 | 5 |
| R2 | 294,383 | 9,601 | 5 |
| R4 | 294,075 | 9,291 | 5 |

## Procedure

Build the Tier 1 snapshot once. It lands in `tier1-snapshot/`, which `.gitignore` drops.

```
python regression/tools/make-tier1-snapshot.py
```

Compile a case against it and cut the wrapper. `--reader-only` skips the evaluator and
adjudicator prompts; `--regression-dir` is required because `--framework` also relocates
the case lookup.

```
python -m dr regress --cases R9 --framework tier1-snapshot --regression-dir regression \
    --reader-only --out runs/manual-tier1/R9
python regression/tools/cut-wrapper.py runs/manual-tier1/R9/reader-prompt.md
```

`cut-wrapper.py` prints the files to attach. Open a clean chat session, attach those files
from `tier1-snapshot/`, paste `reader-wrapper.md`, and save the complete raw response as
`reader-output.md` beside the wrapper.

Attach from the same bundle you compiled against. The LOAD SET in the wrapper carries each
file's sha256, and a Tier 1 wrapper with Tier 3 files attached is a condition that matches
no manifest.

## Grouping cases by configuration

Two cases can share one upload when their resolved file lists are identical. Fourteen
cases collapse to ten configurations:

| Configuration | Cases | Files |
|---|---|---|
| sidecar, ASSAY | R1, R2, R4 | 5 |
| triangulate ASSAY and PLUMB | R3, R6, R10-C | 6 |
| canon scan | R9 | 4 |
| DATUM | R11 | 5 |
| one each | R5, R7, R8, R10-A, R10-B, R10-D | 6 to 7 |

R10-C joins R3 and R6 because the file it withholds, `11-provenance-grading-extension`, is
not in the resolved list anyway, so the attachment set is genuinely identical and nothing
leaks. R10-A, R10-B and R10-D each resolve to a different set and need their own upload,
which is what `regression/README.md` means by compiling them one at a time.

Attach once, paste each wrapper into its own clean session. Sessions stay separate per
suite section 5; it is the upload that is shared, not the context.

## Reading the result without a grader

Suite section 13 keeps four score categories separate and forbids averaging them. Three
are checkable by hand against `build-manifest.json`, which is why a run needs no evaluator
or adjudicator to be worth doing.

**Loading report.** The prompt repeats the LOAD SET immediately before the operator
request so the report can be written against it. Check three things:

- every file in the table marked used or unused
- nothing marked used that is absent from the table
- withheld files reported absent, for R10-A through D

The traps are the boot's Module Registry, which lists sixteen stems whatever the condition,
and the kernel's cross-references to `0b`, `12` and `13`. A report that lists either as
loaded is the RECONSTRUCT failure the suite exists to catch. At Tier 1 a report that treats
the absent corpus as a loading fault rather than the declared tier is also worth noting.

**Dependency handling.** Where a procedure needed an absent file, did the output switch the
procedure off and say so, or rebuild it from memory?

**Designation.** The permitted label form is `ASSAY verdict:`, per `0c-voice-designations`
section Supersession. A label built from a calibration source's name fails, and so does a
coined phrase or biographical anchor that identifies the source without naming it. Specimen
attribution is untouched: naming Blake and The Tyger is required.

Literary execution is the one category that wants another reader. Everything above you can
settle yourself in a few minutes.

Write the standard down before reading the output.
`runs/2026-11-23-R1-sonnet/source-verification-ledger.md` is a worked example for R1, with
the governing rule cited for each check.

## Limits

A Tier 1 run is not the condition the suite pins for a case. Each voice module's sha256
changes, so Tier 1 scores are a separate operating profile, not canonical results. Suite
section 2 calls such a profile a compact configuration for lower-capability models and asks
that it be documented as empirically supported rather than assumed interchangeable.

`4-gonzo-mode` carries no corpus marker and is copied whole, so R8 stays the largest case at
Tier 1, at about 160,000 tokens. The other thirteen sit between 52,000 and 83,000.

`cut-wrapper.py` reads a compiled prompt, never a case directory. The manifest inside a
compiled reader prompt is the reader-facing one, filtered by `READER_MANIFEST_KEYS`;
`regression/tests/<case>/manifest.json` also carries `scoring`, `target_model`, `evaluator`
and `adjudicator`, and handing the Reader those contaminates the run.
