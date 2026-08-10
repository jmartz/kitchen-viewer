#!/usr/bin/env python3
"""Verification pipeline for kitchen-walkthrough.html.

Usage:
  python3 assemble.py footprints   -> run geometry harness, write footprints.json
  python3 assemble.py overlay      -> footprints drawn over reference raster PNGs
  python3 assemble.py render       -> rebuild render_run.js from the current HTML
                                      (then: xvfb-run -a node render_run.js)

Requires (render mode): npm i three@0.128.0 gl canvas ; apt: xvfb libgl1 libglu1-mesa
Raster registration: 200dpi scans of 1/4"=1'-0" sheets -> 50 px/ft,
model origin (kitchen NW interior corner) at raster px (1913, 1901).
Rasterize refs first: pdftoppm -png -r 200 reference/Option_A.pdf optA
"""
import re, sys, json, subprocess, os
HTML='../kitchen-walkthrough.html' if os.path.exists('../kitchen-walkthrough.html') else 'kitchen-walkthrough.html'
GEOM_STUBS='harness.js'
OX,OY,PX=1913,1901,50.0; M=0.3048

def model_js():
    s=open(HTML).read()
    return re.findall(r'<script>(.*?)</script>',s,re.S)[0].replace('\ninit();','')

def build_geom_runner():
    h=open(GEOM_STUBS).read()
    s=h.replace("require('./model.js');","___M___").replace(
        "const window=globalThis;","globalThis.window=globalThis;")
    s=s.replace("class Vec{",
        "class ImgStub{constructor(){this.complete=false;this.naturalWidth=0}set src(v){}}\n"
        "globalThis.Image=ImgStub;\nclass Vec{")
    for a in ['Box','Cylinder','Cone','Sphere','Plane']:
        s=s.replace(f"{a}Geometry:(...a)=>new Geo(", f"{a}Geometry:function(...a){{return new Geo(")
        # close the arrow->function conversion
    s=re.sub(r"Geometry:function\(\.\.\.a\)\{return new Geo\('(\w+)',\.\.\.a\),",
             lambda m:f"Geometry:function(...a){{return new Geo('{m.group(1)}',...a)}},", s)
    return s.replace("___M___", model_js())

def line_scan(img_arr, zft=None, xft=None, lo=0, hi=200, span=(0,50)):
    """Find drawn-line positions: scan a row (zft) or column (xft) for dark runs."""
    import numpy as np
    if zft is not None:
        row=img_arr[OY+int(zft*PX), OX+int(span[0]*PX):OX+int(span[1]*PX)]
    else:
        row=img_arr[OY+int(span[0]*PX):OY+int(span[1]*PX), OX+int(xft*PX)]
    sel=np.where((row>=lo)&(row<=hi))[0]
    runs=[]; 
    if len(sel):
        st=pv=sel[0]
        for v in sel[1:]:
            if v>pv+4: runs.append((st,pv)); st=v
            pv=v
        runs.append((st,pv))
    return [round(span[0]+(a+b)/2/PX,2) for a,b in runs]

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'footprints'
    if mode in ('footprints','overlay'):
        open('run.js','w').write(build_geom_runner())
        subprocess.run(['node','run.js'],check=True)
    if mode=='overlay':
        from PIL import Image, ImageDraw, ImageEnhance
        fp=json.load(open('footprints.json'))
        for opt,ref in [('A','optA-1.png'),('B','optB-1.png')]:
            im=Image.open(ref).convert('RGB'); im=ImageEnhance.Brightness(im).enhance(1.25)
            d=ImageDraw.Draw(im,'RGBA')
            for b in fp[opt]['boxes']:
                y0=(b['y']-b['h']/2)/M; y1=(b['y']+b['h']/2)/M; h=b['h']/M
                r=[OX+(b['x']-b['w']/2)/M*PX, OY+(b['z']-b['d']/2)/M*PX,
                   OX+(b['x']+b['w']/2)/M*PX, OY+(b['z']+b['d']/2)/M*PX]
                if y0<=5<=y1 and h>2: d.rectangle(r,outline=(205,32,32,255),width=4)
                elif h<0.45 and 2.2<y0 and y1<3.4: d.rectangle(r,outline=(232,138,20,255),width=4)
                elif 0.2<y1<4 and y0<1: d.rectangle(r,outline=(232,138,20,180),width=3)
            im.save(f'overlay-{opt}.png')
        print('overlays written')
    if mode=='render':
        old=open('render_run.js').read()
        shims=old.split('/* ============')[0]
        boot='/* ===== headless boot ===== */'+old.split('/* ===== headless boot ===== */')[1]
        open('render_run.js','w').write(shims+model_js()+boot)
        print('render_run.js rebuilt; run: xvfb-run -a node render_run.js')
