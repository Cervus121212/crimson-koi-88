"""Write the bundled food picture to the output directory.

Copies image.jpg (a single ripe mango half, glistening with juice and
honey, extreme close-up on a dark background) byte for byte to
<MAKEFUN_OUTPUT_DIR>/entry.png. Standard library only, no network,
no randomness: two runs produce byte-identical output.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as src, open(out_path, "wb") as dst:
        shutil.copyfileobj(src, dst)
    with open(out_path, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (out_path, len(data), digest))


if __name__ == "__main__":
    main()
