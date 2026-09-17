# UNCAN demo — voiceover pipeline

Narration is text, not audio. Edit YAML, re-run scripts — never hand-edit a rendered video.

## Structure

- `narration/segments/*.yml` — one narration script per topic. Each `step` has `clicks` (which slide/state it covers), `text` (spoken), and optional `pauseAfterMs` / `voiceSettings` / `clausePausesMs` overrides.
- `decks/*.yml` — a deck lists which `segments` play in order, plus `slides` (the Slidev `.md`) for `captureType: slidev` decks.
- `decks/full-demo.yml` — lists which per-deck `recordings/<part>/final.mp4` get concatenated into the final video, in order. A part can carry `pauseBeforeMs` to insert a held-frame gap before it.
- `narration/audio/manifest.json` — cache of generated clips, keyed by `segment:clicks`. Never edit by hand.

## Two capture types

- `captureType: slidev` — fully automated. Script drives a headless browser through the deck, timed to the generated audio.
- `captureType: manual` — you record yourself clicking through a real app while listening to a cue sheet; the script syncs narration on top afterwards.

## Scripts (run from `uncan-demo/`)

```
node --env-file=.env scripts/tts.mjs decks/<deck>.yml [--dry-run]   # generate/cache narration audio
node scripts/record.mjs decks/<deck>.yml                            # slidev decks: auto-record video
node scripts/narrate.mjs decks/<deck>.yml                           # manual decks: build narration.wav + cue-sheet.txt
node scripts/stitch.mjs decks/<deck>.yml <video>                    # mux narration onto video → recordings/<deck>/final.mp4
node scripts/assemble.mjs [decks/full-demo.yml]                     # concatenate all parts → recordings/full-demo/final.mp4
```

`tts.mjs` caches by a hash of the exact clause text (+ any voice settings) — editing `text` is what triggers regeneration, nothing else does. Chromium and the `.env` API key both need to run outside the sandbox, via `!`.

## Workflow for a change

1. Edit the segment YAML.
2. `tts.mjs --dry-run` to see what will regenerate, then run for real.
3. `record.mjs` (slidev) or re-run `stitch.mjs` on existing footage (manual, if only timing changed).
4. `stitch.mjs` to produce that deck's `final.mp4`.
5. `assemble.mjs` to fold it into the full demo.

**Efficiency note: get the dialogue right first, for every segment, before doing any stitching or assembling.** Wording/pacing changes are cheap in isolation but expensive to chase once they're baked into stitched, padded, reassembled video — every re-listen after that point means re-running steps 3–5 again. Finalize all narration text, then do one pass of record → stitch → assemble at the end.
