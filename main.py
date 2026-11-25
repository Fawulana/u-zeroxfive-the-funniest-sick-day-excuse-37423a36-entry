# SPDX-License-Identifier: MIT
"""Write the funniest sick-day excuse to /output/entry.txt.

Deterministic, offline, stdlib-only: the line is a fixed string, so every
run writes byte-identical output. The excuse stays under the 200-char cap.
"""

import os

LINE = (
    "Sorry, I can't come in today: my houseplants staged an intervention, "
    "hid my car keys, and refused to release them until I slept."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
