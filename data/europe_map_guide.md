# Building cohort maps of Europe

How `images/stage_europe_map_all_cohorts.png` is built, and how to rebuild/extend it for a
different set of cohorts. Reusable script: `data/build_cohort_map.py`. Boundary data:
`data/ne_50m_admin_0_countries.geojson`.

## Use real vector map data — don't hand-calibrate a flat image

Earlier attempts to plot cohorts on a flat basemap PNG (`images/blank_europe_map.png`, a
Wikimedia Commons SVG render) needed a hand-fitted lon/lat → pixel transform, calibrated by
manually reading pixel coordinates off a handful of cities via a grid overlay. That approach kept
producing markers that landed in the sea for anything far from the calibration points (Athens,
Barcelona, Valencia) — the source image's projection wasn't the simple affine the fit assumed, and
every new point needed either a new calibration point nearby or blind trust in extrapolation.

The fix: don't use a flat image at all. Use **real country-boundary vector data** and plot
everything — coastlines and cohort markers alike — in the same true (longitude, latitude)
coordinate space with `matplotlib`. A point at a given lon/lat is *by construction* in the right
place; there's no separate "map image" and "pixel calibration" to keep in sync.

```python
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

geo = json.load(open('data/ne_50m_admin_0_countries.geojson'))
fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
for feat in geo['features']:
    geom = feat['geometry']
    if geom is None:
        continue
    polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
    for poly in polys:
        ax.add_patch(Polygon(poly[0], closed=True, facecolor='#c9c9c9', edgecolor='white', linewidth=0.6))

ax.scatter([lon], [lat], s=55, facecolor='#4285F4', edgecolor='white', linewidth=0.8, zorder=3)
ax.set_xlim(-12, 32); ax.set_ylim(34, 71)
ax.set_aspect(1.55)  # rough mid-latitude correction so shapes don't look squashed
ax.axis('off')
```

Only the exterior ring of each polygon is drawn (`poly[0]`) — holes (lakes etc.) are ignored,
which is fine at this scale/zoom.

### Getting boundary data

`data/ne_50m_admin_0_countries.geojson` is Natural Earth's 1:50m admin-0 country boundaries
(public domain), fetched via:

```
curl -sL -o data/ne_50m_admin_0_countries.geojson \
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson
```

`pip install cartopy`/`geopandas` failed in this sandbox (pip's SSL context doesn't trust the
sandbox's filtering proxy — `curl` worked fine because it uses the system trust store). If you hit
the same thing, either fetch data directly via `curl`/`WebFetch` as above and parse the (Geo)JSON
yourself with matplotlib, or ask the user to `pip install` in their own unsandboxed terminal
(`!` prefix) if you actually need a package like geopandas/cartopy rather than just the data.

### Marker size: use `scatter`, not `Circle` patches

`ax.set_aspect(1.55)` (or any non-1 aspect ratio) distorts `matplotlib.patches.Circle`, because its
radius is in *data units* (degrees) — circles come out as ellipses. `ax.scatter(..., s=...)` sizes
markers in points², independent of the axes aspect ratio, so they stay circular. Use `scatter` for
every marker.

## Geocoding cities

Real-world (lon, lat) for each institution's city — ordinary general knowledge / a quick lookup,
not something that needs verifying pixel-by-pixel like the old flat-image approach did. See the
`CITY` dict in `build_cohort_map.py`; extend it for new cities rather than re-deriving anything.

## Multiple cohorts per city

`build_cohort_map.py` has a small deterministic spiral-jitter helper (`next_offset`) that nudges
the 2nd, 3rd, ... marker at the same city outward by a fraction of a degree, so co-located cohorts
(e.g. NFBC1966 and NFBC1986, both Oulu) don't draw exactly on top of each other.

## Colour groups and legend

One colour per project/consortium (STAGE, LifeCycle, NCC, NDTD, Athlete, IPEC, plus a grey
"Other" bucket for anything not in a named group). STAGE markers carry a number; the rest are
colour-only once the cohort count gets large — a legend entry per marker stops being legible well
before 50+ markers, so per-cohort names live in the accompanying data file/table, not on the map.

Where a cohort belongs to multiple projects in the source data, pick one *primary* project per
marker rather than trying to render multi-membership (e.g. a pie-slice marker) — ask for a
priority order if it's not obvious, since it decides which colour a shared cohort gets.

Non-Europe locations (e.g. RAINE in Perth, Australia) don't fit this map's extent — note them as
text rather than trying to force a marker onto a Europe-only plot.

## Data provenance

Keep raw source data (spreadsheet as CSV, web-page fetches) in `data/`, separate from the
rendered map in `images/` — makes it possible to re-derive the map (different colour scheme,
different subset of cohorts) without re-collecting the underlying facts. See
`data/cohorts_extra.csv` for the format used for the LifeCycle spreadsheet import.
