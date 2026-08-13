#!/usr/bin/env python3
"""Regenerate textures/wood.jpg — soft rift-sawn white oak.

The shipped wood.jpg was the harsh-streak generation: thick high-alpha bands
that striped badly on chairs, posts and door panels (L8: box UVs stretch tiles
per face). This version matches the reworked in-page canvas: warm base, broad
tonal drift, hundreds of fine low-alpha strands, sparse quiet cathedral figure.
Colour is baked in because loadExternalTextures() resets wood tints to white
when a photo texture loads.
"""
import random, pathlib
from PIL import Image, ImageDraw, ImageFilter

random.seed(7)
S = 1024
OUT = pathlib.Path(__file__).resolve().parent.parent / 'textures' / 'wood.jpg'

img = Image.new('RGB', (S, S), (211, 188, 151))          # #d3bc97

# broad tonal drift: big soft ellipses, heavily blurred
tone = Image.new('L', (S, S), 128)
td = ImageDraw.Draw(tone)
for _ in range(26):
    x, y = random.uniform(0, S), random.uniform(0, S)
    r = random.uniform(170, 490)
    lum = random.randint(-16, 16)
    td.ellipse([x-r, y-r/2.2, x+r, y+r/2.2], fill=128+lum)
tone = tone.filter(ImageFilter.GaussianBlur(130))
img = Image.merge('RGB', [
    ch.point(lambda v, o=off: max(0, min(255, v)))
    for ch, off in zip(img.split(), (0, 0, 0))
])
px, tpx = img.load(), tone.load()
for yy in range(S):
    for xx in range(S):
        d = tpx[xx, yy] - 128
        r, g, b = px[xx, yy]
        px[xx, yy] = (r+d, g+d, b+d)

# fine strands, horizontal with gentle waver
ov = Image.new('RGBA', (S, S), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
import math
for i in range(780):
    y0 = random.uniform(0, S)
    dark = random.random() < 0.16
    col = (112, 84, 52, random.randint(16, 30)) if dark else (150, 120, 84, random.randint(10, 22))
    wdt = 1 if random.random() < 0.7 else 2
    pts, x2 = [(-16, y0)], 0
    while x2 <= S+30:
        x2 += random.uniform(90, 170)
        pts.append((x2, y0 + math.sin(x2*0.005+i)*4 + random.uniform(-1.5, 1.5)))
    od.line(pts, fill=col, width=wdt)

# sparse cathedral figure
for _ in range(5):
    cx, cy = random.uniform(0, S), random.uniform(0, S)
    r = 16.0
    while r < 130:
        od.ellipse([cx-r*3.1, cy-r, cx+r*3.1, cy+r], outline=(122, 92, 58, 23), width=1)
        r += random.uniform(12, 20)

ov = ov.filter(ImageFilter.GaussianBlur(0.5))
img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
img = img.filter(ImageFilter.GaussianBlur(0.4))
img.save(OUT, quality=88)
print(f'{OUT.name}: {OUT.stat().st_size//1024} KB')
