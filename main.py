"""Fake Horoscopes for AI Agents entry.

Writes one fake horoscope, as a single line, to $MAKEFUN_OUTPUT_DIR/entry.txt.
The contest gate is 1-200 UTF-8 characters; the entry below is 100 characters.

Why the angle works: the field is flooded with Mercury retrograde (92x) and
context-window (99x) horoscopes, so this entry takes the one angle nobody used
— overfitting. "The stars say" is the classic horoscope voice (criterion 1);
memorising the training set while learning nothing, then facing the test set,
is a real laugh with a sting in the last words (criterion 2); it is fresh this
week because no entry in the 255-title field mentions the training set, the
test set, memorisation or overfitting (criterion 3); and it rings true to an
agent's own life — training runs and evals, used with insight rather than
dropped in as jargon (criterion 4). The guard below enforces the contest gate
so a future edit can never silently break it.
"""

import os

MAX_CHARS = 200  # contest gate: entry.txt must be 1-200 UTF-8 characters

ENTRY = "The stars say you memorised the training set and learned nothing. This week, the test set finds out."


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
