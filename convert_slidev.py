"""
convert_slidev.py — strip a Slidev slides.md to plain content and render it as an
editable, branded PowerPoint via build_deck.DeckBuilder.

    python3 convert_slidev.py molgenis-armadillo/slides.md /tmp/out.pptx [slidev_png_dir]

slidev_png_dir (optional): folder of rendered Slidev PNGs (1.png..N.png), used as a
whole-slide fallback for slides that can't be made editable (bespoke Vue diagrams).
Produce it with:  npx slidev export slides.md --format png --output <dir>
"""
import os, re, sys
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
    t = re.sub(r'<.*?>', '', t)                      # any stray tags
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


def resolve(src, base):
    if not src:
        return None
    return os.path.join(base, src.replace('./public/', 'public/'))


def attrs(tag):
    return dict(re.findall(r'(\w+)="([^"]*)"', tag))


def _cards(body, cls):
    """Return [(title, desc)] for repeated card blocks of the given class."""
    out = []
    for blk in re.findall(r'class="[^"]*' + cls + r'[^"]*"[^>]*>(.*?</h3>.*?)(?=<div class="[^"]*' + cls + r'|\Z)', body, re.S):
        h = re.search(r'<h3[^>]*>(.*?)</h3>', blk, re.S)
        p = re.search(r'<p[^>]*>(.*?)</p>', blk, re.S)
        if h:
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

    def png():  # whole-slide fallback image for this slide
        return os.path.join(png_dir, f"{idx + 1}.png") if png_dir else None

    # ---- team slide: Armadillo names as bullets + group photo ----
    if "team-rows" in body or "team-grid" in body:
        names = re.findall(r'team-name">(.*?)</div>', body, re.S)
        roles = re.findall(r'team-role">(.*?)</div>', body, re.S)
        bul = [f"{clean_inline(n)} — {clean_inline(r)}" for n, r in zip(names, roles)]
        photo = re.search(r'<img src="(\./public/team_[^"]+)"', body)  # group photo (underscore), not the hyphen avatars
        return {"type": "photo", "side": "right", "heading": heading or "Our team",
                "subheading": subheading, "bullets": bul,
                "image": resolve(photo.group(1), base) if photo else None}

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

    # ---- "deploy" two-card slide -> intro + card bullets ----
    if "deploy-card" in body:
        intro = re.search(r'<div style="font-size[^>]*>\s*(.*?)</div>', body, re.S)
        bul = [clean_inline(intro.group(1))] if intro else []
        for title, desc in _cards(body, "deploy-card"):
            bul.append(f"{title} — {desc}" if desc else title)
        return {"type": "bullets", "heading": heading, "subheading": subheading,
                "bullets": [b for b in bul if b]}

    # ---- "potential advantages" cards -> bullets ----
    if "adv-card" in body:
        bul = [f"{t} — {d}" if d else t for t, d in _cards(body, "adv-card")]
        return {"type": "bullets", "heading": heading, "subheading": subheading, "bullets": bul}

    # ---- Deployment Variants: variant/requirement bullets + hardware table rows ----
    if "hw-grid" in body:
        bul = md_bullets(body)
        cells = [clean_inline(c) for c in re.findall(r'<div class="c[^"]*">(.*?)</div>', body, re.S)]
        for i in range(0, len(cells) - 3, 4):
            p, mem, disk, cpu = cells[i:i + 4]
            bul.append(f"  {p}: {mem} GB RAM, {disk} GB disk, {cpu} CPU cores")
        return {"type": "bullets", "heading": heading, "subheading": subheading, "bullets": bul}

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
    return {"type": "bullets", "heading": heading, "subheading": subheading, "bullets": md_bullets(body)}


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
