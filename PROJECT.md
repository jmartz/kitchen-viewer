# Kitchen Renovation 3D Walkthrough — Project Handoff

Owner: Jim · Built collaboratively with Claude (chat session, Aug 2026)
Purpose: walkable 3D comparison of two proposed kitchen layouts (Option A / Option B)
from TY Engineering sheet S2.2, verified against the drawings, styled to match the
real house, headed for Quest 2 VR.

---

## 1. Current State

A single self-contained HTML file (`kitchen-walkthrough.html`, three.js r128 from
cdnjs) containing both kitchen options, walkable in first person, with:

- **Option A**: 8'-0" × 3'-2" island (oak or navy toggle), cooktop + 2' oven cabinet
  ending the 10'-5" north run, fridge in the 3'-2" bay, 16"-deep pantry in the 3'-0"
  bay, sink under the west 6' sliding window, banquette nook (L-bench + 2' × 8'-4"
  pedestal table) against the 11'-9" dining wall.
- **Option B**: nook moves west under the sliding window; galley-U east: 8' peninsula
  with tucked stools, sink under a north window, slide-in range + fridge on the
  dining wall.
- **Shared shell**: family room (15'-0" wide, vaulted whitewashed-plank ceiling with
  dark beams), centered tan ledgestone fireplace flanked by two French-door units
  with transoms, 21' × 22'-11" deck with railing + NW stairs, dining room, correct
  wall jogs and passages.
- **Views**: Walk (drag-look + WASD, touch joysticks), 3D top, 2D plan (zoom/pan,
  live model linework over the embedded scanned drawings, dimensions, player dot).
- **Verification toggles**: Plan floor (scanned sheet on the ground at 1:1) and
  X-ray (model at 30% opacity) — the combination that caught most late bugs.
- **Finish**: PBR materials (Standard/Physical), IBL environment, ACES tone mapping,
  2048px soft shadows, procedural textures (oak grain, veined quartz, plaster,
  ledgestone, weave, brushed steel), shaker door/drawer geometry with brass
  hardware, outlets, photo-matched palette (greige walls, white trim + dark levers,
  pale wide-plank floors).
- **textures/ loader**: drops in photo JPGs by filename with per-file fallback and a
  bottom-right toast on misses.

## 2. How to Run

- Windows: extract the zip, double-click `Start-viewer.bat` (serves on
  localhost:8437 and opens the browser — required for Chrome to load textures/).
- Anything else: `python -m http.server` in the folder, open
  `http://localhost:8000/kitchen-walkthrough.html`. Firefox tolerates plain
  double-click (file://) including textures.
- Controls: drag to look, WASD/arrows, Shift runs. Panel top-left: A/B, view modes,
  Oak/Navy island, Plan floor, X-ray, lens (FOV) slider, collapse button.

## 3. Repository Layout (this zip)

```
kitchen-walkthrough.html   the entire app (HTML+CSS+JS, plan sheets embedded b64)
textures/                  9 generated texture JPGs (overwrite with photo textures
                           of the same names to upgrade: floor, stone, wood,
                           quartz, wall, tile, ceiling, fabric, steel)
reference/                 200dpi rasters of both S2.2 sheets (the registration
                           basis for all tooling: 50 px/ft, origin px 1913,1901).
                           NOTE: re-add the original Option_A/B PDFs and the
                           S202-48x.dwg from Jim's copies — they expired from the
                           chat session's upload store.
tools/                     verification pipeline (see §5)
Start-viewer.bat, README.txt, PROJECT.md
```

## 4. Architecture Notes (inside the HTML)

- **Units**: authored in feet, converted by `F(ft)=ft*0.3048` — real meters
  everywhere, deliberately WebXR-safe for the Quest step.
- **Axes**: +X east, +Z south, +Y up. Origin = NW interior corner of the kitchen
  zone (the 21'-1" × 12'-2" room).
- **Builders**: `wallSeg` (walls with openings, auto glass/frames/shade valances,
  variable height), `counter`, `shakerRun` (door/drawer/knob geometry),
  `banquette`, `trestleTable` (pedestal posts), `stool`, `chair`, `fridge`,
  `pendant`, `railing`, `outlet`, `matFit` (world-scale texture clone for a face).
- **Collision**: every solid registers an AABB in `solids[]`; movement does
  circle-vs-AABB pushout; `solids` also feeds the minimap and 2D plan.
- **Layout functions**: `buildShared(opt)` + `buildOptionA/B()`. Option/finish
  toggles rebuild `world` in place (camera stays put — the key comparison trick).
- **2D plan view**: reads live `world.children` geometry every frame (never a
  cached image), draws over the embedded sheet crops. Mapping: the b64 crops cover
  ft x −24.38..37.62, z −5.96..46.04 (raster px (713,1601)-(3813,4201) at
  50 px/ft, corrected origin). See the `PLAN_X0..PLAN_Z1` constants.
- **Raster registration**: sheet scans are 200 dpi of 1/4"=1'-0" → **50 px/ft**;
  model origin sits at raster pixel **(OX,OY) = (1913, 1901)**.
- **PBR**: materials authored as Lambert/Phong for simplicity, then `convertPBR()`
  swaps to Standard/Physical with per-material roughness/metalness/clearcoat/
  bumpScale/envMapIntensity from one `spec` table; colors are
  `convertSRGBToLinear()`ed and texture maps tagged sRGB (see lesson L7).
- **External textures**: `loadExternalTextures()` — per-file async load, repeat per
  target material, wood tints reset to white when photo wood loads, full
  `buildOption(current)` rebuild after loads so `matFit` clones pick up new maps.

### Key verified coordinates (all line-scanned from the raster)
- Kitchen zone 21.08 × 12.17 ft; counters faces at 2.33 from wall lines; aisles
  3'-6" cabinet-face to face (island faces at 5.83).
- North run (A): counter 0.25–8.4, oven cab 8.4–10.42, fridge bay 10.42–13.58,
  shallow pantry 13.58–16.58 (1.35 deep), window 17–20.
- Island (A): body 7.6 × 2.1 under an 8.0 × 3.17 top, 12" seating overhang south.
- Nook (A): table capsule x 17.78–19.78, z 1.5–9.8; east bench face at x=19.96;
  south L-return block x 15.64–17.96, z 9.96–11.42; pendants z 3.66/5.70/7.74.
- Kitchen/dining wall: body x 21.08–21.53 (z 0–11.76); the **family east wall is
  flush** with it at x 21.08–21.53 from z 15.58 south (the old 5" jog was a
  registration artifact); open passage z 11.76–15.58 (~3'-10").
- Family room x 6.1–21.08, z 12.17–35.09; fireplace footprint x 4.66–6.62
  (proud toward deck), z 20.67–27.27; north French doors z 15.02–20.42; south
  door+sidelites z 27.77–34.17. Deck x −14.9–6.1, stairs at NW.

## 5. Verification Tooling (tools/) — the real infrastructure

Three independent checks; between them they caught every major bug.

1. **Geometry harness** (`tools/harness.js` + assembly in `tools/assemble.py`):
   stubs THREE/DOM, executes the HTML's own build functions in Node, dumps every
   placed box/cylinder footprint to `footprints.json`. Guarantees the 2D checks
   describe exactly what the 3D shows.
2. **Overlay renders**: footprints drawn on the brightened sheet raster at 50 px/ft
   from origin (1913,1901). Colors: red = wall-height, orange solid = counter/table
   tops, orange dashed = bases (matches drafting convention), blue = seats.
3. **Headless screenshot renderer** (`tools/render_run.js`): real three.js under
   `xvfb-run` with npm `gl` + `canvas`. Renders actual PBR screenshots of the file
   so Claude can see its own output. Setup on Ubuntu:
   `apt install xvfb libgl1 libglu1-mesa; npm i three@0.128.0 gl canvas;`
   `xvfb-run -a node render_run.js`. Canvas textures are converted to DataTextures
   (row-flipped) because headless-gl can't ingest node-canvas objects; the GL
   context needs `glctx.canvas = fakeCanvas` attached.
4. **Raster line-scan** (technique, in `assemble.py` helpers): to locate any drawn
   element, scan a pixel row/column for dark runs and convert via origin + 50 px/ft.
   This is the *only* trusted way to measure the drawing.

## 6. What We Learned (hard-won — read before continuing)

- **L1 — Read the whole sheet first.** Early errors (family room width, missing
  deck, dining extent) came from cropping straight to the kitchen. Room
  relationships live at sheet scale.
- **L2 — Never measure from screenshot pixels.** A user screenshot has no scale
  reference; doing this once shifted the nook a foot and caused a regression.
  Line-scan the original raster instead (§5.4).
- **L3 — Assert every automated edit.** A silent `str.replace` no-op left the
  entire texture library out of the file for two rounds while "contrast tweaks"
  edited nothing. Every patch now asserts anchor counts.
- **L4 — Close the visual loop before iterating on visuals.** Text-only iteration
  on photorealism wasted rounds; the headless renderer found in minutes what
  guessing missed (black metals, missing textures, shadow spiders).
- **L5 — Drafting conventions carry meaning.** Solid outline = countertop, dashed
  = cabinet base, scallops = tucked seats, wall length dims (11'-9") are the wall,
  gray poché = existing wall, jamb ticks bracket openings, ⊗ per legend = pendant.
  The legend is authoritative; check it before interpreting symbols.
- **L6 — Dimensions measure interior faces.** Walls sit *beside* dim lines, not
  centered on them; adjacent rooms can jog. Model walls
  accordingly or every neighboring room accumulates offset.
- **L7 — Color management bites once per project.** sRGB output + sRGB-authored
  material colors = double gamma washout. Convert colors to linear, tag texture
  maps sRGB, keep exactly one output transform.
- **L8 — Box UVs stretch textures per face.** World-scale realism needs per-mesh
  repeat (`matFit`) on hero surfaces, or triplanar shaders later.
- **L9 — The user's photos outrank my reading of the plan** for existing
  conditions (fireplace centered, French doors, vault) — but the plan outranks
  aesthetic invention (my 10' hearth). Track which lines are drawing-derived vs
  photo-derived vs invented; flag inventions to the user.
- **L10 — Perception issues can be camera issues.** "Everything feels inflated" was
  a 72° FOV, not geometry. Give users a lens control; remind them VR eliminates
  this class entirely.
- **L11 — Small fixtures shouldn't cast shadows** (pendant "spiders"), and interior
  scale reads through furniture (tucked stools, table lengths, bench overlap).
- **L12 — One source of truth.** 2D plan, minimap, dims, and collision all derive
  from the same build functions, so verification can't drift from reality.

## 7. If Starting Over (recommended future methodology)

1. Line-scan the sheet **first** into a JSON layout spec (walls, openings, fixtures
   with coordinates + provenance tags: drawing / photo / assumption).
2. Generate 3D, 2D plan, dimension annotations, and collision from that one spec.
3. Stand up the screenshot pipeline before any visual polish; every change ships
   with a self-rendered before/after.
4. Assert-checked patches only; keep the reassembly scripts in-repo (done — tools/).
5. Work in Cowork with a live browser from day one for interactive-framerate
   feedback (this transfer is that step).
6. textures/ folder + localhost launcher from the start; procedural is fallback.

## 8. Remaining Roadmap

- **Quest 2 / WebXR (next, small)**: `renderer.xr.enabled = true`, add a VR button
  (hand-roll or bundle VRButton), controller thumbstick locomotion reusing the
  existing collide(), snap-turn option. Keep meters (already true). Perf on Quest:
  pixelRatio 1, consider a shadow-off toggle, current poly count is fine. Open via
  the Quest browser at the laptop's LAN address (same http.server, use the
  machine's IP), or host the folder anywhere static.
- **Path-traced photo mode (optional)**: three-gpu-pathtracer for converged stills
  while standing still; or export scene to GLB (`GLTFExporter`) and render in
  Blender Cycles for true finish-decision renders.
- **Photo textures**: overwrite textures/*.jpg with ambientCG / Poly Haven sets.
- **Option B parity audit**: B received far less drawing-verification than A —
  run the same plan-floor/X-ray + overlay passes (peninsula seat scallop positions,
  B nook capsule, B window sizes were never line-scanned).
- **Polish backlog**: vault gable ends are flat boxes (could be true triangles),
  family room furnishing beyond sofa/rug, yard/exterior context, camera bookmarks
  ("stand at the sink" presets), oak grain still slightly stripey on small parts,
  under-cabinet lighting, toe kicks.
- **Decision support**: side-by-side A/B split screen, cost/impact notes overlay.

## 9. Session Continuity

Claude's memory for this project lives under `/areas/kitchen-viewer.md` (project
history, corrections, and the L2/L3-class lessons are recorded there), so a new
Claude session — including Cowork — starts with this context. This PROJECT.md is
the fuller, self-contained version; point the Cowork session at it first.
