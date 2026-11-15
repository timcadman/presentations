# Presentations repo — working instructions

- **Colours:** always use a colour from `COLOURS.md`'s palette. If none of the existing entries fit, say so and propose adding the new colour to `COLOURS.md` — don't invent a hex value ad hoc.
- **Shared slides:** `library/` slides are included by more than one deck, so a change there lands in all of them. Ask before adding a slide to `library/`, before splitting or restructuring one, and before changing anything a deck other than the one being worked on includes. The same goes for `theme/` layouts and styles and for `components/`. Editing a deck's own `slides.md` needs no permission.
- **Reuse first:** before building a new Vue component or bespoke diagram for a slide, check `theme/layouts/` and `components/` for something that already does the job (or is close enough to extend). Only write a new bespoke component when nothing existing fits, and say briefly why.
