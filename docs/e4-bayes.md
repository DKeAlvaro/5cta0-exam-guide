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

!!! idea "Why $\lambda$ appears twice: it is the bar, not part of the ratio"
    The test is a sandwich of **four layers**, each built from something different:

    | layer | symbol | made of | note |
    |---|---|---|---|
    | 1 | $p(x\mid\mathcal H_1)$, $p(x\mid\mathcal H_0)$ | the **model** | the two curve heights |
    | 2 | $L(x)=\dfrac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}$ | layer 1 only | "how many times more likely under $\mathcal H_1$". **Priors and costs are not in here.** |
    | 3 | $\lambda$ (the exam writes $\eta$) | priors + costs | $\lambda=\dfrac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$ — the **bar** |
    | 4 | $\gamma$ | layers 2 + 3 | the cut on $x$: solve $L(x)>\lambda$ for $x$ |

    So there is nothing to "put inside" the LRT: the LRT **is** the sentence "compare layer 2 with layer 3". Bayes only answers *where the bar's number comes from* (priors × costs); Neyman–Pearson answers it differently (pick the bar so $P_{FA}$ is what you tolerate). Either way the ratio itself never changes.

    "Substituting $\lambda$" then just means: put the number in and solve for $x$, which turns "ratio $>9$" into "$x>\gamma(\lambda)$" — layer 4.

    One more trap: the $\lambda(\theta)=\frac{1}{1+e^{-\theta}}$ of [2.1](e2-mle.md) and [2.2](e2-map.md) is a **different lambda** — a model parameter there, unrelated to the detection threshold.

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

*(4b builds the test, 4c adds the prior. Everything is here; you never need to go back.)*

**Step 1 · What the two sentences give us.** "$P(H_0)=0.9$, $P(H_1)=0.1$" = **priors**: before looking at any measurement, the device is present only 10 % of the time. "Equal costs for false alarms and miss-detections" = the **0/1 costs** of the recipe: $C_{10}=C_{01}=1$ (each mistake hurts equally) and $C_{00}=C_{11}=0$ (being right is free).

***

**Step 2 · The threshold number.** The general rule (recipe step 1) says: decide $H_1$ when

$$\frac{p(x\mid H_1)}{p(x\mid H_0)}>\lambda=\frac{(C_{10}-C_{00})\,P_0}{(C_{01}-C_{11})\,P_1}.$$

Fill in the numbers: $\lambda=\dfrac{(1-0)\cdot0.9}{(1-0)\cdot0.1}=\dfrac{0.9}{0.1}=9$. (The exam calls this number $\eta$ in 4b; the recipe calls it $\lambda$: same thing.)

In words: the measurement must be **9 times more likely** under "device" than under "no device" before the sensor says "device" — because devices are rare, one has to be convincing.

***

**Step 3 · The ratio of the two Rayleigh PDFs.** Each PDF is $p(x\mid\sigma)=\dfrac{x}{\sigma^2}\,e^{-x^2/(2\sigma^2)}$, so

$$\frac{p(x\mid H_1)}{p(x\mid H_0)}=\frac{\dfrac{x}{\sigma_1^2}e^{-x^2/(2\sigma_1^2)}}{\dfrac{x}{\sigma_0^2}e^{-x^2/(2\sigma_0^2)}}=\frac{\sigma_0^2}{\sigma_1^2}\;e^{-\frac{x^2}{2\sigma_1^2}+\frac{x^2}{2\sigma_0^2}}$$

The $x$ on top cancels (both PDFs have it), the $\frac{1}{\sigma^2}$ flips into $\frac{\sigma_0^2}{\sigma_1^2}$, and dividing by $e^{u}$ is multiplying by $e^{-u}$, which is why the exponents subtract.

***

**Step 4 · Log, then isolate $x$.** Take $\ln$ of both sides of "ratio $>\lambda$" (the $\ln$ keeps the order because it is increasing):

$$\ln\frac{\sigma_0^2}{\sigma_1^2}+\frac{x^2}{2}\left(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\right)>\ln\lambda$$

$$\frac{x^2}{2}\underbrace{\left(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\right)}_{\text{positive, because }\sigma_1>\sigma_0}>\ln\lambda-\ln\frac{\sigma_0^2}{\sigma_1^2}=\ln\!\Big(\lambda\frac{\sigma_1^2}{\sigma_0^2}\Big)$$

(the last step uses $\ln a-\ln b=\ln\frac ab$). Multiply by 2 and divide by the bracket, $\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}=\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}$:

$$x^2>\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\lambda\frac{\sigma_1^2}{\sigma_0^2}\Big)\qquad\Longrightarrow\qquad \text{decide } H_1 \text{ if } x>\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\lambda\frac{\sigma_1^2}{\sigma_0^2}\Big)}.$$

No "flip": the bracket is positive ($\sigma_1>\sigma_0$), and the ratio grows with $x$, so big envelopes mean $H_1$.

***

**Step 5 · Put $\lambda=9$.** The answer to "when should the sensor accept $H_1$?":

$$x>\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\frac{9\,\sigma_1^2}{\sigma_0^2}\Big)}.$$

***

**Step 6 · Numbers, to see the effect.** Take $\sigma_0=1$, $\sigma_1=2$ (any pair with $\sigma_1>\sigma_0$ shows the same effect). The factor in front: $\dfrac{2\cdot1^2\cdot2^2}{2^2-1^2}=\dfrac{2\cdot4}{3}=\dfrac83=2.67$.

- $\lambda=1$ (ignore the prior): $\ln\!\big(1\cdot\frac41\big)=\ln4=1.386$; $\ 2.67\cdot1.386=3.70$; $\ \gamma=\sqrt{3.70}=1.92$.
- $\lambda=9$ (the 10 % prior): $\ln\!\big(9\cdot\frac41\big)=\ln36=3.584$ (because $\ln36=\ln4+\ln9=1.386+2.197$); $\ 2.67\cdot3.584=9.56$; $\ \gamma=\sqrt{9.56}=3.09$.

***

**Step 7 · Read the result.** With the prior the threshold **rose** from 1.92 to 3.09 mV: devices are rare, so the envelope must be bigger before the sensor believes one is there. That is all the prior does — it moves the line, not the curves.

</div>

!!! exam "Final exam, 13 April 2025 · 4c · 1 p"
    An AI agent detects whether assignments were generated with genAI. $\mathcal{H}_0$: written by a student; $\mathcal{H}_1$: generated by genAI. The student fails if the agent accepts $\mathcal{H}_1$. Assume $C_{0,1} = 100C_{1,0}$, $C_{1,1} = C_{0,0} = 0$, and that the posterior of $\mathcal{H}_0$ is 5 times smaller than the posterior of $\mathcal{H}_1$. Should the student fail the course?

<div class="stepper" markdown>

**Step 0 · Read the cost notation.** $C_{i,j}$ = cost of **deciding $\mathcal H_i$ when $\mathcal H_j$ is true**. So:

- $C_{1,0}$ = decide "genAI" while it was really a student = a **false alarm** = wrongly failing a student.
- $C_{0,1}$ = decide "student" while it was really genAI = a **miss** = letting genAI slip through.
- $C_{1,1}=C_{0,0}=0$: being right costs nothing.

And "the student fails if the agent accepts $\mathcal H_1$": **decide $\mathcal H_1$ = fail**.

***

**Step 1 · What the cost ratio tells us.** $C_{0,1}=100\,C_{1,0}$: letting genAI through is **100× worse** than wrongly accusing a student. So the exam tunes the detector to shout "genAI" easily — expect a very low bar.

***

**Step 2 · Which form of the rule?** They hand us the **posteriors** $P(\mathcal H_0\mid x)$ and $P(\mathcal H_1\mid x)$: what the agent believes *after* reading the assignment. The priors are already baked inside them, so use recipe step 3:

$$\text{decide } \mathcal H_1 \ \text{ if }\ \frac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}>\frac{C_{10}-C_{00}}{C_{01}-C_{11}}=\frac{C_{10}}{C_{01}}$$

(the $C_{00},C_{11}$ drop out because they are 0).

***

**Step 3 · The left side.** "The posterior of $\mathcal H_0$ is 5 times smaller than the posterior of $\mathcal H_1$" means $P(\mathcal H_0\mid x)=\frac{1}{5}P(\mathcal H_1\mid x)$, so

$$\frac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}=\frac{P(\mathcal H_1\mid x)}{\frac15 P(\mathcal H_1\mid x)}=5.$$

In words: the evidence makes genAI **5 times more likely** than a human.

***

**Step 4 · The right side.** $\dfrac{C_{10}}{C_{01}}=\dfrac{C_{10}}{100\,C_{10}}=\dfrac{1}{100}=0.01$. (The unknown $C_{10}$ cancels — only the ratio matters.)

***

**Step 5 · Compare.** $5>0.01$, and not by a hair: the bar is 0.01, so even a *weak* lean towards genAI would already condemn the student. Only if the evidence favoured the student by more than 100 to 1 (ratio below 0.01) would the agent acquit.

***

**Step 6 · Decide.** Accept $\mathcal H_1$: **yes, the student fails.**

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

    **4f · Step 4 · The rule — and why the inequality points left.** The LRT is always "ratio **bigger** → $\mathcal H_1$", that never flips. What changes is the direction on the $y$ axis: here the weighted ratio is

    $$\frac{p(y\mid\mathcal H_1)P_1}{p(y\mid\mathcal H_0)P_0}=\frac{1.2\,e^{-2y}}{0.4\,e^{-y}}=3\,e^{-y},$$

    which **shrinks** as $y$ grows (the $\mathcal H_1$ density $2e^{-2y}$ dies faster than $e^{-y}$). So "ratio $>1$" means "small $y$":

    $$3e^{-y}>1\ \iff\ e^{-y}>\tfrac13\ \iff\ y<\ln3 .$$

    **Decide $\mathcal H_1$ for $y<\ln3$**, $\mathcal H_0$ for $y>\ln3$. Quick check at $y=0$: weighted curves $1.2$ vs $0.4$, ratio $3>1$ → $\mathcal H_1$ ✓. Small values point to $\mathcal H_1$ because that is the curve tall near 0.

    **4g · Step 5 · $P_{FA}$.** False alarm = decide $\mathcal H_1$ while $\mathcal H_0$ is true, i.e. $y<\ln3$ with the $\mathcal H_0$ density:

    $$P_{FA}=\int_0^{\ln3}e^{-y}dy=\Big[-e^{-y}\Big]_0^{\ln3}=1-e^{-\ln3}=1-\frac13=\frac23.$$

    **4g · Step 6 · $P_M$.** Miss = decide $\mathcal H_0$ while $\mathcal H_1$ is true, i.e. $y>\ln3$ with the $\mathcal H_1$ density:

    $$P_M=\int_{\ln3}^{\infty}2e^{-2y}dy=\Big[-e^{-2y}\Big]_{\ln3}^{\infty}=e^{-2\ln3}=\frac{1}{3^2}=\frac19.$$

    **4g · Step 7 · Sanity check.** Both areas are between 0 and 1 ✓. The total error of the test is $0.4\cdot\frac23+0.6\cdot\frac19=0.267+0.067=0.33$, better than the best lazy rule (always decide $\mathcal H_1$: error $P_0=0.4$) ✓.

    !!! answer "Answer"
        $\gamma''=\ln3\approx1.10$ (decide $\mathcal H_1$ for $y<\ln 3$); $P_{FA}=\frac23$, $P_M=\frac19$.

!!! idea "The integrals themselves: three rules, no thinking"
    **1 · Antiderivative.** $\displaystyle\int k\,e^{-ay}\,dy=-\frac{k}{a}\,e^{-ay}$. The minus comes from the exponent, and you divide by the $a$ in front of the $y$. So $\int e^{-y}dy=-e^{-y}$, and $\int 2e^{-2y}dy=-e^{-2y}$ — the $2$ in front **cancels** the $2$ of the exponent (that is why the exam always uses $2e^{-2y}$: a clean, normalised density).

    **2 · Evaluate.** $\big[F\big]_a^b=F(b)-F(a)$: **top minus bottom**. With the minus sign already in $F$ this flips: $\big[-e^{-y}\big]_0^{\ln3}=-(e^{-\ln3}-e^{0})=1-e^{-\ln3}$. And $e^{-\infty}=0$: for a bound at $\infty$ the top contributes nothing and you get "minus the bottom".

    **3 · Logs in the exponent.** $e^{-a\ln b}=\dfrac{1}{b^{a}}$, always: $e^{-\ln3}=\frac13$, $e^{-2\ln3}=\frac1{3^2}=\frac19$. A minus in front of a log = "one over that power".

    **Check:** the integrand is (part of) a density, so every area lands between 0 and 1, and $\int_0^\infty e^{-y}dy=\int_0^\infty 2e^{-2y}dy=1$. Something bigger than 1 means a flipped sign.

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
