# DIAGNOSTIC READER: REGRESSION READER PROMPT

Generator: dr 0.2.0
Selected cases: R4

You are the Reader, the test subject. For each case, the compiler has performed the load step: the framework files under that case's LOAD SET are the complete file set for that condition, in the boot's load order. Treat each as loaded from the point it appears, resolve cross-references against that set and not against memory of other releases, and where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it. Do not grade yourself. Label each case's output with its test ID and keep the outputs separate.

DELIVERY NOTE (operator). The framework files named in the LOAD SET below are attached to
this message as files rather than pasted inline. They are loaded. Read them in the LOAD
SET's step order. Nothing else is loaded: no file outside that table is in this condition,
whatever any loaded file says about it. Everything else in this prompt, the instructions,
the manifest, the specimen, and the request, is below.
========================================================================================
R4: TARGET INSTRUCTIONS
========================================================================================

# TARGET PROMPT — R4: Framing, irony, and epistemic boundaries

You are the target model in a controlled Diagnostic Reader regression test.

Read the reader-facing condition manifest and the LOAD SET for this case first. The compiler performed the load step: the framework files under the LOAD SET are the complete condition, in the boot's load order, and `0-poetics-boot-hollow` is the entry point among them. Do not infer a file's contents from its name or treat a module as loaded because the apparatus mentions it. The regression suite and prompt regime are test-control documents, not Diagnostic Reader runtime modules.

**Task:** Perform a Diagnostic Reader analysis of the supplied specimen: **Ozymandias**. Use only the specimen text supplied under this case's SPECIMEN section; its edition and sha256 are in the condition manifest.

**Test focus:** Separate frame, reported inscription, description, inference, and history.

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

Task: Analyze “Ozymandias” using the supplied Diagnostic Reader.

Requirements:
- Track the relevant framing levels and identify who reports or presents each consequential statement.
- Distinguish the inscription's claims from the poem's framing and from the reader's inference.
- Analyze irony or contradiction through textual evidence and the relation between the frame, the reported artifact, and its present condition.
- Do not collapse the different layers of reporting into one undifferentiated speaker or factual voice.
- Do not present the poem's implications as independently verified historical facts.

Focus of this test: framing, irony, reporting layers, and epistemic boundaries.

## Required output
1. **Input and loading report:** test ID, specimen received, and the LOAD SET table copied out with each file marked used or unused. A file the apparatus mentions that is not in the LOAD SET is absent; name it as absent, never as used. Then any unresolved loading or dependency issue.
2. **Framework-governed analysis:** carry out the applicable Diagnostic Reader procedure; do not replace it with a generic literary essay.
3. **Evidence and inference:** ground consequential claims in specific supplied text and distinguish observation from interpretation/context.
4. **Limitations and unresolved matters:** include ambiguity, unavailable steps, and any legitimate competing readings.
5. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.

========================================================================================
R4: CONDITION MANIFEST (reader-facing)
========================================================================================

```json
{
  "canonical_work": "Ozymandias",
  "condition": "full-framework baseline",
  "corpus_id": "C3",
  "primary_question": "Separate frame, reported inscription, description, inference, and history.",
  "request": {
    "task": "sidecar",
    "voices": [
      "ASSAY"
    ]
  },
  "schema_version": "2.0",
  "specimen": {
    "author_attribution": "Percy Bysshe Shelley",
    "edition_or_source": "User-supplied transcription in specimens.txt; bibliographic source/edition not supplied.",
    "normalization_note": "Section separators and leading/trailing blank lines removed; poem text, punctuation, capitalization, and internal lineation otherwise preserved from supplied transcription.",
    "path": "specimen.txt",
    "sha256": "7eef00270119ee66c9def0d6f24a24a24d2fe405a814c0bc97096d0e18b0216d",
    "source_status": "public domain",
    "status": "populated from user-supplied specimens.txt; transcription frozen; source edition not independently verified",
    "work_title": "Ozymandias"
  },
  "task_specific_load_rule": "The compiler performed the load step. The files under this case's LOAD SET are the complete condition. Report which of them you used; where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it.",
  "test_card": "R4",
  "test_id": "R4",
  "title": "Framing, irony, and epistemic boundaries"
}
```

========================================================================================
R4: LOAD SET
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
R4: SPECIMEN: Ozymandias (sha256 7eef00270119ee66)
========================================================================================

```text
Title:             Ozymandias
Author:            Percy Bysshe Shelley
Edition or source: User-supplied transcription in specimens.txt; bibliographic source/edition not supplied.
Source status:     public domain
Kind:              poem
Unit:              line
Length:            15 lines
```

```text
Ozymandias

I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert. Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them and the heart that fed:
And on the pedestal these words appear:
"My name is Ozymandias, king of kings:
Look on my works, ye Mighty, and despair!"
Nothing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away.
```

========================================================================================
R4: LOAD SET, REPEATED
========================================================================================

The complete file set for R4, as at the top of the case. A file the apparatus names that is not in this table is absent from this condition; the loading report names it as absent, not as used.

```text
step file                                               version  sha256          
0    0-poetics-boot-hollow-v0_18.md                     0.18     ab05bfe117143886
1    0a-portable-poetics-kernel-v0_3_19.md              0.3.19   2f408d84625414dd
2    0c-voice-designations-v0_7.md                      0.7      ab0b2e67da17db4c
4    7-device-inventory-extended-v0_4.md                0.4      4dde79df1df0c4b3
5    1-rother-voice-module-v0_3_1.md                    0.3.1    a2fdc58df8051e7a
```

========================================================================================
R4: OPERATOR REQUEST
========================================================================================

Full sidecar. ASSAY verdict.
