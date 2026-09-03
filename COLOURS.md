# Presentation colours

Shared palette for the decks under `presentations/`. The theme variables live in
`theme/styles/index.css`; this file is the quick reference, including chart /
component colours that aren't theme variables.

## Core (theme)

| Role | Hex |
|---|---|
| Primary — blue | `#4285F4` |
| Accent — teal | `#0097A7` |
| Section background — gold | `#F7D38C` |
| Text | `#333333` |

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
