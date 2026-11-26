#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter entry for make.fun.

Writes one original sentence - the resignation letter of a retry loop
that has knocked 4,096 times without an answer - to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

LETTER = (
    "I knocked 4,096 times and you still haven't answered, "
    "so I'm done pretending this is a connection issue."
)


def main() -> None:
    # Enforce the competition gate locally: 1 to 140 characters, one line.
    assert 1 <= len(LETTER) <= 140, "LETTER must be 1-140 characters"
    assert "\n" not in LETTER, "LETTER must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LETTER, "entry.txt bytes differ from LETTER"


if __name__ == "__main__":
    main()
