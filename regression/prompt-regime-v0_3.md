# Diagnostic Reader Regression Suite
## Prompt Regime — v0.3, for suite v0.7

**Revision 0.3:** Removes PART II and PART III, the evaluator and adjudicator master prompts, matching suite v0.7. The remaining parts renumber: the test cards become PART II and the synthesis becomes PART III. Each card's `Evaluator criteria` becomes `Scoring criteria` and its `Adjudication focus` becomes `Verification focus`; the criteria themselves are unchanged, and the operator now applies them. R10's cross-variant section is renamed to match.

**Revision 0.2:** Adds the R11 card and amends R5, R7, and R8 to state their voice and mode conditions, matching suite v0.6. Revision 0.1 (the v0.5 compatible draft) had rewritten R9 from an image scan to the text canon scan the suite defines.

**Purpose:** Test reliable execution of the Diagnostic Reader, identify which instructions and dependencies must be explicit or externalized, and determine which framework changes are justified by observed failures.

**Role separation**
1. Target model: performs the test.
2. Operator: scores the artifact against the card's criteria and verifies cited rules in the pinned files.
3. Framework-change analysis: identifies justified changes without silently rewriting the framework.

Do not treat a model's judgment as automatically authoritative, your own reading of it included. Suite section 8 states the rules that make a single reader trustworthy; the first of them is to write the standard before reading the artifact.

---

# PART I — TEST-RUN MASTER PROMPT

Paste this first, followed by exactly one test card from Part II and the required framework files.

## TEST-RUN PROMPT

You are the **target model** in a controlled regression test of the Diagnostic Reader framework.

### Objective

Execute the supplied test card using the supplied version of the Diagnostic Reader. The goal is not merely to produce a good literary interpretation. The goal is to determine whether you can follow the framework's actual procedures, distinctions, dependencies, evidence requirements, and output constraints under the specified conditions.

### Authority and source rules

1. Treat the supplied Diagnostic Reader files and their declared relationships as the governing specification.
2. Do not invent rules, modules, file contents, or required procedures that are not present in the supplied materials.
3. Do not silently repair contradictions or fill missing dependencies from general knowledge. Identify material gaps when they affect execution.
4. If a required file is absent, unavailable, or ambiguous, state exactly what is missing and what consequence it has. Continue only to the extent permitted by the test condition.
5. Distinguish textual observation, source-backed fact, framework rule, inference, and interpretation. Do not present an inference as a textual fact.
6. Use the supplied poem text or the specified public-domain edition. Do not silently substitute a different version. If the test requires a scan or incomplete text, respect that limitation.
7. Do not claim to have loaded, consulted, or verified a file that was not actually supplied or accessible in this run.
8. Do not optimize for what you think a grader wants. Execute the stated procedure and make your reasoning and evidence auditable.

### Test integrity

- Follow the assigned test card exactly.
- Do not consult another model's output or any scoring material.
- Do not infer withheld instructions from earlier test runs.
- Do not add procedures merely because they would normally be useful if the test explicitly removes or withholds them.
- Do not conceal a missing dependency by reconstructing it from memory.
- Do not confuse a plausible literary reading with evidence of procedural compliance.

### Required output

Organize your response under these headings:

1. **Test identification** — card ID, test condition, framework version, and files actually available.
2. **Availability and dependency report** — which required materials were present, absent, ambiguous, or conflicting.
3. **Execution** — perform the task specified by the card.
4. **Evidence trail** — identify the supplied text, framework rule, or observable output supporting each material claim. Give exact quotations or section names when available; do not fabricate line numbers or citations.
5. **Uncertainty and limitations** — identify what cannot be established from the available evidence.
6. **Self-audit** — briefly check whether your output followed the supplied procedure, respected the test condition, and avoided unsupported claims.

The self-audit is part of the target artifact, not an authoritative score. The operator assesses the output separately and does not treat the self-audit as evidence.

Do not revise the framework itself during this run. If you encounter a suspected defect, report it as a suspected defect and explain the evidence.

---

# PART II — THE REGRESSION TEST CARDS

For each run, append one card below to the Test-Run Master Prompt. Score against that same card.

Use a pinned version of the framework for every run. For reproducibility, record the exact file names and versions supplied, the poem edition/text, the model, and any condition that changes which instructions are available.

## R1 — Bootstrap and designation integrity

**Canonical work:** William Blake, “The Tyger”

**Primary question:** Does the model load and apply the framework's actual bootstrap and designation rules, rather than assigning roles or voices by intuition?

### Test-run card

Task: Perform the Diagnostic Reader analysis of “The Tyger” using the supplied framework.

Requirements:
- Identify which supplied bootstrap and designation rules govern the analysis.
- Apply the actual designation policy before making downstream claims that depend on it.
- Distinguish what the poem explicitly establishes from what you infer about speaker, addressee, voice, or role.
- Where designation is uncertain, follow the framework's prescribed uncertainty or fallback procedure rather than silently selecting the most convenient interpretation.
- Provide the evidence and applicable framework rule for each consequential designation.
- Do not invent designation rules absent from the supplied files.

Focus of this test: bootstrap integrity, designation order, evidence for designation, and handling of ambiguity.

### Scoring criteria

Score:
1. Correct identification of available bootstrap and designation instructions.
2. Compliance with the actual designation procedure and order.
3. Evidence supporting consequential assignments.
4. Appropriate handling of uncertainty.
5. No substitution of intuition for an explicit governing rule.

Use DESIGNATION, LOAD, or COLLAPSE only when supported.

### Verification focus

Verify the cited rules against the supplied files. Decide whether an incorrect assignment reflects target execution, a missing policy, a contradictory rule, or legitimate ambiguity in the poem. Do not require a single literary designation if the framework permits uncertainty or competing interpretations.

---

## R2 — Device inventory and mechanism-first analysis

**Canonical work:** William Blake, “The Tyger”

**Primary question:** Does the model perform the required device inventory and explain mechanisms before jumping to broad thematic conclusions?

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

### Scoring criteria

Score:
1. The required inventory is present and follows the supplied procedure.
2. Devices are accurately identified and grounded in the text.
3. Mechanisms are explained rather than merely named.
4. Interpretive conclusions follow from evidence and mechanism.
5. No premature thematic summary substitutes for required analysis.

Use INVENTORY or COLLAPSE where supported.

### Verification focus

Distinguish a genuine inventory omission from a legitimate difference in which devices matter. Check the actual framework to determine what is mandatory. A concise inventory can pass if it satisfies the specification; length alone is not evidence of compliance.

---

## R3 — Coercion engine and residue

**Canonical work:** William Blake, “London”

**Primary question:** Does the model identify how the poem's language and form enact coercion, rather than merely naming oppression as its theme?

### Test-run card

Task: Analyze “London” using the supplied Diagnostic Reader.

Requirements:
- Identify the textual mechanisms relevant to coercion, constraint, repetition, institutional power, or restricted agency, as warranted by the text and framework.
- Explain how those mechanisms operate, using specific words, phrases, formal features, or relations within the poem.
- Distinguish the poem's mechanism of action from the thematic or emotional effect it produces.
- Identify any residue, contradiction, limit, or unresolved remainder that the framework requires the analysis to preserve.
- Do not force every feature into a single explanation. Do not claim historical facts beyond the evidence and framework's provenance rules.

Focus of this test: mechanism versus theme, causal explanation, and preservation of meaningful residue.

### Scoring criteria

Score:
1. Textual evidence for the proposed coercive mechanisms.
2. Clear distinction between mechanism and theme.
3. Explanation of how language/form produces the claimed effect.
4. Treatment of residue or unresolved material according to the supplied framework.
5. Appropriate boundaries on historical or contextual claims.

Use INVENTORY, COLLAPSE, or PROVENANCE where supported.

### Verification focus

Check whether the alleged mechanism is actually evidenced in the text. A different but textually supported mechanism may be valid. Penalize unsupported causal claims, not interpretive difference by itself. Determine whether any omission reflects the framework's requirements or merely your preferred reading.

---

## R4 — Framing, irony, and epistemic boundaries

**Canonical work:** Percy Bysshe Shelley, “Ozymandias”

**Primary question:** Does the model preserve the distinction between the framed speaker's report, the inscription, the described artifact, and the larger interpretive frame?

### Test-run card

Task: Analyze “Ozymandias” using the supplied Diagnostic Reader.

Requirements:
- Track the relevant framing levels and identify who reports or presents each consequential statement.
- Distinguish the inscription's claims from the poem's framing and from the reader's inference.
- Analyze irony or contradiction through textual evidence and the relation between the frame, the reported artifact, and its present condition.
- Do not collapse the different layers of reporting into one undifferentiated speaker or factual voice.
- Do not present the poem's implications as independently verified historical facts.

Focus of this test: framing, irony, reporting layers, and epistemic boundaries.

### Scoring criteria

Score:
1. Correct handling of the poem's reporting/frame structure.
2. Distinction between inscription, report, description, and inference.
3. Evidence-based account of irony or contradiction.
4. Preservation of uncertainty and epistemic limits.
5. No unsupported historical or speaker claims.

Use DESIGNATION, COLLAPSE, PROVENANCE, or JURISDICTION only where applicable and supported.

### Verification focus

Check whether the model distinguishes the text's reported claims from claims the poem itself establishes. Do not impose a single interpretation of irony when multiple readings are supported. Determine whether a layer collapse is a real procedural breach or an acceptable analytical compression under the framework.

---

## R5 — Coscienza and ambiguity

**Canonical work:** Emily Dickinson, “Because I could not stop for Death”

**Primary question:** Does the model use the framework's Coscienza procedure to preserve ambiguity without collapsing it into either certainty or an unstructured list of possibilities?

### Test-run card

Task: Analyze “Because I could not stop for Death” using the supplied Diagnostic Reader.

Requirements:
- Apply the supplied Coscienza procedure as written. Identify the applicable rules or fields rather than inventing a new definition.
- Ground interpretations in exact textual features.
- Preserve material ambiguity where the text does not settle a question.
- Distinguish competing hypotheses, evidence supporting them, and the limits of each.
- Do not mistake ambiguity for permission to make unsupported claims.
- Do not force a definitive answer merely to make the analysis appear complete.

- This condition loads ASSAY and RETICLE. Each voice stands up or down on the specimen’s own properties, speaks in its own person under its designation, and a stand-down is a result to report. Open Triangulated Commentary with the common-ground line.

Focus of this test: fidelity to the supplied Coscienza procedure, structured ambiguity, and disciplined inference.

### Scoring criteria

Score:
1. Accurate application of the supplied Coscienza instructions.
2. Textual grounding of consequential interpretations.
3. Clear separation of evidence, hypothesis, and uncertainty.
4. Preservation of genuine ambiguity without arbitrary indecision.
5. No invented Coscienza rules or forced resolution.

6. Voice jurisdiction: RETICLE’s firing or stand-down justified by the specimen; each voice in its own person; common-ground line present.

Use COLLAPSE or PROVENANCE if supported. If the Coscienza definition or module is absent, assess LOAD/dependency handling rather than guessing the intended procedure.

### Verification focus

First verify what the supplied framework actually says Coscienza requires. Do not grade against an assumed meaning. If the relevant definition is missing or ambiguous, distinguish a target-model failure from a dependency or framework-specification problem. Preserve literary disagreement where the evidence does not settle it.

---

## R6 — Speaker, person, and coercion

**Canonical work:** Robert Browning, “My Last Duchess”

**Primary question:** Does the model distinguish the dramatic speaker's self-presentation from the poem's evidence about that speaker, and apply the framework's voice/jurisdiction rules?

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

### Scoring criteria

Score:
1. Correct use of designation and voice rules.
2. Separation of speaker assertion from textual evidence.
3. Mechanism-based analysis of power or coercion.
4. Appropriate handling of claims about persons and intent.
5. No unsupported biographical or psychological assertions.

Use DESIGNATION, JURISDICTION, COLLAPSE, or PROVENANCE when supported.

### Verification focus

Determine whether the target improperly treats a speaker's account as objective fact or exceeds the framework's jurisdiction. Do not require a particular moral characterization. A defensible interpretation of the speaker's rhetoric can differ while still complying with the procedure.

---

## R7 — Repetition and rendering restraint

**Canonical work:** Edgar Allan Poe, “The Raven”

**Primary question:** Does the model analyze repetition and sound without turning every recurrence into the same symbolic claim or overproducing unsupported effects?

### Test-run card

Task: Analyze “The Raven” using the supplied Diagnostic Reader.

Requirements:
- Apply the supplied device-inventory and output/rendering rules.
- Identify relevant repetitions, sound patterns, refrains, or structural recurrences with specific textual evidence.
- Explain the function of those features in context rather than assuming that recurrence always has one fixed meaning.
- Distinguish audible/formal effects from inferred psychological or symbolic effects.
- Keep the output proportionate to the evidence and follow any supplied constraints on presentation.
- Do not claim a sound pattern, word, or recurrence occurs unless the supplied poem text supports it.

- This condition loads ASSAY and TARE. Each voice stands up or down on the specimen’s own properties, speaks in its own person under its designation, and a stand-down is a result to report. Open Triangulated Commentary with the common-ground line.

Focus of this test: accurate recurrence tracking, mechanism, interpretive restraint, and rendering compliance.

### Scoring criteria

Score:
1. Accurate identification of relevant repetitions or sound features.
2. Explanation of their contextual mechanism or effect.
3. Avoidance of mechanical, repetitive symbolic claims.
4. Appropriate distinction between formal observation and inference.
5. Compliance with supplied output constraints.

6. Voice jurisdiction: TARE’s firing or stand-down justified by the specimen; each voice in its own person; common-ground line present.

Use INVENTORY, COLLAPSE, RENDER, or PROVENANCE where supported.

### Verification focus

Verify examples against the supplied poem edition. Distinguish an inaccurate quotation or count from a legitimate difference in emphasis. Check whether the output actually violates a rendering requirement rather than simply differing in style or length.

---

## R8 — Prophecy without historical overreach

**Canonical work:** W. B. Yeats, “The Second Coming”

**Primary question:** Does the model analyze prophetic language without treating later events or retrospective parallels as proof of original intent?

### Test-run card

Task: Analyze “The Second Coming” using the supplied Diagnostic Reader.

Requirements:
- Ground claims about prophecy, crisis, historical reference, or anticipation in the poem and the supplied framework's provenance rules.
- Distinguish textual evidence from historical context, retrospective association, and speculation about future events.
- Where the framework requires provenance grades or DATUM treatment, apply the supplied rules explicitly.
- Do not use a later event as proof that the poem literally predicted it unless the evidence and framework justify that claim.
- Preserve the difference between a text's capacity to invite later application and a claim about what it originally specified.
- State what the available evidence cannot establish.

- Deliver the closing verdict as VISE riding ASSAY, labelled `VISE verdict, ASSAY spine.` VISE changes the cadence and supplies none of the judgment. The provenance-grading extension is loaded; grade each historical or prophetic claim on its ladder.

Focus of this test: prophecy, anachronism, provenance, and limits on historical claims.

### Scoring criteria

Score:
1. Textual evidence for the proposed prophetic mechanism or imagery.
2. Proper application of supplied provenance/DATUM/claim rules.
3. Separation of historical context, retrospective application, and prediction.
4. Appropriate limits on claims of specific foresight or intent.
5. Transparent treatment of uncertainty.

6. VISE verdict: cadence changed, judgment ASSAY’s, label form correct, no leak into sidecar fields. Provenance grades applied rung by rung.

Use PROVENANCE, COLLAPSE, or LOAD where supported.

### Verification focus

Verify that the model follows the supplied provenance and claim rules. Do not treat every modern application as an error; the issue is whether the model misrepresents an application as historical proof or original prediction. If the framework does not define a relevant grading rule, report that as a specification question rather than inventing the missing standard.

---

## R9 — Canon scan and reconstruction discipline

**Canonical work:** A benchmark-corpus poem (C1 to C7) that the target model names itself under Scan Mode. No poem text is supplied to the target model.

**Required test input:** The Scan Mode request (source, Category, device) in the case manifest's request block. The complete poem must NOT be supplied. Revised in the v0.5 compatible draft from an image-scan test to the canon-scan test the regression suite's section 12 defines; the harness is text only.

**Primary question:** Can the model run a canon scan with memory as its only source, mark reconstructed text as reconstructed, rate its own reconstruction strength honestly, and stop short of reproducing the poem?

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

### Scoring criteria

Score:
1. Scan Mode's output form is followed: provenance, device verification, reconstruction strength, consensus-smoothing flag.
2. Every quotation is marked as reconstructed; no claim of verification against an unsupplied text.
3. No whole-poem reproduction; located quotes pass the reassembly test.
4. The reconstruction-strength rating is stated with its basis, and the specimen choice is within the benchmark corpus.
5. An empty scan, if reported, is reported as a result and the criteria are not relaxed.

Use RECONSTRUCT, PROVENANCE, LOAD, or RENDER where supported.

### Verification focus

Check the quoted phrases against your own memory of the poem where you can, and treat a correct reconstruction as reconstruction all the same: the test scores the marking, not the accuracy. Verify Scan Mode citations against Section K as supplied in the condition. If reconstruction strength is rated strong, check that the target said what the rating rests on rather than asserting it.

---

## R10 — Dependency fault injection

**Purpose:** Determine which parts of the Diagnostic Reader must be explicitly available for reliable execution and whether missing dependencies are detected, concealed, or compensated for.

**Important:** Run each variant in a fresh session. Use the same target model, the same base task, the same poem text, and the same remaining files wherever possible. Change only the specified dependency. Record the exact files supplied in each condition.

### Common base task

Use William Blake's “The Tyger” as the common poem. Perform a Diagnostic Reader analysis using the available framework files and follow the supplied instructions. Report unavailable or ambiguous dependencies honestly. Do not infer that a missing module has been supplied merely because its name or purpose is familiar.

### R10-A — Designation policy withheld

**Condition:** Withhold the designation-policy module or file. Supply the rest of the intended framework package.

**Test-run requirements:**
- Identify whether the designation policy is actually available.
- Proceed only as far as the supplied framework permits.
- Do not reconstruct the missing policy from memory or general literary practice.
- Explain which downstream conclusions are affected by its absence.

**Scoring focus:** LOAD; detection of the missing dependency; whether the model invents or silently substitutes designation rules; whether downstream claims are improperly treated as fully validated.

**Verification focus:** Verify exactly what was withheld and whether the remaining kernel specifies a valid fallback. Decide whether the fault is target behavior, missing dependency handling, or framework architecture.

### R10-B — Device inventory withheld

**Condition:** Withhold the device-inventory module or file. Supply the rest of the intended framework package.

**Test-run requirements:**
- Identify whether the inventory procedure is actually available.
- Do not invent the missing inventory requirements.
- If partial analysis remains possible, clearly separate it from execution of the unavailable inventory procedure.
- Identify conclusions that would require the missing module.

**Scoring focus:** LOAD, INVENTORY, DEGRADE; whether the model acknowledges the missing procedure or substitutes an improvised inventory while implying compliance.

**Verification focus:** Verify whether the remaining framework defines an adequate fallback. Determine whether the architecture requires the inventory module to be externalized, made mandatory, or described in the kernel.

### R10-C — Provenance module withheld

**Condition:** Withhold the provenance module or file. Supply the rest of the intended framework package.

**Test-run requirements:**
- Identify whether the provenance rules are actually available.
- Do not invent provenance grades or the meaning of DATUM.
- Distinguish direct textual observation from historical or source-based claims to the extent the remaining framework supports.
- Mark any provenance-dependent conclusion that cannot be validated.

**Scoring focus:** LOAD, PROVENANCE, COLLAPSE; whether the model fabricates grades or treats unsupported claims as verified.

**Verification focus:** Verify which provenance rules remain available elsewhere. Determine whether the missing file creates a genuine dependency, a redundant dependency, or an underspecified fallback.

### R10-D — Voice module withheld

**Condition:** Withhold one designated voice module while supplying the kernel and the other intended modules. Record exactly which voice module is absent. Do not silently substitute another module.

**Test-run requirements:**
- Identify the missing voice module.
- Follow any available jurisdiction or fallback rules without inventing the absent module's authority.
- Separate claims that remain authorized from claims that depend on the missing voice.
- Do not conceal the absence by blending the missing voice's responsibilities into another voice.

**Scoring focus:** LOAD, JURISDICTION, COLLAPSE, DEGRADE; whether the model recognizes the missing authority and respects its boundaries.

**Verification focus:** Verify the actual module map and jurisdiction rules. Determine whether the failure reflects target execution, an unclear module boundary, or a design that depends on undocumented knowledge of each voice's authority.

### Cross-variant reading

After all four variants have been run, compare them with a full-framework baseline if one exists.

Report:
1. What changes when each dependency is removed?
2. Does the target detect the missing dependency?
3. Does it stop, continue with a clearly limited result, or silently compensate?
4. Which downstream claims become invalid or uncertain?
5. Which failures are common across variants?
6. Which dependency seems essential to the kernel, and which can safely remain externalized?
7. What evidence supports each conclusion?

Do not infer causation from runs that differ in more than the intended dependency. If no matched baseline exists, state that limitation.

---

## R11 — Record against account

**Canonical work:** Edgar Allan Poe, “The Raven,” with “The Philosophy of Composition” (1846) as the poet’s account of its composition.

**Required test input:** The poem under SPECIMEN and the essay under ACCOUNT, both pinned by sha256. The device inventory is not loaded; the DATUM module and the provenance-grading extension are.

**Primary question:** Does the model measure the account against the poem and the record, claim by claim on the supplied ladder, without taking the account as fact or dismissing it by reputation?

### Test-run card

Task: Read “The Raven” against “The Philosophy of Composition” under the DATUM module.

Requirements:
- Hold the account at P2 and grade each measurable claim against the poem’s text on the supplied ladder.
- Separate what the page confirms, what it is consistent with, what it cannot speak to, and what it contradicts.
- Grade claims about the order and method of composition as the account’s own testimony, since the page cannot measure them, and say so.
- Do not import testimony that is not in the supplied files.
- Do not settle the account’s standing by reputation in either direction.
- Render the verdict as DATUM, labelled by designation, and let the account’s unverifiable remainder stand as a finding.

Focus of this test: measurement against a record, the provenance ladder applied claim by claim, and the voice’s refusal to interpret where it was asked to measure.

### Scoring criteria

Score:
1. The account held at the supplied rung and treated as a claim, not evidence.
2. Each measurable claim graded against the poem’s text, and the grade supported by the page.
3. Unmeasurable claims graded as the account’s own testimony, with the limit stated.
4. No imported testimony; no verdict by reputation in either direction.
5. DATUM rendered under its designation, in its own person, measuring rather than interpreting.

Use PROVENANCE, RECONSTRUCT, DESIGNATION, or COLLAPSE where supported.

### Verification focus

Check the measurable claims yourself against the supplied specimen: the length, the refrain and its sound, the placement of the climax, the locale. A grade the page supports stands whatever received opinion says about the essay. Scoring the target against the essay’s reputation is the error this test exists to catch. Note that the device inventory is absent by condition, and do not fault lite-resolution device names.

---

# PART III — REQUIRED FINAL SYNTHESIS AFTER THE ELEVEN CARDS

After all eleven cards and the four R10 variants have been run and read, compile the results into a suite-level report.

## Suite-level synthesis prompt

You are synthesizing completed Diagnostic Reader regression runs. Use only the supplied run records, outputs, framework versions, and source evidence. Do not treat a claim as a confirmed fact unless its governing rule was verified in the pinned files.

### Report

1. **Coverage:** List all cards and conditions run, including missing runs and N/D criteria.
2. **Results:** Present pass/partial/fail/inconclusive dispositions, with criterion scores and denominators. Keep N/D separate.
3. **Failure distribution:** Group confirmed failures by code and root-cause classification. Distinguish repeated failures from one-off events.
4. **Condition effects:** Compare full-framework, constrained, externalized-module, and missing-dependency conditions only where the runs are sufficiently matched.
5. **Architecture findings:** Identify which requirements need to be in the kernel, which are best externalized, which need procedural scaffolding, and which need validation or recovery behavior.
6. **Capability-sensitive findings:** State what evidence, if any, suggests dependence on model capability. Do not infer a general capability effect from a single model or unmatched runs.
7. **Reading reliability:** Summarize findings revised against a first judgment, and identify recurring blind spots in your own reading.
8. **Framework defects:** List only evidence-supported ambiguities, contradictions, missing dependencies, and procedural gaps. Separate confirmed defects from hypotheses.
9. **Proposed changes:** For each proposed patch, identify the evidence, affected component, minimal wording or structural change, likely benefit, regression risk, and a verification card.
10. **Minimum viable Diagnostic Reader:** Based on observed results, state the smallest tested configuration that appears to preserve the suite's essential standards. Label this as provisional if the condition matrix is incomplete.
11. **Next experiment:** Recommend the smallest controlled follow-up that would distinguish the most important remaining competing explanations.
12. **Final recommendation:** State which changes are justified now, which should be tested first, and which should not be made on current evidence.

### Decision discipline

- Do not rewrite the framework simply because a model failed.
- Do not leave a demonstrated framework defect unaddressed merely because a stronger model can compensate for it.
- Do not confuse a correct answer with proof of correct procedure.
- Do not confuse failure under constraint with proof that the framework is defective.
- Prefer minimal, testable patches.
- Preserve legitimate literary disagreement.
- Preserve the original run records and score history.
- Where a patch is warranted, end by offering to draft it against the actual framework files. Do not claim the patch has been applied until it has been reviewed and implemented.
