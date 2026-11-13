import json, os
os.environ.setdefault('MPLCONFIGDIR', os.environ.get('TMPDIR', '/tmp') + '/mplcache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(DATA_DIR, '..', 'images')
geo = json.load(open(os.path.join(DATA_DIR, 'ne_50m_admin_0_countries.geojson')))

LON_MIN, LON_MAX = -10, 29
LAT_MIN, LAT_MAX = 34, 66.4  # top gap above Oulu ≈ bottom gap below Crete

# palette matches the rest of the deck (theme/styles/index.css, LatencyStack.vue, TimeBar.vue)
BLUE   = '#4285F4'   # STAGE / theme primary
GOLD   = '#E6B96A'   # LifeCycle (other)
TEAL   = '#0097A7'   # NCC / theme accent
PURPLE = '#6A4C93'   # NDTD
RED    = '#D9534F'   # Athlete
NAVY   = '#1E3A5F'   # IPEC
GREY   = '#9AA4B0'   # Other (Longitools/PCN)

# True geocoded (lon, lat) per city — the source of truth. Look a new city up here first;
# only nudge away from it (see below) when another marker already sits on the same spot.
CITY = {
    'Amsterdam': (4.9041, 52.3676), 'Barcelona': (2.1686, 41.3874), 'Munich': (11.5820, 48.1351),
    'Paris': (2.3522, 48.8566), 'Copenhagen': (12.5683, 55.6761), 'Groningen': (6.5665, 53.2194),
    'Helsinki': (24.9384, 60.1699), 'Athens': (23.7275, 37.9838), 'Oslo': (10.7522, 59.9139),
    'Oulu': (25.4651, 65.0121), 'Rennes': (-1.6778, 48.1173), 'Kuopio': (27.6782, 62.8924),
    'Heraklion': (25.1442, 35.3387), 'Southampton': (-1.4044, 50.9097), 'Porto': (-8.6291, 41.1579),
    'Kaunas': (23.9036, 54.8985), 'London': (-0.1276, 51.5072), 'Brno': (16.6068, 49.1951),
    'Rotterdam': (4.4777, 51.9244), 'Grenoble': (5.7245, 45.1885), 'Manchester': (-2.1591, 53.4084),
    'Turku': (22.2666, 60.4518), 'Stockholm': (18.0686, 59.3293), 'Aberdeen': (-2.0943, 57.1497),
    'Dublin': (-6.2603, 53.3498), 'Cork': (-8.4756, 51.8985), 'Maastricht': (5.6909, 50.8514),
    'Utrecht': (5.1214, 52.0907), 'Leiden': (4.4970, 52.1601), 'Warsaw': (21.0122, 52.2297),
    'Krakow': (19.9450, 50.0647), 'Kosice': (21.2611, 48.7164), 'Bologna': (11.3426, 44.4949),
    'Pisa': (10.4017, 43.7228), 'Milan': (9.1900, 45.4642), 'Valencia': (-0.3763, 39.4699),
    'Turin': (7.6869, 45.0703), 'Bristol': (-2.5879, 51.4545), 'Doetinchem': (6.2887, 51.9645),
    'Leidsche_Rijn': (5.0333, 52.0833),
}

# STAGE cohorts for the STAGE-only map. (lon, lat) here are real for singly-occupied cities;
# NFBC86 is nudged 0.45/-0.1 degrees east/south of Oulu's true coordinate — a fake position
# chosen only so its dot doesn't sit exactly on top of NFBC66's, not a real place.
STAGE = [
    ('1', 25.4651, 65.0121, 'NFBC66'),   # true Oulu coordinate
    ('2', 25.9151, 64.9121, 'NFBC86'),   # fake — nudged off Oulu for visibility
    ('3', 4.4777, 51.9244, 'Gen-R'),     # true Rotterdam coordinate
    ('4', 7.6869, 45.0703, 'NINFEA'),    # true Turin coordinate
    ('5', -2.5879, 51.4545, 'ALSPAC'),   # true Bristol coordinate
]

# Same 5 STAGE cohorts as plotted inside the all-cohorts map — tighter fake nudges (a few km)
# since that map is much denser; kept as a separate list because the two maps use different
# amounts of spacing for the same underlying cohort.
STAGE_IN_ALL_MAP = [
    ('1', 25.4699, 64.9570, 'NFBC66'),   # fake — small nudge off Oulu
    ('2', 25.5036, 65.0623, 'NFBC86'),   # fake — small nudge off Oulu
    ('3', 4.4445, 51.9548, 'Gen-R'),     # fake — small nudge off Rotterdam
    ('4', 7.6869, 45.0703, 'NINFEA'),    # true Turin coordinate (no other marker there)
    ('5', -2.5879, 51.4545, 'ALSPAC'),   # true Bristol coordinate (no other marker there)
]

# All other cohorts for the all-cohorts map. (lon, lat) are real geocoded city coordinates;
# where several cohorts share a city, every entry but the first has been nudged a few km off
# the true point (small fake offset, purely so dots don't stack) — see CITY above for the
# real coordinate each one is nudged from.
DOTS = [
    ('ABCD', 4.9041, 52.3676, GOLD, 'LifeCycle'),                          # true Amsterdam
    ('Dutch Famine BC', 4.8709, 52.3980, GOLD, 'LifeCycle'),               # fake — nudged off Amsterdam
    ('MoBa', 10.7522, 59.9139, GOLD, 'LifeCycle'),                         # true Oslo
    ('HUMIS', 10.7190, 59.9443, GOLD, 'LifeCycle'),                        # fake — nudged off Oslo
    ('STEPS', 22.2666, 60.4518, GOLD, 'LifeCycle'),                        # true Turku
    ('LUKAS', 27.6782, 62.8924, GOLD, 'LifeCycle'),                        # true Kuopio
    ('HBCS', 24.9384, 60.1699, GOLD, 'LifeCycle'),                         # true Helsinki
    ('BAMSE', 18.0686, 59.3293, GOLD, 'LifeCycle'),                        # true Stockholm
    ('DNBC', 12.5683, 55.6761, GOLD, 'LifeCycle'),                         # true Copenhagen
    ('SEATON', -2.0943, 57.1497, GOLD, 'LifeCycle'),                       # true Aberdeen
    ('SWS', -1.4044, 50.9097, GOLD, 'LifeCycle'),                          # true Southampton
    ('ROLO', -6.2603, 53.3498, GOLD, 'LifeCycle'),                         # true Dublin
    ('SCOPE BASELINE', -8.4756, 51.8985, GOLD, 'LifeCycle'),               # true Cork
    ('KOALA', 5.6909, 50.8514, GOLD, 'LifeCycle'),                         # true Maastricht
    ('PIAMA', 5.1214, 52.0907, GOLD, 'LifeCycle'),                         # true Utrecht
    ('PRIDE', 4.4970, 52.1601, GOLD, 'LifeCycle'),                         # true Leiden
    ('GECKO', 6.5665, 53.2194, GOLD, 'LifeCycle'),                         # true Groningen
    ('REPRO_PL', 21.0122, 52.2297, GOLD, 'LifeCycle'),                     # true Warsaw
    ('GINI/LISA-plus', 11.5820, 48.1351, GOLD, 'LifeCycle'),               # true Munich
    ('CHOP', 11.5488, 48.1655, GOLD, 'LifeCycle'),                         # fake — nudged off Munich
    ('Krakow', 19.9450, 50.0647, GOLD, 'LifeCycle'),                       # true Krakow
    ('Slovak PCB Study', 21.2611, 48.7164, GOLD, 'LifeCycle'),             # true Kosice
    ('Co.N.ER', 11.3426, 44.4949, GOLD, 'LifeCycle'),                      # true Bologna
    ('GASPII', 10.4017, 43.7228, GOLD, 'LifeCycle'),                       # true Pisa
    ('Piccolipiu', 9.1900, 45.4642, GOLD, 'LifeCycle'),                    # true Milan
    ('Generation XXI / G21', -8.6291, 41.1579, GOLD, 'LifeCycle'),         # true Porto
    ('INMA', -0.3763, 39.4699, GOLD, 'LifeCycle'),                         # true Valencia
    ('Genesis', 23.7275, 37.9838, GOLD, 'LifeCycle'),                      # true Athens
    ('RHEA', 25.1442, 35.3387, GOLD, 'LifeCycle'),                         # true Heraklion
    ('EDEN', 2.3522, 48.8566, GOLD, 'LifeCycle'),                          # true Paris
    ('ELFE', 2.3190, 48.8870, GOLD, 'LifeCycle'),                          # fake — nudged off Paris
    ('PELAGIE', -1.6778, 48.1173, GOLD, 'LifeCycle'),                      # true Rennes
    ('OULU1935 / OULU1945', 25.4651, 65.0121, GOLD, 'LifeCycle'),          # true Oulu

    ('De Maastricht Studie', 5.6577, 50.8818, TEAL, 'NCC'),                # fake — nudged off Maastricht
    ('Rotterdam Study (ERGO)', 4.4777, 51.9244, TEAL, 'NCC'),              # true Rotterdam
    ('LRGP', 5.0333, 52.0833, TEAL, 'NCC'),                                # true Leidsche Rijn
    ('Leiden Longevity Study', 4.4638, 52.1905, TEAL, 'NCC'),              # fake — nudged off Leiden
    ('Doetinchem Cohort', 6.2887, 51.9645, TEAL, 'NCC'),                   # true Doetinchem
    ('Helius', 4.9089, 52.3125, TEAL, 'NCC'),                              # fake — nudged off Amsterdam
    ('NEO', 4.5018, 52.1050, TEAL, 'NCC'),                                 # fake — nudged off Leiden
    ('Lifelines', 6.5333, 53.2498, TEAL, 'NCC'),                           # fake — nudged off Groningen
    ('Epic-NL', 5.0882, 52.1211, TEAL, 'NCC'),                             # fake — nudged off Utrecht
    ('Netherlands Twin Register', 4.9426, 52.4178, TEAL, 'NCC'),           # fake — nudged off Amsterdam
    ('LASA', 4.8352, 52.3554, TEAL, 'NCC'),                                # fake — nudged off Amsterdam

    ('Amsterdam UMC', 4.9681, 52.3269, PURPLE, 'NDTD'),                    # fake — nudged off Amsterdam
    ('Parnassia Groep', 4.8830, 52.4460, PURPLE, 'NDTD'),                  # fake — nudged off Amsterdam
    ('Pro Persona', 4.8644, 52.2911, PURPLE, 'NDTD'),                      # fake — nudged off Amsterdam

    ('BISC', 2.1686, 41.3874, RED, 'Athlete'),                             # true Barcelona
    ('HELIX', 2.1354, 41.4178, RED, 'Athlete'),                            # fake — nudged off Barcelona
    ('EnvironAGE', 2.1734, 41.3323, RED, 'Athlete'),                       # fake — nudged off Barcelona
    ('KANC', 23.9036, 54.8985, RED, 'Athlete'),                            # true Kaunas
    ('CELSPAC-TNG (Recetox)', 16.6068, 49.1951, RED, 'Athlete'),           # true Brno
    ('SEPAGES', 5.7245, 45.1885, RED, 'Athlete'),                          # true Grenoble
    ('RCGP RSC', -0.1276, 51.5072, RED, 'Athlete'),                        # true London

    ('NFBC1966 G0', 25.4319, 65.0425, NAVY, 'IPEC'),                       # fake — nudged off Oulu
    ('NOMA', 10.7570, 59.8588, NAVY, 'IPEC'),                              # fake — nudged off Oslo
    ('PANIC', 27.6450, 62.9228, NAVY, 'IPEC'),                             # fake — nudged off Kuopio
    ('UK Biobank', -2.1591, 53.4084, NAVY, 'IPEC'),                        # true Manchester
    ('ELIPA / FEF / FinnGeDi', 24.9052, 60.2003, NAVY, 'IPEC'),            # fake — nudged off Helsinki
    ('Finnish Maternity/Register Cohorts', 24.9432, 60.1148, NAVY, 'IPEC'),# fake — nudged off Helsinki

    ('Borealis biobank', 10.7907, 59.9641, GREY, 'Other'),                 # fake — nudged off Oslo
    ('Constances', 2.3570, 48.8015, GREY, 'Other'),                        # fake — nudged off Paris
    ('SYSDIMET', 27.6830, 62.8373, GREY, 'Other'),                         # fake — nudged off Kuopio
    ('FCOU', 20.9790, 52.2601, GREY, 'Other'),                             # fake — nudged off Warsaw
]


def draw_countries(ax):
    for feat in geo['features']:
        geom = feat['geometry']
        if geom is None:
            continue
        polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
        for poly in polys:
            ring = poly[0]
            ax.add_patch(Polygon(ring, closed=True, facecolor='#c9c9c9', edgecolor='white',
                                  linewidth=0.6, zorder=1))
    ax.set_xlim(LON_MIN, LON_MAX)
    ax.set_ylim(LAT_MIN, LAT_MAX)
    ax.set_aspect(1.55)
    ax.axis('off')
    ax.set_facecolor('white')


def build_stage_map():
    """STAGE cohorts only, numbered markers with a name legend at top."""
    fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    draw_countries(ax)

    for num, lon, lat, name in STAGE:
        ax.scatter([lon], [lat], s=140, facecolor=BLUE, edgecolor='white', linewidth=1.2, zorder=4)
        ax.text(lon, lat, num, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white', zorder=5)

    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=BLUE,
                           markeredgecolor='white', markersize=9,
                           label=f'{num}  {name}')
               for num, lon, lat, name in STAGE]
    leg = ax.legend(handles=handles, loc='upper left', frameon=True, fontsize=10,
                     title='STAGE cohorts', title_fontsize=12,
                     bbox_to_anchor=(0.01, 0.99), borderaxespad=0.5)
    leg.get_frame().set_edgecolor('#b4b4b4')
    leg.get_frame().set_facecolor('white')
    leg._legend_box.align = 'left'

    out = os.path.join(IMAGES_DIR, 'stage_europe_map.png')
    fig.savefig(out, bbox_inches='tight', pad_inches=0.05, dpi=150)
    plt.close(fig)
    print('saved', out)


def build_all_cohorts_map():
    """All cohorts, coloured by consortium/group. STAGE dots unnumbered, same style as the rest."""
    fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    draw_countries(ax)

    for label, lon, lat, color, group in DOTS:
        ax.scatter([lon], [lat], s=140, facecolor=GOLD, edgecolor='white', linewidth=0.8, zorder=3)

    for num, lon, lat, name in STAGE_IN_ALL_MAP:
        ax.scatter([lon], [lat], s=140, facecolor=BLUE, edgecolor='white', linewidth=0.8, zorder=3)

    groups = [('STAGE', BLUE), ('Other DataSHIELD infrastructure', GOLD)]
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c,
                           markeredgecolor='white', markersize=7, label=n)
               for n, c in groups]
    leg = ax.legend(handles=handles, loc='upper left', frameon=True, fontsize=8,
                     title='Cohort groups', title_fontsize=10,
                     bbox_to_anchor=(0.01, 0.99), borderaxespad=0.5)
    leg.get_frame().set_edgecolor('#b4b4b4')
    leg.get_frame().set_facecolor('white')
    leg._legend_box.align = 'left'

    out = os.path.join(IMAGES_DIR, 'stage_europe_map_all_cohorts.png')
    fig.savefig(out, bbox_inches='tight', pad_inches=0.05, dpi=150)
    plt.close(fig)
    print('saved', out)


if __name__ == '__main__':
    build_stage_map()
    build_all_cohorts_map()
