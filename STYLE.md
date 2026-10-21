# Style contract for this guide ("ultra mascado")

Every page must be understandable by someone who has **never** taken a signals/statistics course.
This file is the checklist used to convert the remaining pages. The reference implementation is
`docs/p3-windows.md` (theory) + `docs/p0-foundations.md` (background chapter).

## The test

> Pick any sentence. Could a first-year who has never seen the notation say what it means,
> using only what appears earlier on the page (or one click away)? If not, rewrite it.

## Page-level rules

1. **`!!! need "Before this page"`** box at the top: exactly which earlier sections the page
   requires, each a link. Nothing else may be assumed. If a page needs something that does not
   exist yet, write it into `docs/p0-foundations.md` first (or into a new 0.x page).
2. **Order inside a theory section**: plain words → tiny concrete example with real numbers →
   the formula → what the exam asks about it. Never formula first.
3. **Every symbol is explained** (inline in parentheses, or in a small table) at its first
   appearance on the page — including "obvious" ones like $n$, $T$, $N$, $\theta$.
4. **Every formula shows where it comes from**: a one-line derivation, or a link to the exact
   section where it is derived. No formula appears "because I say so".
5. **No unexplained algebra**: when an equation is transformed, name the identity used
   ("use $\sin^2\alpha = \frac{1-\cos 2\alpha}{2}$, from [Chapter 0 §0.4](...)").
6. **Show the arithmetic**: write `1/(1-0.1353) = 1/0.8647 ≈ 1.1565`, not `≈ 1.16`. For letters
   (e.g. $A^2/2$) say which symbols survive and why.
7. **Jargon**: either avoid it, or define it inline in plain words the first time, and add it to
   the `*[term]: definition` tooltip list at the bottom of the page.
8. Cross-link instead of repeating; keep the exam wording untouched inside `!!! exam` boxes.

## Exam-solution template

```
???+ solution "Solution"

    **What is being asked?**  one or two plain sentences.

    **Symbols in this question**   (omit only if truly trivial)
    | Symbol | Meaning |

    **Step 1 — <name the step>.** what you do, and *why you are allowed to* (identity/definition + link).
    **Step 2 — ...**

    !!! trap "..."     (only where points are actually lost)

    !!! answer "Answer"
        the final answer, labelled.
```

## Box vocabulary

| Box | Use for |
|---|---|
| `!!! need` | prerequisites of this page (teal) |
| `!!! exam` | original exam text, unmodified (grey) |
| `???+ solution` | worked solution (green, collapsible) |
| `!!! answer` | final answer inside a solution (green, bordered) |
| `!!! trap` | where points get lost / false statements (orange) |
| `!!! recipe` | reusable procedure (blue) |
| `!!! idea` | shortcut, sanity check, "why" aside (purple) |
| `!!! freq` | how often a pattern comes up in exams (red) |
| `!!! example` | tiny worked example inside theory |

## Pictures and animations

Every theory idea gets a picture next to it, placed right after the paragraph it illustrates, with a caption
that says **how to read it** (what each colour/axis is, what to notice), not just what it is.

| What | Source | Output | Rebuild |
|---|---|---|---|
| exam-solution figures | `scripts/plots.py` | `docs/img/gen/*.svg` | `python scripts/plots.py` |
| theory figures | `scripts/theory_plots.py` | `docs/img/gen/*.svg` | `python scripts/theory_plots.py [name ...]` |
| animations (Manim) | `scripts/videos.py` (+ `vidkit.py`) | `docs/video/*.mp4` + `.jpg` poster | `python scripts/render_videos.py [Scene ...]` |

- Figure markup: `<figure markdown>` + `![alt](img/gen/x.svg)` + `<figcaption>`. Never indent a figure inside a
  list item (it breaks the list); put it after the list.
- Video markup: `<figure class="anim"><video class="anim" src="video/x.mp4" poster="video/x.jpg" muted loop
  playsinline controls preload="none"></video><figcaption><b>Animation.</b> …</figcaption></figure>`.
  `javascripts/video.js` plays it only while it is on screen.
- Animations need no LaTeX: `vidkit.MT()` renders `$math$` with matplotlib. Check a scene quickly with
  `PREVIEW=<dir> python scripts/render_videos.py --last Scene` (last frame as PNG).
- In inline math write `\lt` instead of `<` before a letter (`$M\lt N$`): `<N` looks like an HTML tag to
  Markdown and breaks the figures that follow.

## Conversion status

All pages are converted: `p0-foundations.md` (with 0.6 probability from zero), Part 1 to Part 4,
`toolbox.md` (one-line "why" per identity). `exams.md` and `cheatsheet.md` already link every
question to the page that explains it. New material should follow the same contract.

Each converted page must keep its existing heading anchors (`{#apr25-3a}` etc.): other pages and
external links point at them.
