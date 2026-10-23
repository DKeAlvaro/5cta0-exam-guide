# 1.1 Bayes word problems

<div class="meta"><span class="hot">In 7 of the last 7 exams</span><span>0.25–0.3 points</span><span>15 min</span></div>

## What the exam asks

Several **sources** (machines, scanners) make items; each source has its own failure rate. Two questions:

1. What is the probability that a random item **fails**?
2. Given that it failed, what is the probability it came from **source k**?

A variant: a disease test that is "99 % accurate" for a rare disease: given a positive test, what is the probability of being sick? Usually *"provide only the final answer"*: only the number counts.

## The idea in one minute

Percentages of percentages are confusing. **Counts** are not. Pretend you have exactly 1000 items and follow them:

<div class="widget" data-w="bayes"></div>

That is all there is. The two formulas below are the same steps written with symbols ($P(A\mid B)$ reads "probability of $A$ **given** $B$"):

<div class="key" markdown>

$$P(D)=\sum_k P(D\mid M_k)\,P(M_k)\qquad\qquad P(M_k\mid D)=\frac{P(D\mid M_k)\,P(M_k)}{P(D)}$$

</div>

## The recipe

!!! recipe key "Bayes with counts"
    1. Pretend there are **1000** items (1 000 000 if a probability is tiny, like 0.0005).
    2. **Split by source**: count$_k$ = share$_k$ × 1000.
    3. **Bad ones per source**: bad$_k$ = rate$_k$ × count$_k$.
    4. $P(\text{bad})$ = (sum of bad$_k$) / 1000.
    5. $P(\text{source }k\mid\text{bad})$ = bad$_k$ / (sum of bad$_k$). Divide by the **pile**, not by 1000.

## Watch it once: June 2026 · 1b

!!! exam "Resit, June 2026 · 1b · 0.3 p"
    Machines $M_1$, $M_2$, $M_3$ produce 40 %, 35 % and 25 % of the chips. The probability that a chip is defective is 2 % for $M_1$, 4 % for $M_2$, and 5 % for $M_3$. **Provide only the final answer.**
    1. What is the probability that a randomly selected chip will be defective? [0.15]
    2. If a chip is found to be defective, what is the probability that it was produced by $M_2$? [0.15]

<div class="stepper" markdown>

**Step 1 · 1000 chips, split by machine.** $400$ from $M_1$, $350$ from $M_2$, $250$ from $M_3$.

***

**Step 2 · Defective in each.** $0.02\times400=8$, $\ 0.04\times350=14$, $\ 0.05\times250=12.5$.

***

**Step 3 · Total.** $8+14+12.5=34.5$ defective out of 1000: $P(D)=\mathbf{0.0345}$.

***

**Step 4 · Given defective.** $P(M_2\mid D)=\dfrac{14}{34.5}=\mathbf{0.41}$.

</div>

## Your turn

!!! exam "Final exam, 13 April 2025 · 1a · 0.3 p"
    85 % of the images from CT1 have sufficient quality; for CT2 and CT3 it is 90 % and 66 %. Each day CT1 scans 18 patients, CT2 22, CT3 15. Images are mixed at random before quality control. **Provide only the final answer.**
    1. What is the probability that one image will NOT pass the quality test?
    2. What is the probability that a bad quality image comes from CT2?

??? solution "Check your answer"
    Two twists: the counts are already given (18 + 22 + 15 = 55 patients, use them instead of 1000), and the rates are for **good** images, so bad = 1 − good: 15 %, 10 %, 34 %.

    Bad: $18\times0.15=2.7$, $\ 22\times0.10=2.2$, $\ 15\times0.34=5.1$. Pile: $10$.

    !!! answer "Answer"
        1. $10/55=0.18$. 2. $2.2/10=0.22$.

!!! exam "Final exam, April 2024 · 1b · 0.25 p"
    The probability of having tuberculosis (TB) is 0.0005, and a test for TB is 99 % accurate. What is the probability one has TB if one tests positive? **Provide only the final answer.**

??? solution "Check your answer"
    "99 % accurate" = sick people test positive 99 % of the time **and** healthy people test negative 99 % of the time (so 1 % of healthy people test positive).

    1 000 000 people: 500 have TB → 495 test positive. 999 500 are healthy → 1 % = 9 995 test positive. Pile of positives: $495+9995=10490$.

    !!! answer "Answer"
        $P(TB\mid+)=\frac{495}{10490}\approx0.047$. Only about 5 %: most positives are healthy people, because healthy people are so many more.

## Two small ones that also appear

**Independent events (June 2026 1a, MC).** $A$ and $B$ independent means knowing $B$ tells you nothing about $A$: $P(A\mid B)=P(A)$, equivalently $P(A\cap B)=P(A)P(B)$. Not $P(A\cap B)=0$ (that is "cannot happen together", the opposite of independent).

**"Given it survived" (April 2024 1a, MC).** $P(T\ge t)=e^{-t/5}$; it has worked for 2 years; probability it breaks in year 3?
Conditional = part / whole: $P(2\le T\lt 3\mid T\ge2)=\dfrac{P(T\ge2)-P(T\ge3)}{P(T\ge2)}=1-\dfrac{e^{-3/5}}{e^{-2/5}}=1-e^{-1/5}=1-0.819=\mathbf{0.18}$, answer (d).

## Traps

!!! trap key "Where points are lost"
    - The rate is given for the **good** items ("quality", "accurate"): convert to bad $=1-$rate.
    - Step 5 divides by the **pile of bad ones**, not by 1000.
    - Round only at the very end ("final answer only" = no partial credit).
