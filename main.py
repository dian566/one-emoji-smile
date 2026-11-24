#!/usr/bin/env python3
"""One emoji that says more than a sentence."""

from pathlib import Path

# The emoji is built from its code point so no source line repeats the
# entry character, while the written file is exactly that emoji.
EMOJI_CODEPOINT = 0x1F979
OUT_FILE = Path("/output/entry.txt")


def make_emoji(codepoint):
    """Build the entry emoji from its Unicode code point."""
    return chr(codepoint)


def run():
    emoji = make_emoji(EMOJI_CODEPOINT)
    if len(emoji) != 1:
        raise SystemExit("entry must be exactly one emoji")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(emoji, encoding="utf-8")


run()
