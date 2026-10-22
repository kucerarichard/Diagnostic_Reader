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

`manifests/` contains machine-readable condition definitions. `tests/<ID>/` contains the condition's human-operable files. `prompts/` contains shared evaluator and adjudicator prompts. `specimens/` is the canonical specimen store once texts/scans are pinned. `test-runs/` is for raw target outputs and evaluator reports. `results/` is for adjudicated results. Never overwrite raw outputs; create a new run record per repetition.

## Roles and sequence

1. **Target:** receives the condition package, specimen, and target prompt; returns raw output only.
2. **Evaluator (Muse):** receives the raw target output, the same test manifest/card, and the relevant framework files; scores the output independently.
3. **Adjudicator (separate ChatGPT chat):** receives the same condition snapshot, raw target output, evaluator report, and scoring prompt; audits the evaluator and independently inspects the target artifact.
4. Save each artifact separately and record model/version, settings if visible, date, files actually received, and any archive-reading limitation.

The target should not receive evaluator/adjudicator prompts. The evaluator should not see the adjudicator report before grading. The adjudicator must see the raw target output, not only the evaluator summary.

## Version and checksum discipline

The ZIP supplied for this scaffold has no Git commit hash embedded in the available metadata. Do not invent one. Record the Git commit/tag when available, and SHA-256 checksums for the ZIP and each specimen. Framework versions can be read from file contents, but file version labels are not a substitute for a repository commit.

## R9 scan caution

R9 is not executable until an actual scan image is selected. Put the image at `specimen.png` (or use a stable image format) and record its source, edition if known, visible/cropped portions, and SHA-256. Do not add the full poem transcription to the target's package.

## R10 variants

R10-A withholds `0c-voice-designations-v0_7.md`; R10-B withholds `7-device-inventory-extended-v0_4.md`; R10-C withholds `11-provenance-grading-extension-v0_1.md` and explicitly exercises DATUM; R10-D withholds `2-harris-voice-module-v0_3_1.md` and explicitly requires a Harris-dependent triangulation step. Each variant must be packaged from a clean copy and verified by listing its actual contents before upload.
