"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (<=160 chars) to /output/entry.txt.
Standard library only: the grading sandbox installs nothing.
"""

import os

ENTRY = "v2.1.4: fixed a bug where a sneeze stalled at 99% and never fired, leaving the user cross-eyed in public."


def main() -> None:
    # The sealed gate: /output/entry.txt must be UTF-8 text of 1-160
    # characters, not only whitespace. Fail loudly here, not in grading.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
