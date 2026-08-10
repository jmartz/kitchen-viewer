# Running the walkthrough on the Quest

## The one-line version

Put the headset on, open the **Browser**, go to:

    https://jmartz.github.io/kitchen-viewer/

Tap **Enter VR** (gold button, bottom of the screen). You're standing in the kitchen
at your real height.

---

## Why that URL and not the laptop

WebXR only runs in a **secure context** — `https://` or `localhost`. The Quest is not
the laptop, so `http://192.168.10.50:8437` is not localhost to it, and Chrome/the Quest
Browser will not even define `navigator.xr` there. The **Enter VR button will not
appear** on a plain LAN address. `Start-viewer.bat` is still the right way to work on
the laptop; it just can't drive the headset.

GitHub Pages gives us https for free, so that's the delivery path. If the page ever
says *"VR needs an https:// address"* instead of *"Enter VR"*, that is exactly this
problem.

## Making it one tap (do this once)

In the Quest Browser, with the page open:

1. Open the **⋮** menu on the browser window.
2. Choose **Install** (some versions say *Add to Home / Install app*).
3. It appears in your app library as **Kitchen VR** with its own icon.

After that it launches from the library like a native app, fullscreen, no address
bar. If **Install** isn't offered on your browser version, just **bookmark** it — the
bookmark row is the first thing on a new tab, so it's still one tap.

## Controls in VR

| Input | Does |
|---|---|
| **Left thumbstick** | glide, in the direction you're looking |
| **Right thumbstick** ←/→ | 30° snap turn (snap, not smooth — much easier on the stomach) |
| **Either trigger** (hold) | move at double speed |
| **A** (right) | swap **Option A ⇄ Option B** — the whole point; stand in one spot and flip |
| **B** (right) | oak ⇄ navy island |
| **X** (left) | recenter to the start position |
| **Y** (left) | plan-floor overlay — drops the scanned S2.2 sheet on the ground at 1:1 |

A small legend card rides on the **left controller** showing which option is live, so
whoever is wearing the headset doesn't have to remember any of this.

You can also physically walk — the play space maps 1:1 to the room, and you can't walk
through cabinets.

## First-time headset checklist

If the Quest has been in a drawer for a while, budget **an hour** before the demo:

1. **Charge it first.** A flat Quest 2 needs 20–30 min on the cable before it will even
   power on. Leaving it plugged into the laptop works; a wall charger is faster.
2. **Fresh AA batteries in both controllers.** This is the one that ruins demos.
3. Power on → join Wi-Fi → **Settings ▸ System ▸ Software Update**. A long-dormant
   headset may pull several updates back-to-back with a reboot between each.
4. **Update the Browser app too** — Library ▸ (filter) Updates. WebXR support lives in
   the browser, not the OS, so an old browser is the likeliest cause of a missing
   Enter VR button.
5. Redraw the **Guardian / boundary** for wherever you're standing. Give yourself at
   least a 6' × 6' square if you want to walk around the island.
6. If it asks you to sign in and the old login doesn't work: Facebook logins were
   retired, so the headset may want a **Meta account**. Do that on the phone app
   first — it's much less painful than typing in the headset.

## If Enter VR doesn't show up

- Not on `https://`? → see above.
- Browser out of date? → Library ▸ Updates.
- Page loaded before the headset finished booting → reload.
- Still nothing: open `chrome://gpu` equivalent isn't available, so just try the
  official test page `immersiveweb.dev` — if that can't enter VR either, it's the
  headset, not this page.

## Performance notes

On entering VR the page automatically drops the sun shadow map to 1024² and turns on
fixed foveated rendering (level 0.7). If it still feels choppy on a Quest 2, the next
things to cut, in order: shadows off entirely, then the IBL environment.
