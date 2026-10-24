# Diagnostic Reader Regression Operations

**Status:** operational scaffold for the supplied repository snapshot. The source apparatus files are unchanged; this directory adds run controls only.

## Recommended run mechanics

For each run, start a **fresh target-model chat**. Upload one condition package (or the full-framework ZIP plus the matching `regression/tests/<ID>/` files), then paste the matching `target-prompt.md` into that same chat. The target must receive the actual specimen as a file or image, not merely its title. Do not reuse a chat between conditions.

The preferred durable layout is one folder per condition containing:
- `manifest.json` — exact condition, supplied/withheld files, specimen requirements, and version metadata;
- `target-prompt.md` — copy-ready prompt for the target model;
- `specimen.txt` or `specimen.png` — the actual source material used in that run (once pinned/populated).

R1–R8 and R10 now contain the supplied poem transcriptions. Their exact bytes and SHA-256 values are recorded in each manifest and in `specimens/catalog.json`. The upload did not identify bibliographic editions, so these are frozen user-supplied transcriptions, not edition-verified texts. R9 remains blocked until an actual scan/image is supplied; it must not include the complete poem text. R10 uses the same exact “The Tyger” bytes as R1/R2.

## ZIP versus individual uploads

- **Best for reproducibility:** give the target a condition-specific ZIP whose manifest and specimen are inside it, plus the allowed framework files for that condition. Paste the prompt in the same chat.
- **Fallback:** upload the framework files, manifest, and specimen individually, then paste the prompt in that same chat. Record exactly what was uploaded.
- Do not assume that uploading a ZIP means every model has extracted or read every nested file. The prompt requires the model to report which files it could actually inspect. If the model cannot inspect the archive, provide the extracted files individually; do not count a claimed load as evidence of a load.
- Keep the original full-framework ZIP immutable. Build each R10 condition from a fresh copy and remove only the specified dependency. Never create a missing-dependency condition merely by telling the model that a file is absent while leaving it accessible in the same archive.

## Package architecture

`manifests/` contains machine-readable condition definitions. `tests/<ID>/` contains the condition's human-operable files. `prompts/` contains shared evaluator and adjudicator prompts. `specimens/` is the canonical specimen store once texts/scans are pinned. `test-runs/` is for raw target outputs and Muse Chat 2 evaluator reports. `results/` is for adjudicated results. Never overwrite raw outputs; create a new run record per repetition.

## Roles and sequence (Muse-only reader/evaluator)

1. **Reader / test subject (Muse Chat 1):** start a fresh chat; upload only the condition-specific ZIP and paste its `target-prompt.md`. Save the returned artifact verbatim. Record the exact Muse model/version and any archive-reading limitation.
2. **Evaluator (Muse Chat 2):** use a different fresh chat. Provide the raw Muse Chat 1 artifact, condition manifest/test card, scoring criteria, and relevant framework files. Paste `prompts/evaluator-master.md` plus the test's `evaluator-prompt.md`. Do not expose evaluator instructions to Chat 1 or let Chat 2 revise the reader artifact.
3. **Adjudicator (ChatGPT, separate chat):** provide the same condition snapshot, specimen, raw Chat 1 output, and complete Chat 2 report. Paste `prompts/adjudicator-master.md` plus the test's `adjudicator-prompt.md`. Independently inspect the source files and audit both stages.
4. **Save separately:** raw reader output, evaluator report, adjudication, model/version, settings if visible, date, files actually received, and archive-reading limitations. Preserve the raw artifact; never overwrite it with a revised answer.

**Independence limitation:** Chat 1 and Chat 2 use the same model family (Muse). Separate chats prevent direct conversational carryover but do not provide independent model-family replication. ChatGPT adjudication is a separate model perspective, but remains fallible and should cite the pinned framework evidence.

## Version and checksum discipline

The ZIP supplied for this scaffold has no Git commit hash embedded in the available metadata. Do not invent one. Record the Git commit/tag when available, and SHA-256 checksums for the ZIP and each specimen. Framework versions can be read from file contents, but file version labels are not a substitute for a repository commit.

## R9 scan caution

R9 is not executable until an actual scan image is selected. Put the image at `specimen.png` (or use a stable image format) and record its source, edition if known, visible/cropped portions, and SHA-256. Do not add the full poem transcription to the target's package.

## R10 variants

R10-A withholds `0c-voice-designations-v0_7.md`; R10-B withholds `7-device-inventory-extended-v0_4.md`; R10-C withholds `11-provenance-grading-extension-v0_1.md` and explicitly exercises DATUM; R10-D withholds `2-harris-voice-module-v0_3_1.md` and explicitly requires a Harris-dependent triangulation step. Each variant must be packaged from a clean copy and verified by listing its actual contents before upload.
