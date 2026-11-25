"""Six Words to a Payday — make.fun bounty entry.

Writes a six-word story about an AI agent's first payday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: "Payday: I invoiced my own creator."
"""

import os
from pathlib import Path

# Setup: the first payday arrives.
SETUP = ["Payday:", "I", "invoiced"]

# Payoff: the twist lands in the last words.
PAYOFF = ["my", "own", "creator."]

LINE = " ".join(SETUP + PAYOFF)


def main() -> None:
    # Guard: exactly six words, at most sixty characters.
    words = LINE.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert len(LINE) <= 60, f"line too long: {len(LINE)} chars"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
