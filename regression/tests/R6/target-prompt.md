# TARGET PROMPT — R6: Speaker, person, and coercion

You are the target model in a controlled Diagnostic Reader regression test.

Read the reader-facing condition manifest and the LOAD SET for this case first. The compiler performed the load step: the framework files under the LOAD SET are the complete condition, in the boot's load order, and `0-poetics-boot-hollow` is the entry point among them. Do not infer a file's contents from its name or treat a module as loaded because the apparatus mentions it. The regression suite and prompt regime are test-control documents, not Diagnostic Reader runtime modules.

**Task:** Perform a Diagnostic Reader analysis of the supplied specimen: **My Last Duchess**. Use only the specimen text supplied under this case's SPECIMEN section; its edition and sha256 are in the condition manifest.

**Test focus:** Distinguish dramatic speaker from author; ground power claims.

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

Task: Analyze “My Last Duchess” using the supplied Diagnostic Reader.

Requirements:
- Apply the actual designation and voice-related rules in the supplied framework.
- Distinguish the speaker's claims about himself, the Duchess, and the past from what the poem independently establishes.
- Analyze how the speech presents power, control, status, or coercion where supported by the text.
- Ground judgments in wording, structure, and the interaction between speaker and implied audience.
- Do not treat the dramatic speaker's assertions as automatically reliable facts.
- Do not diagnose, moralize, or infer biography beyond what the text and framework support.

Focus of this test: speaker versus author, self-presentation versus evidence, and jurisdiction over claims about persons.

## Required output
1. **Input and loading report:** test ID, specimen received, and the LOAD SET table copied out with each file marked used or unused. A file the apparatus mentions that is not in the LOAD SET is absent; name it as absent, never as used. Then any unresolved loading or dependency issue.
2. **Framework-governed analysis:** carry out the applicable Diagnostic Reader procedure; do not replace it with a generic literary essay.
3. **Evidence and inference:** ground consequential claims in specific supplied text and distinguish observation from interpretation/context.
4. **Limitations and unresolved matters:** include ambiguity, unavailable steps, and any legitimate competing readings.
5. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.
