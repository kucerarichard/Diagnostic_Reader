# Diagnostic Reader Hollow Boot

Version: 0.17
Kernel: `0a-portable-poetics-kernel`, v0.3.17 or later
Source policy: no embedded raw source
Status: shareable loader wrapper

v0.17 changes: registers `12-confinement-inventory` at 0.16, which changes no entries and records Jackfruit as a recurrence of cf-rs-02 and cf-ob-03 in Section D, lifting it from the held row of the Candidate Log. No other file changes.

v0.16 changes: registers `14-attridge-staten-extraction` at 0.2, which applies the operator's ruling after reading the source's first chapter: every tool in the file is a brake, the kernel's crediting machinery governs wherever a tool meets it, and no tool may refuse a finding that has an address. Tool 2 loses its narrow association boundary, Tool 1 gains the import-versus-withheld sentence, and the file gains the Depth seam, the wince in its refusal ledger, and the Brake Stack failure mode. No other file changes.

v0.15 changes: registers `14-attridge-staten-extraction` at 0.1, a critic extraction on the model of `8` and `9`, after checking identifier 14 free against this registry and against every file in the bundle. Registers the kernel at 0.3.18 for the two seams the extraction occasioned, `7-device-inventory-extended` at 0.4 for the matching reading-order line, `12-confinement-inventory` at 0.15 for the prior-entry clause and the Prufrock convergence notes, `0b-voice-slot-registry` at 0.6 for the candidate log row and the asymmetry instances, and `0c-voice-designations` at 0.7 for the pointer to Section F. Closes the Outstanding item on specimens reprinted inside a calibration corpus, which `0c` now points to the catalog for and the catalog governs in both directions. Adds two Outstanding items: the extraction's tools are unexercised on a live specimen, and the activation notices of `8` and `9` carry source names against the rule `0c` states for extensions. The kernel floor is unchanged at 0.3.17. The plugin registry is unchanged.

v0.14 changes: registers the found-text widening. The kernel at 0.3.17, `0c-voice-designations` at 0.6, the workshop at 0.7.0, `7-device-inventory-extended` at 0.3, `12-confinement-inventory` at 0.14, and `13-speaker-dials` at 0.3, and raises this file's kernel floor to 0.3.17. Registers `8-frye-extraction` at 0.6, since the widening gives it a default load condition, and removes it from the list of files referenced and not held; `9`, `10`, and the Compartmentalization Engine module stay on that list and the registry gap stays open. Adds three Outstanding items: admission of non-verse specimens to the confinement catalog, candidate devices for found text not added at `7` v0.3, and an audit of the new unit address forms against the reassembly test. The plugin registry is unchanged.

v0.13 changes: closes two Outstanding items by operator ruling, the doctrinal seams between the workshop's and the dial file's calibration sources, and the rename question for the workshop's section 7 heading, and records both under Closed. Registers `13-speaker-dials` at 0.2 and the workshop at 0.6.1, the two files the seam ruling changed. The plugin registry is unchanged.

v0.12 changes: registers `13-speaker-dials` at 0.1, a new catalog extension, after checking identifier 13 free against this registry and against every apparatus file supplied to the session. The files listed below as referenced and not held were not checked; confirm on disk. Registers the Extended Device Inventory as `7-device-inventory-extended` at 0.2, its first stamped version, and removes it from the list of files referenced and not held. Registers the kernel at 0.3.16, `0b-voice-slot-registry` at 0.5, `0c-voice-designations` at 0.5, the workshop at 0.6.0, and `12-confinement-inventory` at 0.13, and raises this file's kernel floor to 0.3.16, which the dial file and the workshop now need. Updates Outstanding: adds six items, corrects the axis item, which had been stale since v0.6 of the catalog, and adds the reprinted-specimen gap that the catalog's Section F has cited since its v0.6 without the item existing here. The plugin registry is unchanged.

v0.11 changes: registers `12-confinement-inventory` at 0.12. The plugin registry is unchanged.

v0.4 changes: registers `12-confinement-inventory` at 0.5, the kernel at 0.3.15, `0c-voice-designations` at 0.4, and the workshop at 0.5.1, and corrects the kernel and catalog rows, stale since v0.3. The plugin registry is unchanged.

v0.3 changes: registers `12-confinement-inventory` and the workshop's move to 0.5.0. The plugin registry is unchanged.

v0.2 changes: adds the Module Registry, adds the apparatus-level files that have accumulated since v0.1 to the load order, and adopts the kernel's File Reference Rule. The plugin registry is unchanged.

## Purpose

This hollow boot loads the portable kernel, declares what else is loadable, and declares the available full monty plugins. It contains no source poems, no private-core verdicts, and no source-bearing worked examples.

It is also the apparatus's only complete inventory. Nothing else lists every file, which is why a module could be built onto an identifier another module already held.

## Load Order

1. Load `0a-portable-poetics-kernel`.
2. Load `0c-voice-designations`. Without it, every voice module emits a label built from its calibration source's name, and the apparatus is out of policy from the first verdict.
3. Load `0b-voice-slot-registry` when slot status, the voice test, or the candidate log is in question. It is not needed to run a reading.
4. Load device and catalog extensions the task requires. `11-provenance-grading-extension` is a hard dependency of the DATUM module and is optional for everything else; `12-confinement-inventory` writes its stake levels on that ladder and reads without it. `12-confinement-inventory` is a hard dependency of the workshop's Confinement Bay and is optional for everything else. `13-speaker-dials` is a hard dependency of the workshop's dial trials and dial overlays and is optional for everything else; it needs kernel 0.3.16 and names its devices from `7-device-inventory-extended` at 0.2 or later. `8-frye-extraction` loads by default when a specimen's kind is not poem, per the kernel's Found Text Compatibility at 0.3.17, and is optional for poems. `14-attridge-staten-extraction` loads on request for a reading that wants its tools; it fires on warrant and is optional for everything.
5. Load the voice modules the task needs.
6. Load style or workshop modes last, since both ride a voice.
7. Load one or more full monty plugins only when source-bearing calibration is needed.
8. Set Full Monty State according to the portable kernel contract.

The order is tolerant. A file arriving later in the session applies from that point forward.

## Module Registry

Versions current as of the v0.13 sweep. References use unversioned stems per the kernel's File Reference Rule; resolve each against the file on disk.

| Stem | Version | Type | Designation |
|---|---|---|---|
| `0a-portable-poetics-kernel` | 0.3.18 | kernel | none |
| `0b-voice-slot-registry` | 0.6 | apparatus registry | none |
| `0c-voice-designations` | 0.7 | apparatus policy | none |
| `1-rother-voice-module` | 0.3.1 | voice module | ASSAY |
| `2-harris-voice-module` | 0.3.1 | voice module | PLUMB |
| `3-kowit-voice-module` | 0.3.1 | voice module | TARE |
| `3-perloff-voice-module` | 0.3.1 | voice module | RETICLE |
| `5-hersh-voice-module` | 0.1 | voice module | DATUM |
| `3a-workshop` | 0.7.0 | workshop mode | JIG |
| `4-gonzo-mode` | 0.3.1 | style mode | VISE |
| `7-device-inventory-extended` | 0.4 | device extension | none |
| `8-frye-extraction` | 0.6 | directive extension | none |
| `11-provenance-grading-extension` | 0.1 | device extension | none |
| `12-confinement-inventory` | 0.16 | catalog extension | none |
| `13-speaker-dials` | 0.3 | catalog extension | none |
| `14-attridge-staten-extraction` | 0.2 | directive extension | none |

Referenced by the apparatus and not held here: `9-casanova-extraction`, `10-monadology-foundations`, the Compartmentalization Engine module, and `0-poetics-boot`, the private core, which loads as a legacy full monty plugin. The Compartmentalization Engine module's identifier is not recorded anywhere this file can see, so `6` looks free and is not known to be; check the disk before building on it.

Two identifiers carry history a reader would otherwise have to reconstruct. The `2` and `5` voice modules were built together and the second shipped under `4`, which the style mode already held; it moved in the v0.2 sweep. The `3` prefix holds two unrelated voice modules, TARE and RETICLE, from an earlier numbering that did not anticipate a second module on the same digit. Both are recorded rather than renumbered, because renumbering a loaded module costs more than the confusion it removes.

## Outstanding

The three modules at v0.3.1 that received a cross-voice pass but not an operational hygiene pass still carry calibration-source names in their labels, zone names, and gate lines: `1-rother-voice-module`, `3-kowit-voice-module`, and `3-perloff-voice-module`. Loading `0c-voice-designations` supersedes every label at runtime, so nothing here breaches the policy. It is consistency work, and until it is done those three headers disagree with `2-harris-voice-module` and `5-hersh-voice-module` about how a zone is named.

Tier B and Tier C are unaudited across all five voice modules. Operational lexicons carry source coinages as examples and several recurring moves anchor on a source's history. Both are legitimate header prose. Neither has been checked against what the modules render in output, and the two audits run so far both found their real leak at Tier B rather than Tier A.

Confinement extraction is unaudited against Tier B. The catalog's entry fields describe operations and carry no source phrasing by rule, and the rule has not been checked against what a trial renders in output. A trial that arrives at a catalog source's own sentences is a Tier B leak in the most-shipped position the new bay has, which is the same shape as the two findings the earlier audits produced.

Confinement assembly in `12-confinement-inventory` from v0.3 on is partial. The primitives added since v0.3 were checked within their specimens and against the seed primitives, not exhaustively against each other.

The axis item carried here since the catalog's v0.5 said inward held one specimen. It went stale at the catalog's v0.6, which weighted its batch toward inward. At v0.13 the catalog stands at thirteen upward, seventeen sideways, twelve inward, and fifteen outward composites, and no axis is thin enough to direct the next pass.

Speaker dial trials are unaudited against Tier B, on the same terms as confinement extraction above. The dial file holds its source's chapter terms in the header and its experiments are the apparatus's restatements, and neither rule has been checked against what a dial trial renders.

Five of the nine speaker dials are provisional. Their ranges are the apparatus's, and promotion waits on trials across more than one draft and an operator call.

A `carrier` field for the confinement catalog is deferred. Back-filling it needs every specimen's text on the page. Until then dial overlay pairs report carrier change at the seam.

Section K of `7-device-inventory-extended` predates the kernel's removal of specimen retrieval and carries a guard at its head instead of a rewrite. The venue list and fetch rules are still printed there and do not run.

Admission of non-verse specimens to `12-confinement-inventory` is deferred at the catalog's v0.14. Confinement Bay extracts from a found text at runtime and the catalog does not take the entries, because its recurrence findings measure a corpus of whole poems. The call is whether a second corpus, a `kind` field, or continued exclusion serves the findings, and it is the operator's.

Three devices entered `7-device-inventory-extended` at v0.3 for found text: stage direction, dateline, and attribution formula. Candidates noticed and not added: the speaker cue, the name before a speech in a script, which the stage direction entry does not cover; the byline; the caption. Each waits on a specimen that needs it.

The unit address forms added to the kernel at 0.3.17 (`Sp`, `SD`, `P`, `Hd`, `Dl`, `By`, `Frag`) are unaudited against the reassembly test. The test was written for lines, and a quarter of a report's paragraphs reproduces more text than a quarter of a poem's lines. The kernel states the proportional-or-absolute reading; what counts as the ceiling on a long prose specimen has not been set.

The tools of `14-attridge-staten-extraction` are unexercised on a live specimen. Each fires on a stated warrant and attaches to a field the kernel already has, so the first readings that load it should report, per tool, whether it changed the reading or relabelled a finding; the extraction's Relabelling failure mode is the test.

The activation notices of `8-frye-extraction` and `9-casanova-extraction` carry their sources' names in output. `0c-voice-designations` holds from v0.5 that an extension ships no labelled output of its own, and `14` follows that rule with a notice that names no source. The two earlier notices predate the rule. Whether to bring them under it is the operator's call; nothing else in either file is affected.

## Closed

Items closed by operator ruling, kept so the history is visible without the revision notes.

Specimens reprinted inside a calibration corpus, closed at v0.15. The item recorded that `0c-voice-designations` had no rule for a specimen reprinted in a calibration corpus with the source's commentary, and that the catalog excluded such specimens under its Section F alone. The first corpus to reprint a specimen the catalog already held, the source of `14-attridge-staten-extraction`, showed that Section F also ran only forward. The catalog at v0.15 gained a prior-entry clause: existing entries stand, carry a convergence note, and are frozen against revision in any session where the extension is loaded, with no further extraction from the specimen; `0c` at v0.7 points to Section F for the case. The division is now stated in both files: `0c` covers the author's identity, the catalog the specimen's text.

The doctrinal seams, closed at v0.13. The dial file's calibration source and the workshop's disagreed on personality, on what plain speech does to cost, on reader position, and on abstraction. The operator ruled for the workshop's position on all three that were open: voice comes from depth of attention, plainness is for exposing cost, and the reader stays a peer. Speaker dials are probes for what a draft holds, and a dial trial that only changes how a span sounds reached nothing. Abstraction had already been settled by the kernel's open-or-corner test. Recorded in `13-speaker-dials` v0.2, Section H, and in the workshop at 0.6.1.

The section 7 heading, closed at v0.13. Voice and Moral Substrate keeps its name. The rename question arose only because the kernel's `voice` homograph, registered at 0.3.16, marks the heading as a legacy use of the craft sense; the homograph entry is sufficient. Device Inventory Lite's Voice Devices bin keeps its name on the same terms.

## Plugin Registry

- Snow Crust: `full-monty-snowcrust-example`. Floor-origin hypothesis and accidental ars poetica.
- Small Branch: `full-monty-santos-small-branch-example`. Sayability, seam pressure, and appropriation risk.
- Whoso List: `full-monty-wyatt-whoso-list-plugin`. Steganographic surface and load-bearing foreignness.
- Kowit Hell: `full-monty-kowit-hell-plugin`. Complaint loop and comic clarity.
- Hellenistics: `full-monty-jeffers-hellenistics-plugin`. Anti-laundering engine default and transparent ugliness.
- Poetry Reading: `full-monty-kowit-poetry-reading-plugin`. Captive attention and access-asymmetry.

Plugin names carry specimen authors, which the Designation Policy protects rather than masks. A plugin is a source-bearing calibration file for a poem, and a reading that cannot name the poem it reads is not a reading.

One plugin pair is a calibration collision. Two of the six carry poems by a poet who also calibrates a voice module, so a reading of either specimen under that voice would be the voice reading its own source. Per `0c-voice-designations`, the voice stands down for those specimens and the stand-down is recorded as a jurisdiction note without stated cause.

Two plugin specimens carry the stand-down flag for confinement extraction, for the reason already recorded above. `12-confinement-inventory` records that the flag exists without naming which entries carry it, following this file's own precedent.

## Default State

Full Monty State: absent.

The apparatus runs from the portable kernel until a plugin is loaded. When a plugin is loaded, it enriches calibration beneath active module zones. It does not seize voice, workshop, or device output outside its declared authority.

## Source Rule

Raw source belongs in full monty plugins. This hollow boot may point to source files but must not embed them.

## Loader Notice

When a plugin changes output, use the portable notice:

```text
Full Monty State: present. Using [plugin name] for [specific enrichment].
```

Omit the notice when plugin presence does not change output.
