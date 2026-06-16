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
  - Layouts (exact names matter): **Title, Bullets, Photo Right, Photo Left, Image Right, Image Left, Table**.
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

## What's LEFT — the main remaining task
**Write the Slidev → spec converter.** Parse `molgenis-demonstrator/slides.md` (and `molgenis-armadillo/slides.md`) and emit `build_deck.py` slide specs, stripping all HTML/Vue:
- Frontmatter `layout:` + `heading:`/`subheading:` → slide type + title/subheading.
  - `layout: content` → `bullets` (or `image`/`photo` if it has a side image).
  - `content-img-right` / `content-img-left` → `photo` (full-bleed) **or** `image` (contained) — these decks mostly use full-bleed (`object-fit: cover`), but screenshots read better contained; let the user choose per slide or by image type.
  - `<DemoSlide step=.. image=.. text=..>` → `demo` (step drives the highlight + colour).
  - markdown/HTML tables → `table`; the "one open stack" slide → `stack`.
- Convert markdown bullets (incl. nested) to the `bullets` list; resolve `./public/...` image paths.
- Drop Slidev-only constructs (v-click, custom components other than DemoSlide, `<style>` blocks).
Then: `specs → DeckBuilder().build(specs).save(out)` → render → verify → hand over.

## Open question to confirm with user
- Per-slide image treatment default: **contained (Image)** vs **full-bleed (Photo)**. They said "we need both" — converter should pick a sensible default (contained for screenshots) and allow override.

## Gotchas
- LibreOffice prints `Task policy set failed` to stderr — harmless.
- pandoc CANNOT crop images / vary layout per slide — that's why we build with python-pptx, not pandoc, for the bespoke layouts. (Pandoc path was abandoned.)
- Always render & eyeball before declaring a layout correct.
