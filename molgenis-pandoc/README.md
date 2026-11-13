# MOLGENIS document template

Renders any markdown file to a MOLGENIS-branded A4 PDF, reusing the deck
branding: palette from `../COLOURS.md`, fonts from `../theme/styles/index.css`
(Bebas Neue headings, IBM Plex Mono subheadings/code, Nunito body), UMCG logo
bottom-left and MOLGENIS logo bottom-right as on the slides.

## Usage

```bash
./render.sh path/to/document.md              # writes path/to/document.pdf
./render.sh path/to/document.md out.pdf
```

Title, author and date come from the markdown YAML header:

```markdown
---
title: "My document"
author: "Tim Cadman (t.j.cadman@umcg.nl)"
date: "22 April 2025"
---
```

## Dependencies

`pandoc` and `typst` must be installed and on your `PATH`. Fonts are bundled in
`./fonts`, so nothing else needs installing.

## Files

- `molgenis-doc.typ` — pandoc→typst template carrying the branding
- `render.sh` — one-shot pipeline: pandoc (md → typst) then typst compile
- `molgenis-logo.png`, `umcg-logo.png` — copies of `../images/*` (typst can't
  reach outside its root, so they live here)
- `fonts/` — the three branding fonts (Bebas Neue, IBM Plex Mono, Nunito),
  bundled so the folder is self-contained
