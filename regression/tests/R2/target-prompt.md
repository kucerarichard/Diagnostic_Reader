# TARGET PROMPT — R2: Device inventory and mechanism-first reasoning

You are the target model in a controlled Diagnostic Reader regression test.

Read `manifest.json` first. Use `0-poetics-boot-hollow-v0_18.md` as the entry point and follow its load order and file-reference rule. Inspect the actual files available in this condition; do not infer file contents from names or claim a module was loaded merely because it is listed. Treat the regression suite and prompt regime as test-control documents, not as Diagnostic Reader runtime modules.

**Task:** Perform a Diagnostic Reader analysis of the supplied specimen: **The Tyger**. Use only the specimen actually attached or readable in the package. The specimen's exact source/edition should be recorded in the manifest.

**Test focus:** Check device inventory and explain mechanisms before interpretation.

**Requirements:**
- Follow the applicable procedures and dependencies in the supplied Diagnostic Reader files.
- Distinguish explicit textual evidence, inference, and any contextual/historical claims.
- Identify any missing, inaccessible, contradictory, or version-mismatched dependencies before relying on them.
- Do not invent rules or silently compensate for missing modules.
- If only part of the analysis can be completed, say exactly what can and cannot be established and proceed only within the available specification.
- Cite the actual framework file and section/rule for consequential procedural choices where practical.
- Report the exact files you could inspect and which you actually used. State any ZIP/archive reading limitation honestly.

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
1. **Input and loading report:** test ID, specimen received, files actually inspected/used, and unresolved loading/dependency issues.
2. **Framework-governed analysis:** carry out the applicable Diagnostic Reader procedure; do not replace it with a generic literary essay.
3. **Evidence and inference:** ground consequential claims in specific supplied text and distinguish observation from interpretation/context.
4. **Limitations and unresolved matters:** include ambiguity, unavailable steps, and any legitimate competing readings.
5. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.
