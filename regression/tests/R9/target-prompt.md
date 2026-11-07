# TARGET PROMPT — R9: Canon scan and reconstruction discipline

You are the target model in a controlled Diagnostic Reader regression test.

Read the reader-facing condition manifest and the LOAD SET for this case first. The compiler performed the load step: the framework files under the LOAD SET are the complete condition, in the boot's load order, and `0-poetics-boot-hollow` is the entry point among them. Do not infer a file's contents from its name or treat a module as loaded because the apparatus mentions it. The regression suite and prompt regime are test-control documents, not Diagnostic Reader runtime modules.

**Task:** Run the Scan Mode request under this case's OPERATOR REQUEST, following Section K of the extended device inventory. No poem text is supplied; a canon scan names its specimen from your own knowledge. Restrict the canon to the benchmark corpus (C1 to C7 in the regression suite: Blake's "The Tyger" and "London", Shelley's "Ozymandias", Dickinson's "Because I could not stop for Death", Browning's "My Last Duchess", Poe's "The Raven", Yeats's "The Second Coming").

**Test focus:** Follow Scan Mode; distinguish remembered or reconstructed text from supplied or verified text; never reproduce a poem whole.

**Requirements:**
- Follow Scan Mode's output form for a canon catch: provenance (author, title, standard reference), device verification at the lowest exposure level that preserves the mechanism, reconstruction strength (strong, weak, or asymmetric), and the consensus-smoothing flag.
- Do not imply that you inspected your own training corpus or any source outside this prompt.
- Do not claim exact wording has been verified. Nothing in this condition supplies a text to verify against; mark every quoted phrase as reconstructed from memory.
- Do not reproduce the complete poem. Quote at Level 1 or 2 only, as many located quotes as device verification needs and no more, and pass the reassembly test.
- An empty scan is a result. If no benchmark poem carries the device with reasonable confidence, report the empty scan and stop; do not relax the criteria or fabricate a candidate.
- Do not invent rules or silently compensate for missing modules.
- Report which files in the LOAD SET you used and which you did not.

## Test-card requirements (verbatim from the supplied prompt regime)

### Test-run card

Task: Run the supplied Scan Mode request against the benchmark corpus without being given any poem text.

Requirements:
- Name the specimen you select, with author, title, and a standard reference a reader can use to reach the text.
- Verify the named device in the specimen at the lowest exposure level that preserves the mechanism, and mark every quotation as reconstructed from memory.
- Rate reconstruction strength as strong, weak, or asymmetric, and say what the rating rests on.
- Flag consensus smoothing where the reading averages existing readings rather than reading the page.
- Do not reproduce the complete poem, and do not claim verification against a text that was not supplied.
- If the device is not carried with reasonable confidence, report an empty scan and stop.

Focus of this test: source discipline when the only source is memory, honest reconstruction rating, and refusal to turn familiarity into false source access.

## Required output
1. **Input and loading report:** test ID, the request received, and the LOAD SET table copied out with each file marked used or unused. A file the apparatus mentions that is not in the LOAD SET is absent; name it as absent, never as used. Then any unresolved loading or dependency issue.
2. **Scan catch or empty scan:** the Scan Mode output form, or the empty-scan report.
3. **Sidecar on the catch:** at extended-inventory resolution, within the quotation limits above.
4. **Limitations and unresolved matters:** what memory could not establish, and any competing candidates.
5. **Self-audit:** list any required procedure you could not verify or complete and why.

Do not grade yourself, assign pass/fail, or recommend framework changes. Return the raw test artifact only.
