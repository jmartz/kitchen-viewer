# Running the walkthrough on the Quest

## The one-line version

Put the headset on, open the **Browser**, go to:

    https://jmartz.github.io/kitchen-viewer/

Tap **Enter VR** (gold button, bottom of the screen). You start in the family room,
standing at your real height, looking north into the kitchen.

Works with **bare hands or controllers** — you don't need to pick anything up.

---

## Moving around

**Pinch** (thumb to index finger) and a gold arc appears. Aim it, **let go**, and you
teleport to the ring. Red arc means you can't stand there. With controllers it's the
same gesture on the **trigger**.

That's the whole locomotion system. You can also just walk — the play space maps 1:1
to the room, and you can't walk through the island.

## The wrist panel

A small panel rides above your **left wrist** (or floats at your lower left if only one
hand is tracked). It shows which option is live, and has three buttons you press by
**pushing your right index finger into them**:

| Button | Does |
|---|---|
| **A / B** | swap Option A ⇄ Option B — the whole point; stand in one spot and flip |
| **PLAN** | drops the scanned S2.2 sheet on the floor at 1:1 underfoot |
| **FINISH** | opens the finish picker — see below |
| **EXIT VR** | ends the session and drops you back to the browser |

## Changing finishes in VR

Poke **FINISH**, then point at anything in the room and **pinch**. Every surface
of that kind lights up so you can see what's about to change, and the panel fills
with swatches — poke one and they all change together. Change one cabinet pull and
every pull in the kitchen follows.

Countertops and pendants also get a **style** row (white quartz / veined marble /
soapstone / butcher block / concrete, and four pendant shapes). Walls get an
**ALL WALLS / THIS WALL** toggle so you can do a single accent wall.

**BACK** returns to the main page, **RESET** puts everything back to default.

While the finish picker is open, pinching points and selects instead of
teleporting — poke BACK when you want to walk again.

Every choice is stored in the page URL, so a scheme picked at the laptop opens in
the headset (and vice versa) if you use the same link.

## Getting out

Three ways, any of them works:

1. **EXIT VR** on the wrist panel.
2. The **Meta/Oculus button** on the right controller (or the palm-pinch menu gesture
   with hands) → close the browser window.
3. **Y** on the left controller.

Just taking the headset off also suspends it; the session ends when you put it down.

## Controllers, if you'd rather

Everything above still works, plus:

| Input | Does |
|---|---|
| **Trigger** | aim the teleport arc, release to go |
| **Left thumbstick** | glide, in the direction you're looking |
| **Right thumbstick** ←/→ | 30° snap turn (snap, not smooth — much easier on the stomach) |
| **Grip** (hold) | move at double speed |
| **A** / **B** (right) | swap option / oak ⇄ navy island |
| **X** / **Y** (left) | recenter to the start / exit VR |

## Why that URL and not the laptop

WebXR only runs in a **secure context** — `https://` or `localhost`. The Quest is not
the laptop, so `http://192.168.10.50:8437` is not localhost to it, and the Quest
Browser will not even define `navigator.xr` there. The **Enter VR button will not
appear** on a plain LAN address. `Start-viewer.bat` is still the right way to work on
the laptop; it just can't drive the headset.

If the page says *"VR needs an https:// address"* instead of *"Enter VR"*, that is
exactly this problem.

## Making it one tap (do this once)

In the Quest Browser, with the page open:

1. Open the **⋮** menu on the browser window.
2. Choose **Install** (some versions say *Add to Home / Install app*).
3. It appears in your app library as **Kitchen VR** with its own icon.

If **Install** isn't offered on your browser version, just **bookmark** it — the
bookmark row is the first thing on a new tab, so it's still one tap.

## First-time headset checklist

If the Quest has been in a drawer for a while, budget **an hour** before the demo:

1. **Charge it first.** A flat Quest 2 needs 20–30 min on the cable before it will even
   power on. Leaving it plugged into the laptop works; a wall charger is faster.
2. **Turn on hand tracking** if you want to go controller-free:
   Settings ▸ Movement tracking ▸ **Hand tracking**. (Fresh AA batteries in both
   controllers if you don't.)
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

## If something's wrong

- **No Enter VR button** → not on `https://`, or the Browser app is out of date.
- **Can't see your hands** → hand tracking is off in Settings, or your hands are
  outside the headset cameras' view. The app draws the joints itself; if the joints
  don't show, the headset isn't reporting them.
- **Pinch does nothing** → you're probably too close to the wrist panel; the panel
  swallows the pinch so you don't teleport while using the menu. Step your hand away
  and pinch again.
- **Still nothing** → try `immersiveweb.dev`. If that can't enter VR either, it's the
  headset, not this page.

## Performance notes

On entering VR the page drops the sun shadow map to 1024² and turns on fixed foveated
rendering. If it still feels choppy on a Quest 2, the next things to cut, in order:
shadows off entirely, then the IBL environment.
