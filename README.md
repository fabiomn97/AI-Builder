# Personal website — Fabio Macedo

`index.html` is the deliverable: one self-contained file. No external requests, no CDN, no
web fonts. Open it by double-clicking, email it, drop it on any static host.

It embeds the photos and the CV PDF as base64, so it works offline and the **Download CV**
buttons hand over a real `Fabio-Macedo-CV.pdf` without needing a server.

## Editing

`index.html` is generated — don't edit it directly (it's ~550 KB, mostly base64).

```
site/template.html     the real source: markup, CSS, JS, with {{TOKEN}} asset placeholders
site/assets/           portrait.jpg, avatar.jpg, scene.jpg, Fabio-Macedo-CV.pdf
site/build.py          inlines the assets and writes index.html
```

Edit the template (or swap a file in `site/assets/`), then rebuild:

```bash
python3 site/build.py
```

To update the CV, replace `site/assets/Fabio-Macedo-CV.pdf` and rebuild.

## Notes

- Light and dark themes; follows the OS setting, with a toggle in the nav that remembers
  the choice in `localStorage`.
- Responsive from 320 px up; the hero drops to a single column below 760 px.
- Prints cleanly to PDF (7 pages, no nav, no shadows, no orphaned headings).
- Works with JavaScript disabled — nothing is hidden, and the CV buttons fall back to the
  LinkedIn profile.
