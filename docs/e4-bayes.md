# 4.2 Priors, costs and the theory questions

<div class="meta"><span class="hot">Theory MC in 6 of 6 recent exams</span><span>Bayes test in 3 of the last 3</span><span>0.5–1.5 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep1_detection.mp4" poster="video/pod_ep1_detection.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 1, Detection: the likelihood ratio test</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [4.1 Likelihood ratio test](e4-lrt.md) first.

## The idea in one minute

If devices are present only 10 % of the time, a measurement has to be **more convincing** before you say "device". Bayes does exactly that: it multiplies each curve by its prior and decides $\mathcal H_1$ wherever the weighted $\mathcal H_1$ curve is the taller one. Drag the crossing in the picture (or slide the prior) and watch the threshold move.

<div class="widget" data-w="lrt" data-priors="1"></div>

The same thing as a formula: it is still the LRT of 4.1, only the number on the right is now fixed by priors and costs.

<div class="key" markdown>

$$
\frac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda=\frac{(C_{10}-C_{00})\,P_0}{(C_{01}-C_{11})\,P_1}
$$

</div>

$C_{ij}$ = cost of **deciding $\mathcal H_i$ when $\mathcal H_j$ is true**. So $C_{10}$ = cost of a false alarm, $C_{01}$ = cost of a miss, $C_{00}=C_{11}=0$ almost always (being right costs nothing). Four layers, each from something different:

| layer | symbol | made of | note |
|---|---|---|---|
| 1 | $p(x\mid\mathcal H_1)$, $p(x\mid\mathcal H_0)$ | the **model** | the two curve heights |
| 2 | $L(x)=\dfrac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}$ | layer 1 only | priors and costs are **not** in here |
| 3 | $\lambda$ (the exam writes $\eta$) | priors + costs | the **bar** |
| 4 | $\gamma$ | layers 2 + 3 | the cut on $x$: solve $L(x)>\lambda$ for $x$ |

(Trap: the $\lambda(\theta)=\frac{1}{1+e^{-\theta}}$ of [2.1](e2-mle.md) is a **different lambda** — a model parameter there, not a detection threshold.)

## How to fight this section with the sheet

The exam adds **priors** $P(H_0),P(H_1)$, **costs** $C_{ij}$, "posterior", "Bayesian hypothesis test" to the two PDFs → you open **box 4B** on your A4 sheet: one formula for $\eta$, one for the posterior version, one for "where $p_1P_1=p_0P_0$", each with an exam already done. The theory MC is **box 4C**.

!!! sheet "Box 4B, exactly as it is printed on the sheet"
    IF YOU SEE priors $P(H_0),P(H_1)$, costs $C_{ij}$, "posterior", "Bayesian hypothesis test", "$P_M$" / "miss"

    $C_{ij}$ = cost of deciding $i$ when $j$ is true. $C_{10}$ = false alarm cost, $C_{01}$ = miss cost.

    - Threshold $\eta=\dfrac{P(H_0)\,(C_{10}-C_{00})}{P(H_1)\,(C_{01}-C_{11})}$. Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$. Then do 4A with this $\eta$.<br>
      *Jun26-4c:* $\eta=\frac{0.9}{0.1}=9$ → put $\eta=9$ in the Rayleigh answer of 4A.
    - **Posteriors given** → accept $H_1$ if $\dfrac{P(H_1\mid x)}{P(H_0\mid x)}\gt\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$.<br>
      *Apr25-4c:* $C_{01}=100\,C_{10}$ → right side $=0.01$. Posterior ratio $=5\gt0.01$ → accept $H_1$ → the student fails: **yes**.
    - **"Where $p_1P_1=p_0P_0$"** → write the equality and solve.<br>
      *Nov22:* $0.6\cdot2e^{-2y}=0.4\,e^{-y}$ → $e^{-y}=\frac13$ → $y=\ln3$; decide $H_1$ for $y\lt\ln3$. $P_{FA}=1-e^{-\ln3}=\frac23$, $P_M=e^{-2\ln3}=\frac19$.

Special cases of the $\eta$ formula (from its own line: *"Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$"*):

| Special case | $\lambda$ | what it does |
|---|---|---|
| right costs 0, wrong costs 1 ("0/1 costs") | $\dfrac{P_0}{P_1}$ | minimises the total probability of error $P_e$ |
| 0/1 costs **and** equal priors | $1$ | maximum likelihood rule: pick the taller curve |
| misses 100× worse than false alarms | $\dfrac{P_0}{100P_1}$ | much easier to say $\mathcal H_1$ |

## 1 · June 2026 · 4c — priors onto the Rayleigh test

!!! exam "Resit Q4, June 2026 · 4c · 1 p (after 4b built the Rayleigh LRT)"
    Now assume prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$, reflecting the fact that a transmitting device is present only 10 % of the time. Assume equal costs for false alarms and miss-detections. When should the sensor accept $H_1$?

!!! sheet "In the cheat sheet: box 4B, bullet 1 — the *Jun26-4c* line is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · the formula.**
    *"$\eta=\dfrac{P(H_0)\,(C_{10}-C_{00})}{P(H_1)\,(C_{01}-C_{11})}$. Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$."* Equal costs given → the short form.

    ***

    **Sheet step 2 · the number.**
    *"$\eta=\frac{0.9}{0.1}=9$"* — printed. The measurement must be 9× more likely under $H_1$ before the sensor says $H_1$ (rare device → high bar).

    ***

    **Sheet step 3 · what to do with it.**
    *"Then do 4A with this $\eta$."* And the example line: *"put $\eta=9$ in the Rayleigh answer of 4A"* — the 4A formula gives the cut:

    $$x>\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(9\,\frac{\sigma_1^2}{\sigma_0^2}\Big)}.$$

    ***

    **Sheet check · the example line.**
    $\eta=9$ is printed as the answer to this exact sub-question. (Numbers, $\sigma_0=1,\sigma_1=2$: the threshold moves from $1.92$ at $\eta=1$ to $3.09$ at $\eta=9$ — the prior only moves the line, never the curves.)

    </div>

!!! answer "Answer"
    $\eta=\frac{0.9}{0.1}=9$; accept $H_1$ when $x>\gamma=\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(9\,\dfrac{\sigma_1^2}{\sigma_0^2}\Big)}$.

## 2 · April 2025 · 4c — posteriors and costs (the student fails)

!!! exam "Final exam Q3, 13 April 2025 · 4c · 1 p"
    An AI agent detects whether assignments were generated with genAI. $\mathcal{H}_0$: written by a student; $\mathcal{H}_1$: generated by genAI. The student fails if the agent accepts $\mathcal{H}_1$. Assume $C_{0,1} = 100C_{1,0}$, $C_{1,1} = C_{0,0} = 0$, and that the posterior of $\mathcal{H}_0$ is 5 times smaller than the posterior of $\mathcal{H}_1$. Should the student fail the course?

!!! sheet "In the cheat sheet: box 4B, bullet 2 — the *Apr25-4c* line is this exam, decided"
    <div class="stepper" markdown>

    **Sheet step 1 · which bullet?**
    *"**Posteriors given** → accept $H_1$ if $\dfrac{P(H_1\mid x)}{P(H_0\mid x)}\gt\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$."* The exam hands us posteriors → this bullet, not the $\eta$ one.

    ***

    **Sheet step 2 · the right side.**
    *"$C_{01}=100\,C_{10}$ → right side $=0.01$."* $\frac{C_{10}-0}{C_{01}-0}=\frac{C_{10}}{100C_{10}}=0.01$.

    ***

    **Sheet step 3 · the left side and the verdict.**
    "Posterior of $H_0$ is 5 times smaller" → ratio $=\frac{P(H_1|x)}{P(H_0|x)}=5$. The sheet: *"Posterior ratio $=5\gt0.01$ → accept $H_1$ → the student fails: **yes**."*

    ***

    **Sheet check · the example line.**
    The line ends with the answer word: **yes**.

    </div>

!!! answer "Answer"
    **Yes** — the ratio 5 beats the bar 0.01, so accept $\mathcal H_1$ and the student fails.

## 3 · November 2022 · 4f, 4g — "where $p_1P_1=p_0P_0$"

!!! exam "Final exam, 7 November 2022 · 4f, 4g · 0.5 p each"
    $p(y;\mathcal H_0)=e^{-y}$, $p(y;\mathcal H_1)=2e^{-2y}$ for $y\ge0$. Priors $P_0 = 0.4$ and $P_1 = 0.6$; costs $C_{1,1} = C_{0,0} = 0$, $C_{0,1} = C_{1,0} = 1$, so we decide $\mathcal H_1$ when $p(y|\mathcal{H}_1)P_1 > p(y|\mathcal{H}_0)P_0$.

    **4f** Find the threshold $\gamma''$, i.e. the value of $y$ for which $p(y|\mathcal{H}_1)P_1 = p(y|\mathcal{H}_0)P_0$.

    **4g** Determine $P_M$ and $P_{FA}$ for this test.

!!! sheet "In the cheat sheet: box 4B, bullet 3 — the *Nov22* line is both sub-questions"
    <div class="stepper" markdown>

    **Sheet step 1 · the bullet.**
    *""Where $p_1P_1=p_0P_0$" → write the equality and solve."* $0.6\cdot2e^{-2y}=0.4\,e^{-y}$.

    ***

    **Sheet step 2 · solve (the printed chain).**
    *"$0.6\cdot2e^{-2y}=0.4\,e^{-y}$ → $e^{-y}=\frac13$ → $y=\ln3$"* → $\gamma''=\ln3\approx1.10$. (Divide both sides by $0.4e^{-2y}$: $3=e^{y}$.)

    ***

    **Sheet step 3 · the rule's direction.**
    *"decide $H_1$ for $y\lt\ln3$"* — small $y$ points to $H_1$ because $2e^{-2y}$ is the curve tall near 0 (the ratio $3e^{-y}$ shrinks with $y$).

    ***

    **Sheet step 4 · the two areas (the printed end of the line).**
    $P_{FA}=1-e^{-\ln3}=\frac23$ (decide $H_1$ while $H_0$ true → the $e^{-y}$ area left of $\ln3$), $P_M=e^{-2\ln3}=\frac19$ (the $2e^{-2y}$ area right of $\ln3$).

    ***

    **Sheet check · the example line.**
    One printed line contains $\gamma''$, the direction and both probabilities.

    </div>

!!! answer "Answer"
    $\gamma''=\ln3\approx1.10$ (decide $\mathcal H_1$ for $y<\ln 3$); $P_{FA}=\frac23$, $P_M=\frac19$.

## The integrals: the Calculations strip

The areas above are integrals of $e^{-ay}$ — the **Calculations** strip at the bottom of the sheet prints what you need: $\int e^{cx}dx=\frac1ce^{cx}$, evaluate $[F]_a^b=F(b)-F(a)$, *"$e^{-\infty}=0$"*, $\int_0^\infty e^{-cx}dx=\frac1c$, $\int_0^\infty xe^{-cx}dx=\frac1{c^2}$, $\int_0^\infty x^2e^{-cx}dx=\frac2{c^3}$, plus the number cards ($\ln3=1.099$, $e^{-2}=0.135$…). Three rules make them mechanical:

1. **Antiderivative.** $\int k\,e^{-ay}\,dy=-\frac{k}{a}\,e^{-ay}$ — the $2$ in front of $2e^{-2y}$ **cancels** the $2$ of the exponent.
2. **Evaluate, top minus bottom.** With the minus already in $F$: $\big[-e^{-y}\big]_0^{\ln3}=1-e^{-\ln3}$. At $\infty$ the top is 0 (the strip: $e^{-\infty}=0$).
3. **Logs in the exponent.** $e^{-a\ln b}=\frac1{b^a}$: $e^{-\ln3}=\frac13$, $e^{-2\ln3}=\frac19$.

Check: every area lands between 0 and 1; something bigger than 1 means a flipped sign.

## The theory questions — box 4C

!!! sheet "Box 4C, exactly as it is printed on the sheet (Part 4 true / false)"
    IF YOU SEE "which of the following statements" (in Part 4) about hypothesis testing, $P_{FA}$, errors

    | Statement | T / F |
    |---|---|
    | Bayes detection **minimises** the Bayes risk (average cost) | T ("maximises": F) |
    | $C_{01}=C_{10}$ (1, 10, any equal value), $C_{00}=C_{11}=0$ → minimises total error probability | T |
    | Equal priors + equal costs → maximum-likelihood rule | T |
    | Higher $P(H_0)$ raises $\eta$ → harder to pick $H_1$ | T |
    | Higher $P(H_1)$ raises $\eta$ | F (it lowers it) — Jun26 c |
    | Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$ | T ("minimise": F) |
    | ROC = $P_D$ against $P_{FA}$; diagonal = guessing; better → top-left | T |

    Error table (rows = decision, columns = truth): decide $H_0$ & true $H_0$ = true negative · decide $H_0$ & true $H_1$ = miss, false negative, type II · decide $H_1$ & true $H_0$ = false alarm, false positive, type I · decide $H_1$ & true $H_1$ = detection, true positive (Nov22 a).

    Trap (Apr25-4b): "which statement is FALSE" where all three look true → as printed **all three are true** (official: no false one). Check the verbs: risk **min** · $P_D$ **max** · $P_e$ **min**.

<div class="stepper" markdown>

**Sheet step 1 · Bayes risk (row 1).**
*"Bayes detection **minimises** the Bayes risk (average cost) | T ("maximises": F)"*. The verb is the question.

***

**Sheet step 2 · the 0/1-costs row (row 2).**
$C_{01}=C_{10}$ (any equal value) and $C_{00}=C_{11}=0$ → minimises total error probability | T. Scaling all costs by 10 does not move the threshold.

***

**Sheet step 3 · equal priors (row 3).**
*"Equal priors + equal costs → maximum-likelihood rule | T"* — $\eta=1$, just pick the taller curve.

***

**Sheet step 4 · the prior rows (rows 4–5, one is Jun26's FALSE).**
Higher $P(H_0)$ raises $\eta$ → T. *"Higher $P(H_1)$ raises $\eta$ | F (it lowers it) — Jun26 c"*.

***

**Sheet step 5 · the error table (Nov22 4a).**
The box's error table names all four cells: miss = false negative = **type II**, false alarm = false positive = **type I**. "Positive" = "we said $H_1$".

***

**Sheet check · the trap line.**
Apr25-4b asks for the FALSE statement and all three are true — the box says so. Verbs: risk **min** · $P_D$ **max** · $P_e$ **min**.

</div>

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - Mixing up $C_{10}$ and $C_{01}$: the box defines them — $C_{10}$ = false alarm, $C_{01}$ = miss. The subscripts are "decided, truth".
    - Putting priors into $L(x)$: the ratio is only the two PDFs (layer 2). Priors and costs belong in $\eta$ (layer 3) — the box's formula has them on the right side only.
    - Using the $\eta$ bullet when **posteriors** are given (Apr25-4c): posteriors already contain the priors → the ratio of posteriors against $\frac{C_{10}-C_{00}}{C_{01}-C_{11}}$.
    - The direction flip again: the *Nov22* line decides $H_1$ for $y<\ln3$, not $>$. Small $y$ = the narrow curve.
    - Forgetting that "equal costs" means the short form $\eta=\frac{P(H_0)}{P(H_1)}$ (bullet 1) — no $C$'s left to plug in.
    - In the MC: "maximise the Bayes risk", "minimise $P_D$", "raising $P(H_1)$ raises $\eta$" — all three are the sheet's F rows.
