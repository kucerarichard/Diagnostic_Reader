# FRYE EXTRACTION

Version: 0.6
Source: Northrop Frye, *Anatomy of Criticism: Four Essays*, 1957.

Revision 0.6: gains a default load condition, following the kernel's widening of the specimen to any text at 0.3.17. On a specimen whose kind is not poem, this file loads by default and the radical of presentation is the first field filled, because a play and a label differ in channel before they differ anywhere else. Notes that a found text read as a poem has changed radical by construction. No change to the tools, the guards, or the refusal ledger.

A directive extension for the Portable Poetics Kernel v0.3. It carries three tools, one clarification, and one calibration note lifted from Frye, together with a ledger of what was examined and refused. It runs standalone and requires no private core.

## Module Manifest

Module name: Frye Extraction
Module type: directive extension
Kernel requirement: Portable Poetics Kernel v0.3
Private-core requirement: none
Source status: in copyright. This module paraphrases and names concepts. It does not reproduce Frye's prose.

Exports:

- triggers: none by keyword. Each tool fires on stated warrant during an existing reading
- procedures: radical-of-presentation test; paired fallacy guards; melos and opsis channel separation
- output fields: radical of presentation, and a changed-radical note when reception altered it
- constraints: no voice zone; no taxonomy import; no character-function vocabulary
- failure modes: taxonomy creep, relabelling, systematist drift

## Scope

This is not a voice module. It opens no voice zone, and nothing here may be rendered as Frye speaking. Attributing prose to Frye fails Checkpoint 7 as voice drift.

This is not a mode. It adds no operating mode and no output form of its own. The tools attach to sidecar fields and directives that already exist.

What it does: supply four pieces of machinery the apparatus was reaching for without a name, and record the reasoning for everything left behind.

## Tool 1: Radical of Presentation

Frye bases genre on the delivery channel rather than on form. Words may be acted before a spectator, recited to a listener, sung or chanted, or written for a reader. The genre follows from the conditions established between the poet and the public, which makes this a rhetorical distinction rather than a formal one.

Four channels, in Frye's terms:

| Channel | Frye's name | Condition |
|---|---|---|
| Acted before a spectator | drama | the audience is present and collective |
| Recited to a listener | epos | a reciter addresses a listening audience, in verse or prose |
| Sung, chanted, overheard | lyric | the poet turns away from the audience; the reader overhears |
| Written for a reader | fiction | the printed page reaches one reader at a time |

### The Invariance Rule

The rule that gives the tool its diagnostic force: incidental changes to how a text is delivered do not alter its radical. Printing a lyric does not make it fiction. Reading a novel aloud does not make it epos. Printed Shakespeare remains an acting script.

The apparatus gets a principled ground here for something it has been asserting from evidence alone. When reception delivers a work through a channel other than its own, the artifact in circulation is a rendering, and the original radical remains the artifact's.

### Prompts

> What radical of presentation does this poem assume?

> Has reception delivered it through a different one?

> If so, what did the change take away, and what did readers supply in its place?

### Where It Attaches

Rendering Conditions, as the first question rather than a supplement. L2 and L3 in Genopersistation, where a channel change is a reception event with a date and an agent. Frame, in Core Dimensions, which currently absorbs this work without naming it.

Emit a changed-radical note in the sidecar whenever the answer to the second prompt is yes.

Found text, from v0.6. Load this file by default when a specimen's kind is not poem, and fill the radical field first. A found text read as a poem has changed radical by construction: a label was written to be read at a glance on a shelf, a speech to be heard in a room, a report to be read once and discarded, and the specimen reading delivers each as writing for a reader who will dwell on it. Emit the changed-radical note on the usual terms, naming the original channel and the one the reading uses. The second-channel reading is the apparatus's and not the source's, and Period Fit marks it so.

### Worked Case

*Jubilate Agno* was composed as responsive reading, two alternating voices on separate sheets, which makes its radical epos and specifically antiphonal. The surviving manuscript carries only the `For` half through the Jeoffry stretch. The anthology delivers those lines to one silent reader, which is the radical of fiction.

Under the invariance rule the excerpt does not become a lyric by being printed as one. It remains half an antiphon delivered through the wrong channel, and the closure readers report at the final line is supplied by the channel change and the editorial cut rather than by the poem.

Before this tool, that finding rested on manuscript evidence and a reader-response citation. It now rests on a stated principle as well.

### Failure Mode

Do not use the radical as a second name for form. A poem in stanzas is not thereby lyric, and a long poem is not thereby epos. The question is who the words assume on the other end, not what shape they take on the page.

## Tool 2: Paired Fallacy Guards

Frye's recurring structural move is to name an error together with its mirror image, then show both rest on one bad assumption. The apparatus already thinks in this shape at the Coscienza forward and reverse axes and at the reverse-axis form of Register Is Not Referent. Three of Frye's pairs are not yet present.

### Pair 1: Merit and Reception

One error treats wide reception as evidence of quality. Its mirror treats obscurity or small reception as evidence of quality. Both assume a correlation between merit and public response, direct in the first case and inverse in the second, and Frye's position is that no correlation runs either way.

This one has asymmetric coverage in the current apparatus. Kowit's cult-mimicry diagnostic guards the inverse side well, catching obscurity that advertises itself as depth. Nothing guards the direct side.

The exposure sits inside the Kowit module. His aesthetic prizes accessibility, plain speech, and the poem available to a reader who did not go to graduate school, and the slide from accessible to therefore-good is exactly the direct-correlation error. A Kowit-voiced verdict that praises a poem for being reachable, without saying what the poem does, has made the mistake in the friendly direction.

> Does this reading treat reach as evidence of quality, in either direction?

The direct side now has a mechanism as well as a guard. See Tool 7 in `9-casanova-extraction`, which shows accessibility to be as position-relative as difficulty.

### Pair 2: Advance and Decadence

One error reads formal experiment as a general advance in technique, borrowing a progress model from science. Its mirror reads the same experiment as decline. Frye's correction is to treat such work as lateral exploration within one phase of rhetoric rather than as movement along a line.

This bears on period-fit at Checkpoint 2 and on Perloff-mode lineage claims, which run toward the advance side by construction.

> Is this reading placing the poem on a line of progress or decline that the evidence does not support?

### Pair 3: Wit and Incantation

Wordplay pulls two ways. Wit detaches the reader and addresses the waking intelligence. Incantation impresses without detaching. Frye locates a hazardous balance between them in paronomasia.

This gives a usable axis for the sound-versus-sense cut in Engine vs. Residue. A pun that detaches is doing argumentative work. A pun that hypnotizes is doing sonic work. Naming which one is running stops a reading from crediting a sound effect with a semantic finding.

Also a live check on Rother's pun-as-diagnosis rule, which licenses one pun where it compresses. The license holds for the detaching kind.

## Tool 3: Melos and Opsis

Frye splits the subconscious associative base of lyric into two channels and names them. Babble is sound-association, producing rhyme, assonance, alliteration, and pun. Doodle is its visual counterpart. The pair underwrites lyrical melos and opsis respectively.

### What This Gives the Nôm Battery

Test 3, Ink-Channel Linkage, requires that a candidate not be sound-carried. That requirement has been a rule of thumb without a statement of what it separates. Babble and doodle are that statement: melos is the sound channel and opsis is the ink channel, and Test 3 exists to find linkage that lives only in the second.

The Jeoffry margin scan is the clean case. Seventy-four line-initial instances of `For` make a solid visual column and are carried entirely in sound as anaphora. Babble, not doodle, so Test 3 correctly returns non-trigger.

### Constraint

This is a channel separator, not a new test. Do not add a battery test for doodle. The battery already has one and this names its axis.

### Secondary Observation

Frye notes that rhythm is usually prior to word selection, citing poets' revisions and Beethoven's notebooks, with children's rhythmic babble and nonsense-filled work songs as the popular case.

Useful in Interior Music Scan and in revision diagnostics, where a line that scans well and means little may be a rhythmic slot never filled rather than a failure of thought. That is a different diagnosis and a different repair.

## Clarification: Interest and Authority

Frye's axiom on a poet's commentary is that it carries peculiar interest but not peculiar authority, and that Dante annotating his own canto is one more of Dante's critics.

The apparatus needs half of this and must refuse the other half, and Coscienza and Intention Substitution currently blur the two.

**In-text declaration is evidence.** When a poem states its own procedure on the page, that statement is part of the text and is available like any other line. Smart's `For this he performs in ten degrees` is textual evidence of declared method, and it was load-bearing against the reading that files the structure as symptom.

**Out-of-text statement is testimony.** A poet's note, preface, interview, or workshop comment explaining intent has interest and no authority. It records what the poet meant to do, and the reading is of what the page does.

The line is where the words sit, not what they claim. Apply it in both directions: do not discount a declaration because it is authorial, and do not promote a note because it is authorial.

The same line extends to reception. An author's later acquiescence in a misreading of their own work is testimony too, and carries no authority over the reading. See the Ibsen case in `9-casanova-extraction`.

## Calibration Note: Displacement and Plausibility

Frye defines displacement as the adaptation of myth and metaphor to canons of morality or plausibility, and elsewhere treats a plausibility-principle as the censor against which creative impulse works.

Read alongside Anti-Laundering Engine Default and Engine vs. Residue, this describes the same operation from the composition side rather than the reception side. The mythic or ugly structure is the engine, and the plausible surface is what makes it admissible. Laundering at L3 does to a finished poem what displacement does during composition.

Held as a calibration note rather than a tool, because this rests on the glossary definition and one passage rather than on the argument that supports it. Promote it to a tool after reading the Third Essay's treatment, or drop it.

## Refusal Ledger

Recorded with reasons so that a later operator does not re-import this material on the strength of the book's reputation.

**The four mythoi.** Comedy, romance, tragedy, and irony keyed to spring, summer, autumn, and winter. Refused as an Automatic Position generator. Every poem can be assigned a season, so the assignment carries no information, and the output would sound systematic while diagnosing nothing.

**Character-function vocabulary.** Alazon, eiron, pharmakos, agon, anagnorisis, point of epiphany, architectus, buffoon. Refused on two grounds. These name roles in drama and narrative and have no purchase on a short poem with no characters, and importing them triggers Apparatus Bloom, which the kernel already names.

**The five fictional modes.** Mythic, romantic, high mimetic, low mimetic, ironic, ranked by the hero's power of action relative to the reader's. Tempting to bolt onto Stance and refused, because most lyric poems have no hero and no action, and the assignment would be a labelling exercise.

**The five phases of symbol.** Literal, descriptive, formal, archetypal, anagogic. Refused as a near miss. The literal and descriptive pair, Frye's centripetal and centrifugal meaning, overlaps the Depth dimension closely enough to be redundant, and the anagogic phase is out of scope for a mechanism-level apparatus.

**Evaluative bracketing.** Frye's discipline of holding value judgment outside criticism is not imported as a rule, because the apparatus renders verdicts by design. Retained instead as a standing check: a verdict that reports a reputation rather than a mechanism has become the stock exchange Frye was arguing against.

## Triangulation Note

Frye holds, following a remark of Mill's, that the artist is overheard rather than heard, and that a poem addressing its reader directly falls to the level of metrical talk.

Kowit's project is direct address in plain speech to a reader assumed to be present.

This disagreement is real and should be held open rather than resolved. It belongs in Triangulated Commentary as an axis whenever a specimen turns on address.

### No Frye Voice Module

Decided rather than deferred. This extraction stands in permanently for the whole-system view and no Frye voice module will be built.

His method is defined by claiming synoptic jurisdiction, which is the argument of his Polemical Introduction. A Frye module with honest non-activation conditions would be a Frye who had abandoned his central claim, and one without them would take over every reading it touched. The extraction carries the tools without the jurisdiction claim, which is the trade.

The secondary reason is the shape of the grid. Four mythoi at six phases each is twenty-four cells, and every poem lands in one, which is a flattening rather than a reading.

The general test, the slot matrix, the candidate log, and the reopen conditions live in `0b-voice-slot-registry`. They are apparatus-level and were held here only because this was the first case.

### Known Cost

On an address specimen Kowit renders in the first person while the Frye position appears as a note in the default register. State the imbalance whenever the axis comes up.

This is the live instance of a standing cost that applies to every extraction. The general form is at The Extraction Asymmetry in `0b-voice-slot-registry`.

## Corroboration Log

Frye reads *Jubilate Agno* in the lyric section of the Fourth Essay. He quotes the animal-in-language passage on the power of the cat in Greek and the mouse in Latin, frames it as babble that has not risen into consciousness, notes that parts of the poem are usually considered mentally unbalanced, and uses it to show the creative process at a formative stage.

This is the reverse-axis Coscienza error the Smart scan predicted as the standing reading, appearing in the most influential work of mid-century Anglophone criticism, published in 1957, three years after Bond's edition established the antiphonal design, with no mention of the antiphon.

Two findings follow. The Selective Salvage result strengthens, because the misreading survives a careful reader rather than depending on a careless one. And the keep-list and drop-list repeat at a smaller scale: Frye keeps the paronomasia as raw material and drops the design.

Log entry, not a directive. It records that a prediction held.

## Failure Modes

### Taxonomy Creep

The refused material re-enters through a side door, usually as a single term that seems harmless.

Correction: check the Refusal Ledger before naming any Frye category the tools above do not carry.

### Relabelling

A tool is used to rename a finding the apparatus already had rather than to produce a new one. A radical-of-presentation field that always answers lyric is doing this.

Correction: a tool that has not changed a reading in several specimens is not firing on warrant.

### Systematist Drift

The reading starts placing the poem in literary history rather than diagnosing it, because the source book is organized that way.

Correction: return to Function Before Parts. Frye's Smart reading is what the system view produces without the mechanism check.

## Access Honesty

This extraction rests on roughly six thousand words of a hundred and fifty-eight thousand.

Read closely: the glossary, the opening of the Polemical Introduction, the radical-of-presentation passages in the Fourth Essay, and the babble and doodle passage with its Smart example.

Not read: the First, Second, and Third Essays in substance, the specific-forms sections of the Fourth Essay, the rhetoric of non-literary prose, and the Tentative Conclusion.

The refusals above rest on the table of contents, the glossary, the index, and general familiarity rather than on reading those essays. They are provisional in a way the three tools are not. A later operator who reads the Third Essay may find something the ledger dismisses too fast, and the ledger should be amended rather than defended.

Provenance: v0.4 was briefly reconstructed from a conversation record after the working copy was lost, then rebased on the authentic v0.3 and verified by diff. The source-derived content is unchanged from the versions written against the book. At v0.5 the slot matrix, candidate log, and reopen conditions moved to `0b-voice-slot-registry`; nothing Frye-derived was altered.

## Activation Notice

When this module is loaded and a tool changes output:

```text
Frye Extraction: [tool name] applied.
```

Omit the notice when the module changes nothing.
