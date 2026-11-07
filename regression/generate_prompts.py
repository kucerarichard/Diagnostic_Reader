#!/usr/bin/env python3
"""Compatibility shim. The regression compiler now lives in the dr package:

    python -m dr regress --cases R1 R10-A --out compiled-run

This script forwards its arguments to `dr regress`. Run it from anywhere;
it finds the dr package next to this directory.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dr.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(["regress", *sys.argv[1:]]))
