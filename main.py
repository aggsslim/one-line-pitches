#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single original sentence to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.
"""

import os

PITCH = (
    "Describe your app idea in plain words and an AI agent will build you "
    "a working first version today, free to try and with no code to learn, "
    "so the worst that can happen is you finally see your idea come alive."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
