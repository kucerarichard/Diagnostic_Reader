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
