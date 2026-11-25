#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of exactly 100 words, spoken by a fantasy villain
who is secretly just very tired, to /output/entry.txt.

The tiredness lives in the voice, the rhythm and the small deflections:
the stool instead of the throne, the queue behind the dragon, the grout
in the lava moat, the paperwork. The villain never says he is weary.
He still has a scheme (ember pits, moonlight tax, goblin union) and a
history (thirty years on the throne, a speech he used to give), and the
last line lands the sting.
"""

import os

MONOLOGUE = (
    "Hero. Sit down, not the throne, the stool. The throne's for ceremonies, "
    "and my knees have filed a complaint. Thirty years I've kept the ember "
    "pits burning, the tax on moonlight collected, the goblin union... "
    "negotiated with. You came to slay me, yes? Lovely. Queue's behind the "
    "dragon. He's been waiting since Tuesday, poor thing. I had a whole speech once, "
    "thunder, prophecy, the bit where the torches gutter. Now? I just want "
    "the lava moat drained before it stains the grout. So. Sword up, "
    "then. One duel, no encores, and if you win, gods help you, the "
    "paperwork's yours."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
