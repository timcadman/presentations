"""
build_deck.py — generate an editable, branded MOLGENIS PowerPoint from slide specs.

All styling (fonts, colours, accent bars, logo, layout geometry) lives in the
template (molgenis-template-STARTER.pptx). This builder only routes content into
the template's layouts and draws the two card-based slides (full-stack, demo).

Usage:
    python3 build_deck.py            # builds /tmp/molgenis-demo.pptx from DEMO_DECK

Each slide is a dict with a "type":
  {"type":"title",   "heading":..., "subheading":..., "name":..., "role":...}
  {"type":"bullets", "heading":..., "subheading":..., "bullets":[...]}
  {"type":"section", "heading":..., "subheading":...}
  {"type":"photo",   "side":"right"|"left", "heading":..., "subheading":..., "bullets":[...], "image":path}
  {"type":"image",   "side":"right"|"left", "heading":..., "subheading":..., "bullets":[...], "image":path,
                     "logos":[path,...]}   # optional row of small logos under the bullets
  {"type":"table",   "heading":..., "subheading":..., "rows":[[...],...]}
  {"type":"stack",   "heading":..., "subheading":..., "rows":[(label,desc),...]}
  {"type":"demo",    "step":..., "image":path, "text":...}
  {"type":"video",   "heading":..., "subheading":..., "videos":[{"path":..., "label":...}]}
  {"type":"slide_video", "video":path}
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from pptx.enum.shapes import MSO_SHAPE, PP_PLACEHOLDER
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree
from PIL import Image as PImage
import glob, hashlib, os, shutil, subprocess, tempfile

TEMPLATE = os.path.join(os.path.dirname(__file__), "molgenis-template-STARTER.pptx")
ASSET_ROOT = os.path.dirname(__file__)
BLACK = RGBColor(0x22, 0x22, 0x22)
BLUE_HEX = "4285F4"
GREY = RGBColor(0x44, 0x44, 0x44)
# FAIR gradient (from DemoSlide.vue): label, fill hex, text hex
GRAD = [("Local data", "93c5fd", "ffffff"), ("Catalogue", "60a5fa", "ffffff"),
        ("Request", "3b82f6", "ffffff"), ("Access", "2563eb", "ffffff"),
        ("Analyse", "1e3a5f", "ffffff")]


def find_ffmpeg():
    """ffmpeg on PATH, else the ffmpeg-static binary a deck has installed."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    bundled = sorted(glob.glob(os.path.join(ASSET_ROOT, "*", "node_modules", "ffmpeg-static", "ffmpeg")))
    if not bundled:
        raise RuntimeError("ffmpeg not found: install it, or `npm i ffmpeg-static` in a deck")
    return bundled[0]


def prepare_video(path):
    """Return (mp4, poster_png) for a clip, converting once and reusing the result.

    PowerPoint on Windows does not reliably play QuickTime .mov, so every clip
    is embedded as H.264 .mp4; the poster is the frame shown before playback.
    """
    stat = os.stat(path)
    key = hashlib.sha1(f"{path}:{stat.st_mtime_ns}:{stat.st_size}".encode()).hexdigest()[:16]
    cache = os.path.join(tempfile.gettempdir(), "slidev_pptx_media")
    os.makedirs(cache, exist_ok=True)
    mp4, poster = os.path.join(cache, key + ".mp4"), os.path.join(cache, key + ".png")
    ffmpeg = find_ffmpeg()
    if not os.path.exists(mp4):
        subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-i", path, "-an", "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
                        "-movflags", "+faststart", mp4], check=True)
    if not os.path.exists(poster):
        subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-i", mp4, "-frames:v", "1", poster],
                       check=True)
    return mp4, poster


def as_raster(path):
    """Path to a picture PowerPoint can embed: an SVG is rendered once to a cached PNG."""
    if not path.lower().endswith(".svg"):
        return path
    import fitz  # PyMuPDF, already required by the pipeline to check its output
    stat = os.stat(path)
    key = hashlib.sha1(f"{path}:{stat.st_mtime_ns}:{stat.st_size}".encode()).hexdigest()[:16]
    cache = os.path.join(tempfile.gettempdir(), "slidev_pptx_media")
    os.makedirs(cache, exist_ok=True)
    png = os.path.join(cache, key + ".png")
    if not os.path.exists(png):
        fitz.open(path)[0].get_pixmap(dpi=300, alpha=True).save(png)
    return png


def _sub(parent, tag, **a):
    e = etree.SubElement(parent, qn(tag))
    for k, v in a.items():
        e.set(k, v)
    return e


class DeckBuilder:
    def __init__(self, template=TEMPLATE):
        self.prs = Presentation(template)

    # ---- helpers ----
    def _layout(self, name):
        for l in self.prs.slide_layouts:
            if l.name == name:
                return l
        raise KeyError(f"layout {name!r} not in template")

    @staticmethod
    def _ph(slide, ptype):
        for p in slide.placeholders:
            if p.placeholder_format.type == ptype:
                return p
        return None

    def _title_sub(self, slide, heading, subheading):
        ph = self._ph(slide, PP_PLACEHOLDER.TITLE) or self._ph(slide, PP_PLACEHOLDER.CENTER_TITLE)
        tf = ph.text_frame
        tf.clear()
        tf.paragraphs[0].add_run().text = heading or ""
        if subheading:
            p = tf.add_paragraph(); p.level = 1; p.add_run().text = subheading

    def _bullets(self, ph, items):
        tf = ph.text_frame; tf.clear()
        for i, it in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.level = 0; p.add_run().text = it

    def _fit_picture(self, slide, ph, img, border=True, scale=1.0, valign="top"):
        """Contain-fit an image inside the placeholder's rect (no crop).
        scale<1 shrinks within the rect; valign 'top' keeps the fixed top, 'middle' centres."""
        L, T, W, H = ph.left, ph.top, ph.width, ph.height
        ph._element.getparent().remove(ph._element)
        iw, ih = PImage.open(img).size
        ar, AR = iw / ih, W / H
        if ar > AR:
            w = int(W * scale); h = int(W * scale / ar)
        else:
            h = int(H * scale); w = int(H * scale * ar)
        x = int(L + (W - w) / 2)
        y = int(T) if valign == "top" else int(T + (H - h) / 2)
        pic = slide.shapes.add_picture(img, x, y, w, h)
        if border:
            pic.line.color.rgb = RGBColor(0xD9, 0xD9, 0xD9); pic.line.width = Pt(1)
        return pic

    # ---- slide types ----
    def title(self, heading, subheading="", name="Tim Cadman", role="Senior Data Scientist", **_):
        s = self.prs.slides.add_slide(self._layout("Title"))
        self._title_sub(s, heading, subheading)
        # editable name/role text box bottom-left
        tb = s.shapes.add_textbox(Inches(0.7), self.prs.slide_height - Inches(1.05), Inches(4), Inches(0.8))
        tf = tb.text_frame
        r = tf.paragraphs[0].add_run(); r.text = name
        r.font.bold = True; r.font.size = Pt(14); r.font.name = "Nunito"; r.font.color.rgb = BLACK
        if role:
            p = tf.add_paragraph(); r = p.add_run(); r.text = role
            r.font.size = Pt(11); r.font.name = "Nunito"; r.font.color.rgb = BLACK
        return s

    def bullets(self, heading, subheading="", bullets=(), **_):
        s = self.prs.slides.add_slide(self._layout("Bullets"))
        self._title_sub(s, heading, subheading)
        self._bullets(self._ph(s, PP_PLACEHOLDER.OBJECT), bullets)
        return s

    def section(self, heading, subheading="", **_):
        """Divider between parts of the talk: heading centred on the section colour."""
        s = self.prs.slides.add_slide(self._layout("Section"))
        self._title_sub(s, heading, subheading)
        return s

    def photo(self, side, heading, subheading="", bullets=(), image=None, **_):
        s = self.prs.slides.add_slide(self._layout(f"Photo {side.capitalize()}"))
        self._title_sub(s, heading, subheading)
        self._bullets(self._ph(s, PP_PLACEHOLDER.BODY) or self._ph(s, PP_PLACEHOLDER.OBJECT), bullets)
        if image:
            self._ph(s, PP_PLACEHOLDER.PICTURE).insert_picture(image)  # cover/crop = full-bleed
        return s

    def _logo_row(self, s, logos, left, top, height=Inches(0.3), gap=Inches(0.2)):
        """Small logos side by side at a common height, starting at (left, top)."""
        x = left
        for logo in logos:
            picture = as_raster(logo)
            w, h = PImage.open(picture).size
            width = int(height * w / h)
            s.shapes.add_picture(picture, x, top, width, height)
            x += width + gap

    def image(self, side, heading, subheading="", bullets=(), image=None, border=True, logos=(), **_):
        s = self.prs.slides.add_slide(self._layout(f"Image {side.capitalize()}"))
        self._title_sub(s, heading, subheading)
        if logos:
            body = self._ph(s, PP_PLACEHOLDER.BODY)
            self._logo_row(s, logos, body.left, body.top + body.height + Inches(0.1))
        # screenshot is top-aligned in its region; bullets sit at the layout's fixed top.
        # both share the same top point and the layout height never changes per slide.
        if image:
            # logos (border=False) read better smaller and vertically centred
            kw = dict(border=False, scale=0.62, valign="middle") if not border else {}
            self._fit_picture(s, self._ph(s, PP_PLACEHOLDER.PICTURE), image, **kw)
        self._bullets(self._ph(s, PP_PLACEHOLDER.BODY), bullets)
        return s

    def two_images(self, heading, subheading="", images=(), **_):
        s = self.prs.slides.add_slide(self._layout("Bullets"))
        self._title_sub(s, heading, subheading)
        ph = self._ph(s, PP_PLACEHOLDER.OBJECT) or self._ph(s, PP_PLACEHOLDER.BODY)
        if ph is not None:
            ph._element.getparent().remove(ph._element)
        top, gap, margin = Inches(2.0), Inches(0.4), Inches(0.7)
        bottom = self.prs.slide_height - Inches(0.6)
        H = bottom - top
        halfW = int((self.prs.slide_width - margin * 2 - gap) / 2)
        imgs = [i for i in images if i][:2]
        for i, img in enumerate(imgs):
            iw, ih = PImage.open(img).size
            ar, AR = iw / ih, halfW / H
            if ar > AR:
                w = halfW; h = int(halfW / ar)
            else:
                h = int(H); w = int(H * ar)
            x = int(margin) + i * (halfW + int(gap)) + (halfW - w) // 2
            pic = s.shapes.add_picture(img, x, int(top), w, h)
            pic.line.color.rgb = RGBColor(0xD9, 0xD9, 0xD9); pic.line.width = Pt(1)
        return s

    def slide_image(self, images=(), **_):
        """Whole-slide image fallback for slides that can't be made editable
        (e.g. a bespoke Vue diagram). Each image already contains its own title;
        several images are the slide's click states and become consecutive slides."""
        for image in list(images) or [None]:
            s = self.prs.slides.add_slide(self._layout("Bullets"))
            for p in list(s.placeholders):
                p._element.getparent().remove(p._element)
            if image:
                s.shapes.add_picture(image, 0, 0, self.prs.slide_width, self.prs.slide_height)
        return s

    def video(self, heading, subheading="", videos=(), **_):
        """Playable clips side by side under the title, each with an optional label."""
        s = self.prs.slides.add_slide(self._layout("Table"))
        self._title_sub(s, heading, subheading)
        margin, gap, top, bottom = 0.7, 0.3, 2.1, 5.25
        label_h = 0.35 if any(v.get("label") for v in videos) else 0.0
        cell_w = (10.0 - 2 * margin - (len(videos) - 1) * gap) / max(len(videos), 1)
        cell_h = bottom - top - label_h
        for i, clip in enumerate(videos):
            x = margin + i * (cell_w + gap)
            if clip.get("label"):
                tb = s.shapes.add_textbox(Inches(x), Inches(top), Inches(cell_w), Inches(label_h))
                r = tb.text_frame.paragraphs[0].add_run(); r.text = clip["label"]
                r.font.bold = True; r.font.size = Pt(14); r.font.name = "IBM Plex Mono"
                r.font.color.rgb = RGBColor.from_string(BLUE_HEX)
            mp4, poster = prepare_video(clip["path"])
            pw, ph = PImage.open(poster).size
            scale = min(cell_w / pw, cell_h / ph)
            s.shapes.add_movie(mp4, Inches(x), Inches(top + label_h), Inches(pw * scale),
                               Inches(ph * scale), poster_frame_image=poster, mime_type="video/mp4")
        return s

    def slide_video(self, video, **_):
        """A recording of the whole slide, filling the slide (it shows its own title)."""
        s = self.prs.slides.add_slide(self._layout("Bullets"))
        for p in list(s.placeholders):
            p._element.getparent().remove(p._element)
        mp4, poster = prepare_video(video)
        pw, ph = PImage.open(poster).size
        scale = min(self.prs.slide_width / pw, self.prs.slide_height / ph)
        w, h = int(pw * scale), int(ph * scale)
        s.shapes.add_movie(mp4, (self.prs.slide_width - w) // 2, (self.prs.slide_height - h) // 2,
                           w, h, poster_frame_image=poster, mime_type="video/mp4")
        return s

    def _infobox(self, s, x, y, w, h, title, desc):
        """A bordered rounded card with a blue left accent, blue title, grey body
        (matches the Slidev deploy-card / adv-card style)."""
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        try: box.adjustments[0] = 0.06
        except Exception: pass
        box.fill.solid(); box.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        box.line.color.rgb = RGBColor(0xDD, 0xDD, 0xDD); box.line.width = Pt(1.5)
        box.shadow.inherit = False
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.07), Inches(h))
        bar.fill.solid(); bar.fill.fore_color.rgb = RGBColor.from_string(BLUE_HEX)
        bar.line.fill.background(); bar.shadow.inherit = False
        tf = box.text_frame; tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.12); tf.vertical_anchor = MSO_ANCHOR.TOP
        r = tf.paragraphs[0].add_run(); r.text = title
        r.font.bold = True; r.font.size = Pt(15); r.font.name = "Nunito"; r.font.color.rgb = RGBColor.from_string(BLUE_HEX)
        if desc:
            p = tf.add_paragraph(); p.space_before = Pt(4)
            r = p.add_run(); r.text = desc; r.font.size = Pt(12); r.font.name = "Nunito"; r.font.color.rgb = GREY
        return box

    def cards(self, heading, subheading="", cards=(), intro="", columns=2, **_):
        """Grid of info cards (deploy comparison, potential-advantages grid)."""
        s = self.prs.slides.add_slide(self._layout("Table"))
        self._title_sub(s, heading, subheading)
        top = 2.2
        if intro:
            tb = s.shapes.add_textbox(Inches(0.7), Inches(top - 0.05), Inches(8.6), Inches(0.6))
            tb.text_frame.word_wrap = True
            r = tb.text_frame.paragraphs[0].add_run(); r.text = intro
            r.font.name = "Nunito"; r.font.size = Pt(14); r.font.color.rgb = BLACK
            top += 0.7
        cards = list(cards)
        n = len(cards) or 1
        cols = min(columns, n); rows = (n + cols - 1) // cols
        margin, gap = 0.7, 0.3
        cw = (10.0 - 2 * margin - (cols - 1) * gap) / cols
        ch = (5.625 - top - 0.45 - (rows - 1) * gap) / rows
        for i, (title, desc) in enumerate(cards):
            cx = margin + (i % cols) * (cw + gap)
            cy = top + (i // cols) * (ch + gap)
            self._infobox(s, cx, cy, cw, ch, title, desc)
        return s

    def bullets_table(self, heading, subheading="", bullets=(), rows=(), table_title="", **_):
        """Bullets on the left, a data table on the right (Deployment variants)."""
        s = self.prs.slides.add_slide(self._layout("Bullets"))
        self._title_sub(s, heading, subheading)
        o = self._ph(s, PP_PLACEHOLDER.OBJECT)
        o.left, o.top, o.width, o.height = Inches(0.7), Inches(2.35), Inches(4.4), Inches(2.7)
        self._bullets(o, bullets)
        rx, ry = 5.35, 2.2
        if table_title:
            tb = s.shapes.add_textbox(Inches(rx), Inches(ry), Inches(4.0), Inches(0.4))
            r = tb.text_frame.paragraphs[0].add_run(); r.text = table_title
            r.font.bold = True; r.font.size = Pt(13); r.font.name = "Nunito"
            r.font.color.rgb = RGBColor.from_string(BLUE_HEX)
            ry += 0.5
        if rows:
            rr, cc = len(rows), len(rows[0])
            t = s.shapes.add_table(rr, cc, Inches(rx), Inches(ry), Inches(4.0), Inches(0.45 * rr)).table
            for ri, row in enumerate(rows):
                for ci, val in enumerate(row):
                    cell = t.cell(ri, ci); cell.text = str(val)
                    for para in cell.text_frame.paragraphs:
                        for run in para.runs:
                            run.font.size = Pt(11); run.font.name = "Nunito"
        return s

    def table(self, heading, subheading="", rows=(), **_):
        s = self.prs.slides.add_slide(self._layout("Table"))
        self._title_sub(s, heading, subheading)
        r, c = len(rows), len(rows[0])
        t = s.shapes.add_table(r, c, Inches(0.7), Inches(2.35), Inches(8.6), Inches(2.5)).table
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                t.cell(ri, ci).text = str(val)
        return s

    def stack(self, heading, subheading="", rows=None, **_):
        rows = rows or [(g[0], "") for g in GRAD]
        s = self.prs.slides.add_slide(self._layout("Table"))
        self._title_sub(s, heading, subheading)
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(2.15), Inches(5.2), Inches(2.95))
        box.fill.solid(); box.fill.fore_color.rgb = RGBColor(0xEE, 0xF1, 0xF4)
        box.line.fill.background(); box.shadow.inherit = False
        cy = 2.32
        for (label, desc), (_, hexv, _t) in zip(rows, GRAD):
            self._card(s, 0.95, cy, 4.7, 0.48, hexv, label, RGBColor(0xff, 0xff, 0xff), 100000, desc)
            cy += 0.54
        return s

    def demo(self, step, image=None, text="", subheading=None, **_):
        s = self.prs.slides.add_slide(self._layout("Table"))
        self._title_sub(s, "Demo", subheading if subheading is not None else step)
        tb = s.shapes.add_textbox(Inches(0.7), Inches(2.05), Inches(8.5), Inches(0.5))
        r = tb.text_frame.paragraphs[0].add_run(); r.text = text
        r.font.name = "Nunito"; r.font.size = Pt(15); r.font.color.rgb = BLACK
        fx, fy, fw, fh = 0.7, 2.65, 5.6, 2.5
        frame = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(fx), Inches(fy), Inches(fw), Inches(fh))
        frame.fill.solid(); frame.fill.fore_color.rgb = RGBColor(0xF2, 0xF4, 0xF7); frame.shadow.inherit = False
        frame.line.color.rgb = RGBColor(0xCC, 0xCC, 0xCC); frame.line.width = Pt(1.5)
        _sub(frame._element.spPr.find(qn('a:ln')), 'a:prstDash').set('val', 'dash')
        if image:
            iw, ih = PImage.open(image).size; ar, AR = iw / ih, fw / fh
            if ar > AR: w = fw - 0.2; h = w / ar
            else: h = fh - 0.2; w = h * ar
            s.shapes.add_picture(image, Inches(fx + (fw - w) / 2), Inches(fy + (fh - h) / 2), Inches(w), Inches(h))
        cy = 2.65
        for label, hexv, txc in GRAD:
            active = (label == step)
            self._card(s, 6.5, cy, 2.8, 0.42, hexv, label, RGBColor.from_string(txc),
                       100000 if active else 25000, "", active)
            cy += 0.47
        return s

    def _card(self, s, x, y, w, h, hexv, label, txt_col, alpha, desc="", active=True):
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        try: sh.adjustments[0] = 0.2
        except Exception: pass
        sh.shadow.inherit = False
        spPr = sh._element.spPr
        st = sh._element.find(qn('p:style'));  sh._element.remove(st) if st is not None else None
        for tag in ('a:solidFill', 'a:noFill'):
            e = spPr.find(qn(tag));  spPr.remove(e) if e is not None else None
        f = etree.Element(qn('a:solidFill')); c = _sub(f, 'a:srgbClr', val=hexv)
        if alpha < 100000: _sub(c, 'a:alpha', val=str(alpha))
        spPr.find(qn('a:prstGeom')).addnext(f)
        ln = spPr.find(qn('a:ln')) or _sub(spPr, 'a:ln')
        for e in list(ln): ln.remove(e)
        _sub(ln, 'a:noFill')
        lt = s.shapes.add_textbox(Inches(x + 0.18), Inches(y), Inches(w * 0.55), Inches(h))
        lt.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        r = lt.text_frame.paragraphs[0].add_run(); r.text = label
        r.font.bold = True; r.font.size = Pt(12); r.font.name = "Nunito"
        r.font.color.rgb = txt_col                                    # correct XML placement
        if alpha < 100000:
            srgb = r._r.find(qn('a:rPr')).find(qn('a:solidFill')).find(qn('a:srgbClr'))
            _sub(srgb, 'a:alpha', val='35000')
        if desc:
            dt = s.shapes.add_textbox(Inches(x + w * 0.4), Inches(y), Inches(w * 0.57), Inches(h))
            dt.text_frame.word_wrap = True; dt.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = dt.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
            r = p.add_run(); r.text = desc; r.font.italic = True; r.font.size = Pt(11)
            r.font.color.rgb = RGBColor(0xff, 0xff, 0xff); r.font.name = "Nunito"

    def build(self, deck):
        for spec in deck:
            t = spec["type"]
            if t == "title": self.title(**spec)
            elif t == "bullets": self.bullets(**spec)
            elif t == "section": self.section(**spec)
            elif t == "photo": self.photo(**spec)
            elif t == "image": self.image(**spec)
            elif t == "two_images": self.two_images(**spec)
            elif t == "slide_image": self.slide_image(**spec)
            elif t == "cards": self.cards(**spec)
            elif t == "bullets_table": self.bullets_table(**spec)
            elif t == "table": self.table(**spec)
            elif t == "stack": self.stack(**spec)
            elif t == "demo": self.demo(**spec)
            elif t == "video": self.video(**spec)
            elif t == "slide_video": self.slide_video(**spec)
            else: raise ValueError(f"unknown slide type {t!r}")
        return self.prs


def _p(rel):  # resolve a public asset path
    return os.path.join(ASSET_ROOT, "molgenis-demonstrator", rel)


DEMO_DECK = [
    {"type": "title", "heading": "From Data Discovery to Federated Analysis",
     "subheading": "Supporting the Research Journey"},
    {"type": "bullets", "heading": "Our approach", "subheading": "One open stack",
     "bullets": ["Harmonise data to established standards", "Make collections discoverable",
                 "Federated analysis — data never moves"]},
    {"type": "stack", "heading": "Our approach", "subheading": "One open stack — same at every scale",
     "rows": [("Local data", "Harmonise to established standards"), ("Catalogue", "MOLGENIS meta-data catalogue"),
              ("Request", "BBMRI-ERIC Negotiator"), ("Access", "LS AAI + OIDC"),
              ("Analyse", "DataSHIELD + Molgenis Armadillo")]},
    {"type": "image", "side": "left", "heading": "Features", "subheading": "Manage projects and data",
     "bullets": ["Data are grouped into projects", "Each project can be shared with users",
                 "Admins manage projects from the UI"],
     "image": os.path.join(ASSET_ROOT, "molgenis-armadillo/public/ui-projects.png")},
    {"type": "photo", "side": "right", "heading": "The problem", "subheading": "A fragmented researcher journey",
     "bullets": ["Large quantities of existing data", "Combining sources boosts power",
                 "Fragmented landscape to reuse data"],
     "image": _p("public/screenshot-combining-data.jpeg")},
    {"type": "demo", "step": "Catalogue", "image": _p("public/screenshot-catalogue-search.png"),
     "text": "Search for birth cohorts with relevant harmonised data"},
    {"type": "demo", "step": "Analyse", "image": _p("public/screenshot-forest-plot.jpg"),
     "text": "Preliminary results: mode of delivery and postpartum depression"},
    {"type": "table", "heading": "Armadillo vs Opal", "subheading": "Two DataSHIELD servers",
     "rows": [["Feature", "Armadillo", "Opal"], ["Storage", "Parquet files", "Relational DB"],
              ["Deployment", "Lightweight", "Heavier"]]},
]

if __name__ == "__main__":
    out = "/tmp/molgenis-demo.pptx"
    DeckBuilder().build(DEMO_DECK).save(out)
    print("wrote", out)
