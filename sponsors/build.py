#!/usr/bin/env python3
"""Build sponsors/index.html (GitHub Pages) from src/tracker.html + targets.json.

src/tracker.html is the single source. It is also what gets published as the
shared claude.ai artifact, which is why it has no <html>/<head> wrapper.
This script adds the document wrapper and inlines targets.json so the page
works on GitHub Pages and when opened straight from disk.
"""
import json
from pathlib import Path

here = Path(__file__).parent
body = (here / "src" / "tracker.html").read_text(encoding="utf-8")
title, body = body.split("\n", 1)  # first line is the <title>; it belongs in <head>
assert title.startswith("<title>"), "src/tracker.html must start with its <title>"
data = json.loads((here / "targets.json").read_text(encoding="utf-8"))
seed = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

page = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
    f"{title}\n"
    "<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n"
    "</head>\n<body>\n"
    f"<script id=\"seed-data\" type=\"application/json\">{seed}</script>\n"
    f"{body}\n</body>\n</html>\n"
)
(here / "index.html").write_text(page, encoding="utf-8")
print(f"wrote index.html ({len(page) // 1024} KB, {len(data)} companies)")
