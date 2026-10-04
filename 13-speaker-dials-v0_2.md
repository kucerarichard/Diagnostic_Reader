# SPEAKER DIALS

Version: 0.2

Revision 0.2: applies the operator's ruling on the doctrinal seams. Where this file's calibration source and the workshop's disagree, the workshop's position governs, and dials are probes for what a draft's material holds. `Reached` now has one standard: the trial surfaced something real that the draft's setting kept off the page, or it reached nothing. Selection looks first for a setting doing cover work. Adds an appropriation check, since construction moves borrow other people's talk, and restricts lingo swaps, second speakers, and host forms to what the draft's world already contains. Adds two failure modes. No dial, range, or coupling changes.

A catalog extension for the Portable Poetics Kernel v0.3. It holds speaker dials: settings of how a poem's speaker talks, each with a range, a page test that reads the draft's current setting off the text, and the trial operation that turns it. It runs standalone under the kernel and requires no private core. Its consumer is the JIG Workshop Mode, which runs dial trials in Function Bay, dial overlays on Confinement Bay trials, a tuning question in Engine Bay, and drill-derived experiments in Function Bay's Single Experiment.

A dial is not a device and not a confinement. A device is a local operation, present or absent at an address. A confinement is the enclosure that limits what a poem can know. A dial is a setting every poem has at some value, whether or not anything on the page calls attention to it, and turning it changes how the poem says what it knows while leaving what it knows where it was. That is why a dial fails the knowledge test by construction and enters the apparatus as an overlay rather than as an entry in `12-confinement-inventory`.

A dial is a probe. A trial turns a setting to find out what the draft's material holds that its current setting keeps off the page: a fact, a cost, a body, a relation, a feeling the speaker has not let in. A trial that changes only how a span sounds has decorated it, and reports that it reached nothing. This is the operator's ruling at v0.2, and Section H records it.

## Module Manifest

Module name: Speaker Dials

Module type: catalog extension, extracted from one calibration source

Calibration source: Tony Hoagland with Kay Cosgrove, *The Art of Voice: Poetic Principles and Practice*. Recorded here because a source policy that cannot name the book it governs cannot govern it. This line is header prose and does not reach output.

Kernel requirement: Portable Poetics Kernel v0.3.16, for the trial-text exemption in Register Prohibitions, the open-or-corner test in Parasitic Effort, the `voice` homograph, and Speaker Dial Compatibility

Private-core requirement: none

Consumer: `3a-workshop` v0.6.0 or later. The file has no sidecar consumer. The device-scale names its entries rely on live in the Extended Device Inventory, where a sidecar can reach them without this file.

Exports:

- dial entries, established and provisional
- the absorbed list
- couplings
- the selection rule
- trial forms: dial trial, dial overlay pair, tuning question, experiment
- the laundering, gating, open-or-corner, and appropriation checks
- drill conversions
- doctrinal seams
- rights and leak control
- the candidate log
- failure modes

Imports from kernel:

- Mechanism Before Vibe
- Engine vs. Residue
- Coscienza, both axes
- Checkpoint 2, Period Fit
- Checkpoint 6, Decoration vs. Diagnosis
- Checkpoint 9, Weak Signal and Absence, for the certainty threshold
- Source Policy, Source Exposure Levels, and the Reassembly Test
- Default Register, with the trial-text exemption
- Designation Policy
- Function Before Parts and Parasitic Effort
- Anti-Laundering Engine Default and Plain Speech as Anti-Laundering
- Cult-Gating Diagnostic
- Appropriation Risk and the Sayability Test
- Rendering Conditions, for the tempo page test
- Speaker Dial Compatibility

Imports from extensions:

- Extended Device Inventory, v0.2 or later, for the device names in each entry's `Device` field
- `12-confinement-inventory`, for the overlay cap and the catalog's carrier observations

Source policy: the calibration source is in copyright. Every entry holds it at Level 0. Entries describe operations and quote none of the book's model poems, example sentences, or exercise prompts. See Section I.

Failure condition: without the kernel the file has no knowledge test to fail, no exposure ceiling, and no exemption for trial text, so a dial trial would be graded as apparatus prose. Without the workshop it is a catalog nothing runs.

## Terminology

The kernel registers `voice` as a homograph at v0.3.16. In this file the craft sense of `voice` appears only where Sections H and I report what the two calibration sources say, in their own terms. Everywhere else the poem's speaking presence is the `speaker`, and the controls are `speaker dials`.

Four terms are local.

**Dial.** A dimension of how the speaker talks, along which every draft has a setting.

**Setting.** A dial's value in a given span, named by the located words that fix it. Settings are named, never scored, under the kernel's rule against numerical scoring.

**Zero point.** The unmarked setting, where the source supplies one. A reader does not notice a span at its zero point and does notice a span moved off it.

**Carrier.** The means by which a poem delivers what it knows or withholds: a joke, a borrowed idiom, decorum, a document, grammar, a double entendre. Dials set properties of the carrier. See Why Dials Are Overlays.

Dial names render in lowercase, like device and confinement names, because capitals are reserved for designations.

## Structure

- **Entry Schema.** The fields and the search attributes.
- **A.** Established dials (4). Each passes the four-part test: its setting can be pointed at on the page, it turns without dragging another dial, each setting is defined by an operation, and the Extended Device Inventory had no name for it.
- **B.** Provisional dials (5). The source names the dimension and shows it working; the apparatus supplies the range, and the inventory already names the devices at its poles.
- **C.** Absorbed (5). Dimensions the source treats as voice that the inventory already names. Recorded so they are not proposed again.
- **D.** Couplings.
- **E.** Selection Rule and Trial Forms.
- **F.** Checks.
- **G.** Drill Conversions.
- **H.** Doctrinal Seams.
- **I.** Rights and Leak Control.
- **J.** Candidate Log.
- **K.** Failure Modes.

Total: 9 dials and 5 absorbed dimensions from one source.

Only one dial has a range and a zero point supplied entire by the source, sd-01. The source names the positions of sd-02. For sd-03 and sd-04 it shows the two ends by example, and the intermediate settings are the apparatus's. Each entry says which settings are whose.

### Why Dials Are Overlays

The knowledge test sorts the apparatus's two kinds of trial. A confinement makes something unavailable to the speaker. A dial changes how the speaker says what is available and makes nothing unavailable, so its knowledge test is empty. `12-confinement-inventory` defines an overlay as a rule that adds a requirement and removes nothing knowable, and a dial setting meets that definition.

The source's poetics explains the result. Its argument runs toward saying more: disclosure, assertion, candor, a speaker who tells more truth than we usually get. The confinement catalog has already rejected poems in that mode for holding nothing back, among them a poem by the calibration source and a sample from a recent book that, in the catalog's words, says what it knows. Dials and confinements vary on independent axes, which is why they compose.

The catalog's Provenance notes record a variable it has no field for. The stand-up corpus carries its limits through jokes, anecdotes, and borrowed idiom; the 1900 collection through decorum, prayer, and inherited figures; the recent books through documents and found language; the Beckett selection through grammar; the Hồ Xuân Hương selection through double entendre. That variable is the carrier, and the carrier is what these dials set. A dial overlay on a confinement trial therefore asks a question the catalog could not ask before: does this confinement's fold survive a change of carrier? The pair form in Section E exists so the seam can answer it.

### Dials and the Bays

A dial runs in the existing bays and adds none. At passage scale it is a contrast trial in Function Bay. At poem scale it is a tuning question in Engine Bay, asked before a swap. Over a confinement trial it is an overlay, run as a pair. One dial, sd-07 certainty, crosses into Confinement Bay at a threshold its entry defines.

## Entry Schema

```text
id:           sd-NN
name:         lowercase words
status:       established / provisional
scale:        passage / poem / overlay, in any combination
zero point:   the unmarked setting, or none
checks:       laundering / gating / open-or-corner / appropriation, or none
```

Fields in each entry:

**Range.** The settings, stated as operations rather than adjectives, with a note of which settings the source supplies.

**Page test.** How to read the draft's current setting off L0, and what to point at.

**Turn.** What a trial does to move the setting one step.

**Holds fixed.** What a trial on this dial must leave unchanged, so that the seam has one candidate cause.

**Reaches.** What turning the dial typically gets to. A candidate for the trial's `Reached` line, never a substitute for it.

**Fails at.** The characteristic seam.

**Couplings.** Dials that move with this one. See Section D.

**Device.** Extended Device Inventory names at the poles and at the shift.

**Calibration.** The source chapter the entry draws on. Header prose; never output.

The search attributes are `name`, `status`, and `scale`. A command may name a dial or select by status or scale. See the workshop's Trigger Grammar.

## A. Established Dials

### sd-01 diction altitude

```text
status: established | scale: passage, overlay | zero point: middle
checks: laundering, gating
```

**Range.** Low: slang, profanity, blunt words for the body and its appetites, the clipped forms of insult and complaint. Middle: the plain functional diction of errands and requests, the level at which a speaker asks for directions or says what happened. High: polysyllabic, Latinate, periphrastic, or ornamented diction. High has two settings that share the altitude and differ in stance: ornamental, which enjoys its own constructions, and clinical, which withholds affect and speaks as a report or a textbook would. Name which. All three positions, the zero point, and the two kinds of high are the source's.

**Page test.** Name the setting by two located words that fix it, a verb and a noun where the span allows. Then mark every shift: the address where altitude changes and the direction it moves. A shift is often more legible than a setting, and a single middle-altitude sentence inside a high passage, or the reverse, is often the span's active site.

**Turn.** Re-say the span one step up or down. Change the words that carry altitude and nothing else.

**Holds fixed.** The proposition, the images, the sentence order, and the line count. Keep lineation where the new words allow it, and report the line where they did not.

**Reaches.** Distance or closeness between speaker and subject. A high span over humble material can make the material strange enough to see, which routes to the kernel's Defamiliarization Engine when the strangeness carries the poem. A low span over a grand subject can bring it into reach, or expose a cost the grand diction was softening. A drop to middle inside a marked passage can ground the speaker in one plain sentence.

**Fails at.** High over bodily cost, where the ornament dresses a wound the draft had left plain. Low as costume, where profanity performs a candor the content never risks. Clinical as evasion, where detachment stands in for a feeling the poem will not admit.

**Couplings.** sd-04 idiom density, which pulls toward the low pole without being the same dial. sd-08 speaker count, since a second speaker licenses a pole the main speaker cannot carry.

**Device.** diction altitude and altitude shift (D). Etymological stratification (D) is the opt-in device for altitude collision at the level of word stock and script, and stays opt-in.

**Calibration.** Chapter VII, with the counterpoint examples in Chapters IV and XI.

### sd-02 assertion position

```text
status: established | scale: poem, passage | zero point: none
checks: open-or-corner, gating
```

**Range.** None: the poem is scene, report, and image throughout. Opening line. Middle. Near the close. Last line. The governing assertion is the one general sentence the poem's particulars are read under. A poem with several general sentences either has one governing assertion with the others subordinate to it, or has several competing ones, which is a finding in its own right. The positions are the source's; none is the apparatus's addition.

**Page test.** Locate the governing assertion and give its address. If two sentences compete, name both and say which one the particulars answer to. If none, the setting is none; say whether a general sentence sits buried in a subordinate clause where it could be promoted.

**Turn.** Move the assertion to another position without changing its wording. Adjust only the junctions on either side of the old and new positions. A turn from none to a position is allowed only by promoting a general sentence the draft already contains; the trial does not write a new claim.

**Holds fixed.** The assertion's wording, every other line's content, and the order of the particulars.

**Reaches.** Each position does a different job, and the source states all four. At the opening, the details must develop a claim already made, and the poem is over unless they complicate it. In the middle, the claim gathers the details that came before and changes how the reader holds them. Near the close, the claim arrives carrying the weight of everything before it. In the last line, the poem closes under one claim, which is the position most exposed to cornering.

**Fails at.** Cornering. The assertion tells the reader what the details mean and stops them meaning anything else. A cliché corners in every position, so moving it never helps, and the open-or-corner check runs before the dial turns.

**Checks.** Open-or-corner, from the kernel's Parasitic Effort directive. Gating: the source treats a confident assertion as an invitation for the reader to entrust and even subordinate themselves to the speaker. Run the gating prompt in Section F when an early assertion demands assent the particulars never pay back.

**Couplings.** None stated by the source. In practice sd-01, since a governing assertion often sits at a different altitude from the scene around it, and moving it moves an altitude shift with it. Report that when it happens.

**Device.** assertion placement (E). Abstraction spike (A), hinge line (E), and isolated line (F) name what the assertion often does once placed.

**Calibration.** Chapter X.

### sd-03 phatic density

```text
status: established | scale: passage, overlay | zero point: none
checks: laundering
```

**Range.** Bare: statement only, with no gesture toward the listener. Sparse: an aside at a turn. Conversational: tags, asides, and check-ins at sentence edges through the span. Padded: a contact gesture in most sentences. A phatic gesture carries no information about the subject and works on the contact between speaker and listener: a tag, an aside, a hedge addressed to the listener, a rhetorical question, a check-in. The source shows bare and conversational by example; sparse and padded are the apparatus's.

**Page test.** Mark every phatic gesture with its address. Do not count them into a score. Name the setting by where the gestures fall and what they do there.

**Turn.** Down: delete the gestures and hold everything else. The source runs this ablation on a passage of its own and reports that the story survives while the listener is shut out, which is the dial's clearest calibration. Up: insert gestures at sentence edges only, never inside an image, and only gestures this speaker could plausibly use, which ties the turn to sd-04's lingo source.

**Holds fixed.** Every content word, the images, and the order.

**Reaches.** Down reaches compression and impersonality, and sometimes a hardness the draft was cushioning. Up reaches confiding: the reader placed as a listener, and the speaker's stance toward that listener made audible.

**Fails at.** Warmth over avoidance, where the gestures draw the reader close to material the poem then declines to expose. A gesture that manages the speaker's image rather than the contact is parasitic effort in the kernel's sense. Name the action a gesture performs before deciding which it is.

**Checks.** Laundering, on every upward turn.

**Trial text.** An upward trial produces phrases the kernel bans from apparatus prose as filler openers and glue. Trial text is outside every zone the default register governs, per the kernel's Register Prohibitions. Do not cut the phrases from the trial; cut them from the commentary.

**Couplings.** sd-04, through the lingo source of the gestures.

**Device.** phatic gesture (G). Addressee position (A) and reader activation (G) name what the gestures often set up.

**Calibration.** Chapter III and its exercises.

### sd-04 idiom density

```text
status: established | scale: passage, overlay | zero point: none
checks: laundering, gating, appropriation
```

**Range.** Density runs from none, standard written English, through flavored, an idiom at a junction, and steady, to saturated, an off-standard phrase in most lines. Every setting above none also has a lingo source: the region, trade, generation, class, institution, or online community whose talk the idiom comes from. Name both. The source shows none and saturated by example; flavored and steady are the apparatus's. The lingo source is the source's.

**Page test.** Locate the phrases a reader outside the lingo source would need glossed or would hear as a marker of membership. Name the source.

**Turn.** Change density one step and keep the lingo source, or change the lingo source and keep the density. Never both in one trial. A new lingo source must be one the draft shows the speaker to have, a trade, a place, a family's talk, a generation; see the appropriation check in Section F.

**Holds fixed.** The proposition, the images, and the speaker's situation.

**Reaches.** A speaker placed socially in a phrase. Speed. Humor. A high or remote subject brought into reach. A reader inside the lingo bound to the speaker.

**Fails at.** Wrapping, where the idiom dresses a cost so it goes down easy. The source offers this as a virtue, figuring the vernacular as a covering that can dress almost any material, and it is the inventory's tonal laundering. Gating, where the idiom sorts readers into insiders it rewards and outsiders it shuts out.

**Checks.** Laundering and gating, both mandatory on every trial. The source's own account of the dial calls the reader an initiate, which is the word the Cult-Gating Diagnostic asks about. Appropriation, on every change of lingo source.

**Couplings.** Heavy idiom pulls the lineation toward run-on enjambment and dropped punctuation, by the source's account of its spoken grammar. Hold the lineation or report that it moved. sd-01 toward the low pole, though trade and institutional lingo often sits high.

**Device.** in-group idiom (D). Euphemism and dysphemism (D) where the idiom carries either.

**Calibration.** Chapter V and its exercises.

## B. Provisional Dials

The source names each of these and shows it working in model poems, without positions enough to fix a range, and the inventory already names the devices at the poles. The apparatus supplies the range. A provisional dial runs in trials like an established one, and each trial's seam reports whether the supplied range held on the draft. Promotion is the operator's call, made on trials across more than one draft.

### sd-05 visible revision

```text
status: provisional | scale: passage | zero point: none
checks: none
```

**Range.** Finished: the span delivers its conclusions without a trace of reaching them. Qualified: claims arrive with their conditions attached. Revising: the speaker corrects, withdraws, or replaces a word or claim in the act of saying it.

**Page test.** Locate corrections, qualifications, withdrawals, and self-interruptions.

**Turn.** Up: insert one correction or qualification at a junction where the draft's claim could plausibly be revised. Down: remove them and state the surviving claim.

**Holds fixed.** The claim the span ends on, and the images.

**Reaches.** A speaker seen deciding, whose credibility comes from the record of the change.

**Fails at.** Performed hesitation, the stammer as manner, where nothing is being revised and the corrections only decorate.

**Couplings.** Independent of sd-06, since the source shows revision at both speeds.

**Device.** correctio, modal qualification, interruption, recursive sentence growth (C).

**Calibration.** Chapter II.

### sd-06 tempo

```text
status: provisional | scale: passage | zero point: none
checks: none
```

**Range.** Fast: run-on syntax, coordination, light or absent punctuation, clauses that tumble. Measured: sentences of ordinary length that end where they end. Slow: qualifying clauses, end-stopping, short lines and long pauses.

**Page test.** Name the setting by the syntax and the punctuation, with addresses. Read it from a clean rendering. Tempo is a pace judgment, and the kernel's Rendering Conditions names pace among the judgments a heavy rendering contaminates.

**Turn.** Re-punctuate, and join or split clauses, one step. Change syntax and punctuation only.

**Holds fixed.** The words, as far as the syntax allows. Report any added or removed connective.

**Reaches.** Fast reaches breathlessness and the unedited mind. Slow reaches deliberation and weight on each qualification.

**Fails at.** Speed as hurry with nothing to outrun. Slowness as stall.

**Couplings.** sd-04 pulls toward fast through its run-on lineation.

**Device.** parataxis, hypotaxis, cumulative sentence (C); enjambment, end-stopping, pause length (B).

**Calibration.** Chapter II.

### sd-07 certainty

```text
status: provisional | scale: passage, poem | zero point: none
checks: none
```

**Range.** Assured: the speaker states. Hedged: the speaker states with marked doubt. Unsure: the speaker cannot say how it was.

**Page test.** Locate the doubt markers and say what the doubt is about.

**Threshold.** Before any turn, ask which kind of doubt the span carries.

> Is the speaker unsure how to say it, or unsure what happened?

Doubt about how to say it is a manner, and the dial governs it. Doubt about what happened is a knowledge limit. At that point the setting has become a confinement and the trial routes to Confinement Bay, where the catalog's neighbors are cf-as-04, fading description, and cf-me-04, borrowed testimony. A turn that pushes a draft across the threshold has changed what the poem can know, which is an engine change wearing a dial's name.

**Turn.** Below the threshold only: add or remove doubt markers.

**Holds fixed.** The events reported.

**Reaches.** Toward assured, a speaker's authority. Toward unsure, the credibility of a speaker who admits the edge of what they remember.

**Fails at.** Doubt as modesty, hedging that reports no real uncertainty, which the kernel's hedging ban already names.

**Couplings.** sd-05, since revision often carries doubt.

**Device.** modal qualification, interrogation (C).

**Calibration.** Chapter II and its second exercise.

### sd-08 speaker count

```text
status: provisional | scale: passage, poem | zero point: none
checks: appropriation
```

**Range.** One: a single speaker throughout. Quoted: another speaker's words appear inside the main speaker's account. Several: two or more speakers hold the floor in turn. Self-quoted: the main speaker quotes a version of the self, often at another altitude.

**Page test.** List the speakers by address, including institutional and imagined ones, and give each one's altitude.

**Turn.** Up: give one line of the span to a second speaker the draft's situation already contains. Down: return a quoted line to the main speaker's account.

**Holds fixed.** The proposition and the scene.

**Reaches.** A second kind of talk set against the first, conflict and contrast inside one poem, and an altitude the main speaker could not carry without sounding false. The source names this licensing explicitly: a high-altitude line spoken through quotation, by a speaker who otherwise talks plainly, keeps its shapeliness and lets the reader keep a critical distance.

**Fails at.** A second speaker as decoration, a quoted line that sets nothing against the first. Another person's suffering given a line so the poem can borrow its weight, which the appropriation check exists to catch.

**Couplings.** sd-01, through licensing.

**Recurrence.** Attributing the load-bearing statement to another speaker has the surface of cf-wl-02, found inscription. The position differs. In the catalog entry the speaker lacks the authority to make the statement; in the source's examples the speaker lacks the decorum to make it in his own diction. The catalog already holds evidence that position alone does not fix a confinement. This is the converse, evidence that surface alone does not fix one either. It is a reading of the source's readings and is recorded here rather than in the catalog, since nothing was extracted from a specimen on the page.

**Device.** ventriloquy (A), restored at inventory v0.2. Dialogue and monologue (E). Quotation and prosopopoeia (D).

**Calibration.** Chapters VIII and XI.

### sd-09 host form

```text
status: provisional | scale: passage, poem | zero point: none
checks: gating, appropriation
```

**Range.** Two variables, and a trial turns one. The form: none, or a public genre the speaker borrows, such as a corporate notice, a campaign promise, a review, a police report, a public announcement, a petition, a recipe, an invitation. The power direction: the speaker speaks as the form's power, or the speaker petitions the power in its own form.

**Page test.** Name the form by the formulas that mark it, with addresses. Name the direction.

**Turn.** Reverse the power direction and hold the form. Or, at passage scale only, recast a span in a form the draft's world already contains and hold the direction.

**Holds fixed.** The situation the form is applied to.

**Reaches.** The source reports the direction's effect directly: the same bureaucratic diction is comic when the institution speaks down and poignant when a powerless speaker petitions up. Power direction is the catalog's axis seen from the side of the form, and the petition sits upward.

**Fails at.** Form as costume, a borrowed genre with no power relation in it. A whole draft recast in a host form is an engine swap and belongs in Engine Bay.

**Device.** documentary insert (E), which covers the bureaucratic insert; citation-as-device (D).

**Calibration.** Chapter IX and its exercises.

## C. Absorbed

These dimensions carry weight in the source and already have names in the Extended Device Inventory. Treating them as dials would add a range without adding an operation the inventory lacks. A drill on one of them can still yield an experiment; see Section G.

- **Address.** Addressee position and apostrophe (A).
- **Self-disclosure.** Confession posture (A) and self-implication (G). The source's version is an opening admission of failure or error, which sets the speaker on the reader's level.
- **Noun habitat.** Catalog radius and zoom by noun specificity (A), with the workshop's Specific Over General. The source's claim worth keeping is that the class of nouns a speaker owns is a claim about the speaker's experience, which routes to credibility management (G).
- **Dual diction.** Two altitudes applied to one referent in one moment, so the speaker is attached and detached at once. Affect-content carrying capacity (G), and a use of sd-01 within a line.
- **Occasion mismatch.** A stated intent the diction contradicts, such as thanks for a harm or an apology not meant. Irony (D), at the level of stance.

## D. Couplings

Turning one dial can move another. A trial that turns a coupled dial holds its partner or reports that it moved, because two moved dials give the seam two candidate causes.

| Turned | Moves | Basis |
|---|---|---|
| sd-08 speaker count, up | sd-01 diction altitude, toward a pole | stated by the source |
| sd-04 idiom density, up | lineation toward run-on; sd-06 toward fast | stated by the source |
| sd-04 idiom density, up | sd-01 toward low | observed in the source's examples |
| sd-03 phatic density, up | lingo source of the gestures, to match sd-04 | required by this file's turn rule |
| sd-02 assertion position | any altitude shift the assertion carries | observed in the source's examples |
| sd-07 certainty, toward unsure | sd-05 visible revision, toward revising | observed in the source's examples |

The source denies one coupling: sd-05 and sd-06 are independent, since it shows visible revision at fast and slow speeds alike.

The zero point of sd-01 has a consequence the source states. Middle diction is unmarked and the poles are audible. A shift away from middle is heard as a choice, and a return to middle inside a marked passage is heard as grounding, which is why the shift address is often the active site.

## E. Selection Rule and Trial Forms

### Selection

When a command names a dial and a setting, use them and do not substitute. When it names a dial only, select the setting by the rules below. When it names nothing, the reasoning path selects both.

Select for cover first. Before choosing a direction, ask what the draft's current setting may be protecting. A high span over a death, a clinical span over a body, asides crowded around an admission, an idiom that hurries past a fact: each is a setting doing cover work, and the turn that takes the cover off is the first candidate. The kernel's Weak Signal directive applies, and so does its guard against manufactured signal. Point to the line where the cover sits, or do not claim it. A setting with nothing under it is left alone.

Then select against the draft's setting. A draft at middle altitude is offered high and low; a draft at a pole is offered middle first, because the unmarked setting shows the poet what the pole was doing. Similarity produces a trial that tells the poet what the draft already does, which is the same reason the confinement catalog selects against the draft's axis.

Select the dial whose setting holds the target passage's trouble. A trouble that is a failed action belongs to Function Bay's ordinary procedure; a dial turned there changes a setting where the passage needed a different action.

Abstain when every candidate setting fails its checks on the draft's material. Ship the page test alone and say why. Abstention is a completed judgment.

### One Dial Per Trial

A trial turns one dial one step, holds what the entry's `Holds fixed` field names, and holds or reports every coupled dial. The rule follows from the confinement catalog's reason for its three-primitive cap: beyond one variable the seam has more candidate causes than it can separate. The source's own exercises keep to it, holding a sentence, a referent, or a scene fixed while one setting moves.

### Dial Trial

The passage-scale form, run as Function Bay's contrast trial when the target passage's trouble is a setting. The wrong-way trial turns the dial one way and the cleaner trial the other.

```text
Dial:     [name], from [draft's setting] to [trial setting]
Span:     [address]
[the rewrite]
Reached:  [what real thing surfaced, and the draft line where it was latent]
Seam:     [where it failed, named]
```

`Reached` is the completion test, and from v0.2 it has one standard. The trial surfaced something real that the draft's material holds and its setting kept off the page: a fact, a cost, a body, a relation, a feeling. Name it and point to the draft line where it was latent. A trial that changed the span's sound, flavor, attitude, or charm and surfaced nothing reports `Reached: nothing, setting only`. It is costume, and it ships only as a report of that. `Seam` is mandatory and is not modesty.

The thing surfaced has to be in the draft already. A trial that invents a fact, a wound, or a feeling the draft gives no ground for has not revealed anything; it has written a different poem, and the firewall applies.

### Dial Overlay Pair

The Confinement Bay form. A dial overlay runs paired with the same confinement trial without it.

```text
Trial 1:  [confinement name or names]
Span:     [address]
[the rewrite]
Reached:  [...]
Seam:     [...]

Trial 2:  [the same confinement] + [dial name]: [setting]
Span:     [the same address]
[the rewrite]
Reached:  [what real thing the change of carrier surfaced]
Seam:     [what changed at the fold between trial 1 and trial 2]
```

Both trials meet the `Reached` standard above.

The pair counts as Confinement Bay's two default trials. A dial overlay counts against the one-overlay cap, so the ars poetica overlay and a dial setting do not run in one trial. A lone overlay trial ships only on an explicit command and states that its seam cannot separate the carrier from the confinement.

The second seam reports carrier denaturation when the fold collapses: the confinement's position and surface survived the change of setting, and the fold that held them did not.

### Tuning Question

The Engine Bay form, asked under Tuning Before Swap.

> Which dial setting works against the current engine?

Name the dial, the draft's setting, and the address. A setting that works against the engine is a tuning matter, and a dial cannot propose a new engine.

### Experiment

The Single Experiment form. An experiment is an operation the poet runs on the poet's own draft, stated in workshop speech, drawn from Section G and restated for this draft. The apparatus writes no lines for it.

### Caps

One dial trial pair per Function Bay target passage. One dial overlay pair per treatment. Experiments stay under Function Bay's own cap of one, two at most. Dial trials and overlays run only on command. An experiment may appear unasked, because the workshop's output gate already asks for one.

## F. Checks

Four checks, each a prompt answered against the trial before it ships.

### Laundering

> Does the trial setting make the draft's cost easier to accept than the draft made it?

If yes, the trial has laundered, and the seam says so. It never ships as a success. The check draws on the kernel's Anti-Laundering Engine Default and Plain Speech as Anti-Laundering, and on tonal laundering in the inventory. Mandatory on every upward sd-03 turn, every sd-04 trial, and any sd-01 trial that moves bodily or ethical material toward the ornamental or clinical high.

### Gating

> Does the trial setting sort readers into those it rewards and those it shuts out?

If yes, run the kernel's Cult-Gating Diagnostic on the trial. If no, do not; the kernel deploys that diagnostic only where a coercive attention structure shows, and automatic use turns it into its own priesthood. The prompt is mandatory on sd-01 trials toward high, which gate by prestige; on sd-04 trials, which gate by tribe; on sd-02 trials that move the assertion early, which can demand assent before paying for it; and on sd-09 trials where the speaker voices the form's power.

### Open or Corner

> Does this general sentence open the details around it, or corner them?

From the kernel's Parasitic Effort directive. Mandatory before every sd-02 trial. A sentence that corners is theme announcement and goes; moving it does not help. A sentence that opens is a governing assertion, and its position is a tuning question.

### Appropriation

> Whose talk is the trial borrowing, and does it belong to the draft's world?

From the kernel's Appropriation Risk directive, with its prompts: who speaks, who pays, who disappears, and what the poem gains from the borrowed speech. A trial borrows only talk the draft's world already contains: a lingo the speaker is shown to have, a second speaker the situation holds, a form the speaker's life passes through. A group's idiom imported for its color, a stranger's mouth, or another person's wound given a line fails the check, and the trial does not ship. The Sayability Test applies whenever the borrowed speech carries someone else's suffering. Mandatory on every sd-04 trial that changes lingo source, every sd-08 trial, every sd-09 trial, and any experiment that asks the poet to speak in someone else's way of talking.

## G. Drill Conversions

The source closes with twenty-six exercises across nine chapters. Chapter VI, on influence, has none, and is the one chapter the source never turns into practice.

The drills sort three ways. Ten are stem generators: each takes a model poem's opening as a template, asks for a catalog, then asks the poet to put it in sequence. Nine change one setting with the content held fixed. Seven are other: borrowed forms, a quota, a lingo prompt, an admission opener, and an analysis exercise.

Stem generators are not converted. Their stems are other poets' lines, so a trial built on one reproduces phrasing, and a stem run against a draft imports a different poem. They are recorded by chapter so that nobody converts them later: II-1, II-3, III-1, IV-2, IV-3, V-1, V-2, VIII-2, XI-1, XI-2. The quota drill, IV-1, is absorbed by Specific Over General. The analysis drill, X-3, asks the reader to invent a terminology for a poem's parts, which is the warrant for an apparatus and not an experiment on a draft.

The rest convert to experiments: operations the poet runs on the poet's own draft. Each is the apparatus's restatement in workshop speech and quotes nothing from the source. Fit it to the draft at hand before it ships.

| id | dial | experiment | source drill |
|---|---|---|---|
| ex-01 | sd-01 | Rewrite one stanza one step plainer or one step fancier than it is now, with the same images in the same order. Read both aloud and keep the lines the other version made you hear. | VII-1, VII-2 |
| ex-02 | sd-01 | Say the poem's grandest thing in the plainest words you have, and its humblest object in the most formal words you have, two or three lines each. | VII-1, VII-2 |
| ex-03 | sd-03 | Strike every aside and check-in from one stanza and read what is left. Then, separately, add three this speaker would really say, only at the start or end of sentences. | III-2, and the Chapter III ablation |
| ex-04 | sd-02 | Find the one general sentence the poem's details answer to. Make three copies of the poem with it first, in the middle, and last, changing only the lines on either side of it. | X-1 |
| ex-05 | sd-02 | Allow the poem one general sentence and put it last; every other line has to be scene or report. Then ask whether that sentence opens the details or shuts them. | X-2 |
| ex-06 | sd-08 | Let three people from the poem's own world name its central thing, each in their own way of talking: someone official, someone close, someone who never saw it. Keep any line that tells you something you had not let yourself say. | VIII-1 |
| ex-07 | sd-07 | Retell the poem's event as someone not sure of it: one correction, one question, one admission that a detail may be wrong. Stop if the doubt starts changing what happened. | II-2 |
| ex-08 | sd-09 | Recast one stanza in a form the poem's world already has, a notice or a report or a review. Decide whether the speaker writes as the institution or asks something of it, then try the other. | IX-1, IX-2, IX-3 |
| ex-09 | sd-04 | Rewrite three lines in the working talk of a trade or place the speaker actually belongs to. Then ask whether the talk makes the hard part easier to swallow than it should be. | V-3 |
| ex-10 | absorbed: occasion mismatch | Rewrite the poem's address as thanks, or an apology, the speaker does not mean. | VII-3, VII-4 |
| ex-11 | absorbed: self-disclosure | Open with a fault the speaker would rather not show, and see what the rest of the poem has to do afterward. | III-3 |

## H. Doctrinal Seams

The calibration source and the workshop's calibration source share a lineage and part at four points. The operator ruled on them at v0.2. Where the two disagree, the workshop's position governs: what makes a speaker worth hearing is the depth of attention behind the lines, and a dial is a way of digging there. The source's construction moves stay in this file as probes. Its account of voice as charm, entertainment, and assembled personality governs no trial.

**Personality. Ruled for depth.** The source holds that a voice embodies the presence of a self, a personality or a sensibility, assembled from borrowed speech. The workshop holds that voice is not personality pasted onto language, and the TARE substrate holds that it is moral substrate. Consequence: the `Reached` standard in Section E. A trial that changes how a span sounds and surfaces nothing is costume.

**What plainness does to cost. Ruled for exposure.** The TARE register treats plain speech as a discipline that exposes cost. The source treats the vernacular as a covering that can dress almost any material. Consequence: a phatic or idiom trial passes only when the plainer or more spoken setting brings the cost into view. The laundering check stays mandatory, and a trial that wraps the cost fails.

**Reader position. Ruled for the peer.** The source holds that a reader will entrust and even subordinate themselves to a convincing speaker, and it calls the reader of vernacular an initiate. The workshop keeps the reader a peer. Consequence: a trial that wins the reader by surrender to authority or by insider membership reached nothing. The gating check stays, and the Cult-Gating Diagnostic fires on what it finds.

**Abstraction. Settled by test.** The workshop treats abstraction without image as sermon and lists theme announcement as parasitic effort; the source treats a general assertion as a source of authority. The kernel's open-or-corner test settled this before the ruling and agrees with it: a general sentence that opens the details is a way of revealing them, and one that corners them goes.

**What survives from the source.** The ruling keeps the source's candor strand, which is a mining strand: candor that wants nothing from the reader, a speaker who tells more truth than speakers usually do, an opening admission of failure, a second speaker who takes the poem out of the main speaker's control, a borrowed public form turned to expose the power that owns it. These are the moves the dials and experiments are built from. The apparatus already holds a register to the same discipline: the TARE module states its own register as settings for diction mix, rare-term density, sentence length, and specificity, and those settings serve its aim of keeping cost visible.

**Appropriation.** Construction moves borrow: other people's talk, other groups' lingo, institutions' forms. Borrowed for color, they are both the costume the ruling excludes and the appropriation the kernel's directive names, so the ruling raises the stakes on every borrowing move. The appropriation check in Section F is the gate.

**Extraction asymmetry.** This file has no voice zone. When a dial trial's result meets the TARE voice in a workshop verdict, TARE speaks in its own register and the trial's result enters as a note in the default register. After the ruling the asymmetry runs the way the doctrine does, since the voice that speaks is the one that governs. State the imbalance in any treatment where a trial's result and the verdict disagree.

## I. Rights and Leak Control

A dial is a procedure, and a procedure is not protected expression. Eight items still need control in practice.

**The book.** In copyright and held at Level 0 in every entry. No model poem, example sentence, or exercise prompt from the source is reproduced here or in any trial. The source's calibration ladders, one proposition said at several altitudes, are not reproduced; a trial builds its ladder from the draft.

**Tier A.** The source's name and the book's title appear in this header and nowhere in output. The file name carries no source name, on the precedent of `11-provenance-grading-extension` and `12-confinement-inventory`.

**Tier B.** The source's chapter terms are its coinages in this domain and stay in the header: mind in motion, the sound of intimacy, speech additives, the warmth of worldliness, the material-verbal imagination, the tribal bond of the vernacular, imported voices, voices borrowed from the environment, the voice of authority, the heroic integration of the self. Output uses the entry names. Diction altitude replaces the source's altitude metaphor for register, a field-standard figure, because `register` already names the apparatus's own prose and the critic registers. Phatic density takes a field-standard linguistic term.

**Tier C.** The source carries few biographical anchors, chiefly a friend's account of a formative reading. None is used.

**Tier D.** The source's model poets are cited in a trial only when they bear on the draft, never to sound like the source. Several also appear in the workshop's corpus.

**Drill stems.** A stem is a model poem's opening. A trial or experiment that uses one reproduces a specimen's phrasing and runs Template Transfer. Section G converts drills to operations for this reason.

**Calibration collision.** The source is also a poet. Under `0c-voice-designations` v0.5, a specimen by either credited author stops dial trials, dial overlays, and dial-derived experiments for that specimen, and the rest of the workshop treatment runs. The note is a jurisdiction note without cause. The book's own example poems, marked in the text as improvised, are the source's and are calibration material, not specimens. One further example poem is unattributed and is probably the source's as well (P4).

**Specimens reprinted in this corpus.** The book reprints some fifty model poems in excerpt with the source's commentary. Under Section F of `12-confinement-inventory` they are left out of confinement selection. None of the catalog's specimens is among them, checked against the catalog's handles, titles, and authors.

## J. Candidate Log

| Candidate | Status | Note |
|---|---|---|
| *The Art of Voice* | extracted v0.1 | Four established dials, five provisional, five absorbed, one zero point, six couplings. Chapter VI yields no dial and no drill |
| a `carrier` field in `12-confinement-inventory` | deferred | The overlay pair reports carrier change at the seam without one. Back-filling 194 entries needs the specimen texts on the page, and a carrier read from memory is the fabrication the catalog's Candidate Log forbids |
| the workshop's own pedagogy corpus | declined | Not mined for dials. It calibrates JIG, and dials drawn from it would fuse this extension's register with the mode's |
| further sources | open | A second source would test whether the established dials are operations or the style of one source, the test the confinement catalog's recurrences ran on its primitives |

## K. Failure Modes

### Dial as Confinement

A setting is extracted or selected as a knowledge limit.

Correction: run the knowledge test. If nothing becomes unavailable to the speaker, it is a dial. sd-07 is the one dial with a threshold, and its entry states the test.

### Two Dials Turned

A trial moves two settings, or moves a coupled dial without reporting it, and the seam has two candidate causes.

Correction: the `Holds fixed` field and Section D. Hold the partner or report it.

### Carrier Costume

A dial overlay moves the carrier, the fold collapses, and the trial ships as a success. The dial form of the catalog's Denatured Transfer.

Correction: the pair form. Trial 2's seam states what changed at the fold.

### Wrapped Cost

A setting dresses the draft's cost so it goes down easier, most often on sd-03 and sd-04, and the trial reports the ease as a gain.

Correction: the laundering check.

### Tribal Gate

A setting rewards readers inside a lingo or a prestige class and shuts the rest out, and the trial reports the bond as a gain.

Correction: the gating prompt, then the Cult-Gating Diagnostic if it fires.

### Stem Import

A drill's opening line is run against a draft as a trial, or handed to the poet as an experiment.

Correction: Section G. Experiments are operations, restated for the draft.

### Scored Setting

Settings become counts, and the trial reports a dial moved from one figure to another.

Correction: name settings by located words. The kernel does not score.

### Costume Trial

New in v0.2. A dial trial changes how the span sounds, more charming, more spoken, fancier, more streetwise, surfaces nothing real, and ships as a result. The characteristic failure under the operator's ruling.

Correction: the `Reached` standard in Section E. Name the real thing and the draft line it was latent in, or report `Reached: nothing, setting only`.

### Borrowed Mouth

New in v0.2. A trial borrows a group's idiom, a stranger's speech, or another person's wound for its color, and the borrowing does the poem's work for it.

Correction: the appropriation check in Section F. Borrow only talk the draft's world already contains.

### Dial as Persona

The draft's settings are read as the poet's true voice, and a dial trial is offered as the way the poet should sound. The dial form of Trial Capture.

Correction: the trial firewall. A dial trial is a contrast trial and never a revision route.

## Provenance

Occasioned by an operator-supplied text of the calibration source in October 2026, after a boot of the apparatus and a reading of the book. The operator asked whether the book's account of voice yields dials that can run in the workshop's trials.

The text is a plain-text conversion of the book, with the title page and table of contents present (P0) and the watermark of OceanofPDF.com at each chapter break (P0), the same provenance as the recent books in the confinement catalog's v0.10 batch. Excerpted model poems are elided with rows of dots, and the cross-references to exercise pages cite page numbers the file does not otherwise print. Dates in the book's own examples fall in 2018 (P0). The year of publication, 2019, and the publisher are the apparatus's recollection (P4).

The source sits in the workshop's neighborhood, and the overlap is recorded because it bears on collision and on Tier D. The source and the workshop's calibration source both appear in the stand-up anthology the confinement catalog extracted at v0.6 and v0.7, where the catalog read a poem by the source and rejected it as having nothing withheld (P0, the catalog's Candidate Log). The source names, among poets whose work can start a vocation, the poet who wrote the foreword to the workshop's corpus (P0). Eleven poets the source cites, among them Stern, Gregg, and Rukeyser, also appear in the workshop's corpus (P0, by search). Both books pair short chapters with model poems and exercises.

The extraction found the source's claim to demystify voice partly made. The book argues that a speaker is assembled from borrowed speech, which is what makes a setting possible at all. It scales one dimension, names the positions of a second, shows the poles of two more, and names the rest without a range. No chapter says when a setting should be turned, and the book closes by holding that voice works in more ways than a craft handbook can identify. The selection rule, the checks, the pair form, and the one-dial rule are the apparatus's.

v0.2 applies the operator's ruling on the doctrinal seams, given after the operator read a summary of them: the workshop's position governs, and construction moves are worth running only to mine the draft for what it holds. Dressing a draft up was named as a waste of the poet's time and a source of appropriation risk. The ruling changes the completion test, adds selection for cover and the appropriation check, and leaves the dials themselves as they were.
