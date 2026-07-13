# SoleStepper

A mobile-friendly React app that connects to a Bluetooth smart scale and tracks
your weight change across a workout, then gives you a rehydration target.

## Features

- **Connect Sensor** — pairs with a nearby BLE scale via the Web Bluetooth API
  using the standard GATT **Weight Scale Service (`0x181D`)** and
  **Weight Measurement characteristic (`0x2A9D`)**. Readings are parsed per the
  GATT spec (SI 0.005 kg / imperial 0.01 lb resolution) and captured once two
  consecutive indications agree within 50 g.
- **kg / lb toggle** for all displayed weights and fluid targets.
- **Two-step flow** — log pre-workout and post-workout weight; each reading is
  timestamped.
- **Session result** — absolute and percentage weight change, a plain-language
  explanation that within-session weight loss is fluid (sweat), not fat, and a
  rehydration target of ~1.25–1.5 L per kg lost (~16–24 oz per lb lost).
- **>2% caution** — if fluid loss exceeds 2% of body weight, the app suggests
  electrolyte replacement rather than plain water alone.
- **Session history** — kept in memory only (clears on reload, by design).
- **Manual entry fallback** — shown automatically where Web Bluetooth is
  unavailable (Safari/iOS), and always available as an option.

## Running

```bash
npm install
npm run dev      # local dev server
npm run build    # production build in dist/
```

## Browser support notes

Web Bluetooth requires a secure context (HTTPS or `localhost`) and is
available in Chrome/Edge on desktop and Android. Safari and iOS browsers do
not support it — the app detects this and falls back to manual weight entry.

## Disclaimer

SoleStepper offers general hydration guidance only. It is not a medical device
and does not provide medical advice. People with medical conditions (e.g.
kidney or heart issues) should consult a doctor before following fluid-intake
targets.
