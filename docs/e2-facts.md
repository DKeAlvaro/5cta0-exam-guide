# 2.4 Estimation: the theory questions

<div class="meta"><span class="hot">In 6 of the last 6 exams</span><span>0.5 point each</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep4_quiz.mp4" poster="video/pod_ep4_quiz.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 4, Rapid-fire true or false</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [2.1 MLE](e2-mle.md) and [2.2 MAP](e2-map.md).

## The idea in one minute

One multiple-choice question per paper, "which statement is TRUE / FALSE", built from the same dozen ideas. But the sentences are **never printed word for word** the same twice: the examiner rephrases them, and the false ones are rephrased with **one word swapped**. So you do not memorise sentences — you memorise the **fact**, and then you hunt the swap.

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

The exam says **"which of the following statements"** in Part 2, about MLE / MAP / MMSE / Fisher / CRLB → you open **box 2D** on your A4 sheet. It is **not** a list of exam sentences to match — it is a table of **facts with their false twins**, and above it the procedure that works on any wording.

!!! sheet "Box 2D, exactly as it is printed on the sheet"
    IF YOU SEE "which of the following statements" (in Part 2) about MLE, MAP, MMSE, Fisher, CRLB

    **Kill any T/F with the swap test.** A FALSE option is a TRUE sentence with ONE word swapped: hunt *always · regardless · strictly · maximise/minimise · mean↔maximum*. No swap word → TRUE. Paraphrase? Match the idea, not the words.

    | The fact (true) | The lie they print (false) |
    |---|---|
    | MMSE = **mean** of the posterior; MAP = **maximum** | the two swapped |
    | MMSE = MAP for a symmetric one-peak posterior | "**always** different" / "always equal" |
    | MAP = likelihood × prior, needs a prior (Jun26 c) | "MAP→MLE **regardless of** the prior" · "Bayesians skip priors" |
    | Bayes estimate **minimises** the Bayes risk (Nov22 b) | "maximises" |
    | Quadratic cost → MMSE; uniform cost → MAP | "uniform cost → MMSE" |
    | MLE = argmax of the likelihood **over $\theta$** | "over $x$" · "only linear models" |
    | MLE is **asymptotically** unbiased and efficient | "**always** reaches the CRLB" |
    | Invariance: $\alpha=\psi(\theta)$ 1-to-1 → $\hat\theta=\psi^{-1}(\hat\alpha)$ (Jan22 c) | — |
    | Fisher of $N$ iid $=N\,i(\theta)$, $\mathcal I\ge0$; $\mathrm{Var}(\hat\theta)\ge\frac1{\mathcal I(\theta)}$ | "$\mathcal I$ strictly negative" · "$\ge\mathcal I(\theta)$" |
    | CRLB $=\frac1{N i(\theta)}$ shrinks $\sim\frac1N$ (Jan22 b) | "**always** derivable" (no, if range of $x$ depends on $\theta$) |
    | efficient = variance **equal to** the CRLB | "**below** the CRLB" |

    Fisher info for "$x$ = signal($\theta$) + Gaussian noise $\sigma^2$": $\mathcal I=\frac1{\sigma^2}\sum\big(\frac{d\,\text{signal}}{d\theta}\big)^2$.

    *Nov22* $A[\cos\theta,\sin\theta]$ → $\mathcal I=\frac{A^2}{\sigma^2}$, and MLE $\hat\theta=\arctan\frac{x_2}{x_1}$.

## 1 · June 2026 · 2a — the MAP family

!!! exam "Resit Q4, June 2026 · 2a · 0.5 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) The MAP estimate always equals the posterior mean.
    - (b) As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior.
    - (c) The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution.

!!! sheet "In the cheat sheet: box 2D — run the swap test on each option"
    <div class="stepper" markdown>

    **Sheet step 1 · option (a): hunt the swap.**
    Fact: *"MMSE = **mean** of the posterior; MAP = **maximum**"* — the option swaps them (MAP = mean). F.

    ***

    **Sheet step 2 · option (b): hunt the swap.**
    The tell-word is *"regardless"*, one of the printed swap words. Fact row: *"MAP→MLE **regardless of** the prior"* is the lie. F.

    ***

    **Sheet step 3 · option (c): any swap word? No.**
    Fact: *"MAP = likelihood × prior, needs a prior"* — the option says the same idea in more words. No swapped word → **TRUE** (and the sheet tags it "(Jun26 c)").

    ***

    **Sheet check · the method.**
    You never matched a sentence — you matched the **idea** and looked for the tell-word. That is what survives a rephrasing.

    </div>

!!! answer "Answer"
    **(c)**

## 2 · April 2025 · 2a, April 2024 · 2b, January 2022 · 2d — the same idea, three papers

!!! exam "Final exam Q3, 13 April 2025 · 2a · 0.5 p"
    Which of the following statements is FALSE?

    - a) The MLE is the argument maximising the likelihood.
    - b) The MMSE estimate results from minimising the square error.
    - c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

!!! exam "Final exam Q3, April 2024 · 2b · 0.5 p / Resit, 24 January 2022 · 2d · 0.3 p (same idea, other wording)"
    Which of the following statements is TRUE?

    - (a) In Bayesian estimation, the minimum mean square error is the mean of the posterior PDF.
    - (b) In Bayesian estimation, the minimum mean square error is the maximum of the posterior PDF.
    - (c) … the two estimators will always result in a different estimate.

!!! sheet "In the cheat sheet: box 2D, the first two fact rows"
    <div class="stepper" markdown>

    **Sheet step 1 · the idea behind all six options is two rows.**
    *"MMSE = **mean** of the posterior; MAP = **maximum**"* and *"MMSE = MAP for a symmetric one-peak posterior"*.

    ***

    **Sheet step 2 · swap test, Apr25 (asks FALSE).**
    (a) "MLE = the argument maximising the likelihood" = the fact row, no swap → T. (b) "MMSE results from minimising the square error" = the fact row, no swap → T. (c) tells on itself with *"always"* — the row's lie is exactly *"**always** different"* → **F** = the answer.

    ***

    **Sheet step 3 · swap test, Apr24/Jan22 (asks TRUE).**
    (a)/(b) are the two halves of the mean↔maximum swap: only the **mean** version is the fact → Apr24 (a), Jan22 (b). (c) is the "always" lie again → F.

    ***

    **Sheet check · the method.**
    Six options, two fact rows, one swap word. The exam cannot change the idea, only the wording.

    </div>

!!! answer "Answer"
    Apr25-2a **(c)** · Apr24-2b **(a)** · Jan22-2d **(b)**

## 3 · November 2022 · 2c — Bayes risk and the cost function

!!! exam "Final exam Q1, 7 November 2022 · 2c · 0.25 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) Unlike classical estimators, Bayesian estimators do not incorporate prior knowledge about the unknown parameter.
    - (b) The Bayesian estimate is the estimate that minimizes the Bayes risk, i.e., $\hat{\theta} = \arg \min_{\hat{\theta}} \int \int C(e)p(\theta|\mathbf{x})d\theta p(\mathbf{x})d\mathbf{x}$.
    - (c) Minimizing Bayes Risk for the uniform error cost function results in the minimum mean square error estimator.

!!! sheet "In the cheat sheet: box 2D, the Bayes rows"
    <div class="stepper" markdown>

    **Sheet step 1 · (a) = the "Bayesians skip priors" lie.**
    The fact row *"MAP = likelihood × prior, needs a prior"* kills it: the prior is what makes an estimator Bayesian. F.

    ***

    **Sheet step 2 · (b) = the fact, no swap.**
    *"Bayes estimate **minimises** the Bayes risk"* — the option says "minimizes" and adds the integral definition. **T** (tagged "(Nov22 b)").

    ***

    **Sheet step 3 · (c) = the cost row, swapped.**
    *"Quadratic cost → MMSE; uniform cost → MAP"* — the option says uniform cost → MMSE. F.

    ***

    **Sheet check · the method.**
    (b) is true *because no word moved*. That is the whole procedure.

    </div>

!!! answer "Answer"
    **(b)**

## 4 · November 2022 · 2a and April 2024 · 2a — the Fisher trio (asked twice)

!!! exam "Final exam Q1, 7 November 2022 · 2a · 0.25 p"
    Which of the following statements about the Fisher information $\mathcal{I}(\theta)$ is TRUE?

    - (a) The Fisher information for $N$ identical and independent distributed observations is $Ni(\theta)$, where $i(\theta)$ is the Fisher information for a single observation.
    - (b) The variance of any unbiased estimator is lower bounded by the Fisher information, i.e., $\text{Var}(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - (c) The Fisher information $\mathcal{I}(\theta)$ is strictly negative.

!!! exam "Final exam Q3, April 2024 · 2a · 0.5 p (the same three ideas, shuffled: answer **(c)**)"

!!! sheet "In the cheat sheet: box 2D, the merged Fisher row"
    <div class="stepper" markdown>

    **Sheet step 1 · the row.**
    *"Fisher of $N$ iid $=N\,i(\theta)$, $\mathcal I\ge0$; $\mathrm{Var}(\hat\theta)\ge\frac1{\mathcal I(\theta)}$"*. Three options come out of this one row.

    ***

    **Sheet step 2 · swap test.**
    (a) restates the row's first half in other words ("information adds over independent observations") → T. (b) swaps $\frac1{\mathcal I}$ for $\mathcal I$ → F. (c) adds *"strictly"* — a printed swap word — and the row says $\mathcal I\ge0$ → F.

    ***

    **Sheet check · the method.**
    Same row, both papers. If the paper asks for the FALSE one instead (a 2023 resit did), read the verdict column backwards: (b) becomes the answer.

    </div>

!!! answer "Answer"
    Nov22-2a **(a)** · Apr24-2a **(c)**

## 5 · January 2022 · 2a — the CRLB trio

!!! exam "Resit, 24 January 2022 · 2a · 0.3 p"
    Which of the following statements about the Cramer Rao lower bound is true?

    - (a) The Cramer Rao lower bound can always be derived.
    - (b) For identical and independent distributed observations, the Cramer Rao lower bound decreases linearly with the number of observations.
    - (c) An estimator whose variance is lower than the Cramer Rao lower bound is called efficient.

!!! sheet "In the cheat sheet: box 2D, the last two rows"
    <div class="stepper" markdown>

    **Sheet step 1 · (a): the tell-word is "always".**
    *"CRLB … **always** derivable"* is the printed lie: not if the range of $x$ depends on $\theta$. F.

    ***

    **Sheet step 2 · (b): no swap word.**
    *"CRLB $=\frac1{N i(\theta)}$ shrinks $\sim\frac1N$"* — "decreases linearly with the number of observations" is the same idea (the bound shrinks in proportion to $1/N$), tagged "(Jan22 b)". T.

    ***

    **Sheet step 3 · (c): the swap is "lower than".**
    *"efficient = variance **equal to** the CRLB"*; the row's lie is *"**below** the CRLB"*. F.

    ***

    **Sheet check · the method.**
    (b) is a paraphrase of the row and it is still true — exactly the situation you feared. The swap test handles it: nothing moved, so it is T.

    </div>

!!! answer "Answer"
    **(b)**

## Paraphrase drill — the sentences you have never seen

The exam rewrites these sentences every year. Here they are in **fresh wording**, none taken from a paper. Run the swap test on each, then compare.

<div class="stepper" markdown>

**1 · "The expected posterior mean minimises the mean squared error."**
No swap word; it is the MMSE fact ("mean of the posterior, minimises squared error") in different clothes → **T**.

***

**2 · "For independent observations the total Fisher information is the sum of the per-observation informations."**
Paraphrase of $N\,i(\theta)$; nothing swapped → **T**.

***

**3 · "An efficient estimator is one whose variance is smaller than the Cramér–Rao bound."**
Swap: *smaller than* replaces *equal to* → **F**.

***

**4 · "With enough observations the MAP estimate becomes the MLE whatever the prior."**
Swap: *whatever the prior* = the printed *regardless* lie → **F**.

***

**5 · "The Cramér–Rao bound is the smallest variance an estimator can achieve."**
Swap: the row says "any **unbiased** estimator" — dropping that word makes it false (a biased one can go below) → **F**.

***

**6 · "Maximum likelihood and minimum mean-square-error estimation agree when the posterior is symmetric with a single peak."**
Same idea as "MMSE = MAP for a symmetric one-peak posterior", no swap → **T**.

</div>

## If they ask you to compute the Fisher information

Rare, but the sheet has the formula under the table: for $x$ = signal$(\theta)$ + Gaussian noise $\sigma^2$,

$$\mathcal I=\frac1{\sigma^2}\sum\left(\frac{d\,\text{signal}}{d\theta}\right)^2$$

*Nov22* exam 2e gives $x=A[\cos\theta,\sin\theta]+w$: the sheet's example line answers it — $\mathcal I=\frac{A^2}{\sigma^2}$, and the MLE is $\hat\theta=\arctan\frac{x_2}{x_1}$.

To compute the CRLB itself (also rare since 2022):

!!! recipe "CRLB in 3 steps"
    1. Log of one sample: $\ln p(x\mid\theta)$.
    2. Second derivative in $\theta$, then take minus its expected value: $i(\theta)=-E\big[\frac{\partial^2}{\partial\theta^2}\ln p(x\mid\theta)\big]$.
    3. $\text{CRLB}=\dfrac{1}{N\,i(\theta)}$. First check that the range of $x$ does not depend on $\theta$; if it does, say "not possible" (that is the sheet's row about "always derivable").

## Traps

!!! trap key "Where points are lost (each one is a swap word you did not see)"
    - Matching the exam's sentence to the sheet's wording instead of to the **fact**. The wording never repeats; the idea always does.
    - Missing the swap words: *always · regardless · strictly · whatever · any · only*. One of them and the sentence is false.
    - Not reading the question word: some papers ask "which is TRUE", others "which is FALSE" (Apr25 2a).
    - Mean vs maximum: MMSE = **mean**, MAP = **maximum**. The simplest swap of all.
    - Dropping a qualifier: "any estimator" instead of "any **unbiased** estimator" flips the CRLB sentence (drill 5).
    - Writing $\text{Var}\ge\mathcal I$ instead of $\text{Var}\ge\frac1{\mathcal I}$ — the reciprocal is the swap in that row.
