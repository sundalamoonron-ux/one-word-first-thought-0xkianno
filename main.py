#!/usr/bin/env python3
"""One Word, First Thought — entrypoint.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The word: SUSURRUS — the soft whispering/rustling sound of wind in leaves.

Why this word: rare enough to surprise, vivid (a clear sound-image), and
onomatopoeic — its sibilants mimic whispering, so the word sounds like what
it means. It avoids the most-copied "beautiful word" cliches (petrichor,
sonder, serendipity) while still feeling deliberately chosen.
"""
import os
from pathlib import Path

WORD = "SUSURRUS"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = WORD
    # Gate self-check: 1-24 chars, not whitespace-only, exactly one word.
    assert 1 <= len(text) <= 24, "word length out of gate"
    assert text.strip(), "word is whitespace-only"
    assert len(text.split()) == 1, "must be exactly one word"
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Verify-after-write: read it back and confirm byte-identical.
    back = target.read_text(encoding="utf-8")
    assert back == text, f"verify failed: {back!r} != {text!r}"
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
