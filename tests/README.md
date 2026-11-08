# tests/

The compiler's own test suite. Nothing here is a Diagnostic Reader regression case; those live under `regression/tests/R*/` and are compiled by `dr regress`. The two directories share a word and nothing else.

| Here, `tests/` | There, `regression/tests/` |
|---|---|
| Checks the `dr` package: resolver, parsers, prompt writer, harness | Defines conditions for a language model to be tested under |
| Runs in a second with `python -m unittest discover -s tests` | Runs only by pasting a compiled prompt into a model |
| Passes or fails by assertion | Is scored by an evaluator and an adjudicator against the suite's criteria |
| Changes when the compiler's code or data changes | Changes when a test card changes |

## Files

| File | Holds |
|---|---|
| `test_dr.py` | the suite: 79 tests in ten groups (see `dr/README.md`, Tests) |
| `golden.json` | the pinned load set and request line for each task and each regression case |
| `update_golden.py` | regenerates `golden.json` from the current registry, bundle, and cases |

## Running

```
python -m unittest discover -s tests          the whole suite
python -m unittest tests.test_dr.ResolveTests  one group
python -m unittest tests.test_dr.ResolveTests.test_withhold_is_recorded_and_warns   one test
```

`discover -s tests` is Python's standard runner told to start in this directory and run every `test_*` method in every `test*.py` file. The runner is part of the standard library; nothing is installed.

The suite reads the framework files in the repository root, so it is a test of the bundle on disk as well as of the code. Counts pinned in it (192 devices, 194 confinements, 9 dials, 21 directives, 14 cases) move when the catalogs do; a failing count after a catalog edit is the suite doing its job, and the fix is to update the pinned number once the new count is confirmed.

## What `golden.json` is for

`test_dr.py` checks that the compiler works: floors compare correctly, a ZIP loads, a binary specimen is refused, the fence is longer than any backtick run. Those tests would pass against an empty framework. `golden.json` checks something else: that the data has not quietly changed what gets loaded.

It records, for each of the eight tasks and each of the fourteen regression cases, the ordered stems the resolver produces and the request line it renders. `GoldenTests` compares that record to what the resolver produces now. Edit `framework-registry.json` so a sidecar no longer pulls `7`, or edit R5's manifest and drop RETICLE, and every other test still passes while the golden test fails with a diff naming the case and the change.

That failure has two outcomes:

- The change was unintended. You have caught it; revert.
- The change was intended. Run `python tests/update_golden.py`, read the diff of `golden.json`, and commit it with the change.

The golden file pins stems and request lines, not file hashes or prompt text, so a framework release (kernel 0.3.19 to 0.3.20, say) changes every prompt's bytes without touching it. It speaks only when a load set moves. "Golden file" is a general testing idiom, not a `unittest` feature; the mechanism is a JSON file and one test that reads it.

## When to touch what

| You changed | Then |
|---|---|
| compiler code in `dr/` | run the suite; fix or extend `test_dr.py` |
| `dr/framework-registry.json` | run the suite; if `GoldenTests` fails and the change was intended, `update_golden.py` |
| a manifest under `regression/tests/` | same as above; the specimen sha pin is checked too |
| a catalog file (`7`, `12`, `13`, the kernel's directives) | run the suite; update the pinned count in `CatalogTests` if the new count is right |
| the framework `README.md` tables | run `python -m dr lint`; the `readme` check reports drift against disk and registry |
