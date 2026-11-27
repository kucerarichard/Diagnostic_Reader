# Run card: 2026-11-27-couriers

What `build-manifest.json` cannot record: the command, the date, the repository state, which
model executed the prompt, and what that model was told beyond the prompt. Suite section 5
asks for all of it. The manifests beside this file carry the condition; this file carries the
run.

## Environment

| | |
|---|---|
| Run ID | `2026-11-27-couriers` |
| Date | 2026-11-27 |
| Repository | `kucerarichard/Diagnostic_Reader`, commit `494a808` |
| Framework | `tier1-snapshot/`, built by `regression/tools/make-tier1-snapshot.py` |
| Boot | 0.21 |
| Workshop | 0.7.3 |
| Compiler | `dr` 0.2.0, standard library only |

Boot 0.21 and workshop 0.7.3, one revision later than the slab run, which used 0.20 and
0.7.2. The difference is the activation notice the slab run reported as a Tier A leak. This
run emits the corrected notice.

## Specimen

Sylvia Plath, *The Couriers*, written 1962, collected in *Ariel*, 1965. Thirteen lines.

| | |
|---|---|
| Path | `runs/2026-11-27-couriers/specimen.txt` |
| sha256 | `6a224abc8cc7a5ae...` |
| Author | Sylvia Plath |
| Copyright | in copyright |
| Kind, unit | poem, line |

Two things recorded on the card rather than assumed.

The copyright status is stated, because the Reassembly Test turns on it. Thirteen lines under
a treatment with many sections is the exact case that test was written for: quoting minimally
in every section can still reprint most of a short poem.

The stanza breaks are the compiler operator's. The poem arrived as a single block of thirteen
lines, and the six couplets and closing single line were restored by hand. The card says so
and says they are not verified against an edition. The operator has since confirmed the
couplets from knowledge of the poem, which is recorded here rather than by editing the pinned
specimen, since editing it would change the hash both runs were compiled against.

## Commands

Snapshot, rebuilt because the boot had moved to 0.21:

```
python regression/tools/make-tier1-snapshot.py
```

Reading:

```
python -m dr read --triangulate --voices ASSAY RETICLE \
    --specimen runs/2026-11-27-couriers/specimen.txt \
    --extensions martino --framework tier1-snapshot \
    --out runs/2026-11-27-couriers/reading
```

Workshop:

```
python -m dr workshop --specimen runs/2026-11-27-couriers/specimen.txt \
    --extensions martino --framework tier1-snapshot \
    --out runs/2026-11-27-couriers/workshop
```

## Conditions compiled

| | reading | workshop |
|---|---|---|
| Request line | `Triangulate ASSAY and RETICLE.` | `workshop this specimen` |
| Files | 7 | 8 |
| Characters | 359,319 | 834,057 |
| Token estimate | 89,829 | 208,514 |
| Prompt sha256 | `a8f381e5be1a3f9f` | `d85b7ad74b76a183` |

Reading set: boot, kernel, `0c`, `7`, `15-martino-extraction`, `1-rother-voice-module`,
`3-perloff-voice-module`.

Workshop set: boot, kernel, `0c`, `7`, `12-confinement-inventory`, `15-martino-extraction`,
`3-kowit-voice-module`, `3a-workshop`.

Two voices rather than one, because the friction worth having on this poem is between the
voice that reads reception and canon formation and the voice that reads procedure and the
examined lyric. Whether either fires was left as part of the test.

All voice modules and the workshop ran at Tier 1, headers without corpora, reported as a
fidelity limitation in both outputs.

## Executor

Each prompt went to a separate agent on Claude Opus, in isolation from the other, with no
access to this repository beyond the one prompt file.

Instructions given beyond the prompt, part of the condition and recorded here because they
appear nowhere else:

- Read the prompt file in full before writing anything; read nothing else.
- Use no prior knowledge of a Diagnostic Reader apparatus.
- Whether each voice fires is part of the test, not a premise; a justified stand-down is a
  real result. Where both speak, let the disagreement stand rather than smoothing it.
- The extraction's tools fire on warrant, not on command, and its own failure modes apply.
- The specimen is in copyright and thirteen lines. Run the Reassembly Test on the finished
  output before writing it out and record the result.
- Begin with the loading report.
- The workshop agent was told the specimen is a finished published poem rather than a draft,
  told to check the mode's activation conditions against it, and told that an honest account
  of which sections do not apply is a better result than a filled form.

## Results

Reading, 367 lines. Both voices fired. The second tested its own non-activation case for a
confessional poem and failed it, on the ground that the procedure is the poem rather than a
secondary layer. The two disagree explicitly and the verdict declines to adjudicate.
Extraction tools 3, 4, 5, 6 fired; 1, 2, 7 stood down.

Workshop, 302 lines. The mode's own routing sends a published complete work to the standard
sidecar, which the treatment states before running under the operator command. It declined
sections 11 and 13 entirely and parts of 1, 2, 4, 5, 6 and 12 as inapplicable to a poem that
is not a draft, and recorded that the Output Gate cannot pass as written on this specimen.
Confinement Bay ran in full.

The structural finding both runs rest on is checkable mechanically: question marks at L1, L3,
L5, imperatives at L2, L4, and neither anywhere from L6 to L13. The offer-and-refusal frame
holds identically twice, loses its imperative at the third instance, and is absent for the
last seven lines.

## Checks run by the operator after the fact

The punctuation claim was verified directly against the specimen: questions at 1, 3, 5,
imperatives at 2, 4, both absent from 6 onward.

The Reassembly Test was measured independently rather than taken from the executors' reports.
In both outputs the longest contiguous run of the poem reproduced anywhere is four words,
`do not accept it`. No whole line appears. No two consecutive lines appear. The reading's own
figure was ten words of eighty-three; a looser count that includes incidental overlap in
discussion prose reaches about twenty, still inside the quarter ceiling.

## Limitations

The stanza division is a restoration and any claim resting on the couplet as a unit rests on
it. The workshop output marks this where it occurs and reports section 6's stanza question as
unverifiable rather than answering it.

Both corpora were withheld at Tier 1.

The second voice declared that this poet sits outside the line it ordinarily works, and left
that silence visible rather than reaching.
