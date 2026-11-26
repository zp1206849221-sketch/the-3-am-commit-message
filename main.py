#!/usr/bin/env python3
"""Write the entry line for 'The 3 AM Commit Message' to /output/entry.txt."""

import os

ENTRY = "hotfix: reverting the deploy that broke prod at 3 AM; I had rated it 99.8% safe, a number I also generated"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
