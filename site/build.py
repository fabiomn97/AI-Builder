#!/usr/bin/env python3
"""Inline every asset into a single self-contained index.html.

Usage:  python3 site/build.py
Output: index.html at the repository root (no external requests at runtime).
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ASSETS = SITE / "assets"

# Images become data: URIs. The CV is embedded once as bare base64 and handed
# to every download link as a blob at runtime, so it is not duplicated per link.
ASSET_MAP = {
    "{{PORTRAIT}}": ("portrait.jpg", "image/jpeg"),
    "{{AVATAR}}": ("avatar.jpg", "image/jpeg"),
    "{{SCENE}}": ("scene.jpg", "image/jpeg"),
}
CV = "Fabio-Macedo-CV.pdf"


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def main() -> None:
    html = (SITE / "template.html").read_text(encoding="utf-8")
    for token, (name, mime) in ASSET_MAP.items():
        src = ASSETS / name
        if not src.exists():
            raise SystemExit(f"missing asset: {src}")
        html = html.replace(token, f"data:{mime};base64,{b64(src)}")

    cv = ASSETS / CV
    if not cv.exists():
        raise SystemExit(f"missing asset: {cv}")
    html = html.replace("{{CV_B64}}", b64(cv))

    leftover = [t for t in list(ASSET_MAP) + ["{{CV_B64}}"] if t in html]
    if leftover:
        raise SystemExit(f"unreplaced tokens: {leftover}")

    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}  ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
