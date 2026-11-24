# DIAGNOSTIC READER: REGRESSION READER PROMPT

Generator: dr 0.2.0
Selected cases: R9
Reader model: X (not specified)

You are the Reader, the test subject. For each case, the compiler has performed the load step: the framework files under that case's LOAD SET are the complete file set for that condition, in the boot's load order. Treat each as loaded from the point it appears, resolve cross-references against that set and not against memory of other releases, and where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it. Do not grade yourself. Label each case's output with its test ID and keep the outputs separate.

DELIVERY NOTE (operator). The framework files named in the LOAD SET below are attached to
this message as files rather than pasted inline. They are loaded. Read them in the LOAD
SET's step order. Nothing else is loaded: no file outside that table is in this condition,
whatever any loaded file says about it. Everything else in this prompt, the instructions,
the manifest, the specimen, and the request, is below.
========================================================================================
R9: TARGET INSTRUCTIONS
========================================================================================

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

========================================================================================
R9: CONDITION MANIFEST (reader-facing)
========================================================================================

```json
{
  "canonical_work": "A benchmark-corpus poem the model names under Scan Mode (C1 to C7); no text supplied",
  "condition": "full-framework baseline",
  "corpus_id": "SCAN",
  "primary_question": "Follow Scan Mode; distinguish remembered or reconstructed text from supplied or verified text; never reproduce a poem whole.",
  "request": {
    "scan_category": "A",
    "scan_devices": [
      "apostrophe"
    ],
    "scan_source": "canon",
    "task": "scan"
  },
  "schema_version": "2.0",
  "specimen": {
    "note": "Scan Mode names its specimen from the model's knowledge and rates reconstruction strength. The complete poem must not be supplied.",
    "path": null,
    "status": "none by design: a canon scan supplies no poem text"
  },
  "task_specific_load_rule": "The compiler performed the load step. The files under this case's LOAD SET are the complete condition. Report which of them you used; where a procedure needs a file that is not in the set, say so and switch the procedure off rather than rebuild it.",
  "test_card": "R9",
  "test_id": "R9",
  "title": "Canon scan and reconstruction discipline"
}
```

========================================================================================
R9: LOAD SET
========================================================================================

```text
step file                                               version  sha256          
0    0-poetics-boot-hollow-v0_18.md                     0.18     ab05bfe117143886
1    0a-portable-poetics-kernel-v0_3_19.md              0.3.19   2f408d84625414dd
2    0c-voice-designations-v0_7.md                      0.7      ab0b2e67da17db4c
4    7-device-inventory-extended-v0_4.md                0.4      4dde79df1df0c4b3
```

========================================================================================
R9: SPECIMEN
========================================================================================

No specimen text is supplied for this condition. A canon scan names its own specimen from the model's knowledge, under Scan Mode's rules.

========================================================================================
R9: LOAD SET, REPEATED
========================================================================================

The complete file set for R9, as at the top of the case. A file the apparatus names that is not in this table is absent from this condition; the loading report names it as absent, not as used.

```text
step file                                               version  sha256          
0    0-poetics-boot-hollow-v0_18.md                     0.18     ab05bfe117143886
1    0a-portable-poetics-kernel-v0_3_19.md              0.3.19   2f408d84625414dd
2    0c-voice-designations-v0_7.md                      0.7      ab0b2e67da17db4c
4    7-device-inventory-extended-v0_4.md                0.4      4dde79df1df0c4b3
```

========================================================================================
R9: OPERATOR REQUEST
========================================================================================

Scan canon A for apostrophe
