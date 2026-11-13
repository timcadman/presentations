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


# IHEN map, one marker per cohort. LifeCycle: participating cohorts on the LifeCycle map
# (stage-webinar/public/lifecycle_map_original.png). ATHLETE and LongITools: data/cohorts_extra.csv,
# plus ABCD, HGS, NFBC1966 and NFBC1986 in ATHLETE; LongITools-only entries there are not nodes.
# A cohort in several projects is labelled ATHLETE first, then LongITools, then LifeCycle.
# Nudges are wider than in build_cohort_map.py so co-located markers stay visible.
IHEN_PROJECTS = [('ATHLETE', RED), ('LongITools', TEAL), ('LifeCycle', GOLD)]
IHEN_NODES = [
    ('ALSPAC', -2.5879, 51.4545, 'ATHLETE'),                   # true Bristol
    ('Born in Bradford', -1.7594, 53.7960, 'ATHLETE'),         # true Bradford
    ('DNBC', 12.5683, 55.6761, 'ATHLETE'),                     # true Copenhagen
    ('EDEN', 2.3522, 48.8566, 'ATHLETE'),                      # true Paris
    ('Generation R', 4.4777, 51.9244, 'ATHLETE'),              # true Rotterdam
    ('Generation R Next', 4.4777, 51.4744, 'ATHLETE'),         # fake — nudged off Rotterdam
    ('INMA', -0.3763, 39.4699, 'ATHLETE'),                     # true Valencia
    ('MoBa', 10.7522, 59.9139, 'ATHLETE'),                     # true Oslo
    ('NINFEA', 7.6869, 45.0703, 'ATHLETE'),                    # true Turin
    ('RHEA', 25.1442, 35.3387, 'ATHLETE'),                     # true Heraklion
    ('PELAGIE', -1.6778, 48.1173, 'ATHLETE'),                  # true Rennes
    ('Piccolipiu', 9.1900, 45.4642, 'ATHLETE'),                # true Milan
    ('BISC', 2.1686, 41.3874, 'ATHLETE'),                      # true Barcelona
    ('HELIX', 2.8686, 41.3874, 'ATHLETE'),                     # fake — nudged off Barcelona
    ('EnvironAGE', 5.3378, 50.9307, 'ATHLETE'),                # true Hasselt
    ('KANC', 23.9036, 54.8985, 'ATHLETE'),                     # true Kaunas
    ('CELSPAC-TNG (Recetox)', 16.6068, 49.1951, 'ATHLETE'),    # true Brno
    ('SEPAGES', 5.7245, 45.1885, 'ATHLETE'),                   # true Grenoble
    ('ABCD', 4.9041, 52.3676, 'ATHLETE'),                      # true Amsterdam
    ('HGS', 23.7275, 37.9838, 'ATHLETE'),                      # true Athens

    ('ELFE', 1.6522, 48.8566, 'LongITools'),                   # fake — nudged off Paris
    ('NFBC1966', 24.7651, 65.0121, 'ATHLETE'),                 # fake — nudged off Oulu
    ('NFBC1986', 26.1651, 65.0121, 'ATHLETE'),                 # fake — nudged off Oulu

    ('SWS', -1.4044, 50.9097, 'LifeCycle'),                    # true Southampton
    ('GECKO', 6.5665, 53.2194, 'LifeCycle'),                   # true Groningen
    ('HBCS', 24.9384, 60.1699, 'LifeCycle'),                   # true Helsinki
    ('CHOP-Germany', 11.5820, 48.1351, 'LifeCycle'),           # true Munich
    ('CHOP-Belgium', 4.3517, 50.8503, 'LifeCycle'),            # true Brussels
    ('CHOP-Italy', 9.8900, 45.4642, 'LifeCycle'),              # fake — nudged off Milan
    ('CHOP-Poland', 21.0122, 52.2297, 'LifeCycle'),            # true Warsaw
    ('CHOP-Spain', 1.1069, 41.1561, 'LifeCycle'),              # true Reus
]


def build_ses_no2_map():
    """Cities where high-SEP areas have higher (red, up) or lower (teal, down) NO2."""
    fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    draw_countries(ax)

    for city, diff in SES_NO2:
        lon, lat = CITY[city]
        colour, marker = (RED, '^') if diff > 0 else (TEAL, 'v')
        ax.scatter([lon], [lat], s=320, marker=marker, facecolor=colour, edgecolor='white',
                   linewidth=1.2, zorder=4)
        ax.annotate(f'{city}\n{diff:+.1f} µg/m³', (lon, lat), xytext=(12, 0),
                    textcoords='offset points', ha='left', va='center', fontsize=14,
                    color='#333333', zorder=5)

    handles = [plt.Line2D([0], [0], marker=m, color='w', markerfacecolor=c,
                           markeredgecolor='white', markersize=12, label=n)
               for n, c, m in [('Higher NO₂', RED, '^'), ('Lower NO₂', TEAL, 'v')]]
    leg = ax.legend(handles=handles, loc='upper left', frameon=True, fontsize=12,
                     title='High-SEP areas have', title_fontsize=13,
                     bbox_to_anchor=(0.01, 0.99), borderaxespad=0.5)
    leg.get_frame().set_edgecolor('#b4b4b4')
    leg.get_frame().set_facecolor('white')
    leg._legend_box.align = 'left'

    out = os.path.join(INTRO_PUBLIC, 'ihen_ses_no2_map.png')
    fig.savefig(out, bbox_inches='tight', pad_inches=0.05, dpi=150)
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
    build_ihen_nodes_map()
