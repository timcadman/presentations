#!/usr/bin/env bash
# Render a markdown file to a MOLGENIS-branded PDF.
# Usage: ./render.sh <input.md> [output.pdf]
# Title/author/date are taken from the markdown YAML header.
# Requires pandoc and typst on your PATH. Fonts are bundled in ./fonts.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

command -v pandoc >/dev/null || { echo "pandoc not found on PATH" >&2; exit 1; }
command -v typst  >/dev/null || { echo "typst not found on PATH"  >&2; exit 1; }

IN="$1"
OUT="${2:-${IN%.md}.pdf}"
IN="$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")"
mkdir -p "$(dirname "$OUT")"
OUT="$(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")"

BUILD="$DIR/.build"
mkdir -p "$BUILD"
trap 'rm -rf "$BUILD"' EXIT

pandoc "$IN" -t typst --template="$DIR/molgenis-doc.typ" -o "$BUILD/main.typ"
typst compile "$BUILD/main.typ" "$OUT" --root "$DIR" --font-path "$DIR/fonts"
echo "Rendered $OUT"
