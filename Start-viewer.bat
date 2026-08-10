@echo off
cd /d "%~dp0"
echo Starting local viewer at http://localhost:8437/kitchen-walkthrough.html
start "" http://localhost:8437/kitchen-walkthrough.html
python -m http.server 8437 2>nul || py -m http.server 8437
