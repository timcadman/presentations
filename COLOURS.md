# Presentation colours

Shared palette for the decks under `presentations/`. Two themes exist —
`theme/` (DataSHIELD/MOLGENIS, default) and `theme-uncan/` (UNCAN) — each
defining the same set of `--slidev-theme-*` CSS variables with different
values, so shared components (e.g. `DatashieldArchitecture.vue`)
render correctly under either just by changing a deck's `theme:` frontmatter.
This file is the quick reference, including chart/component colours that
aren't theme variables.

## Core (theme — `theme/styles/index.css`)

| Role | Variable | Hex |
|---|---|---|
| Primary — blue | `--slidev-theme-primary` | `#4285F4` |
| Secondary — gold | `--slidev-theme-secondary` | `#E2A517` |
| Accent — teal | `--slidev-theme-accent` | `#119DA1` |
| Section background — gold tint | `--slidev-theme-section-bg` | `#F9D28C` |
| Section foreground | `--slidev-theme-section-fg` | = primary |
| Text | `--slidev-theme-text` | `#333333` |

## UNCAN theme (`theme-uncan/styles/index.css`)

Sourced from two places, reconciled — UNCAN Connect's official PowerPoint
brand template (`PresentationTemplate_UNCAN-Connect.pptx`, its
`ppt/theme/theme1.xml` colour scheme — authoritative) and the live UNCAN
Connect catalogue's own CSS custom properties (`--uncan-*`, at
uncan-catalogue.molgeniscloud.org — used to independently confirm the
brand-template values and to fill in what the template didn't cover, e.g.
the section-divider dark surface). Not invented ad hoc.

### Theme variables in use

| Role | Variable | Hex | Source |
|---|---|---|---|
| Primary — purple | `--slidev-theme-primary` | `#7A39C4` | website `--uncan-bg`; confirmed by pptx `hlink` `#7939C3` |
| Secondary — amber | `--slidev-theme-secondary` | `#FFAB00` | website `--uncan-accent`; confirmed by pptx `accent6` `#FFB841` |
| Accent — muted purple | `--slidev-theme-accent` | `#6C5084` | pptx `accent3` (distinct 3rd colour, e.g. diagram flows that must differ from both primary and secondary) |
| Section background — deep purple | `--slidev-theme-section-bg` | `#39185E` | pptx `dk1`/`accent1` |
| Section foreground | `--slidev-theme-section-fg` | `#FFFFFF` | pptx `lt1` role, applied as text-on-dark |
| Text | `--slidev-theme-text` | `#333333` | unchanged from DataSHIELD theme default |

Logos: `uncan-connect-logo.png` (colour, light backgrounds) and
`uncan-white.png` (white, for the deep-purple section background) —
configured via `themeConfig.logo` / `themeConfig.logoOnDark` in
`theme-uncan/package.json`, copied into each consuming deck's own `public/`.

### Full UNCAN palette (reference — not all wired to theme variables yet)

From the official PowerPoint theme:

| Role | Hex |
|---|---|
| dk1 — text/dark | `#39185E` |
| lt1 / lt2 — background | `#FEFEFE` |
| dk2 | `#000000` |
| accent1 — brand purple | `#39185D` |
| accent2 — light lavender | `#F3ECFF` |
| accent3 — muted purple | `#6C5084` |
| accent4 — soft grey-purple | `#9F8EAE` |
| accent5 — light amber | `#FFC56B` |
| accent6 — amber/gold | `#FFB841` |
| hlink — bright interactive purple | `#7939C3` |
| folHlink — light lavender | `#E5D4F2` |

From the live website's own CSS custom properties (`--uncan-*`):

| Token | Hex |
|---|---|
| `--uncan-bg` | `#7A39C4` |
| `--uncan-bg-deep` | `#2D1B4E` |
| `--uncan-bg-alt` | `#AC3CB4` |
| `--uncan-bg-alt-deep` | `#7A2A80` |
| `--uncan-bg-alt-soft` | `#F7E8F8` |
| `--uncan-fg` | `#FFFFFF` |
| `--uncan-fg-alt` | `#1A1128` |
| `--uncan-accent` | `#FFAB00` |
| `--uncan-accent-soft` | `#FFF4CB` |
| `--uncan-muted` | `#FFFFFFCC` |
| `--uncan-neutral` | `#6D6D6D` |
| `--uncan-neutral-soft` | `#F4F4F4` |

## Extended (charts, components)

| Name | Hex | Use |
|---|---|---|
| Gold | `#E2A517` | fills; pair with `#BA8118` for text on light backgrounds |
| Dark gold | `#BA8118` | gold text, and gold fills that must carry white text |
| Teal | `#119DA1` | = accent |
| Blue-dark | `#02529B` | deep anchor (was navy `#1E3A5F`) |
| Blue | `#4285F4` | = primary |
| Purple | `#5D408A` | totals / sums |
| Red | `#DA594A` | alerts |
| Grey | `#9AA0A6` | muted, captions |
| DataSHIELD orange | `#E35000` | DataSHIELD / Rock; sampled from the DataSHIELD logo |
| Opal orange | `#D3621F` | Opal (OBiBa) cards, e.g. Armadillo vs Opal; from the existing "Deploying DataSHIELD" slide |
| Flower yellow | `#FDAE00` | Flower outlines; sampled from Flower's own diagrams. Pair with `#B9852A` for text |
| Flower yellow tint | `#FFEFCC` | Flower fills; sampled from Flower's own diagrams |

## Chart series — validated options (not yet applied)

The Extended list above predates any accessibility check and fails four of
five when run as a categorical series palette through the `dataviz` skill's
`scripts/validate_palette.js`: gold `#E6B96A` sits outside the lightness band
and under 3:1 contrast, navy `#1E3A5F` and grey `#9AA0A6` fall below the
chroma floor (they read as grey rather than as hues), and grey ↔ dark gold
`#B9852A` are ΔE 14.1 apart in normal vision — below the floor of 15. Blue ↔
teal, the deck's most-used pairing, is ΔE 14.2 and fails the same check.

Three replacements below, each anchored on MOLGENIS blue and each passing
lightness, chroma, colour-blind separation and normal-vision separation.
Re-check any change with:

```
node scripts/validate_palette.js "<hex,hex,...>" --mode light
```

A contrast WARN on the lighter slots is expected and acceptable here: it
obliges a visible label or legend, which every figure in these decks has.

### Option A — Okabe–Ito with MOLGENIS blue (recommended)

The Color Universal Design set, used by Nature Methods and Claus Wilke's
*Fundamentals of Data Visualization*, with blue substituted into slot 1.
Worst colour-blind pair ΔE 7.6 (needs its label, which figures have); normal
vision ΔE 21.1 — the widest margin of the three.

| Slot | Hex | Name |
|---|---|---|
| 1 | `#4285F4` | MOLGENIS blue |
| 2 | `#D55E00` | Vermillion |
| 3 | `#009E73` | Bluish green |
| 4 | `#CC79A7` | Reddish purple |
| 5 | `#E69F00` | Orange |
| 6 | `#56B4E9` | Sky blue |
| 7 (only if needed) | `#0072B2` | Deep blue |

### Option B — generated, evenly spaced, vivid

Hues stepped 65° around the wheel from blue in OKLCH, lightness varied to
keep each slot inside the band. Full PASS on every check including colour-blind
separation (worst ΔE 8.6).

| Slot | Hex | Name |
|---|---|---|
| 1 | `#4285F4` | MOLGENIS blue |
| 2 | `#AC5DB1` | Orchid |
| 3 | `#C35141` | Brick |
| 4 | `#AB9017` | Ochre |
| 5 | `#24BA7D` | Emerald |
| 6 | `#089AC3` | Cyan |

### Option C — generated, muted/editorial

The same construction at lower chroma (0.13) and 68° steps — quieter on a
white slide, closer in feel to the current deck. Full PASS, worst
colour-blind pair ΔE 8.2.

| Slot | Hex | Name |
|---|---|---|
| 1 | `#4285F4` | MOLGENIS blue |
| 2 | `#C07BC4` | Soft orchid |
| 3 | `#B45245` | Terracotta |
| 4 | `#B89D2B` | Olive gold |
| 5 | `#06915F` | Pine |
| 6 | `#1AA1C9` | Teal blue |

Theme variables are unaffected: `--slidev-theme-primary`,
`--slidev-theme-secondary` and `--slidev-theme-section-bg` keep their current
values. Gold is a background there, not a data series, and passes as such.

## Decomposition semantics (armadillo-opal-comparison)

Used consistently in the "Where does the time go?" bar, the Sampling-strategy
maths, and the LatencyStack:

| Component | Hex |
|---|---|
| Round-trip (total) | `#6A4C93` |
| Server compute | `#E6B96A` (text `#B9852A`) |
| System overhead | `#0097A7` |
| Network | `#1E3A5F` |

## Ordinal-level semantics (low/medium/high — stage-webinar)

For any 3-level ordinal scale (e.g. exposure level, risk, severity), reuse
this low→high progression rather than introducing new hues:

| Level | Hex | Name |
|---|---|---|
| Low | `#0097A7` | Teal |
| Medium | `#E6B96A` | Gold |
| High | `#D9534F` | Red |

Used for the fitted exposure/cognitive-decline trajectory curves in
`stage-webinar`.
