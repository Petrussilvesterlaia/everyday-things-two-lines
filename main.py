#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Everyday Things, Two Lines, Longer Run'.

Writes the two-line explanation to /output/entry.txt, then validates it
against the gate: exactly 2 lines, each exactly one sentence, none empty.
"""

import os

ENTRY_LINES = [
    "A queue is a caterpillar made of people, shuffling forward one tiny step at a time.",
    "The caterpillar fits because everyone lines up single file and moves at the pace of the person in front, but it leaves out that a caterpillar's legs all belong to one body, while each person in a queue can stop, chat, or walk away whenever they like.",
]

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    text = "\n".join(ENTRY_LINES) + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    # Self-validation: read back and check the gate rules.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    for i, line in enumerate(lines, start=1):
        assert line.strip(), f"line {i} is empty"
        assert line.count(".") == 1 and line.rstrip().endswith("."), (
            f"line {i} must be exactly one sentence"
        )
        print(f"line {i}: {len(line)} characters")

    print(f"Wrote {OUTPUT_PATH} ({len(content)} characters total)")


if __name__ == "__main__":
    main()
