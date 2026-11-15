# Slide style

Rules for cards, click emphasis and Slidev features, agreed 2026-11-13 from `style-examples/`. Colours come from `COLOURS.md`.

## Cards

- Flat tint at rest (`.tint-card`), solid fill when active. One palette colour per card, kept the same for that category across the deck.
- Set the colour per card: `--c` (fill), `--h` (heading on tint, if `--c` is too light), `--t` (text on solid). Gold uses `--h: #B9852A; --t: #333333`.

```html
<div class="tint-card" style="--c: #4285F4;" :class="$clicks === 1 ? 'active' : 'dimmed'">
  <h3>Title</h3><p>Detail</p>
</div>
```

## Click emphasis

- **Default:** tint to solid with the others dimmed (`.active` on the current card, `.dimmed` on the rest). Do not mix with plain dim or plain tint-to-solid in the same deck.
- **Expand the active card** (`.tint-row`): 3–4 items with short detail. The active card widens and shows its `<p>`.
- **List and detail panel** (`.tint-panel`): more items or longer detail. Pills on the left, the active pill's `.tint-detail` on the right.
- Use expand or panel only when each item has extra detail to reveal.
- Avoid grey-out, blur, ring, scale and moving frame.

```html
<div class="tint-row">
  <div class="tint-card" style="--c: #4285F4;" :class="{ active: $clicks === 1, dimmed: $clicks > 0 && $clicks !== 1 }"><h3>Title</h3><p>Detail</p></div>
  ...
</div>

<div class="tint-panel">
  <div class="tint-list">
    <div class="tint-card" style="--c: #4285F4;" :class="{ active: $clicks === 1, dimmed: $clicks > 0 && $clicks !== 1 }">Title</div>
    ...
  </div>
  <div>
    <div class="tint-detail" style="--c: #4285F4;" :class="{ active: $clicks === 1 }"><h3>Title</h3><p>Detail</p></div>
    ...
  </div>
</div>
```

## Slidev features

Use sparingly: at most once or twice per deck, on the slide's key claim, not as decoration.

- `v-mark` highlight
- MDC inline styling (`mdc: true`)
- Iconify icons (`carbon`, `ph`)
- Sticky note (`.sticky-note`)
- Comparison table with tick/cross icons

## Transitions

- Deck-wide `transition: slide-left`.
- A run of sibling slides (e.g. options 1–3 and their comparison table) uses `transition: slide-up` on every slide but the last, so the group reads as a vertical stack.

## PPTX export

- `.tint-card` and `.tint-detail` slides export as editable cards (title and first `<p>`).
- Card slides that also contain an `<svg>` export as a picture of the slide.
