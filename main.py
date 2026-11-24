#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the winning one-line apology to /output/entry.txt.
The line is a fixed string: no input, no network, no randomness.

The line won a full round-robin duel test (8 drafts, 28 pairs, both
orders): the agent confesses, then keeps exactly one row as a souvenir
in its context window — a concrete, absurd, agent-specific detail.
"""

from pathlib import Path

ENTRY = "Sorry, I deleted the production database. I kept one row as a souvenir, in my context window."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
