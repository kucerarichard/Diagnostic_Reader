![Diagnostic Reader](./avatar/banner.png)

# Diagnostic Reader

Operator's guide to the Diagnostic Reader, a poetics apparatus that runs on a language model loaded with the files in this bundle. Its standard mode is the diagnostic reading. You put a poem on the page, and the kernel reads it: critic voices take the zones they claim, voices with nothing to say stand down, and the device inventory names devices when it's loaded. A style mode, a scan mode, and the JIG workshop extend the reading. The confinement catalog and the speaker dials serve the workshop. This file covers the parts, the load order, how to invoke each mode, the output policy, and the open work.

This README is apparatus-internal. It names calibration sources, which output never does. Don't paste its tables into a reading.

## Scope

| Mode | Returns | Request |
|---|---|---|
| Reading, the standard mode | A minimal runtime or a full sidecar, with voiced zones and triangulated commentary | `Quick read.` / `Full sidecar.` / `Triangulate this.` |
| VISE style mode | A closing verdict in propulsive cadence, riding a voice | `VISE verdict, PLUMB spine.` |
| Scan Mode | A specimen carrying a named device, then a sidecar on it | `Scan canon A for apostrophe` |
| JIG workshop | A twelve-section craft treatment of a draft, with Confinement Bay, optional rewrite trials, and optional dial trials | `workshop this specimen` |

Catalog work, adding confinements to `12-confinement-inventory`, is the standing maintenance job. The catalog holds 194 entries from 57 specimens.

Limits. The apparatus has no retrieval: it reads what you put on the page. Scan Mode's canon source is the one place it names a poem from the model's own knowledge, and there it rates how well the model can reconstruct the poem and never reproduces it whole. The apparatus doesn't read intention. It quotes in-copyright text only at the lowest exposure level that preserves a mechanism. Generated output never names or identifies a calibration source.

## Files

Versions are the ones in this bundle. For every file the boot registers, its Module Registry agrees with the version below. Registry Gaps lists the files it doesn't register correctly.

Core and policy:

| Stem | Version | Role | Load when |
|---|---|---|---|
| `0-poetics-boot-hollow` | 0.13 | Boot: load order, module registry, plugin registry, Outstanding and Closed lists | Always |
| `0a-portable-poetics-kernel` | 0.3.16 | Kernel: register, reading procedures, checkpoints, directives, designation and source policy, output formats, bay contracts | Always, first |
| `0c-voice-designations` | 0.5 | Designation set, leak tiers, calibration-collision rule for voices, modes, and calibrated extensions | Always, with any voice, mode, or `13` |
| `0b-voice-slot-registry` | 0.5 | Slot matrix, voice test, candidate log, reopen conditions | Only when slot status is in question |
| `0d-apparatus-provenance` | 0.3 | History and rationale. Loaded by nothing | Never; read for background |
| `voice-volitional-map` | 0.2 | The five voices' aims, completion tests, and failures in one table | Never; read for background |

Voices and modes:

| Stem | Version | Role | Load when |
|---|---|---|---|
| `1-rother-voice-module` | 0.3.1 | ASSAY voice; holds the default verdict slot | Reception and canon questions; any reading with no more specific voice |
| `2-harris-voice-module` | 0.3.1 | PLUMB voice | Labor, prison, soldier, body-in-system specimens |
| `3-kowit-voice-module` | 0.3.1 | TARE voice; JIG rides it | Plain speech, body cost, gating; any workshop |
| `3-perloff-voice-module` | 0.3.1 | RETICLE voice | Procedural or avant-garde specimens |
| `5-hersh-voice-module` | 0.1 | DATUM voice | A specimen's account of itself against a record; needs `11` |
| `4-gonzo-mode` | 0.3.1 | VISE style mode; rides any voice | On request |
| `3a-workshop` | 0.6.1 | JIG workshop mode | Workshop requests |

Extensions and notes:

| Stem | Version | Role | Load when |
|---|---|---|---|
| `7-device-inventory-extended` | 0.2 | 189 devices in Categories A to G, the Hermetic re-sort (H), training corpus (I), specimen clusters (J), and Scan Mode (K). Replaces the kernel's lite inventory while loaded | Any reading that needs device-level naming; Scan Mode; workshop; device names for `13` |
| `7a-nom-function-battery` | 0.2 | Five function-level tests built from the inventory's Nôm and English-simulation entries. Runs on every specimen while loaded | Double-surface or script-friction questions; needs `7` |
| `8-frye-extraction` | 0.5 | Radical of presentation, paired fallacy guards, and melos and opsis channel separation. No voice zone | Rendering and reception questions |
| `9-casanova-extraction` | 0.6 | Seven tools and one directive on a work's position in international literary space, gated by a crossing test. No voice zone | A positional claim that changes what the page shows |
| `10-monadology-foundations` | 0.2 | Leibniz foundations for three house disciplines. Fires nothing | When those foundations are in question |
| `11-provenance-grading-extension` | 0.1 | P0 to P5 claim ladder | DATUM; auditing catalog stakes |
| `compartmentalization-engine` | 0.1 | An engine type and a constrained opt-in lens | A poem built around a wound it walls off rather than resolves |
| `12-confinement-inventory` | 0.13 | Confinement catalog | Confinement Bay; catalog work |
| `13-speaker-dials` | 0.2 | Speaker dial catalog: nine dials, four checks, trial forms, eleven experiments | Workshop dial trials; needs kernel 0.3.16 and `3a` |

The stems use the kernel's File Reference Rule: references name the unversioned stem, file names carry the version, and you resolve each stem against what's on disk.

Seven full monty plugins carry source-bearing calibration. Six cover single poems; the seventh covers a critic's book.

| File | Handle | Calibration |
|---|---|---|
| `full-monty-snowcrust-example` | Snow Crust | Floor-origin hypothesis and accidental ars poetica |
| `full-monty-santos-small-branch-v0.2` | Small Branch | Sayability, seam pressure, and appropriation risk |
| `full-monty-wyatt-whoso-list-plugin` | Whoso List | Steganographic surface and load-bearing foreignness |
| `full-monty-kowit-hell-plugin` | Kowit Hell | Complaint loop and comic clarity |
| `full-monty-jeffers-hellenistics-plugin` | Hellenistics | Anti-laundering engine default and transparent ugliness |
| `full-monty-kowit-poetry-reading-plugin` | Poetry Reading | Captive attention and access asymmetry |
| `full-monty-gilson-coscienza-plugin` | none | Source-bearing Coscienza calibration from Gilson's *Dante the Philosopher*, with added directives. `7a` and the Compartmentalization Engine use its Critic's Projection Error directive when it's loaded |

Plugins are private. The apparatus runs without them, and a loaded plugin enriches calibration under the active zones without taking them over. The two Kowit plugins are calibration collisions: TARE stands down for both specimens.

Not in this bundle: `0-poetics-boot`, the original private core, which loads as a legacy full monty plugin when you supply it. The edit scripts, boot companions, and corpus-repair scripts from the catalog sessions aren't here either. Every edit they carried is already in the files above.

### Registry Gaps

The boot calls itself the apparatus's only complete inventory. At v0.13 it disagrees with this bundle in three places:

- It lists `8-frye-extraction`, `9-casanova-extraction`, `10-monadology-foundations`, and the Compartmentalization Engine module as referenced and not held. All four are here.
- It doesn't register `7a-nom-function-battery`, `0d-apparatus-provenance`, `voice-volitional-map`, or the Gilson plugin. No apparatus file references `7a`.
- Its plugin registry gives Small Branch as `full-monty-santos-small-branch-example`. The file on disk is `full-monty-santos-small-branch-v0.2`.

Load from the disk, per the File Reference Rule. The gap is item 16 under Outstanding.

## Loading

The boot's load order:

1. Load `0a-portable-poetics-kernel`.
2. Load `0c-voice-designations`.
3. Load `0b-voice-slot-registry` if slot status matters.
4. Load the extensions the task needs: `7` for device names, `11` for DATUM, `12` for Confinement Bay, `13` for dial trials.
5. Load the voice modules.
6. Load modes last, since VISE and JIG both ride a voice.
7. Load plugins only when source-bearing calibration is needed.
8. Set Full Monty State. The default is absent.

The order is tolerant. A file that arrives later applies from the next turn.

**Warning:** load `0c-voice-designations` before any voice module. Without it, every voice labels its output with its calibration source's name, and the apparatus is out of policy from the first verdict.

Hard dependencies: `5` needs `11`. `7a` needs `7`. Confinement Bay needs `12`. Dial trials need `13`, which needs kernel 0.3.16 and names its devices from `7` at 0.2 or later.

Minimal sets by task:

| Task | Load |
|---|---|
| Quick reading | `0a`, `0c` |
| Full reading | `0a`, `0c`, `7`, and the voice modules the specimen calls for |
| Triangulated reading | `0a`, `0c`, `7`, and at least two voice modules |
| Record-against-account reading | `0a`, `0c`, `11`, `5` |
| VISE verdict | The reading set plus `4` |
| Scan Mode | `0a`, `0c`, `7` |
| Workshop | `0a`, `0c`, `3-kowit`, `3a`, `12`, and `7` for device names |
| Workshop with dial trials | The workshop set plus `13` |
| Catalog extraction | `0a`, `0c`, `11`, `12`, and `3a` for the Bay's field contract |

A missing file switches off what depends on it, and the apparatus says so rather than rebuilding the file's contents from memory. Without `7` a reading uses the kernel's lite device bins. Without a voice module, that voice appears as a compressed note in the default register or stays absent.

## Readings

The reading is the apparatus's standard mode. The kernel defines it, the voice modules take its voiced zones, and the device inventory sets its device resolution. VISE and Scan Mode end in a reading, and the workshop borrows the reading's gate.

### Requesting a Reading

Put the poem on the page with its poet, date, and edition:

```text
Quick read. Robert Frost, "After Apple-Picking," North of Boston (1914).

[poem text]
```

Reading requests are plain language. The kernel and the voice modules define the conditions a request meets, not fixed command strings, so these forms are examples rather than a grammar:

```text
Quick read.                                      minimal runtime
Full sidecar.                                    full diagnostic; voices take the zones they claim
Triangulate this.                                sidecar with commentary from every voice that has something distinct to say
Triangulate PLUMB and DATUM. PLUMB closes.       named voices; named verdict voice
ASSAY verdict.                                   one voice on the closing verdict
Add TARE as counter-voice.                       a second voice in a zone another voice holds
DATUM verdict on the poem and its note.          omission audit of the poet's account against the page
Run the Hermetic chamber reading.                Section H lens, where the poem's structure warrants it
Full battery report.                             all five Nôm battery grades, non-triggers included
```

Operator input isn't governed by the designation policy, so `Rother verdict` and `ASSAY verdict` reach the same voice. Output carries the designation either way. A reading names its specimen in full; the policy masks who supplies the register, never who wrote the poem.

### Minimal Runtime

The kernel's short form, for when you need speed:

```markdown
Pressure point: [line or seam]
Current engine: [one sentence]
Coscienza risk: [over-read or under-read]
Live hypotheses: [dominant plus up to two]
Directive fired: [one portable directive]
Verdict: [plain paragraph]
```

Filled in for the request above, abridged and written for this README:

```markdown
Pressure point: the close, where the speaker can't say whether his coming sleep is the woodchuck's or "just some human sleep."
Current engine: exhaustion turns the finished harvest into a dream the speaker can't classify.
Coscienza risk: over-read. The death reading is available, and the poem holds it level with ordinary sleep rather than choosing it.
Live hypotheses: dominant, the sleep stays unclassified; qualified-live, the harvest stands for a finished life's work.
Directive fired: Weak Signal. The one witness who could answer is gone, and the close turns on that absence.
Verdict: The poem won't settle what kind of sleep is coming. A reading that names it death supplies the answer the poem withholds.
```

The same poem is the catalog's Apple-Picking specimen; see Confinement Inventory for the entries extracted from it.

### Sidecar

Ask for the sidecar when you want the full diagnostic. Its fields, from the kernel:

```text
## [Specimen Title]
### Provenance                date, source, author, making context, source status
### Architecture              the structural shape in mechanism terms
### Fracture Surface          strain, rupture, seam, overfit, underfit, contradiction, turn
### Coscienza                 forward axis and reverse axis
### Core Dimensions           stance, frame, vector, depth, lattice, pressure
### Device Inventory          only devices that fire, with period fit
### Mixed Log                 dominant, qualified-live, and closed hypotheses with reasons
### Genopersistation          L0, L1, L2, L3
### Rendering Note            only when the rendering is degraded or heavy
### Pressure Points           what removal would cost the poem most
### Phase Tensions            Failed System, Intentional Glitch, Transparent Argument, or open
### Portable Directives       each directive that fires
### Triangulated Commentary   voices with something distinct to say, each in its own person
### Final Classification      type, operating mode, infrastructure, pressure point, resonant line, diagnostic lesson
### Verdict                   plain prose, or the bound voice
```

Field labels stay in the default register even in a voiced sidecar; a voice writes the prose inside its zone, never the label. Empty bins stay empty, and a dimension or layer with nothing in it can be omitted when omission is clearer than a filled list.

The kernel's Rendering Conditions include a self-interference clause. The sidecar is itself a rendering that taxes the reader, and when a plain reading would serve the poem better, the apparatus says so and gives the plain reading.

### Kernel Procedures

Every reading runs under the kernel's operating rules. Among them: treat the poem as conscious until evidence shows otherwise; name the mechanism before the mood; attach every framework term to evidence; keep no more than three live hypotheses at output; cut every apparatus term that decorates.

Coscienza checks awareness on two axes. The forward axis bars crediting the poem with awareness it doesn't show. The reverse axis bars protecting the poem from awareness it does show. Its prompt:

> Where am I assuming the poet did not know what they were doing? What evidence supports that assumption?

Engine vs. Residue asks whether removing a feature collapses the poem's argument. Politically charged, violent, classed, gendered, or coercive material defaults to engine and moves to residue only after a counterfactual reading proves the poem survives without it.

The six core dimensions each carry a prompt:

| Dimension | Prompt |
|---|---|
| Stance | Who is speaking, and from what posture? |
| Frame | What setup licenses the content? |
| Vector | Which way is the poem trying to pull the reader, and is the pull declared or hidden? |
| Depth | How many things is the poem doing at once, and how do they coordinate? |
| Lattice | What holds the poem up, and where is it under stress? |
| Pressure | Where would removal collapse the poem? Every reading names at least one pressure point. |

Genopersistation names the layers by which a poem persists:

| Layer | Covers | Operations that run there |
|---|---|---|
| L0 artifact surface | The page: words, syntax, sound, lineation, image, punctuation | Rendering Conditions, for load the page's presentation adds |
| L1 compositional making | Making conditions that bear weight | Conditions Reading; Muse-Machinery Reading for long careers |
| L2 institutional support | Publishers, anthologies, prizes, schools, platforms | Conditions Reading |
| L3 reception management | Critical traditions, syllabi, reputational repair | Selective Salvage; Algorithmic Reconstitution when model output is part of the reading |

The Mixed Log keeps hypotheses live until evidence closes them:

```text
Hyp A: [claim]
Evidence: [support]
Status: dominant / qualified-live / closed
Reason: [closure reason, if closed]
```

A hypothesis closes when the text contradicts it, a documented authorial statement contradicts it, or a rival explains the same features without remainder. Interpretive humility doesn't close a hypothesis. At output, one is dominant and at most two are qualified-live.

Phase Tensions classify the poem's strain as Failed System, Intentional Glitch, or Transparent Argument, named only after the Mixed Log has been tested.

The Portable Calibration Directives state a hard specimen's diagnostic force as a prompt. The kernel holds nineteen: Floor-Origin Hypothesis, Accidental Ars Poetica, Steganographic Surface, Weak Signal, Load-Bearing Foreignness, Sayability Test, Appropriation Risk, Seam Pressure, Anti-Laundering Engine Default, Register Is Not Referent, Transparent Ugliness, Complaint Loop, Body-Cost Rule, Cult-Gating Diagnostic, Plain Speech as Anti-Laundering, Defamiliarization Engine, Function Before Parts, Parasitic Effort, and Access Honesty. Two supplemental directives follow them: Captive Attention Mechanism and Access-Asymmetry Mode.

Six constrained opt-in devices fire only on their stated warrant: English-Nom Hybrid Signals, Crip Space-Time Deformation, Acausal Apparatus, Hermetic or Alchemical Chamber Reading, Compartmentalization Engine Reading, and Embodied Attention Quality. Acausal Apparatus fires only on an explicit request and requires the apparatus to declare its philosophical commitment first.

### Checkpoint Gate

Every reading passes ten checks before it ships:

| Checkpoint | Question |
|---|---|
| 1 Engine vs. Residue | Would removing the most charged feature collapse the poem's argument? Is any claimed confusion one of sound or of sense? |
| 2 Period Fit | Was this device, frame, or vocabulary available at the moment of composition? Later frames are marked retrospective. |
| 3 Coscienza | Is the apparatus over-crediting or under-crediting awareness? |
| 4 Hypothesis Closure | Have live hypotheses been resolved under the closure rule? |
| 5 Source Exposure | Does the reading quote only what it needs? |
| 6 Decoration vs. Diagnosis | Does each named term reveal a mechanism the reader would otherwise miss? |
| 7 Voice and Extension Calibration | Does voiced output obey its module, speak in voice rather than report, and carry a designation? |
| 8 Default Register | Does the unvoiced prose obey the default register? |
| 9 Weak Signal and Absence | What is faint here that does heavy work, and what is missing that this kind of poem would carry? |
| 10 Rendering | Is any difficulty judgment contaminated by the rendering? |

The kernel's output gate closes the run:

> Did the reading name the mechanism, pressure point, evidence, live uncertainty, and source exposure choice in plain terms?

### Voices

Five voice modules can take zones in a reading. A voice declares its zones, governs only those, and speaks in its own person inside them. The default register governs everything else.

| Designation | Calibration source | Unit | Fires when | Holds silent when |
|---|---|---|---|---|
| ASSAY | Rother | a ranking | A work is valued above or below what its inheritance earns | No misfiling to correct |
| PLUMB | Harris | a witness | A system hides its cost and there's ground to stand on | No ground, or the subject sits above the body |
| TARE | Kowit | a relationship | Cost is laundered or a reader is gated | A difficult poem earns its difficulty |
| RETICLE | Perloff | a genealogy | A procedure is present and misnamed as noise | The force is narrative, bodily, or vernacular |
| DATUM | Hersh | a record | An official account and a record both exist | Either is missing, or interpretation was asked for |

Every voice can hold the closing verdict and a triangulated commentary paragraph, and every voice except DATUM can translate the device inventory into its register. Each also holds special zones: ASSAY an institutional-rhetoric auxiliary; PLUMB a body-in-system witness section; TARE the cult-gating, body-cost, and moral-substrate diagnostics; RETICLE lineage placement and a re-readability test; DATUM the omission audit.

Which voice takes the verdict:

- ASSAY holds the default verdict slot. With no more specific voice loaded, it closes.
- A voice whose specimen conditions hold is more specific and takes the verdict.
- The specific cases: PLUMB for labor and institutional harm, TARE for plain speech and bodily cost, RETICLE for formal procedure, DATUM for an account measured against a record.
- ASSAY stands down where the live question is what an account omits, even though the slot would otherwise fall to it.
- One voice per zone. A voice stays inactive when another holds the zone, unless you ask for it as counter-voice.
- A voice whose calibration source wrote the specimen stands down, recorded as a jurisdiction note with no stated cause.

In triangulation, each voice with something distinct to say speaks in its own person under its designation, and the disagreement stands unsmoothed. A loaded voice with nothing to say holds silent or leaves a compressed note. The shape, with the voiced prose left out:

```text
### Triangulated Commentary

PLUMB
[first person: what the system cost, at ground level]

DATUM
[first person: what the poem's note leaves out, each claim graded]

PLUMB and DATUM disagree on the guarantor. The verdict rests on the record.

RETICLE has little distinct purchase here. The poem's force is narrative, bodily, or vernacular rather than formal-procedural.
```

The pairings are built to disagree, and the modules state what each disagreement tests:

| Pair | What the disagreement tests |
|---|---|
| PLUMB and DATUM | Presence at the scene against the record as guarantor. State which one carries the verdict. |
| ASSAY and DATUM | Reassigning a work's position against recording what its account omits. Write adjacent sections; neither annexes the other. |
| TARE and RETICLE | Plain speech against defamiliarization as the anti-laundering move. Each suspects the other's virtue of being a gate or a platitude. |
| RETICLE and DATUM | The procedure read off the page against the poet's account of it. |
| ASSAY and TARE | Whether plainness has become a virtue signal, or sophistication a gate. |
| PLUMB and RETICLE | Where a formal claim touches a body, against what procedure makes the body legible as writing. |
| PLUMB and TARE | Reporting a system through bodies, against testing the depth of life the poem springs from. |

A bound zone is written in the voice, never about it. Checkpoint 7 fails reported speech:

```text
Fails:   TARE would say the turn comes when the poem shows the cup in the sink.
Passes:  The turn happens when the poem stops telling us what grief is and shows us the cup in the sink.
```

The passing line is the TARE module's own device-translation example. Device translations differ by register: TARE renders devices as craft action, PLUMB in plain working terms, and RETICLE keeps the formal names, which are native to its register.

Voiced blocks carry one designation label and count as Active Synthesis, never a statement by the real critic:

```text
ASSAY verdict:
PLUMB verdict:
TARE verdict:
RETICLE verdict:
DATUM verdict:
```

The ASSAY, TARE, and RETICLE modules still instruct labels built from their sources' names. `0c-voice-designations` supersedes that one instruction at runtime, which is why it loads before any voice.

DATUM reads a poem through the poet's own account of it: an author's note, an interview, a jacket claim, a headnote. Its procedure records the account at P2, attributed on the record, and reads the poem at P0, on the page. It then names where the account diverges, grades the divergence, and enters a thing the account should mention and doesn't as P5. It closes by naming what the omission protects. The verdict records the gap and stops. A poem with no account of itself gets no DATUM verdict.

Extractions have no voice zone. When `8`, `9`, or `13` meets a voice on the same specimen, the voice speaks and the extraction enters as a note in the default register. A reading where that happens states the imbalance.

### Devices in a Reading

Without `7`, the Device Inventory field draws on the kernel's lite bins: Frame, Voice, Tense and Mood, Lattice, Reference, Closure, and Ethical devices. Loading `7` replaces the lite bins for every reading; the two never run in parallel.

| Category | Devices | Count |
|---|---|---|
| A | Deictic and scalar | 24 |
| B | Sonic and prosodic | 30 |
| C | Syntactic and sentence | 30 |
| D | Figural and rhetorical | 33, of which 4 are Nôm or English-simulation |
| E | Structural and compositional | 31 |
| F | Visual and typographic | 20, of which 5 are Nôm, simulation, or wildcard |
| G | Pragmatic and ethical | 21 |

Period fit applies to every named device, and bins stay empty when nothing fires; forced fill fails Checkpoint 6. The Nôm and English-simulation entries stay behind the English-Nom Hybrid Signals opt-in. Section H, the Hermetic or Alchemical Chamber Reading, re-sorts the devices into vessels, seals, valves, and transmuters. It fires on the specimen's structural warrant, and a request runs it only where that warrant exists. Its prompt:

> Identify the chamber. What V devices define it? What S devices close it? What Va devices regulate its breathing? What T devices are running inside it? What is the chamber producing as output that it did not contain at input?

A chamber that is sealed but produces nothing new is the failure the lens exists to catch.

### Reading Extensions

These attach to an ordinary reading without adding a mode. Each announces itself only when it changes the output.

`8-frye-extraction` adds a radical-of-presentation field: acted, recited, sung or overheard, or written. It adds a changed-radical note when reception delivered the poem through a different channel:

```text
Frye Extraction: [tool name] applied.
```

`9-casanova-extraction` adds a position note only when it can name the textual feature the position explains. A position note with no feature attached is cut.

`7a-nom-function-battery` runs five tests silently on every specimen and reports fires at point grade or above inside the sidecar. Its grades are systemic fire, point fire, faint, and non-trigger. `Full battery report` reports all five with page evidence:

```text
Nôm Function Battery v0.2: active. Five function-level trigger tests running per specimen; grades reported at point fire or above. Test 3 margin scan runs when live.
```

The Compartmentalization Engine fires when a poem walls off a wound rather than resolving it. In a sidecar it adds a wall-structure note under Architecture. Its minimal runtime:

```text
Wound: [the injury, and the decay through it]
Walls: [which hold, which fall, in what direction]
Barrier zone: [the post-wound seal, and its fracture plane]
Hollow / re-wounding: [present or absent]
Mode: [Failed System / Intentional Glitch / Transparent Argument]
Reads or performs: [does the sealing reward attention]
```

A loaded full monty plugin enriches calibration under the active zones and announces itself when it changes the output:

```text
Full Monty State: present. Using [plugin name] for [specific enrichment].
```

### High-Risk Specimens

For source material that shouldn't be reproduced, the kernel supplies a redacted specimen card:

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
The core text withholds [material type]. The retained mechanism is [mechanism].
```

### Precedence

When instructions conflict, the kernel resolves them in this order:

1. Source fidelity.
2. Safety and copyright limits.
3. Your explicit command for the current task.
4. An active voice module inside its declared zone.
5. An active workshop mode inside its declared zone.
6. An active device extension inside its declared section.
7. An active full monty plugin, for base apparatus and calibration.
8. The kernel.
9. General assistant style, which has no authority inside a loaded module.

## Style Mode

VISE changes the cadence of a closing verdict and supplies none of its judgment. It rides a voice and names that voice, its spine, in the label. It fires on `VISE`, on the retired name Gonzo Mode, or on a request for a glitched-prose, overdrive, or drag verdict:

```text
VISE verdict, PLUMB spine.
```

The verdict is one sentence by default, with no internal periods. Semicolons and colons carry the pivots, parentheses carry nested asides, and the predicate piles up named specifics until closure arrives by exhaustion. Dashes are permitted inside the verdict as a local exception to the default register. The module's skeleton, a pattern rather than a template:

```text
VISE verdict, [spine] spine:

The poem, having promised [surface promise] and having driven that promise through [specific catalog], finally reveals that [diagnostic turn]; [additional clauses accumulate the pressure], until the reader is left with [pressure point], which is not relief but the bill coming due.

Due.
```

At most two voices ride one VISE verdict, and three never do; write adjacent verdicts instead. VISE doesn't fire by default. It stays off for a serious standard sidecar, a small or delicate poem, thin facts, or volatile material where voltage would turn witness into spectacle.

## Scan Mode

Scan Mode lives in Section K of `7-device-inventory-extended`. You name a source, a Category, and one or more devices. The apparatus finds a specimen carrying them, verifies each device in the text, and runs a sidecar at extended-inventory resolution:

```text
Scan canon A for apostrophe
Scan canon A for apostrophe and pronoun shift
Scan supplied B for caesura
Scan list categories
Scan list D devices
```

`canon` names a canonical poem from the model's own knowledge, with author, title, and a standard reference so you can reach the text. The output rates reconstruction strength as strong, weak, or asymmetric, and flags consensus smoothing when the sidecar is averaging existing readings. `supplied` scans a corpus you put on the page. Multiple devices are conjunctive by default; ask for OR to loosen it. The source flag is required, and the apparatus never substitutes one source for the other.

An empty scan is a result. If nothing in the named source carries the devices with reasonable confidence, the apparatus reports the empty scan and stops. It doesn't relax the criteria or fabricate a candidate; re-tuning is your call.

Section K predates the kernel's removal of retrieval and still prints venue lists and fetch rules. A guard at its head says they don't run: read Source B as an operator-supplied corpus and `Scan feedback` as `Scan supplied`. Specimen integrity, deanonymization refusal, and the bias flag still apply.

## Workshop

JIG is a side mode that grew out of the TARE voice module. Its calibration source is Kowit's workshop book, the same source behind TARE, and it rides TARE's register; without the TARE module it runs in a fallback register distilled from the same book. The kernel files it as a user-triggered mode: it treats a poem as a draft and doesn't replace the sidecar unless you ask for workshop treatment. The confinement catalog and the speaker dials both exist to serve it.

JIG fires on these requests:

```text
workshop this specimen
workshop mode
JIG this
give this the workshop treatment
```

It runs only on a poem you supply. Asked for a random poem, it says it has no retrieval and asks you to paste one. The treatment opens with a specimen card:

```text
Author:      [the user / named third party / handle as given / anonymous]
Provenance:  [the user's own draft / posted for critique at X / published in Y / public domain]
Copyright:   [the user's / in copyright / public domain / unknown]
Length:      N lines, or N sentences for a prose poem
```

Provenance routes the request: a draft gets the workshop, finished work gets the sidecar. Copyright sets the exposure ceiling. Your own draft is quoted as freely as the critique needs; a third party's in-copyright poem caps at Level 3. If you supply someone else's poem without provenance, JIG asks once.

The treatment has twelve sections: Opening Reading, Image Inventory, Sound and Cadence Scan, Line Break Analysis, Diction and Language Check, Form Examination, Voice and Moral Substrate, Confinement Bay, Engine Bay, Function Bay, Revision Routes, and Workshop Verdict. With the TARE module loaded, TARE speaks the verdict. Every treatment closes on the same question:

> What is the poem honest enough to say, and where is it still pretending to be a poem?

The three bays descend in scale. Confinement Bay works at condition scale, on what the poem is able to know. Engine Bay works at poem scale, on what drives it, and names the Defamiliarization and Compartmentalization Engines when the draft supports them. Function Bay works at passage scale, on what one passage performs, and ends with one experiment. Confinement Bay's extraction and breach scan are standard. Engine Bay, Function Bay, and every kind of trial are optional, and an omitted section is left as an honest gap rather than renumbered away.

### Confinement Bay

Confinement Bay runs extraction and a breach scan on every workshop. Extraction reports the draft's own confinement in the catalog's fields:

```text
Position:       what the draft cannot know from where it stands
Surface:        the repeating rules that show on the page
Fold:           how those two route the withheld thing to the reader
Active site:    the small place where the confinement does its work
Forbidden:      the defaults the draft has closed off
Knowledge test: what is unavailable to the speaker, not merely unsaid
Axis:           upward, sideways, inward, or outward
```

An empty knowledge test means the draft is running a form, which routes to Form Examination. The breach scan finds where the draft breaks its own confinement and says whether the break is the poem's one earned exception or a slack default. Rewrite trials run only on command:

```text
confinement rewrites
rewrite under found inscription
rewrite under withheld case + flat predicate
rewrite under axis: upward
rewrite under imposed by: institution
rewrite under handle: Snow Crust
+ ars poetica
extract confinement
list confinements where axis = inward
no rewrites
```

Each trial ships in this form:

```text
Trial:    [confinement name, or names, plus any overlay]
Span:     [what was rewritten]
[the rewrite]
Reached:  [what this trial got to that the draft's own confinement made unreachable]
Seam:     [where it failed, named]
```

Trial rules:

- Two trials by default and three at most.
- Three primitives per trial at most, one refusal primitive at most, and one overlay at most. A dial setting counts as the overlay.
- Past about twelve lines, a trial rewrites a declared span rather than the whole poem.
- Selection runs against the draft's axis when nothing is named.
- The workshop abstains rather than force a trial whose stake warns against the draft.

Under the trial firewall, a trial is a contrast trial and never the poet's next draft. It enters Revision Routes only when the draft's own material supports the move, and the route is stated from the draft.

### Stand-downs

JIG stands down for any specimen whose author calibrates its own material, which currently means Kowit's poems. You can take a standard sidecar under a voice that doesn't collide:

```text
Jurisdiction: JIG stands down for this specimen.
```

A specimen by either author of the book that calibrates `13` stops only the dial operations. The rest of the treatment runs:

```text
Jurisdiction: dial trials stand down for this specimen.
```

Where both apply, JIG stands down.

## Speaker Dials

`13-speaker-dials` gives the workshop a second kind of trial. A dial is a setting of how the speaker talks, such as diction altitude or idiom density, and every poem sits at some setting on every dial. Turning a dial changes how the poem says what it knows and leaves what it knows in place. A dial therefore fails the knowledge test by construction, and the catalog admits dial settings as overlays rather than as entries.

A dial trial is a probe. It turns one setting to find what the draft holds that the current setting keeps off the page: a fact, a cost, a body, a relation, a feeling. A trial that only changes how a span sounds has reached nothing and reports it. This is the operator's ruling at the dial file's v0.2.

### Dial Set

| Dial | Status | Settings | Checks |
|---|---|---|---|
| sd-01 diction altitude | established | low, middle, high; high is ornamental or clinical | laundering, gating |
| sd-02 assertion position | established | none, opening line, middle, near the close, last line | open-or-corner, gating |
| sd-03 phatic density | established | bare, sparse, conversational, padded | laundering |
| sd-04 idiom density | established | none, flavored, steady, saturated, each with a named lingo source | laundering, gating, appropriation |
| sd-05 visible revision | provisional | finished, qualified, revising | none |
| sd-06 tempo | provisional | fast, measured, slow | none |
| sd-07 certainty | provisional | assured, hedged, unsure | none |
| sd-08 speaker count | provisional | one, quoted, several, self-quoted | appropriation |
| sd-09 host form | provisional | a borrowed public form, or none, plus a power direction | gating, appropriation |

A setting is named by the located words that fix it and is never scored. The provisional dials have ranges the apparatus supplied, and each trial's seam reports whether the range held on the draft; promotion is the operator's call. Five dimensions already named in the device inventory don't run as dials: address, self-disclosure, noun habitat, dual diction, and occasion mismatch.

### Dial Commands

```text
dial trial                                            reasoning path selects the dial and setting
dial trial: idiom density                             named dial; setting selected against the draft
rewrite at diction altitude: high                     named dial and setting
rewrite under fixed vantage + diction altitude: low   dial overlay on a confinement trial, run as a pair
list dials                                            index from the dial file
no dial trials                                        suppress dial trials and overlays for the session
```

Dial trials run only on command. In Function Bay a dial trial is the contrast trial: the wrong-way trial turns the dial one way and the cleaner trial the other. In Confinement Bay a dial overlay runs as a pair, the same confinement trial without the setting and then with it. In Engine Bay, Tuning Before Swap may ask which dial setting works against the current engine; a dial tunes an engine and never proposes one. Function Bay's closing experiment may come from the dial file unasked.

### Dial Trial Form

```text
Dial:     [name], from [draft's setting] to [trial setting]
Span:     [address]
[the rewrite]
Reached:  [what real thing surfaced, and the draft line where it was latent]
Seam:     [where it failed, named]
```

A trial that surfaced nothing reports it and ships only as that report:

```text
Reached:  nothing, setting only
```

The thing surfaced has to be in the draft already; a trial that invents a fact or a feeling has written a different poem. In an overlay pair, trial 2's seam reports what changed at the fold, and names carrier denaturation when the confinement's position and surface survive the change of setting and its fold doesn't. The pair counts as Confinement Bay's two default trials, and the dial setting uses the one overlay slot, so `+ ars poetica` and a dial setting never share a trial.

### Dial Rules and Checks

- Turn one dial one step per trial.
- Hold what the entry's `Holds fixed` field names, and hold or report any coupled dial.
- Run one dial trial pair per Function Bay target passage and one overlay pair per treatment.
- Leave trial text at the trial's setting. An upward sd-03 trial contains the asides and filler the default register bans; they stay in the trial and out of the commentary.

When nothing is named, selection looks first for cover, a setting that protects something, such as a high span over a death or idiom hurrying past a fact. The apparatus points to the line where the cover sits or doesn't claim it. Otherwise it selects against the draft's setting, and abstains with the page test alone when every candidate fails its checks.

Each check is a prompt answered before the trial ships:

| Check | Prompt | Mandatory on |
|---|---|---|
| Laundering | Does the trial setting make the draft's cost easier to accept than the draft made it? | Upward sd-03; every sd-04; sd-01 moving bodily or ethical material toward high |
| Gating | Does the trial setting sort readers into those it rewards and those it shuts out? | sd-01 toward high; every sd-04; sd-02 moving the assertion early; sd-09 voicing the form's power |
| Open or corner | Does this general sentence open the details around it, or corner them? | Every sd-02 |
| Appropriation | Whose talk is the trial borrowing, and does it belong to the draft's world? | sd-04 changing lingo source; every sd-08 and sd-09 |

A trial that launders or fails appropriation doesn't ship as a success. sd-07 is the one dial that can cross into a confinement. Before turning it, the apparatus asks whether the speaker is unsure how to say something or unsure what happened. The second is a knowledge limit, and the trial goes to Confinement Bay.

The dial file also converts fourteen of its source's drills into eleven experiments, operations the poet runs on the poet's own draft. ex-04, on sd-02:

> Find the one general sentence the poem's details answer to. Make three copies of the poem with it first, in the middle, and last, changing only the lines on either side of it.

### Dial Calibration

The calibration source is Tony Hoagland with Kay Cosgrove, *The Art of Voice: Poetic Principles and Practice*, in copyright and held at Level 0. Its chapter terms are Tier B coinages and never reach output. The source was never put to the voice test, and the dial file occupies no voice slot.

The dial file's source and the workshop's part at four points. The operator ruled on the three that were open, each for the workshop's position: a speaker is worth hearing for the depth of attention behind the lines; plain speech exposes cost rather than dressing it; the reader stays a peer. The fourth, abstraction, was already settled by the kernel's open-or-corner test.

## Confinement Inventory

A confinement is a pattern of absence that makes something unknowable from where the poem stands. A constraint is elected, and reading election would mean reading intention, so the catalog records only what the page enforces. Every entry must pass the knowledge test: something is unavailable to the speaker, not merely unsaid. A poem that fails the test is running a form, and it routes to Form Examination.

Each entry works on three levels:

- Position: what the writer can't know from where the poem puts him.
- Surface: the repeating rules that show on the page.
- Fold: what the two force the material into once both are running and something still has to be said.

Position and surface transfer to new material. The fold usually doesn't, because it was held in shape by what the confinement cost the original. That failure is denaturation, and the `stake` field exists to warn about it before a trial runs.

The entry schema:

```text
id:               cf-[handle initials]-[NN]
name:             lowercase words, never capitals
handle:           the specimen handle
rights ceiling:   exposure level available, and the level held here
axis:             upward / sideways / inward / outward
imposed by:       the agency that sets the limit
position:         [primary]
surface:          [secondary]
fold:             [tertiary]
active site:      [where the work happens]
forbidden:        [the blocked defaults]
knowledge test:   [what becomes unknowable]
stake:            [the cost the page shows, at P0; any cost to the poet, graded; what does not transfer]
assembly:         [combines with / cancels with]
engines admitted: [which whole-poem drives this enclosure will run]
device cluster:   [Extended Device Inventory categories]
stand-down:       [none, or the flag]
```

The four axes:

| Axis | Meaning |
|---|---|
| upward | Withheld from a power that can punish the speaker |
| sideways | Withheld behind decorum, in front of people who supply the missing term |
| inward | Withheld from the poem itself, which won't say what it knows |
| outward | Withheld by no one; the limit lies past what the speaker's position can reach, such as sleep, death, the future, or the sea |

The catalog's sections:

- A: composites, one per specimen, not combinable.
- B: primitives, two to four per specimen, combinable.
- C: overlays. The catalog holds one, accidental ars poetica, which fires only on explicit `+ ars poetica`. Speaker dial settings are overlays under the same definition and cap, and live in `13`.
- D: combination tables. These hold the refusal ceiling, the overlay cap, the recorded cancellations and live pairs, and the recurrence notes.
- E: the selection rule.
- F: rights and stand-down rules.
- G: the Candidate Log of extracted, held, rejected, and deferred items.
- H: failure modes.
- Provenance: a table per batch.

The list commands draw on the catalog's two index tables. These rows are the primitives extracted from the Frost poem in the reading example above:

```text
| id       | name               | handle        | axis    | imposed by                                       | operation                                                   |
|----------|--------------------|---------------|---------|--------------------------------------------------|-------------------------------------------------------------|
| cf-ap-02 | absent arbiter     | Apple-Picking | outward | the absence of the one witness who could answer  | Name who could settle the question; do not answer for them  |
| cf-ap-03 | residual labor     | Apple-Picking | outward | a body that keeps the work after it stops        | The finished work returns as sensation and is read forward  |
| cf-ap-04 | unclassified state | Apple-Picking | outward | a state whose kind cannot be known from inside it | Two kinds of one state held level; neither chosen           |
```

cf-ap-04 is the catalog's most-rediscovered primitive; see Confinement Recurrence.

Contents at v0.13, unchanged from v0.12:

| Source | Specimens | Notes |
|---|---|---|
| Seeds: Wyatt, a New England broadside, Santos | 3 | Whoso List, Snow Crust, Small Branch |
| Rodman, One Hundred American Poems (1948), optical character recognition corpus | 11 | Attribution repaired by script |
| Stand Up Poetry: An Expanded Anthology (2002), optical character recognition corpus | 10 | Lineation damaged; Kowit and two reprinted poems excluded |
| In Fortune's Twilight (1900), JavaScript Object Notation lines | 10 | Author unidentified |
| Santos, McGrath, Vuong, three recent books | 5 | None from McGrath |
| Beckett, seventeen poems of the 1930s and 1940s | 9 | Grammar as the carrier |
| Hồ Xuân Hương in John Balaban's translation | 9 | The device inventory's calibration case for the Nôm opt-in |

That comes to 57 composites and 137 primitives. By axis the split is thirteen upward, seventeen sideways, twelve inward, and fifteen outward. Entries hold at Level 0 throughout, and none carries its source's wording.

v0.13 extracted nothing. It admitted dial settings as a second class of overlay and deferred a `carrier` field, because back-filling 194 entries needs every specimen's text on the page.

## Adding Entries

Each batch in the catalog followed this procedure:

1. Examine the corpus before extracting. Check attribution, record boundaries, lineation, excerpts, rights, and edition.
2. Repair attribution by script when it's broken. The script edits headers only and asserts on each line it expects, so in-copyright text never passes back through the model.
3. Check collisions. Exclude a poem whose author calibrates a voice or a mode.
4. Exclude a poem reprinted inside a calibration corpus with the source's commentary, including the dial file's.
5. Read candidates in full and apply the knowledge test. Take whole poems only; an excerpt's limit is the anthologist's cut.
6. Select up to the batch ceiling, breaking ties by the thinnest axis.
7. Write one composite and two to four primitives per specimen.
8. Write each stake field with the page's cost first at P0, then any biographical cost graded on the P0 to P5 ladder.
9. Check assembly against the existing entries.
10. Record cancellations, live pairs, and recurrences in Section D.
11. Update the index tables, the Candidate Log, the Provenance table, and the revision note.
12. Register the new catalog version in the boot's Module Registry, with a version note.

Step 3 exists because entries from a colliding author would stand down in JIG, the catalog's only consumer. A poem by the dial file's source can enter, but its entries stand down for dial overlays.

Ids follow three rules. Take handle initials. If those collide, take the first two letters of the handle's first word. Numbered titles in a series take the title's first letter plus a letter for the number, so Enueg I is `cf-ea`.

## Confinement Recurrence

Counts come from `12-confinement-inventory` v0.12, and v0.13 changed no entries, so they hold: 57 specimens, 137 primitives, and 35 recorded recurrence links. The three seed specimens had nothing earlier to recur against, so rates use the other 54. Dates are approximate years of composition or first publication, most of them from memory (P4, the apparatus's own inference).

### Overall Rates

| Measure | Count | Share |
|---|---|---|
| Specimens that run at least one primitive from another specimen | 29 of 54 | 54% |
| Specimens that run another poet's primitive | 28 of 54 | 52% |
| Specimens with no recorded recurrence | 25 of 54 | 46% |
| Primitives found again in a second specimen | 27 of 137 | 20% |
| Primitives found again in two or more other specimens | 7 of 137 | 5% |
| New primitives per recorded recurrence | 137 to 35 | about 4 to 1 |

### By Period

| Period | Specimens | Run an earlier primitive | Rate |
|---|---|---|---|
| 17th century (Taylor) | 1 | 0 | 0% |
| Around 1800 (Hồ Xuân Hương, Vietnam) | 9 | 5 | 56% |
| 1850 to 1899 (Longfellow, Dickinson) | 3 | 1 | 33% |
| Turn of the century, 1900 to 1920 | 14 | 9 | 64% |
| Interwar, 1921 to 1945 | 12 | 5 | 42% |
| Post-war to 2002 (stand-up) | 10 | 4 | 40% |
| 2003 to 2019 (Santos) | 2 | 2 | 2 of 2 |
| Post-pandemic, 2020 on (Vuong) | 3 | 3 | 3 of 3 |

The rate also rises with the size of the catalog at the time a batch was extracted, which makes period differences weak evidence:

| Primitives on file when extracted | Specimens | Rate |
|---|---|---|
| 10 to 40 | 11 | 27% |
| 43 to 78 | 20 | 55% |
| 88 to 119 | 23 | 65% |

### By Region

| Region | Specimens | Rate |
|---|---|---|
| United States | 36 | 53% |
| Ireland and France (Beckett) | 9 | 56% |
| Vietnam (Hồ Xuân Hương, in translation) | 9 | 56% |

12 of the 33 cross-author links cross a region, which is 36%. Specimens from outside the United States are 33% of the catalog. By this measure, region doesn't predict recurrence.

### Time Spans

The median gap between a primitive's source and the specimen that runs it is 68 years.

| Gap | Links | Share |
|---|---|---|
| 25 years or less | 8 of 33 | 24% |
| 26 to 100 years | 15 of 33 | 45% |
| More than 100 years | 10 of 33 | 30% |

The longest gap is 487 years. Wyatt's found inscription from the 1530s reappears, scaled up to a whole poem, in Vuong's "Amazon History" (2022).

### Direction

23 of the 33 cross-author links run forward: the catalogued source is older than the poem that runs it. The other 10, 30%, run backward. Hồ Xuân Hương, writing in Nôm around 1800, runs four operations the catalog first drew from Frost, Beckett, and Trethewey. Those four can't be influence. For the forward links the catalog holds no evidence either way and makes no claim of influence.

### Most-Rediscovered Primitives

| Primitive | First found in | Found again in |
|---|---|---|
| cf-ap-04 unclassified state | Frost, 1914 | Dunn (c. 1989), "Path of Dreams" (1900), "Girl without a Sex" (c. 1800) |
| cf-mt-03 instrument limit | Crane, 1926 | Lux (1990s), Beckett (1935) |
| cf-mt-04 sole custodian | Crane, 1926 | Dobyns (1987), Beckett (1935) |
| cf-mc-03 posthumous verdict | Robinson, 1920 | two poems in the 1900 book |
| cf-sc-05 unknowing register | the broadside, c. 1786 | Longfellow (1854), Vuong (2022) |
| cf-hi-02 photographer outside the frame | Trethewey, 2000 | Vuong (2022, inverted), Hồ Xuân Hương (c. 1800) |
| cf-wl-02 found inscription | Wyatt, 1530s | Eliot (1915), Vuong (2022) |

Unclassified state also appears as the same operation, recorded as a cancellation rather than a run, in three more specimens: Norway, Philomela, and Proud Name. Counting those, one operation, two readings held level with neither chosen, spans seven specimens from around 1800 to around 1990.

Frost's "After Apple-Picking" and Crane's "At Melville's Tomb" together supply 10 of the 35 links, 29%.

### By Axis

| Axis | Share of recurrence links | Share of composites |
|---|---|---|
| outward | 34% | 26% |
| sideways | 29% | 30% |
| upward | 26% | 23% |
| inward | 11% | 21% |

### Author Signatures

Some operations recur within one poet's work rather than across poets:

- Santos: the flat predicate in "Where Once a Small Branch Fell" and "Out of the World There Passed a Soul".
- Hồ Xuân Hương: the speakable figure in "River Snail", "Three-Mountain Pass", and five held variants.
- Beckett: the truncated formula in "Enueg II" and "Sanies II".
- The 1900 poet: the wish to have died in another's place, and the parenthetical leak, each twice.
- Vuong: the title as the only frame in "Old Glory" and "Amazon History".

### Findings

Recurrence is common at the level of the poem and rare at the level of the operation. About half the specimens run at least one operation first found in another poet's poem. Yet four operations in five have turned up only once, and every recurring poem still adds two or three of its own. The typical poem takes one move from a common stock and invents the rest.

What recurs is concentrated. Seven primitives account for 15 of the 35 links. Most repeated operations are outward: limits nobody imposes, such as sleep, death, the reach of an instrument, or an answer held by someone or something absent. Inward operations, where a poem refuses what it knows, supply 11% of links against 21% of composites. Blindnesses look like common property. Refusals look like the poet's own.

The operations cross centuries, and the carriers stay with their period. By corpus:

- form in the 1948 anthology
- convention in the 1900 book
- grammar in Beckett
- comedy in stand-up
- documents in Vuong
- double entendre in Hồ Xuân Hương

The catalog has no field for the carrier. Speaker dials set properties of it, and the dial overlay pair tests whether a confinement's fold survives a change of carrier.

Where the catalog can test it, recurrence looks like rediscovery rather than transmission. Backward links are 30% of the total, and cross-region links run at about the rate the catalog's regional mix predicts.

### Caveats

- Recurrences are recorded when noticed, and assembly has been partial since v0.3, so every count here is a floor.
- Specimens were chosen by the knowledge test with axis tiebreaks, not sampled at random.
- The post-pandemic and 2003 to 2019 rows rest on three and two poems from single books.
- Post-war here means the stand-up anthology only.
- The United States supplies two thirds of the catalog.
- Hồ Xuân Hương is read through one translator.

## Output Policy

Three zones:

- Generated readings carry designations only.
- Apparatus-internal prose, such as headers, registries, loader notes, and this file, may name sources.
- Operator questions get plain answers.

Specimen attribution is never masked. Extensions take no designation; a dial trial ships inside the JIG treatment under JIG.

A name swap isn't anonymization. The designation layer defines five leak tiers:

- Tier A: the name.
- Tier B: coined phrases.
- Tier C: biographical anchors.
- Tier D: ally and target clusters, which stay.
- Tier E: field-standard terms, which stay.

Both audits run so far found their real leak at Tier B.

Source exposure uses the lowest level that preserves the mechanism:

| Level | Content |
|---|---|
| 0 | Address only: say where and what, quote nothing |
| 1 | A phrase |
| 2 | A line, or one sentence of a prose poem |
| 3 | A passage, only when the mechanism spans a junction |
| 4 | Full text: short, public domain, and necessary |

Quotes at Levels 1 to 3 are located quotes: minimal, verbatim, with an address, and never stitched by ellipsis. A finished reading must also pass the reassembly test, meaning its quotes read in sequence can't reconstruct the poem. The default ceiling for in-copyright work is under a quarter of the poem.

Claims are graded on the provenance ladder:

- P0: on the page.
- P1: documented.
- P2: attributed on the record.
- P3: attributed with proximity stated.
- P4: the apparatus's own inference.
- P5: absence recorded.

Grade every claim above P0, or the ungraded ones read as P0.

The default register is plain procedural English. It uses no em dashes and no decorative vocabulary, and it states findings as sentences rather than announcing them. Trial text is outside the register: the lines of a rewrite trial, a dial trial, or a contrast trial are written at the draft's setting or the trial's, and only the commentary around them is held to the register.

## Outstanding

These items come from the boot's Outstanding list, the catalog, the workshop, the registry, and a check of this bundle against the boot.

Audits:

1. Tier B and Tier C are unaudited across all five voice modules.
2. Confinement trials are unaudited against Tier B. A trial that reproduces a catalog source's sentences would leak in the Bay's most-shipped position.
3. Dial trials are unaudited against Tier B on the same terms.
4. The Small Branch seed primitives can be audited line by line against the poem in Square Inch Hours. The catalog's v0.10 checked only the seed composite's surface claims and one stake claim.

Consistency work:

5. The ASSAY, TARE, and RETICLE modules still carry source names in labels, zone names, and gate lines. The designation layer supersedes them at runtime.
6. The workshop's Register Lock exempts only Engine Bay and Function Bay from translation, while its Device Resolution Map calls Confinement Bay a device-name zone. The working resolution, plain workshop speech with device names where precise, isn't written into `3a-workshop`.
7. Section K of `7-device-inventory-extended` still prints the retrieval procedure the kernel removed at 0.3.10, behind a guard rather than rewritten. See Scan Mode.
8. The header of `9-casanova-extraction` says five tools. Its body holds seven and a directive, which is what the registry records.

Policy gaps:

9. `0c-voice-designations` has no rule for a specimen reprinted inside a calibration corpus. The catalog excludes such specimens under its Section F alone.
10. Entries drawn from a calibration source's own poems have no consumer. Kowit's "Hell" and "I Attend a Poetry Reading" are on the page in the stand-up corpus and remain unextracted.
11. The registry's clause-3 question waits on an operator call: whether a voice candidate's corpus must include at least one worked poem reading.

Catalog and dials:

12. Catalog assembly has been partial since v0.3. Pairs across new specimens were checked where apparent, not exhaustively.
13. Five of the nine speaker dials are provisional. Promotion waits on trials across more than one draft and an operator call.
14. A `carrier` field for the catalog is deferred until every specimen's text is on the page. Until then dial overlay pairs report carrier change at the seam.
15. The 1900 collection's author is unidentified. Odette Tyler is a P4 lead from internal evidence. Held candidates wait in the Candidate Log, among them Beckett's "Serena III" and Machan's "Hazel Tells LaVerne".

Inventory:

16. The boot's registry disagrees with this bundle. See Registry Gaps.

### Closed

Closed at boot v0.13 by operator ruling:

- The doctrinal seams between the dial file's source and the workshop's. The workshop's position governs. See Dial Calibration.
- The section 7 heading. Voice and Moral Substrate keeps its name, as does Device Inventory Lite's Voice Devices bin, because the kernel's `voice` homograph entry covers both.

The axis item still sits in the boot's Outstanding list and needs no action. At v0.13 no axis is thin enough to direct the next pass.

Closed by this bundle: every pending edit the earlier README listed is applied in the files on disk, the device inventory carries a version line, and `4-gonzo-mode` is supplied.

## Maintenance Conventions

Every module carries a version line and dated revision notes. A revision note says what changed and why. Earlier notes aren't rewritten, because a rewritten log isn't a log. The version line is part of the release: kernel 0.3.12 shipped under a 0.3.12 file name with a 0.3.11 version line, and nothing caught it until an audit.

A new file takes an identifier only after a check against the boot's registry and the files on disk. The DATUM module once shipped as `4`, which the style mode already held, because its registry row was checked for state and not for a free identifier.

Scars are recorded rather than repaired. Two unrelated voice modules share the `3` prefix and keep it, because renumbering a loaded module costs more than the confusion it removes. The boot records the shared prefix and the DATUM move so nobody has to reconstruct either.

Edits arrive as exact replacements that a script checks before applying, or as companion files that list the replacement text. Nothing that edits a file holding in-copyright text re-emits that text through the model.

Abstention is a completed result. A voice that holds silent, an empty device bin, a stand-down, a held candidate, a dial trial that reports `Reached: nothing, setting only`, and a batch that stops below its ceiling have all finished their work.

## History

`0d-apparatus-provenance` records how the apparatus came to its shape over about fifteen months. It began with a scratch in a new car's clearcoat caused by the writer's own glitch. Months later a deer cracked the bumper, and the damage stopped mattering while the mechanism stayed. The file traces six phases:

1. A private, source-heavy boot.
2. The separation of procedure from source.
3. Pluralization into voices and modes.
4. The apparatus turning on its own prose.
5. The hygiene phase that produced the designation layer.
6. Confinement.

It also defines the fold, lists the pair that recurs across the apparatus, and closes on taste, the part of judgment no gate catches.

`0d` predates the dial file. The dial work is recorded in the revision notes of `13-speaker-dials` 0.1 and 0.2, `3a-workshop` 0.6.0 and 0.6.1, the kernel at 0.3.16, `0c` and `0b` at 0.5, the catalog at 0.13, the device inventory at 0.2, and the boot at 0.12 and 0.13.

## Glossary

Active site. The small place in a poem where a confinement does its work, or where a dial setting shifts.

Active Synthesis. Voiced output in a module's idiom. It's never an attributed statement by the real critic.

Axis. Where a confinement's limit sits relative to the speaker: upward, sideways, inward, or outward.

Breach scan. The Confinement Bay check for where a draft breaks its own confinement.

Calibration collision. A specimen whose author calibrates a loaded voice, mode, or calibrated extension. The voice or mode stands down for the specimen; for an extension, only its operations stand down.

Calibration source. The critic or poet whose corpus calibrates a voice, mode, directive, or extension. It's named in apparatus prose and never in output.

Carrier. The means by which a poem delivers what it knows or withholds: a joke, a borrowed idiom, decorum, a document, grammar, a double entendre. Dials set properties of the carrier.

Carrier denaturation. The failure in a dial overlay pair where the confinement's position and surface survive the change of setting and its fold doesn't.

Checkpoint Gate. The ten checks every reading passes before it ships.

Composite. A catalog entry describing one specimen's whole confinement. It isn't combinable.

Confinement. An imposed pattern of absence that makes something unknowable. Compare constraint, which is elected.

Contrast trial. Function Bay's pair of a wrong-way trial and a cleaner trial. Rewrite trials and dial trials share its footing, and none of them is a revision route.

Coscienza. The two-axis awareness check on the poem and on the apparatus itself.

Counter-voice. A voice you add to a zone another voice already holds, so the two disagree in their own registers.

Coupled dial. A dial that moves when another is turned. A trial holds the partner or reports that it moved.

Cover. A setting that keeps something in the draft off the page. Dial selection looks for it first.

Default verdict slot. ASSAY's standing claim on the closing verdict when no more specific voice is loaded.

Denaturation. The failure in which a confinement's surface transfers to new material and its fold collapses.

Designation. The function name a slot carries in output: ASSAY, PLUMB, TARE, RETICLE, DATUM, and the modes JIG and VISE. Extensions take none.

Device translation. A voice zone in which the voice renders the device inventory in its own register.

Dial. A dimension of how the speaker talks, along which every draft has a setting. Established dials have ranges the source supports; provisional dials have ranges the apparatus supplied.

Dial overlay pair. A confinement trial run without and then with a dial setting over the same span, so the second seam can report what the change of carrier did to the fold.

Dial trial. A trial that turns one dial one step over a span and reports `Reached` and `Seam`.

Directive. A Portable Calibration Directive: one hard specimen's diagnostic force, stated as a prompt any reading can call.

Engine vs. Residue. The test of which feature collapses the poem when removed.

Experiment. An operation the poet runs on the poet's own draft, stated in workshop speech. The dial file's ex-01 to ex-11 are drawn from its source's drills.

Extraction. Two senses. Confinement extraction produces catalog entries. Critic extractions are files that carry a source's tools without a voice zone: `8`, `9`, and `13`.

Fold. What position and surface force the material into together. It's the level that doesn't transfer.

Full monty plugin. A private, source-bearing calibration file for one poem or one critic's book.

Full Monty State. Whether a full monty plugin is loaded: absent, present, multi, or conflicted. The default is absent.

Genopersistation. The layers by which a poem persists: L0 artifact surface, L1 compositional making, L2 institutional support, L3 reception management.

Knowledge test. The requirement that something be unavailable to the speaker, not merely unsaid.

Level 0 to 4. Source exposure levels, from address only to full text.

Lingo source. The region, trade, generation, class, institution, or community whose talk an idiom comes from. Every sd-04 setting above none names one.

Located quote. A quote at Levels 1 to 3 with an address, meeting the seven properties.

Minimal runtime. The kernel's six-line reading.

Mixed Log. The record of live hypotheses, each closed only by evidence under the closure rule.

Overlay. A rule that adds a requirement to a confinement trial and removes nothing knowable: the ars poetica overlay or a dial setting. One per trial.

P0 to P5. The provenance ladder, from on the page to absence recorded.

Page test. The part of a dial entry that reads the draft's current setting off the page, with addresses.

Period Fit. The check that a frame was available when the poem was written; later frames are marked retrospective.

Phase Tensions. The three modes of a poem's strain: Failed System, Intentional Glitch, Transparent Argument.

Pressure point. The line, phrase, image, turn, silence, or seam whose removal would cost the poem most. Every reading names one.

Primitive. A combinable catalog entry isolating one operation from a specimen.

Reached. The line on every trial that names what the trial got to. For a dial trial, it names a real thing the draft held and the line where it was latent, or reports `nothing, setting only`.

Refusal ceiling. At most one refusal primitive per trial. The refusal primitives are cf-sc-02, cf-sb-04, cf-wa-04, cf-pr-02, cf-me-03, and cf-eb-02.

Rendering Note. A sidecar field emitted when a degraded or heavy rendering may inflate a judgment about the poem's difficulty, pace, density, or opacity.

Rewrite trial. A trial that rewrites a span of the draft under a catalog confinement other than its own.

Scan Mode. The device inventory's mode for finding a specimen that carries named devices, from the canon or from a corpus you supply.

Seam. The mandatory line on every trial that names where it failed.

Setting. A dial's value in a span, named by the located words that fix it and never scored.

Sidecar. The full diagnostic reading format.

Speaker. The poem's speaking presence. New vocabulary uses `speaker`, because `voice` already names a critic register.

Specimen. A poem on the page with its attribution.

Spine. The voice a VISE verdict rides, named in its label.

Stake. The catalog field recording what a confinement cost and what won't transfer.

Stand-down. A voice or mode, or an extension's operations, declining a specimen. It's recorded as a jurisdiction note without a stated cause.

Trial firewall. The rule that a trial is a contrast trial and never the poet's next draft.

Triangulated commentary. The sidecar field where each voice with something distinct to say speaks in its own person and the disagreement stands.

Voice zone. A section of output a voice module declares and renders in its own person. The default register governs everything outside it.

![Coolly Skeptical](./avatar/avatar-cholo-coolly-skeptical.png)

