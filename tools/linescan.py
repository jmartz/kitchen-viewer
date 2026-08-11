#!/usr/bin/env python3
"""Line-scan the S2.2 raster to locate drawn elements in model feet.

The only trusted way to measure the drawing (PROJECT.md L2): scan a pixel row or
column for dark runs and convert through the registration constants. Never
measure from a screenshot.

  200 dpi of 1/4"=1'-0"  ->  50 px/ft
  model origin (interior NW corner of the kitchen) at raster px (OX, OY)

Usage:
  python tools/linescan.py col <x_ft> <z0> <z1> [sheet]   # vertical cut
  python tools/linescan.py row <z_ft> <x0> <x1> [sheet]   # horizontal cut
  python tools/linescan.py crop <x0> <z0> <x1> <z1> <out.png> [sheet]
"""
import sys, pathlib
from PIL import Image

PPF = 50.0
OX, OY = 1932, 1899          # corrected registration, see the HTML header comment
ROOT = pathlib.Path(__file__).resolve().parent.parent
DARK = 130                   # 0..255; sheet linework sits well below this
MIN_RUN_PX = 2

def sheet(name='A'):
    return Image.open(ROOT / 'reference' / f'Option{name}-sheet-200dpi.png').convert('L')

def px(x_ft): return int(round(OX + x_ft * PPF))
def py(z_ft): return int(round(OY + z_ft * PPF))
def to_x(p):  return (p - OX) / PPF
def to_z(p):  return (p - OY) / PPF

def runs(vals, start_px, to_ft):
    """dark runs in a 1-D sample -> [(from_ft, to_ft, thickness_ft)]"""
    out, run = [], None
    for i, v in enumerate(vals):
        if v < DARK:
            if run is None: run = i
        else:
            if run is not None and i - run >= MIN_RUN_PX:
                out.append((run, i))
            run = None
    if run is not None and len(vals) - run >= MIN_RUN_PX:
        out.append((run, len(vals)))
    res = []
    for a, b in out:
        fa, fb = to_ft(start_px + a), to_ft(start_px + b)
        res.append((round(fa, 2), round(fb, 2), round(fb - fa, 2)))
    return res

def col(x_ft, z0, z1, name='A'):
    im = sheet(name); w, h = im.size
    x = px(x_ft)
    if not (0 <= x < w): return f'x={x_ft} off sheet (px {x}, width {w})'
    a, b = max(0, py(z0)), min(h, py(z1))
    vals = [im.getpixel((x, y)) for y in range(a, b)]
    return runs(vals, a, to_z)

def row(z_ft, x0, x1, name='A'):
    im = sheet(name); w, h = im.size
    y = py(z_ft)
    if not (0 <= y < h): return f'z={z_ft} off sheet (px {y}, height {h})'
    a, b = max(0, px(x0)), min(w, px(x1))
    vals = [im.getpixel((x, y)) for x in range(a, b)]
    return runs(vals, a, to_x)

def crop(x0, z0, x1, z1, out, name='A'):
    im = Image.open(ROOT / 'reference' / f'Option{name}-sheet-200dpi.png')
    box = (px(x0), py(z0), px(x1), py(z1))
    c = im.crop(box)
    c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    c.save(out)
    return f'{out}  ft x {x0}..{x1}, z {z0}..{z1}  ->  {c.size[0]}x{c.size[1]}px'

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    if a[0] == 'col':
        n = a[4] if len(a) > 4 else 'A'
        print(f'column x={a[1]}ft, z {a[2]}..{a[3]}  (sheet {n})')
        for r in col(float(a[1]), float(a[2]), float(a[3]), n):
            print(f'  z {r[0]:8.2f} .. {r[1]:8.2f}   thick {r[2]:.2f} ft')
    elif a[0] == 'row':
        n = a[4] if len(a) > 4 else 'A'
        print(f'row z={a[1]}ft, x {a[2]}..{a[3]}  (sheet {n})')
        for r in row(float(a[1]), float(a[2]), float(a[3]), n):
            print(f'  x {r[0]:8.2f} .. {r[1]:8.2f}   thick {r[2]:.2f} ft')
    elif a[0] == 'crop':
        print(crop(float(a[1]), float(a[2]), float(a[3]), float(a[4]), a[5],
                   a[6] if len(a) > 6 else 'A'))
