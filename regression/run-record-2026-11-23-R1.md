# Run record, 2026-11-23, R1

A record of one attempt to run R1 under an agent harness rather than a chat shell. The attempt
produced no test artifact. This document states what was compiled, what was attempted, what the
attempt established about the suite and what it did not, and a judgement on where the deficiency
actually sits. The short version is that the compiler and the test definitions are sound, the
attempt misdiagnosed prompt size as the obstacle, and the obstacle is that the suite specifies a
protocol it supplies no way to execute.

## Scope

One operator asked for the full suite and for R1 first, with the three roles run as independent
agents and the Reader assigned to a smaller model. The compiler ran. The Reader never finished.
Nothing was scored, and no disposition under suite section 7 was reached for R1 or for any other
case.

## Condition compiled

`dr regress` resolved R1 without error against the repository bundle at commit `236856e`.

```
$ python -m dr regress --explain --cases R1
##### R1: Bootstrap and designation integrity
Request:       sidecar; voices ASSAY
Request line:  Full sidecar. ASSAY verdict.

step file                                             version      size  why
0    0-poetics-boot-hollow-v0_18.md                   0.18        19 KB  entry point
1    0a-portable-poetics-kernel-v0_3_19.md            0.3.19     126 KB  task Full reading
2    0c-voice-designations-v0_7.md                    0.7         22 KB  task Full reading
4    7-device-inventory-extended-v0_4.md              0.4         85 KB  task Full reading
5    1-rother-voice-module-v0_3_1.md                  0.3.1      635 KB  voice ASSAY

Full Monty State: absent
Total: 888 KB across 5 files; ~221,908 tokens at 4 chars/token
Plan OK.
```

The `expect` gate passed, the specimen sha256 pin checked, and the three role prompts were
written. The supporting machinery was sound throughout: `python -m unittest discover -s tests`
ran 79 tests in 2.3 seconds with no failures, and `dr lint` reported 0 errors against 29 framework
files, with all 6 warnings matching the Registry Gaps the framework README already documents.

Nothing in this record is a defect in the compiler. The compiler did its job in both attempts.

## The two Reader attempts

The Reader ran as a background agent on Claude Sonnet, given the compiled `reader-prompt.md` in a
directory holding that file alone, with instructions not to read anything else and not to draw on
any prior knowledge of the apparatus.

First attempt, Tier 3, the canonical condition. The prompt was 887,328 characters across 8,481
lines. The agent ran for about twelve minutes, wrote no artifact, and was stopped.

Second attempt, Tier 1. The operator directed a rerun with the voice corpus withheld. The prompt
was 294,381 characters across 3,810 lines, a 67.6 percent reduction in the token estimate, from
221,908 to 71,928. The agent ran for about eight minutes, wrote no artifact, and was stopped.

Neither attempt failed on context. The second prompt fits a 200,000-token window three times over.
The failure was the shape of the instrument.

A chat shell hands the model the whole prompt as one message, and the model begins generating on
receipt. That is the condition suite section 5 specifies when it says to paste into a clean
session. An agent cannot be handed a prompt. It must fetch one, so it spends a round trip on a
read call, receives the prompt as tool output into a context that already carries a harness system
prompt and tool schemas, and only then begins. The operator reports Muse and ChatGPT completing
these cases in about a minute each from a paste. The agent harness is the variable that changed.

Assigning the Reader role to a cheaper model is sound. Running it as an agent is not. The Reader
is a single completion: one prompt in, one artifact out, no tools. Any harness that makes the
Reader fetch its own prompt has added a step the role does not have.

## Corpus tiers

The second attempt required a Tier 1 load, which `dr` cannot express. The string `tier` appears
nowhere in `dr/` except one unrelated reference to the leak tiers of `0c-voice-designations`. The
resolver loads whole files or none, and `--withhold` removes a file entirely rather than
truncating it.

Four of the five voice modules define corpus tiers themselves. From
`1-rother-voice-module` section Corpus Loading Tiers:

> Tier 1: this header. Use for ordinary Rother-mode deployment.
>
> Tier 3: full corpus. Load when a Rother-mode verdict needs maximum fidelity or when a specimen
> falls outside the Tier 2 range.

The compiler emits Tier 3 unconditionally, including for cases the modules would class as ordinary
deployment. The header is 34 KB of the Rother module's 635 KB.

Tier 1 was simulated from outside the tool. Each voice module was truncated at its own corpus
marker in a scratch copy of the bundle, the corpus replaced by a section declaring the tier, and
`--framework` pointed at that copy. Note that `--framework` also relocates the case lookup, so
`--regression-dir regression` is required alongside it:

```
$ python -m dr regress --cases R1 --framework <snapshot> --regression-dir regression --out runs/...
  R1: 5 files, ~71,928 tokens; Full sidecar. ASSAY verdict.
```

Exactly one file's hash moved. Boot, kernel, `0c`, the device inventory and the specimen stayed
byte-identical:

| file | canonical sha256 | tier 1 sha256 |
|---|---|---|
| `0-poetics-boot-hollow-v0_18.md` | ab05bfe117143886 | ab05bfe117143886 |
| `0a-portable-poetics-kernel-v0_3_19.md` | 2f408d84625414dd | 2f408d84625414dd |
| `0c-voice-designations-v0_7.md` | ab0b2e67da17db4c | ab0b2e67da17db4c |
| `7-device-inventory-extended-v0_4.md` | 4dde79df1df0c4b3 | 4dde79df1df0c4b3 |
| `1-rother-voice-module-v0_3_1.md` | 39e47be1b787f0e8 | a2fdc58df8051e7a |

A snapshot is a poor substitute for a flag. `dr lint` cannot see it, the golden tests cannot see
it, and the hash it produces means nothing to a reader without that scratch directory. A
`--corpus-tier` flag recording the tier in `build-manifest.json` would put the condition where
suite section 5 can pin it. Tier 2 is the harder half, since it means slicing named sections out of
a corpus rather than cutting at one marker.

## Case sizes

The size table was computed from `dr regress --explain` across all fourteen cases, and holds
regardless of how any run goes.

| Case | Token estimate |
|---|---|
| R9 | 63,062 |
| R11 | 159,401 |
| R1, R2, R4 | 221,908 |
| R10-D | 223,905 |
| R7 | 269,070 |
| R8 | 309,602 |
| R5 | 327,025 |
| R10-B | 335,495 |
| R10-A | 351,442 |
| R3, R6, R10-C | 354,855 |

Two of fourteen cases fall under 200,000 tokens. The evaluator prompt is larger than the reader
prompt in every case, because it carries both control documents and a second copy of the framework
on top of the condition. For R1 the evaluator prompt is 992,241 characters before the Reader output
is pasted into it.

The evaluator does not need that second copy. Its work is verification, checking that rules the
Reader cited exist in the pinned files, which is a lookup against a hashed snapshot rather than a
whole-context read. Nothing was tested on this point; it is a design observation.

## The binding constraint

The suite has no execution path. `dr` contains no network code: `grep -rn "urllib\|requests\|api_key"
dr/*.py` returns nothing, and the framework README states the design plainly, "You paste that prompt
into a model." `regression/README.md` says the same, "nothing here calls a model." Prompt
construction is automated. Prompt delivery is a pair of hands.

What the protocol then asks of those hands, for one pass over the fourteen cases at Tier 3:

| Quantity | One pass | With section 15 conditions A, B, C |
|---|---|---|
| Paste operations | 42 | 126 |
| Characters pasted | 48.5 MB | 145.6 MB |
| Output copy operations | 28 | 84 |

The output copies are the handoffs the suite requires between stages, the raw Reader output into the
evaluator slot and the evaluator report into the adjudicator slot. Section 5 adds that each role
needs a clean session, so the pastes cannot be batched into one conversation.

Forty-two pastes averaging 1.2 MB each is not a workload a person completes. It is not a workload a
person should attempt. The operator who commissioned this run named the problem in their first
sentence, that running all the cases by hand is not humanly possible, and a later message gave the
specific cost, repetitive strain. Both were accurate.

## Findings from the files

These came from reading the bundle, not from the attempts, and stand independent of them.

Stale role pins reach the graders. All fourteen case manifests carry
`"target_model": "Gemini (record exact model/version if visible)"`, with matching `evaluator` and
`adjudicator` fields naming Muse and ChatGPT. `READER_MANIFEST_KEYS` in `dr/regress.py` is an
allowlist and correctly withholds those from the Reader. The evaluator and adjudicator receive the
full manifest, so they are told the target was Gemini whatever actually ran, and `--reader-model`
never reconciles the two. Suite section 5 asks for model identity to be concealed from the graders
where practical. The manifests supply a false one instead.

The loading report has no zone. `0c-voice-designations` Leak Tier A names "the module filename" as
never permitted in output. Required output item 1 in every target prompt is the LOAD SET table
copied out, which is a table of module filenames. The policy names three zones, generated readings,
apparatus-internal prose, and operator queries, and the phrase "loading report" appears in none of
`0c`, the kernel, or the boot. A Reader that redacts the table is following `0c`. A Reader that
copies it is following the target prompt. The R1 evaluator criteria and adjudication focus cannot
settle which, so a score either way is unsupported. The smallest patch is one sentence in `0c`
placing a diagnostic loading report in the apparatus-internal zone.

R1 does not pin its own entry point. The case `expect.loaded` block names `0a`, `0c`, and `1`, but
not `0-poetics-boot-hollow`, though bootstrap integrity is the case's stated focus.

The build manifest records no run identity. It carries every file's sha256, which is stronger
per-file evidence than a commit hash, but it records no commit, no run identifier, and no date, and
`snapshot_sha256` is null for a directory snapshot because `dr/regress.py` only hashes a ZIP. Suite
section 5 asks for repository URL, commit hash, and date of run before any test runs. The
repository has a remote and a HEAD that the compiler could read in one line.

A documentation count has drifted. `dr/README.md` line 248 states 77 tests. The suite runs 79, and
both `tests/README.md` and the framework README say 79. The README drift check in `dr lint` does
not cover this number.

## Limits of this record

No individual case was shown to be beyond a model. Two agent runs of one case were stopped before
producing anything, which establishes that this agent harness is the wrong instrument for the Reader
role and nothing further. The operator reports chat-shell runs completing in about a minute, and
nothing here contradicts that. A single case, pasted, runs. The judgement below concerns the suite
at its specified scope, fourteen cases across three roles and three conditions, which is a different
claim and rests on the paste arithmetic rather than on these two stopped runs.

Nothing was established about R1 itself. Whether a model loads and applies the actual bootstrap and
designation rules on The Tyger is still open. No score exists for procedural compliance, literary
execution, dependency handling, or framework integrity, and no failure code was confirmed or ruled
out.

The question the Tier 1 condition was built to answer is also still open. The Rother module states
that the corpus is the calibration. At Tier 1 a Reader holds the Operational Lexicon, the Negative
Lexicon, Recurring Moves, Register, Stance, Failure Modes, and the five-gate voice gate, and holds
no worked example of any of them. Whether an ASSAY verdict clears its own Lexicon, Specificity,
Negative, Pun, and Closure gates on header prose alone decides whether the 67.6 percent saving is
close to free. One completed Tier 1 run would answer it.

## Judgement

The attempt failed, and the failure was in the attempt rather than in the suite.

The proximate cause was an instrument error. Running the Reader as a background agent gave the role
a step it does not have, fetching its own prompt, and no artifact ever appeared. That error is
simple and is now documented above.

The consequential error was a misdiagnosis. The attempt treated prompt size as the binding
constraint, measured it carefully, produced a table showing two of fourteen cases under 200,000
tokens, and built a corpus-tier workaround that cut R1 by 67.6 percent. All of that is accurate and
none of it was the problem. Size stops a model from accepting a prompt. Nothing was stopping the
model. What stops this suite is that a human being must move 48.5 MB by hand to complete a single
pass, and no amount of trimming the prompts changes that. Cutting every case to Tier 1 still leaves
42 pastes. The tier flag is worth building and it is not the fix.

On the framework itself the verdict is favourable, and the attempt did not establish otherwise. The
compiler resolves every case without error, 79 unit tests pass, `dr lint` reports zero errors, the
`expect` gates catch mis-specified conditions at compile time, and the specimen hash pins refuse an
edited transcription. The suite's definitions are more rigorous than a prompt generator usually
receives: separate scores that may not be averaged, N/D held distinct from zero, a critical-failure
rule, an adjudicator charged with auditing the evaluator rather than seconding it, and a standing
instruction to preserve unresolved disagreement. The six items under Findings from the files are
small and local. None of them is a reason the suite cannot run.

The deficiency sits at one seam. The suite specifies a four-stage, three-role, blinded,
repeated-condition protocol, and supplies no means of executing it except manually. That is a
historical artifact rather than an error of design. The protocol was written for chat-shell practice
when pasting was what an operator did, and `dr regress` later automated the construction of the
prompts while leaving their delivery where it found it. The automation stopped one step short.

## Next step

Give `dr` an execution backend. A `dr run` that posts a compiled prompt to a model endpoint and
writes the response to `reader-output.md` is roughly a hundred lines against `urllib.request`, which
keeps the standard-library-only constraint the package already holds. With it, a case becomes one
command, the three stages chain without a human between them, and section 15's repeated conditions
become a loop rather than an injury.

Two notes for whoever builds it. The environment this record was made in has `OPENAI_API_KEY` set
and no Anthropic key, so the first backend can be written and tested today against one provider, and
the role-model assignment the suite already supports maps onto whatever keys are present. Second,
the loading report is mechanically gradeable. Required output item 1 asks for the LOAD SET table with
each file marked used or unused, and the manifest already holds the correct answer, so a checker can
score the LOAD and RECONSTRUCT dimensions without a model at all. That is the cheapest and
highest-signal criterion in the suite, and automating it removes the evaluator from the one judgment
that needs no judgment.

Until the backend exists, the suite is a specification rather than a test, and the ledger in
`runs/2026-11-23-R1-sonnet/` states what R1 would be judged against when it can be run.
## Artifacts on disk

Under `runs/`, untracked, outside the bundle:

| Path | Holds |
|---|---|
| `runs/2026-11-23-R1-sonnet/` | Tier 3 role prompts and `build-manifest.json` for the canonical condition |
| `runs/2026-11-23-R1-sonnet/source-verification-ledger.md` | the standard R1 should be judged against, read out of the pinned files before any artifact existed, with both hash sets and the condition change recorded |
| `runs/manual-tier1/R1/` | the Tier 1 R1 condition, reproducible from `regression/tools/` |

No `reader-output.md` exists in either directory. The ledger was written before the artifact it
was meant to judge, which is the right order and the only part of the protocol this attempt carried
out as the suite specifies.
