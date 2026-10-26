# 4.1 Likelihood ratio test

<div class="meta"><span class="hot">In 9 of 9 exams</span><span>1–1.5 points</span><span>35 min</span></div>

<figure class="pod"><video src="video/pod_ep1_detection.mp4" poster="video/pod_ep1_detection.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 1, Detection: the likelihood ratio test</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

You get **two possible stories** for a measurement $x$, each with its own PDF (the curve that says which values of $x$ are likely): $\mathcal H_0$ "nothing is there" and $\mathcal H_1$ "something is there". You measured one $x$. Ask each story: *"how likely was this $x$ under you?"* — the height of its PDF at $x$. If the $\mathcal H_1$ curve is much higher at your $x$, say $\mathcal H_1$.

So the test is a **ratio of heights** compared with a number $\lambda$ — the **bar** ("how convinced do I need to be"). The exam gives this bar different clothes: $\eta$ (June 2026), $\gamma$ (Nov 2022), or just hands it to you ($\lambda=0.2$):

$$
L(x)=\frac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda
\qquad\text{(bigger than }\lambda\text{ → say }\mathcal H_1\text{, smaller → say }\mathcal H_0).
$$

<div class="key" markdown>

**Who is who** (the letters the exam mixes up):

| symbol | lives on | what it is |
|---|---|---|
| $p(x\mid\mathcal H_1),\ p(x\mid\mathcal H_0)$ | the two curves | the PDF heights |
| $L(x)$ | — | the **ratio** of the two heights (only the PDFs) |
| $\lambda$ (= exam's $\eta$) | the ratio | the **bar** the ratio must beat |
| $\gamma$ | the $x$ axis | the **cut** you get when you solve $L(x)>\lambda$ for $x$ |

Rule of thumb: **the number they give you is the bar; the number they ask you to find is the cut.** $\lambda$ is **always just a number**, even with 1000 samples; $L$ is always a function; $\gamma$ is a number only when the $N$-dimensional region collapses to one axis (Nov 2022 4c: "show that the test takes the form $\sum_n|x_n|\gtrless\gamma'$").

</div>

After a bit of algebra this always becomes a cut on the $x$ axis. Two mistakes are possible, and the threshold trades one for the other:

| | what happened | name | area under... |
|---|---|---|---|
| $P_{FA}$ | $\mathcal H_0$ true, you said $\mathcal H_1$ | false alarm | the $\mathcal H_0$ curve, in the "decide $\mathcal H_1$" zone |
| $P_M$ | $\mathcal H_1$ true, you said $\mathcal H_0$ | miss | the $\mathcal H_1$ curve, in the "decide $\mathcal H_0$" zone |
| $P_D=1-P_M$ | $\mathcal H_1$ true, you said $\mathcal H_1$ | detection | the $\mathcal H_1$ curve, in the "decide $\mathcal H_1$" zone |

Drag the threshold. Watch the blue area ($P_{FA}$) and the red area ($P_M$): you can never shrink both at once.

<div class="widget" data-w="lrt"></div>

Now switch to the **Nov 2022** tab. There the $\mathcal H_1$ curve is the one that is tall near 0, so small values point to $\mathcal H_1$: the rule becomes "$y<\gamma$" and the false alarm area sits on the **left**. This is the trap the exam loves.

## How to fight this section with the sheet

The exam gives **two PDFs** and says **"likelihood ratio test"**, **"binary hypothesis"**, **"when accept $H_1$"**, threshold $\lambda/\gamma/\eta$, **"$P_{FA}$"/"$P_D$"** → you open **box 4A** on your A4 sheet. Four numbered steps, then one worked line per exam that has ever appeared, then a **Probabilities** block for the areas. The multiple choice at the end of the question is **box 4C**.

!!! sheet "Box 4A, exactly as it is printed on the sheet"
    IF YOU SEE two pdfs (one for $H_0$, one for $H_1$) + "binary hypothesis"/"hypothesis testing", "likelihood ratio test", "when accept $H_1$", threshold $\lambda,\gamma,\eta$, "$P_{FA}$"/"$P_D$"

    1. $L(x)=\dfrac{p(x\mid H_1)}{p(x\mid H_0)}$. Cancel what appears on top and bottom. $N$ samples → multiply them ($e^ae^b=e^{a+b}$).
    2. Decide $H_1$ if $L\gt$ threshold. Take $\ln$ of both sides.
    3. Get $x$ alone. Multiplying or dividing by a negative number flips $\gt$ into $\lt$.
    4. Check the side: put a small and a large $x$ into $L$. Where $L$ comes out bigger than the threshold, that side is "decide $H_1$".

    *Apr25* $\frac{6x^{11}}{3x^5}=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=0.68$.

    *Jun26 Rayleigh* $\frac x{\sigma^2}e^{-x^2/2\sigma^2}$ ($\sigma_1\gt\sigma_0$): the $x$ in front cancels, so $L=\frac{\sigma_0^2}{\sigma_1^2}\,e^{\frac{x^2}2\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)}\gt\eta$ → accept $H_1$ if

    $$x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\frac{\sigma_1^2}{\sigma_0^2}\Big)}$$

    Bigger gap between $\sigma_0$ and $\sigma_1$ → the pdfs overlap less → more $P_D$ for the same $P_{FA}$ (better ROC).

    *Apr24* $\frac1{\sqrt{2\pi}}e^{-y^2/2}$ vs $\frac14e^{-y/2}$, $\gamma=1$: $L=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}\gt1$; take $\ln$: $-0.467+\frac{y^2}2-\frac y2\gt0$ → $y^2-y-0.934\gt0$ → root $y=\frac{1+\sqrt{1+3.74}}2=1.59$ → accept $H_1$ if $y\gt1.59$. $P_{FA}=Q(1.59)=0.056$, $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac12e^{-0.795}=0.23$.

    *Nov22* $\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$.

    **Probabilities.** $P_{FA}$ = area under the $H_0$ pdf where you decide $H_1$. $P_D$ = area under the $H_1$ pdf in the same place.<br>
    Tails: Gaussian $N(0,1)$: $P(x\gt t)=Q(t)$ (table) · exponential $ce^{-cx}$: $P(x\gt t)=e^{-ct}$ · Rayleigh: $P(x\gt t)=e^{-t^2/2\sigma^2}$ · two tails $\lvert x\rvert\gt t$ → double.<br>
    "Threshold for $P_{FA}=0.1$": set the $H_0$ area $=0.1$, solve for $t$.

    *Nov22:* $1-e^{-t}=0.1$ → $t=-\ln0.9$; then $P_D=1-e^{-2t}=0.19$.

    "Plot / indicate $P_{FA}$ and $P_M$": draw both pdfs and a vertical line at the threshold. Shade the $H_0$ curve on the "decide $H_1$" side → $P_{FA}$. Shade the $H_1$ curve on the "decide $H_0$" side → $P_M$. (Nov22: $H_1$ when $y\lt1$, so $P_{FA}$ = $H_0$ area left of 1, $P_M$ = $H_1$ area right of 1.)

    **Gaussian with any $\sigma$.** $p(x)=\dfrac1{\sigma\sqrt{2\pi}}e^{-x^2/2\sigma^2}$ (mean 0). Two zero-mean Gaussians, $\sigma_1$ vs $\sigma_0$ (pe21-4b): $\ln L=N\ln\frac{\sigma_0}{\sigma_1}+\frac12\big(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\big)\sum_n x^2[n]$ → decide $H_1$ when $\sum_n x^2[n]$ is **big** = **energy detector** (bigger variance = more energy).<br>
    **erf table** (printed in the question — pe21-4a): the printed CDF $\frac12\big[1+\operatorname{erf}\frac{t-\mu}{\sigma\sqrt2}\big]$ is $P(x\lt t)$; the test needs $P(x\gt t)=1-\text{CDF}=\frac12\big[1-\operatorname{erf}\frac{z}{\sqrt2}\big]$, $z=\frac{t-\mu}{\sigma}$. The table lists $\operatorname{erf}(x/\sqrt2)$ at $x=-3..3$: read it at $x=z$, value at $-z$ = minus the value at $z$.<br>
    **Matched filter** (jan22-4a): correlate the data with the known signal $s[n]$ (FIR filter $h[n]=$ the **time-reversed** $s$) → biggest output SNR; "only for uncorrelated noise" is **false**.

The algebra you need mid-step ($\ln$ rules, $e$ rules, quadratics, $Q$ numbers) is in the **Calculations** strip at the bottom of the sheet.

## 1 · April 2025 · 4a — the sheet's first example

!!! exam "Final exam, 13 April 2025 · 4a · 0.5 p"
    You are conducting a likelihood ratio test using a single datapoint $x$, $0 < x < 1$ whereby $p(x) = k_1 \theta x^{k_2 \theta - 1}$. Two hypothesis can be distinguished

    $$\mathcal{H}_0 : \theta = 3, \qquad \mathcal{H}_1 : \theta = 6.$$

    If $\lambda = 0.2$, $k_1 = 1$, and $k_2 = 2$, what is the value for $x$ for which $\mathcal{H}_1$ should be accepted?

!!! sheet "In the cheat sheet: box 4A — the *Apr25* line is this exam, computed"
    <div class="stepper" markdown>

    **Sheet step 1 · build the two PDFs (the numbers are given).**
    $p(x)=\theta x^{2\theta-1}$ → $H_0$: $3x^5$, $H_1$: $6x^{11}$.

    ***

    **Sheet step 2 · step 1 of the box: the ratio, cancel.**
    *"$L(x)=\frac{p(x\mid H_1)}{p(x\mid H_0)}$. Cancel what appears on top and bottom."* $\frac{6x^{11}}{3x^5}=2x^6$ — the sheet's line: *"$\frac{6x^{11}}{3x^5}=2x^6\gt0.2$"*.

    ***

    **Sheet step 3 · step 3: get $x$ alone.**
    $x^6>0.1$ → $x>0.1^{1/6}=0.68$ (a root is increasing → no flip). The sheet's line ends *"$x\gt0.1^{1/6}=0.68$"*.

    ***

    **Sheet step 4 · step 4: check the side.**
    *"put a small and a large $x$ into $L$"*: at $x=0.9$, $L=2(0.9)^6\approx1.06>0.2$ ✓ decide $H_1$; at $x=0.1$, $L\approx0$ → decide $H_0$. So big $x$ = $H_1$, and the problem's own range $0<x<1$ caps it.

    ***

    **Sheet check · the example line.**
    The whole line is printed: $2x^6>0.2$ → $x^6>0.1$ → $x>0.68$.

    </div>

!!! answer "Answer"
    Accept $\mathcal H_1$ for $x>0.1^{1/6}\approx0.68$ (i.e. $0.68<x<1$).

## 2 · November 2022 · 4c–4e — $N$ samples, the flip, and the areas

!!! exam "Final exam, 7 November 2022 · 4c (0.5 p), 4d (0.25 p), 4e (0.5 p)"
    Under the two hypotheses, a single observation $x$ admits a zero mean Laplacian distribution, but with different variances:

    $$\mathcal{H}_0 : p(x; \mathcal{H}_0) = \frac{1}{2}e^{-|x|}\qquad\text{and}\qquad \mathcal{H}_1 : p(x; \mathcal{H}_1) = e^{-2|x|}.$$

    Each observation $x_n$ of the vector $\mathbf{x}$ (length $N$) is independent and identically distributed.

    **4c** Show that the likelihood ratio test takes the form $\sum_{n=0}^{N-1} |x_n| \underset{\mathcal{H}_1}{\overset{\mathcal{H}_0}{\gtrless}} \gamma'$ and determine $\gamma'$.

    **4d** For $N = 1$, with $Y=|X|$: $p(y; \mathcal{H}_0) = e^{-y}$, $p(y; \mathcal{H}_1) = 2e^{-2y}$. Indicate $P_{FA}$ and $P_M$ for $\gamma' = 1$ in the plot.
    ![pdfs of y](img/exam/nov22-4d.jpg)

    **4e** For a $P_{FA} = 0.1$ calculate the threshold $\gamma'$, and the probability of detection $P_D$ for it.

!!! sheet "In the cheat sheet: box 4A — the *Nov22* lines answer 4c, 4d and 4e"
    <div class="stepper" markdown>

    **Sheet step 1 · 4c = the box's *Nov22* line.**
    *"$\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$."* That is the requested form with $\gamma'=N\ln2-\ln\lambda$. (One sample: $\frac{e^{-2|x|}}{\frac12 e^{-|x|}}=2e^{-|x|}$; $N$ independent samples → step 1's *"N samples → multiply them"* → $2^Ne^{-\sum|x_n|}$; take $\ln$ (step 2), then step 3 flips the inequality when you multiply by $-1$: $\sum|x_n|<N\ln2-\ln\lambda$.)

    ***

    **Sheet step 2 · 4d = the box's "Plot / indicate" line.**
    *"draw both pdfs and a vertical line at the threshold. Shade the $H_0$ curve on the 'decide $H_1$" side → $P_{FA}$. Shade the $H_1$ curve on the 'decide $H_0$" side → $P_M$. (Nov22: $H_1$ when $y\lt1$, so $P_{FA}$ = $H_0$ area **left** of 1, $P_M$ = $H_1$ area **right** of 1.)"* The sheet even names which side — the rule points **left** because $H_1$ is the narrow curve.

    ***

    **Sheet step 3 · 4e = the box's threshold line.**
    *"'Threshold for $P_{FA}=0.1$': set the $H_0$ area $=0.1$, solve for $t$."* With the exponential tail formula (*"exponential $ce^{-cx}$: $P(x>t)=e^{-ct}$"*, here $c=1$, and $P_{FA}$ is the **left** area $1-e^{-t}$): $1-e^{-t}=0.1$ → $t=-\ln0.9\approx0.105$.

    ***

    **Sheet step 4 · $P_D$ = the same line's tail.**
    *"then $P_D=1-e^{-2t}=0.19$"* — printed as is.

    ***

    **Sheet check · the example lines.**
    Three lines of the box = the three sub-questions, with the numbers already done.

    </div>

!!! answer "Answer"
    4c: $\sum_n|x_n|\ \underset{\mathcal H_1}{\overset{\mathcal H_0}{\gtrless}}\ \gamma'=N\ln2-\ln\lambda$ (small sum → $H_1$). 4d: $P_{FA}$ = $e^{-y}$ area left of 1, $P_M$ = $2e^{-2y}$ area right of 1. 4e: $\gamma'=-\ln0.9\approx0.105$, $P_D=1-e^{-2\gamma'}=0.19$.

## 3 · June 2026 · 4b — Rayleigh, straight from the box

!!! exam "Resit Q4, June 2026 · 4b · 1 p"
    A wireless sensor measures the received signal envelope $X$. Under $H_0$ (no device present), $X \sim \text{Rayleigh}(\sigma_0)$. Under $H_1$ (device present), $X \sim \text{Rayleigh}(\sigma_1)$, with $\sigma_1 > \sigma_0 > 0$, both known. The Rayleigh pdf is $p(x \mid \sigma) = \frac{x}{\sigma^2} \exp\left(-\frac{x^2}{2\sigma^2}\right)$, $x \geq 0$.

    - Construct the likelihood-ratio test for a threshold $\eta$.
    - Discuss how the separation between $\sigma_0$ and $\sigma_1$ affects detection performance.

!!! sheet "In the cheat sheet: box 4A — the *Jun26 Rayleigh* block is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · copy the cancelled ratio.**
    *"$\frac x{\sigma^2}e^{-x^2/2\sigma^2}$ ($\sigma_1\gt\sigma_0$): the $x$ in front cancels, so $L=\frac{\sigma_0^2}{\sigma_1^2}\,e^{\frac{x^2}2\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)}\gt\eta$."* The $x$-in-front cancellation is box step 1 (*"Cancel what appears on top and bottom"*).

    ***

    **Sheet step 2 · solve for $x$ = the printed formula.**
    *"accept $H_1$ if $x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\frac{\sigma_1^2}{\sigma_0^2}\Big)}$."* Take $\ln$ (step 2), isolate $x$ (step 3 — no flip because $\sigma_1>\sigma_0$ makes the bracket positive), done.

    ***

    **Sheet step 3 · the discussion = the next printed sentence.**
    *"Bigger gap between $\sigma_0$ and $\sigma_1$ → the pdfs overlap less → more $P_D$ for the same $P_{FA}$ (better ROC)."* That is the whole second bullet.

    ***

    **Sheet check · the example line.**
    The block is tagged with this exam's name. If the formula is on your sheet, the 1 p is a copy job.

    </div>

!!! answer "Answer"
    Decide $H_1$ if $x>\gamma=\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\dfrac{\sigma_1^2}{\sigma_0^2}\Big)}$. Further apart $\sigma_0,\sigma_1$ → less overlap → higher $P_D$ at the same $P_{FA}$ (better ROC); $\sigma_1\to\sigma_0$ → no better than guessing.

## 4 · April 2024 · 4b — Gaussian vs exponential, $\gamma=1$

!!! exam "Final exam, April 2024 · 4b · 1.5 p"

    $$\mathcal{H}_0: p(y) = \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}}\qquad \mathcal{H}_1: p(y) = \frac{1}{4} e^{-\frac{y}{2}},\qquad y > 0.$$

    Sketch the likelihoods. For a threshold $\gamma = 1$, indicate $P_{FA}$ and $P_M$, and calculate $P_D$ and $P_{FA}$. Use $Q(x) = \int_x^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} du$. No need for exact numerical values.

!!! sheet "In the cheat sheet: box 4A — the *Apr24* line is this exam, computed end to end"
    <div class="stepper" markdown>

    **Sheet step 1 · the bar is on the ratio.**
    $\gamma=1$ means $L>1$: *"decide the story whose curve is higher"*. (Trap: it is **not** a value of $y$.)

    ***

    **Sheet step 2 · the printed computation.**
    *"$L=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}\gt1$; take $\ln$: $-0.467+\frac{y^2}2-\frac y2\gt0$ → $y^2-y-0.934\gt0$ → root $y=\frac{1+\sqrt{1+3.74}}2=1.59$ → accept $H_1$ if $y\gt1.59$."* Steps 2–3 of the box: $\ln$ both sides, get $y$ alone (quadratic formula from the **Calculations** strip).

    ***

    **Sheet step 3 · the areas = the Probabilities block.**
    *"$P_{FA}=Q(1.59)=0.056$"* (Gaussian tail: *"Gaussian $N(0,1)$: $P(x\gt t)=Q(t)$"*), *"$P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac12e^{-0.795}=0.23$"* (exponential tail $e^{-ct}$ with $c=\frac12$).

    ***

    **Sheet step 4 · the shading.**
    The "Plot / indicate" line: decide $H_1$ for $y>1.59$ → shade the $H_0$ curve to the **right** of 1.59 ($P_{FA}$), the $H_1$ curve to the **left** ($P_M$).

    ***

    **Sheet check · the example line.**
    *"$P_{FA}=Q(1.59)=0.056$, $P_D=\frac12e^{-0.795}=0.23$."* The exam says "no exact numbers needed" — the sheet's $Q(1.59)$ form is already the answer.

    </div>

!!! answer "Answer"
    Decide $\mathcal H_1$ for $y>1.59$. $P_{FA}=Q(1.59)\approx0.056$, $P_D=\frac12 e^{-0.795}\approx0.23$, $P_M\approx0.27$ (as printed; the densities are not normalised on $y>0$, so $P_D+P_M=\frac12$).

## 5 · The theory questions — box 4C

The MC is not about calculating: the same dozen sentences come back with one word swapped. Who puts the number $\lambda$ in place? **Neyman–Pearson**: fix the false alarms you can tolerate, **maximise $P_D$**. **Bayes** ([4.2](e4-bayes.md)): price each mistake + prior, minimise the average cost. Either way you compare the ratio with a number.

!!! sheet "Box 4C, exactly as it is printed on the sheet"
    IF YOU SEE "which of the following statements" (in Part 4) about hypothesis testing, $P_{FA}$, errors

    Same swap test as 2D — the verb is the question: risk **min** · $P_D$ **max** · $P_e$ **min**; $\eta$ goes **up** with $P(H_0)$, **down** with $P(H_1)$.

    | The fact (true) | The lie they print (false) |
    |---|---|
    | Bayes detection **minimises** the Bayes risk | "maximises" |
    | $C_{01}=C_{10}$, $C_{00}=C_{11}=0$ → minimises total error $P_e$ | (scaling all costs leaves $\eta$) |
    | Equal priors + equal costs → maximum-likelihood rule | — |
    | Higher $P(H_0)$ raises $\eta$ → harder to pick $H_1$ | "higher $P(H_1)$ raises $\eta$" (lowers — Jun26 c) |
    | Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$ | "minimise $P_D$" · "fix $P_D$, max $P_{FA}$" |
    | NP's solution is the LRT; the LRT itself needs **no** priors | "the LRT needs $P_0,P_1$" |
    | $\ln$ of the ratio never changes the decisions | "changes the decisions" |
    | Errors are unavoidable: the pdfs overlap | "a threshold kills both errors" |
    | ROC: $P_D$ up, $P_{FA}$ right; diagonal = guessing; better = top-left | "below diagonal = wrong $\sigma$" (flipped) |
    | miss = false negative = type II · false alarm = false positive = type I (Nov22 a) | labels swapped |

    Matched filter & energy-detector sentences → the last blocks of 4A (time-reversed $s$, "only for uncorrelated noise" **false**, $\sum x^2$ **big**, narrow $H_1$ → sum **small**).

    Trap (Apr25-4b): "which statement is FALSE" where all three look true → as printed **all three are true** (official: no false one). Check the verbs: risk **min** · $P_D$ **max** · $P_e$ **min**.

<div class="stepper" markdown>

**Sheet step 1 · the error-table question (Nov 2022 4a).**
The last table row names the cells: *"miss = false negative = type II · false alarm = false positive = type I"*. *"Positive" means "we said $H_1$"*. Match the shuffled cells to the row.

***

**Sheet step 2 · the NP sentence (Nov 2022 4b, Apr 2024 4a): read the verb.**
Fact: *"Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$"*. "Minimise $P_D$" is the printed lie. A rephrasing ("among all tests with $P_{FA}=\alpha$, the one with the highest detection rate…") changes nothing: same idea, same answer.

***

**Sheet step 3 · the priors sentence (Jun 2026 4c): the lie is printed with the exam tag.**
*"Higher $P(H_0)$ raises $\eta$ → harder to pick $H_1$"* is the fact; *"higher $P(H_1)$ raises $\eta$"* is the lie (it **lowers** it).

***

**Sheet step 4 · the ROC sentence and its lie.**
Fact: *"$P_D$ up, $P_{FA}$ right; diagonal = guessing; better = top-left"*. The false twin blames a wrong $\sigma$ for a curve below the diagonal — a wrong $\sigma$ only flattens it; below means **flipped** decisions.

***

**Sheet step 5 · the matched filter (jan22-4a) and the energy detector (pe21-4b).**
These live in 4A's last blocks, not in the table: *"correlate the data with the known signal $s[n]$ (FIR filter $h[n]=$ the **time-reversed** $s$) → biggest output SNR; "only for uncorrelated noise" is **false**"*, and *"decide $H_1$ when $\sum_n x^2[n]$ is **big** = **energy detector**"*.

***

**Sheet check · the trap line.**
Apr25-4b asks "which statement is FALSE" and, as printed, all three are true — the box says so explicitly. Check the three verbs before choosing: risk **min**, $P_D$ **max**, $P_e$ **min**.

</div>

Fresh wording, never printed in any exam — run the swap test:

<div class="stepper" markdown>

**1 · "The Neyman–Pearson lemma provides, among all tests with a given false-alarm rate, the one with the smallest miss probability."**
"Smallest miss" = "biggest $P_D$", same idea, no swapped verb → **T**.

***

**2 · "Taking the logarithm of the likelihood ratio may change which observations are assigned to $H_1$."**
Swap: *may change* against the fact *"never changes the decisions"* → **F**.

***

**3 · "A detector whose ROC runs below the diagonal should be re-fitted with a better noise model."**
Swap: the fact says below-diagonal = **flipped** decisions; a wrong noise model only flattens the curve → **F**.

</div>

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - **Forgetting to flip** when you multiply or divide by a negative (box step 3). Then the whole rule points the wrong way — the Nov22 case decides $H_1$ for a **small** $\sum|x_n|$.
    - **Wrong curve for the area** (Probabilities block): $P_{FA}$ always uses $p(x\mid H_0)$, $P_D$ and $P_M$ always use $p(x\mid H_1)$.
    - **Shading the wrong side**: first decide where "decide $H_1$" is (box step 4: *"put a small and a large $x$ into $L$"*), then shade.
    - Confusing the bar and the cut: the number they give ($\lambda,\eta,\gamma$ on the ratio) is the bar; the number you solve for is the cut on $x$.
    - $N$ samples: the ratio is a **product**, its log a **sum**. Do not drop the $N$ in front of constants ($2^N\to N\ln2$).
    - Using the CDF instead of the tail for $P(x>t)$ (the erf-table block: the printed table is $P(x<t)$, so $P(x>t)=1-\text{CDF}$).
    - In the MC: swapping "maximise"/"minimise" (box 4C row 6) or calling $h[n]=s[n]$ the matched filter (box 4A: it is the **time-reversed** $s$).
