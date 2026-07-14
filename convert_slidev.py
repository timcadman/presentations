"""
convert_slidev.py — strip a Slidev slides.md to plain content and render it as an
editable, branded PowerPoint via build_deck.DeckBuilder.

    python3 convert_slidev.py molgenis-armadillo/slides.md /tmp/out.pptx [slidev_png_dir]

slidev_png_dir (optional): folder of rendered Slidev PNGs (1.png..N.png), used as a
whole-slide fallback for slides that can't be made editable (bespoke Vue diagrams).
Produce it with:  npx slidev export slides.md --format png --output <dir>
"""
import html, os, re, sys
from build_deck import DeckBuilder

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Slidev theme layout  ->  default PPTX builder spec type (build_deck.py).
# This is the registry to extend when a new layout is added to theme/layouts/.
# Notes:
#   - Body-pattern special cases in to_spec() (team grid, deploy/adv cards,
#     hw-grid table, bespoke <Component/> diagrams) override these.
#   - Per-slide override: add `pptx: <type>` to a slide's frontmatter to force a
#     spec type (e.g. `pptx: photo` for a full-bleed image instead of contained).
#   - content-img-* carry side via the layout name; imageScale/imageWidth/
#     imageAlign are Slidev-only and don't affect the PPTX (the template's
#     Image/Photo layouts have fixed geometry).
# PPTX template layouts these resolve to: Title, Bullets, Image Right/Left,
#   Photo Right/Left, Table  (plus two_images/slide_image drawn on Bullets).
# ---------------------------------------------------------------------------
LAYOUT_MAP = {
    "cover":             "title",        # Slidev's implicit first-slide layout
    "content":           "bullets",
    "content-img-right": "image",        # contained image, right column
    "content-img-left":  "image",        # contained image, left column
    "content-two-images": "two_images",
    "section":           "bullets",
    "default":           "bullets",
}


def parse_frontmatter(block):
    fm = {}
    for line in block.strip().splitlines():
        m = re.match(r'\s*([A-Za-z0-9_-]+):\s*(.*)', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def split_slides(text):
    """Return list of (frontmatter_dict, body_str). First slide has no frontmatter."""
    parts = re.split(r'(?m)^---\s*$', text)
    slides = [({}, parts[2])]
    i = 3
    while i < len(parts):
        fm = parse_frontmatter(parts[i])
        body = parts[i + 1] if i + 1 < len(parts) else ""
        slides.append((fm, body))
        i += 2
    return slides


def clean_inline(t):
    t = re.sub(r'<br\s*/?>', ' ', t)                 # line breaks -> space
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)   # [text](url) -> text
    t = re.sub(r'\*\*?(.*?)\*\*?', r'\1', t)         # **bold** / *em* -> text
    t = t.replace('`', '')                           # `code` -> text (no literal backticks)
    t = re.sub(r'<.*?>', ' ', t)                     # any stray tags -> space (keep word gaps)
    t = html.unescape(t)                             # &amp; &ensp; &nbsp; -> chars
    t = re.sub(r'\s+', ' ', t)
    return t.strip()


def md_bullets(body):
    out = []
    for line in body.splitlines():
        m = re.match(r'(\s*)[-*]\s+(.*)', line)
        if m:
            indent = len(m.group(1))
            out.append(("  " if indent >= 4 else "") + clean_inline(m.group(2)))
    return [b for b in out if b.strip()]


def html_bullets(body):
    return [clean_inline(p) for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
            if clean_inline(p)]


def prose_lines(body):
    """Bare markdown paragraph lines (not bullets/tags/directives) -> bullet items.
    Fallback for content slides whose text isn't in `-` bullets or <p> tags."""
    out = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s[0] in '<#-*:' or s.startswith('---'):
            continue
        c = clean_inline(s)
        if c:
            out.append(c)
    return out


def html_table_rows(body):
    """Parse the first <table>'s <tr><th|td> cells into a list of row lists.
    Header (<thead>) comes first; inline tags / v-click attrs are stripped."""
    m = re.search(r'<table[^>]*>(.*?)</table>', body, re.S)
    if not m:
        return []
    rows = []
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', m.group(1), re.S):
        cells = [clean_inline(c) for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', tr, re.S)]
        if cells:
            rows.append(cells)
    return rows


def resolve(src, base):
    if not src:
        return None
    return os.path.join(base, src.replace('./public/', 'public/'))


def attrs(tag):
    return dict(re.findall(r'(\w+)="([^"]*)"', tag))


def _cards(body):
    """Return [(title, desc)] from <h3>title</h3> ... <p>desc</p> card blocks.
    Robust to both class="card" and Vue :class="[...]" bindings (we only call this
    on slides whose h3/p are all cards)."""
    out = []
    for h in re.finditer(r'<h3[^>]*>(.*?)</h3>', body, re.S):
        p = re.search(r'<p[^>]*>(.*?)</p>', body[h.end():], re.S)
        out.append((clean_inline(h.group(1)), clean_inline(p.group(1)) if p else ""))
    return out


def to_spec(fm, body, idx, base, png_dir):
    # ---- title (first slide) ----
    if idx == 0:
        h = re.search(r'^#\s+(.*)', body, re.M)
        sub = ""
        for l in body.splitlines():
            s = l.strip()
            if s and not s.startswith('#') and not s.startswith('<'):
                sub = clean_inline(s); break
        ps = [clean_inline(p) for p in re.findall(r'<p>(.*?)</p>', body)]
        return {"type": "title", "heading": clean_inline(h.group(1)) if h else "",
                "subheading": sub,
                "name": ps[0] if ps else "Tim Cadman",
                "role": ps[1] if len(ps) > 1 else "Senior Data Scientist"}

    heading, subheading = fm.get("heading", ""), fm.get("subheading", "")
    layout = fm.get("layout", "content")
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.S)  # drop scoped CSS

    def png():  # whole-slide fallback image for this slide
        return os.path.join(png_dir, f"{idx + 1}.png") if png_dir else None

    # ---- section divider (body is just `# Heading`): lift the H1 into the title ----
    if layout == "section":
        h = re.search(r'^#\s+(.*)', body, re.M)
        return {"type": "bullets", "heading": clean_inline(h.group(1)) if h else heading,
                "subheading": subheading, "bullets": []}

    # ---- ProcessCards component -> info cards (must precede the bespoke branch) ----
    m = re.search(r'<ProcessCards\b(.*?)/?>', body, re.S)
    if m:
        steps = re.findall(r"\{\s*title:\s*'([^']*)'\s*,\s*desc:\s*'([^']*)'", m.group(1))
        return {"type": "cards", "heading": heading, "subheading": subheading,
                "cards": [(clean_inline(t), clean_inline(d)) for t, d in steps],
                "columns": len(steps) or 2}

    # ---- LatencyStack (bespoke) -> a titled single figure (pre-rendered PNG) ----
    if re.search(r'<LatencyStack\b', body):
        return {"type": "figure", "heading": heading, "subheading": subheading,
                "image": resolve("./public/latency.png", base)}

    # ---- "Where the time goes" measurement cards (.mcard: name / desc / formula) ----
    if "mcard" in body:
        names = re.findall(r'class="mname"[^>]*>(.*?)</div>', body, re.S)
        descs = re.findall(r'class="mdesc"[^>]*>(.*?)</div>', body, re.S)
        cards = []
        for i, chunk in enumerate(body.split('<div class="mcard">')[1:]):
            mr = clean_inline(chunk.split('class="mr">', 1)[1]) if 'class="mr">' in chunk else ""
            name = clean_inline(names[i]) if i < len(names) else ""
            desc = clean_inline(descs[i]) if i < len(descs) else ""
            cards.append((name, " — ".join(x for x in (desc, mr) if x)))
        return {"type": "cards", "heading": heading, "subheading": subheading,
                "cards": cards, "columns": 2}

    # ---- HTML <table> (server/footprint/function tables) -> editable table ----
    if "<table" in body:
        return {"type": "table", "heading": heading, "subheading": subheading,
                "rows": html_table_rows(body)}

    # ---- figure slide: 1-2 chart PNGs in .res-figs/.fit, no <p> bullets ----
    if ("res-figs" in body or 'class="fit"' in body) and not html_bullets(body):
        figs = [resolve(s, base) for s in re.findall(r'<img[^>]*src="([^"]+)"', body)
                if "logo" not in s]
        if len(figs) >= 2:
            return {"type": "two_images", "heading": heading, "subheading": subheading,
                    "images": figs[:2]}
        if figs:
            return {"type": "figure", "heading": heading, "subheading": subheading,
                    "image": figs[0]}

    # ---- team slide: avatar grid + group photo are bespoke -> whole-slide image ----
    if "team-rows" in body or "team-grid" in body:
        return {"type": "slide_image", "image": png()}

    # ---- two-image slide ----
    if layout == "content-two-images":
        return {"type": "two_images", "heading": heading, "subheading": subheading,
                "images": [resolve(fm.get("imageLeft"), base), resolve(fm.get("imageRight"), base)]}

    # ---- bespoke Vue component (e.g. architecture diagram): whole-slide image ----
    if re.search(r'<[A-Z][A-Za-z0-9]+\s*/?>', body) and "DemoSlide" not in body:
        return {"type": "slide_image", "image": png()}

    # ---- DemoSlide component (other decks) ----
    m = re.search(r'<DemoSlide\b([^>]*?)/?>', body)
    if m:
        a = attrs(m.group(1))
        return {"type": "demo", "step": a.get("step", ""), "subheading": subheading,
                "image": resolve(a.get("image"), base), "text": a.get("text", "")}

    # ---- "deploy" two-card slide -> intro + cards ----
    if "deploy-card" in body:
        intro = re.search(r'<div style="font-size[^>]*>\s*(.*?)</div>', body, re.S)
        return {"type": "cards", "heading": heading, "subheading": subheading,
                "intro": clean_inline(intro.group(1)) if intro else "",
                "cards": _cards(body), "columns": 2}

    # ---- "potential advantages" cards (2x2 grid) ----
    if "adv-card" in body:
        return {"type": "cards", "heading": heading, "subheading": subheading,
                "cards": _cards(body), "columns": 2}

    # ---- Deployment Variants: variant/requirement bullets (left) + hardware table (right) ----
    if "hw-grid" in body:
        bul = md_bullets(body)
        headers = [clean_inline(h) for h in re.findall(r'<div class="h">(.*?)</div>', body, re.S)]
        cells = [clean_inline(c) for c in re.findall(r'<div class="c[^"]*">(.*?)</div>', body, re.S)]
        cols = len(headers) or 4
        rows = ([headers] if headers else []) + [cells[i:i + cols] for i in range(0, len(cells), cols)]
        return {"type": "bullets_table", "heading": heading, "subheading": subheading,
                "bullets": bul, "rows": rows, "table_title": "Hardware requirements"}

    # ---- legacy: journey grid / stack ----
    if "journey-grid" in body:
        c = [clean_inline(x) for x in re.findall(r'<div[^>]*class="cell[^"]*"[^>]*>(.*?)</div>', body, re.S)]
        rows = [["", "Challenge", "Solution"]] + [c[i:i + 3] for i in range(0, len(c), 3)]
        return {"type": "table", "heading": heading, "subheading": subheading, "rows": rows}
    if "stack-card" in body:
        names = re.findall(r'layer-name">(.*?)</span>', body, re.S)
        tools = re.findall(r'layer-tool">(.*?)</span>', body, re.S)
        return {"type": "stack", "heading": heading, "subheading": subheading,
                "rows": [(clean_inline(n), clean_inline(t)) for n, t in zip(names, tools)]}

    # ---- content + side image -> contained image (logos get no border) ----
    # type from LAYOUT_MAP; `pptx: photo` in frontmatter forces full-bleed instead.
    if layout in ("content-img-right", "content-img-left") and fm.get("image"):
        side = "right" if "right" in layout else "left"
        img = fm["image"]
        t = fm.get("pptx") or LAYOUT_MAP.get(layout, "image")
        spec = {"type": t, "side": side, "heading": heading, "subheading": subheading,
                "bullets": md_bullets(body), "image": resolve(img, base)}
        if t == "image":
            spec["border"] = "logo" not in img
        return spec

    # ---- legacy inline flex image + <p> bullets ----
    imgs = [s for s in re.findall(r'<img src="([^"]+)"', body) if "logo" not in s and "icon-" not in s]
    pbul = html_bullets(body)
    if imgs and pbul:
        return {"type": "image", "side": "left", "heading": heading, "subheading": subheading,
                "bullets": pbul, "image": resolve(imgs[0], base)}

    # ---- plain bullets (also handles bullets nested in a styling <div>) ----
    bul = md_bullets(body) or prose_lines(body)
    return {"type": "bullets", "heading": heading, "subheading": subheading, "bullets": bul}


def convert(md_path, out_path, png_dir=None):
    base = os.path.dirname(os.path.abspath(md_path))
    text = open(md_path).read()
    slides = split_slides(text)
    specs = [to_spec(fm, body, i, base, png_dir) for i, (fm, body) in enumerate(slides)]
    DeckBuilder().build(specs).save(out_path)
    print(f"converted {len(specs)} slides -> {out_path}")
    return specs


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "molgenis-demonstrator/slides.md"
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/demonstrator.pptx"
    pdir = sys.argv[3] if len(sys.argv) > 3 else None
    convert(os.path.join(ROOT, src) if not os.path.isabs(src) else src, out, pdir)
