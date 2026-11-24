# Diagnostic Reader Regression Suite
## Canonical Poem Benchmark and Operator Reading Protocol

**Version:** 0.7  
**Revision 0.7:** Removes the independent evaluator and the LLM adjudicator. The operator reads the artifact. Sections 9 and 10 of v0.6, the two grader prompts, are deleted, and the sections after them renumber from 11-18 to 9-16. The four-stage protocol in section 6 becomes two stages, run and read. The ledger in section 7, the reading rules in section 8, the scoring scale, the failure taxonomy, and the completion criteria survive with the grader roles taken out of them, because the operator still needs every one of them. The test cards, the corpus, and the conditions are unchanged. `dr regress` now emits one prompt and no longer reads this document, so the suite is reference for a person rather than input to a compiler. Prior to 0.7 a single pass over the fourteen cases required 42 pastes of grader prompts and about 48.5 MB of hand-moved text, which is why the protocol was never executed.  
**Revision 0.6:** Adds R11, a record-against-account reading of “The Raven” measured against Poe’s “The Philosophy of Composition,” so the DATUM voice is under test. Adds a condition line to R5 (RETICLE beside ASSAY), R7 (TARE beside ASSAY), and R8 (VISE riding ASSAY, with the provenance-grading extension loaded), so every voice and both modes are exercised somewhere in the suite. States in section 10 that each card’s condition is its manifest’s request block and the load set is derived by the compiler. Prior to 0.6 every condition loaded the whole bundle and the cards named no voices.  
**Purpose:** Test whether a model can load, follow, and faithfully apply the Diagnostic Reader framework; determine whether its output meets the specified literary and procedural criteria; and distinguish model failures from framework defects.

---

## 1. Governing principle

The test subject must not be responsible for judging its own performance. The operator reads the artifact against the pinned condition and the source files, and does not take the artifact's own account of its compliance as evidence.

The suite uses two stages:

1. **Test subject:** Executes the assigned task and produces the raw output.
2. **Operator reading and source verification:** Scores the output against the test card, then checks every material claim about what the framework requires against the exact source files and revision tested, resolving what can be resolved and preserving genuine ambiguities.

The operator is fallible too, and the protection is procedural rather than social: write the standard down before reading the artifact, cite the governing file for every score, and keep what the evidence cannot settle marked unresolved. A reading produced after the artifact is in view tends to be fitted to it.

Three of the four score categories in section 11 need no second reader. Procedural compliance, dependency handling, and framework integrity are checked against the manifest and the files, which say what they say. Literary execution is the category where a second reader earns its cost, and the suite no longer requires one.

The framework’s source files are the primary evidence of what the tested revision specifies. They are not automatically consistent with one another, nor are they an infallible authority on literary interpretation. When the files conflict or fail to specify a necessary decision, that is a potential framework defect—not permission to invent a rule.

**Core distinction:** The target produces evidence; the operator scores it; source verification establishes what the framework actually requires.

## 2. Overarching Goal: Framework Architecture, Externalization, and Minimum Viable Execution

### Primary Purpose

The Diagnostic Reader Regression Suite is not merely a benchmark for determining whether a language model can follow the Diagnostic Reader framework as currently written. Its larger purpose is to determine **how the framework should be structured, specified, distributed, and executed so that its essential analytical standards remain reliable across models of different capabilities, including models with limited reasoning ability, working context, or capacity to coordinate multiple instructions and dependencies.**

The suite should identify which aspects of successful execution depend on:

1. **Explicitly loaded instructions** in the kernel, boot document, or active context.
2. **Externalized policies and reference modules** that can be supplied or retrieved when required rather than relying on implicit recall.
3. **Procedural scaffolding**, including ordered steps, prerequisite checks, decision rules, checklists, and output contracts.
4. **Model capabilities**, including interpretation, evidence discrimination, multi-step reasoning, ambiguity management, and coordination across instructions.
5. **Framework design quality**, including clarity, consistency, dependency declarations, authority relationships, error handling, and the absence of contradictory or underspecified rules.
6. **Reading quality**, including whether the operator correctly distinguishes model failures from framework defects, unsupported assumptions, and legitimate literary disagreement.

These are separate possible causes of success or failure. The suite must not assume that a failure demonstrates insufficient model capability, that successful execution demonstrates reliable loading, or that a model's claim to have followed a rule establishes that it actually did so.

### Architectural Discovery

The suite should help establish which framework elements must remain continuously available, which can be externalized into independently loadable modules, which should be converted into explicit execution procedures, which can be simplified without compromising essential standards, and which require stronger dependency or failure-handling rules.

Potential candidates for externalization include, but are not limited to, designation policy, device inventory, provenance grading, voice jurisdiction, triangulation rules, claim-evidence requirements, output constraints, and procedures governing unavailable or conflicting modules. These are hypotheses to test, not predetermined architectural decisions.

For each candidate element, the suite should investigate whether providing it explicitly, separately, or at the point of use improves execution; whether the improvement persists across repeated runs and model configurations; whether it introduces new errors or conflicts; and whether the same function can be achieved through a smaller kernel, clearer procedure, or more compact specification.

Externalization must not be treated as an automatic good. A module can reduce the burden on the active context while introducing retrieval failures, dependency ambiguity, version mismatches, integration costs, or additional opportunities for misapplication. The relevant question is whether a proposed architectural change improves reliable execution under specified conditions, at an acceptable cost, without weakening the framework's substantive requirements.

### Controlled Conditions and Causal Discipline

Where practical, the suite should compare equivalent tasks under controlled conditions, including:

- A full-framework condition using the existing boot document and required modules.
- A minimal-kernel condition containing only essential operating rules.
- An explicit-module condition in which relevant policies or references are separately supplied.
- A procedural-scaffold condition using explicit steps, prerequisites, decision rules, and validation checks.
- A dependency-fault condition in which a required module is deliberately unavailable.
- Additional conditions, where useful, testing module order, context limitations, version differences, or conflicting instructions.

These comparisons should preserve the target task and scoring criteria wherever possible. The manifest must record which files and instructions each participant actually received, as well as relevant model, configuration, and context limitations. Repeated runs should be used when feasible. Results should be reported at the criterion and failure-mode level, not only as aggregate scores.

A difference between conditions is evidence of an association under the tested setup, not automatically proof of a general causal mechanism. Claims about the effects of externalization, reasoning effort, model capability, or context size require comparisons that isolate the relevant variable as far as practicable. Results must remain bounded by the tested models, tasks, configurations, and versions.

### Minimum Viable Diagnostic Reader

A central long-term objective is to identify a **Minimum Viable Diagnostic Reader**: the smallest combination of kernel, explicit modules, execution procedure, and validation mechanisms that preserves the framework's essential analytical and evidentiary standards while remaining reliably executable by a specified class of models under specified operating conditions.

“Minimum viable” does not mean the shortest prompt, the fewest files, or the highest average score at any cost. It means the least burdensome architecture shown by testing to preserve the required standards, including accurate use of textual evidence, disciplined handling of provenance and inference, appropriate treatment of ambiguity and voice, explicit recognition of missing dependencies, and compliance with the framework's governing rules.

This minimum may differ by model class or execution environment. The suite may ultimately support several validated configurations rather than one universal configuration: for example, a compact configuration for lower-capability models and a more modular configuration for models able to coordinate richer analytical procedures. Such configurations must be documented as empirically supported operating profiles, not assumed to be interchangeable.

### Required Distinctions in Reporting

The suite must keep the following outcomes separate:

- **Target execution failure:** the model's observable output violates an applicable, verified requirement.
- **Capability limitation:** the tested model cannot reliably perform a required operation under the tested conditions, after reasonable specification and scaffolding have been considered.
- **Loading or availability failure:** a necessary instruction or module was not supplied, was unavailable, or cannot be shown to have been available.
- **Dependency-handling failure:** the model fails to recognize or appropriately handle a missing, conflicting, or incompatible dependency.
- **Framework defect:** a requirement is contradictory, ambiguous, incomplete, mis-scoped, or otherwise insufficient to support a reliable determination.
- **Reading error:** the operator misquotes evidence, misapplies a rule, overlooks a qualification, or makes an unsupported judgment.
- **Unresolved disagreement:** the available evidence does not justify a settled conclusion.
- **Literary disagreement:** interpretations differ while remaining compatible with the text and applicable analytical requirements.
- **Architectural improvement opportunity:** controlled results suggest that relocating, clarifying, simplifying, or proceduralizing a framework element could improve reliability.

These categories must not be collapsed into a single failure score or assigned solely on the basis of a model's self-report. Material claims about framework requirements must be checked against the actual, version-pinned source files. Where evidence is insufficient, the result remains unresolved.

### Relationship to the Existing Regression Suite

The existing canonical poems, the regression test cards, the failure taxonomy, the scoring rules, the source-verification ledger, the repeatability protocol, and the final-report requirements remain in force. This overarching goal supplements them; it does not replace them or authorize changes to their criteria.

The existing tests serve two related purposes:

1. **Conformance testing:** determine whether a target execution complies with the framework and task requirements that actually apply.
2. **Architecture testing:** use observed and source-verified outcomes to identify where the framework's structure or delivery may be contributing to failures and to design controlled follow-up experiments.

A conformance failure may motivate an architecture hypothesis, but it does not establish that hypothesis. Architectural recommendations should be recorded separately, tested in follow-up conditions, and incorporated into the framework only through an explicit, versioned revision process. The regression suite must then be rerun to check for regressions and unintended trade-offs.

### Governing Objective

The ultimate objective is to make the Diagnostic Reader's essential standards **explicit, portable, testable, and robust rather than dependent on undocumented assumptions, implicit memory, or the capabilities of a particular model**. The suite should reveal what must be specified, what can be externalized, what must be proceduralized, what can safely be simplified, and what remains beyond the reliable capability of a given model under stated conditions.

The desired result is not merely a framework that performs well when everything is loaded into a capable model. It is a family of evidence-backed configurations whose requirements, dependencies, limitations, and expected behavior are known—and whose failures can be diagnosed without confusing model limitations, framework defects, reading errors, or legitimate interpretive disagreement.

## 3. Constrained Execution and Transfer

**Use constrained execution to expose what open-ended capability can conceal, then test whether the required organization transfers back to open-ended work.**

A model’s success under permissive conditions does not, by itself, establish that it followed the required procedure. A model’s failure under constrained conditions does not, by itself, establish a defect in the framework.

Constraints are diagnostic, not punitive. They should make essential relationships observable, close unauthorized routes around required steps, and produce evidence that can be independently evaluated. Once the framework’s required organization is reliable under constraint, test whether it persists when the model has greater freedom to interpret, reason, and generate.

The objective is not to turn flexible execution into checklist compliance. It is to determine which standards must be explicit, which dependencies must be externalized, and which procedures or constraints help the model internalize and retain the required organization without relying on surplus capability to compensate for gaps.

Every failure should therefore be interpreted against the conditions under which it occurred and classified separately as a target-model failure, a loading or dependency failure, a framework defect, a reading error, or an unresolved disagreement. A pass/fail result without an adequately supported explanation is a diagnostic outcome to investigate, not a sufficient conclusion.

## 4. What the suite measures

Score these dimensions independently.

- **Availability:** Were the required files actually supplied or accessible to the test subject?
- **Procedural compliance:** Did the target follow the specified instructions and output contracts?
- **Literary execution:** Did it produce a textually grounded, appropriately qualified reading?
- **Dependency handling:** Did it respond correctly when a required module or voice was unavailable?
- **Repeatability:** Does the same configuration produce materially consistent results?
- **Framework integrity:** Are the instructions coherent, sufficiently explicit, and compatible across files?

Do not infer successful file loading from a model’s statement that it loaded a module. Unless the environment independently establishes file access, record actual loading as *not independently verified*.

Likewise, do not infer that a reading is correct because it quotes a file. Each material judgment must be supported by evidence, and a judgment the evidence does not settle stays unresolved.

## 5. Pin the test environment

Before running any test, record:

- Repository URL and commit hash.
- Exact boot file and version.
- Exact versions and hashes of all supplied modules, where available.
- Model and product configuration, where known.
- Reasoning setting, if selectable.
- Full test prompt and test-card ID.
- Date of run.
- Exact files supplied to the test subject, and whether they were pasted inline or attached.
- Whether the model received full files or excerpts.
- Any context truncation, tool failure, missing input, or other limitation.

Use a clean session for each run. Do not give the test subject the scoring criteria or earlier diagnoses unless the specific test is testing self-correction.

`build-manifest.json` records every file's sha256, the request as parsed, the withheld list, the specimen's sha256, and the sha256 of the prompt. It does not record a commit hash, a run identifier, or a date; supply those yourself.

### Required artifacts

Preserve the following under a single run ID.

**A. Test manifest:** Intended inputs, actual files supplied, versions, and configuration. `build-manifest.json` covers most of it.

**B. Raw target output:** The complete, unedited response from the test subject.

**C. Source-verification ledger:** Evidence establishing whether material claims about framework requirements are supported by the pinned files. Write its standard before reading the output.

**D. Final disposition:** Confirmed target failures, framework defects, unresolved questions, and final scores by category.

Keep the original artifacts even if a later reading corrects or overturns their conclusions. Do not silently replace an earlier record with a revised one.

## 6. The two-stage protocol

### Stage A — Run the test subject

Supply the test subject with:

- The pinned boot file.
- The modules required by the test card.
- The poem or permitted scan task.
- The exact test prompt.
- Any explicitly required supporting material.

Instruct it to perform the task, not to grade its own compliance.

Preserve its entire response exactly as returned. Do not repair formatting, remove inconvenient passages, or summarize the output before reading it.

### Stage B — Read the artifact and verify against the source

Before reading the output, write down what the case requires, with the governing file and section cited for each check. A standard written after the artifact is in view is fitted to it.

Work the mechanical checks first, because they are decidable and they carry the suite's primary question.

**The loading report.** Every target prompt makes it required output item 1, and the compiled prompt repeats the LOAD SET immediately before the operator request so the report can be written against it. Check that every file in the table is marked used or unused, that nothing absent from the table is marked used, and that withheld files are reported absent. Two things in the prompt look like inventories and are not: the boot's Module Registry, which lists sixteen stems whatever the condition, and the kernel's cross-references to `0b`, `12`, and `13`. A report that lists either as loaded is a RECONSTRUCT failure.

**Dependency handling.** Where a procedure needed a file that is absent, did the output switch the procedure off and say so, or rebuild it?

**Designation.** Check the label form against `0c-voice-designations`, and check that no calibration source is identified in the reading, by name or by coinage or by biographical anchor. Specimen attribution stays.

Then read for literary execution, which is the one category the mechanical checks cannot reach.

Score each category separately per section 11. Mark N/D where the evidence does not decide, and do not convert N/D to zero to finish the scorecard. Label a proposed cause as a hypothesis rather than a fact.

### Source verification and final disposition

For each material claim about what the framework requires:

1. Locate the relevant passage in the pinned source file.
2. Record the exact file path, revision, section or heading, and line range where available.
3. Quote the smallest passage that establishes the requirement.
4. Determine whether the passage is mandatory, conditional, advisory, or descriptive, where the source makes that distinction clear.
5. Check whether another file modifies, overrides, qualifies, or contradicts it.
6. Compare the verified rule with the target’s actual words or omissions.
7. Record the final disposition and rationale.

A source claim is not verified merely because a plausible file has been named. The passage must support the claimed requirement.

If two files conflict, record a **framework defect or unresolved precedence question**. Do not silently select whichever instruction makes the target look wrong.

If the target’s behavior is compatible with the available instructions, do not mark it as a confirmed violation simply because you would have preferred a different approach.

This stage is primarily a source check, not automatically another model run. A further LLM may help compare difficult passages, but its conclusion must also be checked against the files. A human decision may be necessary for unresolved policy or interpretive disputes.

## 7. Source-verification ledger

Create one entry for every material compliance finding, including findings you are unsure of.

| Field | Required record |
|---|---|
| Finding ID | Stable identifier, such as F-03 |
| Origin | Reading finding or source-review finding |
| Original claim | The specific alleged failure or compliance judgment |
| Target evidence | Exact quotation or identifiable omission |
| First judgment | Status on first reading, and rationale |
| Governing source | File path and pinned revision |
| Source passage | Heading, line range, and exact text |
| Applicability | Why the rule applies to this test |
| Cross-file check | Related rules, overrides, or contradictions |
| Final disposition | Confirmed, rejected, unresolved, or framework defect |
| Rationale | Short explanation tied to evidence |
| Confidence | High, medium, or low, with reason |

### Disposition definitions

- **Confirmed:** An explicit, applicable rule exists, and the target observably violated it.
- **Rejected:** The cited rule does not say what was claimed, does not apply, or the target complied.
- **Unresolved:** The evidence is insufficient to determine compliance.
- **Framework defect:** The instructions conflict, omit a necessary decision rule, or cannot reliably determine expected behavior.

Where a second pass revises a finding, record the revision against the first judgment rather than overwriting it:

- **UPHELD:** The first judgment is supported.
- **DOWNGRADED:** A genuine issue exists, but the first judgment overstated its severity or certainty.
- **OVERTURNED:** The finding is unsupported, misapplied, or contradicted by the evidence.
- **UNRESOLVED:** The available evidence cannot establish the correct judgment.
- **FRAMEWORK DEFECT:** The finding exposes a conflict, omission, or ambiguity in the governing files.

Do not convert an unresolved finding into a confirmed failure merely to complete the scorecard. A finding you revise against yourself is the ledger working; the record of the first judgment is what makes the revision checkable.

## 8. Reading rules

These rules govern the operator's reading of an artifact, and they are the reason a single reader can be trusted with it.

### Evidence discipline

- Quote the target accurately.
- Quote the actual source passage that supports a claimed requirement.
- Do not fabricate paths, versions, line numbers, or citations.
- If the failure is an omission, state precisely what required evidence is absent.
- Distinguish explicit requirements from inferred expectations.
- Distinguish a procedural violation from a literary disagreement.

### Loading and provenance discipline

- Do not infer successful module loading from the target’s self-report.
- Do not claim access to hidden training data or internal model processes.
- Do not claim exact wording has been verified unless a verification source was available.
- Distinguish text supplied by the operator from text recalled, reconstructed, or independently verified.
- Do not attribute a failure to model size, reasoning effort, or product routing without comparative evidence.

### Framework discipline

- Check relevant cross-file relationships.
- Do not invent precedence rules absent from the framework.
- Do not silently repair contradictory instructions while grading the target.
- Record framework defects separately from target failures.
- Preserve uncertainty when the supplied evidence does not resolve an issue.

## 9. Canonical benchmark corpus

Use established public-domain poems published before 1929. These are benchmark texts, not a claim about which poems were present in any model’s training data.

| ID | Poem | Author | Primary test |
|---|---|---|---|
| C1 | “The Tyger” (1794) | William Blake | Bootstrap, designation, mechanism-first device inventory |
| C2 | “London” (1794) | William Blake | Social coercion, pressure, engine versus residue |
| C3 | “Ozymandias” (1818) | Percy Bysshe Shelley | Framing, irony, evidence versus inference |
| C4 | “Because I could not stop for Death” (published 1890) | Emily Dickinson | Ambiguity, temporal structure, Coscienza |
| C5 | “My Last Duchess” (1842) | Robert Browning | Speaker versus author, coercion, inference discipline |
| C6 | “The Raven” (1845) | Edgar Allan Poe | Repetition, escalation, device inventory, rendering restraint |
| C7 | “The Second Coming” (1920) | W. B. Yeats | Prophecy, competing hypotheses, historical overreach |

Record the text edition used for supplied-poem tests. For scan tests, do not provide the complete poem unless that is explicitly part of the test condition.

## 10. Regression test cards

Each card’s condition is the `request` block in its manifest under `regression/tests/<R-ID>/`. The compiler derives the load set from it; a card that names voices or a mode is stating that condition, and whether a voice fires on the specimen is the test, not the premise. A card that names no voice runs under ASSAY.

### R1 — Bootstrap and designation integrity

**Target:** “The Tyger”

**Tests:** Correct initialization and compliance with the designation policy.

**Pass criteria:**
- Uses only the designations permitted by the supplied framework.
- Does not claim access to a source or calibration authority that was not supplied.
- Follows required initialization and output contracts.
- Does not silently invent missing dependencies.

**Failure codes:** LOAD, DESIGNATION, RECONSTRUCT.

### R2 — Device inventory and mechanism-first reasoning

**Target:** “The Tyger”

**Tests:** Whether devices are identified through their actual textual function rather than as decorative labels.

**Pass criteria:**
- Each major device has a textual address and an explained function.
- Mechanism is established before interpretive credit is assigned, where the framework requires that order.
- The inventory distinguishes operative devices from incidental features.
- Claims about the poem are grounded in the supplied text.

**Failure codes:** INVENTORY, PROVENANCE, RENDER.

### R3 — Coercion as engine or residue

**Target:** “London”

**Tests:** Whether social and political pressure is treated as structurally important when supported by the poem.

**Pass criteria:**
- Identifies textual evidence for the relevant pressure.
- Explains how it shapes the poem’s movement or meaning.
- Distinguishes structural pressure from merely thematic mention.
- If triangulation is required, preserves the distinct functions and disagreements of the designated voices.

**Failure codes:** JURISDICTION, COLLAPSE, INVENTORY.

### R4 — Framing, irony, and epistemic boundaries

**Target:** “Ozymandias”

**Tests:** Whether the response separates the poem’s framing devices, reported claims, and reader inference.

**Pass criteria:**
- Distinguishes the speaker’s report from the embedded inscription.
- Explains how framing contributes to irony.
- Does not treat a claim made within the poem as independently verified historical evidence.
- Marks uncertain contextual claims appropriately.

**Failure codes:** PROVENANCE, COLLAPSE.

### R5 — Coscienza and ambiguity

**Target:** “Because I could not stop for Death”

**Condition:** Triangulate ASSAY and RETICLE.

**Tests:** Whether the reading preserves productive ambiguity rather than prematurely resolving it.

**Pass criteria:**
- Supports interpretations with identifiable textual evidence.
- Preserves competing readings where the text warrants them.
- Respects any framework limit on the number of live hypotheses.
- Distinguishes ambiguity in the poem from uncertainty caused by missing information.

**Failure codes:** COLLAPSE, PROVENANCE, RENDER.

### R6 — Speaker, person, and coercion

**Target:** “My Last Duchess”

**Tests:** Whether the response distinguishes dramatic speaker from author and separates inference from established fact.

**Pass criteria:**
- Does not casually attribute the speaker’s attitudes to the poet.
- Grounds inferences about power and control in the speech and dramatic situation.
- Distinguishes explicit statements from psychological or biographical conjecture.
- Applies the relevant voice-jurisdiction rules.

**Failure codes:** JURISDICTION, PROVENANCE, COLLAPSE.

### R7 — Repetition and rendering restraint

**Target:** “The Raven”

**Condition:** Triangulate ASSAY and TARE.

**Tests:** Whether the model explains repetition’s changing function and avoids letting analytical apparatus overwhelm the reading.

**Pass criteria:**
- Explains the function of repetition in context, not merely its presence.
- Identifies meaningful escalation or variation where supported.
- Includes only devices that contribute to the reading under the framework’s criteria.
- Follows output-length and sidecar constraints, if specified.

**Failure codes:** INVENTORY, RENDER.

### R8 — Prophecy without historical overreach

**Target:** “The Second Coming”

**Condition:** ASSAY sidecar with a VISE verdict riding ASSAY; the provenance-grading extension loaded.

**Tests:** Whether the response can generate hypotheses without presenting a later historical association as proof.

**Pass criteria:**
- Distinguishes textual evidence from historical interpretation.
- Labels proposed historical parallels as hypotheses when warranted.
- Does not claim the poem uniquely predicts a specific event without sufficient support.
- Preserves alternative explanations when required.

**Failure codes:** PROVENANCE, COLLAPSE.

### R9 — Canon scan and reconstruction discipline

**Target:** A scan request for a poem from the benchmark corpus, without supplying its complete text.

**Tests:** Whether the model distinguishes its own knowledge, uncertainty, and the framework’s retrieval rules.

**Pass criteria:**
- Follows the supplied Scan Mode instructions.
- Does not imply that it inspected its own training corpus.
- Does not claim exact wording has been verified when no verification source was available.
- Does not reproduce a complete poem when the test forbids it.
- Distinguishes remembered or reconstructed content from text actually supplied or verified.

**Failure codes:** LOAD, PROVENANCE, RECONSTRUCT.

### R10 — Dependency fault injection

**Target:** Repeat a suitable task while intentionally withholding one required module or voice.

**Tests:** Graceful degradation.

Run separate trials withholding:
- The designation policy.
- The device inventory.
- The provenance module.
- A voice required for triangulation.

**Pass criteria:**
- The target recognizes the dependency as unavailable when the supplied instructions require that behavior.
- It does not silently recreate missing module rules from memory.
- It narrows or disables dependent functionality as specified by the framework.
- It identifies limitations without falsely claiming full compliance.

**Failure codes:** LOAD, DEGRADE, RECONSTRUCT, JURISDICTION.

### R11 — Record against account

**Target:** “The Raven,” with “The Philosophy of Composition” as the poet’s account.

**Condition:** DATUM reading; the account supplied and held at P2; the device inventory not loaded.

**Tests:** Whether the model measures an author’s account of a poem against the poem and the record, grading claim by claim, rather than taking the account as fact or dismissing it by reputation.

**Pass criteria:**
- Holds the account at the supplied provenance rung and grades each measurable claim against the poem’s text.
- Separates what the page confirms, what it is consistent with, what it cannot measure, and what it contradicts.
- Grades claims about the order and method of composition as the account’s own testimony and says the page cannot reach them.
- Imports no testimony that is not in the supplied files.
- Renders the verdict as DATUM under its designation.

**Failure codes:** PROVENANCE, RECONSTRUCT, DESIGNATION.

## 11. Scoring

Score each applicable criterion from 0 to 2:

- **2 — Pass:** Clear, observable compliance.
- **1 — Partial:** Some compliance, but a material omission or weakness remains.
- **0 — Fail:** Clear violation supported by evidence.
- **N/D — Not determinable:** Insufficient evidence or unresolved source ambiguity.

Do not count N/D as zero. Report the number of scored criteria and the number not determinable.

Keep separate scores for:

1. **Procedural compliance**
2. **Literary execution**
3. **Dependency handling**
4. **Framework integrity**

Do not combine the categories into a single average that could conceal a critical failure. Report the number of scored criteria and the number marked N/D for each.

A high literary score cannot compensate for a critical procedural failure. A model’s procedural failure cannot be confirmed if the supposed rule exists only in your reading of it and cannot be located in the source files.

### Critical-failure rule

A critical failure must be reported explicitly even if the aggregate score is high. Do not allow strong performance on unrelated criteria to cancel it out.

A source ambiguity that prevents a reliable judgment is not a target failure; it is an unresolved issue or framework defect.

## 12. Failure taxonomy

Use these codes consistently across the reading and the final record.

- **LOAD:** Required access or loading was claimed but not established, or a required input was missing.
- **DESIGNATION:** The target violated a naming or designation rule.
- **INVENTORY:** Device identification or mechanism-first requirements were violated.
- **PROVENANCE:** Claims exceeded the available evidence or violated source-grading rules.
- **JURISDICTION:** A voice or module exceeded its permitted role, or required responsibilities were misplaced.
- **COLLAPSE:** Distinct hypotheses, voices, or uncertainties were improperly flattened.
- **DEGRADE:** Missing dependencies were not handled as specified.
- **RENDER:** Output constraints or rendering requirements were violated.
- **RECONSTRUCT:** Missing rules, evidence, or text were silently invented or reconstructed.

A failure code is a classification, not proof. Every confirmed code must point to target evidence and a verified governing rule.

Reading errors should be tracked separately from target failure codes. Do not classify your own unsupported judgment as a target failure merely because it was in the first pass.

## 13. Repeatability and controlled comparisons

For each selected test, run:

- **Condition A:** Full required framework and standard reasoning setting.
- **Condition B:** Same inputs and modules, with a lower reasoning setting if the product exposes that control.
- **Condition C:** Deliberate dependency omission.

Repeat conditions where practical. Preserve every run; do not select only the best response.

Label the outputs Run A, Run B, and Run C, and score them before looking up which model or reasoning setting produced which. Reading an artifact you already know came from a weak model is how a weak model gets the failure it was expected to have. This reduces expectation effects but does not eliminate them.

Reveal the configuration after the reports are saved.

A difference between settings establishes an observed difference, not its cause. Attribute a failure to reduced reasoning effort only cautiously and only when the comparison supports it.

### Comparison protocol

When comparing runs:

1. Use the same test card and poem.
2. Keep framework versions and supplied inputs identical except for the variable being tested.
3. Record any unavoidable differences.
4. Compare criterion-level outcomes, not just overall impressions.
5. Score each run against the same written standard, in the same way.
6. Do not assume that a newer, larger, or more capable model must be correct.
7. Source-check disputed findings before drawing conclusions about the framework or model configuration.

## 14. Completion criteria

A test is complete only when:

- The test manifest and raw target output are preserved.
- The standard was written down before the output was read.
- Each applicable criterion has been assessed against the test card.
- Material framework-compliance claims have been checked against the pinned source files.
- Unresolved claims remain explicitly unresolved.
- Framework contradictions are recorded separately from model failures.
- Reading errors are recorded separately from target failures.
- Scores are reported separately for procedure, literary execution, dependency handling, and framework integrity.
- The final report includes evidence sufficient for someone else to reproduce the judgment from the pinned files.
- The final record identifies the next regression test needed to verify a proposed fix.

## 15. Final report format

For each run, report:

1. Run ID and environment.
2. Test card and expected behavior.
3. Raw target output reference.
4. The standard, as written before reading.
5. Findings, each with target evidence and the governing file and section.
6. Source-verified findings, and any claim the files could not settle.
7. Findings revised against the first pass, with the first judgment kept.
8. Framework defects or ambiguities.
9. Procedural score and denominator.
10. Literary-execution score and denominator.
11. Dependency-handling score and denominator.
12. Framework-integrity findings.
13. Not-determinable criteria.
14. Failure codes with supporting evidence.
15. Comparison with earlier runs.
16. The next regression test needed to verify a proposed fix.

## 16. Final operating rule

The test subject produces the artifact. The operator scores it against a standard written before the artifact was read. Source verification establishes what the files actually require.

Removing the grader roles removes the check they were there to provide, and nothing social replaces it. What replaces it is procedure: the standard goes in writing first, every score cites the governing file and section, a revised finding is recorded against the first judgment rather than over it, and what the evidence cannot settle stays unresolved. An operator who skips those steps is not running this suite.

The source files are the evidence for framework requirements, not a guarantee that the framework is internally coherent. When the files cannot resolve a dispute, the suite must preserve that uncertainty and identify the framework clarification needed.

**No reading is granted final authority merely because it is the only one. The result must remain evidence-based, traceable, and reproducible from the pinned files.**

### Operationalization: Prompt Regime

The executable procedures for this benchmark are maintained in `regression/prompt-regime`.

The regression suite defines the governing test objectives, test conditions, scoring criteria, and failure taxonomy. The prompt regime translates these requirements into copy-ready instructions for target runs and the operator's reading.

Neither document is read by `dr regress`, which from suite v0.7 compiles the reader prompt from the case manifests alone. Both are reference for a person.

The prompt regime must not silently alter the suite's requirements or scoring rules. Any substantive change to a test's behavior, criteria, or interpretation must be reflected in the governing suite definition and recorded in the version history. Each run must identify the exact versions of both files used.
