"""news-image-20261124 V1 entry program.

Copies the pre-rendered entry.png that ships in this repository to the
output directory requested by the harness. Python 3.13, standard library
only. No network, no clock, no randomness: every run writes the same
bytes, so two runs are byte-identical.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        print(f"error: {IMAGE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)
    os.chmod(destination, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
