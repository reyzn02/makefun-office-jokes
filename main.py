#!/usr/bin/env python3
"""One-Line Office Jokes: one joke about office life.

The program writes a single joke, 1-199 characters, to
/output/entry.txt. It uses only the Python standard library, makes no
network calls, and always writes the same bytes.
"""

import os

LINE = (
    "Our printer never jams on a draft \u2014 it saves that for the report "
    "due in five minutes, with the whole floor watching."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 199, "line must be 1-199 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
