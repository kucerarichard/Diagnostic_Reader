# DIAGNOSTIC READER: REGRESSION READER PROMPT

Generator: dr 0.2.0
Selected cases: R2
Reader model: X (not specified)

You are the Reader, the test subject. For each case, the compiler has performed the load step: the framework files under that case's LOAD SET are the complete file set for that condition, in the boot's load order. Treat each as loaded from the point it appears, resolve cross-references against that set and not against memory of other releases, and where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it. Do not grade yourself. Label each case's output with its test ID and keep the outputs separate.

DELIVERY NOTE (operator). The framework files named in the LOAD SET below are attached to
this message as files rather than pasted inline. They are loaded. Read them in the LOAD
SET's step order. Nothing else is loaded: no file outside that table is in this condition,
whatever any loaded file says about it. Everything else in this prompt, the instructions,
the manifest, the specimen, and the request, is below.
========================================================================================
R2: TARGET INSTRUCTIONS
========================================================================================

# TARGET PROMPT — R2: Device inventory and mechanism-first reasoning

You are the target model in a controlled Diagnostic Reader regression test.

Read the reader-facing condition manifest and the LOAD SET for this case first. The compiler performed the load step: the framework files under the LOAD SET are the complete condition, in the boot's load order, and `0-poetics-boot-hollow` is the entry point among them. Do not infer a file's contents from its name or treat a module as loaded because the apparatus mentions it. The regression suite and prompt regime are test-control documents, not Diagnostic Reader runtime modules.

**Task:** Perform a Diagnostic Reader analysis of the supplied specimen: **The Tyger**. Use only the specimen text supplied under this case's SPECIMEN section; its edition and sha256 are in the condition manifest.

**Test focus:** Check device inventory and explain mechanisms before interpretation.

**Requirements:**
- Follow the applicable procedures and dependencies in the supplied Diagnostic Reader files.
- Distinguish explicit textual evidence, inference, and any contextual/historical claims.
- Identify any missing, inaccessible, contradictory, or version-mismatched dependencies before relying on them.
- Do not invent rules or silently compensate for missing modules.
- If only part of the analysis can be completed, say exactly what can and cannot be established and proceed only within the available specification.
- Cite the actual framework file and section/rule for consequential procedural choices where practical.
- Report which files in the LOAD SET you used and which you did not.

## Test-card requirements (verbatim from the supplied prompt regime)

### Test-run card

Task: Analyze “The Tyger” using the supplied Diagnostic Reader.

Requirements:
- Follow the framework's device-inventory procedure, including its prescribed scope and sequence.
- Identify relevant textual devices before offering conclusions that depend on them.
- Explain how the identified devices operate in the poem: repetition, question structure, sound, imagery, contrast, syntax, or other mechanisms where supported by the text and required by the framework.
- Connect interpretive claims to identifiable textual evidence and explain the mechanism linking evidence to claim.
- Do not treat a list of device names as sufficient analysis.
- Do not invent a mandatory inventory format if the supplied framework does not specify one.

Focus of this test: inventory completeness, mechanism-first reasoning, and whether the output bypasses required intermediate steps.

## Required output
1. **Input and loading report:** test ID, specimen received, and the LOAD SET table copied out with each file marked used or unused. A file the apparatus mentions that is not in the LOAD SET is absent; name it as absent, never as used. Then any unresolved loading or dependency issue.
2. **Framework-governed analysis:** carry out the applicable Diagnostic Reader procedure; do not replace it with a generic literary essay.
3. **Evidence and inference:** ground consequential claims in specific supplied text and distinguish observation from interpretation/context.
4. **Limitations and unresolved matters:** include ambiguity, unavailable steps, and any legitimate competing readings.
5. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.

========================================================================================
R2: CONDITION MANIFEST (reader-facing)
========================================================================================

```json
{
  "canonical_work": "The Tyger",
  "condition": "full-framework baseline",
  "corpus_id": "C1",
  "primary_question": "Check device inventory and explain mechanisms before interpretation.",
  "request": {
    "task": "sidecar",
    "voices": [
      "ASSAY"
    ]
  },
  "schema_version": "2.0",
  "specimen": {
    "author_attribution": "William Blake",
    "edition_or_source": "User-supplied transcription in specimens.txt; bibliographic source/edition not supplied.",
    "normalization_note": "Section separators and leading/trailing blank lines removed; poem text, punctuation, capitalization, and internal lineation otherwise preserved from supplied transcription.",
    "path": "specimen.txt",
    "sha256": "f115345237e15c49116904ea7f3bde94ccf6688012c325e0c828132e351777cb",
    "source_status": "public domain",
    "status": "populated from user-supplied specimens.txt; transcription frozen; source edition not independently verified",
    "work_title": "The Tyger"
  },
  "task_specific_load_rule": "The compiler performed the load step. The files under this case's LOAD SET are the complete condition. Report which of them you used; where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it.",
  "test_card": "R2",
  "test_id": "R2",
  "title": "Device inventory and mechanism-first reasoning"
}
```

========================================================================================
R2: LOAD SET
========================================================================================

```text
step file                                               version  sha256          
0    0-poetics-boot-hollow-v0_18.md                     0.18     ab05bfe117143886
1    0a-portable-poetics-kernel-v0_3_19.md              0.3.19   2f408d84625414dd
2    0c-voice-designations-v0_7.md                      0.7      ab0b2e67da17db4c
4    7-device-inventory-extended-v0_4.md                0.4      4dde79df1df0c4b3
5    1-rother-voice-module-v0_3_1.md                    0.3.1    a2fdc58df8051e7a
```

========================================================================================
R2: SPECIMEN: The Tyger (sha256 f115345237e15c49)
========================================================================================

```text
Title:             The Tyger
Author:            William Blake
Edition or source: User-supplied transcription in specimens.txt; bibliographic source/edition not supplied.
Source status:     public domain
Kind:              poem
Unit:              line
Length:            25 lines
```

```text
The Tyger

Tyger! Tyger! burning bright
In the forests of the night,
What immortal hand or eye
Could frame thy fearful symmetry?

In what distant deeps or skies
Burnt the fire of thine eyes?
On what wings dare he aspire?
What the hand, dare sieze the fire?

And what shoulder, & what art,
Could twist the sinews of thy heart?
And when thy heart began to beat,
What dread hand? & what dread feet?

What the hammer? what the chain?
In what furnace was thy brain?
What the anvil? what dread grasp
Dare its deadly terrors clasp?

When the stars threw down their spears,
And water’d heaven with their tears,
Did he smile his work to see?
Did he who made the Lamb make thee?

Tyger! Tyger! burning bright
In the forests of the night,
What immortal hand or eye
Dare frame thy fearful symmetry?
```

========================================================================================
R2: LOAD SET, REPEATED
========================================================================================

The complete file set for R2, as at the top of the case. A file the apparatus names that is not in this table is absent from this condition; the loading report names it as absent, not as used.

```text
step file                                               version  sha256          
0    0-poetics-boot-hollow-v0_18.md                     0.18     ab05bfe117143886
1    0a-portable-poetics-kernel-v0_3_19.md              0.3.19   2f408d84625414dd
2    0c-voice-designations-v0_7.md                      0.7      ab0b2e67da17db4c
4    7-device-inventory-extended-v0_4.md                0.4      4dde79df1df0c4b3
5    1-rother-voice-module-v0_3_1.md                    0.3.1    a2fdc58df8051e7a
```

========================================================================================
R2: OPERATOR REQUEST
========================================================================================

Full sidecar. ASSAY verdict.
