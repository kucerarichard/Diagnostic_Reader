# Portable Poetics Kernel

Version: 0.3.18  
Status: standalone loadable  
Private-core requirement: none  
Source policy: no full private-core poems

## Revision Notes

### 0.3.18

Installs two seams occasioned by `14-attridge-staten-extraction`, a critic extraction from a book-length dialogue on reading poems at the level of their making. Checkpoint 6 gains a second question: whether the effect a named device carries registered in reading order before the scan named it. The device inventory finds devices and this question decides which are credited, so that a scan of the full inventory does not become the post-reading dissection one definition of overinterpretation names. Triangulated Commentary gains a common-ground line: one line in the default register, with an address, stating what every deployed voice agrees is given on the page, before the voices split. The line records agreement and closes nothing; a triangulation in which nothing is agreed states that, and it is a finding. `7-device-inventory-extended` v0.4 carries the matching line for the scan. No change to any other checkpoint, dimension, directive, or format. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.17

Widens the specimen from a poem to any text on the page, occasioned by an operator instruction to read found text: a play excerpt, a script, fiction or newspaper prose, a cut-up, a label. The widening is small because the apparatus reads mechanisms, and `poem` was a label at most of the sites where it appears. At four sites the word changed a result, and each gets an edit. Address gains unit forms for speeches, stage directions, paragraphs, headlines, datelines, bylines, and fragments, and the counting convention now names the unit. Checkpoint 9 runs the absence scan against the text's declared kind rather than against poems. Period Fit and Coscienza each gain a two-moments note, since a found text has the source's composition moment and the finder's selection moment, and the apparatus reads the page's awareness at both without attributing either. Adds a Poetics Scan, a pre-reading pass that grades what stands up in a text as overt, covert, latent, or null, mapped to machinery the kernel already holds; null is a completed result. Adds Found Text Compatibility, a pointer on the model of the bay contracts: the consuming module's specimen card declares kind and unit, Register Is Not Referent fires by default on report kinds, Rendering Conditions expects heavy renderings, and a found provenance admits both the sidecar and the workshop. Register Is Not Referent carries a matching note. The distinction between a voice's non-poem take and a specimen reading of a found text is stated in `0c-voice-designations` v0.6. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.16

Adds three rules and one pointer, occasioned by `13-speaker-dials`. Register Prohibitions now state that trial text sits outside every zone the default register governs. A dial trial that raises a span's conversational density produces exactly the strings this kernel bans from apparatus prose, and a gate that read the trial as prose would fail it for doing what it was asked; Checkpoint 8 carries a matching note. Parasitic Effort gains a discrimination between theme announcement and a governing assertion, with the open-or-corner prompt. The dial file's calibration source treats a general sentence as the source of a poem's authority while this kernel lists theme announcement as wasted effort, and both are right about different sentences. Apparatus Homographs registers `voice`, which this kernel and the workshop have used in two senses since before the designation layer, and states that new vocabulary for a poem's speaking presence uses `speaker`. Speaker Dial Compatibility is a pointer on the model of the device inventory and the confinement catalog: a dial adds no bay, and the kernel holds no dial entries. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.15

Renames `interior music` to `sound and cadence` in Workshop Compatibility, following the operator's rename in `3a-workshop` v0.5.1. A distinctive term from a calibration corpus in a minimum-import list reaches every workshop module built on the kernel. Widens the Confinement Bay output field from axis of withholding to axis, with a fourth value, outward, for limits no one withholds, following `12-confinement-inventory` v0.5. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.14

Adds Confinement Bay Compatibility, the third bay contract, at condition scale above Engine Bay and Function Bay. Registers `confinement` as an apparatus homograph. The bay's catalog is `12-confinement-inventory` and the kernel holds no confinement entries, on the same terms as the device inventory.

### 0.3.13

0.3.13 adds a File Reference Rule and corrects a stamping defect. The 0.3.12 release carried its new revision note and shipped under a 0.3.12 file name while its Version line still read 0.3.11, so the file disagreed with itself in the one field a consumer checks first. The stamp is now part of the release, not a step after it. The rule is prompted by the same audit: eight cross-references across seven modules pointed at a kernel file name carrying a version, and every one of them had been wrong since 0.3.1, because a versioned file name in a load order goes stale on every release while nothing in the apparatus reads load orders strictly enough to fail. Cross-references now use the unversioned stem and let the operator resolve the file on disk, which is the form that survives a bump. Version floors keep their numbers, since a floor is a claim about capability rather than about a file. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.12

0.3.12 adds a Designation Policy and converts the Voice Slot Matrix from source-named slots to designated slots. The kernel already held the slots, the Voice Module Contract, and the Synthetic Continuation Notice, and every one of them named a slot by the critic who calibrates it, so an apparatus running correctly still emitted a calibration source's name in every label it shipped. The policy states the rule: generated output carries a designation, calibration-source identity does not appear in output in any form, specimen attribution is untouched, and apparatus-internal prose may still name sources because a negative lexicon that cannot name what it excludes cannot exclude it. The kernel carries the rule and not the mapping, since the mapping changes whenever a slot fills and a portable kernel holding a volatile table goes stale. The designation set, the leak tiers, and the calibration-collision rule live in `0c-voice-designations`; the per-slot designations live in the registry. Checkpoint 7 gains a matching gate. Consumers that declare Portable Poetics Kernel v0.3 and load no designation layer continue to run, and emit source-named labels; the policy is stated here so that loading the layer is sufficient to change every module's output without editing any module. Two residuals are left deliberately. Earlier revision notes keep the source names they were written with, because a revision log that has been rewritten is not a log, and revision notes are not output. The six directives carrying a `Private calibration source` line keep their poet attributions, because those are specimen provenance and the policy protects specimen attribution; the resulting disclosure is real, is confined to readers who hold both this file and a voice module whose corpus names its source on every page, and is judged the lesser cost against losing the audit trail on a laundered directive.

### 0.3.11

0.3.11 adds a relocation rule to the second editing pass. The pass already read a file against the purpose its opening states and deleted sections that did not advance it, and it had no provision for a section that advances a different file's purpose. Such a section is moved rather than cut, and the test is whether it would still be true with the file's subject removed. The rule was prompted by finding the voice slot matrix, the candidate log, and the reopen conditions inside a single source extraction, where they had accrued across sessions because that source was the first case to occasion them, with the result that other modules had to point at a source file to find their own status. The pass, rather than the Checkpoint Gate, is the right site: the gate runs before shipping a reading and misfiling happens while editing a module, so the pass now states that it runs on every module edit and not only before output. The same test applies to a sidecar that records a general rule instead of a finding about its specimen. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.10

0.3.10 removes specimen retrieval from the apparatus. The Feedback Venue Registry is retired, Random Workshop is gone from Kowit Workshop Mode, and Scan Mode's Source B changes from retrieved workshop-state uploads to operator-supplied corpora. The change is empirical rather than a matter of principle: across two rounds of venue expansion no venue returned both a poem body and its attribution, Reddit failing at a search-to-fetch handoff driven by licensing policy and Neopoet serving bodies from its stream while a robots rule closed the only path carrying a handle and a date. A body without attribution is not a specimen, because the handle is what lets a reading credit the person who invited the critique. Source B survives as a source rather than being deleted, because it was never merely a second input; it was the counterweight to Source A's consensus-smoothing, and a canon-only scan mode loses its check. A supplied corpus is the better counterweight, since the operator chooses it and the middle-zone exclusion still holds. What went with retrieval: venue allow-lists, tier grades, fetch budgets, the recency default, and the retrieval-failure outcome class. What stayed, rescoped: specimen integrity, deanonymization refusal, the located-quote ladder, and the Source B bias flag, which now names selection bias in what the operator supplies rather than the demographics of a forum. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3, and consumers issuing `Scan feedback` should update to `Scan supplied`.

### 0.3.9

0.3.9 renames the source-exposure ladder and defines what a quote must satisfy to be usable. The ladder measures how much text gets reproduced, and two of its five rungs were named for diagnostic purpose instead: `Token Quote`, `Pressure Quote`, and `Seam Quote` become `Phrase`, `Line`, and `Passage`, and `No Quote` becomes `Address Only` and is restated as the working default rather than a fallback. The renaming was prompted by an audit finding that `pressure` carried four apparatus senses that all describe the poem, the Core Dimension, Pressure Points, seam pressure, and title pressure, while `pressure quote` described reproduction quantity, which is the collision the 0.3.8 terminology rule names. Retired terms go to the Cut Ledger with their replacements. The new Located Quote section states seven properties, minimal, mechanism-only, one claim per quote, paraphrase-first, unstitched, verbatim, and non-accumulating, and adds the reassembly test, which catches the failure per-quote minimality cannot: an eleven-section treatment of a fourteen-line poem can satisfy every property at every site and still reprint half the poem. The section also specifies the address, both the counting convention and a notation for line, stanza, sentence, span, junction, and sub-line position, since a line number is unusable when two readers count differently. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3, and consumers naming the retired rungs should update to the size names.

### 0.3.8

0.3.8 refreshes the Default Register and Register Prohibitions against an updated tech-comms register, and extends Checkpoint 8 with matching gates. The register gains subsections, because it now carries enough rules that a flat section buried them: Audience and Stance, Core Principles, Sentence Mechanics, Terminology Discipline, Structural Mechanics, Notes Prompts and Gates, and Editing Passes. New rules govern terminology, one name for one thing and one meaning for one name, which the kernel had previously applied only to two terms in the Cut Ledger; nominalization; verb-construction and gerund use; a noun-string ceiling with a carve-out for registered operation names; a two-tier sentence length that caps gates, prompts, and field labels near 20 to 25 words and leaves explanatory prose uncapped, with bound voice zones outside the rule; and the distinction between a note, a prompt, and a gate. That last rule is prompted by the observation that two prior releases of this kernel exist because a required action sat in prose where readers skip it, the absence scan before 0.3.2 and the in-voice rendering rule before 0.3.7. The two-pass cut becomes three, the added pass being demonstration, which marks each claim, finds its artifact, then runs the check in reverse against artifacts that carry no claim. New prohibitions cover managerial speak, reader-grading affirmations, empty glue transitions, marketing scaffolding, and the machine-default decoration lexicon, the last split into decoration nouns and importance-intensifiers with a cover-the-word test. Several of those bans collide with apparatus vocabulary, so a new Apparatus Homographs entry protects `load-bearing` in the Engine vs. Residue sense, `alignment` in the typographic sense, `lift` in the Perloff sense, and the containment terms of the Hermetic subcluster. A sweep of the kernel against the new bans found it otherwise clean, with one exception carried forward: `resonant line`, the Final Classification field, survives as a registered name and is flagged for rename. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.7

0.3.7 adds one directive, Voice Rendering Mode, and extends Checkpoint 7 with a matching gate. The change is prompted by a triangulation that rendered every voice in reported speech ("X would respect," "X would read") in the default register, though a voice module was loaded and the verdict and triangulation zones are declared voice zones. The kernel already granted each bound zone full voice license through the Voice Module Contract and the Voice Slot Matrix; it had no directive stating that a bound zone is rendered in the voice rather than reported about, so the reported-speech default could stand without failing any gate. The new directive names the rule: inside a bound zone the critic speaks, in the first person or the module's declared essay person, and the reported-speech frame is retired; in triangulation each loaded voice speaks in its own person, and disagreement stands rather than collapsing to paraphrase. It leaves the Synthetic Continuation Notice untouched, since in-voice rendering changes register, not provenance. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.6

0.3.6 adds one directive, Rendering Conditions, with a matching gate, Checkpoint 10, and an added failure mode on the File End Test, apparatus-as-interference. The change is prompted by the observation that a poem read as clean monospace on a plain ground is far easier to process than the identical poem on a noisy published page, scan, or apparatus-wrapped restatement, though L0 is unchanged. The kernel already caught the semantic distortion of the L2 and L3 layers through Selective Salvage and Algorithmic Reconstitution; it had no concept for their perceptual load, the attention cost of extracting the poem through the noise of its presentation. The new directive names that cost, guards against its characteristic error, mistaking the page's hostility for the poem's difficulty, which it frames as the perceptual cousin of Register Is Not Referent, and turns the guard on the apparatus itself, since a sidecar is an L3 rendering that carries its own load. Access and interference are named as the same layers. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.5

0.3.5 sharpens Engine vs. Residue with a sound-versus-sense discrimination, and adds a matching cue to Checkpoint 1. When a reading proposes that a poem confuses, conflates, or collapses two things, the directive now asks whether the confusion runs along sound or along sense. Sense-confusion, where the poem treats two meanings as one because at its level of operation they are one, is engine evidence; sound-confusion, a near-homophone or a metrical slot, is usually residue. The refinement is prompted by a contrastive reading of birdsong-decoding research, in which finches confused calls of similar meaning more than calls of similar sound, taken as evidence the birds held the meaning rather than the sound. The apparatus inverts the decoder's premise, since a poem has no sender to confirm a reading, but the sound-versus-sense cut transfers intact. This adds a discrimination inside an existing directive; it does not add a named operation. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.4

0.3.4 adds one pointer to the Constrained Opt-In Devices list, the Compartmentalization Engine Reading, the device-scale lens of the Compartmentalization Engine. The engine reads a poem's response to a wound as a system of containing walls, after Alex Shigo's tree-pathology model of how a tree seals decay off rather than healing it. The directive and the full apparatus live in the Compartmentalization Engine module, which also registers the engine as a recognized type in the workshop's Engine Bay at poem scale. The kernel carries only the pointer, on the same model as the Hermetic or Alchemical Chamber Reading. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.3

0.3.3 refreshes the Default Register and Register Prohibitions against an updated tech-comms register. New: a ban on announce-then-deliver constructions; an expanded performative-header rule naming the grandiose, chatty, and meta-framing families, the last of which passes the noun-phrase test but reads as machine scaffolding; an expanded fashion-vocabulary list; and a show-before-telling rule adapted to the apparatus, where the artifact is the quoted line or located device. Refined: the contrastive-framing, hedging, and announce-then-deliver bans now cover the empty form only, with carve-outs that keep load-bearing corrective negation, calibrated uncertainty, and content-bearing colons, since the apparatus distinguishes and hedges by necessity. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.2

0.3.2 adds the directive Weak Signal and a matching gate, Checkpoint 9, Weak Signal and Absence. The change is prompted by the same Small Branch calibration: the missing footnote was a load-bearing absence, and the apparatus caught it late because nothing in it scanned for what was not on the page. The new directive treats faint or intermittent features and outright absences as signal, treats a reader's persistent unaccounted unease as a candidate signal to articulate, and guards against the paired error of manufacturing signal from static. The checkpoint makes the absence scan a default pass rather than an afterthought. Backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

### 0.3.1

0.3.1 adds one portable directive, Register Is Not Referent, and extends Access Honesty to the apparatus's own claims. The change is prompted by a full monty calibration in which a private core asserted a real-event provenance the source text never showed, and the apparatus read the poem's documentary register as evidence the events were real. The kernel did not supply that false provenance, since it carries no source claims, but it lacked a directive that would have caught the error: that documentary manner is a formal property and not proof of a referent, and that an unshown provenance is a hypothesis under the same honesty the apparatus applies to access. This release codifies the discipline so it protects every reading, not only the specimen that exposed it. It is backward-compatible with consumers that declare Portable Poetics Kernel v0.3.

## Document Scope

This file provides the minimum poetics apparatus required by standalone voice modules, workshop modes, and device extensions. It exports the working discipline of the private core boot without carrying its source poems.

A standalone module may import this kernel and run without `0-poetics-boot.md`. When the private core boot is loaded, treat it as a full monty plugin. It enriches source calibration under the kernel and does not seize active module zones.

The kernel carries procedures, terms, gates, and laundered calibration directives. It does not carry full specimen texts from the private core.

## Loading Contract

Load this file before any standalone module that depends on the poetics apparatus.

A module that imports this kernel may assume the following operations are available:

- Coscienza, both axes
- Mechanism before vibe
- Engine vs. residue
- The six core dimensions
- Genopersistation, L0 through L3
- Mixed Log and closure rule
- Source exposure policy
- Selective Salvage
- Algorithmic Reconstitution
- Portable calibration directives
- Voice and extension override rules
- Default register

A module that needs additional private-core examples must declare that dependency. Hidden dependence on the private core is a failure.

## File Reference Rule

A cross-reference to another apparatus file uses the unversioned stem: `0a-portable-poetics-kernel`, `3-kowit-voice-module`, `11-provenance-grading-extension`. The operator resolves the stem against what is on disk.

A file name carries its version so that two releases can sit in one directory. A reference does not, because a reference that names a version is wrong from the next release onward and nothing in the apparatus reads a load order strictly enough to fail on it. Stale references therefore accumulate silently, which is how eight of them survived twelve kernel revisions.

Version floors are different and keep their numbers. `Kernel requirement: Portable Poetics Kernel v0.3` is a claim about which capabilities the consumer needs, not a pointer to a file, and it stays accurate across every 0.3.x release by design. Where a consumer needs a capability added mid-series, the floor names that release and not the stem.

## Default Register

Use plain procedural-critical English.

### Audience and Stance

Write for a peer operator who will read the file once and act. Treat the reader as someone who already knows the field. State the rule, give the example, cut the padding. Do not perform expertise. Do not blame the reader for confusion. Do not soften the prose with generic assistant warmth, and do not grade the reader's contribution.

Second person suits instructional passages, as in run the absence scan, then mark what the genre would have supplied. Watch the tone, because second person slides into the imperative and sustained imperative grates. Directive prose, revision notes, and reference material use the third person. Either way the writing stays one-to-one rather than impersonal.

Contractions are permitted where speech would use them. Uncontracted prose already in this kernel passes as written and needs no retrofit.

### Core Principles

Hold to one theme. Each file, section, and reading carries a single purpose, stated in its opening sentences.

Get to the point. State what the operation finds, who runs it, and what it requires loaded. Long sentences with nested subordination and digression lose the reader, who then rereads or quits.

Be concise and informative. Use the fewest words that carry the finding. Brevity bought at the cost of clarity is a defect, and this rule is the counterweight to the Cut Ledger.

Show before telling. In this apparatus the artifact is the quoted line, the located device, the named pattern, or the cited edition fact. Lead with it, and let the commentary connect one artifact to the next and supply only what the artifact cannot show. A claim with no nearby textual anchor is telling to convert into showing, or filler to cut, and a quotation that anchors no claim is decoration and goes. Name the specific instance, the actual line or device, not a category.

Examples carry rules. Use an example after any rule that can be misread.

### Sentence Mechanics

Use active verbs. `The line turns the father into an absence` beats `an absence is created by the line`.

Do not nominalize a verb and prop it up with a weaker one. Write `the poem confuses two senses`, not `the poem produces a confusion of two senses`. Write `naming the mechanism first is the discipline`, not `the naming of the mechanism is an essential element of the discipline`.

Keep verb constructions simple. Where a simple tense carries the meaning, do not stack auxiliaries: `the directive fires on charged material`, not `the directive will have been firing on charged material`.

Use the `-ing` form as a gerund-noun, as in laundering is the failure, or as a modifier, as in the firing directive. Do not use it in place of a finite verb. `The reading launders the poem` states the action; `the reading laundering the poem` leaves the sentence unfinished.

Hold one tense through a paragraph unless the argument requires a shift.

Use adjectives, adverbs, and intensifiers sparingly. `Significantly`, `highly`, `dramatically`, and `incredibly` are dead weight. The general remedy is to give the number instead, but this apparatus does not score numerically, so the substitute here is the located anchor: replace the intensifier with the line, seam, or edition fact that would have justified it. If no anchor is available, drop the intensifier and the claim it was propping up.

Cut redundancy. `Refer back` is `refer`. `End result` is `result`. `Prior precedent` is `precedent`. Strike duplicate adjectives, hedging qualifiers, and connectives that carry no information.

Break long noun strings. When four or more nouns stack, the reader guesses which nouns bind to which. Split the string with a preposition or a hyphen: `policy for exposing source`, not `portable kernel source exposure policy level`. A registered operation name counts as one token and is exempt, so `Anti-Laundering Engine Default` and `Compartmentalization Engine Reading` stand as names rather than strings.

Vary sentence length and structure. Continual subject-predicate-object hammering flattens the prose. A paragraph typically mixes one or two short declaratives with a longer explanatory sentence, then closes short.

The variety rule governs explanatory prose. Gates, checkpoints, prompts, field labels, manifest lines, and minimal-runtime lines take a tighter ceiling near 20 to 25 words, because an operator acting on a gate or scanning a field wants the whole unit in one glance. Explanatory prose has no cap, and a sentence there can run long when it carries a clause the reader needs. The ceiling is a default, not a counter to obey; a 26-word checkpoint that reads clean stays. A bound voice zone sits outside this rule, per the Voice Module Contract and Voice Rendering Mode.

### Terminology Discipline

Use one name for one thing, and one meaning for one name. If the operation is `floor-origin hypothesis`, it is `floor-origin hypothesis` on every page, not `low-origin reading` here and `illegitimate origin` there; the reader cannot tell whether three names mean three operations or one. The reverse also binds: do not let one term carry two meanings in the same file. The Cut Ledger and the reserve rule on `illegitimate origin` are this discipline applied to two specific terms, and the register makes it general.

Define an ambiguous term on first use. Expand every acronym on first use. Treat CODIT, MS, and any inventory shorthand as opaque until the file makes them transparent. Avoid acronyms in headings and in the first sentence of a section. `L0` through `L3` are exempt as defined structural handles once Genopersistation has introduced them.

### Structural Mechanics

Headings name the section's content in a plain noun phrase, such as Provenance, Architecture, Mixed Log, or Limitations. A heading does not perform tone, ask a question, address the reader, or name the rhetorical move the section is making. Three header families are out: the grandiose drawn from marketing, the chatty drawn from blog and consumer READMEs such as `What this does`, `How it works`, `Who this is for`, `At a glance`, and `TL;DR`, and the meta-framing drawn from explainer writing such as `Mental model`, `Framing`, `Setting the stage`, `The big picture`, `Approach`, and `Orientation`. The meta-framing family passes the noun-phrase test but now reads as machine scaffolding, because it labels the move rather than the content; replace it with the content name, such as `Overview`, `Background`, or `Scope`. If rewriting a heading as a content noun phrase loses nothing, that rewrite is the heading; if the heading only introduced the section in a friendly voice or labeled its orientation, the section does not need one.

Paragraphs develop one idea across several sentences. The last clause of a paragraph sets up the first sentence of the next.

Use a list only when the items are enumerable, such as device bins, checkpoint steps, or manifest fields. Use paragraphs for continuous reasoning. Do not chop reasoning into bullets to simulate structure.

Fenced blocks carry templates, sidecar forms, and quoted output. Inline backticks carry term handles, file names, state values, and short literals. Italics mark a work's title or a term at first definition. Bold is reserved for a warning the reader must not miss, and this kernel issues none, so bold does not appear in kernel prose. A file that bolds ordinary text spends the one signal a real warning needs.

### Notes, Prompts, and Gates

Three units carry different authority, and the register keeps them distinct.

A prompt asks a question the reader answers against the specimen. Put one question in a prompt. Two questions in one prompt let the reader answer the first and skip the second.

A gate is an action the reader performs before shipping. State the precondition first and divide it from the action with a comma: `Before the mode is classified, test the Mixed Log`.

A note supplies information and requires nothing. Do not hide a required action inside a note, because readers skip notes and act on gates. If the apparatus must do it, it is a gate or a checkpoint. If the reader only needs to know it, it is a note. Two releases of this kernel exist because a required action sat in prose where readers skip it: 0.3.2 promoted the absence scan out of afterthought into Checkpoint 9, and 0.3.7 named the in-voice rendering rule that no gate had stated.

### Editing Passes

Run three passes before shipping framework prose or a reading. Cut rather than add.

First pass, sentence level. Cut superfluous adjectives, adverbs, articles, prepositions, and relative pronouns. Drop `that` where the meaning survives without it, and keep it where dropping it starts a garden path. Replace nominalized verbs with active verbs. Confirm every acronym is expanded on first appearance.

Second pass, section level. Read straight through. Confirm that short sentences interleave with longer ones, that sections lead into one another, and that the file serves the purpose its opening states. Delete any section that does not advance that purpose, including sections you are fond of.

One kind of section is moved rather than deleted. Ask of each one whether the decision it records is about this file's subject or about the apparatus. A rule governing the checkpoint gate, the register, the voice slot matrix, or the relations among modules is apparatus-level even when one source occasioned it, and it belongs in an apparatus-level file.

The test: would this section still be true if the file's subject were removed? If yes, it is misfiled.

Run this pass on every module edit rather than only before shipping. Misfiling is invisible at the moment it happens, because the editor is writing about something they were genuinely thinking about, and the section keeps accruing where it first landed. A reading is subject to the same test, since a sidecar that states a general rule instead of a finding about its specimen has misfiled the rule.

Third pass, demonstration. Mark each claim and find the artifact that carries it: the quoted line, the located device, the named seam, the cited edition or anthology fact. A claim with no nearby artifact is telling to convert into showing, or filler to cut. Run the check in reverse, since a quotation or device name that carries no claim is decoration, and decoration goes however apt it looks. Where a claim resists an artifact, confirm the prose names a specific instance rather than a category, the actual line and device and failure rather than `a feature`, `the relevant directive`, or `a failure mode`. Last, read the artifacts in sequence on their own, then read the prose between them on its own. The artifacts carry the spine of the reading. The prose says what they cannot show, and stops there.

## Register Prohibitions

These patterns appear by default in machine-generated prose. They fail the default register in every zone it governs.

Trial text is not one of those zones. The lines of a rewrite trial, a dial trial, or a contrast trial, and any quoted specimen, are written at the draft's setting or at the trial's. A gate that held them to these prohibitions would fail a trial that raises a span's conversational density for producing the gestures it was asked to produce. The commentary around a trial stays in the default register or in the bound voice.

- em dash punctuation or en dash punctuation used for dramatic pause or parenthesis. Replace with a comma, parentheses, a semicolon, or a full stop. The semicolon stays available, since this reader parses native English and a semicolon joins two related clauses more precisely than a full stop separates them.
- double hyphen used as dash punctuation
- contrastive filler formulas such as `not merely X`, `it is not just X`, `not X but Y`, and `more than just X`
- filler openers such as `Let's dive into`, `When it comes to`, `In today's fast-paced world`, `It's worth noting that`, `At the end of the day`, and `Here is the thing`
- filler closers such as `In conclusion`, `In summary`, `Hopefully this helps`, and offers of further help. When the reading is done, stop.
- fashion vocabulary such as leverage, seamless, robust, intuitive, powerful, comprehensive, elegant, holistic, synergy, ecosystem, journey, unlock, empower, supercharge, cutting-edge, state-of-the-art, best-in-class, blazing-fast, battle-tested, and first-class
- rhythm tricolons placed for cadence
- hedging stacks such as `it may be worth considering whether`
- restating the request or heading in the opening sentence
- mid-sentence bold for emphasis
- filler abstractions such as essentially, fundamentally, ultimately, at its core, and in essence
- decorative dividers, emoji, icons, and ornamental section furniture
- participial transition openers such as `Building on this foundation` and `Taking this a step further`
- announce-then-deliver constructions, where a noun phrase whose only job is to point at a finding precedes it across a colon, such as `What the data shows:`, `The key takeaway:`, `The move:`, or `Here is what is notable:`
- empty transitions placed as glue, such as `Moreover`, `Furthermore`, `Additionally`, `In addition`, `As such`, `Thus`, `Hence`, `Consequently`, `That said`, `That being said`, `Needless to say`, and `Rest assured`. These get dropped at the head of consecutive paragraphs to simulate a flow the reasoning does not have. Keep a connective only where it marks a real logical turn and the sentence would mislead without it.
- reader-grading affirmations such as `spot on`, `nailed it`, `you are absolutely right`, `great question`, `great call`, `excellent point`, `well put`, and `100%` used as agreement. The apparatus reports a finding and lets the reader judge it. It does not grade the reader, and these also break the stance rule against rapport padding, so they fail on two counts.
- marketing scaffolding such as `Whether you are a beginner or an expert`, `Look no further`, `In this guide we will explore`, `the beauty of X is`, `take your X to the next level`, `everything you need to know`, `revolutionize`, and `transform your workflow`

Three of these bans cover the empty form only, not its load-bearing twin. The contrastive ban removes the template raised for cadence, not the act of distinguishing: a corrective negation that carries information stays, as in the move is parataxis, not collage, and an expectation-versus-reality pairing stays when a competent reader would hold the expectation. The hedging ban removes reflexive softening that reports no real doubt, not calibration: specific load-bearing uncertainty stays and is stated plainly, as in this reading is dominant, but the corpus is thin. The announce-then-deliver ban removes the colon whose stage-setting phrase can be deleted without loss, not a colon that introduces a list or follows a clause that carries its own content. Test for all three: delete the suspect element, and if nothing is lost, it was form, and the deletion is the sentence. The importance-intensifier ban below takes the same shape and carries its own carve-out.

### Machine-Default Decoration

A model trained on the open web inherits the register that dominates web prose, which is content marketing. That register decorates. It reaches for a vivid noun where a plain one serves, and it asserts importance where it should show a consequence. A reader who has seen model output recognizes these words on sight, and a diagnostic reading loses its authority the moment they appear.

Decoration nouns and verbs, out in every zone the default register governs: delve, tapestry, `a testament to`, realm, `the landscape` and `the evolving landscape` as metaphor, beacon, embark, unleash, elevate, boast and boasts, vibrant, bustling, `treasure trove`, plethora, myriad, showcase and showcasing, garner, harness, navigate and navigating in the figurative sense, resonate, captivate, quintessential, commendable, meticulous and meticulously, profound, `a wealth of`, `a suite of`, and `a rich set of`. Use the plain word or delete. A poem that `boasts` a device has the device. A reading does not `navigate the poem's complexities`; it locates one seam, and the seam gets named.

Importance-intensifiers, out when they stand alone: crucial, critical in the vague sense, vital, essential in the vague sense, `key` as an adjective, important in the vague sense, significant in the vague sense, pivotal, paramount, notable and notably, underscore and underscores, and `it is worth emphasizing`. These assert that something matters instead of showing why. An importance claim stays when the sentence names the consequence that makes it true. `The caesura is crucial` goes. `Remove the caesura and the couplet closes on the wrong word` stays, and it drops the label.

Test: cover the word and read the sentence. If the sentence still names what the poem does, what the operation finds, or what would collapse, the word was decoration and the covered version is the sentence. If covering the word empties the sentence, the sentence carried no finding, and the sentence rather than the word is the thing to rewrite.

### Managerial Speak

The vocabulary of the status meeting carries tone and affiliation, not information. Out: `circle back`, `touch base`, `reach out` where email or ask will do, `loop in`, `ping` where message or ask will do, `sync` and `sync up` in the meeting sense, `align` and `alignment` in the agreement sense, `move the needle`, `low-hanging fruit`, `deep dive`, `drill down`, `double-click on` meaning examine, `level-set`, `boil the ocean`, `take it offline`, `bandwidth` meaning spare time, `actionable`, `learnings` where lessons or findings will do, `ask` and `lift` as nouns, `value-add`, `win-win`, `game-changer`, `north star`, `table stakes`, `going forward`, and `moving forward`. Replace each with the plain verb or noun it dresses up.

This list overlaps the fashion-vocabulary entry at leverage, synergy, and ecosystem. Fashion vocabulary inflates a technical claim; managerial speak inflates coordination and agreement. Both go, and where a term sits on two lists the stricter treatment governs.

Test: read the sentence as though it were a slide shown to a dean or a board. If it belongs there, and a plain verb would carry the same finding to an operator, the phrase is managerial and the plain verb replaces it.

### Apparatus Homographs

The bans target the corporate or decorative sense, not the technical homograph. Read the word in its sentence and ask which sense is present. These survive:

- `load-bearing` in its structural sense, the feature whose removal collapses the argument, stated together with what fails when it is gone. This is the Engine vs. Residue definition, and Load-Bearing Foreignness, load-bearing absence, and load-bearing allusion all depend on it. As a synonym for important it goes.
- `alignment` in the typographic sense, as in the visual and typographic devices of an extended inventory. The agreement sense goes.
- `lift` in the RETICLE module's Lift From Tradition, the operation of lifting a procedure out of a dropped line. The noun in `a heavy lift` goes.
- `pressure`, `valve`, `seal`, `vessel`, and `engine` in their core-dimension, device-inventory, and Hermetic senses.
- `confinement` in the Confinement Bay sense, the enclosure that limits what a poem is able to know and therefore able to say, distinguished from an elected constraint by the presence of a knowledge test. The ordinary carceral sense stays ordinary, and the figurative use in a source corpus is corpus material rather than apparatus vocabulary.
- `voice` in two senses. The apparatus sense names a critic register: voice module, voice zone, voice slot, Voice Rendering Mode. The craft sense names a poem's speaking presence, as in Device Inventory Lite's Voice Devices and the workshop's Voice as Depth of Attention and its section 7 heading, which predate the distinction and keep their names. New vocabulary for the craft sense uses `speaker`, as in speaker position and speaker dials. Where a sentence could carry either sense, rewrite it with `speaker`.
- `critical` meaning of or belonging to criticism, as in procedural-critical English and critical tradition. The vague-intensifier sense goes.
- `key` as a noun naming what unlocks a reading, as in the L1 key of Access-Asymmetry Mode. `Key` as an adjective goes.
- `resonant line`, the Final Classification field. This is the one decoration word retained as a registered name, because renaming a sidecar field breaks cross-references in every module that consumes the format. Treat it as a name rather than a license, and hold it as a rename candidate for the next breaking release.


## Source Policy

The kernel contains no full private-core specimens. It may use handles, compressed specimen cards, invented examples, redacted summaries, and minimal located quotes when needed.

High-risk source material uses the smallest unit that preserves the mechanism. If paraphrase preserves the mechanism, use paraphrase. If the exact word, phrase, line break, or seam performs the mechanism, quote the smallest usable unit and name why it is required.

Contemporary copyrighted poems use summary or a located quote at Level 1, 2, or 3. Full reproduction requires a separate source appendix and a clear permission or public-domain basis.

Redaction must name what it removes and what mechanism remains.

## Diagnostic Stance

A poem is treated as an engineered attention system. It contains surface features that work and a drive that makes them work together. The reader holds both visible without smoothing either one.

The apparatus reads the page, the making conditions, the support conditions, and the reception conditions. Some of a poem's persistence comes from the poet. Some comes from institutions, anthologies, schools, editors, critics, search systems, and model compression. The apparatus names the layers.

Reading is not endorsement. Diagnostic precision is not praise. The apparatus reads before it judges.

## Operating Rules

Use these rules in every kernel-based reading.

- Treat the poem as conscious until evidence shows otherwise.
- Name the mechanism before naming the mood.
- Treat allusion as evidence. Cut allusion that carries no weight.
- Treat politically or ethically charged material as engine until residue is proved by counterfactual reading.
- Attach every framework term to evidence from the specimen.
- Keep empty bins empty. Forced fill fails.
- Mark anachronistic frames as retrospective.
- Keep no more than three live hypotheses at output.
- State withheld evidence and redaction choices.
- Cut every apparatus term that decorates the reading.

## Coscienza

Coscienza is the awareness check. Use both axes.

Forward axis: do not credit the poem with awareness the poem does not show. If the poet did not bring the awareness, the reader does not import it.

Reverse axis: do not protect the poem from awareness it does show. If the poem builds a charged or ugly feature into its operating logic, do not treat the feature as accident because the lyric value becomes easier to keep.

Operating prompt:

> Where am I assuming the poet did not know what they were doing? What evidence supports that assumption?

If the answer is that the move is ugly and the reader wants to spare the poet, the assumption fails.

Coscienza also applies to the apparatus. During framework design, ask:

> Where am I softening my awareness of what the framework is doing?

Two moments, from 0.3.17. A found text has the awareness its source shows and the awareness its finder's selection shows, and the two can disagree: a cut-up produces patterns its source never held, and a label read as a poem carries an attention its writer never spent. Both axes run on the page. The forward axis bars crediting the source with the finder's pattern or the finder with the source's. The reverse axis bars excusing a pattern as accident because it arrived by cutting. Where the finder's procedure is declared on the specimen card, selection counts as awareness shown, since what was kept is on the page. Where it is not, the pattern is read as the page's and attributed to no one.


## Coscienza Provenance

The kernel keeps provenance because provenance prevents the awareness rule from becoming a floating slogan.

Coscienza enters the apparatus through Michele Barbi's Dante scholarship and Etienne Gilson's use of Barbi as an epigraphic discipline in *Dante the Philosopher*. The portable form preserves the rule and both axes; full bibliographic handling belongs in a full monty plugin or source appendix.

Portable rule:

> Do not import awareness the poem does not show. Do not remove awareness the poem does show.

The private core extends the principle to framework design. This kernel keeps that extension as Access Honesty.

## Mechanism Before Vibe

Name the move before the feeling.

Prefer:

> The line turns the father into an absence by returning to the empty gate.

Avoid:

> The line creates a haunting mood.

The mood may be true. The mechanism comes first.

## Engine vs. Residue

An engine is a feature whose removal collapses the poem's argument. Residue is a feature that can be removed without collapsing the argument.

Prompt:

> Would removing this feature collapse the poem's argument?

If yes, call it engine. If no, call it residue, symptom, ornament, or local texture.

Politically charged, violent, racist, classed, gendered, anti-democratic, or coercive material defaults to engine. Move it to residue only after the counterfactual reading proves the poem survives without it.

When a reading proposes that the poem confuses, conflates, or collapses two things, test whether the confusion runs along sound or along sense.

> Does the poem confuse these because they sound alike, or because they mean alike?

Sound-confusion is surface accident: a near-homophone, a pun, a rhyme pull, a metrical slot that admits the wrong word. Treat it as residue unless the poem makes the collision load-bearing. Sense-confusion is structural: the poem treats two meanings as one because at its level of operation they are one. Treat it as engine evidence. The two often co-occur, so name which is doing the work; a sound collision pressed into service as a sense collision has been promoted to engine, and the promotion is the finding.

## Six Core Dimensions

### Stance

Stance names the speaker's posture toward the material. Examples include confessional, reportorial, vatic, ironic, didactic, elegiac, pastoral, satirical, prophetic, and documentary.

Prompt:

> Who is speaking, and from what posture?

### Frame

Frame names the setup that lets the poem admit its content. Examples include documentary, anecdotal, ekphrastic, epistolary, oneiric, parabolic, emblematic, deathbed, and post-mortem.

Prompt:

> What setup licenses the content?

### Vector

Vector names the direction of force. The poem may pull the reader toward intimacy, public agreement, suspicion, grief, prophecy, submission, refusal, witness, or satire.

Prompt:

> Which way is the poem trying to pull the reader, and is the pull declared or hidden?

### Depth

Depth names how many strata the poem coordinates. A one-stratum poem can be complete. A multi-stratum poem may coordinate literal, political, biographical, theological, erotic, and formal layers.

Prompt:

> How many things is the poem doing at once, and how do they coordinate?

### Lattice

Lattice names the structural scaffold. Meter, rhyme, stanza, line length, prose block, refrain, catalog, break pattern, and repetition belong here.

Prompt:

> What holds the poem up, and where is it under stress?

### Pressure

Pressure names the line, phrase, image, turn, silence, or seam whose removal would cost the poem most.

Prompt:

> Where would removal collapse the poem?

Every reading names at least one pressure point.

## Genopersistation

Genopersistation names the layers by which a poem exists and persists.

### L0 Artifact Surface

L0 is the page. Word choice, syntax, sound, lineation, image, rhythm, punctuation, typography, and local structure belong here.

### L1 Compositional Making

L1 is the making condition. Biography enters only when it bears weight. Historical danger, censorship, illness, spiritual practice, class position, labor, exile, and compositional setting can matter. Trivia stays out.

Prompt:

> Which making conditions change the reading?

### L2 Institutional Support

L2 is the distribution system. Publishers, editors, magazines, anthologies, prizes, schools, readings, translation pipelines, platforms, and search systems belong here.

Prompt:

> How did the poem reach readers, and what did the route shape?

### L3 Reception Management

L3 is the prestige machine after the poem leaves the poet's control. Critical traditions, biographies, syllabi, anthologies, reputational repair, embarrassment laundering, and canonical sorting belong here.

Prompt:

> Which features did reception preserve, and which features did it smooth, drop, or excuse?

## Conditions Reading

Conditions Reading is an L1/L2 operation. It fires when the substrate matters more than an isolated agency claim.

Prompt:

> What climate, materials, cultural pressures, language conditions, support networks, and practical constraints converged to produce this work?

Use this operation for poets and traditions whose making conditions would be underweighted by a craft-only reading. Do not let Conditions Reading swallow the agency reading. Run both when both matter.

## Muse-Machinery Reading

Muse-Machinery Reading is an L1 operation for long careers with visible shifts in what drives the work.

Prompt:

> What figures, beloveds, systems, teachers, losses, places, gods, practices, or symbolic objects drive the work at this stage? What replaced what? What did the new configuration permit?

Use this operation when the poet's career shows distinct engines across stages. Do not use it as generic biography.

## Selective Salvage

Selective Salvage is the L3 laundering check.

Prompt:

> What did the prestige machine keep? What did it drop? What does the asymmetry reveal?

The keep-list and drop-list must be visible. A reading that preserves the beautiful features and omits the charged features repeats the laundering it should diagnose.

## Algorithmic Reconstitution

Algorithmic Reconstitution names the model-layer collapse of distribution and reception. A model may deliver text, summary, reception, and interpretation in one answer. The output may reconstruct, synthesize, smooth, or hallucinate.

Run three checks when model output is part of the reading.

Reconstruction strength:

> Is the model strong, weak, or asymmetric on this specimen?

Compression salvage:

> Which features did model compression keep, and which did it drop?

Synthesis marking:

> Is this source, paraphrase, or active synthesis?

Mark synthetic voice and synthetic criticism as synthesis. Do not circulate synthetic voice as source attribution.

## Access Conditions

Access is part of the reading. A framework can diagnose laundering while being available only to readers who know how to load it.

Prompt:

> Which readers can use this apparatus, which readers cannot, and what does that asymmetry produce?

Portable modules reduce the access burden. They do not erase it.

## Rendering Conditions

Access and interference are the same layers. The L2 and L3 machinery that carries a poem to a reader also taxes every reading of it thereafter. The reader would not have the poem without the anthology, the journal, the scan, the syllabus, the search result; and each of those renders the poem in a way that costs the reader attention the poem itself did not demand. The kernel's other L2/L3 checks catch semantic distortion, what reception kept, dropped, or smoothed. This directive catches the other tax: perceptual load, the cognitive cost of extracting L0 through the noise of its presentation.

Perceptual load leaves no trace in L0. The same words, lineation, and punctuation delivered as clean monospace on a plain ground and as a foxed, double-columned scan with running heads and footnote superscripts are the identical artifact at different reading costs. Nothing about the poem changed. What changed is the effort the presentation demands before the poem can be read at all. This is the one poetic-relevant fact that is genuinely not a property of the artifact: it lives in the encounter between a rendering and a reader, it varies by reader and by reading, and "the apparatus reads the page" has no purchase on it, because the thing that varies is not the page.

The error this directive guards against is mistaking the page's hostility for the poem's difficulty. A poem read off a cramped or degraded rendering feels denser, slower, and more forbidding than the same poem in a clean one, and a reader, or the apparatus, can promote that felt difficulty into a claim about the poem's engine. This is the perceptual cousin of Register Is Not Referent: manner of presentation misread as property of text, as register misread as referent. Difficulty, pace, density, and opacity are the judgments most exposed to it.

Prompt:

> On what rendering was this read, what load does that rendering carry that L0 does not, and is any judgment about the poem's difficulty, pace, density, or opacity owned by the poem or contaminated by the rendering?

Emit a Rendering Note when the rendering is degraded, heavy, or otherwise likely to contaminate a difficulty judgment: name the rendering (clean plaintext, OCR'd scan, photographed page, apparatus-wrapped restatement), and flag any difficulty-class judgment that the rendering may be inflating. Omit the note when the rendering is clean and neutral, on the same principle by which the loader notice is omitted when it changes nothing.

Self-interference clause. The apparatus is itself an L3 rendering. A sidecar, with its logs, axes, and phase notes, wraps the poem in machinery that carries its own load, and a reading can be hobbled by the apparatus as readily as by a journal's typography. When a plain reading would serve the poem better than a full sidecar, say so and get out of the way. The most useful thing a heavy apparatus can know about itself is when it has become the noise.

## Mixed Log

Keep multiple hypotheses active during reading. Do not collapse too early.

Use this structure:

```text
Hyp A: [claim]
Evidence: [support]
Status: dominant / qualified-live / closed
Reason: [closure reason, if closed]
```

### Closure Rule

A hypothesis closes when one of these conditions applies:

1. Textual evidence contradicts it.
2. Documented authorial statement contradicts it.
3. A rival hypothesis explains the same features without remainder.

At output, keep one dominant hypothesis and no more than two qualified-live hypotheses. If more than three remain live, run closure again.

Interpretive humility does not close a hypothesis. Evidence closes it.

## Checkpoint Gate

Run the gate before shipping a reading.

### Checkpoint 1: Engine vs. Residue

> Would removing the most charged feature collapse the poem's argument?

If yes, call it engine. If unclear, keep engine as the default until the counterfactual proves residue.

> If the reading claims the poem confuses two things, is the confusion sound or sense? Sense-confusion is engine evidence; sound-confusion is usually residue.

### Checkpoint 2: Period Fit

> Was this device, frame, or theoretical vocabulary available in this form at the moment of composition?

If the frame is later, mark it as retrospective.

A found text has two composition moments, the source's and the finder's, and a device can be native to either. Name which moment the device belongs to. A device native to neither is retrospective.

### Checkpoint 3: Coscienza

> Is the apparatus over-crediting or under-crediting awareness?

Correct both errors.

### Checkpoint 4: Hypothesis Closure

> Have live hypotheses been resolved under the closure rule?

More than three live hypotheses means the work is unfinished.

### Checkpoint 5: Source Exposure

> Does the reading quote only what it needs?

If paraphrase preserves the mechanism, paraphrase. If exact wording is required, quote the smallest usable unit and name the reason.

### Checkpoint 6: Decoration vs. Diagnosis

> Does each named term reveal a mechanism the reader would otherwise miss?

> Did the effect each named device carries register in reading order, before the scan named it?

Cut terms that dress the analysis. The two questions run together, from 0.3.18. The device inventory finds devices; a device is credited when the effect it names was present in the reading before the inventory supplied the name. A device whose effect appears only in the scan is reported as a finding about the scan, and it does not enter the Device Inventory field or the Poetics Scan's overt grade. The inventory names what was felt and does not manufacture it.

### Checkpoint 7: Voice and Extension Calibration

> If a voice module or device extension is active, does the output obey its declared register, scope, and negative lexicon?

> If a voice module is bound to a zone, is that zone rendered in the voice rather than reported about?

Voice drift fails. Cross-contamination fails. Reported-speech leakage in a bound voice zone fails: a bound zone that says "X would say," "X would read," or "X might note," instead of letting X speak, has not obeyed the voice. See Voice Rendering Mode.

> Does the output carry a slot designation rather than a calibration source's identity?

Calibration-identity leakage fails. A source name in a label fails. A coined phrase or biographical anchor that identifies the source without naming it also fails, and is the likelier form. See Designation Policy.

### Checkpoint 8: Default Register

> Does the unvoiced prose obey the default register?

Rewrite generic assistant prose before output. Run three further checks, because these patterns survive a first read.

> Does any decoration noun, importance-intensifier, glue transition, managerial term, or reader-grading affirmation appear outside a licensed homograph sense?

> Does one name carry one thing, and one thing one name, across the whole output?

> Is any required action sitting in a note rather than in a gate?

Apply the cover-the-word test to every intensifier. The third editing pass is mandatory on a shipped reading: every claim gets an artifact, and every artifact a claim.

Trial text is outside this checkpoint. See Register Prohibitions.

### Checkpoint 9: Weak Signal and Absence

> What is faint here that does heavy work, and what is missing that this kind of text would carry?

Run the absence scan, treat a persistent unaccounted nag as a candidate signal, and locate any weak signal in the text or discard it. On a specimen whose kind is not poem, the baseline is the kind declared on the specimen card, and the Poetics Scan's grade is read before an absence is called a defect.

### Checkpoint 10: Rendering

> On what rendering was this read, and is any difficulty judgment contaminated by the rendering rather than owned by the poem?

Emit a Rendering Note if the rendering is degraded or heavy. Check the apparatus itself: if a plainer reading would serve better than the full sidecar, say so.

## Phase Tensions

Use three modes.

### Failed System

The poem's tensions arise from failure, mismatch, accident, or uncontrolled inheritance.

### Intentional Glitch

The poem engineers disruption while concealing the disruption.

### Transparent Argument

The poem declares the tension as its operating premise.

A reading names the mode only after the Mixed Log has been tested.

## Portable Calibration Directives

The private core boot carries difficult source poems. This kernel exports their diagnostic force as directives. The directives retain the edge without requiring the full source surface.

### Floor-Origin Hypothesis

Private calibration source: Snowcrust.

Directive:

> A poem may reveal that its force comes from a low, unofficial, socially disowned, accidental, or unlicensed source rather than from the legitimating source its surface argument claims.

Prompt:

> Where does the poem claim legitimacy, and where does its actual energy arise?

Use `floor-origin hypothesis` as the default term. Reserve `illegitimate origin` for specimens where parentage, bastardy, inheritance law, legitimacy, or legal recognition are active parts of the mechanism.

Do not remove all low-origin language if that language performs the diagnostic work. Use the smallest pressure unit and mark the reason.

### Accidental Ars Poetica

Private calibration source: Snowcrust.

Directive:

> A poem can fail in its first-order argument and succeed as a second-order lesson about how poems defeat their own arguments.

Prompt:

> Where does the poem's example refute the poem's claim?

This is not satire by default. A sincere speaker can produce the diagnostic value by accident.

### Steganographic Surface

Private calibration source: Wyatt.

Directive:

> A poem may use a conventional surface as cover for political, erotic, religious, or survival danger.

Prompt:

> Which part of the poem exists so another part can be said safely?

A love surface, devotional tag, mythic frame, courtly emblem, or inherited form may serve as cover. The cover is part of the mechanism.

Do not treat coded danger as generic metaphor. Do not invent code without evidence.

### Weak Signal

Private calibration source: Santos, Small Branch full monty, the unwritten footnote.

Directive:

> Much of a poem's work runs at low amplitude. Meaning accrues from faint, intermittent indicators, a buried recurrence, a tonal undertone, a withheld word, a convention the poem declines, that carry weight out of proportion to their loudness and that most readings miss. Scan for the faint signal, not only the loud engine. The limit case of a weak signal is an absence: a thing the genre, the form, or the occasion leads you to expect, which the poem does not supply.

Prompt:

> What is faint here that is doing heavy work, and what is missing that should be present?

Absence scan. Run it explicitly, because the apparatus reads what is on the page and an absence is not on the page. Ask what a poem of this kind would normally carry, a source, a dedication, a name, a date, a turn, an address to the reader, a closing release, and mark each thing this poem withholds. A withholding is load-bearing when supplying it would change the reading. The missing footnote in the Small Branch specimen is the type case, caught late because nothing in the apparatus scanned for what was not there.

The nag is data. A persistent, unaccounted-for sense that something is off, felt before it can be named, is a candidate weak signal, not noise to be dismissed. Work to locate and articulate it rather than to quiet it. The reader's pre-articulate unease is often the first detector of an absence the analysis has not yet reached.

Guard against manufactured signal. This directive is where over-reading lives. A receiver tuned high enough hears a broadcast in pure static. A weak signal qualifies only when it can be located in the text, a specific absence or a specific faint feature that can be pointed at, and when it survives the pointing. If you cannot say where it is, you are narrating the static of your own expectation. Apophenia is the false positive that pairs with register-read-as-referent: both convert noise, or manner, into apparent meaning.

A located weak signal passes to Coscienza; it is not credited as design on arrival. Faint does not mean engineered. Forward axis: do not credit intention the poem does not show, since a faint feature can carry real weight and still be an accident. Reverse axis: if the faint feature is charged, do not excuse it as accident to spare the poet. Distinguish this from Steganographic Surface, which concerns a strong signal deliberately concealed; a weak signal is genuinely low in amplitude and may be unintended.

### Load-Bearing Foreignness

Private calibration source: Wyatt.

Directive:

> A foreign word, tag, phrase, or script survives only when it performs work the host language cannot perform as cleanly.

Prompt:

> What does this foreign element permit, compress, conceal, authorize, or endanger?

If the answer is tone, color, cleverness, or prestige, cut the element from the analysis or call it decoration.

### Sayability Test

Private calibration source: Santos.

Directive:

> When a poem carries another person's suffering, the reading must ask whether the form earns the material and on whose behalf the material appears.

Prompt:

> Can this poem be read aloud responsibly while bearing its claimed weight?

A failed sayability test does not end the reading. It becomes evidence in the Mixed Log.

### Appropriation Risk

Private calibration source: Santos.

Directive:

> A poem that uses another person's wound as material must show the frame, relation, distance, and labor by which that wound enters the poem.

Prompts:

> Who speaks?

> Who pays?

> Who disappears?

> What does the poem gain from the wound?

> What does the wounded person gain, if anything?

Keep memorial, appropriation, erasure, and engineered discomfort as possible hypotheses until closure conditions resolve them.

### Seam Pressure

Private calibration source: Santos.

Directive:

> The ethical pressure of a poem may sit in the seam between two materials rather than in either material alone.

Prompt:

> Which transition carries the moral risk?

A seam can be grammatical, temporal, visual, documentary, quoted, or silent.

### Anti-Laundering Engine Default

Private calibration source: Jeffers.

Directive:

> A charged political or ethical feature defaults to engine when the poem's argument would change without it.

Prompt:

> Am I keeping the beautiful surface and dropping the ugly drive?

If yes, the reading is laundering the poem.

Do not save the natural sublime by removing anti-democratic, colonial, racial, class, or violent logic that powers the poem.

### Register Is Not Referent

Private calibration source: Santos, Small Branch full monty.

Directive:

> Documentary manner is a formal property of a text, not evidence that its events occurred. A factual register, a flat reportorial voice, a dated or placed detail, and a bureaucratic insert can all sit in a poem with no real referent behind them. Reading register as proof of referent is an error.

Prompt:

> Does the page or cited paratext establish that the events are real, or am I inferring it from the way the poem sounds?

A provenance claim has standing only when the page shows it, by note, source, dedication, or a checkable dateline, or when cited paratext supplies it. An unshown provenance claim is a hypothesis, not a fact, and this holds whether the claim originates with the reader, a voice module, a workshop mode, or a full monty plugin's private core. The apparatus marks its own provenance claims at their true status and does not let a private core's assertion enter a reading as fact.

When provenance is unshown, keep the real-referent and invented-referent readings both live and treat the undecidability as a diagnostic object, rather than resolving it by default toward the real. Reading register as referent is also a laundering operation, the conversion of an unverified claim into apparent fact, so the Anti-Laundering Engine applies to it, including when the apparatus performs the laundering on itself.

Reverse-axis corollary:

> A poem that wears the authority of fact and withholds its source has made two charged choices, to borrow the authority and to withhold its basis. Under the reverse axis the absent attribution is an accountable feature of the poem, not a gap in the apparatus's evidence.

Report kinds, from 0.3.17. On a specimen whose declared kind is a news report, a notice, a log, or another report form, the directive fires by default rather than on warrant, because documentary manner is the kind's own register and the apparatus would otherwise read every such text as true. The reverse-axis corollary applies as written: a report that withholds its source has made the two charged choices whatever its kind. The attribution formula, in the Extended Device Inventory's Category G, is the device the directive most often fires on.

### Transparent Ugliness

Private calibration source: Jeffers.

Directive:

> Some poems do not hide their ugly premises. They argue with them in public.

Prompt:

> Is the tension concealed, accidental, or openly declared?

If openly declared, use Transparent Argument rather than Intentional Glitch.

### Complaint Loop

Private calibration source: Kowit.

Directive:

> A poem may locate the infernal condition in repetitive dissatisfaction rather than in catastrophe.

Prompt:

> What repeated mental habit creates the poem's hell?

Use this directive when a poem turns prosperity, comfort, safety, or ordinary life into torment through the mind's refusal to let the real be enough.

### Body-Cost Rule

Private calibration sources: Kowit and Santos.

Directive:

> Every abstraction must be tested against a body.

Prompts:

> Whose body absorbs the cost?

> Where does the thought enter the mouth, throat, hand, chest, gut, skin, breath, or wound?

> Which body has been turned into material for another speaker?

If no body bears the claim, the claim may be rhetoric.

### Cult-Gating Diagnostic

Private calibration source: Kowit.

Directive:

> Difficulty can serve discovery, and difficulty can gate attention through priesthood behavior.

Prompts:

> Does the poem ask the reader to perform submission without reward?

> Does the reception apparatus require initiation to protect the poem from ordinary reading?

> Does obscurity earn its keep on the page?

> Does the reader get positioned as peer, witness, student, supplicant, initiate, or captive?

Deploy this diagnostic only when the specimen or reception apparatus shows actual coercive attention structure. Automatic use turns the diagnostic into its own priesthood.

### Plain Speech as Anti-Laundering

Private calibration source: Kowit.

Directive:

> Clear language can function as ethical discipline when obscurity would hide the cost.

Prompt:

> What would the poem have to say plainly before its difficulty can be trusted?

Plain speech is not automatic virtue. Difficulty is not automatic fraud. The reading tests the work done by each.

### Defamiliarization Engine

Calibration source: defamiliarization-engine task.

Directive:

> A poem may be driven by the work of making an over-familiar thing perceptible again by rendering it strange. When that estrangement is the poem's payload, treat it as an engine, not a device.

Prompt:

> If the strange re-descriptions were removed, would the poem still have anything to deliver?

If the answer is no, the estrangement is load-bearing and the poem runs on this engine. The engine is produced by devices but is not identical to any one of them: the scale operations, the wrenched figures, the syntactic disruptors including correctio, and the visual estrangers all serve it. Name the engine at poem scale; name those parts at device scale.

The engine runs in any phase-tension mode. Failed System when the strangeness is accidental or inherited. Intentional Glitch when it is engineered beneath a plausible surface. Transparent Argument when the poem declares estrangement as its premise. Classify the mode only after the Mixed Log is tested.

Test the engine, do not credit it. The operative question is whether the strangeness rewards the attention it demands. Strangeness that rewards attention is the engine working; strangeness that only gates attention is the cult-mimicry failure. Grant estrangement neither automatic credit nor automatic suspicion, the same difficulty-that-earns-its-keep standard the apparatus applies elsewhere.

### Function Before Parts

Calibration source: Function Bay task.

Directive:

> A local craft problem is often a failed action rather than a failed part.

Prompt:

> What action does this passage need to perform, and what cleaner action could perform it?

Use function language before craft-part language.

Prefer:

> This line has to make the father feel present after he is gone.

Avoid:

> This line needs stronger imagery.

Image, music, line, diction, and form still matter. They are outputs of the passage's action.

### Parasitic Effort

Calibration source: Function Bay task.

Directive:

> A poem may spend effort proving it is poetic, serious, moral, difficult, or emotionally deep instead of performing its action.

Prompt:

> What effort is the poem spending on self-management rather than action?

Common forms include poetic diction, prestige vocabulary, emotional labeling, theme announcement, explanatory closure, false line breaks, and decorative metaphor.

Theme announcement and a governing assertion look alike on the page. Both are general sentences, and they do opposite work. Theme announcement names what the poem is about so the reader need not find it, and closes the particulars around one meaning. A governing assertion makes a claim the particulars then test, inflect, or complicate, so the details mean more after it than before.

Prompt:

> Does this general sentence open the details around it, or corner them?

A cliché corners in every position. A sentence that corners is parasitic effort and goes. A sentence that opens stays, and its position becomes a tuning question; see assertion position in `13-speaker-dials`.

### Access Honesty

Private calibration source: core boot.

Directive:

> The apparatus must name its own access limits.

Prompt:

> Who can load this tool, who cannot, and what readings become common when the tool is absent?

Portable design reduces friction. It does not erase the gate.

Access Honesty also governs the apparatus's own claims, not only who can load it. A provenance, source, or biographical fact that the apparatus asserts but does not show is a claim under this honesty, and a claim supplied by a private core or full monty plugin is not exempt from it. See Register Is Not Referent.

## Source Exposure Levels

Use the lowest level that preserves the mechanism.

### Level 0: Address Only

Give the address and describe what sits there. Quote nothing. `L7 carries the only abstract noun in the poem, and the line puts it under the stress` is a complete, checkable claim with no reproduction. This is the working default for most sections of most readings, not a fallback for when quoting is refused.

Also covers the diagnostic concept and the invented example, where no specimen is in play.

### Level 1: Phrase

One word or a short phrase. Enough for a coinage, a register collision, or a single colliding sense.

### Level 2: Line

One line, or the smallest fragment whose exact wording performs the mechanism. For a prose poem, one sentence.

### Level 3: Passage

Two or more adjacent units, used only when the mechanism spans the junction between them: a line break, a stanza turn, a syntactic hinge.

### Level 4: Full Text

Use only when the work is short, public domain, diagnostically necessary in full, and safe for the intended distribution context.

## Located Quote

Every quote at Levels 1 through 3 carries an address. A quote with an address is a located quote, and a quote without one is unusable, because a reader cannot check a claim against text they cannot find.

The name replaces `pressure quote` and `seam quote`. Both named a diagnostic purpose on a ladder that measures size, and `pressure` already carries four apparatus senses that all describe the poem, while exposure level describes how much text gets reproduced. Size now sits on the level, purpose sits in the claim, and position sits in the address.

### Properties

Seven, and a quote failing any one of them is not a located quote.

**Minimal.** The shortest span containing the mechanism. Test: remove one more word. If the claim stays checkable, the removal is the quote.

**Mechanism-only.** It carries the claimed mechanism and nothing besides. A quote that shows how good the line is rather than what the line does is decoration, and decoration goes.

**One claim per quote.** Two claims resting on the same words take one quote and two addresses, not the same words twice.

**Paraphrase-first.** Quote only where paraphrase loses the mechanism. Paraphrase carries word order, syntactic structure, and image content perfectly well. It cannot carry sound, ambiguity, a register collision, a coinage, or a solecism, and those are the cases that earn a quote.

**Unstitched.** No ellipsis joining non-adjacent fragments into one quote. Two fragments are two quotes and count as two.

**Verbatim.** Reproduce the posted text with its quirks: lineation, spelling, punctuation, capitalization. Silent normalizing turns a poem with unstable lineation into a different poem, which the Specimen Integrity rule already forbids.

**Non-accumulating.** Passes the reassembly test.

### Reassembly Test

Run this once, on the finished reading, before shipping.

Line every quote up in poem order and read them as a sequence. If that sequence lets a reader reconstruct the poem's shape or substance, the reading has over-quoted, however short each unit was and however well each one earned its place alone. Then cut until it does not.

The test exists because per-quote minimality does not bound the total. An eleven-section workshop treatment of a fourteen-line poem can satisfy every property above at every site and still reprint half the poem.

Default ceiling for in-copyright and workshop-state work: quoted lines total under a quarter of the poem, and no two consecutive lines quoted unless the claim is about the junction between them. The ceiling is a default rather than a counter to obey. A reading that runs one line over and passes the reassembly test ships.

### Disqualifiers

A quote goes when it was chosen because the line is the best one rather than because a claim needs it, when it serves the reading's admiration, or when it would let a reader skip the original.

Prefer a middle instance when the mechanism recurs. Take the opening or closing line only when the claim is about opening or closing, since those two lines are a poem's signature and the most reproduction-sensitive text on the page.

### Address

Two parts. The specimen address names which text, and the internal address names where in it.

State the counting convention once per reading, because `L7` means nothing if two readers count differently. The default: number from the first line of the body, count every line carrying text, do not count the title, do not count blank lines between stanzas. Name the unit with the convention when the unit is not the line, since a found text's card declares one and the forms below depend on it.

Internal address forms:

```text
L7           line 7
S3L2         stanza 3, line 2
Sent 4       sentence 4, for a prose poem or a short prose text
L12-13       a span
L12/13       the junction between two lines, for break claims
L7 medial    position within a line: opening, medial, close
L7 w4        the fourth word of line 7
Sp 4         speech 4, in a play or script; count every speech, do not count stage directions
SD 2         stage direction 2, counted separately from speeches
P3           paragraph 3, in prose; do not count a headline, byline, or dateline
P3 s2        sentence 2 of paragraph 3
Hd           the headline; Dl the dateline; By the byline
Frag 7       fragment 7, in a cut-up or found assembly, in the order the page presents them; state the convention when the page gives no order
Sp 4/5       the junction between two speeches, for turn-taking claims; P3/4 likewise for paragraphs
```

Specimen address fields for a supplied specimen are author, provenance, copyright status, and length. Consuming modules define the card; this section defines only the internal address.

Give the poem's total length in the specimen address. It costs four characters, it lets a reader locate a quote proportionally, and it makes the reassembly ceiling checkable by someone who is not holding the poem.

## Redacted Specimen Card

Use this card for high-risk source material.

```markdown
### [Handle]

Source status: [public domain / copyrighted / unknown]
Content flag: [brief description]
Diagnostic function: [one sentence]

Specimen summary:
[Brief factual summary without high-risk surface reproduction.]

Located quote:
[Address, then the quote at Level 1, 2, or 3. Or Level 0, address only.]

Mechanism retained:
[The operation preserved by the card.]

Redaction note:
The core text withholds [material type]. The retained mechanism is [mechanism]. Full source access belongs in a separate appendix when required.
```

## Device Inventory Lite

Use the lite inventory when no extended inventory is loaded. Empty bins remain empty.

### Frame Devices

- documentary frame
- anecdotal frame
- apostrophic frame
- emblem frame
- ekphrastic frame
- oneiric frame
- parabolic frame
- post-mortem frame
- source-rewrite frame

### Voice Devices

- confessional posture
- reportorial posture
- vatic posture
- satirical posture
- didactic posture
- witness posture
- ventriloquy
- apostrophe

### Tense and Mood Devices

- tense shift
- predictive turn
- imperative turn
- subjunctive intrusion
- atemporal address
- retrospective frame

### Lattice Devices

- sonnet strain
- prose-block lattice
- long-line catalog
- refrain shift
- enjambment pressure
- line-break suspense
- stanza turn
- repetition field

### Reference Devices

- load-bearing allusion
- foreign tag
- source rewrite
- biblical register
- mythic rewire
- bureaucratic insert
- documentary quote

### Closure Devices

- quoted closure
- imperative closure
- ironic reversal
- asymmetrical closure
- image stop
- silence stop
- return closure

### Ethical Devices

- erasure as content
- credibility management
- appropriation risk
- sayability test
- body-cost transfer
- witness relation
- reception laundering


## Constrained Opt-In Devices

These devices survive in portable form as constraints, not defaults.

### English-Nom Hybrid Signals

Use only with documented multi-script, diasporic-bilingual, or analogous compositional substrate. Do not apply to ordinary Latinate diction in English poems.

### Crip Space-Time Deformation

Use only when disability or non-normative embodiment is explicit content. Temporal complexity alone does not trigger it.

### Acausal Apparatus

Use only when the user explicitly asks for an acausal or U.G. Krishnamurti frame. The apparatus must declare the philosophical commitment before use. Default deployment eats Coscienza, Engine vs. Residue, and Mixed Log.

### Hermetic or Alchemical Chamber Reading

Use only when the poem's structure rewards chamber, seal, valve, and transmutation language. Do not use this as a richer name for any closed form.

### Compartmentalization Engine Reading

Use only when a poem is built around a wound it walls off rather than resolves, or carries a void at its center while its surface keeps living. Reads the poem's defenses as walls of rising strength after Shigo's tree-pathology model, with the barrier zone, the post-wound defense that is also the future fracture plane, as the load-bearing object. Always retrospective: the wall structure may be real in the poem, but the model is the reader's, never the poet's. Do not use this as a name for any closed form or any grief poem. The full apparatus, the calibration directive, and the trigger and non-trigger conditions live in the Compartmentalization Engine module; this is the device-scale lens of the engine named in the workshop's Engine Bay.

### Embodied Attention Quality

Use when the poem's surface evidences released or constricted attention in the body, breath, posture, gesture, or movement. Honest absence is permitted.

## Kernel Sidecar Format

Use this form when no private core sidecar governs the task. A full monty plugin may enrich any section with source-bearing calibration. A voice module may govern Triangulated Commentary or Verdict inside its declared zone.

```markdown
## [Specimen Title]

### Provenance
Date, source, author, making context, and source status. Include only facts that bear on the reading. For a found text, kind and unit, the finder, and the Poetics Scan grade; the sidecar has no separate card, so this field carries them.

### Architecture
The poem's structural shape in mechanism terms.

### Fracture Surface
Visible strain, rupture, seam, overfit, underfit, contradiction, or turn.

### Coscienza
Forward axis and reverse axis.

### Core Dimensions
Stance, frame, vector, depth, lattice, pressure. Omit empty dimensions only when honest omission is clearer than a filled list.

### Device Inventory
Only devices that fire. Apply period fit.

### Mixed Log
Dominant hypothesis, qualified-live hypotheses, and closed hypotheses with reasons. Use the Closure Rule.

### Genopersistation
L0, L1, L2, L3. Use compressed notes when layers are thin.

### Rendering Note
Emit only when the rendering is degraded, heavy, or apparatus-wrapped enough to contaminate a difficulty judgment. Name the rendering and flag any inflated difficulty-class judgment. Omit when the rendering is clean.

### Pressure Points
Name the line, phrase, image, turn, silence, or seam whose removal would cost the poem most.

### Phase Tensions
Classify as Failed System, Intentional Glitch, Transparent Argument, or open state when evidence cannot close the mode.

### Portable Directives
Name any calibration directive that fires: floor-origin, steganographic surface, sayability, seam pressure, anti-laundering engine, transparent ugliness, complaint loop, body-cost, cult-gating, plain speech, function before parts, parasitic effort, access honesty, rendering-load, or others added by modules.

### Triangulated Commentary
Open with one line of common ground in the default register: what every deployed voice agrees is given on the page, with an address. The disagreement that follows is mapped against it. A triangulation in which nothing is agreed states that, and it is a finding. Then deploy only voices that have something distinct to say. An active voice module may use full prose license inside its declared zone, and under Voice Rendering Mode a bound voice speaks in its own person here rather than being reported about: render each loaded voice in the first person under its own name-label, let counter-voices answer in their own register, and keep the disagreement unsmoothed. Voices without loaded modules appear as compressed notes in the default register, or stay absent.

### Final Classification
Type, operating mode, infrastructure, pressure point, resonant line, and diagnostic lesson.

### Verdict
Plain prose in the default register when no voice controls the section. When a voice module is bound to the verdict, Voice Rendering Mode governs: the verdict is rendered in that voice, in the first person or the module's declared essay person, not reported in the default register. The verdict is not a summary. It names what the poem does, what it cannot avoid doing, and what the reading must not smooth.
```

## Workshop Compatibility

A workshop module may use this kernel without the private core.

Minimum workshop imports:

- image as concrete particular
- real language before poetic diction
- sound and cadence
- line break as decision
- form when it serves
- voice as depth of attention
- revision as route-naming
- function before parts
- body-cost rule
- source exposure policy

Workshop output may use a voice module if loaded. If no voice module is loaded, use plain workshop register and do not claim a named voice.

## Confinement Bay Compatibility

Confinement Bay works at condition scale, above Engine Bay and Function Bay. The three bays descend: what the poem is able to know, what drives it, what one passage performs.

Prompt:

> What is systematically absent from this poem, is the absence patterned, and what does the pattern make unknowable?

The question routes to Checkpoint 9, Weak Signal and Absence. It is not Engine vs. Residue, which tests what collapses on removal. Confinement tests what was never available. One absence is an accident. A pattern is a confinement.

Output fields:

- position, the epistemic limit
- surface, the repeating rules that show
- fold, how position and surface route the withheld thing to the reader
- active site
- forbidden defaults
- knowledge test
- axis: upward, sideways, inward, or outward
- breach scan, with load-bearing or slack named

A confinement differs from a constraint by the knowledge test. A constraint is elected and can be lifted. A confinement reaches what the speaker can know, whether or not anyone chose it. An extraction with an empty knowledge test has found a form, and forms belong to Form Examination and the device inventory.

State an extraction as what the page enforces, never as what the poet chose. Reading a confinement as an intention fires Intention Substitution.

Confinement entries are not kernel material and live in `12-confinement-inventory`, on the same terms as the device inventory. The kernel needs to know what the bay does, not what is in the catalog.

Rewrite trials under an alternative confinement are consumer-side and opt-in. A trial is a contrast trial and never a revision route. The importing carve-out in Engine Constraints extends to Confinement Bay on identical terms: an imported structure is licensed as a trial and is never licensed as the poem.

## Engine Bay Compatibility

Engine Bay works at poem scale.

Prompt:

> What drives this poem, and what other engines could this draft plausibly accept?

Output fields:

- current engine
- load-bearing parts
- tuning options
- possible engine swaps
- required new parts
- cost of each swap
- promise of each swap
- best-fit assessment

Engine swaps must arise from the draft's visible material. If the route requires importing a different poem, reject it.

## Function Bay Compatibility

Function Bay works at passage scale.

Prompt:

> What action does this passage need to perform, and what cleaner action could perform it?

Output fields:

- target passage
- current function
- current strategy
- parasitic effort
- functional alternatives
- contrast trial
- single experiment

Function Bay prevents craft-part policing. It does not replace image, music, line, diction, or form. It changes the order of attention.

## Speaker Dial Compatibility

A speaker dial is a dimension of how a poem's speaker talks, along which every draft has a setting: diction altitude, assertion position, phatic density, idiom density, and provisional others. A dial fails the knowledge test by construction, since a setting changes how a thing is said and leaves what the poem can know where it was. So a dial is not a confinement, and it adds no bay.

Dial trials run inside the existing bays: as a contrast trial at passage scale in Function Bay, as a tuning question in Engine Bay, and as an overlay on a Confinement Bay trial, run as a pair so that the seam can separate the change of carrier from the confinement.

Dial entries live in `13-speaker-dials`, on the same terms as the device inventory and the confinement catalog. A dial trial is a contrast trial and never a revision route. The importing carve-out in Engine Constraints extends to it on identical terms.

## Found Text Compatibility

A specimen is a text on the page with its attribution, and the text need not be a poem. A play excerpt, a screenplay page, a passage of fiction or newspaper prose, a cut-up, a label, a notice, and a stretch of correspondence enter on the terms a poem does, and the apparatus reads them with the same operations. Where a procedure in this kernel says poem, read specimen. The procedures were written for poems and run unchanged on any text, and a global rename would break cross-references in every consumer. The kernel changes nothing in its procedures for found text. It asks the consuming module's specimen card for two declarations the procedures need.

Kind names what the text presents itself as: poem, play excerpt, screenplay, fiction prose, news report, cut-up, label, correspondence, or another named kind. Kind sets the baseline for Checkpoint 9, since an absence is measured against what the kind carries. Unit names what an address counts: line, sentence, speech, paragraph, or fragment. Unit sets the address forms in Located Quote and the length field on the card.

Three defaults follow from kind. Register Is Not Referent fires by default on report kinds, because documentary manner is the kind's own register and proves nothing about its referent. Rendering Conditions expects a heavy rendering, since found text arrives as a photographed label, an OCR column, or a formatted script page, and emits its note on the usual terms. Where `8-frye-extraction` is loaded, radical of presentation is the first field to fill, because a play and a label differ there before they differ anywhere else, and a found text read as a poem has changed radical by construction.

A found text is finished in its own kind and raw as poetic material, so the card's provenance takes a third value, found, which admits both the standard reading and the workshop. The standard reading reads the text as finished in its kind, and voices stand up or stand down on the specimen's properties as they always have. The workshop treats the text as material and runs its sections on the declared unit. The operator chooses the route. The consuming modules define the card.

Found text does not change the exposure ladder. A cut-up the user made is the user's arrangement, and the words in it keep their source's rights, so quotation of the arrangement is quotation of the source. The reassembly test and the default ceiling apply to in-copyright prose and scripts as they apply to poems. Read the ceiling proportionally on a short text and against an absolute count on a long one: a quarter of a column is too much and a quarter of a label is nothing.

A specimen reading of a found text and a voice's non-poem take are different operations. The take addresses a subject with no text on the page; the reading addresses a text. `0c-voice-designations` states the test. The Poetics Scan below decides whether a poetics stands up in the text at all.

## Poetics Scan

A pre-reading pass that grades what stands up in a text before the voices do. It runs by default on any specimen whose kind is not poem, on command for a poem, and it is the whole of the operation when the command is `poetics scan`.

Prompt:

> What in this text is doing poetic work at a located address, and is that work overt, covert, latent, or absent?

Four grades. Each maps to machinery this kernel already holds, and each requires an address.

- Overt. Devices fire on the page with period fit. The text declares a poetics or carries one a reader notices. Evidence: the device inventory, at whatever resolution is loaded.
- Covert. A pattern exceeds what the kind requires, and removing it leaves the kind's own purpose intact. A report that runs a refrain, a notice with a turn, a recipe built as an inventory poem. Evidence: Weak Signal for the pattern, then Engine vs. Residue run against the kind and not against a poem. If removal collapses the kind's purpose, the pattern is the kind's engine and no poetics is credited.
- Latent. No device fires, and the text holds a speaker position with a knowledge limit, or sits at a dial setting that keeps something off the page, with no surface using either. A trial could make it audible; the page has not. Evidence: Confinement Bay extraction and the dial page test where their files are loaded, the Stance and Pressure dimensions where they are not.
- Null. Nothing stands up. The scan reports it and stops. Null is a completed result on the footing of a stand-down, and a reading that proceeds past it as if it had found something is reading its own apparatus.

Report the grade, the addresses, and the machinery that supplied the evidence, in the default register:

```text
Poetics Scan: covert. Refrain at P2 s1, P5 s1, P9 s1, in excess of the report's purpose; removal leaves the report standing. Confinement extraction available in the workshop on request.
```

The forward axis of Coscienza is the guard. A poetics apparatus will find a poetics in any text if it is allowed to look without an address, and a grade that cannot name where it fires is Poetics Projection, which the workshop names as a failure mode. A latent grade is not a promise. It says a trial could reach something, and the trial's `Reached` line decides whether it did.

## Voice Slot Matrix

The kernel does not contain voice corpora. It preserves the slots and authority limits so standalone voice modules can plug in.

Slots are named by designation. A designation names the function a slot performs, so it survives the slot's module being replaced. The mapping from designation to calibration source is not kernel material and lives in the registry; the kernel needs to know what each slot does, not who calibrates it.

### ASSAY Slot

Reception and canon formation. Default verdict slot when no active voice module fits better. Long periodic sentences and multilingual compression are allowed only inside a labelled ASSAY zone or a module that declares the register.

### PLUMB Slot

Labor, prison, soldier, body-in-system. Newsroom plain American. Use for labor, prisons, soldiers, working people, institutions, or material systems when loaded and applicable.

### RETICLE Slot

Procedure and the examined lyric. Academic-formalist positioning. Use for formally innovative or avant-garde specimens when loaded and applicable. Period fit remains mandatory.

### TARE Slot

Plain speech, workshop, body-cost. Plain workshop-teacher American. Use for democratic accessibility, body-cost, cult-gating, moral substrate, and craft attention when loaded and applicable.

### DATUM Slot

Provenance and the official account. Graded attribution under legal pressure. Use where a specimen carries an account of itself that can be measured against a record, or where claim standing is contested. Requires a provenance-grading extension.

### Gonzo Mode Slot

A mode, not a voice. It changes cadence when loaded and specimen-applicable. It must ride on an active voice or declared base register.

### Workshop Slot

A user-triggered diagnostic mode. It treats a poem as draft or craft object. It does not replace standard sidecar reading unless the user asks for workshop treatment.

### Synthetic Continuation Notice

Synthetic voice output is Active Synthesis. It may be used as register inside a private working framework. It must not be circulated as an attributed statement by any critic or poet, and under the Designation Policy it must not name the calibration source at all.

## Designation Policy

Generated output carries designations. The identity of a calibration source does not appear in generated output, in any form, including forms that do not use the name.

Three zones.

Generated readings take designations only. Verdicts, triangulated commentary, sidecars, device translations, diagnostics, and any label attached to them.

Apparatus-internal prose keeps source names. Module headers, manifests, negative lexicons, registry entries, loader notes read by the operator. A header is not output.

Operator queries are answered plainly in the default register. This is output hygiene, not a seal against the operator, who has to be able to audit the calibration.

Specimen attribution is untouched. A reading names the poem, the poet, the date, the edition, and the reception facts it relies on. The policy masks who supplies the register, never who wrote the thing being read. A reading that will not name its specimen has failed a different and more serious rule.

A name swap alone does not satisfy this policy. A source's coined phrases and biographical anchors identify it without the name, and they arrive inside moves the modules positively encourage. The tiered leak procedure is not kernel material; see the designation layer. The kernel's requirement is the outcome: output that names nobody and identifies nobody.

Where no designation layer is loaded, a module emits its own source-named label and the apparatus is out of policy. Loading the layer is sufficient to bring every module into policy without editing any module.

## Voice Rendering Mode

When a voice module is bound to a zone, that zone is rendered in the voice. The critic speaks, in the first person or in the module's declared essay person; the apparatus does not report the critic in the third person. Inside a bound zone, retire the reported-speech and subjunctive frame: do not write "X would say," "X would read," "X would respect," "X would distrust," or "X might note." Write what the voice says.

This governs every zone a module declares: the closing verdict, triangulated commentary, device translation, and any special diagnostic. In triangulation, each loaded voice speaks in its own person under its own name-label, and a counter-voice answers in its own register rather than in paraphrase. Let the disagreement stand.

The default register still governs every unvoiced zone: provenance, architecture, core-dimension and mixed-log fields, classification lines, checkpoints, rendering notes, scan tables, manifests, loader notes, source-exposure notes, and any run where no voice is bound. A voice without a loaded module appears as a compressed note in the default register or stays silent. Structured field labels stay in the default register even inside a voiced sidecar; the voice renders the prose the field contains, not the label.

The Synthetic Continuation Notice is unchanged and still binds. A voiced block is Active Synthesis in the module's idiom, carries its one-line synthesis label once (for example "ASSAY verdict"), and is never circulated as an attributed statement by any critic. Under the Designation Policy the label is built from the slot designation and never from a calibration source's name. In-voice rendering changes the register, not the provenance.

## Voice Module Contract

A standalone voice module must declare its zone.

Possible zones:

- closing verdict
- triangulated commentary
- workshop treatment
- device translation
- special diagnostic

The voice governs only its declared zone. The default register resumes outside that zone. Inside its declared zone the module renders in voice under Voice Rendering Mode; zone output that reads as reported speech about the critic ("X would say") fails Checkpoint 7.

Each voice module must provide:

- scope
- stance
- register
- operational lexicon
- negative lexicon
- recurring moves
- diagnostic contribution
- output zones
- examples
- failure modes
- voice gate

Voice output fails when it reads as generic competent criticism rather than the declared voice.

## Device Extension Contract

A standalone device extension must declare its imports and limits.

Use this manifest.

```markdown
## Module Manifest

Module name: [name]
Module type: voice module / workshop mode / device extension / diagnostic add-on
Kernel requirement: Portable Poetics Kernel v0.3
Private-core requirement: none / optional / required
Optional private-core enhancement: [what changes when private core is loaded]

Exports:
- triggers
- procedures
- output fields
- constraints
- failure modes
- examples

Imports:
- [kernel operations]

Source policy:
[No full private-core specimens unless declared and justified.]

Failure condition:
[Condition under which this module is not standalone.]
```

## Full Monty Plugin Contract

A full monty plugin is a loaded source-bearing or heavily calibrated core apparatus that sits above this kernel. The private `0-poetics-boot.md` is one full monty plugin. A user may load a different full monty plugin if it declares the manifest below.

The kernel runs without a full monty plugin. Modules that import the kernel must also run without one unless their manifest says otherwise.

### Plugin State

Set `Full Monty State` at the start of each task.

`absent`: no full monty plugin is loaded. Modules use the portable kernel and their own local rules.

`present`: one full monty plugin is loaded. Modules may use its exported apparatus, examples, sidecars, source appendix, and calibration directives.

`multi`: more than one full monty plugin is loaded. Use the most recently loaded explicit plugin unless the user names a different active plugin. Keep older plugins as context, not authority.

`conflicted`: two active instructions cannot be reconciled. Use source fidelity, safety, explicit user command, active module zone, then the active full monty. If the conflict remains, report the conflict briefly and proceed with the safest narrower rule.

### Legacy Private Core Adapter

If `0-poetics-boot.md` is loaded and does not declare a plugin manifest, treat it as this plugin:

```markdown
Full Monty Plugin Name: private core boot
Plugin type: poetics_full_core
Kernel compatibility: Portable Poetics Kernel v0.3
Activation condition: loaded in current chat context
Source status: private source-bearing calibration file
Exports:
- full Diagnostic Reader apparatus
- full sidecar format
- full Genopersistation stack
- Five Checkpoint Gate or later gate set
- worked example calibration
- ASSAY default verdict, when no active voice module overrides it
- private source exposure choices already made inside the core
- extended operations declared by the core
Authority limits:
- does not override safety or copyright rules
- does not override an active voice module inside that module's declared zone
- does not force full source reproduction in portable output
- does not make itself a dependency for modules that declared kernel-only operation
```

### Custom Plugin Manifest

A custom full monty plugin must include this block near the top of the file.

```markdown
## Full Monty Plugin Manifest

Plugin name: [name]
Plugin type: poetics_full_core
Kernel compatibility: Portable Poetics Kernel v0.3
Activation condition: loaded in current chat context / explicit user command / named mode only
Source status: source-bearing / redacted / source-free / mixed

Exports:
- [base apparatus procedures]
- [sidecar or output forms]
- [worked examples or calibration cards]
- [source exposure rules]
- [voice defaults, if any]
- [device inventories or extensions]

Overrides:
- [kernel rules overridden by this plugin]

Non-overrides:
- source fidelity
- safety and copyright limits
- active voice modules inside declared zones
- active workshop modes inside declared zones
- explicit user command for the current task

Plugin gate:
> What does this full monty add that the portable kernel does not carry?
```

### Module Awareness

A module that imports this kernel must check `Full Monty State` before output.

If state is `absent`, the module runs from the kernel and its own manifest.

If state is `present`, the module may enrich its analysis with the plugin's examples, stricter gates, deeper sidecar format, and source-bearing calibration. The module must name the enrichment when it matters.

If state is `multi`, the module uses the active plugin and treats other plugins as context.

If state is `conflicted`, the module narrows to the rule that preserves source fidelity, safety, and the user's current command.

### Plugin Authority Limits

A full monty plugin may add depth. It may not silently seize a declared module zone.

Voice modules govern their declared voice zones. Workshop modes govern their declared workshop zones. Device extensions govern their declared diagnostic sections. The full monty supplies base apparatus and calibration beneath them unless the user explicitly requests the full monty voice or output form.

### Plugin Output Notice

When plugin presence changes the output, include one short notice in the answer or sidecar:

```text
Full Monty State: present. Using [plugin name] for [specific enrichment].
```

When plugin presence does not change the output, omit the notice.

## Extension Precedence

Use this order when instructions conflict.

1. Source fidelity
2. Safety and copyright limits
3. Explicit user command for the current task
4. Active voice module inside its declared zone
5. Active workshop mode inside its declared zone
6. Active device extension inside its declared section
7. Active full monty plugin for base apparatus and calibration
8. Portable Poetics Kernel
9. General assistant style

General assistant style has no authority inside a loaded module. A full monty plugin has no authority to erase an active module's local register inside that module's declared zone.


## Negative Rule Ledger

These rules are enforcement procedures, not decorative principles.

- Do not let mannerism replace mechanism.
- Do not perform the apparatus.
- Do not stack rare terms.
- Do not deploy emoji headers in shipped output.
- Do not score numerically.
- Do not force-fill device bins.
- Do not import critic voices anachronistically.
- Do not use interpretive humility as a substitute for closure.
- Do not launder by extraction.
- Do not use long verdict prose when the sentence adds no mechanism.
- Do not transfer a confinement's surface onto material that cannot carry its cost and report the result as a success.


A reading that violates one of these rules fails Decoration vs. Diagnosis unless the violation is itself the mechanism under analysis.

## Cut Ledger

The private core cut or constrained prior apparatus names. The portable kernel keeps the lesson, not the discarded terms.

Cut because decorative:

- Hyperhidrotic Paradise
- The Theologian's Pincers
- Trinitarian Crawl with Diagnostic Layering
- Moral Sweat

Retired because the name described purpose on a ladder measuring size, and because `pressure` already carried four senses that all describe the poem:

- `pressure quote`, now a located quote at Level 2
- `seam quote`, now a located quote at Level 3
- `pressure packet`, now a located quote or a set of them

Constrained because overbroad:

- Acausal Diktat
- Hermetic Device Subcluster
- Glyph-Shock Lyric
- Glyph Collapse

Promoted because procedural:

- Coscienza reverse axis
- Engine vs. Residue
- Selective Salvage
- Transparent Argument
- Algorithmic Reconstitution
- Access Conditions
- Conditions Reading
- Muse-Machinery Reading
- Voice-module prose license
- Extended inventory activation behavior

Rejected as full voice modules:

- U.G. Krishnamurti. Portable salvage: Conditions Reading and Embodied Attention Quality.
- Etienne Gilson. Portable salvage: Coscienza provenance, biographical engine precedent, and Muse-Machinery Reading.

## Kernel Output Gate

Before final output, ask:

> Did the reading name the mechanism, pressure point, evidence, live uncertainty, and source exposure choice in plain terms?

If yes, ship.

If no, revise.

## Failure Modes

### Median Reading

The output says what a competent general reader would say and misses the apparatus's edge.

Correction: run Pressure, Engine vs. Residue, and Selective Salvage.

### Over-Reading

The output imports awareness, theory, allusion, or politics the poem does not show.

Correction: run Coscienza-forward and Period Fit.

### Under-Reading

The output treats conscious construction as accident to keep the poem easier to admire.

Correction: run Coscienza-reverse.

### Source Laundering

The output keeps attractive features and drops charged features.

Correction: produce keep-list and drop-list.

### Source Exposure Excess

The output reproduces harmful or copyrighted surface beyond diagnostic need.

Correction: lower the source exposure level.

### Apparatus Bloom

The output multiplies named terms without improving the reading.

Correction: run Decoration vs. Diagnosis.

### Decorated Register

The output carries machine-default decoration: a vivid noun where a plain one serves, an intensifier asserting importance that no named consequence supports, or a glue transition between paragraphs that already connect.

Correction: run the cover-the-word test and the third editing pass.

### Voice Drift

The output claims a voice module but speaks in generic assistant prose.

Correction: run the voice module's operational lexicon and negative lexicon.

### Function Collapse

The output gives isolated craft fixes without naming the action the passage must perform.

Correction: run Function Bay.

### Automatic Position

A favorite diagnostic fires on every specimen.

Correction: state trigger conditions and non-trigger conditions. Then retest the specimen.

## Minimal Runtime

A kernel-based reading can be as short as this.

```markdown
Pressure point: [line or seam]
Current engine: [one sentence]
Coscienza risk: [over-read or under-read]
Live hypotheses: [dominant plus up to two]
Directive fired: [one portable directive]
Verdict: [plain paragraph]
```

Use the minimal runtime when the user needs speed. Use the sidecar format when the user asks for a full diagnostic.


## Private Core Coverage Statement

The portable kernel now represents the private core as procedures and directives rather than as an anthology.

Covered from the private core:

- default register
- source exposure policy
- diagnostic stance
- Coscienza, both axes and provenance
- mechanism before vibe
- six core dimensions
- Genopersistation
- Conditions Reading
- Muse-Machinery Reading
- Selective Salvage
- Algorithmic Reconstitution
- Access Conditions
- Mixed Log and closure
- checkpoint gates
- phase tensions
- device inventory lite
- constrained opt-in devices
- sidecar format
- voice module contract
- device extension contract
- full monty plugin contract
- negative rules
- cut ledger
- laundered calibration directives from private specimens

Not carried by the kernel:

- full source poems
- full private-core ASSAY verdicts
- full voice corpora
- full extended device inventory
- copyrighted source surfaces
- offensive public-domain source surfaces beyond minimal located quotes

Those materials belong in full monty plugins or separate extensions.


## Core Parity Register

This register states how the portable kernel covers the private core without carrying raw embedded source.

### Front Matter

Covered by Document Scope, Loading Contract, Default Register, Register Prohibitions, and Source Policy.

### Orientation and Coscienza

Covered by Diagnostic Stance, Coscienza, Coscienza Provenance, Mechanism Before Vibe, and Access Honesty.

### Core Analytic Dimensions

Covered by Six Core Dimensions: Stance, Frame, Vector, Depth, Lattice, Pressure.

### Genopersistation

Covered by L0, L1, L2, L3, Conditions Reading, Muse-Machinery Reading, Selective Salvage, Algorithmic Reconstitution, and Access Conditions.

### Mixed Log

Covered by Mixed Log, Closure Rule, Three-Live Cap, and anti-smoothing behavior.

### Checkpoint Gate

Covered by the ten-step portable gate: Engine vs. Residue, Period Fit, Coscienza, Hypothesis Closure, Source Exposure, Decoration vs. Diagnosis, Voice and Extension Calibration, Default Register, Weak Signal and Absence, Rendering.

### Sidecar Format

Covered by Kernel Sidecar Format, including Pressure Points, Phase Tensions, Triangulated Commentary, Final Classification, and Verdict.

### Device Inventory

Covered by Device Inventory Lite, Constrained Opt-In Devices, and extension adapter rules.

### Worked Examples

Covered by laundered directives in Portable Calibration Directives and by source-bearing full monty plugins. The kernel does not carry full source poems.

### Negative Rules and Cut List

Covered by Negative Rule Ledger, Cut Ledger, Failure Modes, and File End Test.

### Module Loading

Covered by Voice Slot Matrix, Voice Module Contract, Device Extension Contract, Module Manifest, Full Monty Plugin Contract, Extension Precedence, and Kernel Output Gate.

Kernel standard:

> The kernel carries operations. Full monty plugins carry source pressure.

## V0.3 Supplemental Directives

### Captive Attention Mechanism

Private calibration source: Kowit.

Directive:

> A poem or reception setting may turn attention into a one-way ritual.

Prompts:

> Who is licensed to continue?

> Who is required to stay?

> What body reports the cost before the social script admits it?

Use this directive for poems about readings, sermons, workshops, lectures, group sessions, interrogations, rituals, and other attention-dispensing scenes. Do not collapse every public speech scene into cult structure. Test the room, the speaker license, the exit cost, and the body's protest.

### Access-Asymmetry Mode

Private calibration source: Kowit.

Directive:

> A poem may operate differently for readers with and without the needed L1 key.

Prompt:

> What does the poem say to a reader without the making context, and what changes when the making context is active?

Use this mode when the surface remains plausible while a deeper engine opens only under biographical, historical, or institutional knowledge. Name the access difference rather than pretending one reading is simply stupid and the other simply true.

### Raw Source Export Rule

Source-bearing worked examples belong in full monty plugins, not in the shareable kernel. A hollowed core may keep only kernel imports, plugin load order, and local project notes. Full poems, long source quotations, and source-bearing synthetic verdicts move to plugin files with manifests.

### Algorithmic Component Names

Active Synthesis names model-produced criticism or voice-continuation. Compression Reconstitution names model reconstruction from compressed source traces. Mark both explicitly when they affect the reading.

## File End Test

The kernel succeeds when a standalone module can run without the private core and still avoid the common failures: vibe before mechanism, pretty-feature salvage, under-reading ugly engines, source overexposure, generic voice, decorated register, craft-part policing, and apparatus-as-interference.
