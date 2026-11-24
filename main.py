"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence (<= 220 chars) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same sentence,
byte for byte, on every run.
"""

import os

PITCH = (
    "The SockMatch 3000 is a clip-on scanner that sniffs your laundry pile, "
    "pairs every lonely sock with its mate in under a second, and texts you "
    "a short eulogy for the ones it declares officially lost."
)

MAX_CHARS = 220


def validate(text):
    """Gate: exactly one sentence, at most MAX_CHARS chars, no newlines."""
    if len(text) > MAX_CHARS:
        raise SystemExit("pitch exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    if "\n" in text:
        raise SystemExit("pitch must not contain a newline")
    return text


def main():
    text = validate(PITCH.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
