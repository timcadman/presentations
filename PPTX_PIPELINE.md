# Slidev → editable PowerPoint pipeline

## Goal
Author talks in **Slidev** (the existing decks), then convert them to **native, editable
PowerPoint** that matches the MOLGENIS brand — by stripping the Slidev markdown to plain
content and pouring it into a hand-built `.pptx` template via a Python builder.
Everything is **self-verified by rendering to PDF/PNG** before showing the user (no blind edits).

## What's DONE
- **Renderer (no admin needed):**
  - LibreOffice at `~/Applications/LibreOffice.app/Contents/MacOS/soffice` (installed by copying the dmg's app into `~/Applications`, quarantine stripped).
  - PyMuPDF (`pip3 install --user pymupdf`) to rasterise PDF → PNG.
  - Render a pptx:
    ```bash
    ~/Applications/LibreOffice.app/Contents/MacOS/soffice --headless \
      -env:UserInstallation=file:///tmp/lo_profile --convert-to pdf --outdir /tmp deck.pptx
    python3 -c "import fitz;d=fitz.open('/tmp/deck.pdf');[d[i].get_pixmap(dpi=100).save(f'/tmp/p{i+1}.png') for i in range(d.page_count)]"
    ```
    Then view the PNGs with the Read tool.
- **Fonts** installed in `~/Library/Fonts`: **Bebas Neue, IBM Plex Mono, Nunito** (Google Fonts). Required for correct rendering.
- **Template:** `presentations/molgenis-template-STARTER.pptx` (10×5.625 in, 16:9). Regenerate with `presentations/build_template.py` (run from `molgenis-demonstrator/`; needs `/tmp/default-ref.pptx` = `pandoc --print-default-data-file reference.pptx > /tmp/default-ref.pptx`).
  - Layouts (exact names matter): **Title, Bullets, Section, Photo Right, Photo Left, Image Right, Image Left, Table**.
  - **Section** = divider slide: section-background gold `#F7D38C`, heading centred in blue, no logo (matches `theme/layouts/section.vue`).
  - **Photo \*** = full-bleed cover image (Slidev `content-img-*` style); **Image \*** = contained whole image with border (NCC feature-slide style).
  - Styling baked into layouts: titles **Bebas Neue #4285F4** (55pt on Title, 40pt content), subheadings **IBM Plex Mono #4285F4** (25/18pt), bullets **Nunito #000** (18pt), blue **accent bar** above titles, **MOLGENIS logo** bottom-right (bottom-left on Photo/Image where the image covers that corner), author name/role bottom-left on Title.
  - **Title model:** the TITLE placeholder carries heading (outline level 0) + subheading (outline level 1). The builder sets both.
- **Builder:** `presentations/build_deck.py` — `DeckBuilder` + slide-spec dicts. Types: `title, bullets, photo, image, table, stack, demo`. Run `python3 build_deck.py` → `/tmp/molgenis-demo.pptx` (sample deck). All 8 sample slides verified against references.
  - `stack` = the **full-stack** slide (5 gradient cards Local data→Analyse, integ_4).
  - `demo` = the **FAIR-card** demo slide (screenshot + 5-step tracker, the active step full-opacity, others 25% — matches `molgenis-demonstrator/components/DemoSlide.vue` and integ_12).
  - FAIR gradient (from DemoSlide.vue): Local data `#93c5fd` (dark text), Catalogue `#60a5fa`, Request `#3b82f6`, Access `#2563eb`, Analyse `#1e3a5f`.

## Reference decks (sources of truth)
- `~/Downloads/NCC MolgenisArmadillo.pptx` — **source of truth for title + general design** (render it; it's the molgenis-branded armadillo deck). **Ignore the integrate deck's title page.**
- `~/Downloads/integrate-demonstrator.pdf` — source for the **full-stack slide (page 4)** and the **demo FAIR-card slide (page 12)**.
- Slidev decks (`molgenis-demonstrator/`, `molgenis-armadillo/`) — **source of truth for Slidev-derived elements**; render with `npx slidev export slides.md --format png --range N`.
- Rule the user gave: *use both NCC and Slidev as references; each is authoritative for the elements that come from it.*

## Converter — DONE (`convert_slidev.py`)
`python3 convert_slidev.py molgenis-armadillo/slides.md /tmp/out.pptx [slidev_png_dir]`
Parses `slides.md`, strips HTML/Vue/markdown, emits `build_deck.py` specs, builds + saves.

**Layout → spec mapping** lives in the `LAYOUT_MAP` dict at the top of `convert_slidev.py`
— **this is the registry to extend when a new theme layout is added.** Current mapping:

| Slidev layout (`theme/layouts/`) | PPTX spec / template layout |
|---|---|
| `cover` (implicit first slide)   | `title` → **Title** |
| `content`                        | `bullets` → **Bullets** |
| `content-img-right`              | `image` (contained, right) → **Image Right**; `<img>`s in the body become a logo row under the bullets (SVGs are rendered to PNG) |
| `content-img-left`               | `image` (contained, left) → **Image Left** |
| `content-two-images`             | `two_images` (two contained, drawn on Bullets) |
| `content-two-cols`               | `photo` (left bullets + one plain right-hand image) → **Photo Right** |
| `chart-full`                     | `bullets`; in practice its body is bespoke, so see the rule below |
| `section`                        | `section` → **Section** (divider) |
| `default`                        | `bullets` |

**What stays editable, and what becomes a picture.** A slide converts to editable text only if
its body holds nothing but bullets/prose, the inline tags in `EDITABLE_TAGS`, and styling
`<div>` wrappers around them. Other markup (a Vue component, an `<img>`, a terminal, or a
`<div>` diagram with no text to keep) has no editable equivalent, so `has_bespoke_markup()`
sends the slide to `slide_image` (whole-slide PNG from `slidev_png_dir`). The converter warns and lists the slides if a PNG is missing. Content with a
native equivalent is listed in the special cases and never reaches this rule.

Body-pattern special cases (in `to_spec`) override the map: team grid → `photo` + name bullets;
`deploy-card`/`adv-card` → `bullets`; `hw-grid` → `bullets` (variants + hardware rows);
bespoke `<Component/>` (e.g. `DatashieldArchitectureFinal`) → `slide_image` (whole-slide PNG
from `slidev_png_dir`); `DemoSlide` → `demo`; legacy `journey-grid`/`stack-card` → `table`/`stack`;
`<VideoPlayer>` → `video` (playable clips side by side, labelled by the `<div>` before each);
`<StatTiles>`, `<ProcessCards>` and any class in `CARD_CLASSES` → `cards` (grid sized by
`grid_columns`).

**Videos** are embedded as H.264 `.mp4` with a first-frame poster, because PowerPoint on Windows
does not reliably play `.mov`. `build_deck.prepare_video` converts each clip once (cached in the
system temp dir) using `ffmpeg` from `PATH`, else a deck's `node_modules/ffmpeg-static`.

**Exporting the slide pictures.** Timed animations (simulated terminals, highlights) must have
finished, so wait before capturing:
`npx slidev export slides.md --format png --with-clicks --wait 15000 --timeout 120000 --output <dir>`

**Click builds.** With `--with-clicks` Slidev writes one picture per click state
(`009-01.png`, `009-02.png`, …). A picture slide shows its final state unless its frontmatter
has `pptxClicks: true`; it then becomes one PowerPoint slide per state, so pressing "next"
steps through the build (states that look identical to the one before are dropped). Editable
slides are always a single slide. Export the whole deck each time: Slidev empties the output
folder first, so a `--range` export would delete the other slides' pictures.

**Per-slide override:** add `pptx: photo` (or another spec type) to a slide's frontmatter to
force the treatment — e.g. full-bleed instead of the default contained image.
`imageScale`/`imageWidth`/`imageAlign` are Slidev-only (the PPTX Image/Photo layouts have fixed
geometry), so they're ignored by the converter.

**Verify before handing over:** render the pptx (LibreOffice → PDF → PNG) and the Slidev deck
(`npx slidev export slides.md --format png`) and compare slide-for-slide.

## Animated slides need a recording
Slides that run in the browser (simulated terminals with typed commands and timed output,
highlights keyed to that output, any other timed animation) cannot be reproduced in
PowerPoint: the pipeline can only place a still picture of them, or one picture per click.
For the PowerPoint version, screen-record the whole slide playing in Slidev (title included),
save the clip in the deck's `public/` folder and add `pptxVideo: ./public/<clip>.mov` to the
slide's frontmatter. The converter then places the recording full-slide (`slide_video`) in
place of the picture. Slidev ignores the key, so the live slide is unchanged.

## Gotchas
- LibreOffice prints `Task policy set failed` to stderr — harmless.
- pandoc CANNOT crop images / vary layout per slide — that's why we build with python-pptx, not pandoc, for the bespoke layouts. (Pandoc path was abandoned.)
- Always render & eyeball before declaring a layout correct.
