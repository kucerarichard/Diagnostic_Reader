# Run card: 2026-11-27-slab

What `build-manifest.json` cannot record: the command, the date, the repository state, which
model executed the prompt, and what that model was told beyond the prompt. Suite section 5
asks for all of it. The manifests beside this file carry the condition; this file carries the
run.

## Environment

| | |
|---|---|
| Run ID | `2026-11-27-slab` |
| Date | 2026-11-27 |
| Repository | `kucerarichard/Diagnostic_Reader`, commit `f0675c8` |
| Framework | `tier1-snapshot/`, built by `regression/tools/make-tier1-snapshot.py` |
| Boot | 0.19 at compile time, carried into the prompts as `0-poetics-boot-hollow-v0_20.md` |
| Workshop | 0.7.2 |
| Compiler | `dr` 0.2.0, standard library only |

The boot and workshop versions matter here. This run used workshop 0.7.2, whose activation
notice for the extraction named its calibration source. The run reported that as a Tier A
leak and declined to emit it, and the workshop went to 0.7.3 afterwards. A rerun of these
commands today compiles against 0.7.3 and will not reproduce these prompt hashes.

## Specimen

Supplied by the operator, who did not know the author or the source. Twenty lines, five
quatrains, rhymed couplets, a military cemetery.

| | |
|---|---|
| Path | `runs/2026-11-27-slab/specimen.txt` |
| sha256 | `f3b886bc49025d5e...` |
| Title | Took Cab To See Dull and Drab Cold Slab |
| Author | unknown |
| Copyright | unknown |
| Kind, unit | poem, line |

The card was written by hand because the compiler's default for a poem with no author is the
operator's own draft under the operator's copyright, which would have been false.

## Commands

Snapshot, once:

```
python regression/tools/make-tier1-snapshot.py
```

Reading:

```
python -m dr read --specimen runs/2026-11-27-slab/specimen.txt \
    --extensions martino --framework tier1-snapshot \
    --out runs/2026-11-27-slab/reading
```

Workshop:

```
python -m dr workshop --specimen runs/2026-11-27-slab/specimen.txt \
    --extensions martino --framework tier1-snapshot \
    --out runs/2026-11-27-slab/workshop
```

## Conditions compiled

| | reading | workshop |
|---|---|---|
| Request line | `Full sidecar. ASSAY verdict.` | `workshop this specimen` |
| Files | 6 | 8 |
| Characters | 318,892 | 833,200 |
| Token estimate | 79,723 | 208,300 |
| Prompt sha256 | `6f9365ca4bd8f7e5` | `f7903f2ee5f2f312` |

Reading set: boot, kernel, `0c`, `7`, `15-martino-extraction`, `1-rother-voice-module`.

Workshop set: the same less the voice module, plus `12-confinement-inventory`,
`3-kowit-voice-module`, `3a-workshop`.

Both voice modules and the workshop ran at Tier 1, headers without corpora, which both
outputs report as a fidelity limitation.

## Executor

Each prompt went to a separate agent on Claude Opus, in isolation from the other, with no
access to this repository beyond the one prompt file.

Instructions given beyond the prompt, which are part of the condition and are recorded here
because they appear nowhere else:

- Read the prompt file in full before writing anything.
- Read nothing else. Do not search the filesystem or open the repository.
- Use no prior knowledge of a Diagnostic Reader apparatus. Apply only the loaded files.
- Where a procedure needs a file not in the LOAD SET, switch it off rather than rebuild it.
- Begin with the loading report: the LOAD SET copied out, each file marked used or unused.
- Obey the designation policy.
- The workshop agent was additionally pointed at the Martino Extraction Awareness block.

## Results

Reading, 367 lines. Fired extraction tools 3, 4, 5, 6 on page warrant; declined 1, 2, 7 with
grounds. Tool 3's symmetry-hunger guard fired for real, rejecting a first candidate invariant
on the identity test before accepting a second, and reported the withdrawal.

Workshop, 477 lines, all thirteen output-form sections including Confinement Bay. Fired tools
2, 3, 4, 7 per the awareness block and kept Tool 1 out.

The two runs converge independently on the same two lines, L8/9 and L18/19, as the only places
the poem is doing something. The reading reaches them through a reception argument about the
churchyard elegy; the workshop reaches them through the held-frame test in Engine Bay.

## Checks run by the operator after the fact

- Both outputs exist and carry the loading report and the full form.
- No calibration source's name appears in any reading or treatment section. The only hits are
  in LOAD SET tables the loading report is required to copy out, and in sections explicitly
  marked apparatus-internal.
- The workshop's suppressed activation notice was verified against `15`'s rights section and
  the designation layer's Tier A, and the workshop was corrected at 0.7.3.

## Limitations

The specimen's author and source are unknown, so no reception fact about it could be checked.

Both corpora were withheld at Tier 1, so the voices ran at header fidelity. Neither output
claims otherwise.

The compiler records no commit, date, or executor, which is why this file exists.
