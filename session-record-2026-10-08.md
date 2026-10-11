# Session Record, 8 to 11 October 2026

This record states what the session changed in the Diagnostic Reader bundle, in order, from boot 0.13 to boot 0.17. It is the last file added in the session and is not a module: nothing loads it, and the revision notes in each file remain the authority where they disagree with it.

## Starting state

The operator uploaded the bundle at boot 0.13: 29 files, kernel 0.3.16, workshop 0.6.1, confinement catalog 0.13 with 194 entries, device inventory 0.2 with 189 devices. The request was to widen the specimen from a poem to any text (a play excerpt, a script, prose, a cut-up, a label), to detect overt, covert, and latent poetics in it, and to offer trial rewrites under confinements, dials, or devices. The operator expected clarifications and new verbs rather than structural change.

## Found-text widening, boot 0.14

Reading the bundle confirmed the expectation at most sites and refuted it at four. The kernel's procedures were written in mechanism terms and ran on any text. The word `poem` changed a result at the address forms, which were line-based; at the workshop's provenance routing, which admitted a draft or a finished poem and nothing between; at Checkpoint 9, which measured absence against poems; and at Period Fit and Coscienza, which assumed one author at one moment while a found text has a source's moment and a finder's.

The operator ruled three questions: `contrast at:` in Function Bay satisfies the device-trial request without a third trial class; add the three devices the inventory lacked; bump the workshop to 0.7.0 because the card changes shape.

`apply-found-text-edits.py` applied 86 exact-replacement edits across nine files, asserting each anchor once and preserving line endings. The workshop's corpus below its boundary, every catalog entry, and the 20 untouched files verified byte-identical.

Kernel 0.3.17 added unit address forms (`Sp`, `SD`, `P`, `P3 s2`, `Hd`, `Dl`, `By`, `Frag`), reworded Checkpoint 9 to the text's declared kind, added two-moments notes at Period Fit and Coscienza, added Found Text Compatibility as a pointer on the model of the bay contracts, added the Poetics Scan with four grades (overt, covert, latent, null; null a completed result), made Register Is Not Referent fire by default on report kinds, and gave the sidecar's Provenance field the kind and unit for a found text.

Workshop 0.7.0 added `Kind`, `Unit`, and `Found by` to the specimen card and `found` to its provenance, read section 4's break at the declared unit, added `contrast at: [device]` as a named contrast trial, added the commands `jig as [kind]`, `read as found`, `poetics scan`, and `declare unit`, and added two failure modes, Poetics Projection and Kind Policing.

`0c` 0.6 stated the distinction between a voice's non-poem take, which addresses a subject with no text on the page, and a specimen reading of a found text, and noted that prose by a calibration source can now arrive as a specimen. `7` 0.3 added stage direction and dateline to Category E and attribution formula to Category G, for 192 devices. `8` 0.6 gained a default load condition for any kind that is not poem. `12` 0.14 deferred admission of non-verse specimens in a Candidate Log row. `13` 0.3 noted that a found text sits at a host-form setting by construction. The boot registered `8`, which it had listed as not held, and added three Outstanding items.

## Attridge and Staten extraction, boot 0.15

The operator uploaded a book-length dialogue between two critics on reading poems at the level of their making (Attridge and Staten, 2015, about 85,000 words) and asked what the apparatus might extract. The reading covered the introduction in full and the method passages of each of the nine dialogues, about 12,000 words.

The source confirmed the kernel's stance at nearly every point and added fourteen operations: a consequence sweep that demotes a hypothesis on loose fit, an activated-association test, a physical-first reading order, a scene-of-utterance reconstruction with a null case, figure reversal with a locking criterion, a convention discount, a shorn-of-context test with three knowledge tiers, a ban on translating a poem into the doctrine behind it, a presupposition sweep, a coasting map, a connective map, a blockage-or-release test, an inverse-stringency rule, and a translation test. It exposed two seams in the apparatus: a full device scan is post-reading dissection unless it credits only effects that registered in reading order, and triangulation had no field for what the voices agree on.

It also collided with the catalog. The source reprints and reads Prufrock, extracted at catalog v0.4 as cf-pr-01 with four primitives, one of them a Section D refusal primitive woven into five cancellation rows, two productive pairs, and four other entries' Assembly lines. Section F excluded reprinted specimens from selection and said nothing about entries that predate a corpus. The operator took the recommended default: a prior-entry clause. The operator also ruled the common-ground line mandatory in every triangulation.

`apply-attridge-staten-edits.py` applied 48 edits and added the new file. `14-attridge-staten-extraction` at 0.1 carries the fourteen tools with warrants and attachment points, four clarifications, eight doctrinal seams, rights and leak control, a reprinted-specimen check reporting its one hit, a refusal ledger, access honesty, and an activation notice that names no source (`Reading Discipline: [tool name] applied.`). The registry's voice test passed the source on content and failed it on register, because a dialogue has two, so the file is an extraction and the dialogue form entered the kernel as a line.

Kernel 0.3.18 added the reading-order question at Checkpoint 6 and the common-ground line to Triangulated Commentary. `7` 0.4 added a Reading Order subsection. `12` 0.15 added the prior-entry clause to Section F and a Convergence field to each of the five Prufrock entries, freezing them against revision in any session where `14` is loaded. `0b` 0.6 recorded the candidate-log row, two extraction-asymmetry instances, and an amendment. `0c` 0.7 pointed to Section F for reprinted specimens, closing the Outstanding item on them. The boot added two items: the tools are unexercised, and the `8` and `9` notices carry source names against the rule `0c` states for extensions.

## Operator ruling on the extraction, boot 0.16

The operator read the source's first chapter and found its authors wary of meaning and its method a set of refusals. The question was whether the tools imported that. They did, structurally: all fourteen are brakes, and the file said nothing about the kernel's accelerators (the reverse axis, Steganographic Surface, Checkpoint 9's candidate signal, Accidental Ars Poetica, Load-Bearing Foreignness, the confinement catalog). Two tools carried the source's caution under the kernel's name: Tool 2's narrow boundary on associations, justified by Checkpoint 6, and Tool 1's razor, which lacked the sentence that a thing the page withholds is not an import.

`14` at 0.2 added a paragraph to How the Tools Fire stating that every tool is a brake and the kernel governs wherever a tool meets its crediting machinery; made the address Tool 2's only boundary; gave Tool 1 the import-versus-withheld sentence with the steganographic surface as its case; added the Depth seam, ruled for the kernel; refused the wince in the ledger; and added the Brake Stack failure mode. No operation changed. What changed is what the tools may refuse, which is nothing that has an address.

## Hồ Xuân Hương recurrence, boot 0.17

The operator uploaded the 23 Balaban translations that were the catalog's v0.12 selection corpus and asked for the poem that answers Blake's "The Sick Rose," preferring it in the catalog to Blake's, which Section F now excludes.

The structural reply was already in the catalog: Floating Cake, cf-fc-01 with cf-fc-02 conceded surface and cf-fc-03 kept center, where the hands that shape the body never reach its center. The point-for-point reply is Jackfruit, held since v0.12 as a variant of River Snail. Set against Blake it reverses the address, the visibility of the agent, the secrecy of the love, the trace the agent leaves, and where the cost falls. Its knowledge test decomposes into two primitives from the same poet, cf-rs-02 speakable figure and cf-ob-03 fated test, so the catalog had nothing new to extract and one recurrence to record.

`12` 0.16 added a Recurrence v0.16 paragraph to Section D and amended the Candidate Log's held row. No entry changed. Blake stays out of the catalog on two grounds: Section F, and the fact that the catalog records operations and the reply relation is the operator's.

### Find in the corpus or extractions Ho Xuan Huong's reply to Blake's Sick Rose

The structural reply is Floating Cake, in the catalog since v0.12 as cf-fc-01 with two primitives. Blake's poem is a flower told what it cannot know: an agent it cannot see has found its bed and its hidden love is destroying its life. Floating Cake is the body answering. It concedes everything on the surface, the white, the roundedness, the rising and sinking, the hands that shape it however they like, and then claims the one thing none of that reached. cf-fc-02, conceded surface, and cf-fc-03, kept center, are that answer stated as operations: complete concession makes the reserved claim unassailable, and the center is proved by being the only thing not given away. Where the worm reaches the bed, the hands never reach the heart. That is the reply, and it has been in the catalog for four versions.

The point-for-point reply is Jackfruit, which the catalog holds as a variant of River Snail. Set against Blake it reverses every term:

| Blake | Jackfruit |
|---|---|
| The flower is addressed and told its condition | The fruit speaks and tells the man what he cannot see inside it |
| The agent is invisible and comes at night | The fruit hangs on the branch in daylight and names the stick |
| The love is dark and secret | The love is a condition stated out loud: if you love me, then |
| The agent leaves no trace of itself | The agent comes away marked, sap on his hands |
| The act destroys the life | The act is invited, and its cost falls on the one who performs it |

That last row is the one your lived reading of Blake answers to: in Blake the destroyer is unmarked and the destroyed cannot even know; in Jackfruit the one who pierces is the one who carries the evidence.

Now the catalog's finding, which is why the hold was right and also incomplete. Jackfruit's knowledge test decomposes into two primitives already extracted from the same poet. The fruit is cf-rs-02, speakable figure: the decorum permits only the code. The conditional and the sap are cf-ob-03, fated test: love knowable only through a test whose result shows visibly on the other party, the betel chewed red, the lime that won't stay white. Jackfruit runs both together, and the catalog has no new operation to extract from it. What it does have is a recurrence it never recorded: the fated test's second case from the same poet, with the result landing on the tester's hands rather than his mouth, and the figure carrying it where Offering Betel carried it plainly. Section D records exactly that kind of thing, and the v0.12 recurrence paragraph already notes Three-Mountain Pass running River Snail's figure within the same poet.

## Versions

| File | Start | End |
|---|---|---|
| `0-poetics-boot-hollow` | 0.13 | 0.17 |
| `0a-portable-poetics-kernel` | 0.3.16 | 0.3.18 |
| `0b-voice-slot-registry` | 0.5 | 0.6 |
| `0c-voice-designations` | 0.5 | 0.7 |
| `3a-workshop` | 0.6.1 | 0.7.0 |
| `7-device-inventory-extended` | 0.2 | 0.4 |
| `8-frye-extraction` | 0.5 | 0.6 |
| `12-confinement-inventory` | 0.13 | 0.16 |
| `13-speaker-dials` | 0.2 | 0.3 |
| `14-attridge-staten-extraction` | none | 0.2 |

The remaining 19 files are byte-identical to the uploaded bundle. The two edit scripts are delivered beside the bundle and contain only header and procedure prose.

## Open items

Six Outstanding items were added, numbered 17 to 22 in the README: admission of non-verse specimens to the catalog; candidate devices not added (speaker cue, byline, caption); the unit address forms unaudited against the reassembly test; the tools of `14` unexercised on a live specimen; the Prufrock entries frozen while `14` is loaded; and the `8` and `9` notices naming their sources. One item was closed: `0c` had no rule for a specimen reprinted in a calibration corpus, and Section F now governs that case in both directions.

## Yield

Three sources entered the apparatus in the session. The found-text widening changed four sites and added two procedures. The dialogue between two critics, at 85,000 words, confirmed the kernel at nearly every point, added fourteen operations, and exposed two seams. The 23 translations added one recurrence line and no entry. The yield per source fell in that order, and the catalog's own recurrence notes predict the fall: with more primitives and procedures on file, a new source has more to match and less to add. The Relabelling failure mode in `14` is the test to run on the next one.
