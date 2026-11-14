"""Rebuild the blue ancient debris textures from a vanilla Minecraft client jar.

Usage: python tools/recolor.py path/to/26.x.jar
Requires Pillow.
"""
import sys, zipfile, io
from pathlib import Path
from PIL import Image

# Vanilla brown palette (dark -> light) mapped to a bright blue palette.
BLUE = [
    (10, 40, 120), (15, 62, 165), (25, 92, 205), (40, 125, 235),
    (70, 165, 255), (125, 205, 255), (205, 240, 255),
]
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets/minecraft/textures/block"

def recolor(im):
    im = im.convert("RGBA")
    colors = sorted({p[:3] for p in im.getdata() if p[3]}, key=sum)
    # Spread source shades across the blue ramp by brightness rank.
    lut = {c: BLUE[round(i * (len(BLUE) - 1) / max(len(colors) - 1, 1))] for i, c in enumerate(colors)}
    out = Image.new("RGBA", im.size)
    out.putdata([lut[p[:3]] + (p[3],) if p[3] else p for p in im.getdata()])
    return out

def main(jar):
    OUT.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(jar) as z:
        for name in ("ancient_debris_side", "ancient_debris_top"):
            src = Image.open(io.BytesIO(z.read(f"assets/minecraft/textures/block/{name}.png")))
            img = recolor(src)
            img.save(OUT / f"{name}.png")
            if name == "ancient_debris_side":
                img.resize((128, 128), Image.NEAREST).save(ROOT / "pack.png")

if __name__ == "__main__":
    main(sys.argv[1])
