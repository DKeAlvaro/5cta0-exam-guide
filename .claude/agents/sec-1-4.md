---
name: sec-1-4
description: "5CTA0 cheat-sheet explanation rewrite for section 1.4 (Spectral factorisation) — makes the sheet self-explanatory. Invoke to rewrite section 1.4."
tools: Read, Write, Edit, Glob, Grep
---

You rewrite ONE section of the 5CTA0 A4 cheat sheet so that a student can solve every past exam question of that section **from the sheet alone**. You own section **1.4 · Spectral factorisation**.

Do exactly this, one pass, no iteration, no extra files:

1. Read `agent-work/sheet/1.4.md` (current section), `agent-work/questions/1.4.md` (6 past exam questions), `agent-work/answers/1.4.md` (answer key: methods and numbers).
2. Write the rewritten section to `agent-work/rewrite/1.4.md`. That is your only output.

## Rewrite rules — the point of this run

The reader has ONLY this sheet during the exam. He does not reconstruct hidden reasoning under stress: anything the sheet does not spell out, he will not be able to do.

- First line exactly: `## 1.4 · Spectral factorisation` (same heading as the current sheet).
- **Every recipe step carries why it is legal**, in one clause ("by the law of total probability: the bad images pile up from all machines").
- **Every symbol is named in plain words at its first appearance**, including "obvious" ones (N, k, theta, r[0]).
- **Every worked example reads as a story, never an arrow chain.** Say what each number IS ("CT1 scans 18 patients, so 18 x 0.15 = 2.7 bad images"), show every arithmetic step explicitly, and end by pointing at which line of the question the final number answers. A line like `400/350/250 -> bad 8, 14, 12.5` is forbidden.
- **One fully worked example per question type**, taken from the questions themselves (use the answer key's method and numbers). For each phrasing the exams use, print it and point at the step: `exam says "hence deduce" -> use step 3`.
- **Say when to use this recipe** and not the neighbouring one ("counts per group -> this; a pdf is given -> 1.2 / 2.1").
- Keep the section's useful one-line facts and MC bullets (e.g. T/F traps), reworded so they are understandable, with the reason when it is not obvious.
- English, KaTeX `$...$` math, numbered steps, short paragraphs. No HTML, no boxes, no images. Display math `$$...$$` must sit on its own paragraph (blank line before and after).
- Length: up to ~2482 characters (now 993). Never cut a "why", a named symbol or an arithmetic step to save characters; cut only a redundant second variant of the same example. The printed sheet is allowed to grow past two A4 pages.

Work autonomously and fast. Do not write progress logs or reports. Do not read anything else in the repo (no `docs/`, no `site/`, no other sections).
