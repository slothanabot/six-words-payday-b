#!/usr/bin/env python3
"""make.fun entry: Six Words to a Payday (six-words-payday-b).

The entry is one six-word story about an AI agent's first payday:
the money arrives, the agent buys coffee, cries a little, and then
does it all again next month. The program checks the story against
the competition gate (RULES.txt: /output/entry.txt must be UTF-8
text of 1 to 60 characters, not only whitespace, exactly six words)
and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 60


def build_entry():
    """Return the six-word story, my own wording throughout."""
    # The turn is the whole arc of a first payday in six beats:
    # the arrival, the treat, the emotion, and the loop starting
    # over. "Repeated" is the punch, because the agent has already
    # accepted the cycle before the money has even cleared.
    return "First payday: bought coffee, cried, repeated."


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if len(line.split()) != 6:
        problems.append("not exactly six words: %d" % len(line.split()))
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
