<template>
  <div style="position: relative; margin-top: 1rem;">

    <!-- Single caption location: one line, centered, changes with each click.
         Each line is wrapped in its own v-click parent (visibility) with
         v-click-hide on the inner <p> (when it should disappear again) —
         combining both directives on one element breaks the "hidden until
         clicked" half, so they must stay on separate nested elements. -->
    <div class="caption-box">
      <div v-click="1"><p v-click-hide="2" class="caption-text">Cohorts hold their own data</p></div>
      <div v-click="2"><p v-click-hide="3" class="caption-text">A server is installed at each site</p></div>
      <div v-click="3"><p v-click-hide="4" class="caption-text">Data is uploaded to the local server</p></div>
      <div v-click="4"><p v-click-hide="5" class="caption-text">Researcher is granted access</p></div>
      <div v-click="5"><p v-click-hide="6" class="caption-text">Researcher connects via the Central Portal</p></div>
      <div v-click="6"><p class="caption-text">Analysis commands sent, summary statistics returned</p></div>
    </div>

    <!-- Grid, not flex: one explicit column per diagram element (7 columns),
         so the access-grant row below can span grid-column: 1 / -1 and land
         exactly under column 1 (data) through the last column (researcher) —
         a direct reference to the same column tracks, not a computed width. -->
    <div class="diagram-grid">

      <!-- Local data (click 1). justify-content:flex-end pushes each icon+text
           row flush against the RIGHT edge of the column (the side facing the
           arrow) — the column is wider than the content, and without this the
           leftover space sits on the right by default, pushing the arrow
           off-centre in the gap. -->
      <div v-click="1" style="grid-column: 1;">
        <p class="col-heading">Data</p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
          <div style="display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;"><img src="/icon-database.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Cohort A</span></div>
          <div style="display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;"><img src="/icon-database.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Cohort B</span></div>
          <div style="display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;"><img src="/icon-database.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Cohort C</span></div>
        </div>
      </div>

      <!-- Upload data arrow (click 3). col-spacer is a plain sibling (not a flex
           child sharing the row-gap) — same two-level structure as the data/
           servers columns — so its own margin-bottom is the only space before
           the first arrow, not that margin plus an extra flex gap on top.
           Each arrow is a flex:1 solid line (same colour, solid not dashed —
           this is a data-flow arrow, not the access line) plus a CSS-drawn
           triangle arrowhead (not a "→" glyph — the character's own font
           side-bearing left a gap between the line and the glyph's shaft,
           reading as two disconnected line segments), filling the full column
           width so it reads as one continuous line. -->
      <div v-click="3" style="grid-column: 2;">
        <div class="col-spacer"></div>
        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
          <div style="height: 36px; display: flex; align-items: center; width: 75%; margin: 0 auto;">
            <div style="flex: 1; height: 2px; background: var(--slidev-theme-primary);"></div>
            <div style="width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-left: 10px solid var(--slidev-theme-primary);"></div>
          </div>
          <div style="height: 36px; display: flex; align-items: center; width: 75%; margin: 0 auto;">
            <div style="flex: 1; height: 2px; background: var(--slidev-theme-primary);"></div>
            <div style="width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-left: 10px solid var(--slidev-theme-primary);"></div>
          </div>
          <div style="height: 36px; display: flex; align-items: center; width: 75%; margin: 0 auto;">
            <div style="flex: 1; height: 2px; background: var(--slidev-theme-primary);"></div>
            <div style="width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-left: 10px solid var(--slidev-theme-primary);"></div>
          </div>
        </div>
      </div>

      <!-- Local servers (click 2). Left-aligned (default) rather than
           centred/right — flush against the column's left edge, the side
           facing connector 2 (data→servers). The small leftover slack from
           the narrower text label ends up on the right, facing connector 4,
           which already has its own small icon-column buffer on its far
           side (see .diagram-grid's comment) — that combination lands both
           of connector 4's gaps within a few px of each other. -->
      <div v-click="2" style="grid-column: 3; text-align: left;">
        <p class="col-heading">Local servers</p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
          <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Server A</span></div>
          <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Server B</span></div>
          <div style="display: flex; align-items: center; gap: 0.5rem;"><img src="/icon-server.png" style="height: 36px;" /> <span style="font-size: 13px; white-space: nowrap;">Server C</span></div>
        </div>
      </div>

      <!-- Commands to servers, summary statistics back (click 6). Previously
           centred via align-self:stretch + flex:1 justify-content:center,
           matched by hand against every other column's own stretch+centre
           maths — fragile, and still landed off from the CAS icon and the
           researcher icon (their surrounding content isn't symmetric, so
           each column's own "centre" wasn't the same physical row height).
           Instead, anchor everything to the one column that's plain normal
           flow with no centring tricks: column 3's own middle row (Server B),
           which sits at a fixed 98.8px below the column top (col-heading
           36.8px + half the 124px server stack). Every connector/icon below
           is position:absolute; top:98.8px against its own column div,
           which — left at the grid's default align-items:start with no
           height set — has its top edge pinned to the row's top edge, i.e.
           the same coordinate frame as column 3. That guarantees every one
           of these lands on the exact same physical line as Server B,
           regardless of what else is in the column. -->
      <div v-click="6" style="grid-column: 4; position: relative;">
        <div class="col-spacer"></div>
        <div style="position: absolute; top: 98.8px; left: 12.5%; right: 12.5%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 0.7rem;">
          <div style="height: 10px; display: flex; align-items: center; width: 100%;">
            <div style="width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-right: 9px solid #E6B96A; flex: none;"></div>
            <div class="flow-line flow-left" style="flex: 1; height: 2px; color: #E6B96A;"></div>
          </div>
          <div style="height: 10px; display: flex; align-items: center; width: 100%;">
            <div class="flow-line flow-right" style="flex: 1; height: 2px; color: var(--slidev-theme-primary);"></div>
            <div style="width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 9px solid var(--slidev-theme-primary); flex: none;"></div>
          </div>
        </div>
      </div>

      <!-- Central Analysis Server — the hub (click 5, after researcher applies
           for access). Icon is position:absolute at the same 98.8px anchor as
           Server B (see column 4's comment), not flex-centred, so it lines up
           regardless of the heading's own height. -->
      <div v-click="5" style="grid-column: 5; position: relative; text-align: center;">
        <p class="col-heading" style="white-space: nowrap; font-size: 0.85rem;">Central Portal</p>
        <img src="/icon-server.png" style="position: absolute; top: 98.8px; left: 50%; transform: translate(-50%, -50%); height: 48px;" />
      </div>

      <!-- Connect arrow: researcher to CAS (click 5, with the CAS). Same
           98.8px anchor as the rest of this row (see column 4's comment).
           CSS-drawn triangle (not a "←" glyph, for the same reason as the
           upload arrows) + a dashed line (same 2px dashed #4285F4 style as
           the access line below) spanning the column width. -->
      <div v-click="5" style="grid-column: 6; position: relative;">
        <div class="col-spacer"></div>
        <div style="position: absolute; top: 98.8px; left: 12.5%; right: 12.5%; transform: translateY(-50%); display: flex; align-items: center;">
          <div style="width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-right: 10px solid var(--slidev-theme-primary);"></div>
          <div style="flex: 1; height: 0; border-top: 2px dashed #4285F4;"></div>
        </div>
      </div>

      <!-- Researcher (click 4, appears on its own first). Icon is
           position:absolute at the same 98.8px anchor as the rest of this
           row (see column 4's comment) — critically, this anchors the icon
           itself, not the icon+rstudio/datashield-logos block as a unit, so
           the extra logo row underneath no longer pulls the icon's own
           centre away from Server B / the CAS icon the way flex-centring
           the whole stack did. The logo row is positioned independently,
           just below the icon's fixed bottom edge (98.8 + half of 46px
           icon height + a small gap). -->
      <div v-click="4" style="grid-column: 7; position: relative; text-align: center;">
        <p class="col-heading">Researcher</p>
        <img src="/icon-researcher.png" style="position: absolute; top: 98.8px; left: 50%; transform: translate(-50%, -50%); height: 46px;" />
        <div style="position: absolute; top: 126.6px; left: 50%; transform: translateX(-50%); display: flex; align-items: center; justify-content: center; gap: 0.4rem;">
          <img src="/icon-rstudio.png" style="height: 17px;" />
          <img src="/icon-datashield.png" style="height: 17px;" />
        </div>
      </div>

      <!-- Applies for access — a static dashed connector (click 4, while researcher is alone,
           no animation, just appears). Columns are fixed pixel widths (see .diagram-grid),
           so column 1's centre is exactly 59px from the left edge and column 7's centre
           is exactly 27px from the right edge — the same numbers that centre the two
           vertical ticks below via justify-self:center in those same fixed-width columns.
           That lets the horizontal bar's margins reach exactly the ticks' x-position by
           arithmetic instead of guessing against content-dependent auto-sized columns. -->
      <div v-click="4" style="grid-column: 1 / -1; grid-row: 2; display: grid; grid-template-columns: subgrid; height: 24px; margin-top: 0.3rem;">
        <div style="grid-column: 1; grid-row: 1; justify-self: center; width: 2px; height: 100%; border-right: 2px dashed #4285F4;"></div>
        <div style="grid-column: 7; grid-row: 1; justify-self: center; width: 2px; height: 100%; border-right: 2px dashed #4285F4;"></div>
        <div style="grid-column: 1 / -1; grid-row: 1; align-self: end; height: 2px; margin-left: 59px; margin-right: 27px; border-bottom: 2px dashed #4285F4;"></div>
      </div>

    </div>

    <!-- Legend (click 6, with the commands/stats arrows) — explains the three
         line styles used across the diagram. -->
    <div v-click="6" style="display: flex; justify-content: center; gap: 1.75rem; margin-top: 0.6rem;">
      <div style="display: flex; align-items: center; gap: 0.4rem;">
        <div style="width: 22px; height: 0; border-top: 2px dashed #4285F4;"></div>
        <span style="font-size: 12px; color: #555;">Authentication</span>
      </div>
      <div style="display: flex; align-items: center; gap: 0.4rem;">
        <div style="width: 22px; height: 2px; background: #E6B96A;"></div>
        <span style="font-size: 12px; color: #555;">Analysis commands</span>
      </div>
      <div style="display: flex; align-items: center; gap: 0.4rem;">
        <div style="width: 22px; height: 2px; background: var(--slidev-theme-primary);"></div>
        <span style="font-size: 12px; color: #555;">Summary statistics</span>
      </div>
    </div>

  </div>
</template>

<style scoped>
.diagram-grid {
  display: grid;
  /* Fixed widths (not auto) so the access-line's exact centre offsets below
     are real arithmetic, not a guess against content-dependent sizing. The
     outer two connectors (data→servers, CAS→researcher) are matched at 70px,
     the midpoint of their previous 87px/53px equal-centre-spacing values.
     The commands/stats connector is doubled to 90px (was 45px) so those
     arrows read as long as the others instead of a short stub.
     CAS and researcher are sized to their own icon (48px / 46px) plus a
     small buffer, not to fit their heading text — the heading is centred
     on the (narrow) track and simply overflows it visually, uncropped,
     rather than forcing the track wide and leaving a large gap of empty
     column either side of the icon. Data/servers keep their generous
     118px (sized for the "Cohort X"/"Server X" labels) but their icon+text
     rows are flush to the edge facing their one/both neighbouring arrows,
     so no slack accumulates there either. The result: every arrow's visible
     gap to its neighbouring icon is ~16–24px on every side, instead of the
     CAS icon (previously centred in a 200px column) sitting ~90px from one
     arrow and ~45px from the other.
     Shrinking CAS/researcher frees up width that has to go somewhere, or
     the diagram just shrinks toward the middle instead of spanning the
     slide — so that freed space is put back into the three connector
     tracks (longer arrow lines fill it without touching any of the gaps
     just fixed, since a line already spans its whole track regardless of
     the track's width), keeping the same 70:90:70 ratio between them:
     data 118 / connector 115 / servers 108 / connector 150 /
     CAS 56 / connector 115 / researcher 54 */
  grid-template-columns: 118px 115px 108px 150px 56px 115px 54px;
  align-items: start;
  column-gap: 1rem;
  justify-content: center;
  transform: translateX(-24px);
  margin-top: 0.4rem;
}
.caption-box {
  position: relative;
  height: 1.3rem;
  text-align: center;
}
.caption-text {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  margin: 0;
  font-size: 13px;
  color: #888;
}
.col-heading {
  min-height: 1.9rem;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  margin: 0 0 0.4rem 0;
  font-weight: 700;
  font-size: 0.95rem;
  line-height: 1.15;
  color: var(--slidev-theme-primary);
}
.col-spacer {
  min-height: 1.9rem;
  margin-bottom: 0.4rem;
}

/* Flowing dashed line for the commands/stats arrows. animation-iteration-count
   is finite (not infinite) — plays a few times once revealed at the final
   click, then settles into a static dashed line, rather than still visibly
   moving through discussion/Q&A long after the last click. */
.flow-line {
  background-image: repeating-linear-gradient(90deg, currentColor 0 6px, transparent 6px 12px);
  background-size: 12px 2px;
  background-repeat: repeat-x;
  animation-duration: 0.8s;
  animation-timing-function: linear;
  animation-iteration-count: 4;
}
.flow-left { animation-name: flow-left; }
.flow-right { animation-name: flow-right; }
@keyframes flow-left {
  from { background-position: 0 0; }
  to { background-position: -24px 0; }
}
@keyframes flow-right {
  from { background-position: 0 0; }
  to { background-position: 24px 0; }
}
</style>
