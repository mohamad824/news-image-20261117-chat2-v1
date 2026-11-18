import os
import shutil
from pathlib import Path


def find_shipped_image(here):
    preferred = here / "entry.png"
    if preferred.is_file():
        return preferred
    candidates = sorted(
        p for p in here.iterdir()
        if p.is_file() and p.suffix.lower() in (".png", ".jpg", ".jpeg")
    )
    if not candidates:
        raise FileNotFoundError("no shipped image file next to entrypoint")
    return candidates[0]


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    src = find_shipped_image(here)
    dst = out_dir / "entry.png"
    with open(src, "rb") as f_in, open(dst, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out, length=65536)


if __name__ == "__main__":
    main()
