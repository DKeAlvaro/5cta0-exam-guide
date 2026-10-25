"""Render the A4 cheat sheet to PDF locally, so the print result can be checked
without going through the browser print dialog.

Usage:
    python scripts/mkpdf.py               # build site + write cheatsheet.pdf
    python scripts/mkpdf.py --open        # ...and open the PDF
    python scripts/mkpdf.py --no-build    # skip the mkdocs build (faster edits)
    python scripts/mkpdf.py --scale 1.1   # print scale, 1.0 = 100 %

The output lands next to this repo as cheatsheet.pdf (gitignored).
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site" / "cheatsheet.html"
OUT = ROOT / "cheatsheet.pdf"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# The page typesets math with KaTeX's auto-render on the theme's document$ event,
# which headless printing does not always wait for: do it by hand.
RENDER = """() => {
  if (typeof renderMathInElement !== 'function') return 'renderMathInElement missing';
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\\\(", right: "\\\\)", display: false },
      { left: "\\\\[", right: "\\\\]", display: true }
    ],
    ignoredClasses: ["md-search", "md-header"],
    throwOnError: false
  });
  return document.querySelectorAll('.katex').length + ' formulas';
}"""


def chrome_path() -> str | None:
    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", type=float, default=0.82)
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    if not args.no_build:
        print("building site ...")
        subprocess.run([sys.executable, "-m", "mkdocs", "build", "-q"], cwd=ROOT, check=True)

    if not SITE.exists():
        print("site/cheatsheet.html not found — run without --no-build first")
        return 1

    from playwright.sync_api import sync_playwright

    exe = chrome_path()
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe, headless=True) if exe else p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1200, "height": 1600})
        page.goto("file:///" + SITE.as_posix())
        page.wait_for_timeout(2500)  # KaTeX fonts + scripts from the CDN
        print(page.evaluate(RENDER))
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(1000)
        page.emulate_media(media="print")
        page.pdf(path=str(OUT), format="A4", print_background=True, scale=args.scale,
                 margin={"top": "1mm", "bottom": "1mm", "left": "3mm", "right": "3mm"})
        browser.close()

    try:
        import pdfplumber
        with pdfplumber.open(OUT) as pdf:
            print(f"pages: {len(pdf.pages)}")
    except Exception:
        pass

    # Strip identifying metadata (Chrome writes the page title = "A4 cheat sheet - 5CTA0 ...")
    try:
        from pypdf import PdfReader, PdfWriter
        reader = PdfReader(str(OUT))
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        tmp = OUT.with_suffix(".tmp.pdf")
        with open(tmp, "wb") as fh:
            writer.write(fh)
        os.replace(tmp, OUT)
        print("metadata cleared (no title/author)")
    except Exception as exc:
        print("metadata strip skipped:", exc)

    # Also drop a copy into docs/ so the site serves it at .../5cta0-exam-guide/cheatsheet.pdf
    docs_copy = ROOT / "docs" / "cheatsheet.pdf"
    try:
        import shutil
        shutil.copy2(OUT, docs_copy)
        print("saved:", OUT, "and", docs_copy)
    except Exception:
        print("saved:", OUT)
    if args.open:
        os.startfile(str(OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
