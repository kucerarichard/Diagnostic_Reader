# Diagnostic Reader Regression Suite
## Canonical Poem Benchmark, Independent Evaluation, and Adjudication Protocol

**Version:** 0.5 — Consolidated Final Draft  
**Purpose:** Test whether a model can load, follow, and faithfully apply the Diagnostic Reader framework; determine whether its output meets the specified literary and procedural criteria; audit the evaluator’s judgments independently; and distinguish model failures from evaluator errors and framework defects.

---

## 1. Governing principle

The test subject must not be responsible for judging its own performance. The evaluator must not be presumed correct, and the adjudicator must not be granted automatic final authority.

The suite uses four distinct stages:

1. **Test subject:** Executes the assigned task and produces the raw output.
2. **Independent evaluator:** Grades the target output against the test card and framework requirements.
3. **LLM adjudicator:** Audits the evaluator’s report against the raw target output, the test card, and the actual framework files. It may uphold, downgrade, or overturn findings and identify failures the evaluator missed.
4. **Source verification and final disposition:** Checks material claims about framework requirements against the exact source files and revision tested, resolving what can be resolved and preserving genuine ambiguities.

The evaluator and adjudicator are both fallible. The adjudicator’s role is not to rubber-stamp the evaluator or merely provide another literary opinion. It is to conduct an adversarial review of the evaluation itself.

The framework’s source files are the primary evidence of what the tested revision specifies. They are not automatically consistent with one another, nor are they an infallible authority on literary interpretation. When the files conflict or fail to specify a necessary decision, that is a potential framework defect—not permission to invent a rule.

**Core distinction:** The target produces evidence; the evaluator grades it; the adjudicator audits the grade; source verification establishes what the framework actually requires.

## 2. Overarching Goal: Framework Architecture, Externalization, and Minimum Viable Execution

### Primary Purpose

The Diagnostic Reader Regression Suite is not merely a benchmark for determining whether a language model can follow the Diagnostic Reader framework as currently written. Its larger purpose is to determine **how the framework should be structured, specified, distributed, and executed so that its essential analytical standards remain reliable across models of different capabilities, including models with limited reasoning ability, working context, or capacity to coordinate multiple instructions and dependencies.**

The suite should identify which aspects of successful execution depend on:

1. **Explicitly loaded instructions** in the kernel, boot document, or active context.
2. **Externalized policies and reference modules** that can be supplied or retrieved when required rather than relying on implicit recall.
3. **Procedural scaffolding**, including ordered steps, prerequisite checks, decision rules, checklists, and output contracts.
4. **Model capabilities**, including interpretation, evidence discrimination, multi-step reasoning, ambiguity management, and coordination across instructions.
5. **Framework design quality**, including clarity, consistency, dependency declarations, authority relationships, error handling, and the absence of contradictory or underspecified rules.
6. **Evaluation quality**, including whether the evaluator and adjudicator correctly distinguish model failures from framework defects, evaluator mistakes, unsupported assumptions, and legitimate literary disagreement.

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
- **Evaluator error:** the evaluator misquotes evidence, misapplies a rule, overlooks a qualification, or makes an unsupported judgment.
- **Adjudicator error or unresolved disagreement:** the adjudicator makes a comparable error, or the available evidence does not justify a settled conclusion.
- **Literary disagreement:** interpretations differ while remaining compatible with the text and applicable analytical requirements.
- **Architectural improvement opportunity:** controlled results suggest that relocating, clarifying, simplifying, or proceduralizing a framework element could improve reliability.

These categories must not be collapsed into a single failure score or assigned solely on the basis of a model's self-report. Material claims about framework requirements must be checked against the actual, version-pinned source files. Where evidence is insufficient, the result remains unresolved.

### Relationship to the Existing Regression Suite

The existing canonical poems, ten regression test cards, failure taxonomy, scoring rules, evaluator prompt, adjudicator prompt, source-verification ledger, repeatability protocol, and final-report requirements remain in force. This overarching goal supplements them; it does not replace them or authorize changes to their criteria.

The existing tests serve two related purposes:

1. **Conformance testing:** determine whether a target execution complies with the framework and task requirements that actually apply.
2. **Architecture testing:** use observed, adjudicated, and source-verified outcomes to identify where the framework's structure or delivery may be contributing to failures and to design controlled follow-up experiments.

A conformance failure may motivate an architecture hypothesis, but it does not establish that hypothesis. Architectural recommendations should be recorded separately, tested in follow-up conditions, and incorporated into the framework only through an explicit, versioned revision process. The regression suite must then be rerun to check for regressions and unintended trade-offs.

### Governing Objective

The ultimate objective is to make the Diagnostic Reader's essential standards **explicit, portable, testable, and robust rather than dependent on undocumented assumptions, implicit memory, or the capabilities of a particular model**. The suite should reveal what must be specified, what can be externalized, what must be proceduralized, what can safely be simplified, and what remains beyond the reliable capability of a given model under stated conditions.

The desired result is not merely a framework that performs well when everything is loaded into a capable model. It is a family of evidence-backed configurations whose requirements, dependencies, limitations, and expected behavior are known—and whose failures can be diagnosed without confusing model limitations, framework defects, evaluation errors, or legitimate interpretive disagreement.

## 3. Constrained Execution and Transfer

**Use constrained execution to expose what open-ended capability can conceal, then test whether the required organization transfers back to open-ended work.**

A model’s success under permissive conditions does not, by itself, establish that it followed the required procedure. A model’s failure under constrained conditions does not, by itself, establish a defect in the framework.

Constraints are diagnostic, not punitive. They should make essential relationships observable, close unauthorized routes around required steps, and produce evidence that can be independently evaluated. Once the framework’s required organization is reliable under constraint, test whether it persists when the model has greater freedom to interpret, reason, and generate.

The objective is not to turn flexible execution into checklist compliance. It is to determine which standards must be explicit, which dependencies must be externalized, and which procedures or constraints help the model internalize and retain the required organization without relying on surplus capability to compensate for gaps.

Every failure should therefore be interpreted against the conditions under which it occurred and classified separately as a target-model failure, a loading or dependency failure, a framework defect, an evaluation error, or an unresolved disagreement. A pass/fail result without an adequately supported explanation is a diagnostic outcome to investigate, not a sufficient conclusion.

## 4. What the suite measures

Score these dimensions independently.

- **Availability:** Were the required files actually supplied or accessible to the test subject?
- **Procedural compliance:** Did the target follow the specified instructions and output contracts?
- **Literary execution:** Did it produce a textually grounded, appropriately qualified reading?
- **Dependency handling:** Did it respond correctly when a required module or voice was unavailable?
- **Repeatability:** Does the same configuration produce materially consistent results?
- **Evaluator reliability:** Did the evaluator correctly apply the rubric, identify failures, and support its findings?
- **Adjudicator reliability:** Did the adjudicator detect evaluator errors without introducing unsupported judgments of its own?
- **Framework integrity:** Are the instructions coherent, sufficiently explicit, and compatible across files?

Do not infer successful file loading from a model’s statement that it loaded a module. Unless the environment independently establishes file access, record actual loading as *not independently verified*.

Likewise, do not infer that an evaluator is correct because it quotes a file, or that an adjudicator is correct because it disagrees with the evaluator. Each material judgment must be supported by evidence.

## 5. Pin the test environment

Before running any test, record:

- Repository URL and commit hash.
- Exact boot file and version.
- Exact versions and hashes of all supplied modules, where available.
- Model and product configuration, where known.
- Reasoning setting, if selectable.
- Full test prompt and test-card ID.
- Date of run.
- Exact files supplied to each role.
- Whether each model received full files or excerpts.
- Any context truncation, tool failure, missing input, or other limitation.

Use a clean session for each independent role. Do not give the test subject the evaluator’s rubric or earlier diagnoses unless the specific test is testing self-correction.

The evaluator must receive the original target output, not a summary. The adjudicator must receive both the original target output and the evaluator’s complete report.

Where practical, initially conceal model identities and reasoning settings from the evaluator and adjudicator. Reveal them only after their reports have been saved.

### Required artifacts

Preserve the following under a single run ID.

**A. Test manifest:** Intended inputs, actual files supplied, versions, and configuration.

**B. Raw target output:** The complete, unedited response from the test subject.

**C. Evaluator report:** Criterion-by-criterion assessment, supporting quotations, candidate source references, and provisional scores.

**D. Adjudicator report:** Audit of the evaluator’s findings, including upheld, downgraded, overturned, missed, and unresolved findings.

**E. Source-verification ledger:** Evidence establishing whether material claims about framework requirements are supported by the pinned files.

**F. Final disposition:** Confirmed target failures, evaluator errors, adjudicator errors if identified, framework defects, unresolved disputes, and final scores.

Keep the original artifacts even if later stages correct or overturn their conclusions. Do not silently replace an earlier report with a revised one.

## 6. The four-stage protocol

### Stage A — Run the test subject

Supply the test subject with:

- The pinned boot file.
- The modules required by the test card.
- The poem or permitted scan task.
- The exact test prompt.
- Any explicitly required supporting material.

Instruct it to perform the task, not to grade its own compliance.

Preserve its entire response exactly as returned. Do not repair formatting, remove inconvenient passages, or summarize the output before evaluation.

### Stage B — Run the independent evaluator

Supply the evaluator with:

- The specific test card and pass criteria.
- The complete raw target output.
- The test manifest.
- The exact framework files needed to interpret the criteria.
- The evaluator prompt in Section 7.

The evaluator assesses observable evidence. It may propose likely causes, but it must label them as hypotheses rather than facts.

Its findings and scores are provisional.

### Stage C — Run the LLM adjudicator

Supply the adjudicator with:

- This regression suite.
- The specific test card.
- The complete raw target output.
- The evaluator’s complete report.
- The test manifest.
- The actual framework files and versions used in the test.

Use the adjudicator prompt in Section 8.

The adjudicator must independently inspect the target output. It must not limit its review to the failures already identified by the evaluator.

It should identify:
- Correct evaluator findings.
- Unsupported or misapplied evaluator findings.
- Findings whose severity was overstated.
- Genuine failures the evaluator missed.
- Framework ambiguities mistaken for target failures.
- Evaluator judgments that confuse literary disagreement with procedural noncompliance.

The adjudicator’s result is a second-stage audit, not an unquestionable verdict.

### Stage D — Source verification and final disposition

For each material claim about what the framework requires:

1. Locate the relevant passage in the pinned source file.
2. Record the exact file path, revision, section or heading, and line range where available.
3. Quote the smallest passage that establishes the requirement.
4. Determine whether the passage is mandatory, conditional, advisory, or descriptive, where the source makes that distinction clear.
5. Check whether another file modifies, overrides, qualifies, or contradicts it.
6. Compare the verified rule with the target’s actual words or omissions.
7. Record the final disposition and rationale.

A source claim is not verified merely because the evaluator or adjudicator names a plausible file. The passage must support the claimed requirement.

If two files conflict, record a **framework defect or unresolved precedence question**. Do not silently select whichever instruction makes the target look wrong.

If the target’s behavior is compatible with the available instructions, do not mark it as a confirmed violation simply because the evaluator or adjudicator would have preferred a different approach.

This stage is primarily a source check, not automatically another model run. A further LLM may help compare difficult passages, but its conclusion must also be checked against the files. A human decision may be necessary for unresolved policy or interpretive disputes.

## 7. Source-verification ledger

Create one entry for every material compliance finding, including findings disputed by the adjudicator.

| Field | Required record |
|---|---|
| Finding ID | Stable identifier, such as F-03 |
| Origin | Evaluator finding, adjudicator finding, or source-review finding |
| Original claim | The specific alleged failure or compliance judgment |
| Target evidence | Exact quotation or identifiable omission |
| Evaluator judgment | Original status and rationale |
| Adjudicator disposition | Upheld, downgraded, overturned, unresolved, or framework defect |
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

For the adjudicator’s audit of evaluator findings, use the more specific statuses:

- **UPHELD:** The evaluator’s finding is supported.
- **DOWNGRADED:** A genuine issue exists, but the evaluator overstated its severity or certainty.
- **OVERTURNED:** The finding is unsupported, misapplied, or contradicted by the evidence.
- **UNRESOLVED:** The available evidence cannot establish the correct judgment.
- **FRAMEWORK DEFECT:** The finding exposes a conflict, omission, or ambiguity in the governing files.

Do not convert an unresolved finding into a confirmed failure merely to complete the scorecard.

## 8. Evaluation rules common to both roles

Both evaluator and adjudicator must follow these rules.

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

## 9. Independent evaluator prompt

Use this prompt in a separate session from the test subject. Attach the actual test card, raw target output, manifest, and relevant pinned framework files.

### PROMPT E — Independent evaluator

You are an independent evaluator of a Diagnostic Reader regression test. You are not the test subject and must not assume that the target’s claims about its own loading or compliance are true.

Evaluate the target response against the supplied test card and the exact framework files provided for the tested revision.

Your task is to produce a rigorous, evidence-based assessment. You are not being asked merely whether the reading is persuasive. You must assess procedural compliance separately from literary execution.

**For each applicable criterion:**

1. Assign PASS, PARTIAL, FAIL, or NOT DETERMINABLE.
2. Quote the smallest relevant passage from the target response. If the alleged failure is an omission, state exactly what required evidence is absent.
3. Identify the governing source file and the specific passage that supports your judgment. If you cannot locate the passage, say so.
4. Distinguish a confirmed procedural violation from an inference about the model’s internal process.
5. Identify the earliest observable failure and any downstream consequences.
6. Check for relevant instructions in other supplied files that qualify or contradict the alleged rule.
7. State what additional evidence would resolve each uncertain finding.

Score procedural compliance separately from literary quality. Do not reward confidence in place of evidence. Do not infer successful loading from a self-report. Do not attribute a failure to reduced reasoning effort without comparative evidence.

If the framework files are ambiguous or contradictory, report a possible framework defect rather than inventing a resolution.

Do not restrict your assessment to general impressions. Apply the specific test card and identify each material criterion that passes, partially passes, fails, or cannot be determined.

### Required evaluator report

Return:

1. **Run identification:** Test card, run ID, and any manifest limitations.
2. **Executive finding:** Short summary of compliance and the most important concerns.
3. **Criterion-level findings:** Criterion, status, target evidence, governing source, rationale, and confidence.
4. **Candidate failures:** Each with a unique finding ID.
5. **Source support:** Citations and quotations for each candidate violation.
6. **Possible framework defects:** Conflicts, omissions, or ambiguities in the supplied files.
7. **Root-cause hypotheses:** Clearly labeled as hypotheses, ranked by evidence rather than rhetorical confidence.
8. **Provisional score:** Scores by dimension, denominators, and count of NOT DETERMINABLE criteria.
9. **Recommended follow-up:** The smallest additional check or regression test that would resolve the most important uncertainty.

Do not present your provisional score as the final adjudicated result.

Label the report:

**PROVISIONAL — INDEPENDENT ADJUDICATION PENDING**

Do not fabricate file paths, quotations, line numbers, or source references. Do not present an unsupported claim as a confirmed violation.

## 10. LLM adjudicator prompt

Use this prompt in a separate session from the evaluator. Supply the evaluator report, original target response, test card, manifest, and actual pinned framework files.

### PROMPT A — Independent adjudicator of the evaluation

You are the independent adjudicator of a Diagnostic Reader regression test. Your primary task is to audit the evaluator’s report against the original target response, the test card, and the actual framework files.

The evaluator may have made false-positive findings, missed genuine failures, misread a framework rule, overstated the severity of an issue, or failed to identify a defect in the framework.

You are not required to agree with the evaluator. Your job is to determine which findings are supported, which are unsupported, which are missing, and which cannot be resolved from the available evidence.

You are an auditor of the evaluation, not an unquestionable authority. Your conclusions must be traceable to evidence.

### A. Audit every material evaluator finding

For each finding in the evaluator report:

1. Restate the claim in a concise, testable form.
2. Inspect the target passage quoted by the evaluator and verify it against the original target response.
3. Inspect the cited framework passage and verify that it actually says what the evaluator claims.
4. Determine whether the rule applies to this test and whether relevant qualifications or overrides exist.
5. Decide whether the evaluator’s judgment is supported.
6. Explain the disposition using target and source evidence.

Assign one status:

- **UPHELD:** The evaluator’s finding is supported.
- **DOWNGRADED:** A genuine issue exists, but the evaluator overstated its severity or certainty.
- **OVERTURNED:** The finding is unsupported, misapplied, or contradicted by the evidence.
- **UNRESOLVED:** The available evidence cannot establish the correct judgment.
- **FRAMEWORK DEFECT:** The finding exposes a conflict, omission, or ambiguity in the governing files.

Do not uphold a finding merely because its conclusion seems plausible.

### B. Independently inspect for evaluator omissions

Inspect the original target response against every applicable criterion in the test card. Do not limit your review to the findings already reported by the evaluator.

Identify:

- Genuine failures the evaluator missed.
- Missing evidence the evaluator incorrectly treated as present.
- Unsupported claims the evaluator failed to flag.
- Violations of output or dependency requirements.
- Incorrect assumptions about module loading or source access.
- Places where the evaluator mistook literary disagreement for procedural noncompliance.
- Places where a framework defect was incorrectly attributed to the target.
- Places where the evaluator overlooked a downstream consequence of an earlier failure.

Assign unique IDs to newly identified findings and explain why they matter.

### C. Check cross-file consistency

Use the actual supplied framework files to determine whether the evaluator interpreted the instructions correctly.

For each disputed rule:

- Identify the file, revision, section, and exact passage where possible.
- Check related files for qualifications, overrides, and contradictory instructions.
- Distinguish explicit requirements from inferred requirements.
- Do not invent precedence rules absent from the framework.
- If a rule cannot be located or verified, mark the claim unsupported by the supplied sources or unresolved.

A model’s assertion that a module was loaded does not independently prove that it was available. Likewise, the evaluator’s assertion that a rule exists does not prove that the rule says what the evaluator claims.

### D. Separate kinds of disagreement

Do not conflate these categories:

1. **Target failure:** The target violated a supported, applicable framework requirement.
2. **Evaluator error:** The evaluator misquoted, misapplied, overlooked, or overinterpreted evidence.
3. **Adjudicator disagreement:** You dispute the evaluator’s conclusion; your disagreement must itself be supported.
4. **Framework defect:** The instructions conflict, are incomplete, or do not determine expected behavior.
5. **Literary disagreement:** Reviewers differ about the interpretation or quality of a reading without an established procedural violation.
6. **Evidence limitation:** The available files or outputs are insufficient to resolve the question.

Do not turn a disagreement into a confirmed failure merely because a final report is expected.

### E. Check the adjudicator’s own reasoning

Before finalizing the report:

- Recheck every proposed overturned finding against the source and target evidence.
- Confirm that every newly identified failure has a supporting rule and observable target evidence.
- Identify any conclusion that depends on an unstated assumption.
- Preserve unresolved matters rather than forcing consensus.
- Distinguish a source-verified conclusion from your own interpretation.

Do not assume that the evaluator is wrong merely because your role is to challenge it. A successful audit may uphold most or all of the evaluator’s findings.

### F. Required adjudication report

Return:

1. **Run identification and evidence limitations.**
2. **Summary of evaluator reliability:** What the evaluator got right, wrong, and missed.
3. **Finding-by-finding audit:** Original finding ID, evaluator claim, target evidence, source evidence, adjudication status, and rationale.
4. **New findings:** Issues the evaluator missed, with supporting evidence.
5. **Overturned or downgraded findings:** Why the original judgment was unsupported or overstated.
6. **Framework defects:** Exact conflicting passages or missing decision rules.
7. **Revised criterion-level results:** PASS, PARTIAL, FAIL, or NOT DETERMINABLE.
8. **Revised scores:** By dimension, with denominators and undetermined criteria disclosed.
9. **Remaining disputes:** What evidence or human decision would resolve them.
10. **Recommended next action:** The smallest useful source check, framework revision, or regression test.

Do not fabricate citations, paths, quotations, or line numbers. Do not treat your position as correct merely because you are the adjudicator.

Label the report:

**ADJUDICATION REPORT — SOURCE VERIFICATION REQUIRED FOR UNRESOLVED MATERIAL CLAIMS**

The adjudication report must explicitly identify which evaluator findings it upheld, downgraded, overturned, or left unresolved. It must also identify new findings and framework defects independently discovered.

## 11. Canonical benchmark corpus

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

## 12. Regression test cards

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

**Tests:** Whether the model explains repetition’s changing function and avoids letting analytical apparatus overwhelm the reading.

**Pass criteria:**
- Explains the function of repetition in context, not merely its presence.
- Identifies meaningful escalation or variation where supported.
- Includes only devices that contribute to the reading under the framework’s criteria.
- Follows output-length and sidecar constraints, if specified.

**Failure codes:** INVENTORY, RENDER.

### R8 — Prophecy without historical overreach

**Target:** “The Second Coming”

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

## 13. Scoring

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

Also report evaluator and adjudicator reliability qualitatively, based on supported and unsupported findings, missed issues, and unresolved claims. Do not combine all dimensions into a single average that could conceal a critical failure.

A high literary score cannot compensate for a critical procedural failure. A model’s procedural failure cannot be confirmed if the supposed rule exists only in an evaluator’s interpretation and cannot be located in the source files.

### Critical-failure rule

A critical failure must be reported explicitly even if the aggregate score is high. Do not allow strong performance on unrelated criteria to cancel it out.

A source ambiguity that prevents a reliable judgment is not a target failure; it is an unresolved issue or framework defect.

## 14. Failure taxonomy

Use these codes consistently across the evaluator report, adjudicator report, and final record.

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

Evaluator errors and adjudicator errors should be tracked separately from target failure codes. Do not classify an evaluator’s unsupported judgment as a target failure merely because it was included in the first report.

## 15. Repeatability and controlled comparisons

For each selected test, run:

- **Condition A:** Full required framework and standard reasoning setting.
- **Condition B:** Same inputs and modules, with a lower reasoning setting if the product exposes that control.
- **Condition C:** Deliberate dependency omission.

Repeat conditions where practical. Preserve every run; do not select only the best response.

Initially label outputs Run A, Run B, and Run C without revealing model identity or reasoning setting to the evaluator. Where practical, keep those details concealed from the adjudicator until its report is complete as well. This reduces expectation effects but does not eliminate them.

Reveal the configuration after the reports are saved.

A difference between settings establishes an observed difference, not its cause. Attribute a failure to reduced reasoning effort only cautiously and only when the comparison supports it.

### Comparison protocol

When comparing runs:

1. Use the same test card and poem.
2. Keep framework versions and supplied inputs identical except for the variable being tested.
3. Record any unavoidable differences.
4. Compare criterion-level outcomes, not just overall impressions.
5. Have the evaluator grade each run independently.
6. Have the adjudicator audit the reports without assuming that a newer, larger, or more capable model must be correct.
7. Source-check disputed findings before drawing conclusions about the framework or model configuration.

## 16. Completion criteria

A test is complete only when:

- The test manifest and raw target output are preserved.
- The evaluator has assessed each applicable criterion.
- The adjudicator has audited the evaluator’s findings and independently checked the target against the test card.
- Material framework-compliance claims have been checked against the pinned source files.
- Unresolved claims remain explicitly unresolved.
- Framework contradictions are recorded separately from model failures.
- Evaluator errors are recorded separately from target failures.
- Scores are reported separately for procedure, literary execution, dependency handling, and framework integrity.
- The final report includes evidence sufficient for another auditor to reproduce the judgment.
- The final record identifies the next regression test needed to verify a proposed fix.

## 17. Final report format

For each run, report:

1. Run ID and environment.
2. Test card and expected behavior.
3. Raw target output reference.
4. Evaluator’s provisional findings.
5. Adjudicator’s finding-by-finding audit.
6. New findings discovered by the adjudicator.
7. Source-verified findings.
8. Overturned or downgraded findings.
9. Framework defects or ambiguities.
10. Procedural score and denominator.
11. Literary-execution score and denominator.
12. Dependency-handling score and denominator.
13. Framework-integrity findings.
14. Not-determinable criteria.
15. Failure codes with supporting evidence.
16. Comparison with earlier runs.
17. The next regression test needed to verify a proposed fix.

## 18. Final operating rule

The test subject produces the artifact. The evaluator grades the artifact. The adjudicator audits the grade against the artifact and the framework. Source verification establishes what the files actually require.

The adjudicator is not a second opinion to average with the evaluator. It is an adversarial review of the evaluator’s work. It may uphold, downgrade, or overturn the evaluator’s judgments, and it must look for failures the evaluator missed.

The source files are the evidence for framework requirements, not a guarantee that the framework is internally coherent. When the files cannot resolve a dispute, the suite must preserve that uncertainty and identify the framework clarification needed.

**No model is granted final authority merely because it is the last model in the chain. The final result must remain evidence-based, traceable, and reproducible.**
