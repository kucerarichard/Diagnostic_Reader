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
