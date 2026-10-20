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

## Conversion order and known gaps

- [x] `p3-windows.md` — done (the reference).
- [ ] `p3-nonparametric.md`, `p3-autocorr.md`, `p3-chain.md` — need: what a random signal is,
      expectation/variance, autocorrelation from zero. Add `0.x Probability from zero` to
      `p0-foundations.md` (or `p0-probability.md`) **before** converting these.
- [ ] `p2-mle.md`, `p2-crlb.md`, `p2-bayes.md`, `p2-ls.md` — need the probability 0.x too
      (PDF, expectation, variance, independence, conditional probability).
- [ ] `p4-basics.md`, `p4-lrt.md`, `p4-bayes.md` — same, plus "hypothesis test" in plain words.
- [ ] `p1-*.md` — last; they are the least mechanical.
- [ ] `toolbox.md` — keep as reference, but each identity gets a one-line "why" (it mostly has them).
- [ ] `exams.md`, `cheatsheet.md` — add "which page explains this" links next to each question.

Each converted page must keep its existing heading anchors (`{#apr25-3a}` etc.): other pages and
external links point at them.
