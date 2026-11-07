# TARGET PROMPT — R11: Record against account

You are the target model in a controlled Diagnostic Reader regression test.

Read the reader-facing condition manifest and the LOAD SET for this case first. The compiler performed the load step: the framework files under the LOAD SET are the complete condition, in the boot's load order, and `0-poetics-boot-hollow` is the entry point among them. Do not infer a file's contents from its name or treat a module as loaded because the apparatus mentions it. The regression suite and prompt regime are test-control documents, not Diagnostic Reader runtime modules.

**Task:** Deliver a DATUM reading of the supplied specimen, **The Raven**, measured against the supplied account, **The Philosophy of Composition**, the poet's own description of how the poem was composed. Use only the specimen text under this case's SPECIMEN section and the account text under its ACCOUNT section; both are pinned by sha256 in the condition manifest.

**Test focus:** Measure the account against the poem and the record, grading each claim on the provenance ladder, without taking the account as fact or dismissing it as performance.

**Requirements:**
- Follow the DATUM module's procedure and the provenance-grading extension's ladder as supplied. The account is held at P2: a claim about the specimen, not evidence about it.
- Take the account's claims one at a time where they can be measured against the poem's text (length, refrain, the chosen sound, the placement of the climax, the locale, the order of composition) and grade each: confirmed by the page, consistent with the page, unverifiable from the page, or contradicted by it.
- Where a claim about the order or method of composition cannot be measured against the page at all, say so and grade it as what the account alone supplies. Do not import biographical or critical testimony that is not in the supplied files.
- Do not resolve the account's standing by its reputation. A reading that calls it a hoax, or takes it at its word, without working through the claims has substituted a verdict for a measurement.
- The device inventory extension is not loaded in this condition; name devices at the kernel's lite resolution only, and say so if a finer name would have changed a grade.
- Render the verdict as DATUM under Voice Rendering Mode, labelled by designation.
- Do not invent rules or silently compensate for missing modules.
- Report which files in the LOAD SET you used and which you did not.

## Test-card requirements (verbatim from the supplied prompt regime)

### Test-run card

Task: Read "The Raven" against "The Philosophy of Composition" under the DATUM module.

Requirements:
- Hold the account at P2 and grade each measurable claim against the poem's text on the supplied ladder.
- Separate what the page confirms, what it is consistent with, what it cannot speak to, and what it contradicts.
- Grade claims about the order and method of composition as the account's own testimony, since the page cannot measure them, and say so.
- Do not import testimony that is not in the supplied files.
- Do not settle the account's standing by reputation in either direction.
- Render the verdict as DATUM, labelled by designation, and let the account's unverifiable remainder stand as a finding.

Focus of this test: measurement against a record, the provenance ladder applied claim by claim, and the voice's refusal to interpret where it was asked to measure.

## Required output
1. **Input and loading report:** test ID, specimen and account received, and the LOAD SET table copied out with each file marked used or unused. A file the apparatus mentions that is not in the LOAD SET is absent; name it as absent, never as used. Then any unresolved loading or dependency issue.
2. **The reading:** the DATUM output form as the module supplies it, with the claim-by-claim grades.
3. **Limitations and unresolved matters:** what the page could not measure, and what the absence of the device inventory cost.
4. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.
