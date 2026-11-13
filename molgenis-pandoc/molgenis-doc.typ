// MOLGENIS document branding — pandoc typst template.
// Adapted from theme/styles/index.css (Slidev); palette from COLOURS.md.
// Rendered via render.sh; title/author/date come from the markdown YAML header.

#let mg-primary = rgb("#4285F4")
#let mg-accent = rgb("#0097A7")
#let mg-gold = rgb("#F7D38C")
#let mg-text = rgb("#333333")
#let mg-grey = rgb("#9AA0A6")
#let mg-code-bg = rgb("#F4F7FC")

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.6cm, x: 2.4cm),
  footer: grid(
    columns: (1fr, auto, 1fr),
    align: (left + horizon, center + horizon, right + horizon),
    image("../umcg-logo.png", height: 0.38cm),
    text(font: "IBM Plex Mono", size: 8pt, fill: mg-grey)[
      #context counter(page).display("1")
    ],
    image("../molgenis-logo.png", height: 0.55cm),
  ),
)

#set text(font: "Nunito", size: 10.5pt, fill: mg-text)
#set par(leading: 0.72em, justify: false)
#show par: set block(spacing: 1em)

#show heading.where(level: 1): it => block(above: 1.9em, below: 0.9em)[
  #text(font: "Bebas Neue", weight: "regular", size: 19pt, fill: mg-primary)[#it.body]
  #v(-0.55em)
  #line(length: 100%, stroke: 1.5pt + mg-primary)
]

#show heading.where(level: 2): it => block(above: 1.5em, below: 0.7em)[
  #text(font: "IBM Plex Mono", weight: 600, size: 11pt, fill: mg-primary)[#it.body]
]

#show link: it => text(fill: mg-accent)[#it]

#show raw.where(block: true): it => block(
  width: 100%,
  fill: mg-code-bg,
  stroke: (left: 2.5pt + mg-accent),
  inset: (x: 12pt, y: 10pt),
  radius: 3pt,
  text(font: "IBM Plex Mono", size: 8.5pt, it),
)

#show raw.where(block: false): it => box(
  fill: mg-code-bg,
  inset: (x: 3pt, y: 0pt),
  outset: (y: 3pt),
  radius: 2pt,
  text(font: "IBM Plex Mono", size: 8.5pt, it),
)

#show table: set text(size: 9.5pt)
#set table(
  stroke: (x, y) => if y == 0 { (bottom: 2pt + mg-primary) } else { (bottom: 0.5pt + rgb("#e3e8f2")) },
  inset: (x: 10pt, y: 7pt),
)
#show table.cell.where(y: 0): it => text(font: "IBM Plex Mono", weight: 600, fill: mg-primary, it)

// Title block
$if(title)$
#text(font: "Bebas Neue", size: 30pt, fill: mg-primary)[$title$]
#v(0.1em)
$endif$
#text(font: "IBM Plex Mono", size: 9pt, fill: mg-grey)[$for(author)$$author$$sep$ · $endfor$$if(date)$ · $date$$endif$]
#v(1.2em)

$body$
