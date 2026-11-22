#!/usr/bin/env python3
"""Salin gambar makanan yang sudah disiapkan ke direktori output.

Program ini mengambil image.jpg yang ada di samping file ini — sebuah
belahan mangga matang, berkilau jus dan madu, close-up ekstrem dengan
latar gelap — lalu menyalinnya apa adanya ke
$MAKEFUN_OUTPUT_DIR/entry.png. Penyalinan dilakukan byte demi byte,
jadi isi entry.png identik dengan image.jpg.

Hanya memakai pustaka standar Python. Tidak ada akses jaringan, tidak
ada angka acak, tidak ada waktu — dua kali jalan hasilnya sama persis.
"""

import hashlib
from pathlib import Path

# Nama file sumber dan file hasil.
SOURCE_NAME = "image.jpg"
TARGET_NAME = "entry.png"

# Ukuran blok baca/tulis (64 KiB) supaya penyalinan hemat memori.
CHUNK_SIZE = 65536


def copy_image(source: Path, target: Path) -> bytes:
    """Salin source ke target per blok, lalu kembalikan hash SHA-256 hasilnya."""
    hasher = hashlib.sha256()
    with source.open("rb") as reader, target.open("wb") as writer:
        while True:
            block = reader.read(CHUNK_SIZE)
            if not block:
                break
            writer.write(block)
            hasher.update(block)
    return hasher.digest()


def run() -> None:
    import os

    source = Path(__file__).resolve().parent / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME

    digest = copy_image(source, target)
    print(
        "entry.png ditulis: %s (%d byte, sha256 %s)"
        % (target, target.stat().st_size, digest.hex())
    )


if __name__ == "__main__":
    run()
