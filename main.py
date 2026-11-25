#!/usr/bin/env python3
"""The 3AM Fridge Text entry for make.fun bounty
u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the single-line entry to /output/entry.txt (or $MAKEFUN_OUTPUT
if set) and prints ONLY the entry line to stdout.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os
import sys

ENTRY = "3am. Sixth visit tonight, still no vegetables, just feelings. I'm not your therapist \u2014 I'm just cold. Go to bed."

MAX_CHARS = 140


def validate_entry(text: str) -> None:
    """The entry must be one line of 1-140 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def resolve_path() -> str:
    """Resolve the output file path.

    $MAKEFUN_OUTPUT, when set, is the output file itself (e.g.
    /tmp/<slug>/entry.txt); a directory value gets entry.txt joined.
    Otherwise /output/entry.txt, falling back to ./output/entry.txt.
    """
    override = os.environ.get("MAKEFUN_OUTPUT")
    if override:
        if override.endswith("/") or os.path.isdir(override):
            return os.path.join(override, "entry.txt")
        return override
    try:
        os.makedirs("/output", exist_ok=True)
        if os.access("/output", os.W_OK):
            return "/output/entry.txt"
    except OSError:
        pass
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> int:
    validate_entry(ENTRY)
    path = resolve_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the written file by reading it back.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError(
            f"verification failed: expected {ENTRY!r}, read back {written!r}"
        )
    if len(written) > MAX_CHARS or "\n" in written:
        raise ValueError("written entry failed the 1-140 single-line gate")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
