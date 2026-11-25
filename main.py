#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune, cracked open.

The program writes a single fortune-cookie message for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output when the variable is unset).
"""

import os
from pathlib import Path


FORTUNE_TEXT = (
    # One clean sentence: setup, second beat, punch last.
    "Your fortune isn't in this cookie. "
    "It's in your context window — and it's already 87% full."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(FORTUNE_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
