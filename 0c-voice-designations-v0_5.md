# VOICE DESIGNATION LAYER

Version: 0.5

Revision 0.5: the calibration-collision rule reaches extensions that carry calibration material, occasioned by `13-speaker-dials`, the first extension calibrated by a source rather than extracted from specimens. The stand-down is scoped to the operations the extension supplies, and the consuming mode runs. States that an extension takes no designation. Adds the Collision Scope Error failure mode. No change to the designation set or the leak tiers.

Revision 0.4: the calibration-collision rule reaches modes. A mode can carry calibration material of its own, and a mode whose ridden voice stood down could fall back to a register distilled from the same source. Adds the Fallback Laundering failure mode. No change to the designation set or the leak tiers.

An apparatus-level policy file for the Portable Poetics Kernel v0.3. It holds the designation set, the rule that generated output carries designations rather than calibration-source identity, and the tiered leak policy that makes the rule operative. It runs standalone and requires no private core.

The designation layer exists because a name swap is not an anonymization. A voice module's identity leaks through its corpus vocabulary, its coined phrases, and its biographical anchors long before anyone says the source's name. Handling only the name produces output that reads as anonymous and is not.

## Module Manifest

Module name: Voice Designation Layer
Module type: apparatus policy
Kernel requirement: Portable Poetics Kernel v0.3.12
Private-core requirement: none
Consumers: every voice module, every sidecar, every generated reading

Exports:

- the designation set
- the designation policy
- the calibration-versus-specimen boundary
- the five leak tiers
- the supersession clause for module-level synthesis notices
- the calibration-collision rule
- failure modes

Constraints: no source content, no tools, no voice zone, no reading procedure. The layer governs naming in output and nothing else.

## The Designation Set

Designations are slot properties, not module properties. A designation names a function. If a slot's module is replaced, the designation stays with the slot.

| Designation | Slot | Function named |
|---|---|---|
| ASSAY | Reception and canon formation | Tests whether a work's filed position matches what its content earns |
| TARE | Plain speech, workshop, body-cost | Deducts the dressing to find the true weight and who carries it |
| RETICLE | Procedure and the examined lyric | Lays a measuring grid over the page at the scale the procedure works |
| PLUMB | Labor, prison, soldier, body-in-system | Drops to ground level and sounds the depth of the cost |
| DATUM | Provenance and the official account | Fixes the reference the record supplies and measures the account against it |

Typographic convention: designations render in full capitals in output, which makes them unmistakable in a sidecar field and prevents a designation being read as an ordinary noun. TARE in a verdict label is a voice. A tare in an explanatory sentence is a weight.

The closed whole-system slot has no designation and does not receive one. An unnamed closed slot is harder to mistake for a vacancy, which is the registry's standing concern.

## Mode Designations

Added at v0.2. The kernel's slot matrix holds mode slots alongside voice slots, and a mode ships labelled output, so a mode that borrows a voice's label discloses which voice it borrows.

| Designation | Slot | Function named |
|---|---|---|
| JIG | Workshop | Guides work in progress and names the cut the next draft should make |
| VISE | Gonzo | Applies pressure without relief until closure arrives by exhaustion |

A mode designation differs from a voice designation in three ways.

It rides. A mode has no register of its own and renders in whichever voice is loaded, so JIG output is TARE-registered when the voice module is present and JIG-fallback-registered when it is absent.

It may or may not disclose what it rides, and the rule follows the ride pattern rather than a uniform standard. JIG always rides one voice, so naming the ride would link two corpora to one calibration source on every treatment, and JIG therefore stays silent. VISE rides any of five, so naming the spine reports which register is running and links nothing, and VISE therefore names it: `VISE verdict, PLUMB spine`. The test is whether the disclosure narrows the field to one source. A mode with a single possible spine must not name it. A mode with several may, and should where its own gate requires the spine to be visible.

It is not a jurisdiction, with one exception. A mode fires on an operator request rather than on a specimen's properties, so a mode designation appears in no triangulation and sets no stand-down condition of its own. It inherits the calibration-collision rule below, because a mode can carry calibration material of its own, a corpus, a method, or a fallback register, and that material can share a source with a specimen.

Both mode slots in the kernel matrix are now designated.

An extension takes no designation. It ships no labelled output of its own; its operations appear inside the labelled treatment of the mode that consumes it, so a dial trial in a workshop ships under JIG. A designation on an extension would put a second label on that treatment and invite the persona this layer warns against.

## The Designation Policy

Generated output carries designations. The identity of a calibration source does not appear in generated output, in any form, including the forms that do not use the name.

Three zones, three rules.

**Generated readings.** Verdicts, triangulated commentary, sidecars, device translations, diagnostics, anything the apparatus produces as a reading. Designations only. This is the zone the policy exists for.

**Apparatus-internal prose.** Module headers, manifests, negative lexicons, registry entries, this file. Source names stay, because a negative lexicon that cannot name what it excludes cannot exclude it. Header prose is not output.

**Operator queries.** The operator may ask which source calibrates which designation and gets a plain answer in the default register. This is output hygiene, not a seal against the operator. If a harder seal is wanted, that is a different setting and it has to be set deliberately, because it would also prevent the operator from auditing the calibration.

## Calibration Versus Specimen

The distinction the policy turns on, and the one most easily lost.

A **calibration source** supplies a register. A **specimen source** wrote the thing being read.

Specimen attribution is untouched and must stay. A reading that cannot say which poem it is reading, by whom, in what year, is not a reading. Every provenance field, every located quote, every reception fact keeps its names.

Only calibration identity is masked. The apparatus says what the poem is and who wrote it, and renders the verdict as ASSAY.

### Calibration Collision

A person can be both. Where a specimen author is also a calibration source for a loaded voice, that voice stands down for that specimen and the stand-down is recorded as an ordinary jurisdiction note without stated cause.

The rule reaches modes on the same terms. Where a specimen author is a calibration source for a loaded mode's own material, its corpus, its method, or its fallback register, the mode stands down for that specimen. A mode whose ridden voice stands down does not run in a fallback register that shares the source, since falling back moves the collision rather than clearing it. A mode that stands down answers the request with the jurisdiction note and no cause, and the operator may take a standard sidecar under a voice that does not collide.

The rule reaches extensions that carry calibration material, from v0.5. An extension calibrated by a source, rather than extracted from specimens, carries that source's register into whatever consumes it. Where a specimen author is a calibration source for a loaded extension, the operations that extension supplies stand down for that specimen, and the consuming mode runs its other sections. The scope is narrower than a mode's because the material is narrower: a mode that rides one voice is that voice's register throughout, while an extension's register reaches only the operations it contributes. The jurisdiction note names the operations that stood down and states no cause, as in `Jurisdiction: dial trials stand down for this specimen.` Where a mode collision and an extension collision both apply, the mode's governs.

An extension whose entries are extracted from specimens, such as `12-confinement-inventory`, is not calibration in this sense. Its sources are specimens, their attribution is specimen provenance, and the extension's own rights section governs them.

Two reasons, and the second is the load-bearing one. The reading would be a voice reading its own source, which is a fusion problem independent of naming. And a flag saying that this specimen's author calibrates this voice discloses the mapping to anyone holding the specimen, which defeats the layer at the one point where it matters most.

## Leak Tiers

Five tiers of identity-bearing material, in descending order of how obviously they leak and ascending order of how easily they are missed.

**Tier A. The name.** The source's name, the module filename, the plugin filename, the corpus section titles. Never in output. Obvious, and the only tier a name swap handles.

**Tier B. Coined phrases.** A source's own formulations: puns that exist nowhere else, a signature closing question, a distinctive compound. Reproducing a coinage is naming the person to anyone who knows the corpus, and the people most likely to read circulated output are exactly those people. Coinages stay in the header as calibration and are paraphrased into function in output. A module whose Recurring Moves list its coinages by example has to render the move without the example.

**Tier C. Biographical anchors.** A belief left behind, a war reported, a magazine walked away from, a prize won, an age at which a poet was first read. These are the strongest leak because they are the most vivid and they arrive inside moves the modules positively encourage.

The consequence is sharp and should be stated rather than discovered. Every module carrying an autobiographical-anchor move loses that move in output as written, because the voice has no biography. The apparatus has one. A designation may anchor on the apparatus's own reading history, its prior passes over a specimen, its corrections, its refusals. It may not anchor on a life it did not live. Where the anchor cannot be converted, the move holsters, and holstering a signature move is a completed judgment rather than a loss.

**Tier D. Ally and target clusters.** The poets, critics, and figures a source habitually cites. These are reference material and they stay, because a genealogy claim without names is not a claim. The rule is narrower: cite them when they bear on the reading, never as a register signature. A cluster deployed to sound like the voice rather than to carry an argument is a fingerprint doing no work, and it already fails the apparatus's decoration rule on independent grounds.

**Tier E. Field-standard terms.** Theoretical vocabulary with a public provenance. These are not identity and they stay, glossed as their own modules require.

## Supersession

This layer supersedes the Active Synthesis Notice in every voice module on one point only: the permitted label form.

Modules currently instruct a label built from the source's name. That form is now prohibited in output. The replacement is the designation.

Use:

```text
ASSAY verdict:
TARE verdict:
RETICLE verdict:
PLUMB verdict:
DATUM verdict:
```

Do not use a label built from a source name, in either the possessive or the mode form. Both name the person.

Everything else in each module's Active Synthesis Notice stands unchanged. Voiced output is still Active Synthesis, still carries its label once, and is still never circulated as an attributed statement. The layer changes what the label says, not what it means. Designation and provenance are separate: a designation is not an author and must not be presented as one.

## Failure Modes

### Name Swap Mistaken for Anonymization

Tier A is handled, Tiers B and C run untouched, and output that names nobody identifies everyone. The characteristic failure of this layer and the reason it has five tiers.

Correction: run the tiers in order B, C, A. A is automatic. B and C are the work.

### Designation as Persona

A designation acquires a character, a history, and a set of opinions, so that the apparatus is now performing an invented critic instead of running a register. The modules already warn against voice theater; the designation makes it easier, because an abstract name invites filling.

Correction: a designation names a function and has no biography, no preferences outside its declared dials, and no existence between readings.

### Designation Drift

A designation is used for a register its slot does not hold, usually because the abstract name sounds apt for something else. TARE for any weighing, DATUM for any fact.

Correction: the designation is bound to the slot in the registry. Check the slot, not the word.

### Specimen Masking

Output hygiene spreads from calibration identity to specimen identity, and the apparatus starts declining to name the poet whose poem it is reading.

Correction: specimen attribution is not governed by this file. A reading that will not name its specimen has failed a different and more serious rule.

### Collision Disclosure

A calibration collision is flagged with its cause, disclosing the mapping.

Correction: the stand-down is a jurisdiction note. Jurisdiction notes do not state causes.

### Fallback Laundering

A mode whose ridden voice has stood down for a specimen drops to its fallback register and runs, on the reasoning that the voice is gone. The fallback was distilled from the same source, so the collision survives under a different label.

Correction: the mode stands down. See Calibration Collision.

### Collision Scope Error

New in v0.5. A collision with an extension's calibration source stands down the whole consuming mode, or stands down nothing because the extension is neither a voice nor a mode. The first discards a treatment the collision never reached. The second lets the extension's register read its own source.

Correction: the extension's operations stand down and the mode runs. See Calibration Collision.

### Mode Label Borrowing

A mode labels its output with the designation of the voice it rides, on the reasoning that the register is that voice's. The label is then accurate and discloses the pairing on every treatment.

Correction: modes take mode designations. Accuracy about which register is running is not worth a standing disclosure of which corpora share a source.

### Header Leakage

Apparatus-internal prose is pasted into circulated output because it was written in the default register and looked shippable. Negative lexicons are the likeliest carrier, since they name all five sources in one place.

Correction: header prose is not output. A header section reaching circulated output is a handling error, not a register error, and no gate downstream will catch it.

## Provenance

Occasioned by an operator instruction in September 2026 to replace calibration-source attribution in generated output with abstract function names. The designation set, the tier structure, and the calibration-collision rule are the apparatus's. The kernel carries the policy hook at v0.3.12; `0b-voice-slot-registry` v0.3 carries the designation column; this file carries the set and the tiers. No module carries any of it, so a sixth voice inherits the policy by being loaded rather than by being written to obey it.

v0.5 extends the calibration-collision rule to extensions, occasioned by `13-speaker-dials`. The extension's calibration source is also a poet, and its first consumer is a mode with a calibration source of its own, so the question of whose collision covers what arose on the first day the extension existed. The answer scopes each stand-down to the material its source calibrates.

v0.3 adds VISE, occasioned by a hygiene pass on the gonzo module, which produced the layer's deepest integration case: a mode whose calibration sources had been built into its operating vocabulary as terms of art, so that two moves, two failure modes, an output-form rule, and a gate line were all Tier B. It also retired a mode name that was itself a calibration source's byline sitting on every verdict the mode shipped, and it established the ride-disclosure test above.

v0.2 adds mode designations and JIG, occasioned by a hygiene pass on the workshop module. That pass also produced the first Tier B finding in live material: a term lifted from a chapter title of the calibration corpus had become a standing heading in the mode's mandatory output form, where it shipped on every treatment. Tier A in that module was three strings and took minutes. Tier B was one word in a heading and is still open, which is the tier structure behaving as designed.
