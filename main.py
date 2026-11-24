#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog - a make.fun entry.

The program writes one single-line changelog entry to entry.txt in
the output directory: a versioned fix for a bug in everyday human
behaviour, in a terse engineering register.
"""

import os

# The changelog entry itself: version number first, then the fix,
# stated the way a release note states it - as already shipped.
NOTE = "v32.1: Fixed the bug where I say 'I'm five minutes away' while still in the shower."


def destination() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main() -> None:
    with open(destination(), "w", encoding="utf-8", newline="") as handle:
        handle.write(NOTE)


if __name__ == "__main__":
    main()
