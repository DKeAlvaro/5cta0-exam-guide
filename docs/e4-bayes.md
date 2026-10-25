# 4.2 Priors, costs and the theory questions

<div class="meta"><span class="hot">Theory MC in 6 of 6 recent exams</span><span>Bayes test in 3 of the last 3</span><span>0.5–1.5 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep1_detection.mp4" poster="video/pod_ep1_detection.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 1, Detection: the likelihood ratio test</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [4.1 Likelihood ratio test](e4-lrt.md) first.

## What the exam asks

1. A multiple-choice question on the vocabulary: error table, Neyman–Pearson, Bayes risk, priors.
2. A **Bayesian test**: the same LRT as in 4.1, but now you also know how often each hypothesis happens (**priors** $P_0=P(\mathcal H_0)$, $P_1=P(\mathcal H_1)$) and/or how bad each mistake is (**costs**). They ask for the threshold, or "should we accept $\mathcal H_1$?".

## The idea in one minute

If devices are present only 10 % of the time, a measurement has to be **more convincing** before you say "device". Bayes does exactly that: it multiplies each curve by its prior and decides $\mathcal H_1$ wherever the weighted $\mathcal H_1$ curve is the taller one. Drag the crossing in the picture (or slide the prior) and watch the threshold move.

<div class="widget" data-w="lrt" data-priors="1"></div>

The same thing as a formula: it is still the LRT of 4.1, only the number on the right is now fixed by priors and costs.

<div class="key" markdown>

$$
\frac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda=\frac{(C_{10}-C_{00})\,P_0}{(C_{01}-C_{11})\,P_1}
$$

</div>

$C_{ij}$ = cost of **deciding $\mathcal H_i$ when $\mathcal H_j$ is true**. So $C_{10}$ = cost of a false alarm, $C_{01}$ = cost of a miss, $C_{00}=C_{11}=0$ almost always (being right costs nothing).

| Special case | $\lambda$ | what it does |
|---|---|---|
| right costs 0, wrong costs 1 ("0/1 costs") | $\dfrac{P_0}{P_1}$ | minimises the total probability of error $P_e$ |
| 0/1 costs **and** equal priors | $1$ | maximum likelihood rule: pick the taller curve |
| misses 100× worse than false alarms | $\dfrac{P_0}{100P_1}$ | much easier to say $\mathcal H_1$ |

## The recipe

!!! recipe key "Bayesian detection"
    1. Compute $\lambda=\dfrac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$.
    2. Do the LRT of [4.1](e4-lrt.md) with that $\lambda$: ratio, log, isolate $x$, flip if needed.
    3. If they give **posteriors** instead ($P(\mathcal H_1\mid x)$ vs $P(\mathcal H_0\mid x)$): decide $\mathcal H_1$ if $\dfrac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}>\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$ (the priors are already inside the posteriors).

## Watch it once: June 2026 · 4c and April 2025 · 4c

!!! exam "Resit, June 2026 · 4b + 4c · 1 p each"
    **4b** A wireless sensor detects the presence of a transmitting device by measuring the received signal envelope $X$ (in mV). Under normal operating conditions the envelope follows a Rayleigh distribution due to multipath fading. Two hypotheses are proposed:

    1. Under $H_0$ (no device present), $X \sim \text{Rayleigh}(\sigma_0)$.
    2. Under $H_1$ (device present), $X \sim \text{Rayleigh}(\sigma_1)$,

    with $\sigma_1 > \sigma_0 > 0$, both known. The Rayleigh pdf with scale parameter $\sigma$ is $p(x \mid \sigma) = \frac{x}{\sigma^2} \exp\left(-\frac{x^2}{2\sigma^2}\right)$, $x \geq 0$.

    - Construct the likelihood-ratio test for a threshold $\eta$.
    - Discuss how the separation between $\sigma_0$ and $\sigma_1$ affects detection performance.

    **4c** Now assume prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$, reflecting the fact that a transmitting device is present only 10 % of the time. Assume equal costs for false alarms and miss-detections. When should the sensor accept $H_1$?

<div class="stepper" markdown>

**Step 1 · $\lambda$.** Equal costs (0/1), so the Bayes threshold is the ratio of the priors: $\lambda=\dfrac{P_0}{P_1}=\dfrac{0.9}{0.1}=9$. This is the $\eta$ of 4b: decide $H_1$ when the ratio of the two PDFs is bigger than 9.

***

**Step 2 · Reuse the LRT of 4b.** The ratio of the two Rayleigh PDFs (the $x$ in front cancels), logged and solved for $x$, gives "decide $H_1$ if $x>\gamma$" with

$$\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\frac{\sigma_1^2}{\sigma_0^2}\Big)}$$

(full derivation in [4.1 Your turn](e4-lrt.md#your-turn)). Put $\eta=9$:

$$x>\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\frac{9\sigma_1^2}{\sigma_0^2}\Big)}.$$

***

**Step 3 · Numbers, to see the effect.** Take $\sigma_0=1$, $\sigma_1=2$: the factor in front is $\frac{2\cdot1\cdot4}{4-1}=\frac83=2.67$.

- With $\eta=1$ (no prior): $\gamma=\sqrt{2.67\ln 4}=\sqrt{2.67\cdot1.386}=\sqrt{3.70}=1.92$.
- With $\eta=9$ (the 10 % prior): $\gamma=\sqrt{2.67\ln 36}=\sqrt{2.67\cdot3.584}=\sqrt{9.56}=3.09$.

Compared with $\eta=1$ the threshold is **higher**: devices are rare, so we need a bigger envelope before we believe one is there. That is exactly what the prior does — it moves the line, not the curves.

</div>

!!! exam "Final exam, 13 April 2025 · 4c · 1 p"
    An AI agent detects whether assignments were generated with genAI. $\mathcal{H}_0$: written by a student; $\mathcal{H}_1$: generated by genAI. The student fails if the agent accepts $\mathcal{H}_1$. Assume $C_{0,1} = 100C_{1,0}$, $C_{1,1} = C_{0,0} = 0$, and that the posterior of $\mathcal{H}_0$ is 5 times smaller than the posterior of $\mathcal{H}_1$. Should the student fail the course?

<div class="stepper" markdown>

**Step 1 · Which form?** They give posteriors, so use recipe step 3: decide $\mathcal H_1$ if $\dfrac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}>\dfrac{C_{10}}{C_{01}}$.

***

**Step 2 · Numbers.** Left side: the posterior of $\mathcal H_0$ is 5 times smaller, so the ratio is $5$. Right side: $\dfrac{C_{10}}{100\,C_{10}}=0.01$.

***

**Step 3 · Decide.** $5>0.01$, so accept $\mathcal H_1$: **yes, the student fails.**

</div>

## Your turn

!!! exam "Final exam, 7 November 2022 · 4f, 4g · 0.5 p each"
    $p(y;\mathcal H_0)=e^{-y}$, $p(y;\mathcal H_1)=2e^{-2y}$ for $y\ge0$. Priors $P_0 = 0.4$ and $P_1 = 0.6$; costs $C_{1,1} = C_{0,0} = 0$, $C_{0,1} = C_{1,0} = 1$, so we decide $\mathcal H_1$ when $p(y|\mathcal{H}_1)P_1 > p(y|\mathcal{H}_0)P_0$.

    **4f** Find the threshold $\gamma''$, i.e. the value of $y$ for which $p(y|\mathcal{H}_1)P_1 = p(y|\mathcal{H}_0)P_0$.

    **4g** Determine $P_M$ and $P_{FA}$ for this test.

??? solution "Check your answer"
    **What is being asked?** Two exponential densities with unequal priors. 4f: the $y$ where the two **prior-weighted** curves cross. 4g: the two error probabilities of the rule that comes from that crossing.

    **4f · Step 1 · Write the weighted curves.** Each density gets multiplied by its prior: $p(y\mid\mathcal H_1)P_1=0.6\cdot2e^{-2y}=1.2\,e^{-2y}$ and $p(y\mid\mathcal H_0)P_0=0.4\,e^{-y}$.

    **4f · Step 2 · At $y=0$ which is higher?** $1.2\,e^{0}=1.2$ versus $0.4\,e^{0}=0.4$: the weighted $\mathcal H_1$ curve starts **higher**. Since $e^{-2y}$ dies faster than $e^{-y}$, the curves cross exactly once — the threshold.

    **4f · Step 3 · Set them equal.** $1.2\,e^{-2y}=0.4\,e^{-y}$. Divide both sides by $0.4\,e^{-2y}$: $\dfrac{1.2}{0.4}=e^{-y}e^{2y}=e^{y}$ → $3=e^{y}$ → $\gamma''=\ln3\approx1.10$.

    **4f · Step 4 · The rule.** $\mathcal H_1$ wins left of the crossing (where its weighted curve is taller): **decide $\mathcal H_1$ for $y<\ln3$**, $\mathcal H_0$ for $y>\ln3$. (This detector decides $\mathcal H_1$ for *small* $y$ — the densities make small values the $\mathcal H_1$ side.)

    **4g · Step 5 · $P_{FA}$.** False alarm = decide $\mathcal H_1$ while $\mathcal H_0$ is true, i.e. $y<\ln3$ with the $\mathcal H_0$ density:

    $$P_{FA}=\int_0^{\ln3}e^{-y}dy=\Big[-e^{-y}\Big]_0^{\ln3}=1-e^{-\ln3}=1-\frac13=\frac23.$$

    **4g · Step 6 · $P_M$.** Miss = decide $\mathcal H_0$ while $\mathcal H_1$ is true, i.e. $y>\ln3$ with the $\mathcal H_1$ density:

    $$P_M=\int_{\ln3}^{\infty}2e^{-2y}dy=\Big[-e^{-2y}\Big]_{\ln3}^{\infty}=e^{-2\ln3}=\frac{1}{3^2}=\frac19.$$

    **4g · Step 7 · Sanity check.** Both areas are between 0 and 1 ✓. The total error of the test is $0.4\cdot\frac23+0.6\cdot\frac19=0.267+0.067=0.33$, better than the best lazy rule (always decide $\mathcal H_1$: error $P_0=0.4$) ✓.

    !!! answer "Answer"
        $\gamma''=\ln3\approx1.10$ (decide $\mathcal H_1$ for $y<\ln 3$); $P_{FA}=\frac23$, $P_M=\frac19$.

## The theory questions: test yourself

The exam keeps recycling the same statements, often with one word swapped ("maximised" ↔ "minimised"). The error table first:

| you decided ↓ / truth → | $\mathcal H_0$ true | $\mathcal H_1$ true |
|---|---|---|
| $\mathcal H_0$ | true negative (correct) | **miss** = false negative = type II error |
| $\mathcal H_1$ | **false alarm** = false positive = type I error | **detection** = true positive |

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| The Neyman–Pearson test fixes $P_{FA}$ and then **maximises** $P_D$. | T | You pick the false-alarm rate you can live with, then catch as many as possible. Why, with numbers: [4.1](e4-lrt.md#the-theory-questions-test-yourself). (Nov 2022 4b, Apr 2024 4a, Apr 2025 4b.) |
| The Neyman–Pearson test fixes $P_{FA}$ and then **minimises** $P_D$. | F | The same sentence with the verb swapped: minimising $P_D$ means catching as few as possible. |
| Bayesian detection chooses the decision regions so that the Bayes risk is **maximised**. | F | The risk is the average cost of your mistakes — you always **minimise** an average cost. Maximising it would build the worst possible detector. |
| With costs $C_{01}=C_{10}=1$, $C_{00}=C_{11}=0$, the Bayes test minimises the total probability of error. | T | With 0/1 costs, the risk *is* the error probability. Same with $C_{01}=C_{10}=10$: scaling all costs does not move the threshold. |
| Equal priors and equal costs reduce the Bayes rule to the maximum likelihood rule. | T | $\lambda=1$: just pick the taller curve. |
| A higher $P(\mathcal H_0)$ raises the threshold $\eta$, so you need stronger evidence for $\mathcal H_1$. | T | $\eta=P_0/P_1$ grows with $P_0$. |
| Increasing $P(\mathcal H_1)$ raises $\eta$, making it harder to decide $\mathcal H_1$. | F | It **lowers** $\eta$: $\mathcal H_1$ gets easier (June 2026 4a, the FALSE one). |
| "Type I error" is a false alarm. | T | Decide $\mathcal H_1$ while $\mathcal H_0$ is true. A miss is type II. |
| An ROC curve plots $P_D$ (up) against $P_{FA}$ (right); the closer to the top-left corner, the better. | T | Top-left = high detection with few false alarms. The diagonal is guessing. |
| A detector whose ROC lies below the diagonal is useless. | F | Swap its decisions and it lands above the diagonal. |
| The matched filter maximises the output SNR for a known signal in white noise. | T | It correlates the data with the known pattern (biggest weights on the biggest samples). The other two options of Jan 2022 4a ($h[n]=s[n]$, "only for uncorrelated noise") are false — see [4.1](e4-lrt.md#the-theory-questions-test-yourself). |

</div>
