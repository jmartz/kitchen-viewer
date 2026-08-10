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
