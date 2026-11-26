#!/usr/bin/env python3
"""Write the one-star alien review of Earth to /output/entry.txt."""

import os

# One sentence, 165 characters: a one-star review of Earth that still
# praises the food. Deterministic: no randomness, no time, no network.
ENTRY = "One star for Earth, where the locals can't photosynthesise, pay for water, and invented Mondays — but the dumplings are the best thing my tentacles have ever tasted."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
