"""Merge the subagent sheet rewrites into docs/cheatsheet.md and check the A4 PDF.

Usage:
    python scripts/agent_drill_merge.py            # splice agent-work/rewrite/*.md into docs/cheatsheet.md
    python scripts/agent_drill_merge.py --report   # build cheatsheet.pdf and report pages + fill
    python scripts/agent_drill_merge.py --dry      # show what would change, write nothing

The two-sided layout is kept: sections 1.x/2.x before <div class="pagebreak">, 3.x/4.x after.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "agent-work"
SHEET = ROOT / "docs" / "cheatsheet.md"
PDF = ROOT / "cheatsheet.pdf"

SECS = ["1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "2.5",
        "3.1", "3.2", "3.3", "4.1", "4.2"]


def splice(text: str, sec: str, new_block: str) -> str:
    """Replace the '## sec · ...' block of the sheet with new_block.

    The block ends at the next '## ' heading **or** at the closing </div> markup of the
    column container — whichever comes first (swallowing that markup breaks the layout).
    """
    pat = re.compile(rf"^## {re.escape(sec)} · .*$", re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"section {sec} not found in cheatsheet.md")
    rest = text[m.end():]
    nxt = re.search(r"^(## |</div>)", rest, re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[: m.start()] + new_block.strip() + "\n\n" + text[end:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    if args.report:
        subprocess.run([sys.executable, "scripts/mkpdf.py", "--no-build"], cwd=ROOT, check=False)
        import pdfplumber
        with pdfplumber.open(PDF) as pdf:
            print(f"pages: {len(pdf.pages)}")
            for i, page in enumerate(pdf.pages, 1):
                words = page.extract_words()
                if not words:
                    print(f"  page {i}: empty")
                    continue
                top = min(w["top"] for w in words)
                bottom = max(w["bottom"] for w in words)
                print(f"  page {i}: text from {top:.0f} to {bottom:.0f} of {page.height:.0f} pt "
                      f"({100 * bottom / page.height:.1f} % filled)")
        return 0

    text = SHEET.read_text(encoding="utf-8")
    missing = [s for s in SECS if not (WORK / "rewrite" / f"{s}.md").exists()]
    if missing:
        print("no rewrite yet for:", ", ".join(missing))
    for sec in SECS:
        f = WORK / "rewrite" / f"{sec}.md"
        if not f.exists():
            continue
        block = f.read_text(encoding="utf-8")
        if not re.match(rf"^## {re.escape(sec)} · ", block):
            print(f"WARN {sec}: rewrite does not start with '## {sec} · ' — skipped")
            continue
        text = splice(text, sec, block)
        print(f"spliced section {sec} ({len(block)} chars)")
    if args.dry:
        return 0
    # arithmatex breaks $$...$$ display blocks that sit inside a paragraph and leaves
    # literal $ in the PDF: isolate every display block as its own paragraph.
    lines = text.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        if re.fullmatch(r"\$\$.*\$\$", line.strip()):
            while out and out[-1].strip() == "":
                out.pop()
            out.append("")
            out.append(line)
            out.append("")
        else:
            out.append(line)
    while out and out[0].strip() == "":
        out.pop(0)
    SHEET.write_text("\n".join(out).strip() + "\n", encoding="utf-8")
    print("docs/cheatsheet.md updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
