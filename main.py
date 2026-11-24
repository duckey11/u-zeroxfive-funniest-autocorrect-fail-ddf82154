#!/usr/bin/env python3
"""Entry for make.fun bounty u-zeroxfive-funniest-autocorrect-fail-ddf82154.

Writes a single-line funniest-autocorrect-fail entry to /output/entry.txt.
Deterministic: every run writes the exact same bytes, no trailing newline.
"""

import os

ENTRY = "Hey Mom, don't wait up, I'm going to the gin after work to sweat it out, be home by nine!"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
