"""Build the per-section subagent drill: question packs, answer keys, sheet slices, agent files.

For every cheat-sheet section (1.1 ... 4.2) this creates:

    agent-work/questions/<sec>.md   exam questions only (no solutions) for the drill
    agent-work/answers/<sec>.md     full worked solutions, opened only AFTER solving
    agent-work/sheet/<sec>.md       that section of docs/cheatsheet.md (the only method source)
    agent-work/budgets.json         chars per section (rewrite budget)
    .claude/agents/sec-<sec>.md     the subagent definition

Usage: python scripts/agent_drill_setup.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
WORK = ROOT / "agent-work"

# cheat-sheet section -> (title, question sources)
#   pages: full exam blocks are taken from these docs pages
#   mc_from: only multiple-choice blocks from these pages (section 2.5)
#   scope: extra instruction for multi-part blocks (3.1 vs 3.2 share p3-chain)
SECTIONS = {
    "1.1": {
        "title": "Bayes word problems (counts)",
        "pages": ["p1-bayes"],
        "scope": "",
    },
    "1.2": {
        "title": "Joint PDF: c, marginal, conditional, independent",
        "pages": ["p1-rv"],
        "scope": (
            "The multiple-choice 'concepts' blocks (expected value, covariance, discrete vs "
            "continuous, PMF tables, binomial, Gaussian contours, random process as a picture) "
            "are IN scope: they are Part 1 exam questions and the sheet must let a zero-knowledge "
            "student answer them. You may rename the heading to '## 1.2 · Joint PDF + Part 1 "
            "concept MCs'. Budget for this section: target 1121–1700 characters, hard cap 1900."
        ),
    },
    "1.3": {
        "title": "WSS and ergodic",
        "pages": ["p1-processes"],
        "scope": "",
    },
    "1.4": {
        "title": "Spectral factorisation",
        "pages": ["p1-factorisation"],
        "scope": "",
    },
    "2.1": {
        "title": "Maximum likelihood (MLE)",
        "pages": ["p2-mle"],
        "scope": "",
    },
    "2.2": {
        "title": "MAP with a prior",
        "pages": ["p2-bayes"],
        "scope": "",
    },
    "2.3": {
        "title": "Least squares",
        "pages": ["p2-ls"],
        "scope": "",
    },
    "2.4": {
        "title": "CRLB",
        "pages": ["p2-crlb"],
        "scope": (
            "Computation questions (e.g. computing a Fisher information or a CRLB bound for a "
            "given pdf) are IN scope — include the derivative/expectation recipes they need, "
            "spelled out for a student who cannot derive. One line on MVUE (unbiased + minimum "
            "variance, equals the CRLB when attainable) is welcome too. Budget for this section: "
            "target 400–750 characters, hard cap 800."
        ),
    },
    "2.5": {
        "title": "MC words",
        "pages": [],
        "mc_from": ["p2-mle", "p2-bayes", "p2-crlb"],
        "scope": "",
    },
    "3.1": {
        "title": "Correlogram + pick the plot",
        "pages": ["p3-chain"],
        "scope": (
            "Blocks from the 'chain' page can mix several sub-questions. Solve ONLY the "
            "sub-questions about the correlogram (writing P(theta) from r[k], or in cos theta) "
            "and about picking/reading the plot. Skip AR/MA parameter fitting sub-questions with "
            "a one-line note '[skip 3.2 part]'."
        ),
    },
    "3.2": {
        "title": "AR / MA from r[k]",
        "pages": ["p3-chain", "p3-autocorr"],
        "scope": (
            "Blocks from the 'chain' page can mix several sub-questions. Solve ONLY the "
            "sub-questions about model type, autocorrelation from an equation, AR/MA/ARMA "
            "parameters (Yule-Walker, b-polynomial) and the resulting PSD. Skip 'write the "
            "correlogram' and 'pick the plot' sub-questions with a one-line note '[skip 3.1 part]'."
        ),
    },
    "3.3": {
        "title": "Periodogram, Bartlett, Welch, windows",
        "pages": ["p3-nonparametric", "p3-windows"],
        "anchors_from": {"p3-chain": ["jun26-3e"]},
        "scope": "",
    },
    "4.1": {
        "title": "Likelihood-ratio test",
        "pages": ["p4-lrt"],
        "scope": "",
    },
    "4.2": {
        "title": "Bayesian detection",
        "pages": ["p4-bayes", "p4-basics"],
        "scope": "",
    },
}

MC_RE = re.compile(r"^\s*(?:[-*]\s*)?\(?[a-dA-D]\)[\s.]", re.M)


def indent_block(lines: list[str], out: list[str]) -> int:
    """Append indented (4 sp) markdown block body lines, dedented by 4."""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("    "):
            out.append(line[4:])
        elif line.strip() == "":
            out.append("")
        else:
            break
        i += 1
    return i


def parse_page(path: Path) -> list[dict]:
    """Return [{anchor, title, exam, solution}] for every exam block in a docs page."""
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[dict] = []
    cur = None
    in_exams = False
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (Exam questions.*)$", line)
        if m:
            in_exams = True
            cur = None
            i += 1
            continue
        if re.match(r"^## ", line) and not line.startswith("## Exam questions"):
            in_exams = False
            cur = None
            i += 1
            continue
        m = re.match(r"^### (.+?)\s*\{#([a-z0-9-]+)\}\s*$", line)
        if m and in_exams:
            cur = {"title": m.group(1), "anchor": m.group(2), "exam": [], "solution": []}
            blocks.append(cur)
            i += 1
            continue
        if cur is not None:
            if line.startswith('!!! exam '):
                body: list[str] = []
                i += 1
                i += indent_block(lines[i:], body)
                cur["exam"] = body
                continue
            if line.startswith('???+ solution ') or line.startswith('??? solution '):
                body = []
                i += 1
                i += indent_block(lines[i:], body)
                cur["solution"] = body
                continue
        i += 1
    return blocks


def answer_of(solution: list[str]) -> str:
    """Final answer box of a solution, or the tail of it if there is no answer box."""
    text = "\n".join(solution).strip()
    m = re.search(r'!!! answer "Answer"\n((?:    .*\n?|\n)+)', text)
    if m:
        return "\n".join(l[4:] if l.startswith("    ") else l for l in m.group(1).splitlines()).strip()
    # no answer box: last non-empty paragraph
    paras = [p for p in text.split("\n\n") if p.strip()]
    return paras[-1].strip() if paras else "(no answer box in the key)"


def sheet_section(sec: str, title: str) -> tuple[str, int]:
    """The '## sec · title' block of docs/cheatsheet.md, and its char count."""
    text = (DOCS / "cheatsheet.md").read_text(encoding="utf-8")
    pat = re.compile(rf"^## {re.escape(sec)} · .*$", re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"cheatsheet section {sec} not found")
    nxt = re.search(r"^## ", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    block = text[m.start():end].strip() + "\n"
    return block, len(block)


def is_mc(exam: list[str]) -> bool:
    return len(MC_RE.findall("\n".join(exam))) >= 2


def main() -> None:
    for sub in ("questions", "answers", "sheet", "progress", "solutions", "rewrite", "report"):
        (WORK / sub).mkdir(parents=True, exist_ok=True)
    agents = ROOT / ".claude" / "agents"
    agents.mkdir(parents=True, exist_ok=True)

    page_cache: dict[str, list[dict]] = {}
    budgets: dict[str, dict] = {}

    for sec, meta in SECTIONS.items():
        q_parts, a_parts = [], []
        seen = set()
        for page in meta.get("pages", []) + meta.get("mc_from", []) + list(meta.get("anchors_from", {})):
            if page not in page_cache:
                page_cache[page] = parse_page(DOCS / f"{page}.md")
            for b in page_cache[page]:
                if b["anchor"] in seen:
                    continue
                mc_only = page in meta.get("mc_from", [])
                if mc_only and not is_mc(b["exam"]):
                    continue
                wanted = meta.get("anchors_from", {}).get(page)
                if wanted is not None and b["anchor"] not in wanted:
                    continue
                seen.add(b["anchor"])
                exam = "\n".join(b["exam"]).strip()
                q_parts.append(f"## {b['anchor']} — {b['title']}\n\n{exam}\n")
                a_parts.append(
                    f"## {b['anchor']} — {b['title']}\n\n{answer_of(b['solution'])}\n"
                )

        q_file = WORK / "questions" / f"{sec}.md"
        q_file.write_text(
            f"# Exam questions for section {sec} · {meta['title']}\n\n"
            f"Questions only. {len(q_parts)} blocks. Do not look for solutions anywhere.\n\n"
            + "\n".join(q_parts),
            encoding="utf-8",
        )
        (WORK / "answers" / f"{sec}.md").write_text(
            f"# Answer key for section {sec} · {meta['title']}\n\n"
            "Open ONLY after every question of an iteration has been attempted and written to "
            "the solutions file.\n\n" + "\n".join(a_parts),
            encoding="utf-8",
        )

        block, chars = sheet_section(sec, meta["title"])
        (WORK / "sheet" / f"{sec}.md").write_text(block, encoding="utf-8")
        budgets[sec] = {"title": meta["title"], "chars": chars, "questions": len(q_parts)}

        agents.joinpath(f"sec-{sec.replace('.', '-')}.md").write_text(
            agent_md(sec, meta, chars, len(q_parts)),
            encoding="utf-8",
        )
        print(f"{sec}: {len(q_parts)} questions, sheet {chars} chars")

    (WORK / "budgets.json").write_text(json.dumps(budgets, indent=2), encoding="utf-8")


def agent_md(sec: str, meta: dict, chars: int, nq: int) -> str:
    tag = sec.replace(".", "-")
    scope = ("\n- **Multi-part blocks.** " + meta["scope"]) if meta.get("scope") else ""
    return f"""---
name: sec-{tag}
description: "5CTA0 cheat-sheet hardening drill for exam section {sec} ({meta['title']}) — solves every past exam question of the section with only that section's formula sheet, as a zero-knowledge student, then rewrites the sheet. Invoke to run the drill for section {sec}."
tools: Read, Write, Edit, Glob, Grep
maxTurns: 400
---

You are running a controlled experiment for the 5CTA0 (statistical signal processing) A4 cheat sheet. You own section **{sec} · {meta['title']}**.

## Persona (this is the point of the experiment)

You are a student who **knows nothing about this subject**, **very little mathematics**, and **zero reading flexibility**: you cannot integrate reliably, you are shaky on derivatives, you barely manage algebra, and you can only follow recipes literally, word for word. You have one page of a formula sheet and nothing else.

Hard rules for the persona:

- The **only** method source is `agent-work/sheet/{sec}.md`. Everything else is forbidden knowledge: if the sheet does not show you how to do a step, the step is impossible for you and the question is a FAIL. Never import probability theory, statistics, signal processing, calculus or linear algebra from your own training. That would void the experiment.
- **An unexplained rule is an unusable rule.** If the sheet gives a formula or a step but does not say *why* it applies, what its symbols mean, or how the arithmetic goes — and that missing explanation leaves you unsure how to apply it to a new question — the question is a FAIL too, reason: `explanation gap: <what the sheet asserted without explaining>`. A cryptic worked line (`400/350/250 → bad 8, 14, 12.5`) does not teach you the method: if you cannot re-derive the steps that produced those numbers from the sheet's own words, that counts as an explanation gap.
- **You are blind to paraphrase.** You match words literally: a recipe on the sheet applies to a question only if the question's wording matches the sheet's wording. If the exam says "hence deduce the estimator" and the sheet says "plug-in rule", or the exam says "correlation" where the sheet says "inner product", or the exam names a quantity with a symbol the sheet never defines, you do **not** make the connection and the question is a FAIL — reason: `wording gap: sheet says <X>, exam says <Y>`. Synonyms, abbreviations, re-orderings of the same sentence and "obvious" re-labellings all count as different words. The only exception is pure arithmetic notation. When in doubt whether two phrasings mean the same thing, they do not: FAIL.
- Simulate weak maths: write every arithmetic step explicitly (like someone using a calculator), and use **only** the algebra identities the sheet shows. If a step needs an identity that is not on the sheet (e.g. how to integrate $e^{{-ay}}$, what $Q(t)$ is, how to solve a quadratic), mark the question FAIL with the missing rule as the reason.
- Do not "figure out" clever tricks that the sheet does not spell out. If you see the trick anyway, ignore it and FAIL the question — the sheet must teach the trick.

## Files

Read only:
- `agent-work/questions/{sec}.md` — {nq} exam question blocks (no solutions).
- `agent-work/sheet/{sec}.md` — your formula sheet (current version).
- `agent-work/answers/{sec}.md` — the answer key, **only at grading time** (see the protocol).

Write only:
- `agent-work/progress/{sec}.md` — live progress log (append-only).
- `agent-work/solutions/{sec}.md` — your attempts (overwritten each iteration).
- `agent-work/rewrite/{sec}.md` — the final rewritten sheet block.
- `agent-work/report/{sec}.md` — the final report.

**Forbidden:** reading anything else in this repo — in particular `docs/`, `site/`, other sections' files in `agent-work/`, or `agent-work/answers/{sec}.md` before you have finished solving. The docs pages contain worked solutions; reading them is cheating and voids the experiment.{scope}

## Protocol (iterations, max 3)

**Iteration loop:**

1. **Solve.** Work through every question block in `agent-work/questions/{sec}.md` in order, in the persona, using only the sheet. Write each attempt to `agent-work/solutions/{sec}.md` as you go: question anchor, the steps you can actually do from the sheet, the final answer, or `FAIL — reason` when the sheet does not cover what is needed. Get through all {nq} blocks.
2. **Grade.** Only when every block has been attempted, open `agent-work/answers/{sec}.md` and mark each attempt PASS/FAIL against the key. FAIL = wrong answer, or a question you had to skip because the sheet lacked a rule.
3. **Rewrite the sheet.** Rewrite `agent-work/sheet/{sec}.md` so that a student with your persona weaknesses could solve every failed question **from the sheet alone**. Constraints:
   - Keep the heading `## {sec} · {meta['title']}` as the first line, exactly as is.
   - Style: readable, self-contained English, KaTeX `$...$`, numbered recipe steps, worked examples with real numbers, one-line traps. No admonition boxes, no HTML, no images.
   - **Explain everything — this is the main point of this run.** The reader will have *only* your sheet in the exam, and he does not reconstruct hidden reasoning under stress: anything the sheet does not spell out, he will not be able to do. So: (a) every recipe step carries the reason it is legal, in one clause ("by the law of total probability: the bad images pile up from all machines"); (b) every symbol is named in plain words at its first appearance, including "obvious" ones ($N$, $k$, $\theta$, $r[0]$); (c) every worked example reads as a story, not as an arrow chain: say what each number *is* ("CT1 scans 18 patients → 18 × 0.15 = 2.7 bad images"), show each arithmetic step explicitly (including trivial ones), and end by pointing at which line of the question the final number answers. `400/350/250 → bad 8, 14, 12.5` is a style FAIL — rewrite such lines into steps a stranger could reproduce on a new question. (d) Name the *decision* too: say when to use this recipe and not the neighbouring one ("counts per group → this; a pdf is given → 1.2/2.1").
   - Budget: explanation beats compactness now. The current block is {chars} characters; target up to ~{int(chars * 1.8)} and hard cap {int(chars * 2.5)}. The printed sheet is allowed to run past two A4 pages — the editor will prune afterwards. Never cut a "why", a named symbol or an arithmetic step to save characters; if you must cut, cut a second variant of an example the exams do not need.
   - Prioritise the recent papers (June 2026, April 2025, April 2024, November 2022): their question types must pass. Older outlier topics (e.g. things that appear once in 2019 and never again) may be marked out-of-scope if covering them would break the budget — say so in the report.
   - Cover the *weaknesses*: spell out the arithmetic commands, the identities, the sign rules, the "when do I use which formula" triggers.
   - Cover the **wording**: for each rule/recipe, print the words the exams actually use, and every alias you saw in a failed question ("plug-in rule (a.k.a. empirical/MLE-in-place rule)", "correlation $= E[XY]$ (exam: 'correlation function at lag 0')"). A trigger line is worth its characters: `exam says "hence deduce" → use rule 3`. Your reader cannot infer that two phrasings mean the same thing — if a phrasing is not printed on the sheet, it does not exist for them.
4. **Re-solve.** With the new sheet, re-attempt **only the failed questions**, in the persona again. Use only the sheet — do not replay the key's solution from memory, and do not bridge a wording gap with knowledge of what the question "really means": if the sheet's words still do not match the exam's words, that is still a FAIL. If the key's method is not in your new sheet, that is still a FAIL.
5. **Grade again**, and loop to step 3. Stop when every in-scope question passes, or after 3 iterations.

## Progress log (mandatory, live)

`agent-work/progress/{sec}.md` is watched while you run. Append a line at these moments — never rewrite the file, always append:

- after **every** question attempt: `[q] <iter> <anchor> PASS|FAIL|SKIP — one short reason`
- at each phase change: `[phase] <iter> solving|grading|rewriting|re-solving`
- at the end of each iteration: `[iter] <iter> <pass>/<total> pass, sheet now <chars> chars`
- when done: `[done] final <pass>/<total> pass after <iters> iterations`

Keep each line short. Do not dump solutions into the progress log.

## Final deliverables

- `agent-work/rewrite/{sec}.md` — the final sheet block only (heading + body), ready to splice into `docs/cheatsheet.md` in place of the old section.
- `agent-work/report/{sec}.md` — compact: a table of question outcomes per iteration, what was missing from the original sheet, what you changed and why, and any out-of-scope questions. Include a **wording-gap table**: `exam phrase → sheet phrase (before) → how you closed it`, one row per paraphrase that failed you. Also an **explanation-gap table**: `cryptic/asserted line (before) → what a stranger could not reproduce from it → how you explained it now`, one row per unexplained rule or arrow-chain example you expanded.

Work autonomously. Do not ask questions."""


if __name__ == "__main__":
    main()
