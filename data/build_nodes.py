"""Rebuild data/datashield_nodes.csv from every source, start to finish."""
"""Build data/datashield_nodes.csv — the source of truth for DataSHIELD nodes.

Re-run after editing any input:  python3 data/build_nodes.py

Inputs
  cohorts_extra.csv        institution and country per cohort
  build_cohort_map.py      city coordinates, and the NCC/NDTD/STAGE grouping
  datashield_org_map.png   the network map from datashield.org, used as the
                           evidence that a node exists at all
  ne_50m_admin_0_countries.geojson   to name the country of an unnamed pin
  the lists below          project membership, from each project's own published list

Rules
  * A cohort is listed only where a pin on the datashield.org map covers it, or
    where it is a planned node. Project membership alone is not a node.
  * LongITools is a label, not a group: it is carried only by cohorts that are
    also LifeCycle or ATHLETE. Its other studies run no server.
  * Other is a strict catch-all — never alongside a named project.
"""
import csv, re, json, math, os, unicodedata
from collections import deque
import numpy as np
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
def path(*p): return os.path.join(D, *p)

src = open(path('build_cohort_map.py')).read()

city_blk = src[src.index('CITY = {'):src.index('}', src.index('CITY = {'))]
CITY = {n: (float(lo), float(la)) for n, lo, la in
        re.findall(r"'([^']+)': \(([-\d.]+), ([-\d.]+)\)", city_blk)}
CITY.update({'Bradford': (-1.7594, 53.7960), 'Perth': (115.8605, -31.9505),
             'Hasselt': (5.3378, 50.9307)})
def nearest_city(lon, lat):
    return min(CITY, key=lambda c: (CITY[c][0]-lon)**2 + (CITY[c][1]-lat)**2)

def k(n):
    n = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore').decode().lower()
    n = re.split(r'[/(]', n)[0]
    n = re.sub(r'\b(generation|gen)\b', 'gen', n)
    return re.sub(r'[^a-z0-9]', '', n)
ALIAS = {'borninbradfordbib': 'bib', 'bornibradfordbib': 'bib', 'nfbc66': 'nfbc1966',
         'nfbc86': 'nfbc1986', 'genxxi': 'genxxi', 'g21': 'genxxi',
         'celspactng': 'celspac', 'celspac': 'celspac', 'alspacgen0': 'alspac',
         'alspacgen1': 'alspac', 'alspacgen2': 'alspac', 'genr': 'genr',
         'genrnext': 'genrnext', 'dutchfaminebirthcohortstudy': 'dutchfaminebc',
         'dutchfaminebirthcohort': 'dutchfaminebc',
         'rotterdamstudyfirstcohort': 'rotterdamstudy',
         'rotterdamstudysecondcohort': 'rotterdamstudy',
         'rotterdamstudythirdcohort': 'rotterdamstudy',
         'rotterdamstudyergo': 'rotterdamstudy', 'psyconnipec': 'psyconn', 'opus': 'opus'}
def K(n):
    x = k(n); return ALIAS.get(x, x)

PROJ = ['LifeCycle', 'Athlete', 'Longitools', 'IPEC', 'NCC', 'NDTD', 'STAGE',
        'JOIN-MIND', 'FEDHAFRICA', 'MDR-RA', 'DSWB', 'Other']
COLS = ['cohort', 'institution', 'country', 'city', 'lon', 'lat'] + PROJ + ['status', 'sources']

rec = {}
def get(name):
    key = K(name)
    if key not in rec:
        rec[key] = {c: '' for c in COLS}
        rec[key].update({'cohort': name, 'status': 'live', 'sources': set()})
    return rec[key]

# --- coordinates and the map builder's own grouping
dots = re.findall(r"\('([^']+)', *([-\d.]+), *([-\d.]+), *[A-Z]+, *'([^']+)'\)", src)
stage = re.findall(r"\('\d', *([-\d.]+), *([-\d.]+), *'([^']+)'\)", src)
for name, lon, lat, group in dots:
    r = get(name)
    c = nearest_city(float(lon), float(lat))
    r['city'] = c; r['lon'], r['lat'] = CITY[c]
    if group in ('NCC', 'NDTD'): r[group] = 'x'
    r['sources'].add('map')
for lon, lat, name in stage:
    r = get(name)
    c = nearest_city(float(lon), float(lat))
    r['city'] = c; r['lon'], r['lat'] = CITY[c]
    r['STAGE'] = 'x'; r['sources'].add('map')

# --- institution / country
for row in csv.DictReader(open(path('cohorts_extra.csv'))):
    name = (row['Cohort'] or '').strip()
    if not name or name in ('IPEC', 'PCN'): continue
    r = get(name)
    r['institution'] = r['institution'] or (row['Institution'] or '').strip()
    r['country'] = r['country'] or (row['Country'] or '').strip()
    r['sources'].add('csv')

# --- project membership, from each project's own published list
LC = ['ALSPAC','BIB','CHOP','DNBC','EDEN','ELFE','GECKO','Generation R','Generation R Next',
      'HBCS','INMA','MoBa','NFBC1966','NFBC1986','NINFEA','RAINE','RHEA','SWS']
AT = ['BIB','BiSC','DNBC','EDEN','ENVIRONAGE','G21','Generation R','Generation R Next','INMA',
      'KANC','MoBa','NINFEA','PELAGIE','Piccolipiu','RHEA','SEPAGES','CELSPAC-TNG','ABCD']
LT = ['ALSPAC','EDEN','ELFE','Generation R','NFBC1966','NFBC1986']   # label only; see note
IPEC = ['PSYCONN','OPUS']
for names, col in ((LC,'LifeCycle'), (AT,'Athlete'), (LT,'Longitools'), (IPEC,'IPEC')):
    for n in names:
        get(n)[col] = 'x'
        get(n)['sources'].add('project list')

# a few fixes the sources got wrong
if 'environage' in rec:
    rec['environage'].update({'city':'Hasselt','country':'Belgium','lon':5.3378,'lat':50.9307})
if 'psyconn' in rec:
    rec['psyconn'].update({'cohort':'PSYCONN','city':'Groningen','country':'NL',
                           'lon':CITY['Groningen'][0],'lat':CITY['Groningen'][1]})
if 'opus' in rec:
    rec['opus'].update({'cohort':'OPUS','city':'Copenhagen','country':'Denmark',
                        'lon':CITY['Copenhagen'][0],'lat':CITY['Copenhagen'][1]})
INFER = {'bib':'Bradford','raine':'Perth','hgs':'Athens','genrnext':'Rotterdam',
         'piccolipiu':'Milan'}
for key, c in INFER.items():
    if key in rec and not rec[key]['lon']:
        rec[key].update({'city':c, 'lon':CITY[c][0], 'lat':CITY[c][1]})
        rec[key]['sources'].add('inferred')

# HELIX is a project assembled from BiB, EDEN, INMA, KANC, MoBa and RHEA, all listed
# separately — it is not a node of its own.
rec.pop('helix', None)

# NDTD sites the map builder missed
r = get('GGZ inGeest')
r.update({'city': 'Amsterdam', 'country': 'NL',
          'lon': CITY['Amsterdam'][0], 'lat': CITY['Amsterdam'][1]})
r['NDTD'] = 'x'; r['sources'].add('Tim')

named = list(rec.values())

# --- projects whose nodes are not on the datashield.org map yet. Deployed where the
# grant is running; `planned` is reserved for pre grant-award sites.
DEPLOYED = {'MDR-RA', 'DSWB', 'NDTD'}
PLANNED = [('UMCG','Groningen','NL',CITY['Groningen'][0],CITY['Groningen'][1],'NDTD'),
           ('VU Amsterdam','Amsterdam','NL',4.9041,52.3676,'JOIN-MIND'),
           ('Stichting Vluchteling','The Hague','NL',4.3007,52.0705,'JOIN-MIND'),
           ('Save the Children','London','UK',-0.1276,51.5072,'JOIN-MIND'),
           ('Geneva','Geneva','Switzerland',6.1432,46.2044,'JOIN-MIND')]
for country, sites in [
    ('Kenya',[('Nairobi',36.8219,-1.2921),('Mombasa',39.6682,-4.0435),('Kisumu',34.7680,-0.0917)]),
    ('Uganda',[('Kampala',32.5825,0.3476),('Gulu',32.2990,2.7746),('Mbarara',30.6585,-0.6072)]),
    ('Senegal',[('Dakar',-17.4677,14.7167),('Thies',-16.9246,14.7910),('Saint-Louis',-16.4896,16.0179)]),
    ('Tanzania',[('Dar es Salaam',39.2083,-6.7924),('Dodoma',35.7516,-6.1630),('Mwanza',32.8990,-2.5164)])]:
    for city, lon, lat in sites:
        PLANNED.append((f'FEDHAFRICA {city}', city, country, lon, lat, 'FEDHAFRICA'))
# MDR-RA (Horizon Europe, mdr-ra.eu): the clinical and university partners that
# plausibly hold patient data. The project does not publish which sites host servers.
for name, city, country, lon, lat in [
    ('Humanitas University', 'Milan', 'Italy', 9.1900, 45.4642),
    ('University of Verona', 'Verona', 'Italy', 10.9916, 45.4384),
    ('UMC Utrecht', 'Utrecht', 'Netherlands', 5.1214, 52.0907),
    ('Karolinska Institute', 'Stockholm', 'Sweden', 18.0686, 59.3293),
    ('Queen Mary University of London', 'London', 'United Kingdom', -0.1276, 51.5072),
    ('University of Manchester', 'Manchester', 'United Kingdom', -2.2426, 53.4808),
    ('University Hospital Zurich', 'Zurich', 'Switzerland', 8.5417, 47.3769),
    ('Medical University of Vienna', 'Vienna', 'Austria', 16.3738, 48.2082),
    ('Odense University Hospital', 'Odense', 'Denmark', 10.3883, 55.4038),
    ('Cliniques Universitaires Saint-Luc', 'Brussels', 'Belgium', 4.3517, 50.8503),
    ('FAU Erlangen', 'Erlangen', 'Germany', 11.0170, 49.5897),
    ('Diakonhjemmet Hospital', 'Oslo', 'Norway', 10.7522, 59.9139),
]:
    PLANNED.append((name, city, country, lon, lat, 'MDR-RA'))

# Data Science Without Borders (Kiragga et al. 2025, Front Public Health): APHRC and
# its three Pathfinder institutions. Planned — federated deployment is their Phase 4.
for name, city, country, lon, lat in [
    ('APHRC', 'Nairobi', 'Kenya', 36.8219, -1.2921),
    ('IRESSEF', 'Dakar', 'Senegal', -17.4677, 14.7167),
    ('AHRI', 'Addis Ababa', 'Ethiopia', 38.7578, 9.0320),
    ('Douala General Hospital', 'Douala', 'Cameroon', 9.7679, 4.0511),
]:
    PLANNED.append((name, city, country, lon, lat, 'DSWB'))

planned = []
for name, city, country, lon, lat, proj in PLANNED:
    r = {c: '' for c in COLS}
    r.update({'cohort':name,'city':city,'country':country,'lon':lon,'lat':lat,
              proj:'x','status':'live' if proj in DEPLOYED else 'planned',
              'sources':{{'FEDHAFRICA':'FEDHAFRICA site illustrative',
                          'MDR-RA':'mdr-ra.eu','DSWB':'Kiragga 2025','NDTD':'INDEPTH partners'}.get(proj, 'JOIN-MIND')}})
    planned.append(r)

# --- the datashield.org map: projection fitted to the European cohorts we hold
def pin_boxes(png):
    """Bounding box of every red marker blob. Overlapping markers merge into one
    box, which is why coverage is tested against the box and not a centroid."""
    im = np.array(Image.open(png).convert('RGB')).astype(int)
    r, g, b = im[:, :, 0], im[:, :, 1], im[:, :, 2]
    mask = (r > 150) & (g < 90) & (b < 90)
    H, W = mask.shape
    seen = np.zeros_like(mask, bool)
    out = []
    for y in range(H):
        for x in np.nonzero(mask[y] & ~seen[y])[0]:
            if seen[y, x]: continue
            q = deque([(y, x)]); seen[y, x] = True; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True; q.append((ny, nx))
            if len(pts) >= 12:
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                out.append((min(xs), min(ys), max(xs), max(ys), len(pts)))
    return np.array(out)

boxes = pin_boxes(path('datashield_org_map.png'))
s, cx, cy = 2064.0, 928.0, 573.0
kpx = s / 360.0
def merc(lat): return math.log(math.tan(math.pi/4 + math.radians(lat)/2))
def to_px(lon, lat): return cx + lon*kpx, cy - merc(lat)*(s/(2*math.pi))
def inv(x, y):
    lon = (x - cx)/kpx
    return lon, math.degrees(2*math.atan(math.exp((cy-y)/(s/(2*math.pi)))) - math.pi/2)

PAD = 14   # fit error (~7px) plus half a marker
def covered(r):
    if not r['lon']: return False
    x, y = to_px(float(r['lon']), float(r['lat']))
    return any(b[0]-PAD <= x <= b[2]+PAD and b[1]-PAD <= y <= b[3]+PAD for b in boxes)

for r in named:
    if covered(r): r['sources'].add('datashield.org map')

# unnamed nodes: blobs with no cohort of ours inside them
claimed = set()
for r in named:
    if not r['lon']: continue
    x, y = to_px(float(r['lon']), float(r['lat']))
    for i, b in enumerate(boxes):
        if b[0]-PAD <= x <= b[2]+PAD and b[1]-PAD <= y <= b[3]+PAD: claimed.add(i)
geo = json.load(open(path('ne_50m_admin_0_countries.geojson')))
ring_pts = [(x, y, f['properties'].get('NAME') or f['properties'].get('ADMIN'))
            for f in geo['features'] if f['geometry']
            for poly in (f['geometry']['coordinates'] if f['geometry']['type']=='MultiPolygon'
                         else [f['geometry']['coordinates']])
            for x, y, *_ in poly[0]]
def snap(lo, la): return min(ring_pts, key=lambda c: (c[0]-lo)**2 + (c[1]-la)**2)[2]
# country names arrive in three spellings: ISO-ish codes from cohorts_extra.csv,
# full names from the geojson, and a few local forms
COUNTRY = {'NL': 'Netherlands', 'UK': 'United Kingdom', 'USA': 'United States of America',
           'Italia': 'Italy', 'Czech Republic': 'Czechia', 'Espana': 'Spain'}
for r in named:
    r['country'] = COUNTRY.get(r['country'], r['country'])

# rows that came only from the map builder carry no country
for r in named:
    if r['lon'] and not r['country']:
        r['country'] = snap(float(r['lon']), float(r['lat']))

unnamed = []
for i, b in enumerate(boxes):
    if i in claimed: continue
    lo, la = inv((b[0]+b[2])/2, b[3])
    r = {c: '' for c in COLS}
    r.update({'cohort':'(unnamed node)','country':snap(lo,la),'lon':round(lo,3),'lat':round(la,3),
              'Other':'x','status':'live','sources':{'datashield.org map'}})
    unnamed.append(r)

# NDTD sites: the pins above only show that a server exists near Amsterdam. The sites
# themselves are UMCG (Groningen), GGZ inGeest (Amsterdam), Pro Persona (Nijmegen) and
# Parnassia Groep (The Hague); Amsterdam UMC is not one of them. Placed after the pin check.
for name, city, lon, lat in [('Pro Persona', 'Nijmegen', 5.8372, 51.8126),
                             ('Parnassia Groep', 'The Hague', 4.3007, 52.0705)]:
    rec[K(name)].update({'city': city, 'lon': lon, 'lat': lat, 'country': 'Netherlands'})
rec[K('Amsterdam UMC')]['NDTD'] = ''

rows = named + planned + unnamed
for r in rows:
    if r['cohort'] != '(unnamed node)':
        if r['Other'] and any(r[p] for p in PROJ if p != 'Other'): r['Other'] = ''
        if not any(r[p] for p in PROJ): r['Other'] = 'x'

# LongITools runs few nodes of its own: keep its studies only where they are also
# a LifeCycle/ATHLETE cohort or already hold a node under another project.
LT_ONLY = {'arcticbiobank','borealisbiobank','constances','dutchfaminebc','elipa','fef',
           'fibrefects','finngedi','finnishmaternitycohort','finnishregistersample',
           'finnishmaternityregistercohorts','nfbc1966g0','noma','nordcap','oulu1935',
           'oulu1945','oulu1935oulu1945','panic','sysdimet','ukbiobank','rcgprsc',
           'finnishmaternityregistercohorts','finnishmaternity','elipa'}
OTHERP = [p for p in PROJ if p not in ('Longitools','Other')]
before = len(rows)
# nodes a project told us about are evidence in themselves; only the cohorts we
# inferred from the two local files have to be backed by a pin
project_rows = {id(r) for r in planned}
dropped = [r for r in rows if r['cohort'] != '(unnamed node)' and id(r) not in project_rows
           and (K(r['cohort']) in LT_ONLY and not any(r[p] for p in OTHERP)
                or 'datashield.org map' not in r['sources'])]
rows = [r for r in rows if r not in dropped]
print('dropped %d (LongITools study with no node, or no pin on the map):' % len(dropped))
for r in sorted(dropped, key=lambda r: r['cohort'].lower()):
    print('   %-34s %s' % (r['cohort'], r['city'] or r['country']))
print()

rows.sort(key=lambda r: (r['cohort'] == '(unnamed node)', r['cohort'].lower()))
for r in rows:
    r['sources'] = '+'.join(sorted(r['sources'])) if isinstance(r['sources'], set) else r['sources']
w = csv.DictWriter(open(path('datashield_nodes.csv'), 'w', newline=''), fieldnames=COLS)
w.writeheader(); w.writerows(rows)

# the deck reads this, so a component never parses the CSV at runtime
js = [{'name': r['cohort'], 'city': r['city'], 'country': r['country'],
       'lon': float(r['lon']), 'lat': float(r['lat']), 'status': r['status'],
       'projects': [p for p in PROJ if r[p]]}
      for r in rows if r['lon']]
with open(path('..', 'components', 'datashield-nodes.js'), 'w') as fh:
    fh.write('// Generated by data/build_nodes.py — do not edit.\n')
    fh.write('export const NODES = ' + json.dumps(js, indent=0).replace('\n', '') + '\n')
    fh.write('export const EXPOSOME = [\'LifeCycle\', \'Athlete\', \'Longitools\']\n')

nm = [r for r in rows if r['cohort'] != '(unnamed node)']
print('named', len(nm), '| unnamed', len(unnamed), '| planned', len(planned))
nopin = [r for r in nm if r['status']=='live' and 'datashield.org map' not in r['sources']]
print('\nlive cohorts with no pin covering them (%d):' % len(nopin))
for r in nopin: print('   %-34s %s' % (r['cohort'], r['city'] or r['country']))
print()
for p in PROJ:
    m = [r['cohort'] for r in nm if r[p]]
    print(f'{p:11} {len(m):3}  {", ".join(m[:14])}{" …" if len(m)>14 else ""}')
