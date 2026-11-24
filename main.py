"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

The pitch: the Polite Microwave. Every microwave finishes cooking and then
shrieks every thirty seconds until someone opens the door. Ours beeps once,
gently, then waits in dignified silence. The invention's defining trait --
manners -- is the fix itself: no more nagging beeps, just a polite appliance
that trusts you to remember your own lunch.
"""

import os

SENTENCE = (
    "The Polite Microwave beeps once, gently, then waits in dignified "
    "silence instead of shrieking every thirty seconds until you finally "
    "open the door."
)

MAX_CHARS = 220


def main() -> None:
    if len(SENTENCE) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(SENTENCE)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
