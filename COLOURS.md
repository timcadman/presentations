# Presentation colours

Shared palette for the decks under `presentations/`. Two themes exist —
`theme/` (DataSHIELD/MOLGENIS, default) and `theme-uncan/` (UNCAN) — each
defining the same set of `--slidev-theme-*` CSS variables with different
values, so shared components (e.g. `DatashieldArchitectureArmadillo.vue`)
render correctly under either just by changing a deck's `theme:` frontmatter.
This file is the quick reference, including chart/component colours that
aren't theme variables.

## Core (theme — `theme/styles/index.css`)

| Role | Variable | Hex |
|---|---|---|
| Primary — blue | `--slidev-theme-primary` | `#4285F4` |
| Secondary — gold | `--slidev-theme-secondary` | `#E6B96A` |
| Accent — teal | `--slidev-theme-accent` | `#0097A7` |
| Section background — gold | `--slidev-theme-section-bg` | `#F7D38C` |
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
| Gold | `#E6B96A` | fills; pair with `#B9852A` for text |
| Dark gold | `#B9852A` | gold text on light backgrounds |
| Teal | `#0097A7` | = accent |
| Navy | `#1E3A5F` | deep anchor |
| Blue | `#4285F4` | = primary |
| Purple | `#6A4C93` | totals / sums |
| Red | `#D9534F` | alerts; `#B52B27` dark |
| Grey | `#9AA0A6` | muted, captions |

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
