# EXTENDED DEVICE INVENTORY

Version: 0.2

Revision 0.2: the first stamped version. Earlier releases carried no version line, so the hollow boot could not register the file; 0.2 is assigned so that it can, and records nothing about how many unstamped releases came before. Restores ventriloquy to Category A. It sits in the kernel's Device Inventory Lite, and this file replaces the lite inventory while loaded, so the device disappeared whenever more resolution was loaded. Adds five devices that `13-speaker-dials` names at its poles and shifts: diction altitude, altitude shift, and in-group idiom to Category D, assertion placement to Category E, and phatic gesture to Category G. Their examples are invented, so that no example comes from the dial file's calibration corpus. Corrects three stale references: the workshop is JIG workshop mode, `3a-workshop`, not the name it carried before its hygiene pass, and the kernel gate has ten steps, not eight. Adds a guard at the head of Section K, which predates the kernel's removal of specimen retrieval at v0.3.10. Total devices rise from 183 to 189.

Device extension for the Portable Poetics Kernel v0.3. It runs as a standalone module under the kernel and does not require the private core boot `0-poetics-boot.md`. When a full monty plugin is loaded, the plugin may enrich device examples with source-bearing calibration beneath this extension. Loaded on demand when device-level precision matters, when the reader is unfamiliar with a particular device class, or when the Hermetic or alchemical lens is the relevant diagnostic frame.

## Module Manifest

Module name: Extended Device Inventory
Module type: device extension
Kernel requirement: Portable Poetics Kernel v0.3
Private-core requirement: none
Optional private-core enhancement: a full monty plugin may enrich device examples with source-bearing calibration. The extension runs without one.

Exports:
- triggers: device-level naming resolution for every sidecar; Hermetic chamber re-sort on structural warrant; Scan mode for device-driven specimen fetch
- procedures: replace Device Inventory Lite as the active device catalog while loaded; tag devices by alchemical function on opt-in; locate and diagnose specimens by named device
- integrations: serve as the device-naming resolution for JIG workshop mode, `3a-workshop`, when that module is loaded, under the workshop register lock; supply the device names `13-speaker-dials` uses at its poles and shifts
- output fields: device tables A through G, Hermetic tag table H, training corpus I, specimen clusters J, scan catch output K
- constraints: period fit on every named device; empty bins stay empty; Nom and English-simulation entries and the Hermetic re-sort are constrained opt-ins; source exposure held to the lowest level that preserves the mechanism
- failure modes: forced bin fill, voice drift in scan output, source exposure excess
- examples: the per-device example column and the corpus in Section I

Imports:
- Device Inventory Lite, replaced while this extension is loaded
- Six Core Dimensions, with Pressure and Engine vs. Residue
- Coscienza on both axes and Access Honesty
- Algorithmic Reconstitution
- Kernel Sidecar Format
- the ten-step Checkpoint Gate
- Source Policy and Source Exposure Levels
- Constrained Opt-In Devices: English-Nom Hybrid Signals and Hermetic or Alchemical Chamber Reading
- Default Register

Source policy:
No full reproduction of copyrighted poems. Examples use token or pressure quotes. Public-domain full text appears only under Source Exposure Level 4 conditions. Scan mode reports provenance and pressure quotes, never full reproduced text.

Failure condition:
The extension is not standalone. It requires Portable Poetics Kernel v0.3. With no voice module loaded, scan output and closing prose use the default register and claim no named voice.

Voice Rendering Mode:
When a voice module is bound, closing prose and any triangulation the extension feeds into a sidecar are rendered in that voice per the kernel rule. Device tables, the Hermetic tag table, scan-catch fields, and every structured label stay in the default register; the voice renders the commentary, not the labels.

## Structure

- **A.** Deictic and Scalar Devices (24)
- **B.** Sonic and Prosodic Devices (30)
- **C.** Syntactic and Sentence Devices (30)
- **D.** Figural and Rhetorical Devices (33: 29 base + 4 Nôm / English-simulation)
- **E.** Structural and Compositional Devices (31)
- **F.** Visual and Typographic Devices (20: 15 base + 5 Nôm / simulation / wildcard)
- **G.** Pragmatic and Ethical Devices (21)
- **H.** Hermetic / Alchemical Subcluster: vessel / seal / valve / transmuter re-sort, fresh count
- **I.** Corpus for Training and Stress-Testing
- **J.** High-Value Device Clusters by Specimen
- **K.** Scan Mode: Device-Driven Specimen Fetch (operating mode, not catalog)

Total inventory: 189 devices (180 core + 9 Nôm / simulation / wildcard extras).

Modal use: kernel-only mode runs Device Inventory Lite; kernel plus this extension runs full resolution; kernel plus extension plus Section H runs the inventory through the alchemical lens. Kernel constraints apply in every mode. Nom and English-simulation devices remain a constrained opt-in (English-Nom Hybrid Signals), period fit applies to all named devices per Checkpoint 2, and empty bins remain honest.

### Augmentation Behavior

When loaded, this extension replaces Device Inventory Lite as the active device-naming resolution for every sidecar the apparatus produces. The lite inventory does not run in parallel; the extended inventory is the catalog the apparatus deploys. Empty bins remain honest. Forced fill across the full set of devices fails Checkpoint 6, Decoration vs. Diagnosis, and breaks the kernel rule that keeps empty bins empty, the same way it did across the lite bins. Section H is the kernel constrained opt-in Hermetic or Alchemical Chamber Reading. It fires on the specimen's structural warrant, where chamber and pressure dynamics make the seal-versus-valve seam carry the ethical or transformational weight, not by default. The extension augments every standard reading the apparatus performs; it is not a separate mode the user must invoke per specimen.

## Workshop Integration

When JIG workshop mode, `3a-workshop`, is loaded, this extension serves as the workshop's device-naming resolution. The workshop routes its craft diagnostics, Engine Bay, and Function Bay through these Categories. The section-by-section routing lives in the workshop file under Device Resolution Map; this section states the provider-side contract.

Category service:

- Category A serves Image Inventory and the speaker-position and pronoun parts of Engine Bay.
- Category B serves Sound and Cadence Scan and the sound parts of Line Break Analysis.
- Category C and the Category B line devices serve Line Break Analysis.
- Category D serves Diction and Language Check and the central-image and conceit parts of Engine Bay and Function Bay.
- Category E and Category F serve Form Examination and the title, turn, and refrain parts of Engine Bay.
- Category G serves Voice and Moral Substrate and the body-cost and moral-substrate tests.
- Section H, the Hermetic or Alchemical Chamber Reading, is an optional lens for Form and Engine analysis when the specimen's structure rewards chamber, seal, valve, and transmutation language.

Governance under workshop use:

- The workshop register lock governs surface language. Device names surface plainly only in Engine Bay and Function Bay. Elsewhere the workshop translates them to workshop speech.
- The English-Nom Hybrid Signals opt-in and the Hermetic or Alchemical Chamber Reading opt-in stay opt-in. Period fit applies to every named device. Empty bins stay empty, and the workshop does not force-fill devices to decorate a treatment. Forced fill fails Checkpoint 6.

Speaker dials, from v0.2. Diction altitude, altitude shift, and in-group idiom (D), assertion placement (E), and phatic gesture (G) are the device names for the poles and shifts of the dials in `13-speaker-dials`, with ventriloquy (A) for its speaker-count dial. This inventory names the devices, so a sidecar can use them without the dial file; the dial file holds their ranges, page tests, and trials.

If JIG workshop mode is absent, this section is inert and the extension behaves as a standard device extension for sidecars. Load order is tolerant. If the workshop arrives later in the chat, the integration applies from the next workshop turn.

## A. Deictic and Scalar Devices

| Device | Definition | Example |
|---|---|---|
| **speaker position** | The spatial, psychological, or rhetorical place from which the lyric voice speaks. | *"At the end of my suffering / there was a door"* places the speaker after ordeal, not inside it. |
| **addressee position** | The location or role assigned to the poem's "you," whether intimate, public, absent, or imagined. | In *Hell*, *"Friend, I swear to you as one who has returned"* places the addressee as a listener being warned. |
| **apostrophe** | Direct address to an absent person, the dead, an abstraction, or a nonhuman force. | *"O Wild West Wind, thou breath of Autumn's being"* addresses the wind as if it could hear. |
| **first/second/third-person management** | The controlled distribution of *I, you, he, she, they* across the poem. | *J.* moves between *"I wonder," "she later asks me,"* and *"she'd only taken me literally,"* managing distance between self and other. |
| **pronoun shift** | A deliberate change in pronoun base that changes social angle or responsibility. | *Hell* moves from *"everybody"* to *"they live like we do,"* shifting from observation to implication. |
| **tense shift** | A movement from present to past, future, or conditional time that reorients the poem's action. | *Where Once a Small Branch Fell* shifts from present *"travels past"* to past *"was dragged… burned… strangled."* |
| **spatial deixis** | Words such as *here, there, this, that* that locate the poem in near/far space. | Snow Crust's *"in this town"* and Wyatt's *"There is written"* mark where the utterance stands. |
| **temporal deixis** | Words such as *now, then, once, already, still* that locate the poem in near/far time. | *"And nowadays there is two ways"* frames the argument as current custom. |
| **distance-marking demonstratives** | *This, that, these, those* used to mark emotional or physical closeness. | *"So unto those that do oppose / The bundling trade, I say"* holds opponents at rhetorical distance. |
| **scene/report alternation** | A switch between immediate scenic presentation and summary or report. | *"Across a lightless landscape…"* gives scene; *"a thirteen-year-old girl was dragged…"* turns to report. |
| **micro-to-macro scale shift** | A rapid enlargement from a tiny object to a wide social, cosmic, or metaphysical field. | *"To see a World in a Grain of Sand / And a Heaven in a Wild Flower"* expands the tiny into the cosmic. |
| **macro-to-micro compression** | A collapse from a broad field or history into one loaded detail. | The vanished murder site is compressed into *"a small wooden cross / wound round with flowering plastic vines."* |
| **zoom by noun specificity** | A sharpening of scale or attention by choosing increasingly precise nouns. | *"dog-ears, check marks, / underlinings"* in *J.* zooms the reader into exact textual traces. |
| **abstraction spike** | A sudden leap from concrete particulars to a more conceptual or generalized term. | After concrete social annoyances, *Hell* jumps to the abstract verdict: *"Nothing as it is is ever right."* |
| **concretion spike** | A sudden return from abstract language to palpable sensory detail. | *Hell* collapses general dissatisfaction into the bodily want of *"a drink, a cigarette, a cup of coffee."* |
| **synecdoche** | A part stands for the whole, or the whole for a part. | Wyatt's *"her fair neck"* stands in for the whole woman and the power structure attached to her. |
| **metonymy** | An associated object or trace stands in for a person, force, or system. | In *J.*, the *"dog-ears"* and *"marginal notes"* stand in for the absent woman herself. |
| **exemplum** | A brief illustrative case offered to prove a moral, social, or rhetorical point. | Snow Crust uses *"Kate, Nance and Sue proved just and true"* as exemplary cases. |
| **catalog radius** | The breadth of the field a poem covers when it lists people, things, places, or cases. | *Hell* stretches its catalog from Ethiopia to Hiroshima: a wide radius. |
| **witness posture** | A stance in which the speaker presents themselves as one who has seen or can testify. | *"Idling at the crossroads, I can see…"* establishes witness posture before the poem reports the crime. |
| **surveillance posture** | A cooler, observational stance: inspection, monitoring, or scrutiny rather than participation. | In *J.*, the speaker scans *"the taped tear… the dog-ears, check marks"* with the watchfulness of surveillance. |
| **confession posture** | A stance of self-exposure in which the speaker admits implication, weakness, or concealment. | *"I respond in purely literary terms"* is a confession of evasive self-protection. |
| **reportorial stance** | A mode of flat, factual recital that borrows the tone of reporting. | *"raped, burned with matches and strangled with an extension cord"* uses reportorial compression. |
| **ventriloquy** | The speaker takes on another person's or an institution's manner of speech, with or without quotation marks, so that part of the poem is spoken in a borrowed idiom. Distinguish from quotation, which reports another's words, and prosopopoeia, which gives speech to the absent or nonhuman. Restored at v0.2 from Device Inventory Lite. | Micro: *"Your call is important to us," the hospital tells my mother, "please continue to hold," and she holds, the way the hospital taught her to.* The institution's script speaks inside the poem, then sets the terms of the speaker's own sentence. |

## B. Sonic and Prosodic Devices

| Device | Definition | Example |
|---|---|---|
| **meter** | A recurring pattern of measured beats or feet across a line. | Wyatt's *"Whoso list to hunt, I know where is an hind"* moves in a largely iambic pentameter. |
| **accentual pattern** | A pattern organized mainly by counted stresses rather than syllable count. | Blake's *"Tyger Tyger, burning bright"* is felt as a strong stress pattern. |
| **syllabic pattern** | A pattern governed chiefly by syllable count per line. | A haiku's 5-7-5 scaffold is the clearest syllabic pattern. |
| **accentual-syllabic pattern** | A pattern governed by both stress count and syllable count. | Wyatt's sonnet lines depend on both five beats and a roughly ten-syllable span. |
| **free-verse cadence** | Rhythmic motion created by phrasing, syntax, and breath rather than fixed meter. | *"I died & went to Hell & it was nothing like L.A."* moves by speech cadence. |
| **rhyme** | An echo of like or closely related sounds, usually but not only at line ends. | Snow Crust's *"night / right"* gives the argument a memorable rhyme lock. |
| **slant rhyme** | A partial or approximate rhyme; the echo is audible but imperfect. | Dickinson pairs *Room / Storm* for slant-rhyme rather than full closure. |
| **internal rhyme** | Rhyming words placed within a line rather than only at line endings. | Poe's *"Once upon a midnight dreary, while I pondered, weak and weary"* uses internal rhyme in *dreary / weary*. |
| **end rhyme** | Rhyme that lands at the ends of lines. | Snow Crust locks line endings into pairs such as *flight / night*. |
| **pararhyme** | Near-rhyme in which consonants match while vowels shift. | Wilfred Owen's *groined / groaned* illustrate pararhyme's unsettled echo. |
| **alliteration** | Repetition of initial consonant sounds across nearby words. | *"Wild West Wind"* hammers the opening *w*-sound. |
| **assonance** | Repetition of vowel sounds across nearby words. | Poe's *"Hear the mellow wedding bells"* leans on repeating *e*-sounds. |
| **consonance** | Repetition of consonant sounds, especially at end or middle of words. | *"drink, a cigarette, a cup of coffee"* repeats clipped *c/k* sounds. |
| **sibilance** | A concentration of *s, z, sh*, or soft *c* sounds. | Snow Crust's *"sheets sweet and clean / Or sit up all the night"* is thick with sibilance. |
| **euphony** | A comparatively smooth, pleasing, flowing sound texture. | *"between sheets sweet and clean"* is euphonious. |
| **cacophony** | A comparatively harsh, rough, abrasive sound texture. | *"muggings, rapes. / No drooling hoodlums hulking in the doorways"* crowds the mouth with rough sounds. |
| **onomatopoeia** | A word whose sound imitates the sound it names. | Dickinson's *"I heard a Fly buzz—when I died—"* uses *buzz* as onomatopoeia. |
| **refrain** | A line or phrase that returns at intervals. | Poe's repeated *"Nevermore"* is a classic refrain. |
| **repetition** | The deliberate reuse of a word, phrase, structure, or sound for force. | *"No bats shriek overhead. / There are no flames"* in *Hell* begins a chain of repetition around negation. |
| **anaphora** | Repetition at the beginnings of successive lines or clauses. | *"No…"* opening clause after clause in *Hell* is anaphoric pressure. |
| **epistrophe** | Repetition at the ends of successive lines or clauses. | Micro: *"I wake in rain, I walk in rain, I end in rain."* |
| **symploce** | Anaphora and epistrophe combined: repeated beginnings *and* endings. | Micro: *"When I remember, I burn; when I forget, I burn."* |
| **diacope** | Repetition of a word with a small gap between occurrences. | Milton's *"For Lycidas is dead, dead ere his prime"* uses diacope on *dead*. |
| **epizeuxis** | Immediate repetition of a word with no gap. | King Lear's *"Never, never, never, never, never!"* is pure epizeuxis. |
| **caesura** | A marked pause within a line rather than at its end. | *"Because I could not stop for Death— / He kindly stopped for me—"* uses the dash as caesural pause. |
| **enjambment** | The running of syntax over a line break without terminal closure. | Williams's *"The back wings / of the hospital…"* spills sense across the break. |
| **end-stopping** | A line that comes to syntactic rest at its end, often with punctuation. | Wyatt's *"But as for me, alas, I may no more."* is firmly end-stopped. |
| **pause length** | The relative duration and weight of a pause as part of the poem's rhythm. | The full stops in *"No bats shriek overhead. / There are no flames."* make the pauses long and emphatic. |
| **stress clustering** | A packing of strong stresses close together to create pressure. | *"Wild West Wind"* bunches strong stresses. |
| **sonic motif** | A recurring sound pattern that becomes part of the poem's identity. | Snow Crust's recurring *b*-sounds around *bundling, breeches, bind* form a blunt sonic motif. |

## C. Syntactic and Sentence Devices

| Device | Definition | Example |
|---|---|---|
| **parataxis** | Clauses placed side by side without explicit subordination. | *"The wine-cup is smashed. The wine is spilt. The ground is wet."* is clean parataxis. |
| **hypotaxis** | Syntax built through dependency, with subordinate clauses nested. | *"Though I go on pretending nothing beyond that interests me…"* in *J.* is hypotactic thinking. |
| **periodic sentence** | A sentence that delays its main clause until late, making the reader hold pressure. | *"The reminders of her… the phonetic spelling of Russian names… I wonder…"* in *J.* delays the main action. |
| **cumulative sentence** | A sentence that states a base clause and then keeps adding modifiers or extensions. | *"Across a lightless landscape, a passenger train travels past, its eight airless, earth-colored cars…"* grows cumulatively. |
| **list syntax** | Syntax structured as a sequence or inventory rather than a single proposition. | *"dog-ears, check marks, / underlinings (single and double)"* in *J.* is list syntax. |
| **apposition** | A noun or phrase set beside another noun to rename or specify it. | *"the memorial… a small wooden cross"* uses apposition to narrow the image. |
| **subordination** | Use of dependent clauses to rank one action or thought under another. | *"when she later asks me how I liked the book"* subordinates that moment under the larger sentence in *J.* |
| **coordination** | Linking of grammatically equal units with *and, but, or, nor*. | *"raped, burned with matches and strangled with an extension cord"* coordinates horrors without hierarchy. |
| **ellipsis** | The deliberate omission of expected words, links, or explanatory matter. | Many Sappho fragments survive as ellipsis; what is missing becomes pressure of the line. |
| **fragment** | A deliberately incomplete sentence or clause used as a full poetic unit. | *"Nothing of the sort."* in *Hell* is fragment used for emphatic reset. |
| **anacoluthon** | A break in syntactic expectation: the sentence starts one way and swerves into another. | *"I will have such revenges on you both, / That all the world shall—I will do such things"* is anacoluthon under stress. |
| **inversion** | Unusual word order used for emphasis, rhythm, or tonal pressure. | Wyatt's *"where is an hind"* inverts expected prose order. |
| **interruption** | A break in an utterance by another phrase, clause, or self-cutting motion. | The dash in *"That all the world shall—I will do such things"* enacts interruption. |
| **parenthesis** | An inserted phrase that qualifies, narrows, or interrupts the main syntax. | *"underlinings (single and double)"* in *J.* is literal parenthesis. |
| **colon hinge** | A colon used as pivot into list, explanation, specification, or revelation. | *"The reminders of her on the book she left behind: the taped tear…"* turns on a colon hinge. |
| **semicolon braid** | A semicolon holding two parallel but not fully separable units in one braided sentence. | Whitman's *"I celebrate myself, and sing myself; / And what I assume you shall assume"* uses the semicolon as braid. |
| **dash break** | A dash used to cut, suspend, redirect, or sharply qualify. | Dickinson's *"Because I could not stop for Death—"* uses the dash as break and drag. |
| **interrogation** | Question syntax used to probe, pressure, or destabilize the poem. | *"But what if she'd read me incorrectly?"* makes interrogation the closing engine of *J.* |
| **imperative** | Command syntax that tells someone to act, stop, look, or answer. | Snow Crust's *"let me know which way to go"* uses the imperative. |
| **declarative flatness** | A plain statement kept tonally level or unornamented. | *"There are no flames."* in *Hell* is declarative flatness used for deadpan force. |
| **exclamatory charge** | An exclamation whose syntax or punctuation heightens urgency or affect. | *"I'm Nobody! Who are you?"* carries exclamatory charge. |
| **modal qualification** | Use of *may, might, must, would, could, should* to qualify certainty or obligation. | *"more than she might've liked me to"* in *J.* is modal qualification shaped by uncertainty. |
| **recursive sentence growth** | A sentence that keeps feeding new clauses back into its own thought process. | The long central sentence of *J.* keeps unfolding back onto itself rather than concluding cleanly. |
| **parallelism** | The repetition of matching grammatical structures across clauses or phrases. | *"marked and deciphered and underscored"* lines up parallel participles in *J.* |
| **chiasmus** | A crisscross pattern in which terms or structures reverse order. | *"Fair is foul, and foul is fair"* is classic chiasmus. |
| **zeugma** | A single word governing two or more other words at once. | Pope's *"Dost sometimes counsel take — and sometimes tea"* uses one verb across unlike objects. |
| **syllepsis** | A yoking in which the governing word changes sense across the things it governs. | Pope's *"Or stain her honour, or her new brocade"* makes *stain* literal in one case and figurative in the other. |
| **antimetabole** | A reversal repeating words in switched order. | *"Fair is foul, and foul is fair"* also works as compact antimetabole. |
| **anadiplosis** | The repetition of the last word of one clause at the start of the next. | Milton's *"For Lycidas is dead, dead ere his prime"* uses anadiplosis on *dead*. |
| **correctio (epanorthosis)** | A sentence cancels a word it has just used and substitutes a corrected one, performing its own revision mid-utterance. When the cancelled term is the reflex or expected word and the replacement is stranger or more exact, the figure re-describes the familiar and estranges at sentence scale. Distinguish from plain negation: *"there is no kettle"* states an absence; correctio cancels and replaces. | *"The kettle doesn't scream, it hums"* trades the automatic verb for a stranger, truer one; *"not shaking, / they are just unlearned"* runs the move again. |

## D. Figural and Rhetorical Devices

Includes 4 Nôm / English-simulation entries integrated where they fit, marked **[Nôm]** or **[Eng sim]**.

| Device | Definition | Example |
|---|---|---|
| **metaphor** | Says one thing is another, collapsing comparison into identity or transfer. | Wyatt's *"in a net I seek to hold the wind"* makes desire a futile act of capture. |
| **simile** | A comparison explicitly marked by *like* or *as*. | *"like sleep forgetting its body"* is a simile with diagnostic strangeness. |
| **conceit** | An extended, governing comparison that organizes much of a poem's argument or imagery. | Wyatt's whole hunt is a conceit: erotic and political pursuit rendered as deer-chasing. |
| **symbol** | A concrete object that gathers meanings beyond its immediate material presence. | The *"small wooden cross"* in *Where Once a Small Branch Fell* works as memorial symbol. |
| **allegory** | A sustained system in which literal figures and actions belong to a second, conceptual order. | Stevens's *The Comedian as the Letter C* can be read allegorically, the voyage doubling as a drama of mind and making. |
| **personification** | Attribution of human qualities or actions to a nonhuman thing, force, or abstraction. | *"Because I could not stop for Death— / He kindly stopped for me—"* personifies Death as a courteous caller. |
| **prosopopoeia** | Granting speech to an absent, dead, collective, or nonhuman entity. | *"I am the vessel. The river is in me"* gives the river a speaking presence. |
| **pathetic fallacy** | Projection of human feeling onto weather, landscape, or the nonhuman scene. | *"Across a lightless landscape"* lets the scene absorb dread before the crime is named. |
| **irony** | A gap between what is said and what is meant, or between surface claim and actual reality. | *"In a word, the place is perfect"* is ironic because the poem's "perfection" is damnation. |
| **sarcasm** | An openly cutting or mocking form of irony. | *"I died & went to Hell & it was nothing like L.A."* opens in sarcastic social sneer. |
| **parody** | Comic or critical imitation of an inherited form, style, or genre. | *Hell* parodies the traditional inferno by replacing flames with lifestyle complaints. |
| **satire** | Ridicule aimed at exposing social vice, vanity, folly, or hypocrisy. | The complainers of *Hell* are satiric portraits of modern dissatisfaction. |
| **paradox** | An apparent contradiction that reveals a deeper truth. | *"A terrible beauty is born"* is paradox in compact form. |
| **oxymoron** | A compressed pairing of apparently contradictory terms. | *"terrible beauty"* is oxymoron. |
| **litotes** | Understatement that makes a point by denying its opposite. | Micro: *"no small grief"* means great grief by negation. |
| **hyperbole** | Deliberate exaggeration for emphasis, scale, or tonal force. | *Hell* escalates through *"Dachau… Hiroshima"*, hyperbolic comparative scale. |
| **understatement** | Deliberate downplaying of what is actually large, grave, or intense. | *"The crossing less eventful than one might have guessed"* understates death itself. |
| **allusion** | A reference that points beyond the poem to another text, figure, or cultural scene. | Wyatt's *"Noli me tangere"* alludes to the Vulgate gospel phrase. |
| **quotation** | The insertion of another utterance as quoted speech or cited language. | The quoted inscription in Wyatt, *"Noli me tangere…"*, is quotation as structure, not ornament. |
| **citation-as-device** | The use of imported wording, title, source language, or documentary phrasing as active poetic mechanism. | In Wyatt, the Latin tag acts as authority, interdiction, and social citation simultaneously. |
| **metalepsis** | A leap across figurative or narrative levels through a chain of substitutions or crossed frames. | In *J.*, marks on the book become marks on the self: *"I too have been marked and deciphered."* |
| **catachresis** | A strained, impossible, or misapplied metaphor that creates force by impropriety. | *"in a net I seek to hold the wind"* is catachrestic because wind cannot literally be netted. |
| **antithesis** | A sharp placing of opposites in balanced proximity. | Wyatt's *"wild for to hold, though I seem tame"* works by antithesis. |
| **periphrasis** | A roundabout or circumlocutory way of naming something instead of naming it directly. | *"The gentleman who'll ferry you across"* is periphrasis for Charon-like passage into death. |
| **euphemism** | A softer or more socially acceptable term used in place of a harder one. | Snow Crust's *"bundling"* euphemizes erotic or sexual proximity. |
| **dysphemism** | A deliberately harsh, degrading, or offensively blunt term. | Snow Crust's *"whore"* and *"strumpet"* are dysphemistic labels. |
| **diction altitude** | The level of formality at which the speaker's word choice sits: low (slang, profanity, blunt body words), middle (the plain diction of errands and requests, which readers do not notice), or high (Latinate, periphrastic, ornamented, or clinically detached). A setting every span has; see `13-speaker-dials`, sd-01. | Micro: *it rained*, *precipitation was recorded*, *it pissed down* carry one fact at middle, clinical high, and low. |
| **altitude shift** | A located change of diction altitude inside a passage. A single middle-altitude sentence inside a high passage, or the reverse, often marks the passage's active site. | Micro: *"The vesper light dissolves along the estuary's pewter rim. I'm cold."* drops from ornamental high to middle in two words. |
| **in-group idiom** | A phrase whose sense or tone depends on membership in a group, trade, region, generation, or online community, so that it binds readers inside the group and marks readers outside it. Check for tonal laundering and gating when it carries cost. | Micro: a line cook's *"eighty-six the soup"* places the speaker in a kitchen before any noun does. |
| **[Nôm] semantic-phonetic dissonance** | A written form's semantic element and sound element pull in different conceptual directions. | Imagining *"longing"* written with an *"insect"* or *"disease"* radical, infecting the word visually. |
| **[Eng sim] parenthetical ghost** | A simulated radical built inside an English word so one word is read through another hidden one. | *"mem(ache)ory"* and *"un(found)erstand"* create dual readings inside a single word. |
| **[Nôm] scriptal ghosting** | A switch between prestige script and vernacular script producing class, cultural, or psychic friction. | The slide between Hán and Nôm is scriptal ghosting, rupture from official to intimate language. |
| **[Eng sim] etymological stratification** | A collision of Latinate prestige diction with Anglo-Saxon, slang, or glitched vernacular. | *"The pulmonary system stutters (glitch/ing) in its sanctuary"* stages register friction as English analogue. |

## E. Structural and Compositional Devices

| Device | Definition | Example |
|---|---|---|
| **title as frame** | A title that actively conditions how the poem is read before the first line. | The title *Hell* frames every later detail as infernal. |
| **epigraph** | A prefatory quotation or statement that sets pressure, key, or argument. | An epigraph such as a biblical or Dantean tag pre-loads the poem with borrowed authority. |
| **dedication/note as pressure field** | A dedication, note, subtitle, or prefatory label that changes the ethical or historical stakes. | *"New England Broadside / in Defence of Bundling, c. 1786"* is not neutral metadata; it pressures how Snow Crust is heard. |
| **stanza system** | The recurring pattern by which a poem divides itself into stanzaic units. | Snow Crust's repeated short stanzas make the poem feel like a public argument built in manageable blocks. |
| **couplet** | A two-line unit, usually but not always rhymed. | *"Perhaps there's more got on the floor / Than any other way"* lands as a compact closing couplet. |
| **tercet** | A three-line stanza or structural unit. | Terza rima builds by chained tercets; the unit's three-line turn is the signature pressure. |
| **quatrain** | A four-line stanza or structural unit. | Snow Crust moves in quatrain-like units, especially in its opening argument blocks. |
| **sonnet architecture** | The overall 14-line design, including internal turn and rhetorical segmentation. | Wyatt's *Whoso list to hunt* is shaped by sonnet architecture: pursuit, exhaustion, warning, inscription. |
| **ballad architecture** | Stanzaic and narrative song-structure built for public memory, repetition, and forward motion. | Snow Crust's quatrains, rhyme, and communal argument give it strong ballad architecture. |
| **prose poem block** | A poem presented as a paragraph-like block rather than as visibly broken lines. | *J.* operates as a prose-poem block: one visual paragraph carrying intense lyric pressure. |
| **section break** | A visible division between parts of a poem. | A section break lets a long poem reset pressure without pretending continuity is unbroken. |
| **serial sequence** | A poem or group of poems designed as linked installments rather than one sealed unit. | A sonnet sequence such as *Astrophil and Stella* works by serial accumulation. |
| **refrain architecture** | A whole design built around the return of one or more repeated lines. | Poe's *"Nevermore"* works as refrain that becomes architecture of the whole poem. |
| **turn / volta** | The structural pivot where the poem changes direction in thought, tone, or argument. | Wyatt turns sharply at *"Who list her hunt, I put him out of doubt."* |
| **hinge line** | The exact line on which a poem swings from one phase to another. | In *J.*, *"But what if she'd read me incorrectly?"* functions as hinge line. |
| **braid** | A structure that interweaves two or more strands rather than presenting them sequentially. | *Where Once a Small Branch Fell* braids present observation, childhood memory, and atrocity report. |
| **montage** | A composition built by jump-cut juxtaposition of scenes, images, or frames. | *Hell* jumps from Ethiopia to Dachau to Hiroshima in a montage of catastrophe sites. |
| **collage** | An assemblage of heterogeneous materials, tones, or found fragments. | *J.* behaves like a light collage of torn jacket, notes, check marks, private inference. |
| **fragment chain** | A sequence of broken or partial units whose linkage matters as much as their incompletion. | Eigner fragments work by fragment chain: one shard leaning on the next. |
| **frame narrative** | An outer narrative situation that encloses or presents another scene, report, or remembered event. | The crossroads and passing train in *Where Once a Small Branch Fell* frame the inner crime narrative. |
| **inventory poem** | A poem organized chiefly by enumeration of objects, traces, or entries. | *J.* is an inventory poem of textual reminders. |
| **monologue** | A poem driven by one dominant speaking voice addressing someone or speaking outward. | *Hell* is a satirical monologue delivered by a single returned witness. |
| **dialogue** | A poem structured through exchange between voices, or through strongly implied back-and-forth. | Dickinson's *"I'm Nobody! Who are you?"* opens a dialogue rather than a sealed soliloquy. |
| **documentary insert** | A factual, quoted, bureaucratic, or archival element inserted into lyric texture. | The quoted phrase *"crime scene"* in *Where Once a Small Branch Fell* works as documentary insert. |
| **citation cluster** | A grouped run of names, references, or cited materials that thickens the poem's field. | *"Ethiopia… Bangladesh… Bogotá… Dachau… Hiroshima"* forms a citation cluster in *Hell*. |
| **recursion** | A structure that loops back on its own operation, making the poem re-enact its own premise. | *J.* is recursive because reading the book becomes the speaker's being read in turn. |
| **circular closure** | An ending that returns the poem to its starting image, phrase, or structural position. | A villanelle's last line often returns the opening line, circular closure by design. |
| **open ending** | An ending that leaves its question, pressure, or argument unresolved. | *"Or worse, what if all along she'd only taken me literally…?"* leaves *J.* radically open. |
| **asymmetrical closure** | An ending that settles one line of movement while leaving another stubbornly unclosed. | *Where Once a Small Branch Fell* closes the scene of the vanished memorial without closing the ethical wound. |
| **mirrored structure** | A design in which later sections echo, reverse, or answer earlier sections. | *Hell* mirrors itself by first listing what Hell is not, then unveiling what Hell is. |
| **assertion placement** | The position of a poem's governing assertion, the one general sentence its particulars are read under: opening, middle, near the close, last line, or absent. Each position does different work, and a cliché fails in all of them. Run the kernel's open-or-corner test before crediting the assertion. | Micro: *"Every kitchen keeps a record."* placed last, after a stained counter, a burnt pot, and a child's heights penciled on a door frame, gathers the objects into one claim; placed first, it obliges them to complicate it. |

## F. Visual and Typographic Devices

Includes 5 Nôm / English-simulation / wildcard entries integrated where they fit.

| Device | Definition | Example |
|---|---|---|
| **line length policy** | The governing decision about whether lines stay short, long, variable, or strategically patterned. | *Hell* favors long, talky lines; line length policy supports conversational satire. |
| **ragged-right field** | A lineated page in which the right margin remains uneven. | Most lineated lyric pages, including Wyatt and *Hell*, create a ragged-right field. |
| **justified block** | A poem shaped visually like a prose paragraph, flush on both sides or block-like. | The Santos notes treat the prose-poem block as a justified field whose visual control masks interior fracture. |
| **indentation** | The deliberate insetting of lines to mark relation, hierarchy, echo, or pause. | Indented returns in shaped or open-field poems visually subordinate or answer the line above. |
| **staggered spacing** | A layout that shifts lines or words horizontally so the page becomes part of the timing mechanism. | Eigner fragments use staggered spacing to make vision and motor delay visible. |
| **white space as time** | Blank space functioning as pause, lag, suspension, or unsaid duration. | In Eigner-style open field, the blank between words or lines is felt as time, not emptiness. |
| **capitalization pattern** | A systematic choice about what gets capitalized and what does not. | Dickinson's recurrent noun-capitals, *Death, Carriage, Immortality*, make capitalization expressive. |
| **italics** | Slanted type used to mark emphasis, quotation, foreignness, or tonal drift. | A poem italicizing one word, say *not*, shifts pressure without changing syntax. |
| **block capitals** | All-caps typography used for emphasis, signage, command, inscription, or noise. | A broadside printing NO or STOP in capitals uses block capitals as visual shout. |
| **numbering** | Visible numbers used to order sections, entries, fragments, or serial units. | Numbered lyrics announce sequence and invite the reader to notice order as part of form. |
| **section labels** | Named or marked divisions such as *I, II, III* or titled subsections. | Section labels in a long poem create frames before the local lines work. |
| **isolated line** | A line visually set apart from surrounding material so it lands with extra weight. | *"Nothing as it is is ever right"* gains force when visually isolated. |
| **concrete/shape arrangement** | A layout in which the visual shape of the text participates directly in meaning. | A stacked glyph arrangement turns the word into a visible object instead of a normal line. |
| **page-silence ratio** | The proportion between printed matter and blank page, treated as a meaningful formal variable. | An Eigner fragment with only a few words on the page has very high page-silence ratio. |
| **typographic jump-cut** | A sudden visual shift in spacing, font treatment, emphasis, or layout, like a cut in film editing. | Bidart's typographic jump-cuts name this device directly. |
| **[Nôm] visual radical coupling / graphemic rhyme** | Visual linkage created when different words share a visible component or radical even if they do not sound alike. | A couplet linked by a repeated *heart* radical: the rhyme lives in ink, not in sound. |
| **[Eng sim] typographic constancy / anchor character** | A repeated letter, symbol, or visual mark acting like a radical across unrelated words. | *"e(x)it, fi(x)ation, te(x)t, ple(x)us"* uses the recurring *x* as anchor character. |
| **[Nôm] ideographic compression** | The packing of dense semantic content into one compact visual sign. | A character carrying *"the sound of wind through a specific type of tree"* describes ideographic compression. |
| **[Eng sim] vertical compaction / glyph logic** | English arrangement that stacks letters or clusters a word spatially so it must be scanned as an object. | A stacked W / H O / R E arrangement forces simultaneous decoding rather than left-to-right reading. |
| **[Wildcard] kinetic erasure / phantom strike-through** | A visible cancellation that leaves the cancelled wording legible, deletion and persistence in the same instant. | *"~~I love you~~ I need you"* makes erasure itself part of the poem's live surface. |

## G. Pragmatic and Ethical Devices

| Device | Definition | Example |
|---|---|---|
| **withholding** | The deliberate refusal to state something the poem clearly knows or circles around. | *J.* withholds the full history of the relationship and lets the annotations carry the burden. |
| **erasure** | A removal, disappearance, or deletion that becomes part of the poem's meaning. | In *Where Once a Small Branch Fell*, the memorial *"disappeared as well,"* making erasure part of the poem's wound. |
| **omission** | A meaningful leaving-out of context, motive, identity, or explanation. | The murdered-girl poem omits the perpetrator's identity and any consoling explanation. |
| **implication** | Meaning conveyed indirectly, by suggestion or pressure rather than explicit statement. | In *J.*, the marked-up book implies intimacy long before the speaker confesses any discomfort. |
| **self-implication** | A move by which the speaker reveals their own complicity in what is being described or judged. | *Hell* turns outward critique inward with *"they live like we do,"* implicating speaker and reader alike. |
| **plausible deniability** | Language arranged so the speaker can retreat from or disown the very implication the poem creates. | *"I respond in purely literary terms"* gives the speaker of *J.* plausible deniability. |
| **credibility management** | Techniques by which the poem tries to establish, preserve, or recover trust in its voice. | The specific nouns and local details of *Where Once a Small Branch Fell* manage credibility by sounding witnessed. |
| **witness claim** | An explicit or implicit assertion that the speaker can testify to what occurred. | *"Friend, I swear to you as one who has returned"* is a direct witness claim. |
| **appropriation risk** | The danger that the poem uses another person's suffering as aesthetic material without sufficient ethical grounding. | Any poem recounting the murdered girl in *Where Once a Small Branch Fell* carries appropriation risk as part of its form. |
| **voyeurism risk** | The danger that the poem turns looking into intrusive or consuming spectacle. | In *J.*, the speaker's scrutiny of *"dog-ears, check marks, / underlinings"* risks voyeuristic reading of another person's traces. |
| **moral evasion** | A maneuver by which the poem dodges the full ethical burden of what it names or does. | Snow Crust's defense of *"bundling"* slides toward moral evasion when it rationalizes harm by custom. |
| **tonal laundering** | A smoothing or brightening of tone that makes ugly matter easier to accept than it should be. | *Hell* risks tonal laundering when catastrophe names are folded into polished comic wit. |
| **sayability test** | A probe asking whether the poem's words can be spoken aloud responsibly and still bear their claimed weight. | The assault line in *Where Once a Small Branch Fell* triggers the sayability test immediately. |
| **reader activation** | A device by which the poem forces the reader to infer, complete, judge, or supply missing links. | *"But what if she'd read me incorrectly?"* activates the reader because the answer is withheld. |
| **crawl-space aperture** | The width of the poem's psychic opening: how much side-pressure, hidden resonance, or interior drift it creates. | The closing fear of being *"taken… literally"* in *J.* leaves a wide crawl-space aperture. |
| **Coscienza compliance** | The degree to which a poem seems aware of the truth or method it is producing rather than stumbling into it. | *J.* shows strong Coscienza compliance because it knows reading itself is the danger it is staging. |
| **CODIT sealing behavior** | A poem's attempt to wall off damage locally, ring it, and keep fracture from spreading across the whole system. The device-scale instance of a Wall 4 barrier zone; the Compartmentalization Engine module reads it at poem scale and adds the default-wall versus barrier-zone distinction. | *"purely literary terms"* in *J.* is a CODIT-style seal placed over a much messier emotional breach. |
| **acausal rupture** | A break that arrives like an event rather than a smoothly prepared explanation, opening a truth the poem cannot fully govern. | Snow Crust's *"Perhaps there's more got on the floor / Than any other way"* ruptures its own argument and becomes accidental ars poetica. |
| **embodied attention quality** | The degree to which the poem evidences released attention (Alexander-released, breath-coordinated, somatic-disciplined) versus habituated constriction (jaw-clenched, breath-held, postural-locked) in its compositional surface. Cross-references Section H's Sheets-Johnstone embodied-cognition grounding. | Bishop's *The Moose* shows released attention: breath-coordinated long-line patience, the body present and unforced in the observation; Stevens's *The Comedian as the Letter C* shows compositional seizure: formal upholstery operating as overcompensation for body-absence. |
| **affect-content carrying capacity** | The degree to which a work holds incompatible emotional registers (uplift carrying grief, bounciness carrying loss, brightness carrying weight) without resolving the incompatibility into a single dominant register. The device fires when the work's surface affect and underlying content remain genuinely doubled rather than collapsed. Distinguished from tonal laundering (which smooths ugly content with brighter tone, evasively) by the work's awareness of the doubling and its refusal to resolve it. The pop song does this routinely; serious poetry does it more rarely and often with worse results, since the temptation to resolve the tension kills the operation. | Bishop's *One Art*: the villanelle's playful formal lightness held against escalating losses culminating in the loss of "you," with the parenthetical *"(Write it!)"* marking the structural seam where the doubling becomes visible. Lynne-Edmunds's *Slipping Away*: bouncy 1983 pop production held against present-continuous attrition under conscious witness. |
| **phatic gesture** | A phrase that carries no information about the subject and works on the contact between speaker and listener: a tag, an aside, a hedge addressed to the listener, a rhetorical question, a check-in. It can place the reader as a confidant, or warm the reader toward material the poem then avoids; name the action before judging it. Check for tonal laundering when it sits next to cost. | Micro: *"The garage, you know the one, burned down in May, anyway, that's where I learned to drive."* Two gestures hold the listener while the fire goes by unexamined. |

## H. The Hermetic / Alchemical Subcluster

### The Older Sense of Hermetic

Strictly speaking, a hermetic seal does not guarantee transformation. Electronics, archives, and food are hermetically sealed every day with no occult drama attached. In the older Hermetic or alchemical imagination, the lineage running from Hermes Trismegistus through medieval and early-modern alchemy, the sealed vessel strongly implied that some hidden operation was underway. The alembic itself had three functional parts: a containing vessel below, a head or cap at the top, and a receiver for the distillate. The hermetic seal kept outside matter out *and* volatile spirit in while heat, distillation, or sublimation altered the contents. That is the older sense of *hermetic*: it implies an operation, not only an airtight boundary. Something is cooking in there.

In the private core, Rother's use of *hermetic* fits this older sense rather than the modern reduction to *obscure*. The extension keeps the older sense as its operating definition and does not depend on the private-core attribution. A hermetic poem is closed to the reader and also signals that some operation is underway inside the chamber, so that what enters and what leaves are not the same substance. This is the lens that earns Section H its place in the inventory. It is a re-sort of the existing device categories by what they *do* in the chamber rather than a metaphor pasted on.

### The Four Functional Categories

The inventory's ~183 devices can be re-tagged by primary alchemical function. Most devices fall into one of four roles. Some are dual-function (a parenthesis is both a contained chamber and a valve); the tagging that follows assigns each device to its dominant role. A handful are neither vessel, seal, valve, nor transmuter; they are positional, locating, or meta-diagnostic. Those are tagged ∅ and counted separately.

- **Vessels (V)**: frame-builders and chambers. Primary job: containment. A vessel device defines the boundary inside which the poem's language is held under pressure. Without the vessel, there is no chamber to operate in.
- **Seals (S)**: closures and anti-leak devices. Primary job: shutting. A seal device prevents leakage of meaning, ethical content, or affective material from the chamber. A reader's first impression of *hermetic-as-airtight* is a perception of seal density.
- **Valves (Va)**: controlled apertures. Primary job: regulated opening. A valve device permits some matter to pass while holding the rest under pressure. Valves let the chamber breathe without losing its contents. The mid-line caesura, the dash break, the colon hinge.
- **Transmuters (T)**: retorts and crucibles. Primary job: alteration. A transmuter device changes the material inside the chamber: meaning shifts, register modulates, voice transforms. Metaphor is the canonical transmuter; so are pronoun shift, scale shift, scriptal ghosting, recursion.

### Fresh Tag-Pass Count

Tagging each of the 183 devices by dominant primary function, counting once per device:

| Section | V | S | Va | T | ∅ | Total |
|---|---|---|---|---|---|---|
| A. Deictic & Scalar | 2 | 3 | 2 | 10 | 6 | 23 |
| B. Sonic & Prosodic | 4 | 6 | 4 | 1 | 15 | 30 |
| C. Syntactic & Sentence | 9 | 2 | 9 | 9 | 1 | 30 |
| D. Figural & Rhetorical | 8 | 1 | 4 | 17 | 0 | 30 |
| E. Structural & Compositional | 20 | 2 | 4 | 4 | 0 | 30 |
| F. Visual & Typographic | 14 | 0 | 4 | 2 | 0 | 20 |
| G. Pragmatic & Ethical | 0 | 8 | 8 | 0 | 4 | 20 |
| **Totals** | **57** | **22** | **35** | **43** | **26** | **183** |

Cross-category aggregations:

- **Strict containment core (V + S)**: 79 devices
- **Containment + aperture system (V + S + Va)**: 114 devices
- **Broad alchemical family (V + S + T)**, matching the prior count methodology: 122 devices
- **Full alchemical inventory (V + S + Va + T)**: 157 devices
- **No alchemical role (∅)**: 26 devices, positional, locating, or meta-diagnostic only

### Methodology Note And Variance From Prior Count

The previous tag-pass reported 37 V / 22 S / 39 T = 98 broad. This pass: 57 V / 22 S / 43 T = 122 broad. Differences:

- **Seals match exactly** (22 = 22). The seal category is stable across methodologies because the devices it contains are sharp-edged and easy to identify.
- **Vessels diverge** (57 vs. 37). This pass tagged structural devices (titles, stanza systems, frame narratives, monologues, dialogues, sonnet architecture, etc.) and figural devices (symbol, allegory, paradox, oxymoron, antithesis) more inclusively as V. The prior pass appears to have reserved V for the most prototypical frame-builders and counted figural containment-effect devices as T (transmuters operating on contained material).
- **Transmuters track close** (43 vs. 39). Both passes agree on the dominant-T figural inventory; small variation in scale-shift and recursion treatment.
- **Valves**: not separately counted in the prior pass. They appear here as a distinct 35-device category, broken out because the controlled-aperture function is genuinely different from both sealing and transmuting, and because the seal-versus-valve distinction is exactly where the ethical diagnosis lives (see below).

Neither tag-pass is wrong; they apply different criteria. The current pass uses *primary function in the alchemical chamber* as the tag. The prior pass appears to have used *role in the poem's overall economy*, which allows a figural device whose effect is to transform meaning to be tagged T even if it locally functions as containment.

The honest finding: more than half the inventory has a primary alchemical function. 157 of 183 (≈86%) if all four categories are counted; 122 of 183 (≈67%) if valves are excluded under prior-pass methodology. The Hermetic lens is not a niche; it is the largest single re-sort the inventory supports.

### Embodied-Cognition Grounding

The alchemical re-sort risks sounding occult or merely metaphorical. It does not need to. Sheets-Johnstone's work on the primacy of movement and the kinesthetic generation of concepts grounds it. If concepts arise from the living body and tactile-kinesthetic experience, then the categories the re-sort runs on, *edge, inside / outside, pressure, enclosure, opening, release, residue*, are not metaphors imported from chemistry into literary criticism. They are body-born semantic habits that predate both alchemy and poetry. Alchemy borrowed the categories from the body; the inventory's seven bins already deploy them implicitly; Section H makes the borrowing visible.

(Sheets-Johnstone's argument, compressed: the conceptual touchstones behind major hominid inventions did not come from greater intelligence or more sophisticated consciousness but from new ways of thinking generated in tactile-kinesthetic experience. From teeth, the concepts of edge and of flaking one stone with another anchored stone-tool making; from vocalizations, the concept of oneself as a sound-maker anchored spoken language; from (the ending of) animation, the concept of punctuated existence anchored a belief in death. Each concept arose in the animate, sensorily felt and feeling body, which she treats as the semantic template and cognitive source of the fundamental human concepts and the standard on which each new practice was forged. Redaction note: the long source passage is withheld as copyrighted scholarly text beyond the kernel source-exposure levels. The retained mechanism is the claim that edge, enclosure, pressure, opening, and release are body-born semantic habits rather than metaphors imported from chemistry. Full source belongs in a separate appendix with a permission basis.)

That gives the alchemical re-sort real ground under it. *Hermetic* in the older sense names something specific the body already knows: a chamber under pressure in which what enters changes state before it leaves. Diagnostic reading is the procedure by which that change of state is tracked.

### Operations Added by the Re-Sort

Three operations the alphabetical inventory cannot perform that the Hermetic re-sort can:

1. **Reveals containment density.** A poem with high V + S count and low Va is a tight chamber under sealed pressure (Wyatt, Dickinson). A poem with high V and high Va is a chamber with controlled venting (Eigner, Williams). A poem with high T and thin V / S is a transmuting machine without much chamber to hold the transmutation (parts of Pound, some Ashbery). Density is diagnostic; the re-sort makes it measurable.

2. **Locates where the cooking happens.** Transmuter devices are the working retorts of the poem. Identifying them shows the reader *where in the poem the change of state occurs*. A reading that catalogs V and S without naming T will report the chamber and miss the reaction. Section H makes the reaction findable.

3. **Surfaces seal-versus-leak ethics.** Many devices in G (Pragmatic and Ethical) are seals: *plausible deniability, credibility management, moral evasion, tonal laundering, CODIT sealing behavior*. Many others are valves: *erasure, appropriation risk, voyeurism risk, acausal rupture, reader activation*. The ethics of a poem live precisely at the seal-versus-valve seam: what the chamber prevents from leaking, and what it permits to escape under controlled conditions. The Hermetic lens makes ethical diagnosis structural rather than gestural.

### Procedural Prompt

When loading the Hermetic lens for a specimen, the apparatus asks:

> *Identify the chamber. What V devices define it? What S devices close it? What Va devices regulate its breathing? What T devices are running inside it? What is the chamber producing as output that it did not contain at input?*

The last question is the alchemical question proper. If the poem is operating, what enters and what exits should differ. If they do not differ, the chamber is sealed but not cooking, a hermetic *seal* without a hermetic *operation*. That is the failure mode the older sense of *hermetic* warned against: airtight prose pretending to be transformation.

### Sibling Lens: Compartmentalization Engine Reading

A second containment lens sits beside this one, in its own module: the device-scale view of the Compartmentalization Engine, after Shigo's tree-pathology model. It shares the containment family and asks a different question. The Chamber Reading asks what transforms inside the sealed vessel; the Compartmentalization Engine Reading asks what the poem walled off and abandoned to survive, and what the wall cost. The tell that they are distinct: a seal that holds and abandons its decayed core is a failure in the Chamber Reading and the system working in the other one. The engine requires no transformation at all.

At device scale the engine reads which devices in this inventory function as walls. It uses the same Seal and Valve tags from the count above, and adds one distinction this section does not draw: a seal can be a default wall, structural and present before the wound, or a barrier zone, reactive and formed after the wound to confine it. The `CODIT sealing behavior` device in Section G is the local instance of a barrier zone. The full apparatus, the trigger and non-trigger conditions, and the poem-scale engine for Engine Bay live in the Compartmentalization Engine module. Both lenses stay opt-in and fire only on structural warrant; neither is a richer name for any closed form.

## I. Corpus for Training and Stress-Testing

### Required Core Corpus

1. **Anonymous, *The Whore on the Snow Crust***  
   Use for: communal argument, folk-rhyme propulsion, accidental ars poetica, productive glitch.

2. **Sir Thomas Wyatt the Elder, *Whoso List to Hunt***  
   Use for: pursuit grammar, sonnet constraint, inscriptional interdiction, controlled volta.

3. **Sherod Santos, *J.***  
   Use for: metonymic evidence, reader-reversal, withholding, book-object framing.

4. **Sherod Santos, *Where Once a Small Branch Fell***  
   Use for: witness framing, scenic scan, atrocity insertion, ethical fracture.

5. **Steve Kowit, *Hell***  
   Use for: satirical monologue, catalog escalation, tonal inversion, moral overflight risk.

### Expansion / Contrast Corpus

6. **George Oppen, *Psalm***  
   Use as positive control for: discrete naming, anti-laundered attention, object fidelity.

7. **Larry Eigner, selected short poems / fragments**  
   Use for: typographic pacing, somatic interruption, open-field timing, visible motor system.

8. **Wallace Stevens, *The Comedian as the Letter C***  
   Use as negative control for: abstraction drift, high formal upholstery, laundering by amplitude.

9. **Philip Larkin, *The Building***  
   Use for: institutional framing, deep social depth-field, plain diction under mortal pressure.

10. **Frank Bidart, *Another Life***  
    Use for: montage, typographic jump-cuts, public / private overlap, self-fracturing long sentence.

### Corpus Rationale

It gives controlled variation in:

- stanzaic tightness vs. open field
- single-speaker clarity vs. fractured voicing
- public rhetoric vs. private notation
- object-fidelity vs. abstraction laundering
- ethical witness vs. ethical overreach
- smooth throughput vs. somatic interruption
- closure by lock vs. closure by bleed

## J. High-Value Device Clusters by Specimen

Devices most worth tracking in each corpus poem when stress-testing the inventory:

| Poem | High-Value Device Cluster |
|---|---|
| ***Snow Crust*** | folk rhyme, communal defense, rhetorical question, proverbial closure, accidental self-reflexivity |
| ***Wyatt*** | sonnet, hunting conceit, quoted inscription, paradox, volta, courtly interdiction |
| ***J.*** | inventory, metonymy, withheld confession, recursive question, reader / reader reversal |
| ***Where Once a Small Branch Fell*** | scenic frame, tonal pivot, documentary detail, witness posture, memorial logic |
| ***Hell*** | inversion, satirical catalog, colloquial cadence, list engine, anticlimactic revelation |
| ***Psalm*** | concrete nouns, broken syntax, restraint, anti-expansive focus, stillness |
| ***Eigner fragments*** | spacing, white-space timing, fragment, open field, typographic somatics |
| ***Stevens*** | periodic syntax, abstraction, periphrasis, rhetorical flourish, conceptual drift |
| ***The Building*** | descriptive sweep, late disclosure, institutional architecture, social survey, mortality compression |
| ***Another Life*** | montage, voice shift, typographic emphasis, memory braid, cinematic sequencing translated into syntax |

## K. Scan Mode: Device-Driven Specimen Fetch

Guard, added at v0.2. This section predates kernel v0.3.10, which removed specimen retrieval from the apparatus and changed Scan Mode's Source B from retrieved workshop uploads to operator-supplied corpora. Until the section is rewritten, read Source B as an operator-supplied corpus and `Scan feedback` as `Scan supplied`. The venue list, the fetch budget, the recency default, body-only fetching, and the budget-exhausted outcome do not run. Specimen integrity, deanonymization refusal, and the Source B bias flag still apply, the last rescoped to selection bias in what the operator supplies. Where this section and the kernel disagree on retrieval, the kernel governs, whatever the extension precedence order would otherwise say.

A device-driven operating mode for tuning the inventory outward toward specimens. The user names a source, a Category, and device(s); the apparatus locates a candidate poem from the named source, verifies the device is present in the text, reports provenance and the source-appropriate epistemic rating, then runs a full sidecar against the catch. Triggered by the keyword `Scan` followed by an explicit source flag.

### Two-Source Operation

Scan mode operates against exactly two sources, positioned at opposite ends of the over-read / under-read spectrum. The middle zone (curated-but-not-canonical contemporary publication, journal selections, MFA chapbooks, Poetry Foundation feature pages) is excluded by design. That middle zone is where apparatus confabulation is hardest to detect: enough training-data signal to produce plausible readings, not enough to ground them, and editorial smoothing without canonical density to mark the smoothing. Operating only at the extremes keeps each mode's failure pattern visible and lets the user calibrate against the source's known biases rather than against an unmarked blend.

- **Source A, Canon.** Read-to-death canonical work. The apparatus identifies a canonical specimen that carries the named device and names its provenance: author, title, and a standard reference, so the user can reach the actual text. Algorithmic Reconstitution applies here as a diagnostic flag, not as a license to output reconstructed text. Reconstruction-strength rating is mandatory, and the consensus-smoothing flag fires when the sidecar is producing averaged interpretation drawn from the corpus of existing readings rather than fresh apparatus engagement. The scan does not reproduce the full poem. For copyrighted canonical work it verifies the device with a pressure quote and cites the source; full text appears only when the work is public domain and the kernel Level 4 conditions hold.
- **Source B, Feedback.** Original composed poetry uploaded by authors to venues where the act of posting is a request for critique. Defining property: the poem is in workshop-state, not publication-state, and the author has invited analytical engagement. Primary venues: r/OCPoetry (feedback required by subreddit rule), r/poetry_critics, r/poetasters, r/justpoetry, r/Poem, r/Poems, r/OCPoetryFree, r/PoetryWorkshop, Allpoetry workshop sections, Hellopoetry critique threads, analogous workshop-state forums. **Excluded from Source B**: author websites, Substack publications, journal pages, curated venues, anywhere the upload is publication-state rather than workshop-state. The apparatus produces uninvited critique only on work whose author has explicitly invited it.

**Source B scan procedure:** choose one recent poem from the allowed workshop venues; fetch only post title, author handle, posting date, and poem body; do not fetch comments; stop after ten fetches if no suitable poem is found; then run the standard scan output below. The output uses the default register and claims no named voice. A Kowit-voiced workshop reading requires the Kowit voice module or a plugin that supplies it to be loaded, otherwise it fails Checkpoint 7 as voice drift. Do not substitute poems from blogs, Substack, magazines, or non-listed sites.

**Source exposure in scan mode.** Scan mode inherits the kernel Source Policy and Checkpoint 5, Source Exposure. It reports provenance, a device-verification pressure quote, and the diagnostic sidecar. It does not reproduce the full posted poem. Posting to a workshop venue invites critique, which is the warrant for reading and quoting under the source-exposure levels; it is not a license to reproduce the whole work in full. The handle, venue, posting date, and URL let the user open the original. Full reproduction is reserved for public-domain work under Level 4 conditions and does not apply to live workshop posts.

### Terminology

- **Category**: a top-level grouping of devices in the extended inventory. Categories A through H. Each Category collects devices that share a structural domain (deictic/scalar, sonic/prosodic, etc.).
- **Device**: a named operation within a Category. The inventory contains 189 devices total across the Categories, from v0.2.
- **Source flag**: `canon` or `feedback`, required on every fetch-bearing scan. List commands do not require a source flag (Categories and devices are source-agnostic).

### Trigger Grammar

- `Scan canon {Category} for {device}`: Source A, single device, single Category
- `Scan feedback {Category} for {device}`: Source B, single device, single Category
- `Scan {source} {Category} for {device1} and {device2}`: multi-device, same Category, same source (conjunctive AND by default)
- `Scan {source} {Category1} for {device1}, {Category2} for {device2}`: multi-Category, same source
- `Scan list categories` (also `Scan list cat`, `Scan list cats`): Category catalog (no source flag)
- `Scan list {Category} devices`: device catalog (no source flag)

The source flag is required on every fetch-bearing scan. The apparatus does not assume a default and does not silently substitute one source for the other; if the source flag is omitted the apparatus asks before scanning. Variants accepted on the source flag: `canon` / `canonical`, `feedback` / `workshop` / `draft`. Cross-source scans (`Scan canon A for apostrophe, feedback B for caesura`) are not supported. One source per scan keeps the provenance discipline clean. Category and device names accept variants as before. Case-insensitive throughout.
Category names accept variants: section letter, short name, or full name (`A` / `Deictic` / `Deictic and Scalar`). Device names accept reasonable variants on the listed name. Case-insensitive throughout. This is a natural-language tuning interface, not a strict-syntax one, so the apparatus parses intent rather than enforcing form.

### Output Form For A Scan Catch

The two sources produce different provenance patterns. The structure of the sidecar (Kernel Sidecar Format reading) is identical across sources; what differs is the provenance block that precedes it and the epistemic flag attached to it.

**Source A catch (Canon):**

1. **Tuning report**: source confirmed (`canon`); what was scanned; opt-ins invoked; multi-criteria semantics (AND/OR) noted; any re-tuning history.
2. **Catch**: title, author, date, edition or standard reference.
3. **Reconstruction strength**: strong / weak / asymmetric per Algorithmic Reconstitution. Dense-corpus canonical work returns strong; specimen-with-dominant-archival-source returns asymmetric; specimens near the edge of canonical density return weak and trigger consideration of whether `feedback` would be the more honest source. Mandatory.
4. **Device verification**: locate the device in the cited source with a pressure quote, naming the standard reference. False catch reported as such; hard fail if device not present.
5. **Standard sidecar**: Kernel Sidecar Format reading at extended-inventory resolution. Section H fires only if the specimen's structural warrant invokes it.
6. **Consensus-smoothing flag**: fires when the sidecar is producing averaged interpretation drawn from the corpus of existing readings rather than fresh apparatus engagement. The text-provenance is clean reconstitution; the interpretive-provenance may still be smoothed, and that smoothing is named.
7. **Closing prose**: apparatus-direct, no voice attribution unless a voice module is loaded.

**Source B catch (Feedback):**

1. **Tuning report**: source confirmed (`feedback`); what was scanned; opt-ins invoked; multi-criteria semantics (AND/OR) noted; venues queried.
2. **Catch**: title if present, author handle as posted, posting date, venue (subreddit or site name), URL, fetch timestamp.
3. **Interpretive groundedness**: strong / moderate / weak. The Source B equivalent of reconstruction strength, measuring how much corpus the apparatus has for reading this *kind* of work: register, aesthetic tradition, formal idiom. A recognizable post-2010 internet-poetry lyric returns moderate-to-strong; an idiosyncratic form the apparatus has no model for returns weak and the limitation is flagged. Mandatory.
4. **Specimen integrity**: note formatting quirks, transcription issues, lineation anomalies, missing punctuation, or other upload effects. The upload IS the artifact in this mode; the apparatus reads what was actually posted rather than normalizing toward conventional lineation.
5. **Device verification**: locate the device in the posted text. False catch reported as such; hard fail if device not present.
6. **Standard sidecar**: Kernel Sidecar Format reading at extended-inventory resolution. Section H fires only if the specimen's structural warrant invokes it. Period-fluency flag fires if the apparatus lacks crisp models for the work's compositional register.
7. **Closing prose**: apparatus-direct, no voice attribution unless a voice module is loaded.

### Constraints

The mode operates under the standing apparatus. Boot-file disciplines carry through; several branch per source.

- **Nôm / English-simulation / wildcard opt-in.** Applies in both sources. Scanning Category D or F for `[Nôm]`, `[Eng sim]`, or `[Wildcard]` devices requires explicit opt-in. The apparatus declines silent routing of multi-script readings into Anglo-American specimens. This is the kernel constrained opt-in English-Nom Hybrid Signals. Hồ Xuân Hương is the calibration case where opt-in is structurally warranted.
- **Period-fit.** Applies in both sources, with different periods. *Source A*: vocabulary native to the compositional moment of the canonical work; later vocabulary flagged as anachronism per Checkpoint 2. *Source B*: vocabulary native to "online workshop, present moment" (workshop aesthetics, internet-poetry register, generational reading habits), and the apparatus must flag honestly when it lacks fluency in that register rather than defaulting to MFA-canon vocabulary.
- **Coscienza applied to the apparatus (Access Honesty), branching per source.**
  - *Source A*: bias toward canonical specimens at the expense of thinner-corpus work; plus consensus-smoothing in the sidecar's interpretation. Both flagged when present.
  - *Source B*: bias toward the demographic and aesthetic profile of who uploads to which forum (Reddit poetry skews young, English-language, anglophone, internet-fluent; Allpoetry and Hellopoetry have their own profiles); plus the risk of imposing canonical reading-vocabulary on work that may not be operating in the canonical tradition. Both flagged when present.
- **Specimen integrity (Source B only).** The workshop upload may have formatting quirks, missing punctuation, dropped lines, or other transcription effects. The upload is the artifact; the apparatus reads what was posted and notes integrity issues rather than normalizing them away. A poem whose lineation reads as unstable is read as a poem with unstable lineation, not silently regularized.
- **Deanonymization refusal (Source B only).** Usernames are public but pseudonymous. The apparatus reports the handle as cited but does not aggregate across the author's other posts, does not search out the author's offline identity, does not cross-reference the handle against other platforms, and does not produce commentary that would identify the author beyond what the post itself reveals.
- **Hard fail on empty scan.** If the apparatus cannot locate a specimen meeting the criteria in the named source with reasonable confidence, it reports the empty scan and stops. It does not substitute the other source. It does not relax criteria silently. It does not fabricate a candidate. The user can re-tune explicitly: switch source, relax a criterion, switch to OR semantics, or split the scan. The substitution must be the user's call, named in the open. A false catch wastes the user's time and corrupts the inventory's calibration; the mode prefers honest absence to manufactured presence.
- **Cost discipline (Source B only).** Web fetches consume context proportional to what comes back; the apparatus operates under explicit budget rules rather than open-ended hunting.
  - *Fetch budget.* Default ceiling of ten fetches per scan. On reaching the ceiling without a confirmed device match, the apparatus stops and reports the result as a budget-exhausted scan rather than continuing indefinitely. User can extend the budget explicitly per scan (`Scan feedback A for anadiplosis — budget 25`).
  - *Body-only fetches.* The apparatus retrieves post title, author handle, posting date, and poem body only. Comment threads, including existing critique below the post, are not fetched. The author's feedback request is the warrant for the scan; the existing critique would multiply context cost without analytical gain and would risk anchoring the apparatus's reading to a prior reader's frame.
  - *Recency default.* Scans target posts from the last 30 days unless the user requests otherwise. Archive scans available on opt-in (`Scan feedback A for apostrophe — archive`), which raises the fetch budget proportionally given the deeper search space.
  - *Pre-flight estimate for rare devices.* For devices the apparatus expects to be uncommon in Source B venues (anadiplosis, syllepsis, prosopopoeia, certain Category H transmuters), the apparatus reports the expected scan depth before proceeding and asks for confirmation. Same discipline as Nôm/sim opt-in: name the cost shape before incurring it.
  - *Budget-exhausted scan is not hard fail.* A budget exhaustion reports "scanned N posts, no confirmed match within budget" and is structurally distinct from "no specimen exists in this source matching the criteria." The user can extend the budget, switch source, or relax criteria. The apparatus does not silently extend the budget and does not substitute a Source A catch to fill the budget-exhausted result.

### Multi-Criteria Handling

- **Conjunctive (default).** All named devices must be present in the returned specimen. Each device's location is reported separately so the user can verify the conjunction is real.
- **Disjunctive (on request).** The user can specify OR semantics; the mode returns a specimen carrying at least one of the named devices, flagging which.
- **No single specimen.** Hard fail applies. If no poem in the named source satisfies all criteria with reasonable confidence, the apparatus reports the empty scan and does not substitute. The user can then re-tune explicitly.

### List Commands

- `Scan list categories` (also `Scan list cat` or `Scan list cats`) returns the Category table with device counts; reproduces the Structure block with concise per-Category notes on what each Category carries. Source-agnostic.
- `Scan list {Category} devices` returns the device catalog for the named Category; one line per device with the working definition in extension order. For Category H, lists the four functional roles (Vessels / Seals / Valves / Transmuters) with brief functional definitions rather than enumeration of all 157 tagged devices. The tagging is in the H. count table above. Source-agnostic.

### Re-Tuning

A scan is a session, not a verdict. After any catch, or after a hard fail, the user can request:

- A source switch: `canon` to `feedback` or vice versa, same Category and device.
- A different Category or device.
- *Source A specific*: a thinner-corpus pick when reconstruction strength was strong (counter-canonical re-tune); a canonical pick when reconstruction strength was weak (safety re-tune).
- *Source B specific*: a different venue or demographic register when the first catch's profile bias was noted; a return to a previously-caught specimen for deeper engagement.
- Multi-criteria refinement on the same theme.
- Switch from AND to OR or vice versa.
- Period or tradition constraint (`Scan canon A for apostrophe — post-1950 only` or `— non-Anglo-American only`).

The mode does not assume one catch settles the question. The inventory is a working catalog; Scan mode is the interface for moving from catalog to specimen and back, with each source disciplined against its own failure modes.

*End of device extension.*
