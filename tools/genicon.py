#!/usr/bin/env python3
"""Generate the PWA icons (icon-192.png / icon-512.png) and icon.svg.

Pure stdlib PNG writer — no Pillow. The mark is a stylised plan of Option A:
room outline, north counter run, island, and the nook bench, in the viewer's
gold on its ink background.
"""
import struct, zlib, pathlib

INK = (0x1c, 0x1a, 0x17)
GOLD = (0xc8, 0xa2, 0x4a)
OUT = pathlib.Path(__file__).resolve().parent.parent


def png(path, size):
    s = size
    u = s / 100.0                      # 1 unit == 1% of the icon
    px = [[INK] * s for _ in range(s)]

    def rect(x, y, w, h, c=GOLD):
        x0, y0 = int(x * u), int(y * u)
        x1, y1 = int((x + w) * u), int((y + h) * u)
        for yy in range(max(0, y0), min(s, y1)):
            row = px[yy]
            for xx in range(max(0, x0), min(s, x1)):
                row[xx] = c

    def frame(x, y, w, h, t):
        rect(x, y, w, t); rect(x, y + h - t, w, t)
        rect(x, y, t, h); rect(x + w - t, y, t, h)

    T = 3.2
    frame(14, 16, 72, 68, T)           # room outline
    rect(14, 16, 46, T * 2.6)          # north counter run (heavier)
    rect(38, 44, 34, 13)               # island
    rect(70, 62, 16, 22)               # nook bench block
    rect(14, 60, T * 2.6, 24)          # west run

    raw = b''.join(
        b'\x00' + b''.join(bytes(c) for c in row) for row in px)

    def chunk(tag, data):
        c = tag + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c))

    blob = (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', s, s, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9))
            + chunk(b'IEND', b''))
    path.write_bytes(blob)
    print(f'{path.name}  {s}x{s}  {len(blob)} bytes')


SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<rect width="100" height="100" fill="#1c1a17"/>
<g fill="#c8a24a">
<path d="M14 16h72v3.2H14zM14 80.8h72V84H14zM14 16h3.2v68H14zM82.8 16H86v68h-3.2z"/>
<rect x="14" y="16" width="46" height="8.3"/>
<rect x="38" y="44" width="34" height="13"/>
<rect x="70" y="62" width="16" height="22"/>
<rect x="14" y="60" width="8.3" height="24"/>
</g></svg>
'''

png(OUT / 'icon-512.png', 512)
png(OUT / 'icon-192.png', 192)
(OUT / 'icon.svg').write_text(SVG, encoding='utf-8')
print('icon.svg written')
