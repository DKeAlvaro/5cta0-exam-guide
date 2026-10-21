---
hide:
  - toc
---

# 5CTA0 Statistical Signal Processing: pass the exam

<p class="lead">Every question from every 5CTA0 exam we have (2019 → June 2026), copied word for word, labelled with where it comes from, and solved step by step, the way you would do it on paper. It is grouped by the <b>patterns</b> that come back year after year. No prior knowledge assumed.</p>

<div class="hero" markdown>
<div class="grid3" markdown>
<div markdown>
<div class="big">Mon 26 Oct</div>
13:30, written exam, 3 h. Resit: January 2027.
</div>
<div markdown>
<div class="big">≥ 5.0</div>
needed **on the exam itself**, then ≥ 5.5 after averaging with the lab (exam 70 %, lab 30 %).
</div>
<div markdown>
<div class="big">1 × A4</div>
your own notes, both sides, plus a calculator. The [cheat sheet](cheatsheet.md) is built for that A4.
</div>
</div>
</div>

## How the exam looks (recent years)

Four blocks, always in this order. Points from the three most recent papers (April 2024, April 2025, June 2026):

| Block | Topic | Points | What they actually ask |
|---|---|---|---|
| 1 | Probability, random variables, random processes | **1.5** | a Bayes word problem, a joint PDF, a stationarity/ergodicity MC, a spectral factorisation |
| 2 | Estimation theory | **3.0–3.5** | one MC + derive MLE / MAP (sometimes MMSE, CRLB, least squares) |
| 3 | Spectral estimation | **3.0** | theory MC/table + the chain *autocorrelation → correlogram → AR → MA → pick the plot* |
| 4 | Detection theory | **2.0–2.5** | one MC + a likelihood ratio test with a threshold, $P_{FA}$, $P_D$, priors/costs |

Multiple choice has one correct answer. Some open questions say *"provide only the final answer, the workout will not be checked"*. For those, only the number counts, so be careful with arithmetic.

## How to use this guide

This guide assumes **zero prior knowledge**: every term is defined where it first appears, every formula is derived or linked to where it is derived, and every solution shows *why* each step is allowed, not just what the step is.

1. Read **[The exam, decoded](patterns.md)** first (10 min). It tells you which question types come back and how many points each one is worth.
2. Read **[Chapter 0 · From zero](p0-foundations.md)** (30–45 min, once). It builds the background the whole course uses: what a signal is, frequency, complex numbers, the little bit of calculus (integrals, limits, geometric series), what a spectrum is, probability from zero (PDF, mean, variance, Gaussian, likelihood, autocorrelation), and a word book of every term the exams use. If a sentence anywhere in the guide confuses you, the missing piece is in that chapter.
3. Keep the **[Toolbox](toolbox.md)** open as a reference (it is not a chapter to study): the identity tables the solutions quote (logs, derivatives, the recurring integrals, $|1+ae^{-j\theta}|^2$, 2×2 systems).
4. Go through the parts in this order: **Part 3 → Part 2 → Part 4 → Part 1**. Part 3 is the most mechanical and has the most points.
5. Every idea comes with a **picture**, and the ones that are about something *changing* (a window growing, a threshold sliding, a filter sliding along a signal) also come with a short silent **animation**. Animations play by themselves while they are on screen and pause when you scroll past; tap one to pause it or scrub through it. Read the caption: it says what to look at.
6. Every question has a **Solution** block: *what is being asked* → *the symbols involved* → *every step with its justification* → a boxed **answer**. Solutions start hidden (quiz mode is always on): try first, then open them.
7. Two days before: do **April 2025** and **June 2026** from [Every exam](exams.md) timed, then print the [A4 sheet](cheatsheet.md).
8. Stuck on something? Hit **Ask** (button bottom-right), or **select any text** and press *Ask about this* to question that exact passage. It uses **your own API key** (Gemini, OpenAI or OpenRouter — custom base URL supported for proxies), kept in your browser only — nothing is stored on this site.

!!! idea "Box legend"
    - **Exam question** (grey box): the original text, unchanged. The header says which exam, which question, how many points.
    - **Solution** (green, collapsible): first *what is being asked* and *which symbols are involved*, then the steps (each with the reason it is allowed), then a boxed **answer**.
    - **Trap** (orange): where people lose points.
    - **Recipe** (blue): the reusable procedure for that question type.
    - **Before this page** (teal): exactly which earlier sections this page needs, with links. Nothing else is assumed.
    - **Idea** (purple): shortcuts, sanity checks and "why is this true" asides.

## Sources used

Exams: Jan 2019 retake · Nov 2019 · Jan 2020 retake · Practice exam Oct 2021 · Jan 2022 resit · Nov 2022 · Apr 2024 (Q3) · Apr 2025 (Q3) · Jun 2026 resit (Q4).
Questions from other exams shown in the 2026-27 review lectures: Q3 2022-23, Q1 2023 resit, Q3 2023 resit, Q2 2023-24 resit, Jan 2024 resit, Jun 2024 resit, Jan 2025 resit.
Plus the official keys (some re-issued in September 2026), the four review decks, and the course reader 2026-27.

!!! trap "Where the official keys are wrong or ambiguous"
    Every number in this guide was recomputed with a script. Where an official key disagrees, the guide says so:
    Jan 2019 2b (MMSE formula off by a factor 2), Nov 2019 2b ($\sigma_i^2=0.5098$, not 0.5089), Nov 2019 1a (no option is right, B is shifted by 3), Jan 2020 1a ($r_B$ is not strictly valid either), Jan 2020 4d (the key gives Newton–Raphson, not Gauss–Newton), Nov 2022 1c (key and review slides disagree), Apr 2025 4b (as printed, no option is false).
