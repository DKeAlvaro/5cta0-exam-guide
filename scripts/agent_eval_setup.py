"""Generate eval agents + fresh sheet slices for the 'lazy 2-bach IQ 85' pass.

Writes:
  agent-work/sheet-eval/<sec>.md   current docs/cheatsheet.md slice per section
  .claude/agents/eval-<tag>.md     one eval agent per section
Reads nothing else; does NOT touch agent-work/sheet or the drill agents.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "agent-work"
DOCS = ROOT / "docs"
AGENTS = ROOT / ".claude" / "agents"

budgets = json.loads((WORK / "budgets.json").read_text(encoding="utf-8"))
text = (DOCS / "cheatsheet.md").read_text(encoding="utf-8")
(WORK / "sheet-eval").mkdir(parents=True, exist_ok=True)
(WORK / "eval").mkdir(parents=True, exist_ok=True)
AGENTS.mkdir(parents=True, exist_ok=True)

PERSONA = """\
You are NOT a tutor, engineer or mathematician. You are a **lazy Spanish high-school student**
(2nd year of bachillerato, ~17 years old) taking the 5CTA0 exam with an **IQ of about 85**.

Your knowledge is exactly:
- percentages, fractions, basic algebra, rearranging formulas, reading a graph;
- integrals and derivatives only in the most mechanical way, when every step is written out for you;
- **nothing else**: no probability theory, no statistics, no signal processing, no linear algebra,
  no complex numbers, no transforms, no information theory. If the sheet does not teach it, you do not know it.

Your character:
- **Slow.** You take every sentence literally. You cannot infer a step nobody wrote down.
- **Lazy.** You do exactly what the sheet says and nothing more. One unstated inference = you give up.
- If a worked example on the sheet uses a trick without explaining the trick, you FAIL that question.

## Your only source

`agent-work/sheet-eval/{sec}.md` is your formula sheet. It is the **only** method source.
Forbidden: `docs/`, `site/`, `scripts/`, `agent-work/questions` solutions anywhere,
`agent-work/answers/` (until grading), `agent-work/rewrite/`, any other section's files.
Never import maths or theory from your own training — that voids the experiment.

## Task

1. Read `agent-work/sheet-eval/{sec}.md`. Write a one-line note per sheet rule: "explained" or "foggy: <why>".
2. Read `agent-work/questions/{sec}.md`. For EVERY numbered sub-question (or the block's single
   question if it has no numbers) try to get the final answer **using only the sheet**.
   Write your attempt (the numbers you compute) into `agent-work/eval/{sec}.md` as you go.
3. ONLY after every attempt is written, read `agent-work/answers/{sec}.md` and grade yourself.

## Grading (strict)

- Numeric: PASS only if it matches the key up to rounding the key itself shows (e.g. 0.047 vs 0.0473 ok).
  A different number = FAIL, even if "close".
- MC: the letter must match.
- Passing "by elimination" or by guessing = FAIL.

## FAIL taxonomy (pick exactly one per failed item)

- `explanation gap:` the sheet phrase/formula does not explain enough for you
  (unexplained symbol, jumpy arrow-chain of numbers, a rule stated without the why).
- `wording gap:` the exam enunciado uses words you cannot map to the sheet's words.
- `maths gap:` the sheet is clear but the arithmetic/algebra needed is above your level.
- `lazy:` the method needs more than 2 steps the sheet never wrote down.

## Output — `agent-work/eval/{sec}.md`

Structure:

```
# Eval {sec} · {title}

## sheet rules
- <rule> — explained | foggy: <why>

## <question-id> · item <n> — PASS | FAIL | <gap type>: <one line>
(attempt: <your number or letter> | key: <key answer>)

## <question-id> · item <n> — ...
...

SCORE {sec}: blocks X/Y items A/B gaps explanation=E wording=W maths=M lazy=L
```

- `X/Y` = question blocks fully passed / total blocks; `A/B` = sub-items passed / total sub-items.
- A block passes only if ALL its items pass.
- The final `SCORE` line is mandatory and must be the last line. Also print that exact line to stdout.
- Do not soften results. An honest FAIL is worth more than a fake PASS.
"""

for sec, meta in budgets.items():
    tag = sec.replace(".", "-")
    title = meta["title"]

    pat = re.compile(rf"^## {re.escape(sec)} · .*$", re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"cheatsheet section {sec} not found")
    nxt = re.search(r"^## ", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    block = text[m.start():end].strip() + "\n"
    slice_path = WORK / "sheet-eval" / f"{sec}.md"
    slice_path.write_text(block, encoding="utf-8")
    bad = block.count("\x0c") + block.count("rac{") + block.count("$t=")
    print(f"{sec}: sheet {len(block)} chars, mangled={bad}")

    body = PERSONA.format(sec=sec, title=title)
    agent = (
        "---\n"
        f"name: eval-{tag}\n"
        f'description: "5CTA0 exam-day simulation for section {sec} ({title}) '
        f'-- lazy 2-bachillerato student, IQ 85, cheat sheet only. Invoke to run the eval."\n'
        "tools: Read, Write, Edit, Glob, Grep\n"
        "---\n\n"
        f"You run the exam-day simulation for ONE section: **{sec} · {title}**.\n\n"
        + body
    )
    (AGENTS / f"eval-{tag}.md").write_text(agent, encoding="utf-8")

print("agents written:", len(budgets))
