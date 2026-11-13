"""Node maps for the datashield-network deck: all nodes, then one map per example project.

Node lists come from ihen-26/build_maps.py (IHEN_NODES) and data/build_cohort_map.py (NDTD).
Africa project nodes are not yet known, so that map is not built.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, 'public')
sys.path.insert(0, os.path.join(HERE, '..', 'data'))
from build_cohort_map import plt, draw_countries, DOTS, BLUE, RED, PURPLE  # noqa: E402

GREY = '#9AA0A6'


def load_ihen_nodes():
    """Return IHEN_NODES from ihen-26/build_maps.py as (label, lon, lat, project) tuples."""
    spec = importlib.util.spec_from_file_location(
        'ihen_build_maps', os.path.join(HERE, '..', 'ihen-26', 'build_maps.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.IHEN_NODES


def collect_nodes():
    """Return every node as (label, lon, lat, project), adding the NDTD sites to the IHEN list."""
    ndtd = [(label, lon, lat, 'NDTD') for label, lon, lat, _, group in DOTS if group == 'NDTD']
    return load_ihen_nodes() + ndtd


def save_map(nodes, highlight, colour, legend_label, filename):
    """Plot all nodes, colouring those in the highlighted project, and save into public/."""
    fig, ax = plt.subplots(figsize=(12, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    draw_countries(ax)
    for _, lon, lat, project in nodes:
        is_on = highlight is None or project == highlight
        ax.scatter([lon], [lat], s=140, facecolor=colour if is_on else GREY,
                   edgecolor='white', linewidth=0.8, zorder=4 if is_on else 3)
    count = sum(1 for *_, p in nodes if highlight is None or p == highlight)
    handle = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colour,
                        markeredgecolor='white', markersize=9, label=f'{legend_label} ({count})')
    leg = ax.legend(handles=[handle], loc='upper left', frameon=True, fontsize=12,
                    bbox_to_anchor=(0.01, 0.99), borderaxespad=0.5)
    leg.get_frame().set_edgecolor('#b4b4b4')
    out = os.path.join(PUBLIC, filename)
    fig.savefig(out, bbox_inches='tight', pad_inches=0.05, dpi=150)
    plt.close(fig)
    print('saved', out)


if __name__ == '__main__':
    nodes = collect_nodes()
    save_map(nodes, None, BLUE, 'DataSHIELD nodes', 'map_all_nodes.png')
    save_map(nodes, 'ATHLETE', RED, 'ATHLETE', 'map_athlete.png')
    save_map(nodes, 'NDTD', PURPLE, 'NDTD', 'map_ndtd.png')
