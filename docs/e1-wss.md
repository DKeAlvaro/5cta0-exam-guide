# 1.3 Stationary and ergodic

<div class="meta"><span class="hot">In 5 of the last 5 exams</span><span>0.25–0.3 points</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

A multiple-choice question ("which condition is required for WSS?", "the infinite dice: which statement is true?") or a small table: "for these processes, indicate if they are WSS and ergodic in the mean".

## The idea in one minute

A **random process** is a whole stack of signals. Example: infinitely many dice, each rolled forever. Die $i$ gives one signal $x_i[n]$, called a **realisation**. Stack them as rows. Now there are two ways to average:

- **Down a column**: all realisations at the same time $n$. That is the **ensemble mean** $E[X[n]]$ (what probability theory computes).
- **Along a row**: one realisation over all time. That is the **time average** (what you can measure from one recording).

Two definitions follow:

<div class="key" markdown>

- **WSS** (wide-sense stationary): the column average is the **same at every $n$**, **and** the correlation between times $n$ and $n+k$ depends **only on the gap $k$**.
- **Ergodic in the mean**: the time average of a single row **equals** the ensemble mean. (Ergodic in the variance: the same for the spread.)

</div>

Try the four tabs. In each, compare the red line (time average of row 1) with the blue dashed line (ensemble mean):

<div class="widget" data-w="ensemble"></div>

## The recipe

!!! recipe key "Is it WSS? Is it ergodic in the mean?"
    1. **Mean**: compute $E[X(t)]$ (average over the random thing: $U$, $A$, ...). If it depends on $t$ → **not WSS**, and not ergodic. Stop.
    2. **Autocorrelation**: $E[X(t)X(t+\tau)]$. If it depends only on $\tau$ → **WSS**.
    3. **Ergodic in the mean**: fix one value of the random thing (one row) and average over time. Same as step 1 for every row → **ergodic**. If the result still depends on the random thing (like $A$) → **not ergodic**.

## Watch it once: April 2024 · 1d

!!! exam "Final exam, April 2024 · 1d · 0.3 p"
    For the following random processes, indicate if they are WSS and ergodic in the mean:

    1. $X(t) = \cos(t + U)$, where $U \sim Uniform(0, 2\pi)$
    2. $X(t) = A \cos(t)$, where $A \sim N(1, 2)$

    Useful: $\cos(\alpha) \cos(\beta) = \frac{\cos(\alpha + \beta) + \cos(\alpha - \beta)}{2}$

<div class="stepper" markdown>

**Step 1 · Process 1, mean.** $U$ is a random phase spread evenly over a full turn, so averaging $\cos(t+U)$ over $U$ averages a cosine over a full period: $E[X(t)]=0$. Constant ✓. (Third tab of the widget.)

***

**Step 2 · Process 1, autocorrelation.** With the hint:
$E[\cos(t+U)\cos(t+\tau+U)]=\tfrac12E[\cos(2t+\tau+2U)]+\tfrac12\cos\tau$.
The first part is again a cosine averaged over full turns of $U$: 0. Left: $\frac12\cos\tau$, only $\tau$ ✓ → **WSS**.

***

**Step 3 · Process 1, ergodic?** One row = $\cos(t+u_1)$ with a fixed number $u_1$. Its long-time average is 0 = the ensemble mean ✓ → **ergodic in the mean**.

***

**Step 4 · Process 2, mean.** $E[A\cos t]=E[A]\cos t=1\cdot\cos t$. It **changes with $t$** → **not WSS**, and therefore not ergodic. (Fourth tab.)

***

**Answer.**

| | WSS | ergodic in the mean |
|---|---|---|
| 1. $\cos(t+U)$ | Yes | Yes |
| 2. $A\cos t$ | No | No |

</div>

## The dice question (asked twice, same answer)

!!! exam "January 2022 1c and April 2025 1d"
    Suppose we have infinitely many fair dice and define a random process as the ensemble of the random signals obtained by rolling each die infinitely many times and recording the number on the upward face. Which statement is true?

??? solution "Check your answer"
    **What is being asked?** Which statement about "infinitely many dice, each rolled forever" is true — mainly: is this process ergodic?

    **Step 1 · What a row is.** One die rolled forever is one realisation. Its **time average**: a fair die shows each face in $\frac16$ of its rolls, so the average is $1\cdot\frac16+\dots+6\cdot\frac16=3.5$.

    **Step 2 · What a column is.** Fix a time $n$ and look at all dice at once (**ensemble**): each face again in $\frac16$ of them, so the ensemble average is the same 3.5.

    **Step 3 · Compare.** Time average of any single row $=$ ensemble mean → **ergodic in the mean**. The same argument for the spread (the variance $\frac{35}{12}$ of one roll) → **also ergodic in the variance**.

    **Step 4 · Kill the wrong options.** "Only in the mean" understates it. "$E[X]=0$" confuses dice with zero-mean noise: the mean here is 3.5.

    !!! answer "Answer"
        **Ergodic in both the mean and the variance** (option (b) both times). Not "only in the mean", and not "$E[X]=0$" (it is 3.5).

## Test yourself

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| WSS requires: mean constant and autocorrelation depending only on the lag. | T | That is the definition (June 2026 1d, answer (b)). |
| WSS means the time averages of every realisation equal the ensemble averages. | F | That is **ergodicity**, a different property. |
| WSS means the PDF stays exactly the same at every time. | F | That is (strict) stationarity, which asks much more than WSS. |
| WSS means the PSD is constant over frequency. | F | That is **white** noise. |
| $X[n]=A$ with $A$ random (a flat line at a random height) is ergodic in the mean. | F | One row always averages to its own $A$, not to $E[A]$ (second tab). |
| $X[n]=A$ with $A$ random is WSS. | T | Mean $E[A]$ and correlation $E[A^2]$ do not depend on time. WSS but not ergodic. |
| A random phase cosine $\cos(\omega n+U)$, $U$ uniform on $[0,2\pi)$, is WSS. | T | Mean 0, correlation $\frac12\cos(\omega k)$. |
| Every WSS process is ergodic. | F | The random-constant process is the counter-example. |

</div>
