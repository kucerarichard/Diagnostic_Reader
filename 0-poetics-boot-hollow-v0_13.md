# Diagnostic Reader Hollow Boot

Version: 0.13
Kernel: `0a-portable-poetics-kernel`, v0.3.16 or later
Source policy: no embedded raw source
Status: shareable loader wrapper

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
4. Load device and catalog extensions the task requires. `11-provenance-grading-extension` is a hard dependency of the DATUM module and is optional for everything else; `12-confinement-inventory` writes its stake levels on that ladder and reads without it. `12-confinement-inventory` is a hard dependency of the workshop's Confinement Bay and is optional for everything else. `13-speaker-dials` is a hard dependency of the workshop's dial trials and dial overlays and is optional for everything else; it needs kernel 0.3.16 and names its devices from `7-device-inventory-extended` at 0.2 or later.
5. Load the voice modules the task needs.
6. Load style or workshop modes last, since both ride a voice.
7. Load one or more full monty plugins only when source-bearing calibration is needed.
8. Set Full Monty State according to the portable kernel contract.

The order is tolerant. A file arriving later in the session applies from that point forward.

## Module Registry

Versions current as of the v0.13 sweep. References use unversioned stems per the kernel's File Reference Rule; resolve each against the file on disk.

| Stem | Version | Type | Designation |
|---|---|---|---|
| `0a-portable-poetics-kernel` | 0.3.16 | kernel | none |
| `0b-voice-slot-registry` | 0.5 | apparatus registry | none |
| `0c-voice-designations` | 0.5 | apparatus policy | none |
| `1-rother-voice-module` | 0.3.1 | voice module | ASSAY |
| `2-harris-voice-module` | 0.3.1 | voice module | PLUMB |
| `3-kowit-voice-module` | 0.3.1 | voice module | TARE |
| `3-perloff-voice-module` | 0.3.1 | voice module | RETICLE |
| `5-hersh-voice-module` | 0.1 | voice module | DATUM |
| `3a-workshop` | 0.6.1 | workshop mode | JIG |
| `4-gonzo-mode` | 0.3.1 | style mode | VISE |
| `7-device-inventory-extended` | 0.2 | device extension | none |
| `11-provenance-grading-extension` | 0.1 | device extension | none |
| `12-confinement-inventory` | 0.13 | catalog extension | none |
| `13-speaker-dials` | 0.2 | catalog extension | none |

Referenced by the apparatus and not held here: `8-frye-extraction`, `9-casanova-extraction`, `10-monadology-foundations`, the Compartmentalization Engine module, and `0-poetics-boot`, the private core, which loads as a legacy full monty plugin. The Compartmentalization Engine module's identifier is not recorded anywhere this file can see, so `6` looks free and is not known to be; check the disk before building on it.

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

Specimens reprinted inside a calibration corpus with the calibration source's commentary are excluded from confinement selection by the catalog's Section F alone. `0c-voice-designations` covers author collisions, and from v0.5 it covers calibrated extensions, but it does not cover this case. The catalog has cited this item since its v0.6; it is recorded here for the first time at v0.12.

## Closed

Items closed by operator ruling, kept so the history is visible without the revision notes.

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
