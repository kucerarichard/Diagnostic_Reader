# PROVENANCE GRADING EXTENSION

Version: 0.1

A device extension for the Portable Poetics Kernel v0.3. It supplies a graded claim-standing field for any reading, plus the properties a graded claim must satisfy. It runs standalone and requires no private core and no voice module.

This file exists because the Hersh corpus made the gap visible. `Register Is Not Referent` states the rule that a register's claim about its own referent is not the referent, and supplies no procedure for grading the claim once it is caught. Every Hersh attribution states what standing its claim has. That practice is apparatus-level, so it belongs here rather than inside a voice module, and it is filed here before the misfiling rather than after.

## Module Manifest

Module name: Provenance Grading Extension
Module type: device extension
Kernel requirement: Portable Poetics Kernel v0.3
Private-core requirement: none
Consumers: any voice module, extraction, or sidecar that makes claims about a specimen, its author, or its reception

Exports:

- the provenance ladder, P0 through P5
- four properties of a graded claim
- the absence entry
- elision disclosure
- the scoping rule that resolves the conflict with Located Quote `unstitched`
- failure modes

Imports from kernel:

- Source Policy and source exposure Levels 0 through 4
- Located Quote properties
- Register Is Not Referent
- Weak Signal
- Default Register
- Mixed Log and closure rule

Constraints: no source content, no voice zone, no first-person rendering. The extension grades claims; it does not make them.

## The Provenance Ladder

Six levels. A reading may carry claims at several levels at once, and the point of the ladder is that they are not interchangeable.

**P0. On the page.** The artifact shows it. Line breaks, diction, a rhyme, a date printed in the colophon. No attribution needed because the reader can check it against the specimen.

**P1. Documented.** A dated record exists and is named. A letter, a contract, a manuscript variant, a magazine issue, a print run, a court filing, a log entry. The record is identified well enough that a reader could go find it.

**P2. Attributed on the record.** A named party asserts it and can be held to the assertion. An interview, a memoir, a preface, a public statement. P2 does not mean true; it means someone's name is on it.

**P3. Attributed with proximity stated.** An unnamed party asserts it, and the party's distance from the thing asserted is specified. Not "a source says" but the specific standing: someone who read the document, someone who was in the room, someone who was told by a person in the room. P3 without a proximity credential is not P3, it is P4 wearing a costume.

**P4. Unsourced inference.** The apparatus's own reading, marked as the apparatus's. Legitimate and frequently necessary. Illegitimate only when it presents as P0 through P3.

**P5. Absence recorded.** The document or statement that should exist does not, and the non-existence is the finding. P5 is the strongest claim on the ladder when it is earned and the weakest when it is guessed, so it carries an extra requirement: state where in the record the missing item should have appeared.

## Four Properties of a Graded Claim

**Standing declared.** Every claim above P0 carries its level, in the sentence or in the sidecar field. A reading that grades some claims and not others has graded none, because the ungraded ones read as P0 by default.

**Proximity credentialed.** At P3 the credential is specific and checkable in kind if not in identity. Rank, role, or access, not adjectives. "A senior figure" is not a credential. "Someone who read the classified report" is.

**Denial survival.** A claim is written so that a flat denial by the interested party does not dissolve it. This is a drafting test, not a truth test: if the only support for the claim is that the apparatus finds it plausible, the claim is P4 and must say so.

**Absence at the timestamp.** A P5 entry is placed at the point in the sequence where the missing item should have existed, not at the end as a summary complaint. An absence with no position in the record is not evidence.

## Elision Disclosure

Quotation that compresses a source by ellipsis declares the elision. Two forms.

**Specimen quotation.** Governed absolutely by the kernel's Located Quote property `unstitched`. No ellipsis joining non-adjacent fragments, no exceptions, no extension override. A specimen is the thing under examination and its surface is the evidence.

**Testimony and account quotation.** A quoted deposition, interview, memoir, letter, or log entry may be compressed, and each compression is marked at its site. State the count of elision sites when a single quoted passage carries more than one.

This is the scoping rule, and it is a scoping rule rather than an exemption. `unstitched` was written for specimens and continues to govern them without modification. Testimony is a different object and gets a stated discipline rather than an unstated one.

## Sidecar Field

Add one line to the sidecar when a reading makes claims above P0.

```text
Provenance: P0 [count] | P1 [count] | P2 [count] | P3 [count] | P4 [count] | P5 [count]
```

Add a second line when any P3 or P5 claim is load-bearing for the verdict.

```text
Load-bearing above P2: [claim] at [level], credential: [credential] or absence position: [position]
```

Omit both lines when every claim in the reading is P0. Do not pad the field to look rigorous.

## Interaction With Register Is Not Referent

`Register Is Not Referent` catches the move where a register's claim about its referent gets read as the referent. This extension supplies what happens next. A poem in a documentary register asserting a fact about a place makes a P2-shaped claim inside a P0 artifact, and the two must not be collapsed. The poem's assertion is on the page at P0. The fact asserted is at whatever level the record supports, which is often P4 and sometimes P5.

The productive case is P5. A poem whose speaker claims an experience that the record shows the poet could not have had is not a lie to be scored; it is an absence at a timestamp, and the reading names what the absence does.

## Failure Modes

### Grade Inflation

A P4 inference gets written in the syntax of a P2 attribution, usually by an impersonal construction: it is known, it is established, the record shows. Correction: name the party or drop to P4 and say so.

### Credential Padding

A P3 claim carries an adjective where a credential belongs. Senior, informed, well-placed, knowledgeable. Correction: state the access, or the claim is P4.

### Hedge as Reflex

A qualifier gets attached to a claim that carries no real doubt, so the reader cannot tell which hedges are load-bearing. Correction: the kernel's hedging carve-out applies. A hedge reports doubt or it comes out.

### Absence Fabricated

A P5 entry gets made from the apparatus's failure to look rather than from a gap in the record. Correction: state where the item should have appeared and what search established that it is not there. If neither can be stated, the claim is P4.

### Footnote Laundering

A claim is demoted to a note to avoid standing behind it, while still doing work in the reading. Correction: a note may hold a claim that is peripheral. A claim the verdict rests on stands in the body at its declared level.

### Field Padding

The sidecar provenance line gets filled out on readings where every claim is on the page, producing the appearance of rigor at the cost of the signal. Correction: omit the field. Its value is that it appears when standing is genuinely mixed.

## Provenance

Occasioned by five complete Seymour Hersh chapters read against the Harris corpus in September 2026. The practice is Hersh's; the ladder, the properties, and the scoping rule are the apparatus's. The extension is not a Hersh module and carries no voice zone. `5-hersh-voice-module` imports it and does not restate it.
