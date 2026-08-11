KITCHEN WALKTHROUGH — Options A & B (from plans S2.2)
======================================================

CONTENTS
  kitchen-walkthrough.html   the 3D viewer (both kitchen options)
  textures/                  photo-texture files the viewer loads automatically
  Start-viewer.bat           double-click this on Windows (recommended)

HOW TO RUN (Windows)
  1. Extract this whole zip anywhere (keep the folder structure).
  2. Double-click Start-viewer.bat
     - it starts a tiny local web server and opens the viewer in your browser
     - requires Python (most systems have it; if not: python.org, or see below)

WHY THE .BAT?  Chrome blocks 3D textures when you open an .html file directly
(file:// security rule). Served from localhost, everything loads. Firefox will
usually work by double-clicking the .html directly if you prefer.

SWAPPING IN REAL PHOTO TEXTURES
  The textures/ folder ships with generated textures. To upgrade any surface,
  download a free texture (e.g. ambientcg.com or polyhaven.com), rename it to
  the matching filename below, and overwrite the file — then reload:
    floor.jpg     wood floor        stone.jpg    fireplace ledgestone
    wood.jpg      oak cabinetry     quartz.jpg   countertops
    wall.jpg      wall paint        tile.jpg     backsplash
    ceiling.jpg   vault planks      fabric.jpg   banquette cushions
    steel.jpg     appliances
  If a file is missing the viewer falls back to built-in materials and shows
  a small note in the bottom-right corner.

CONTROLS
  Drag to look - WASD/arrows to move - Shift runs - panel top-left for
  Option A/B, views (Walk / 3D top / 2D plan), island finish, plan-floor
  and X-ray overlays.

FINISHES
  Click "Finishes" in the top-left panel, then click anything in the room.
  Everything of that kind lights up, and picking a colour changes all of
  them at once - change one cabinet pull and every pull follows.
    Adjustable: cabinets, island, countertops, backsplash, walls,
    appliances, cabinet hardware, faucet, sink bowl, pendants, bench
    cushions, sofa, rug, stools & chairs, trim & doors, window frames,
    fireplace, deck & railing.
    Metal things (hardware, faucet, pendants, frames, appliances) get named
    finishes - Stainless, Chrome, Nickel, Pewter, Brass, Polished brass,
    Bronze, Matte black - which set the metal response, not just the hue.
    Appliances can also be painted (white/black/green/navy).
    Contrast details follow along instead of flattening: the dark reveals
    between fridge doors and the shaker rails on cabinet fronts take a
    derived shade of whatever you pick.
    Countertops have 5 styles (white quartz, veined marble, soapstone,
    butcher block, concrete); pendants have 4 shapes.
    Walls have an "All walls / Just this wall" toggle.
  "Copy link" puts the whole scheme in the URL - send it to someone or
  open it in the headset and it comes back exactly. "Reset all" undoes it.

IN VR (Meta Quest) - hands or controllers, either works
  Open https://jmartz.github.io/kitchen-viewer/ in the Quest Browser and tap
  the gold "Enter VR" button. NOT the localhost/LAN address - WebXR needs
  https, and the button won't appear on a plain http:// address.
  You start in the family room looking north into the kitchen.
    PINCH AND HOLD (right hand)     a ray grows, then the gold arc appears;
                                    let go to jump. Short pinch = tap.
    SHORT PINCH / CLICK             opens fridge, oven, range and pantry doors
    CONTROL PANEL, below eye line   poke it, or point at it and pinch:
                                      A/B  swap option
                                      PLAN  scanned sheet on the floor at 1:1
                                      EXIT VR  end the session
    Controllers also: left stick glides, right stick snap-turns 30 degrees,
    grip runs, A swaps, B changes island finish, X recenters, Y exits.
  You can also just walk - the play space is 1:1 and you can't walk through
  the island. See QUEST.md for the full setup checklist (charging, updates,
  turning hand tracking on, Guardian).
