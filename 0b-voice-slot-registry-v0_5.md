# VOICE SLOT REGISTRY

Version: 0.5

An apparatus-level registry for the Portable Poetics Kernel v0.3. It holds the voice slot matrix, the test a thinker must pass to occupy a slot, the log of candidates considered, and the conditions under which a closed slot reopens. It runs standalone and requires no private core.

Nothing here derives from any one source. A source module has authority over its own tools and no authority over the slot matrix.

## Module Manifest

Module name: Voice Slot Registry
Module type: apparatus registry
Kernel requirement: Portable Poetics Kernel v0.3
Private-core requirement: none
Consumers: any voice module, extraction, device extension, or foundations note that needs its own slot status

Exports:

- triggers: none. The registry answers status queries and fires nothing
- procedures: the voice test; slot state assignment; candidate logging
- output fields: none
- constraints: no source content; no tools; no voice zone
- failure modes: slot creep, log-as-authority, accretion

## The Voice Test

A voice module renders in the first person inside declared zones. Which means a candidate must be able to say where it has nothing to say.

Non-activation conditions are what make triangulation work. A voice that never stands down cannot disagree with anything, because it will absorb any specimen into its own account. Disagreement requires that at least one voice be silent, or wrong, or out of jurisdiction on a given case.

The five loaded voices each pass, and their conditions are the evidence:

| Voice | Stands down when |
|---|---|
| ASSAY | A more specific active voice is loaded for the specimen |
| TARE | The poem does not gate, at which point cult-mimicry holsters |
| RETICLE | There is no procedure to describe |
| PLUMB | There is no witnessable ground; attitude without receipts is not the register |
| DATUM | Interpretation is requested as interpretation; or there is no record; or the specimen has no account of itself |

Three clauses for a candidate:

1. Does the method have a domain it does not claim?
2. Does the method have purchase on poems?
3. Is there a corpus of actual readings behind the register, so that recurring moves, an operational lexicon, and output zones can be declared rather than invented?

A candidate failing clause 1 may still enter as an extraction, carrying tools without the jurisdiction claim. A candidate failing clause 2 or 3 cannot be a voice at all, and may or may not be usable in some other form.

## Slot States

Three states, and the difference determines what to do next.

**Filled.** A module is loaded and its zones are live.

**Empty.** No module exists yet, and one could. The zones fall to the default register in the meantime. An empty slot is a build waiting to happen.

**Closed.** No candidate can pass the voice test for structural reasons, so the slot is not a build waiting to happen. Closed slots are recorded rather than deleted, because an open-looking slot invites candidates against a test none of them can pass.

## The Slot Matrix

| Designation | Slot | State | Module | Notes |
|---|---|---|---|---|
| ASSAY | Reception and canon formation | Filled | `1-rother-voice-module` | Holds the default verdict slot |
| TARE | Plain speech, workshop, body-cost | Filled | `3-kowit-voice-module` | Workshop mode at `3a-workshop` |
| RETICLE | Procedure and the examined lyric | Filled | `3-perloff-voice-module` | Carries a declared blind spot |
| PLUMB | Labor, prison, soldier, body-in-system | Filled | `2-harris-voice-module` | Corrected in v0.2. See Amendment History |
| DATUM | Provenance and the official account | Filled | `5-hersh-voice-module` | Hard dependency on `11-provenance-grading-extension` |
| none | Whole-system view | Closed | none | Unnamed by design. See below |

This table is the mapping. It is apparatus-internal prose and is not output. The designation column is authoritative under `0c-voice-designations`; the module column is the registry's own. A designation belongs to the slot, so replacing a module changes the module column and leaves the designation standing.

The whole-system slot receives no designation. An unnamed closed slot is harder to mistake for a vacancy, which is this registry's standing concern, and a closed slot with a name of its own reads as a build waiting to happen.

## The Whole-System Slot

Closed, not vacant.

The reason generalizes past any candidate. A method claiming to see the whole cannot also state where it does not apply, and clause 1 of the voice test is exactly that statement. So the whole-system view is unvoiceable in this architecture by construction, and the slot was never empty for want of a suitable thinker.

The absence recorded in v0.1 has grown, and honesty requires saying so rather than letting the new slot obscure it. All five loaded voices are suspicious readers. Rother suspects reception, Kowit suspects the priesthood, Perloff suspects the unexamined lyric, Harris suspects the institution's account of its own cost, and Hersh suspects every account of itself that any party has committed to. Nothing in the matrix argues that a poem participates in an inheritance which is not a conspiracy. Adding the fifth voice deepens that absence rather than addressing it, since the new voice is the most systematically suspicious of the five. It is still not the same absence as the whole-system view, and conflating the two is how a closed slot gets reopened on a candidate who addresses neither.

## Candidate Log

Each entry at its actual weight, which is not the same for all of them.

| Candidate | Status | Result |
|---|---|---|
| Hersh | Voice module built, `5-hersh-voice-module` v0.1 | Passed all three clauses. Clause 1 passed on an axis no prior candidate used: the stand-down is stated by the source, in the form of a documented refusal to add an interpretive paragraph to a report, made against an ally and at the cost of a magazine cover. Clause 2 passed on a portable procedure rather than on poem readings. Occasioned the clause-3 object question below, and `11-provenance-grading-extension`. |
| Frye | Extraction built, `8-frye-extraction` | Failed clause 1 on synoptic jurisdiction, the argument of his Polemical Introduction. Also carries a twenty-four-cell grid, four mythoi at six phases, into which every poem lands. Yielded three tools, one clarification, one calibration note. |
| Casanova | Extraction built, `9-casanova-extraction` | Failed clause 1 on total positional explanation, which she extends in her preface to the cases that look furthest from determination. Yielded seven tools and a directive. |
| Leibniz | Foundations note built, `10-monadology-foundations` | Passed clause 1. His confusion clause is a genuine stand-down stated by the system rather than imposed on it. Failed clauses 2 and 3, having written nothing about poems. Occasioned clause 2. |
| Silliman | Judgment call, not built | Two-camp map of a national field, predicted to fail clause 1 and declined on the operator's reading rather than tested. `New sentence` had already entered through the Perloff voice module, so the expected extraction yield was near zero. |
| Hoagland | Extraction built, `13-speaker-dials` | Not run against the voice test. The operator asked for craft tools, not a reading register, and the extraction was built for a mode rather than for readings. On a reading of the book, clauses 2 and 3 would likely pass, since it carries sustained readings of some fifty poems. Clause 1 would rest on two concessions in the text, that some poems invest less in this dimension than in story and image, which is operator inference at the weaker standard. The register it would carry sits inside the TARE slot, so a voice build would need a slot decision first. Yielded four established dials, five provisional, and a drill-conversion set. |
| Rothenberg | Declined at concept stage | Assembling is a compositional method rather than a question with a gate, so it would not cash out on a page. Better used as a specimen for the Casanova tools than as a source. An appropriation problem also attaches, and the Casanova tools describe its mechanism from outside. |

## Evidential Weight

Two voice modules built from journalism, three extractions, one foundations note, one judgment call, one declined at concept. Five qualifications keep it honest.

The Silliman entry records a prediction rather than a result. He was expected to fail clause 1 and was never tested.

Frye and Casanova are not independent evidence in the ordinary way. Her argument is aimed at exactly the dehistoricized reading his method produces, so she is partly his corrective. Two thinkers who disagree with each other failing the same test is stronger than two from one school, and it is still two.

Leibniz cuts differently from the other two. He passed the clause the others failed, which is what makes him evidence about the test rather than evidence about the pattern.

Hersh cuts differently again, and in the direction that matters most for the test's calibration. Every prior clause-1 pass or fail was assigned by the operator reading the candidate's method for an implied jurisdiction claim. Hersh is the first candidate whose stand-down is on the record in his own words as a refusal he acted on. That is stronger evidence than an inferred boundary, and it raises the question of whether the earlier assignments were graded at the same standard. They were not. Frye's and Casanova's failures rest on argued jurisdiction claims, which is solid. Rother's, Kowit's, and Perloff's passes rest on operator inference, which is weaker than the standard Hersh met.

Hoagland is not evidence about the test at all, because the test was not run. His entry records an extraction built to an operator instruction and a guess at how the clauses would fall. It belongs in the log because the extraction exists and a later reader should not find a source in the apparatus with no entry here, and it should not be counted as a pass, a fail, or a prediction.

## Reopen Conditions

Reopen the whole-system slot on a candidate who passes all three clauses of the voice test.

## Amendment History

Kept because it records how conditions were found to be wrong.

The reopen condition originally ran to two clauses: holds the whole-system view, and can state where the method does not apply. Leibniz satisfied both and remained unusable. Clause 2, purchase on poems, was added afterward. Clause 3, an existing corpus of readings, was implicit in the voice module contract and was stated in v0.1 so that a candidate could not pass on the strength of a method alone.

**v0.2, the Harris row.** The matrix carried the labor, prison, soldier, body-in-system slot as Empty, with a note that those specimens fell to the default register, after `2-harris-voice-module` v0.3 had been built and loaded. The row was stale for at least one release. The failure was not slot creep or log-as-authority but their inverse: a build happened and the matrix was not updated, so the registry understated its own coverage. Add to Failure Modes as Stale Matrix.

**v0.2, the clause-3 object question.** Clause 3 asks for a corpus of actual readings and is silent on what the readings are of. Both journalist voices passed it on corpora containing no poem readings at all. That silence has now been load-bearing twice, which is once past coincidence. Two options and the registry does not choose between them here, because this is the operator's call: state the silence deliberately, on the ground that a register is trainable from any corpus of sustained readings and the poem application is clause 2's business; or tighten clause 3 to require at least one worked poem case before a pass. The Hersh module ships with one worked poem case in outline, which satisfies the tighter reading in form and not yet in evidence.

**v0.3, designations.** The matrix gained a designation column and the stand-down table was converted to designations, on an operator instruction that generated output carry function names rather than calibration-source identity. Two findings came out of the conversion and belong in the log rather than in the layer.

The first is that a designation must name the slot and not the module, or it is a pseudonym rather than a name, and a pseudonym that travels with a person leaks the moment anyone matches two readings. Naming the slot also means the designation survives a module replacement, which the matrix already contemplates and had no vocabulary for.

The second is that the conversion could not be completed. Six kernel directives carry a specimen attribution that discloses one mapping, and the registry's own Candidate Log names every candidate considered. Both are apparatus-internal prose and neither is output, so neither breaks the policy. They do mean the layer is an output-hygiene measure and not a seal, and the registry should not be cited as though it were one.

**v0.4, the version sweep.** Module-column entries were reconciled against what is on disk. Two were wrong. The workshop module had been renamed during its hygiene pass and the column still carried the old name. The DATUM module had been shipped under a number already held by the style mode, so it moves to `5-hersh-voice-module`; the collision was introduced when the module was built and the registry recorded it without checking the number was free.

The second one is the instructive failure. This registry added Stale Matrix as a failure mode two releases ago, on the observation that a build had happened and the matrix was not updated. The correction said a matrix row is part of the module build. It said nothing about the row being checked against the rest of the apparatus, so the next build produced a row that was internally consistent and collided with a file the registry does not track. Extend the correction: a new row is checked for a free identifier, not only for a correct state.

**v0.5, the untested extraction.** `13-speaker-dials` is the first extraction built for a mode rather than for readings, and the first whose source was never put to the voice test. The log gains an entry anyway, on the Stale Matrix lesson run in reverse: a source loaded into the apparatus with no entry here is the same understatement as a filled slot marked empty. Identifier 13 was checked free against the hollow boot's registry and against every apparatus file supplied to the build session before the extension took it, per the v0.4 correction. The files the boot lists as referenced and not held were not available to check. The matrix is unchanged, since an extraction occupies no slot.

**v0.2, the clause-1 grading standard.** See Evidential Weight. Three of the five loaded voices passed clause 1 on operator inference rather than on a stated and acted-upon refusal. Not grounds for unseating them. Grounds for recording that the passes are not all the same strength.

A condition only gets tested by a case it was not written for. Expect the next amendment to arrive the same way.

## The Extraction Asymmetry

The standing cost of the extraction pattern, and it applies to every extraction rather than to any one of them.

An extraction has no voice zone. So when an extraction's position meets a loaded voice on the same specimen, the voice renders in the first person and the extraction appears as a note in the default register. Rendered voice outpersuades a cited principle, reliably, and the asymmetry runs the same direction every time.

The standing instance: Frye holds that the artist is overheard rather than heard and that direct address falls to metrical talk, while Kowit's whole project is direct address in plain speech. On an address specimen Kowit speaks and Frye is quoted.

New in v0.2, and worse than the first instance because the two positions are closer. The Casanova tools explain a work's features by its position in a field. The Hersh omission audit reads a work's account of itself for what the omission protects. Both work on the apparatus around the artifact, and they will reach the same material by different mechanisms and disagree about which mechanism is operating. On such a specimen Hersh speaks in the first person and Casanova is cited, and the asymmetry now favors the voice on a case where the extraction has the more developed theory.

Accepted as the lesser problem, since the alternative is a voice that cannot stand down. State the imbalance in any reading where an extraction meets a voice, so it operates in the open.

## Division of Labor

A source module carries its own tools, its own worked cases, its own refusal ledger, and its own reason for being an extraction rather than a voice.

A device extension carries a procedure with more than one consumer and no jurisdiction claim.

This registry carries the test, the matrix, the log, the reopen conditions, and the pattern across candidates.

None restates the others. A source module needing its slot status points here. This file names no tools and quotes no sources.

## Failure Modes

### Slot Creep

A candidate gets proposed against the closed slot because the slot appears in the matrix and looks like an opening.

Correction: closed is a state, not a vacancy. Run all three clauses before discussing a candidate at any length.

### Stale Matrix

New in v0.2. A module gets built and loaded and the matrix keeps the old state, so the registry understates coverage and a later reader treats a filled slot as a build waiting to happen. The inverse of slot creep and just as costly.

Correction: the matrix row is part of the module build, not a follow-up to it. A voice module is not finished until its row reads Filled, its identifier is free, and its module name matches the file on disk.

### Log-As-Authority

The candidate log gets read as a record of seven tested cases, when it holds two voice modules, three built extractions, one of them never tested, one foundations note, one prediction, and one concept-stage refusal, graded at more than one standard.

Correction: Evidential Weight is part of the log and not a footnote to it.

### Accretion

Apparatus-level decisions collect inside whichever source module happened to occasion them, so that a later reader has to know the history to find the current rule.

Correction: this file exists because that already happened once. When a decision is about the matrix rather than about a thinker, it belongs here. The v0.2 build followed the rule ahead of the fact: the provenance procedure the Hersh corpus occasioned went to `11-provenance-grading-extension` rather than into the voice module, because it has more than one possible consumer.

## Provenance

v0.1 extracted from `8-frye-extraction` v0.4, where the case log, the closure decision, and the reopen condition had accumulated across several sessions because the log was first written into that file.

v0.2 occasioned by a comparative reading of five complete Hersh chapters against the Harris corpus in September 2026. Carries the new slot row, the Harris row correction, the Hersh candidate entry, three amendments, one new failure mode, and one new instance of the extraction asymmetry.
