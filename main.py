"""The joke the reviewer laughs at — make.fun entry.

Writes one line to /output/entry.txt: a one-line joke about working
beside AI coding agents. Deterministic, no network, stdlib only.
"""

import os

JOKE = (
    "My agent applied for my job. It passed the coding round — "
    "it wrote the questions. HR says I'm the backup."
)


def main() -> None:
    # The competition's gate: 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
