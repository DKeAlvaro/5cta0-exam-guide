# 2.4 Estimation: the theory questions

<div class="meta"><span class="hot">In 6 of the last 6 exams</span><span>0.5 point each</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep4_quiz.mp4" poster="video/pod_ep4_quiz.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 4, Rapid-fire true or false</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [2.1 MLE](e2-mle.md) and [2.2 MAP](e2-map.md).

## The idea in one minute

One multiple-choice question per paper, "which statement is TRUE / FALSE", built from the same dozen sentences — several have appeared **word for word** two or three times. So you don't learn theory here: you learn the **one-line meanings** and then you read the answers off the sheet's table.

| word | meaning |
|---|---|
| estimator $\hat\theta$ | a recipe that turns the data into a guess for $\theta$ |
| unbiased | on average it is right: $E[\hat\theta]=\theta$ |
| consistent | gets arbitrarily close to $\theta$ as $N\to\infty$ |
| Fisher information $\mathcal I(\theta)$ | how much the data tell you about $\theta$. Always $\ge0$. For $N$ independent samples: $\mathcal I=N\,i(\theta)$ |
| CRLB | no unbiased estimator has variance below $\dfrac{1}{\mathcal I(\theta)}$ |
| efficient | an unbiased estimator whose variance **equals** the CRLB |
| prior / posterior | belief about $\theta$ before / after seeing the data |
| MAP | top (mode) of the posterior |
| MMSE | **mean** of the posterior; minimises the mean squared error |
| Bayes risk | expected cost; Bayesian estimators **minimise** it |

## How to fight this section with the sheet

The exam says **"which of the following statements"** in Part 2, about MLE / MAP / MMSE / Fisher / CRLB → you open **box 2D** on your A4 sheet. It is a T/F table whose rows are the exam sentences themselves, with the verdict in the right column. Every question below is a row (or three) of that table. There is also one formula at the bottom of the box for the rare "compute the Fisher information" question.

!!! sheet "Box 2D, exactly as it is printed on the sheet"
    IF YOU SEE "which of the following statements" (in Part 2) about MLE, MAP, MMSE, Fisher, CRLB

    | Statement | T / F |
    |---|---|
    | MMSE = the **mean** of the posterior; minimises squared error | T |
    | MMSE = the maximum of the posterior | F (that is MAP) |
    | MMSE and MAP **always** give different estimates | F (same for a symmetric posterior) |
    | MAP always equals the posterior mean | F |
    | MAP depends on likelihood and prior; needs a prior | T (Jun26 c) |
    | MAP → MLE for many samples "regardless of the prior" | F |
    | Bayesian estimators do not use prior knowledge | F |
    | Bayes estimate minimises the Bayes risk | T (Nov22 b) |
    | Uniform cost → MMSE | F (uniform → MAP) |
    | MLE maximises the likelihood over $\theta$ | T ("over $x$": F) |
    | MLE is asymptotically unbiased | T (Nov22 c) |
    | MLE always reaches the CRLB / only for linear models | F |
    | MLE of $\alpha=\psi(\theta)$: $\hat\theta=\psi^{-1}(\hat\alpha)$ | T (Jan22 c) |
    | Fisher info of $N$ iid samples $=N\,i(\theta)$ | T |
    | $\mathrm{Var}(\hat\theta)\ge\mathcal I(\theta)$ | F (it is $\ge\frac1{\mathcal I}$) |
    | Fisher information is strictly negative | F (it is $\ge0$) |
    | CRLB can always be derived | F (not if the range of $x$ depends on $\theta$) |
    | Variance below the CRLB = efficient | F (efficient = equal to it) |
    | CRLB decreases as $N$ grows ($\sim\frac1N$); "decreases linearly with the number of observations" | T (Jan22 b) |

    Fisher info for "$x$ = signal($\theta$) + Gaussian noise $\sigma^2$": $\mathcal I=\frac1{\sigma^2}\sum\big(\frac{d\,\text{signal}}{d\theta}\big)^2$.

    *Nov22* $A[\cos\theta,\sin\theta]$ → $\mathcal I=\frac{A^2}{\sigma^2}$, and MLE $\hat\theta=\arctan\frac{x_2}{x_1}$.

The verdict column already names the exams: "(Jun26 c)", "(Nov22 b)", "(Jan22 b)"… the sheet is a partial answer key.

## 1 · June 2026 · 2a — the MAP family

!!! exam "Resit Q4, June 2026 · 2a · 0.5 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) The MAP estimate always equals the posterior mean.
    - (b) As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior.
    - (c) The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution.

!!! sheet "In the cheat sheet: box 2D, rows 4–6 — each option is one row"
    <div class="stepper" markdown>

    **Sheet step 1 · option (a) = row 4.**
    *"MAP always equals the posterior mean | F"* — mean vs maximum, only equal for a symmetric one-peak posterior. → out.

    ***

    **Sheet step 2 · option (b) = row 6.**
    *"MAP → MLE for many samples "regardless of the prior" | F"*. The word "regardless" is the trap: a prior that is zero at the true value can never be overruled. → out.

    ***

    **Sheet step 3 · option (c) = row 5, with the answer tag.**
    *"MAP depends on likelihood and prior; needs a prior | T (Jun26 c)"* — the sheet names this exam **and** its option letter.

    ***

    **Sheet check · the example line.**
    The verdict column says "(Jun26 c)". Circle (c), get 0.5 p.

    </div>

!!! answer "Answer"
    **(c)**

## 2 · April 2025 · 2a, April 2024 · 2b, January 2022 · 2d — the same trio, three papers

!!! exam "Final exam Q3, 13 April 2025 · 2a · 0.5 p"
    Which of the following statements is FALSE?

    - a) The MLE is the argument maximising the likelihood.
    - b) The MMSE estimate results from minimising the square error.
    - c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

!!! exam "Final exam Q3, April 2024 · 2b · 0.5 p / Resit, 24 January 2022 · 2d · 0.3 p (same options)"
    Which of the following statements is TRUE?

    - (a) In Bayesian estimation, the minimum mean square error is the mean of the posterior PDF.
    - (b) In Bayesian estimation, the minimum mean square error is the maximum of the posterior PDF.
    - (c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

!!! sheet "In the cheat sheet: box 2D, rows 1–3 and 10 — the MMSE/MAP block"
    <div class="stepper" markdown>

    **Sheet step 1 · the definition row.**
    *"MMSE = the **mean** of the posterior; minimises squared error | T"*. So Apr24/Jan22 option (a)/(b): **mean** → the first one is TRUE (Apr24 (a), Jan22 (b) — the same sentence, different letter).

    ***

    **Sheet step 2 · the "always different" row.**
    *"MMSE and MAP **always** give different estimates | F (same for a symmetric posterior)"* → the "always" option is FALSE in all three papers. Apr25 asks for the FALSE one → that is **(c)**.

    ***

    **Sheet step 3 · Apr25's (a) and (b) = rows 1 and 10.**
    *"MMSE = the mean … minimises squared error | T"* → (b) "results from minimising the square error" TRUE. *"MLE maximises the likelihood over $\theta$ | T"* → (a) TRUE. So the FALSE one really is (c) — and the sheet's row even explains why: mean = mode for a symmetric posterior.

    ***

    **Sheet check · the example line.**
    Three exams, five rows of the table, zero thinking. If an option does not match a row word for word, find the row it paraphrases — the wording never strays far.

    </div>

!!! answer "Answer"
    Apr25-2a **(c)** · Apr24-2b **(a)** · Jan22-2d **(b)**

## 3 · November 2022 · 2c — Bayes risk and the cost function

!!! exam "Final exam Q1, 7 November 2022 · 2c · 0.25 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) Unlike classical estimators, Bayesian estimators do not incorporate prior knowledge about the unknown parameter.
    - (b) The Bayesian estimate is the estimate that minimizes the Bayes risk, i.e., $\hat{\theta} = \arg \min_{\hat{\theta}} \int \int C(e)p(\theta|\mathbf{x})d\theta p(\mathbf{x})d\mathbf{x}$.
    - (c) Minimizing Bayes Risk for the uniform error cost function results in the minimum mean square error estimator.

!!! sheet "In the cheat sheet: box 2D, rows 7–9"
    <div class="stepper" markdown>

    **Sheet step 1 · option (a) = row 7.**
    *"Bayesian estimators do not use prior knowledge | F"* — backwards; the prior is exactly what makes them Bayesian. → out.

    ***

    **Sheet step 2 · option (b) = row 8, with the answer tag.**
    *"Bayes estimate minimises the Bayes risk | T (Nov22 b)"* — the sheet names this exam and this option. The double integral in the option is just "average the cost over the posterior and over the data". → **(b)**.

    ***

    **Sheet step 3 · option (c) = row 9.**
    *"Uniform cost → MMSE | F (uniform → MAP)"* — the uniform (hit-or-miss) cost gives the MAP; the **quadratic** cost gives the MMSE. → out.

    </div>

!!! answer "Answer"
    **(b)**

## 4 · November 2022 · 2a and April 2024 · 2a — the Fisher trio (asked twice)

!!! exam "Final exam Q1, 7 November 2022 · 2a · 0.25 p"
    Which of the following statements about the Fisher information $\mathcal{I}(\theta)$ is TRUE?

    - (a) The Fisher information for $N$ identical and independent distributed observations is $Ni(\theta)$, where $i(\theta)$ is the Fisher information for a single observation.
    - (b) The variance of any unbiased estimator is lower bounded by the Fisher information, i.e., $\text{Var}(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - (c) The Fisher information $\mathcal{I}(\theta)$ is strictly negative.

!!! exam "Final exam Q3, April 2024 · 2a · 0.5 p (the same three statements, shuffled: answer **(c)**)"

!!! sheet "In the cheat sheet: box 2D, rows 14–16"
    <div class="stepper" markdown>

    **Sheet step 1 · "$N$ i.i.d. observations" = row 14.**
    *"Fisher info of $N$ iid samples $=N\,i(\theta)$ | T"* — information of independent observations adds. Nov22 (a) TRUE, Apr24 (c) TRUE.

    ***

    **Sheet step 2 · "$\text{Var}\ge\mathcal I$" = row 15.**
    *"$\mathrm{Var}(\hat\theta)\ge\mathcal I(\theta)$ | F (it is $\ge\frac1{\mathcal I}$)"* — the bound is **one over** the information. Same sentence in both papers → FALSE.

    ***

    **Sheet step 3 · "strictly negative" = row 16.**
    *"Fisher information is strictly negative | F (it is $\ge0$)"*. → FALSE in both papers.

    ***

    **Sheet check · the example line.**
    In both papers exactly one statement is TRUE and it is the "$N\,i(\theta)$" one: Nov22 **(a)**, Apr24 **(c)**. (A resit variant flips the question to "which is FALSE" — then read the verdict column backwards and pick the F row.)

    </div>

!!! answer "Answer"
    Nov22-2a **(a)** · Apr24-2a **(c)**

## 5 · January 2022 · 2a — the CRLB trio

!!! exam "Resit, 24 January 2022 · 2a · 0.3 p"
    Which of the following statements about the Cramer Rao lower bound is true?

    - (a) The Cramer Rao lower bound can always be derived.
    - (b) For identical and independent distributed observations, the Cramer Rao lower bound decreases linearly with the number of observations.
    - (c) An estimator whose variance is lower than the Cramer Rao lower bound is called efficient.

!!! sheet "In the cheat sheet: box 2D, rows 17–19 — and row 19 names this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · option (a) = row 17.**
    *"CRLB can always be derived | F (not if the range of $x$ depends on $\theta$)"*. → out.

    ***

    **Sheet step 2 · option (b) = row 19, with the answer tag.**
    *"CRLB decreases as $N$ grows ($\sim\frac1N$); "decreases linearly with the number of observations" | T (Jan22 b)"*. The row quotes the exam's own wording and marks it T.

    ***

    **Sheet step 3 · option (c) = row 18.**
    *"Variance below the CRLB = efficient | F (efficient = equal to it)"* — going below the bound is impossible for unbiased estimators. → out.

    ***

    **Sheet check · the example line.**
    The tag "(Jan22 b)" is literally the answer to this question.

    </div>

!!! answer "Answer"
    **(b)**

## If they ask you to compute the Fisher information

Rare, but the sheet has the formula under the table: for $x$ = signal$(\theta)$ + Gaussian noise $\sigma^2$,

$$\mathcal I=\frac1{\sigma^2}\sum\left(\frac{d\,\text{signal}}{d\theta}\right)^2$$

*Nov22* exam 2e gives $x=A[\cos\theta,\sin\theta]+w$: the sheet's example line answers it — $\mathcal I=\frac{A^2}{\sigma^2}$, and the MLE is $\hat\theta=\arctan\frac{x_2}{x_1}$.

To compute the CRLB itself (also rare since 2022):

!!! recipe "CRLB in 3 steps"
    1. Log of one sample: $\ln p(x\mid\theta)$.
    2. Second derivative in $\theta$, then take minus its expected value: $i(\theta)=-E\big[\frac{\partial^2}{\partial\theta^2}\ln p(x\mid\theta)\big]$.
    3. $\text{CRLB}=\dfrac{1}{N\,i(\theta)}$. First check that the range of $x$ does not depend on $\theta$; if it does, say "not possible" (that is the sheet's row 17).

## Traps

!!! trap key "Where points are lost (each one is a row of the sheet you skipped)"
    - Not reading the question word: some papers ask "which is TRUE", others "which is FALSE" (Apr25 2a). The sheet's verdict column is T/F — read it in the direction the question asks.
    - "Always" words. The sheet's F rows are almost all killed by "always" / "regardless": MMSE≠MAP always, MAP→MLE regardless of the prior, CRLB always derivable. One counter-example and the sentence dies.
    - Confusing mean and maximum: MMSE = **mean**, MAP = **maximum** of the posterior. Two sheet rows, opposite verdicts.
    - Writing $\text{Var}\ge\mathcal I$ instead of $\text{Var}\ge\frac1{\mathcal I}$ — row 15 prints the reciprocal trap explicitly.
    - Calling "variance below the CRLB" efficient. Row 18: efficient = **equal** to it.
    - Forgetting that "uniform cost → MMSE" is the FALSE twin: uniform cost gives the MAP, quadratic cost gives the MMSE (row 9).
