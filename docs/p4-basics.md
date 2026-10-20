# 4.1 Errors, ROC, Neyman–Pearson

<p class="lead">Detection = deciding between two explanations of the data. This page covers the vocabulary that every Part 4 question uses (the four outcomes, $P_{FA}$, $P_D$, $P_M$, ROC curves, Neyman–Pearson) and the multiple-choice questions built on it.</p>

## The idea, from zero

Two hypotheses:

- $\mathcal H_0$, the **null** hypothesis: "nothing there" (only noise, no device, the student wrote it).
- $\mathcal H_1$, the **alternative**: "something there" (signal present, device transmitting, AI-generated).

Under each hypothesis the observation $x$ has a different PDF, $p(x\mid\mathcal H_0)$ and $p(x\mid\mathcal H_1)$. Because the two PDFs overlap, some values of $x$ could come from either, so mistakes are unavoidable. A **detector** splits the axis of possible $x$ into a region where you say $\mathcal H_0$ and a region where you say $\mathcal H_1$, usually with a threshold.

### The four outcomes

| You decide ↓ / Truth → | $\mathcal H_0$ true | $\mathcal H_1$ true |
|---|---|---|
| $\mathcal H_0$ | ① true negative ($1-P_{FA}$) | ② **miss**, false negative, type II error ($P_M$) |
| $\mathcal H_1$ | ③ **false alarm**, false positive, type I error ($P_{FA}$) | ④ **detection**, true positive ($P_D$) |

Rows are what you **decide**, columns what is **true**. "Positive" = you said $\mathcal H_1$. Type I = rejecting a true $\mathcal H_0$.

### Each probability is an area

$$P_{FA}=\int_{\text{decide }\mathcal H_1}p(x\mid\mathcal H_0)\,dx,\qquad P_D=\int_{\text{decide }\mathcal H_1}p(x\mid\mathcal H_1)\,dx,\qquad P_M=1-P_D.$$

<figure markdown>
![P_FA, P_D and P_M as areas](img/gen/p4_regions.svg)
<figcaption>The same threshold (vertical line) in all three panels. $P_{FA}$ is the part of the $\mathcal H_0$ curve that falls in the "decide $\mathcal H_1$" region. $P_D$ is the part of the $\mathcal H_1$ curve in that region. $P_M$ is the rest of the $\mathcal H_1$ curve. Moving the threshold right lowers $P_{FA}$ but also lowers $P_D$: you trade one error for the other.</figcaption>
</figure>

!!! recipe "Recipe: shading questions ('indicate $P_{FA}$ and $P_M$ in the plot')"
    1. Find which side of the threshold is "decide $\mathcal H_1$". Look at the inequality, not your intuition: in Nov 2022 you decide $\mathcal H_1$ for **small** $y$.
    2. $P_{FA}$: shade under the **$\mathcal H_0$** curve on the **$\mathcal H_1$** side.
    3. $P_M$: shade under the **$\mathcal H_1$** curve on the **$\mathcal H_0$** side.

### ROC curve

Sweep the threshold from $+\infty$ to $-\infty$ and plot $P_D$ (vertical) against $P_{FA}$ (horizontal). That is the **receiver operating characteristic**.

<figure markdown>
![How to read a ROC](img/gen/p4_roc_explain.svg)
<figcaption>Every ROC starts at (0,0) (never say $\mathcal H_1$) and ends at (1,1) (always say $\mathcal H_1$). The diagonal is guessing. A good detector bends towards the top-left corner (perfect: $P_{FA}=0$, $P_D=1$). The more separated the two PDFs (higher SNR), the closer to that corner. A curve **below** the diagonal means something was swapped: flip your decision and it goes above.</figcaption>
</figure>

### Neyman–Pearson

Fix the false-alarm probability you can tolerate, $P_{FA}=\alpha$, and **maximise $P_D$**. The solution is always a **likelihood ratio test** (next page): $L(x)=\frac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\gtrless\lambda$, with $\lambda$ chosen so that $P_{FA}=\alpha$. Why constrain $P_{FA}$? Under $\mathcal H_0$ there is only noise, so its PDF is known and $P_{FA}$ can be computed.

---

## Exam questions

### November 2022 exam · 4a {#nov22-4a}

!!! exam "Final exam Q1, 7 November 2022 · 4a · 0.25 p"
    In binary hypothesis testing, we assess whether the null hypothesis $\mathcal{H}_0$ or the alternative hypothesis $\mathcal{H}_1$ is true, based on observations $\mathbf{x}$. In general, both hypotheses can cause the same observation $\mathbf{x}$ and, thus, making a wrong decision is unavoidable. We can discern four events depending on the true hypothesis and our decision, which can be summarized in the table below.

    | Decision | True $\mathcal{H}_0$ | True $\mathcal{H}_1$ |
    |---|---|---|
    | $\mathcal{H}_0$ | 1 | 2 |
    | $\mathcal{H}_1$ | 3 | 4 |

    - (a) 1= true negative, 2 = false negative/miss/type II error, 3 = false positive/false alarm/type I error, 4 = true positive/detection
    - (b) 1 = true positive/detection 2 = false negative/miss/type II error, 3 = false positive/false alarm/type I error, 4 = true negative
    - (c) 1 = true negative, 2 = false positive/false alarm/type I error, 3 = false negative/miss/type II error, 4 = true positive/detection
    - (d) 1 = false negative/miss/type II error, 2 = true negative, 3 = true positive/detection, 4 = false positive/false alarm/type I error

???+ solution "Solution"
    The diagonal (1, 4) holds the correct decisions. Cell 2 = said $\mathcal H_0$ while $\mathcal H_1$ was true = miss. Cell 3 = said $\mathcal H_1$ while $\mathcal H_0$ was true = false alarm. (b) swaps 1 and 4; (c) swaps the error types; (d) calls the diagonal errors.

    !!! answer "Answer"
        **(a)**

### November 2022 exam · 4b {#nov22-4b}

!!! exam "Final exam Q1, 7 November 2022 · 4b · 0.25 p"
    To make a decision in binary hypothesis testing, we partition the observation space in two disjoint sets $\mathcal{X}_0$ and $\mathcal{X}_1$. If the observation $\mathbf{x}$ is part of the decision region $\mathcal{X}_0$, we decide for $\mathcal{H}_0$, and we decide for $\mathcal{H}_1$ if the observation is in the decision region $\mathcal{X}_1$. For a continuous observation space, there uncountable many different partitions. The Neyman-Pearson test partitions the observation space such that

    - (a) for a fixed probability of false alarm, the probability of detection is minimized.
    - (b) for a fixed probability of false alarm, the probability of detection is maximized.
    - (c) for a fixed probability of detection, the probability of false alarm is minimized.
    - (d) the probability of false alarm is equal to the probability of detection.

???+ solution "Solution"
    NP: fix $P_{FA}=\alpha$, maximise $P_D$. (c) sounds similar but fixes the wrong quantity; (d) is the coin-flip diagonal.

    !!! answer "Answer"
        **(b)**

### April 2024 exam · 4a {#apr24-4a}

!!! exam "Final exam Q3, April 2024 · 4a · 0.5 p"
    Which statement about hypothesis testing is TRUE?

    - a) In Bayesian detection, the decision region is partitioned such that the so-called Bayesian risk is maximised.
    - b) In Bayesian detection, the cost assignment $C_{0,1} = C_{1,0} = 1, C_{1,1} = C_{0,0} = 0$ minimizes the total probability of error.
    - c) With the Neyman-Pearson test, for a fixed probability of false alarm, the probability of detection is minimized.

???+ solution "Solution"
    Risk is **minimised** (a ✗), $P_D$ is **maximised** (c ✗). With 0/1 costs the Bayes risk is $P_0P_{FA}+P_1P_M$, the total probability of error (b ✓). See [4.3](p4-bayes.md).

    !!! answer "Answer"
        **(b)**

### April 2025 exam · 4b {#apr25-4b}

!!! exam "Final exam Q3, 13 April 2025 · 4b · 0.5 p"
    Which statement about hypothesis testing is FALSE?

    - a In Bayesian detection, the decision region is partitioned such that the so-called Bayesian risk is minimised.
    - b In Bayesian detection, the cost assignment $C_{0,1} = C_{1,0} = 10, C_{1,1} = C_{0,0} = 0$ minimizes the total probability of error.
    - c With the Neyman-Pearson test, for a fixed probability of false alarm, the probability of detection is maximised.

???+ solution "Solution"
    (a) and (c) are the definitions: true. (b) is also true: with $C_{01}=C_{10}=10$ the risk is $10\,P_e$, and multiplying all costs by the same factor does not change the threshold $\lambda=\frac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$. The official 2026 solutions confirm: **as printed, all three statements are true**, so there is no false one. Same family as April 2024 4a, with the "max/min" words flipped.

    !!! answer "Answer"
        No option is false (official key). If this reappears, check each verb: risk **min**, $P_D$ **max**.

### Practice exam 2021 · 1e {#pe21-1e}

!!! exam "Practice exam, 28 October 2021 · 1e · 0.5 p"
    When plotting the receiver operating characteristic (ROC) curves, the common practice is to have the probability of detection $P_d$ on the vertical axis and the probability of false alarm $P_{fa}$ on the horizontal axis. In that case, the ROC curves should appear on the upper triangular part of the plot. Assume you are running simulations to generate ROC curves. The two hypotheses are

    $$y[n] \sim \begin{cases} \mathcal{N}(0, \sigma^2), & \text{if } \mathcal{H}_0 \\ \mathcal{N}(\mu, \sigma^2), & \text{if } \mathcal{H}_1 \end{cases},$$

    where $\mu > 0$. If your curves appeared on the lower triangular part of the plot, which one of the following cannot be the reason?

    - a) The variance of the null hypothesis $\mathcal{H}_0$ is set too high.
    - b) $\mathcal{H}_0$ and $\mathcal{H}_1$ are switched in the likelihood ratio.
    - c) The cumulative probability density function is used to calculate $P_d$.
    - d) $P_d$ and $P_{fa}$ are switched.

???+ solution "Solution"
    Below the diagonal means $P_d<P_{fa}$: the decision is "upside down". Each of (b), (c), (d) flips it: inverting the ratio decides the wrong way, using the CDF $P(y<t)$ gives $1-P_d$ instead of $P_d$, and swapping the axes mirrors the curve. A wrong variance changes *how good* the test is, not its direction: a likelihood ratio test computed from the PDFs you assume still lands above the diagonal.

    !!! answer "Answer"
        **(a)**

### Practice exam 2021 · 1f {#pe21-1f}

!!! exam "Practice exam, 28 October 2021 · 1f · 0.5 p"
    Consider the t-statistic: $t = \frac{\hat{\mu} - \mu}{\frac{\hat{\sigma}}{\sqrt{N}}}$, where $\mu$ is the mean of the distribution for the null hypothesis $\mathcal{H}_0$, $\hat{\mu}$ is the estimation of the mean, $\hat{\sigma}$ is the estimation of the standard deviation and $N$ is the number of samples. Which one of the following expressions is not correct?

    - a) Deviation of the estimated mean from the mean of the null hypothesis becomes more significant when the number of samples is larger.
    - b) When the estimated standard deviation is large, deviation of the estimated mean from the mean of the null hypothesis becomes less significant.
    - c) As the t-statistic gets smaller, there is a greater chance that the samples do not belong to the null hypothesis $\mathcal{H}_0$.
    - d) The t-statistic is a random variable itself.

???+ solution "Solution"
    $t$ measures how many standard errors $\hat\mu$ is away from the $\mathcal H_0$ mean. Larger $N$ → larger $|t|$ (a ✓). Larger $\hat\sigma$ → smaller $|t|$ (b ✓). It is computed from random data, so it is random (d ✓). (c) is backwards: a **large** $|t|$ is evidence against $\mathcal H_0$. (The t-statistic is no longer in the reader; low priority.)

    !!! answer "Answer"
        **(c)**

### Practice exam 2021 · 4a {#pe21-4a}

!!! exam "Practice exam, 28 October 2021 · 4a · 1 p (also shown as 'Resit 2021 4a' in the Part 4 review)"
    For a binary hypothesis testing problem, the distributions for the underlying hypotheses are

    $$y[n] \sim \begin{cases} \mathcal{N}(0, \sigma^2), & \text{if } \mathcal{H}_0 \\ \mathcal{N}(\mu, \sigma^2), & \text{if } \mathcal{H}_1 \end{cases}$$

    where $\sigma^2 = 1$. Given the cumulative distribution function is evaluated as $p(y < y_{th}; \mu, \sigma) = 0.5 \left( 1 + \operatorname{erf} \left( \frac{y_{th} - \mu}{\sigma\sqrt{2}} \right) \right)$ and using the table for the function $\operatorname{erf} \left( \frac{x}{\sqrt{2}} \right)$ given below (TABLE I), calculate the probability of detection $P_d$ and probability of false alarm $P_{fa}$ for the threshold values $y_{th}$ and means $\mu$ listed in TABLE II. Use the calculated $P_d$ and $P_{fa}$ values to plot receiver operating characteristics (ROC) curves, with $P_d$ in the vertical axis and $P_{fa}$ in the horizontal axis.

    TABLE I: $\operatorname{erf}(x/\sqrt2)$ for $x=-3,\dots,3$: $-0.997,\ -0.954,\ -0.683,\ 0,\ 0.683,\ 0.954,\ 0.997$.

    TABLE II: $(y_{th},\mu)$ = $(-1,1)$, $(-1,2)$, $(0,1)$, $(0,2)$, $(1,1)$, $(1,2)$, $(2,1)$, $(2,2)$, $(3,1)$, $(3,2)$; fill in $P_d$ and $P_{fa}$.

???+ solution "Solution"
    You decide $\mathcal H_1$ when $y>y_{th}$, so both are **right tails** (1 − CDF):

    $$P_{fa}=\tfrac12\Big[1-\operatorname{erf}\Big(\tfrac{y_{th}}{\sqrt2}\Big)\Big],\qquad P_d=\tfrac12\Big[1-\operatorname{erf}\Big(\tfrac{y_{th}-\mu}{\sqrt2}\Big)\Big].$$

    Read the erf table at $x=y_{th}$ for $P_{fa}$ and at $x=y_{th}-\mu$ for $P_d$:

    | $y_{th}$ | $\mu$ | $y_{th}-\mu$ | $P_d$ | $P_{fa}$ |
    |---|---|---|---|---|
    | −1 | 1 | −2 | 0.977 | 0.8415 |
    | −1 | 2 | −3 | 0.9985 | 0.8415 |
    | 0 | 1 | −1 | 0.8415 | 0.5 |
    | 0 | 2 | −2 | 0.977 | 0.5 |
    | 1 | 1 | 0 | 0.5 | 0.1585 |
    | 1 | 2 | −1 | 0.8415 | 0.1585 |
    | 2 | 1 | 1 | 0.1585 | 0.023 |
    | 2 | 2 | 0 | 0.5 | 0.023 |
    | 3 | 1 | 2 | 0.023 | 0.0015 |
    | 3 | 2 | 1 | 0.1585 | 0.0015 |

    ![ROC points](img/gen/p4_roc_pe21.svg)

    Each threshold gives one point $(P_{fa},P_d)$; add (0,0) and (1,1) and connect. $\mu=2$ lies above $\mu=1$: more separation between the means (higher SNR) gives a better detector.

    !!! trap "Read the CDF formula carefully"
        The text gives $P(y<y_{th})$. Detection and false alarm are $P(y>y_{th})$, so use **1 minus** it. Using the CDF directly is exactly the mistake from [1e](#pe21-1e) that puts the ROC below the diagonal.
