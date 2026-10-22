# Condition-specific target packages

Run `python regression/build_condition_packages.py` from the repository root to create one isolated target ZIP per condition. The script excludes evaluator/adjudicator prompts and other test cards, and verifies that the named R10 dependency is absent.

**Important:** the current `specimen.txt` / `specimen.png` files are placeholders, not valid test inputs. Replace each placeholder with the pinned poem transcription or actual R9 scan, update edition/source and SHA-256 in its manifest, and only then build target packages. The builder overwrites packages with the same names; preserve packages from scored runs and archive their hashes in run records.
