"""
convert_slidev.py — strip a Slidev slides.md to plain content and render it as an
editable, branded PowerPoint via build_deck.DeckBuilder.

    python3 convert_slidev.py molgenis-demonstrator/slides.md /tmp/out.pptx
"""
import os, re, sys
from build_deck import DeckBuilder

ROOT = os.path.dirname(os.path.abspath(__file__))


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
    # parts[0]='', parts[1]=headmatter, parts[2]=slide1 body, then (fm, body) pairs
    slides = [({}, parts[2])]
    i = 3
    while i < len(parts):
        fm = parse_frontmatter(parts[i])
        body = parts[i + 1] if i + 1 < len(parts) else ""
        slides.append((fm, body))
        i += 2
    return slides


def md_bullets(body):
    out = []
    for line in body.splitlines():
        m = re.match(r'\s*[-*]\s+(.*)', line)
        if m:
            t = re.sub(r'\*\*?(.*?)\*\*?', r'\1', m.group(1)).strip()  # drop * emphasis
            out.append(t)
    return out


def html_bullets(body):
    return [re.sub(r'<.*?>', '', re.sub(r'^[•\s]+', '', p)).strip()
            for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)]


def resolve(src, base):
    if not src:
        return None
    return os.path.join(base, src.replace('./public/', 'public/'))


def attrs(tag):
    return dict(re.findall(r'(\w+)="([^"]*)"', tag))


def to_spec(fm, body, first, base):
    if first:
        h = re.search(r'^#\s+(.*)', body, re.M)
        lines = [l.strip() for l in body.splitlines() if l.strip() and not l.strip().startswith('#') and '<' not in l]
        ps = [re.sub(r'<.*?>', '', p).strip() for p in re.findall(r'<p>(.*?)</p>', body)]
        return {"type": "title", "heading": h.group(1).strip() if h else "",
                "subheading": lines[0] if lines else "",
                "name": ps[0] if ps else "Tim Cadman",
                "role": ps[1] if len(ps) > 1 else "Senior Data Scientist"}

    heading, subheading = fm.get("heading", ""), fm.get("subheading", "")
    layout = fm.get("layout", "content")

    m = re.search(r'<DemoSlide\b([^>]*?)/?>', body)
    if m:
        a = attrs(m.group(1))
        return {"type": "demo", "step": a.get("step", ""), "subheading": subheading,
                "image": resolve(a.get("image"), base), "text": a.get("text", "")}

    if "journey-grid" in body:
        cells = [re.sub(r'<.*?>', '', c).strip()
                 for c in re.findall(r'<div[^>]*class="cell[^"]*"[^>]*>(.*?)</div>', body, re.S)]
        rows = [["", "Challenge", "Solution"]] + [cells[i:i + 3] for i in range(0, len(cells), 3)]
        return {"type": "table", "heading": heading, "subheading": subheading, "rows": rows}

    if "stack-card" in body:
        names = re.findall(r'layer-name">(.*?)</span>', body, re.S)
        tools = re.findall(r'layer-tool">(.*?)</span>', body, re.S)
        rows = [(n.strip(), t.strip()) for n, t in zip(names, tools)]
        return {"type": "stack", "heading": heading, "subheading": subheading, "rows": rows}

    if layout in ("content-img-right", "content-img-left") and fm.get("image"):
        side = "right" if "right" in layout else "left"
        return {"type": "photo", "side": side, "heading": heading, "subheading": subheading,
                "bullets": md_bullets(body), "image": resolve(fm["image"], base)}

    # inline flex image + <p> bullets  (feature slides -> contained image left)
    imgs = [s for s in re.findall(r'<img src="([^"]+)"', body)
            if "logo" not in s and "icon-" not in s]
    pbul = html_bullets(body)
    if imgs and pbul:
        return {"type": "image", "side": "left", "heading": heading, "subheading": subheading,
                "bullets": pbul, "image": resolve(imgs[0], base)}

    # centered quote (Demo / Research question)
    if "italic" in body and "<p" in body:
        q = re.search(r'<p[^>]*>(.*?)</p>', body, re.S)
        return {"type": "bullets", "heading": heading, "subheading": subheading,
                "bullets": [re.sub(r'<.*?>', '', q.group(1)).strip()] if q else []}

    return {"type": "bullets", "heading": heading, "subheading": subheading, "bullets": md_bullets(body)}


def convert(md_path, out_path):
    base = os.path.dirname(os.path.abspath(md_path))
    text = open(md_path).read()
    slides = split_slides(text)
    specs = [to_spec(fm, body, i == 0, base) for i, (fm, body) in enumerate(slides)]
    DeckBuilder().build(specs).save(out_path)
    print(f"converted {len(specs)} slides -> {out_path}")
    return specs


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "molgenis-demonstrator/slides.md"
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/demonstrator.pptx"
    convert(os.path.join(ROOT, src) if not os.path.isabs(src) else src, out)
