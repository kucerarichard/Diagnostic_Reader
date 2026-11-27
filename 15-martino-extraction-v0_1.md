# MARTINO EXTRACTION

Version: 0.1
Source: Pat Martino, *Here and Now! The Autobiography of Pat Martino*, with Bill Milkowski, 2011; and Martino's filmed demonstration "The Nature of the Guitar," transcript in the operator's hands.

A directive extension for the Portable Poetics Kernel v0.3. It carries seven tools taken from a jazz guitarist's account of how he rebuilt music after a brain aneurysm left him amnesic, and of the symmetrical system he built in place of the memory he had lost. It runs standalone and requires no private core.

The source is not a critic and never wrote about poetry. What it supplies is an unusually explicit account of a competence rebuilt from the outside, by a player who could no longer draw on the ear he had, and who therefore had to state in procedure what players normally leave tacit. That is the condition of a reader with a trained ear in one art and none in another, and the operations transfer because they were built for exactly that passage.

One operation here is literal and runnable. The rest are structural, and the file says which is which.

## Module Manifest

Module name: Martino Extraction

Module type: directive extension, a source extraction on the model of `8-frye-extraction`, `9-casanova-extraction`, and `14-attridge-staten-extraction`

Calibration source: the autobiography and the filmed demonstration named above. Recorded here because a source policy that cannot name what it governs cannot govern it. This line is header prose and does not reach output.

Kernel requirement: Portable Poetics Kernel v0.3

Private-core requirement: none

Consumer: any reading. Tool 1 also runs outside a reading, as an exercise.

Source status: the autobiography is in copyright; the filmed demonstration is the source's own speech, transcribed. This module paraphrases operations and names tools. It reproduces no passage of either.

Exports:

- triggers: none by keyword. Each tool fires on stated warrant
- procedures: the seven tools below
- output fields: none of its own. Tools write into the Mixed Log, Core Dimensions, Architecture, Pressure Points, and Fracture Surface
- constraints: no voice zone; no mode; no designation
- failure modes: numerology, the wrong automatic imported twice, transcription as analysis, symmetry hunger

Imports from kernel:

- Mechanism Before Vibe
- Engine vs. Residue
- Core Dimensions, Lattice and Pressure in particular
- Mixed Log and the Closure Rule
- Checkpoint 6, Decoration vs. Diagnosis
- Checkpoint 9, Weak Signal and Absence
- Rendering Conditions
- Found Text Compatibility and the Poetics Scan
- Access Honesty
- Source Policy and the Reassembly Test

Imports from extensions:

- Extended Device Inventory, Category B for the prosodic devices Tool 2 declines to use as a starting point, and Category E for structural repetition under Tool 3

Failure condition: without the kernel the tools have no Mixed Log to write into and no decoration rule to cut against, and Tool 1 degenerates into a party trick. The file is not standalone.

## Scope

This is not a voice module. It opens no voice zone and takes no designation. The source is a musician, not a critic, and nothing here may be rendered as him speaking. An extension ships no labelled output of its own; its operations appear inside the treatment of whatever consumes them.

This is not a mode. It adds no output form.

This is not a theory of sound in poetry. English spelling is not a phonetic transcription, and Tool 1 operates on letters. The file says so where it matters and does not pretend otherwise.

What it does: supply a reader who can hear music, and cannot yet hear verse, with operations that run on structure rather than on ear, and that produce something an ear already trained elsewhere can take hold of.

## How the Tools Fire

No keyword. Each tool names its warrant. Tool 1 is an exercise and fires on request. Tools 2 through 7 fire during a reading when the page gives them something to work on.

The source's governing idea is the distinction between what an instrument makes **automatic** and what a pedagogy **imposes**. On a piano the C major scale is automatic: it is the white keys, and the hand finds it without being taught. On a guitar it is not automatic, and the source observes that guitar teaching has historically taught the piano's automatic anyway, by way of scales and root-third-fifth construction. What is automatic on a guitar is something else entirely: a fingering shape that holds its identity as it moves, so that the same grip at one position and another position is the same chord, rearranged.

The whole file follows from that. A competence can fail not because the faculty is absent but because the wrong automatic was installed. The operations below look for what a poem makes automatic, and decline the system that was imposed on it.

## Looking Around

One tool here runs as a program. `tools/martino-transcribe.py` is standard library only and consults no model.

```
python tools/martino-transcribe.py COLTRANE TENOR --compact      the source's own worked words
python tools/martino-transcribe.py beautiful ugly --compact      the two he plays on film
python tools/martino-transcribe.py "Dare frame thy fearful symmetry"
python tools/martino-transcribe.py --file regression/tests/R1/specimen.txt --max-lines 4
python tools/martino-transcribe.py --help
```

The long form prints the notes, the scale degrees against A minor, a contour of rises and falls, the span, the landing note, and a seven-line plot. `--compact` prints the notes alone, one line per input, which is the form to use on a whole poem.

Load the file into a reading with either name:

```
python -m dr explain read --extensions 15
python -m dr explain read --extensions martino
python -m dr explain read --extensions martino attridge-staten --voices ASSAY
```

It is a step 4 extension of 26 KB, so it costs about 6,600 tokens on top of whatever the task already loads.

The rest of the tools are read and applied by hand. Tool 2 is a question about the reader rather than the poem and runs once, not per specimen. Tools 3 and 4 run on any poem with a repeating shape. Tool 5 runs at the Mixed Log. Tools 6 and 7 are checks on the reading rather than operations on the page.

## Tool 1: Letter-Scale Transcription

The source maps the twenty-six letters onto the seven natural notes, cycling. A to G, then H begins again at A, and so on; twenty-six letters make three full passes of seven with five left over, and he says so in those words. A word then has a pitch sequence, and he composed from it: the title piece of one record was derived by running two words through the mapping and taking the result as a line.

Prompt:

> Run this line through the mapping and play what comes out. Where does the contour it gives you agree with the line's actual movement, and where do they pull apart?

### Operation

Assign each letter its note by position in the alphabet, modulo seven, against the natural notes of A minor or C major. Transcribe a word, a line, a title, or a name. Play or hear the result.

Two things can then be read. The **contour** is where the sequence rises, falls, repeats, and leaps. The **landing** is the note the sequence ends on and what that note is in the key.

The tool produces material. It does not produce a finding. A finding arrives only when the generated contour is set against something the poem independently does, and the two are compared at an address.

### Where It Attaches

Architecture, as a second structure laid over the first. Lattice in the Core Dimensions, where a poem's repeating substructure is already the subject.

### Warrant

The source states the method twice, once in the autobiography with the worked example of a composition built from two words, and once on film with the words *beautiful* and *ugly* played as melodies and the remark that the resolution of either is his decision.

### What It Can and Cannot Show

It cannot show how a line sounds. The mapping reads spelling, and English spelling is not sound: the same letter takes different values in different words, and the mapping is blind to every one of them. A reader who treats the output as the line's music has learned nothing about the line.

What it can do is give a reader with an ear a second object to hear, derived from the text by a rule, which is orthogonal to the meaning and indifferent to taste. That is its whole use, and it is not a small one for a reader whose ear works and has nothing to grip. The source's own case is the argument: the mapping is arbitrary, he knew it was arbitrary, and he got a composition out of it because the arbitrariness was the point. A system that does not already know what it wants to find will hand you something you did not intend, and noticing what you did not intend is the beginning of attention.

Hold the output at the Mixed Log as material, never as evidence. A contour that agrees with the line's movement is a coincidence until the line's movement has been established on its own grounds.

### Worked Case: What the Landing Note Finds in The Tyger

`tools/martino-transcribe.py` runs the mapping. Taking the landing note of each of the twenty-four lines of Blake's *The Tyger* and pairing them by couplet:

```
bright       F   night        F   match
eye          E   symmetry     D   <<< does not match
skies        E   eyes         E   match
aspire       E   fire         E   match
art          F   heart        F   match
beat         F   feet         F   match
chain        G   brain        G   match
grasp        B   clasp        B   match
spears       E   tears        E   match
see          E   thee         E   match
bright       F   night        F   match
eye          E   symmetry     D   <<< does not match

12 couplets, 2 non-matching
```

Twelve couplets, two mismatches, and both are the same pair. `eye` against `symmetry` is the one rhyme in the poem that is not a rhyme, the one every commentator stops at, and it sits in the frame stanza that opens and closes the poem. The tool located it knowing nothing about poetry, rhyme, or Blake.

Then the mechanism, which matters more than the result. The landing note is the note of the line's last letter, so matching landings mean the lines end in the same letter. The tool is a detector for spelling. In *The Tyger* that happens to track the rhyme scheme almost perfectly, because Blake's rhymes here are spelled alike, so the one pair that is not spelled alike is the one that stands out.

On another poem it will mislead, in both directions:

```
rhymes to the ear, flagged anyway:   though/snow  A B      love/of   E F
                                     sea/key      A D      gone/upon E G
spelled alike, not a rhyme, missed:  love/move    E E      cough/though  A A
                                     daughter/laughter  D D
```

So the landing note is not a rhyme test and must never be reported as one. What it is, on a poem whose orthography is regular, is a mechanical index of line endings that a reader can scan in a column without hearing anything. That is worth having when the ear is the faculty in question, and it is worth distrusting the moment the poem's spelling stops being regular.

This is the whole tool in one case: it hands you something you did not intend, and the finding arrives only when you check it against what the poem does on its own grounds.

### Failure Mode

Numerology. The mapping will always produce something, on any text, including a shopping list, and a reader determined to find significance will find it. The guard is the kernel's decoration rule: an output that does nothing in the reading is decoration, however pretty the shape.

A second and more specific trap, from the worked case: reporting a landing-note mismatch as a rhyme finding. It is a spelling finding, and the two coincide only where the poem's orthography is regular.

## Tool 2: The Wrong Automatic

The source's central observation, applied to the reader rather than the poem.

Prompt:

> Is this reader's difficulty with the poem a missing faculty, or a system installed from a neighbouring art that this one does not run on?

### Operation

When a reader reports no ear for verse, do not begin with scansion. Establish first what the reader can already hear elsewhere, and in what terms, then ask whether the system they were taught for verse is native to verse or borrowed.

Metrical feet are the borrowed system in English. They are a Greek and Latin quantitative apparatus fitted to a stress-timed Germanic language, and they are taught first because they are teachable, not because they are what the language makes automatic. A reader who cannot hear iambs may have an ear in perfect order that has been handed the piano's fingering for a guitar.

What English makes automatic is different, and a reader can be pointed at it directly: the phrase rather than the foot, the stretch of syllables a speaker would say in one breath without a decision, and the places where the line's break and the phrase's end either coincide or do not. That is available to anyone who can hear speech, which is everyone.

### Where It Attaches

Rendering Conditions, which already holds that a page's hostility can be mistaken for a poem's difficulty. This tool extends it one step: a reader's training can be mistaken for a reader's capacity.

### Warrant

The source names the pattern exactly, in the way guitar teachers normally teach, and says what he did instead. The transfer is not an analogy. It is the same error in a different art.

### Failure Mode

The wrong automatic imported twice. Replacing scansion with this file's own apparatus, and insisting the reader hear a poem through the letter-scale mapping, repeats the error with a new system. Tool 1 is an exercise, not a prosody.

## Tool 3: Parental Form

The source's two parental forms are the augmented triad and the diminished seventh. Each divides the octave into equal parts, so each keeps its identity when moved: shift the augmented shape by a major third and the notes are the same notes, rearranged. From one such shape, lowering any single tone yields a major chord and raising any single tone yields its relative minor, so one grip holds three majors and three minors.

Prompt:

> Which shape does this poem repeat without altering, and where is the single element that was moved?

### Operation

Find the poem's invariant: a stanza form, a syntactic frame, a refrain, a sentence shape that recurs. Establish that it is genuinely the same shape and not merely a similar one. Then locate every point where one element inside it has been changed and the rest held.

A single altered element inside a held frame is the poem's cheapest and most forceful move, and it is usually load-bearing. Report what the alteration converts the shape into, and what the shape would have stayed if it had not been made.

### Where It Attaches

Lattice, for the invariant. Pressure Points, for the altered element. Fracture Surface, where the alteration is a turn. Category E in the Extended Device Inventory for the structural names.

### Warrant

Blake's *The Tyger* opens and closes on the same four lines, and one word is different: `Could frame thy fearful symmetry` becomes `Dare frame thy fearful symmetry`. The frame is held exactly; one tone is moved; the quality of the whole changes from a question about capacity to a question about nerve. The poem's own last word in that line is *symmetry*, which is the property the operation depends on.

### Failure Mode

Symmetry hunger. Not every repetition is a parental form, and a reader who has just learned the move will find invariants in texts that have none. The test is whether the shape is genuinely identical in its recurrences; a shape that is merely similar is a resemblance, and the altered element in it is not doing the work this tool credits.

## Tool 4: Horizontal and Vertical

The source demonstrates one shape holding its identity along two axes of the fretboard, across the strings and along the neck, and calls the study of the two a study of opposites.

Prompt:

> Does this poem's recurring shape move along the line, down the stanza, or both, and does it keep its identity on each axis?

### Operation

Having found an invariant under Tool 3, test it on both axes. The horizontal axis is within the line: a figure, a rhythm, or a syntactic shape recurring across a single line's length. The vertical axis is down the poem: the same shape recurring at the same position in successive stanzas.

A shape that holds on both axes is structural. A shape that holds on one and not the other is a local device, and saying which axis it holds on is more informative than naming it.

### Where It Attaches

Architecture. Lattice.

### Warrant

The source shows the identical grip at three positions vertically and four horizontally and arrives at twelve, which is the same twelve he reaches by adding seven white keys and five black. Two routes to the same number is his demonstration that the system is a system and not a coincidence.

### Failure Mode

Treating the axes as equally weighted in every poem. Most poems in English are organized vertically, by line and stanza, and a horizontal invariant is the rarer and usually the more deliberate finding.

## Tool 5: Resolution Is the Reader's Decision

Playing the words *beautiful* and *ugly* as melodies, the source observes that neither resolves on its own and says that resolution is his decision.

Prompt:

> What has this poem left unresolved, and what is the reader supplying when it feels closed?

### Operation

Separate what the poem settles from what the reader settles on the poem's behalf. For each closure in the reading, ask whether the text performs it or the reader performs it in order to be finished.

A text may decline to resolve and be complete. The reader's act of resolution is a real act and may be the right one, but it belongs to the reader and is recorded as such.

### Where It Attaches

The Mixed Log and the Closure Rule directly. The kernel already distinguishes a hypothesis closed by evidence from one closed by a rival; this tool adds the one closed by the reader's need for an ending, which is not a closure and is logged as live.

### Warrant

The source's remark is offered about two words with no musical context at all, which is the strongest form of the point: with nothing around them, neither word's melody is finished, and finishing it is an act performed by someone.

### Failure Mode

Using the tool to refuse every closure. A poem that does resolve has resolved, and declining to say so is not rigor.

## Tool 6: Opposites With a Third Point

The source studies pairs, vertical and horizontal, beautiful and ugly, consonance and dissonance, and places objectivity at a third point outside the pair. He declines to eliminate either side and says that wanting to be rid of the bad is like wanting to be rid of the night.

Prompt:

> What pair is this reading running on, and is the reading standing at one end of it or outside it?

### Operation

Name the opposition the reading has adopted. Check whether the reading occupies one pole, which makes it an advocate, or the third point, which makes it a diagnosis.

The third point is not a midpoint and not a refusal to judge. It is the position from which both poles are visible as a pair.

### Where It Attaches

The kernel's Diagnostic Stance, which this tool restates from outside the apparatus and therefore confirms rather than extends. Checkpoint 6, since a reading that has taken a pole usually decorates.

### Warrant

The source arrived at the position through illness and names what it cost him to reach it. That is biography and stays in this header; the operation is what crosses into output.

### Failure Mode

Treating the third point as neutrality. A diagnosis that declines to find anything has not reached the third point; it has left the triangle.

## Tool 7: All Things Sing

Describing a period of depression, the source lists what began to carry music for him: the alphabet, words, the names of streets, licence plates, envelopes with addresses, the names of people. His conclusion is that music came from all things and not only from the craft.

Prompt:

> Does this text's kind exclude it from the apparatus, or only from the apparatus's habits?

### Operation

Apply the kernel's Found Text Compatibility without reservation. A street name, a label, a registration, an address, or a list is a specimen with a kind and a unit, and the full procedure runs on it.

The tool exists because the exclusion is rarely stated and usually just practised. A reader who would not think to read a licence plate is applying a rule nobody wrote down.

### Where It Attaches

Found Text Compatibility and the Poetics Scan, which grade a found text rather than admitting it on faith. The Scan is the guard: this tool widens what may be brought, and the Scan decides what stands up.

### Warrant

The source's list is specific and was produced under conditions where the craft had stopped being available to him. That is the case that matters: the claim is not that everything is art, but that the apparatus for hearing does not stop at the edge of the art.

### Failure Mode

Admission without grading. The kernel already refuses this, and the tool inherits the refusal.

## Doctrinal Seams

**Letters against sound.** Tool 1 maps spelling. A poem works in sound. These are not the same object, and the apparatus's own device inventory holds a whole Category of prosodic devices that operate on sound and that Tool 1 cannot see. The seam is left open rather than patched. A phoneme mapping could be built and would be closer to what a poem does, but it would not be this source's method, and the file extracts what the source has rather than what it might have had. An operator who builds the phoneme version should register it separately.

**The source is not a critic.** Every other extraction in this bundle takes a critic who argued about poems. This one takes a musician who never did. The operations therefore arrive without any prior application to verse, and each is credited here on an argument rather than on a demonstrated reading. Tool 3 is the only one with a worked case on a poem, and that case is the apparatus's, not the source's.

**Symmetry as method and symmetry as subject.** The source's systems are symmetrical because his instrument is, and the guitar's symmetry is a fact about how it is tuned and fretted. A poem has no comparable fixed geometry, so the symmetries Tool 3 and Tool 4 look for are made rather than given. The tools hold because a made symmetry is still a symmetry, but the analogy does not license treating a poem as an instrument with discoverable invariants waiting in it.

**Rebuilding without consulting the original.** Asked whether he studied his own earlier recordings when returning to the instrument, the source said he stayed well away from himself, and that this was the point. The remark bears on a reader trying to recover a competence they believe they ought to have. The file states it here and builds no tool on it, because an instruction to avoid one's own past is a disposition and not an operation.

## Rights and Leak Control

The autobiography is in copyright and the filmed demonstration is the source's recorded speech. No passage of either is reproduced here. Tool names and operations are the apparatus's own wording.

The source's name appears in this header, as the designation layer permits for apparatus-internal prose, and does not appear in generated output. The biographical material in the warrants is Tier C under the leak tiers and stays in the header; a reading that anchors on a guitarist's aneurysm has leaked a life the apparatus did not live.

## Calibration Collision

Where a specimen's author is this source, every operation in this file stands down, and the jurisdiction note states no cause. The condition is remote and is recorded for completeness.

## No Voice Module

No voice is declared from this source and none should be. He is not a critic, he made no readings, and a slot built on him would have no corpus of judgments to calibrate against. The material is procedural and belongs in a directive extension, which is where it is.

## Failure Modes

### Numerology

Tool 1 produces output on any input. The decoration rule is the guard, and it is the one most likely to be needed.

### The Wrong Automatic Imported Twice

Tool 2 diagnoses a borrowed system and this file is another system. Offering it as the replacement prosody repeats the error it names.

### Transcription as Analysis

A reader who runs Tool 1 and stops has a melody and no reading. The tool is a generator and the file says so in three places because the temptation is strong.

### Symmetry Hunger

Tools 3 and 4 reward finding invariants, and a reader will find them where there are none. The identity test is the guard.

## Access Honesty

The filmed demonstration is a performance with musical examples, and the transcript the operator holds carries the speech without the playing. Every musical claim in this file therefore rests on the words rather than on the sounds they describe, and the arithmetic has been checked but the demonstrations have not been heard. An operator who hears them may find an operation here that the words alone did not support.

## Activation Notice

This file supplies operations and no voice. Its tools appear inside the labelled treatment of whatever consumes them and carry no label of their own. Nothing in this header reaches output.

## Provenance

Extracted from the two sources named at the head of this file by an operator reading for what transfers to the reading of poems, on the occasion of a reader with a trained musical ear and no ear for verse asking whether the one could be made to serve the other.

Tool 3's worked case on *The Tyger* is the apparatus's own and was checked against the specimen pinned in `regression/tests/R1/specimen.txt`. Tool 1's arithmetic was checked against the source's stated figures: twenty-six letters as three sets of seven and one of five, and his two worked words.

Outstanding: no tool in this file has been exercised on a live specimen inside a full reading. Tool 1's usefulness to a reader is argued and not demonstrated. The phoneme mapping named in the first doctrinal seam is unbuilt.
