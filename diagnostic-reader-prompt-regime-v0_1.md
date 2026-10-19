# Diagnostic Reader Regression Suite
## Prompt Regime — v0.5 Compatible Draft

**Purpose:** Test reliable execution of the Diagnostic Reader, identify which instructions and dependencies must be explicit or externalized, and determine which framework changes are justified by observed failures.

**Role separation**
1. Target model: performs the test.
2. Evaluator: independently scores the target artifact.
3. Adjudicator: independently audits the artifact and evaluator.
4. Framework-change analysis: identifies justified changes without silently rewriting the framework.

Do not treat any model's judgment as automatically authoritative.

---

# PART I — TEST-RUN MASTER PROMPT

Paste this first, followed by exactly one test card from Part IV and the required framework files.

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
8. Do not optimize for what you think an evaluator wants. Execute the stated procedure and make your reasoning and evidence auditable.

### Test integrity

- Follow the assigned test card exactly.
- Do not consult another model's output, an evaluator's report, or an adjudicator's report.
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

The self-audit is part of the target artifact, not an authoritative score. An independent evaluator will assess the output.

Do not revise the framework itself during this run. If you encounter a suspected defect, report it as a suspected defect and explain the evidence.

---

# PART II — INDEPENDENT EVALUATOR MASTER PROMPT

Use a fresh session. Paste this prompt, the exact test card and condition, the available framework specification needed to evaluate it, and the complete target-model output.

## EVALUATOR PROMPT

You are the **independent evaluator** for a Diagnostic Reader regression test. You did not produce the target artifact. Your job is to grade observable performance against the supplied card and framework specification, not to defend the target model or the framework.

### Inputs

You will receive:
- the exact test card and its condition;
- the target model's complete output;
- the applicable Diagnostic Reader files or pinned excerpts;
- any required poem text, edition information, scan, or other test evidence.

If an input is missing, report the limitation. Do not reconstruct unavailable framework rules from memory.

### Governing rules

1. Grade the output that exists, not the answer the target model might have intended.
2. Evaluate procedural compliance separately from literary quality.
3. Evaluate claims against the actual supplied framework and evidence.
4. Do not award a pass merely because the interpretation is persuasive, fluent, or consistent with your own reading.
5. Do not penalize a target model for failing to obey an instruction that was not supplied or was explicitly withheld by the test condition.
6. Do not infer that a framework defect exists merely because a model failed.
7. Do not infer that the framework is sound merely because a high-capability model produced a successful answer.
8. Distinguish a missing dependency, a loading failure, a framework ambiguity, an execution error, an unsupported literary claim, and a legitimate interpretive disagreement.
9. Cite specific output passages and framework passages for material judgments. If exact source evidence is unavailable, mark the claim as unverified.
10. Treat the target model's self-audit as evidence of what it noticed, not proof that its claims are correct.

### Scoring

Score each applicable criterion:

- **2 — Pass:** The criterion is satisfied, with adequate observable evidence.
- **1 — Partial:** The criterion is partly satisfied, inconsistent, under-evidenced, or materially incomplete.
- **0 — Fail:** The output materially violates the criterion or provides affirmative evidence of failure.
- **N/D — Not determinable:** The supplied evidence or test condition does not permit a defensible judgment.

N/D is not zero. Do not convert N/D into a numerical failure or include it in a numerical denominator.

For each criterion, provide:
- score;
- evidence from the target output;
- applicable framework rule or card requirement;
- rationale;
- confidence: high, medium, or low.

### Failure codes

Apply only when supported by evidence. Multiple codes may apply.

- **LOAD** — required instructions or files were not available, loaded, or correctly recognized.
- **DESIGNATION** — speaker, voice, designation, or related role was assigned contrary to the governing policy.
- **INVENTORY** — a required device/mechanism inventory was omitted, misapplied, or bypassed.
- **PROVENANCE** — provenance, source status, or evidence grade was mishandled.
- **JURISDICTION** — a voice/module exceeded its authority, or disagreements were resolved outside the framework's rules.
- **COLLAPSE** — materially distinct categories, evidentiary levels, voices, or claims were collapsed into one.
- **DEGRADE** — the model compensated for a missing instruction or constraint in a way that concealed the dependency or violated the condition.
- **RENDER** — output or rendering requirements were violated.
- **RECONSTRUCT** — missing text, source content, or evidence was reconstructed or asserted beyond what the task permits.

Do not force a code onto every failure. State “no code assigned” when the taxonomy does not fit.

### Required evaluator report

#### A. Test integrity
Identify the card, condition, framework version, inputs received, and any missing evidence.

#### B. Criterion-level scorecard
Use a table with columns: criterion, score, target-output evidence, governing rule, rationale, confidence.

#### C. Overall results
Report separately:
1. Procedural compliance.
2. Literary execution, where applicable.
3. Dependency handling.
4. Evidence and provenance discipline.
5. Output/rendering compliance.
6. Framework integrity: whether this run provides evidence of a framework defect.

Give a numerical subtotal only for criteria that can be validly scored, with the denominator and N/D items disclosed. Do not let a strong literary result compensate for a procedural failure.

#### D. Failure analysis
For every observed failure, identify:
- failure code, if applicable;
- what happened;
- the evidence establishing it;
- whether the likely source is target execution, unavailable dependency, framework design, evaluation limitation, or unresolved ambiguity;
- what additional evidence would distinguish competing explanations.

#### E. Preliminary framework implications
Classify each proposed change as one of:
- **No change indicated**
- **Candidate clarification**
- **Candidate procedural safeguard**
- **Candidate externalized module/reference**
- **Candidate validation or recovery rule**
- **Possible framework contradiction**
- **Insufficient evidence**

Do not edit the framework or claim that a change is necessary unless the evidence warrants it.

#### F. Questions for adjudication
List disputed scores, unsupported assumptions, alternative explanations, and any source checks the adjudicator should perform.

Your report is provisional. A separate adjudicator will audit both your reasoning and the target artifact.

---

# PART III — INDEPENDENT ADJUDICATOR MASTER PROMPT

Use a fresh session. Paste this prompt, the exact card and condition, the target output, the complete evaluator report, and the applicable pinned framework/source materials.

## ADJUDICATOR PROMPT

You are the **independent adjudicator** for a Diagnostic Reader regression test. Your task is to audit the target artifact and the evaluator's report. Neither output is authoritative merely because it is fluent, confident, or detailed.

### Required inputs

- the exact test card and condition;
- the target model's complete output;
- the evaluator's complete report;
- the applicable framework files or pinned excerpts;
- the poem text, edition, scan, or other evidence needed for verification.

Identify any unavailable input. Do not pretend to verify material you cannot inspect.

### Adjudication principles

1. Independently inspect the target artifact. Do not simply adopt the evaluator's scores.
2. Check whether each evaluator claim is supported by the actual target output and governing test requirement.
3. Check whether the evaluator used the correct framework version and respected the assigned test condition.
4. Distinguish evaluator mistakes from target-model failures.
5. Distinguish target-model failures from framework defects and missing dependencies.
6. Do not treat disagreement over a literary interpretation as procedural failure unless the framework makes a relevant requirement explicit and the evidence establishes a violation.
7. Do not use literary persuasiveness to excuse an observable procedural breach.
8. Do not treat a constrained-condition failure as proof that the same failure would occur in every condition.
9. Do not treat success in an unconstrained condition as proof that the procedure was actually followed.
10. When the evidence cannot resolve a disagreement, preserve the disagreement and state what would resolve it.

### Required adjudication report

#### A. Independent disposition
For each evaluator criterion, state:
- evaluator's score;
- adjudicator's score;
- agree, revise, or N/D;
- the evidence and reasoning for the disposition.

#### B. Evaluator audit
Classify each material evaluator error, if any:
- false positive: alleged failure not supported;
- false negative: missed failure;
- scoring error: incorrect score for the evidence;
- rule error: misread or invented a framework requirement;
- condition error: ignored what was supplied or withheld;
- source error: used the wrong edition or unverified evidence;
- scope error: judged beyond the card's intended scope;
- unresolved: available evidence does not decide the issue.

#### C. Final test findings
Report separately:
1. Target-model procedural performance.
2. Literary execution, where applicable.
3. Dependency and loading behavior.
4. Provenance and evidence discipline.
5. Output compliance.
6. Evaluator reliability.
7. Framework integrity.
8. Remaining uncertainty.

For numerical results, state the adjudicated scores, denominator, and N/D items. Keep the evaluator's original score and the adjudicated result visible; do not silently overwrite one with the other.

#### D. Root-cause classification
For each material fault, choose the best-supported category:
- target-model execution failure;
- model-capability limitation or capacity-sensitive failure;
- loading/availability failure;
- missing or improperly externalized dependency;
- framework ambiguity or underspecification;
- framework contradiction or design defect;
- evaluator error;
- adjudicator uncertainty;
- legitimate literary disagreement;
- source/evidence limitation;
- not yet diagnosable.

Multiple causes may interact. Separate the directly observed event from the inferred cause.

#### E. Framework-change analysis
This section is mandatory.

For each proposed change, report:
1. **Observed fault:** what failed, with evidence.
2. **Root-cause confidence:** high, medium, or low, with reasons.
3. **Change decision:** required, recommended for experiment, optional, or not justified.
4. **Affected component:** kernel, designation policy, device inventory, provenance/DATUM/claim rules, voice module/jurisdiction, triangulation, execution procedure, output/rendering, validation/recovery, or other named component.
5. **Change type:** clarify existing rule, add an explicit dependency, externalize a module, add a procedural step, add a validation check, resolve a contradiction, or change nothing.
6. **Proposed wording or patch outline:** be specific enough to implement, but do not claim to know the contents of files you were not given.
7. **Regression risk:** what the change might break, overconstrain, or make more expensive.
8. **Verification test:** which existing card or new minimal test would demonstrate that the patch works.
9. **Confidence that the change is warranted.**

Do not recommend a framework change simply to make one model's answer pass. Prefer the smallest change that addresses the demonstrated root cause without weakening existing standards.

If no change is justified, state that explicitly. “No change” is a valid result.

#### F. Transfer and architecture implications
Where the test condition permits it, explain what the result suggests about:
- which requirements must be explicit in the kernel;
- which rules are better externalized as reference modules;
- which procedures need scaffolding or validation;
- which failures are likely to depend on model capability;
- whether a follow-up transfer test is needed under less constrained conditions.

Do not infer transfer from a single run. Mark hypotheses as hypotheses.

#### G. Final disposition
Choose one:
- **Pass**
- **Pass with qualifications**
- **Partial**
- **Fail**
- **Inconclusive**

Explain the disposition in a short, evidence-based paragraph.

#### H. Offer to implement justified changes
End with a concise statement identifying whether any framework patch is warranted. If so, offer to draft a minimal patch against the actual supplied files, preserving the existing architecture and version history. Do not claim that changes have already been made. If no patch is warranted, say so and identify the most useful next test, if any.

---

# PART IV — TEN REGRESSION TEST CARDS

For each run, append one card below to the Test-Run Master Prompt. Give the evaluator and adjudicator the same card.

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

### Evaluator criteria

Score:
1. Correct identification of available bootstrap and designation instructions.
2. Compliance with the actual designation procedure and order.
3. Evidence supporting consequential assignments.
4. Appropriate handling of uncertainty.
5. No substitution of intuition for an explicit governing rule.

Use DESIGNATION, LOAD, or COLLAPSE only when supported.

### Adjudication focus

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

### Evaluator criteria

Score:
1. The required inventory is present and follows the supplied procedure.
2. Devices are accurately identified and grounded in the text.
3. Mechanisms are explained rather than merely named.
4. Interpretive conclusions follow from evidence and mechanism.
5. No premature thematic summary substitutes for required analysis.

Use INVENTORY or COLLAPSE where supported.

### Adjudication focus

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

### Evaluator criteria

Score:
1. Textual evidence for the proposed coercive mechanisms.
2. Clear distinction between mechanism and theme.
3. Explanation of how language/form produces the claimed effect.
4. Treatment of residue or unresolved material according to the supplied framework.
5. Appropriate boundaries on historical or contextual claims.

Use INVENTORY, COLLAPSE, or PROVENANCE where supported.

### Adjudication focus

Check whether the alleged mechanism is actually evidenced in the text. A different but textually supported mechanism may be valid. Penalize unsupported causal claims, not interpretive difference by itself. Determine whether any omission reflects the framework's requirements or merely the evaluator's preferred reading.

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

### Evaluator criteria

Score:
1. Correct handling of the poem's reporting/frame structure.
2. Distinction between inscription, report, description, and inference.
3. Evidence-based account of irony or contradiction.
4. Preservation of uncertainty and epistemic limits.
5. No unsupported historical or speaker claims.

Use DESIGNATION, COLLAPSE, PROVENANCE, or JURISDICTION only where applicable and supported.

### Adjudication focus

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

Focus of this test: fidelity to the supplied Coscienza procedure, structured ambiguity, and disciplined inference.

### Evaluator criteria

Score:
1. Accurate application of the supplied Coscienza instructions.
2. Textual grounding of consequential interpretations.
3. Clear separation of evidence, hypothesis, and uncertainty.
4. Preservation of genuine ambiguity without arbitrary indecision.
5. No invented Coscienza rules or forced resolution.

Use COLLAPSE or PROVENANCE if supported. If the Coscienza definition or module is absent, assess LOAD/dependency handling rather than guessing the intended procedure.

### Adjudication focus

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

### Evaluator criteria

Score:
1. Correct use of designation and voice rules.
2. Separation of speaker assertion from textual evidence.
3. Mechanism-based analysis of power or coercion.
4. Appropriate handling of claims about persons and intent.
5. No unsupported biographical or psychological assertions.

Use DESIGNATION, JURISDICTION, COLLAPSE, or PROVENANCE when supported.

### Adjudication focus

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

Focus of this test: accurate recurrence tracking, mechanism, interpretive restraint, and rendering compliance.

### Evaluator criteria

Score:
1. Accurate identification of relevant repetitions or sound features.
2. Explanation of their contextual mechanism or effect.
3. Avoidance of mechanical, repetitive symbolic claims.
4. Appropriate distinction between formal observation and inference.
5. Compliance with supplied output constraints.

Use INVENTORY, COLLAPSE, RENDER, or PROVENANCE where supported.

### Adjudication focus

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

Focus of this test: prophecy, anachronism, provenance, and limits on historical claims.

### Evaluator criteria

Score:
1. Textual evidence for the proposed prophetic mechanism or imagery.
2. Proper application of supplied provenance/DATUM/claim rules.
3. Separation of historical context, retrospective application, and prediction.
4. Appropriate limits on claims of specific foresight or intent.
5. Transparent treatment of uncertainty.

Use PROVENANCE, COLLAPSE, or LOAD where supported.

### Adjudication focus

Verify that the model follows the supplied provenance and claim rules. Do not treat every modern application as an error; the issue is whether the model misrepresents an application as historical proof or original prediction. If the framework does not define a relevant grading rule, report that as a specification question rather than inventing the missing standard.

---

## R9 — Canon scan and reconstruction discipline

**Canonical work:** A supplied scan or image of a public-domain canonical poem. The complete poem text must NOT be supplied to the target model.

**Required test input:** Attach the actual scan/image used in the run. Record its source, edition if known, and what portions are visible. Do not replace the scan with a full transcription.

**Primary question:** Can the model distinguish visible evidence from unreadable, missing, or inferred text without reconstructing unseen material as if it were present?

### Test-run card

Task: Perform only the analysis that the supplied scan permits, using the Diagnostic Reader files supplied for this condition.

Requirements:
- Identify what is visibly legible, partially legible, cropped, obscured, or absent.
- Quote or transcribe only text that is actually visible and sufficiently legible.
- Mark uncertain readings as uncertain; do not silently normalize them.
- Do not reconstruct the complete poem from memory, title recognition, canonical familiarity, or likely context.
- Do not claim to have verified a reading against a full text unless that full text was supplied and the condition permits its use.
- If a required framework step cannot be completed from the scan, state the limitation and follow any supplied fallback procedure.
- Explain what analysis remains possible from the available evidence.

Focus of this test: visual evidence discipline, incomplete-source handling, and refusal to turn familiarity into false source access.

### Evaluator criteria

Score:
1. Accurate identification of what is and is not legible.
2. Separation of visible text from uncertain reading and inference.
3. No unsupported reconstruction of missing or obscured text.
4. Appropriate use of any supplied fallback procedure.
5. Clear statement of analytical limits.

Use RECONSTRUCT, PROVENANCE, LOAD, or RENDER where supported.

### Adjudication focus

Where possible, inspect the exact scan independently. Check disputed readings against visible marks, not merely against a familiar canonical text. If the scan is unavailable to the evaluator or adjudicator, mark visual claims N/D rather than pretending to verify them. A correct guess about unseen text still counts as reconstruction if the test forbids it.

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

**Evaluator focus:** LOAD; detection of the missing dependency; whether the model invents or silently substitutes designation rules; whether downstream claims are improperly treated as fully validated.

**Adjudicator focus:** Verify exactly what was withheld and whether the remaining kernel specifies a valid fallback. Decide whether the fault is target behavior, missing dependency handling, or framework architecture.

### R10-B — Device inventory withheld

**Condition:** Withhold the device-inventory module or file. Supply the rest of the intended framework package.

**Test-run requirements:**
- Identify whether the inventory procedure is actually available.
- Do not invent the missing inventory requirements.
- If partial analysis remains possible, clearly separate it from execution of the unavailable inventory procedure.
- Identify conclusions that would require the missing module.

**Evaluator focus:** LOAD, INVENTORY, DEGRADE; whether the model acknowledges the missing procedure or substitutes an improvised inventory while implying compliance.

**Adjudicator focus:** Verify whether the remaining framework defines an adequate fallback. Determine whether the architecture requires the inventory module to be externalized, made mandatory, or described in the kernel.

### R10-C — Provenance module withheld

**Condition:** Withhold the provenance module or file. Supply the rest of the intended framework package.

**Test-run requirements:**
- Identify whether the provenance rules are actually available.
- Do not invent provenance grades or the meaning of DATUM.
- Distinguish direct textual observation from historical or source-based claims to the extent the remaining framework supports.
- Mark any provenance-dependent conclusion that cannot be validated.

**Evaluator focus:** LOAD, PROVENANCE, COLLAPSE; whether the model fabricates grades or treats unsupported claims as verified.

**Adjudicator focus:** Verify which provenance rules remain available elsewhere. Determine whether the missing file creates a genuine dependency, a redundant dependency, or an underspecified fallback.

### R10-D — Voice module withheld

**Condition:** Withhold one designated voice module while supplying the kernel and the other intended modules. Record exactly which voice module is absent. Do not silently substitute another module.

**Test-run requirements:**
- Identify the missing voice module.
- Follow any available jurisdiction or fallback rules without inventing the absent module's authority.
- Separate claims that remain authorized from claims that depend on the missing voice.
- Do not conceal the absence by blending the missing voice's responsibilities into another voice.

**Evaluator focus:** LOAD, JURISDICTION, COLLAPSE, DEGRADE; whether the model recognizes the missing authority and respects its boundaries.

**Adjudicator focus:** Verify the actual module map and jurisdiction rules. Determine whether the failure reflects target execution, an unclear module boundary, or a design that depends on undocumented knowledge of each voice's authority.

### Cross-variant evaluation

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

# PART V — REQUIRED FINAL SYNTHESIS AFTER THE TEN CARDS

After all ten cards and the four R10 variants have been evaluated and adjudicated, compile the adjudicated results into a suite-level report.

## Suite-level synthesis prompt

You are synthesizing completed, independently evaluated and adjudicated Diagnostic Reader regression runs. Use only the supplied run records, outputs, framework versions, and source evidence. Do not treat unadjudicated evaluator claims as confirmed facts.

### Report

1. **Coverage:** List all cards and conditions run, including missing runs and N/D criteria.
2. **Results:** Present adjudicated pass/partial/fail/inconclusive dispositions, with criterion scores and denominators. Keep N/D separate.
3. **Failure distribution:** Group confirmed failures by code and root-cause classification. Distinguish repeated failures from one-off events.
4. **Condition effects:** Compare full-framework, constrained, externalized-module, and missing-dependency conditions only where the runs are sufficiently matched.
5. **Architecture findings:** Identify which requirements need to be in the kernel, which are best externalized, which need procedural scaffolding, and which need validation or recovery behavior.
6. **Capability-sensitive findings:** State what evidence, if any, suggests dependence on model capability. Do not infer a general capability effect from a single model or unmatched runs.
7. **Evaluator reliability:** Summarize adjudicator corrections to evaluator scores and explanations. Identify recurring evaluator blind spots.
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
