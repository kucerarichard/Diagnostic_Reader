#!/usr/bin/env python3
"""Strip the framework files out of a compiled reader prompt, leaving the wrapper.

A compiled reader prompt is about 97 percent framework files. Chat shells take file
attachments, so the framework can be uploaded instead of pasted, and only the wrapper, the
target instructions, the reader-facing manifest, the LOAD SET, the specimen, and the
operator request, has to be typed.

    python regression/tools/cut-wrapper.py runs/R9/reader-prompt.md

Writes reader-wrapper.md beside the input and prints which files to attach.

Cut the wrapper from the compiled prompt, never from the case directory. The manifest in
the compiled prompt is the reader-facing one, filtered by READER_MANIFEST_KEYS;
regression/tests/<case>/manifest.json additionally carries scoring, target_model,
evaluator and adjudicator, and giving the Reader those contaminates the run.

Standard library only, Python 3.9 or later, same as the dr package.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BAR = "=" * 88
SPLIT = re.compile(r'(?m)^' + re.escape(BAR) + r'\n(.+)\n' + re.escape(BAR) + r'\n')

DELIVERY_NOTE = """
DELIVERY NOTE (operator). The framework files named in the LOAD SET below are attached to
this message as files rather than pasted inline. They are loaded. Read them in the LOAD
SET's step order. Nothing else is loaded: no file outside that table is in this condition,
whatever any loaded file says about it. Everything else in this prompt, the instructions,
the manifest, the specimen, and the request, is below.
"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("prompt", type=Path, help="a compiled reader-prompt.md")
    ap.add_argument("--out", type=Path, default=None,
                    help="output path (default: reader-wrapper.md beside the input)")
    a = ap.parse_args(argv)

    if not a.prompt.is_file():
        print(f"ERROR: no such file: {a.prompt}", file=sys.stderr)
        return 2
    text = a.prompt.read_text(encoding="utf-8")
    parts = SPLIT.split(text)
    if len(parts) < 3:
        print(f"ERROR: {a.prompt} has no section banners; is it a compiled reader prompt?",
              file=sys.stderr)
        return 2

    head, body = parts[0], parts[1:]
    titles, bodies = body[0::2], body[1::2]
    kept, attach = [head.rstrip() + "\n" + DELIVERY_NOTE], []
    for title, content in zip(titles, bodies):
        if "FRAMEWORK FILE" in title:
            # "R9: FRAMEWORK FILE 1: 0a-portable-poetics-kernel-v0_3_19.md" -> the filename
            attach.append(title.split(":", 2)[-1].strip().split(" ")[0])
            continue
        kept.append(f"{BAR}\n{title}\n{BAR}\n{content}")
    if not attach:
        print(f"ERROR: {a.prompt} holds no framework sections; nothing to strip",
              file=sys.stderr)
        return 2

    out = a.out or a.prompt.with_name("reader-wrapper.md")
    out.write_text("".join(kept), encoding="utf-8", newline="\n")
    before, after = len(text), out.stat().st_size
    print(f"{out}: {after:,} bytes, down from {before:,} ({100 - after / before * 100:.1f}% less to paste)")
    print(f"\nAttach these {len(attach)} files, from the framework bundle or snapshot you compiled against:")
    for name in attach:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
