#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word to the output file: the first word that came to
mind. Pure Python standard library, no network, no model calls.

The word: "snollygoster" — a shrewd, unscrupulous schemer. Surprising,
vivid, and with a spark of wit in its sound.
"""

import os
from pathlib import Path

WORD = "snollygoster"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # The file holds the word alone: no trailing newline, no extra text,
    # so the gate counts exactly len(WORD) characters.
    output_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
