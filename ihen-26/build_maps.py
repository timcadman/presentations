"""Maps for the IHEN decks, drawn with the shared basemap from data/build_cohort_map.py.

Each map is saved straight into the public/ folder of the deck that uses it.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'data'))
from build_cohort_map import plt, draw_countries, CITY, RED, TEAL, GOLD  # noqa: E402

CITY = {**CITY, 'Sabadell': (2.1097, 41.5433), 'Bradford': (-1.7594, 53.7960)}
INTRO_PUBLIC = os.path.join(HERE, 'intro', 'public')
FEDERATED_PUBLIC = os.path.join(HERE, 'federated', 'public')



# Difference in pregnancy NO2 (ug/m3) for women in high- vs lower-SEP areas, by city.
# Robinson et al. (2018) Environ Health Perspect 126(7):077005, Table 3 (area-level SEP).
SES_NO2 = [
    ('Sabadell', 10.33),
    ('Kaunas', 1.26),
    ('Valencia', -8.94),
    ('Bradford', -1.96),
]


# IHEN map, one marker per cohort. Membership and coordinates come from
# data/datashield_nodes.csv (built by data/build_nodes.py) — the single source of
# truth; this file holds no cohort list of its own. A cohort in several projects is
# labelled ATHLETE first, then LongITools, then LifeCycle.
IHEN_PROJECTS = [('ATHLETE', RED), ('LongITools', TEAL), ('LifeCycle', GOLD)]
PROJECT_COLUMN = {'ATHLETE': 'Athlete', 'LongITools': 'Longitools', 'LifeCycle': 'LifeCycle'}


def ihen_nodes():
    """Exposome cohorts from the register, fanned out where several share a city.

    The fan is a small deterministic offset so co-located markers stay visible; it
    is not a real position. Markers are larger here than in build_cohort_map.py, so
    the fan is wider too.
    """
    import csv
    from collections import defaultdict

    rows = list(csv.DictReader(open(os.path.join(HERE, '..', 'data', 'datashield_nodes.csv'))))
    picked = []
    for r in rows:
        if r['status'] != 'live' or not r['lon']:
            continue
        project = next((p for p, _ in IHEN_PROJECTS if r[PROJECT_COLUMN[p]]), None)
        if project:
            picked.append([r['cohort'], float(r['lon']), float(r['lat']), project])

    at = defaultdict(list)
    for n in picked:
        at[(round(n[1], 3), round(n[2], 3))].append(n)
    for group in at.values():
        if len(group) == 1:
            continue
        step = 1.4
        for i, n in enumerate(group):
            n[1] += (i - (len(group) - 1) / 2) * step
    return [tuple(n) for n in picked]


IHEN_NODES = ihen_nodes()


def build_ses_no2_map():
    """Cities where high-SEP areas have higher (red, up) or lower (teal, down) NO2.

    Saved as three registered layers — basemap, then one per marker group — so the
    slide can reveal the groups on click by stacking them. The key lives on the
    slide, not in the figure, so it keeps the deck's type. Every layer uses the same
    figure size and axis limits and is saved without a tight bbox, which is what
    keeps them aligned; a tight bbox would crop each layer to its own content.
    """
    # Window cropped to the four cities (Iberia to the Baltic) so the map is
    # landscape and fills the width of the slide's figure column.
    LON, LAT = (-11, 32), (36, 58)
    LABEL = {'Kaunas': (-9, 0), 'Sabadell': (9, 26), 'Valencia': (9, -26)}
    FIGSIZE = (6, 4.75)

    def frame(ax):
        ax.set_xlim(*LON)
        ax.set_ylim(*LAT)
        ax.set_aspect(1.55)
        ax.axis('off')

    def layer(name, cities, basemap):
        fig, ax = plt.subplots(figsize=FIGSIZE, dpi=200)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        if basemap:
            fig.patch.set_facecolor('white')
            draw_countries(ax)
        else:
            fig.patch.set_alpha(0)
        frame(ax)

        for city, diff in cities:
            lon, lat = CITY[city]
            colour, marker = (RED, '^') if diff > 0 else (TEAL, 'v')
            ax.scatter([lon], [lat], s=700, marker=marker, facecolor=colour,
                       edgecolor='white', linewidth=1.8, zorder=4)
            # Hand-placed: at this size the labels collide or run off the edge
            # otherwise — Kaunas reads inwards, Sabadell and Valencia split apart.
            dx, dy = LABEL.get(city, (9, 0))
            ax.annotate(f'{city}\n{diff:+.1f} µg/m³', (lon, lat), xytext=(dx, dy),
                        textcoords='offset points', ha='right' if dx < 0 else 'left',
                        va='center', fontsize=16, color='#333333', zorder=5)

        out = os.path.join(INTRO_PUBLIC, name)
        fig.savefig(out, dpi=200, transparent=not basemap)
        plt.close(fig)
        print('saved', out)

    higher = [(c, d) for c, d in SES_NO2 if d > 0]
    lower = [(c, d) for c, d in SES_NO2 if d < 0]
    layer('ihen_ses_no2_map_base.png', [], basemap=True)
    layer('ihen_ses_no2_map_higher.png', higher, basemap=False)
    layer('ihen_ses_no2_map_lower.png', lower, basemap=False)


def build_federated_basemap():
    """Plain basemaps for the federated-query figure (FederatedQuery.vue).

    Nodes, the researcher and the arcs are drawn in the slide so they can appear on
    click; this is only the land underneath, lightened so the arcs read over it.
    The windows must stay in step with WINDOWS in components/map-windows.js.
    """
    for name, lon, lat, figsize in (
        # figsize must match the window's own ratio, or matplotlib letterboxes the
        # axes and every percentage position in the component is wrong
        ('world-base.png', (-112, 95), (-38, 72), (10.35, 5.5)),
        ('europe-base.png', (-11, 32), (36, 58), (6, 4.75)),
    ):
        fig, ax = plt.subplots(figsize=figsize, dpi=200)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        fig.patch.set_facecolor('white')
        draw_countries(ax)
        for patch in ax.patches:
            patch.set_facecolor('#E4E4E4')
        ax.set_xlim(*lon)
        ax.set_ylim(*lat)
        ax.set_aspect(1.0 if name.startswith('world') else 1.55)
        ax.axis('off')
        out = os.path.join(FEDERATED_PUBLIC, name)
        fig.savefig(out, dpi=200)
        plt.close(fig)
        print('saved', out)


def build_ihen_nodes_map():
    """LifeCycle, ATHLETE and LongITools cohorts, one marker each, coloured by project."""
    fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    draw_countries(ax)

    colour_of = dict(IHEN_PROJECTS)
    for label, lon, lat, project in IHEN_NODES:
        ax.scatter([lon], [lat], s=140, facecolor=colour_of[project], edgecolor='white',
                   linewidth=0.8, zorder=3)

    counts = {p: sum(1 for *_, q in IHEN_NODES if q == p) for p, _ in IHEN_PROJECTS}
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c,
                           markeredgecolor='white', markersize=9, label=f'{p} ({counts[p]})')
               for p, c in IHEN_PROJECTS]
    leg = ax.legend(handles=handles, loc='upper left', frameon=True, fontsize=11,
                     title='Cohorts by project', title_fontsize=12,
                     bbox_to_anchor=(0.01, 0.99), borderaxespad=0.5)
    leg.get_frame().set_edgecolor('#b4b4b4')
    leg.get_frame().set_facecolor('white')
    leg._legend_box.align = 'left'

    out = os.path.join(FEDERATED_PUBLIC, 'ihen_nodes_map.png')
    fig.savefig(out, bbox_inches='tight', pad_inches=0.05, dpi=150)
    plt.close(fig)
    print('saved', out)




if __name__ == '__main__':
    build_ses_no2_map()
    build_federated_basemap()
    build_ihen_nodes_map()
