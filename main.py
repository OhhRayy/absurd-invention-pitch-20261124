"""One-Sentence Absurd Invention Pitch (make.fun bounty u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

Writes a single sentence to /output/entry.txt pitching a ridiculous
invention that fixes a tiny everyday annoyance. Deterministic, no
network, no randomness, no input: the same sentence, byte for byte, on
every run. The pitch was chosen for the judge's brief: a funny
invention (a toaster that apologises in writing before burning your
bread), a clever fix (the betrayal at least comes with paperwork), an
original angle (appliance bureaucracy instead of a smarter appliance),
and one tight sentence - 118 characters, nothing left to explain.
"""

import os

LINE = (
    "A toaster that files a formal apology before burning your bread, "
    "so at least the betrayal comes with paperwork."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters,
    # not only white space. This sentence is 118 characters.
    assert 1 <= len(text) <= 220, "line must be 1-220 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
