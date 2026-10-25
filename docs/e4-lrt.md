# 4.1 Likelihood ratio test

<div class="meta"><span class="hot">In 9 of 9 exams</span><span>1–1.5 points</span><span>35 min</span></div>

<figure class="pod"><video src="video/pod_ep1_detection.mp4" poster="video/pod_ep1_detection.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 1, Detection: the likelihood ratio test</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

You get **two possible stories** for a measurement $x$, each with its own PDF (probability density function: the curve that says which values of $x$ are likely):

- $\mathcal H_0$: "nothing is there" (no device, noise only, the student wrote it), with PDF $p(x\mid\mathcal H_0)$.
- $\mathcal H_1$: "something is there", with PDF $p(x\mid\mathcal H_1)$.

Then they ask some of: **(a)** build the likelihood ratio test and simplify it to a rule like "decide $\mathcal H_1$ if $x>\gamma$", **(b)** shade $P_{FA}$ and $P_M$ in a sketch, **(c)** compute $P_{FA}$ and $P_D$, or the threshold for a given $P_{FA}$.

## The idea in one minute

You measured one $x$. Ask each story: *"how likely was this $x$ under you?"* That is the height of its PDF at $x$. If the $\mathcal H_1$ curve is much higher than the $\mathcal H_0$ curve at your $x$, say $\mathcal H_1$.

So the test is a **ratio of heights** compared with a number $\lambda$ (also called $\eta$ or $\gamma$, it is just "how convinced do I need to be"):

$$
L(x)=\frac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda
\qquad\text{(read: bigger than }\lambda\text{ → say }\mathcal H_1\text{, smaller → say }\mathcal H_0).
$$

After a bit of algebra this always becomes a cut on the $x$ axis: a **threshold** $\gamma$. Two mistakes are possible, and the threshold trades one for the other:

| | what happened | name | area under... |
|---|---|---|---|
| $P_{FA}$ | $\mathcal H_0$ true, you said $\mathcal H_1$ | false alarm | the $\mathcal H_0$ curve, in the "decide $\mathcal H_1$" zone |
| $P_M$ | $\mathcal H_1$ true, you said $\mathcal H_0$ | miss | the $\mathcal H_1$ curve, in the "decide $\mathcal H_0$" zone |
| $P_D=1-P_M$ | $\mathcal H_1$ true, you said $\mathcal H_1$ | detection | the $\mathcal H_1$ curve, in the "decide $\mathcal H_1$" zone |

Who puts the number $\lambda$ there? Two classical answers. **Neyman–Pearson**: you cannot shrink both errors at once, so fix the false alarms you can tolerate ($P_{FA}=\alpha$, say 1 %) and **maximise $P_D$** — and the test that does it is exactly this ratio, with $\lambda$ chosen so that $P_{FA}=\alpha$ (that is what 4e below asks). **Bayes** ([4.2](e4-bayes.md)): give each mistake a price and each hypothesis a prior, and minimise the average cost. Either way you end up comparing the ratio with a number.

Drag the threshold. Watch the blue area ($P_{FA}$) and the red area ($P_M$): you can never shrink both at once.

<div class="widget" data-w="lrt"></div>

Now switch to the **Nov 2022** tab. There the $\mathcal H_1$ curve is the one that is tall near 0, so small values point to $\mathcal H_1$: the rule becomes "$y<\gamma$" and the false alarm area sits on the **left**. This is the trap the exam loves.

## The recipe

!!! recipe key "LRT in 5 steps"
    1. **Ratio.** Write $\dfrac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}>\lambda$. Cancel what you can. With $N$ independent samples, each PDF is a product over $n$, so the ratio is a product too.
    2. **Log both sides.** $\ln$ keeps the direction of $>$ (it is an increasing function). Use $\ln(ab)=\ln a+\ln b$, $\ln e^{u}=u$, $\ln x^k=k\ln x$.
    3. **Isolate $x$** (or $\sum x_n$, $\sum x_n^2$, ...). Every time you multiply or divide by a **negative** number, **flip** the inequality.
    4. **Write the rule**: "decide $\mathcal H_1$ if $x>\gamma$" (or $<$), with $\gamma$ written in terms of $\lambda$.
    5. **Errors.** $P_{FA}=\int p(x\mid\mathcal H_0)\,dx$ over the decide-$\mathcal H_1$ zone; $P_D=\int p(x\mid\mathcal H_1)\,dx$ over the same zone; $P_M=1-P_D$.

## Watch it once: April 2025 · 4a

!!! exam "Final exam, 13 April 2025 · 4a · 0.5 p"
    You are conducting a likelihood ratio test using a single datapoint $x$, $0 < x < 1$ whereby $p(x) = k_1 \theta x^{k_2 \theta - 1}$. Two hypothesis can be distinguished

    $$\mathcal{H}_0 : \theta = 3, \qquad \mathcal{H}_1 : \theta = 6.$$

    If $\lambda = 0.2$, $k_1 = 1$, and $k_2 = 2$, what is the value for $x$ for which $\mathcal{H}_1$ should be accepted?

<div class="stepper" markdown>

**Step 1 · Write both PDFs.** With $k_1=1$, $k_2=2$: $p(x)=\theta x^{2\theta-1}$.
Under $\mathcal H_0$ ($\theta=3$): $3x^{5}$. Under $\mathcal H_1$ ($\theta=6$): $6x^{11}$.

***

**Step 2 · Ratio > λ.**

$$\frac{6x^{11}}{3x^{5}}=2x^{6}>0.2$$

(dividing powers: $x^{11}/x^5=x^{11-5}=x^6$).

***

**Step 3 · Isolate $x$.** Divide by 2 (positive, no flip): $x^6>0.1$. Take the 6th root (increasing, no flip): $x>0.1^{1/6}$.
On the calculator: $0.1^{1/6}=e^{\ln(0.1)/6}=e^{-0.3838}\approx0.681$. No log was needed here because there was no exponential.

***

**Step 4 · The rule.** Accept $\mathcal H_1$ when $\mathbf{0.681\lt x\lt 1}$ (the upper limit 1 comes from the problem: $0\lt x\lt 1$).

</div>

## Watch it once more: November 2022 · 4c–4e (the flip)

!!! exam "Final exam, 7 November 2022 · 4c (0.5 p), 4d (0.25 p), 4e (0.5 p)"
    Under the two hypotheses, a single observation $x$ admits a zero mean Laplacian distribution, but with different variances:

    $$\mathcal{H}_0 : p(x; \mathcal{H}_0) = \frac{1}{2}e^{-|x|}\qquad\text{and}\qquad\mathcal{H}_1 : p(x; \mathcal{H}_1) = e^{-2|x|}.$$

    Each observation $x_n$ of the vector $\mathbf{x}$ (length $N$) is independent and identically distributed.

    **4c** Show that the likelihood ratio test takes the form $\sum_{n=0}^{N-1} |x_n| \underset{\mathcal{H}_1}{\overset{\mathcal{H}_0}{\gtrless}} \gamma'$ and determine $\gamma'$.

    **4d** For $N = 1$, with $Y=|X|$: $p(y; \mathcal{H}_0) = e^{-y}$, $p(y; \mathcal{H}_1) = 2e^{-2y}$. Indicate $P_{FA}$ and $P_M$ for $\gamma' = 1$ in the plot.
    ![pdfs of y](img/exam/nov22-4d.jpg)

    **4e** For a $P_{FA} = 0.1$ calculate the threshold $\gamma'$, and the probability of detection $P_D$ for it.

<div class="stepper" markdown>

**Step 1 · Ratio for ONE sample.** Same recipe as always: $\dfrac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}$. Here that is

$$\frac{e^{-2|x|}}{\tfrac12\,e^{-|x|}}.$$

Two small moves. (i) Dividing by $\tfrac12$ is the same as multiplying by 2, so the $\tfrac12$ becomes a $2$ in front. (ii) Two powers of $e$ divided: $\dfrac{e^{a}}{e^{b}}=e^{a-b}$ (subtract the exponents). With $a=-2|x|$ and $b=-|x|$:

$$2\,e^{-2|x|-(-|x|)}=2\,e^{-2|x|+|x|}=2\,e^{-|x|}\qquad(\text{because }-2|x|+|x|=-|x|).$$

***

**Step 2 · Ratio for $N$ samples.** The samples are independent, so the PDF of the whole vector is the **product** of the PDFs of each sample (that is what "independent" buys you, see [1.3](p4-lrt.md#13-many-samples-products-become-sums)). The same factor $2e^{-|x_n|}$ appears once per sample, $n=0,1,\dots,N-1$:

$$L(\mathbf x)=\prod_{n=0}^{N-1}2\,e^{-|x_n|}=\underbrace{2\cdot2\cdots2}_{N\text{ times}}\cdot e^{-|x_0|}\,e^{-|x_1|}\cdots e^{-|x_{N-1}|}=2^N\,e^{-\sum_n|x_n|}.$$

The last equality uses $e^{a}e^{b}=e^{a+b}$ (multiplying powers of $e$ adds the exponents), so all the $e^{-|x_n|}$ merge into one $e$ whose exponent is $-(|x_0|+\dots+|x_{N-1}|)=-\sum_n|x_n|$.
Tiny check, $N=3$, $\mathbf x=(0.5,\,-1,\,0.5)$: $\sum|x_n|=0.5+1+0.5=2$, so $L=2^3e^{-2}=8\cdot0.1353=1.083$.

The test is: decide $\mathcal H_1$ if $L(\mathbf x)>\gamma$ (the threshold called $\lambda$ above; the exam calls it $\gamma$, and it is a number we are free to choose). So:

$$2^N\,e^{-\sum_n|x_n|}>\gamma.$$

***

**Step 3 · Take $\ln$ to get rid of the $e$.** $\ln$ is increasing, so $>$ stays $>$. Use $\ln(ab)=\ln a+\ln b$, $\ln(2^N)=N\ln2$ and $\ln e^{u}=u$:

$$N\ln2-\sum_n|x_n|>\ln\gamma.$$

***

**Step 4 · Isolate the sum, and FLIP.** First subtract $N\ln2$ from both sides (no flip, it is only a subtraction):

$$-\sum_n|x_n|>\ln\gamma-N\ln2.$$

Now the sum has a minus sign in front and we want it alone, so multiply both sides by $-1$. A negative number: the inequality **flips** ($>$ becomes $<$), and the right side changes sign:

$$\sum_n|x_n|\lt N\ln2-\ln\gamma=:\gamma'.$$

Check the flip with numbers: $-3>-5$ is true; multiply by $-1$: $3<5$ (true), whereas $3>5$ would be false.

So we decide $\mathcal H_1$ when the sum is **small**. In the exam's notation, "decide $\mathcal H_1$ when the sum is below $\gamma'$" is written $\sum|x_n|\ \underset{\mathcal H_1}{\overset{\mathcal H_0}{\gtrless}}\ \gamma'$: the symbol under the sign ($\mathcal H_1$) is the one chosen when the left side is **smaller**, the one on top ($\mathcal H_0$) when it is **bigger**. That is exactly the form asked in 4c. It makes sense: $\mathcal H_1$ is the narrow curve $e^{-2|x|}$, concentrated near 0, so small $|x_n|$ point to it.

!!! answer "Answer 4c"
    The test is

    $$\sum_{n=0}^{N-1} |x_n| \underset{\mathcal{H}_1}{\overset{\mathcal{H}_0}{\gtrless}} \gamma'$$

    with the threshold

    $$\boxed{\gamma'=N\ln2-\ln\gamma}$$

    where $\gamma$ is the threshold of the original test $L(\mathbf x)>\gamma$ (the number we choose, or the Bayes value from priors and costs). Special case $\gamma=1$ (equal priors, plain "which is more likely"): $\gamma'=N\ln2$; for $N=1$ that is $\ln2\approx0.693$.

    Read: if the sum is bigger than $\gamma'$ decide $\mathcal H_0$, if it is smaller decide $\mathcal H_1$.

***

**Step 5 · Shade (4d).** Decide $\mathcal H_1$ when $y<1$. $P_{FA}$ = area under the $\mathcal H_0$ curve $e^{-y}$ **left** of 1. $P_M$ = area under the $\mathcal H_1$ curve $2e^{-2y}$ **right** of 1. (Check it in the widget above, tab Nov 2022.)

***

**Step 6 · Threshold from $P_{FA}$ (4e).**
$P_{FA}=\int_0^{\gamma'}e^{-y}\,dy=\big[-e^{-y}\big]_0^{\gamma'}=1-e^{-\gamma'}$. Set it to 0.1: $e^{-\gamma'}=0.9$, so $\gamma'=-\ln0.9\approx\mathbf{0.105}$.

$P_D=\int_0^{\gamma'}2e^{-2y}\,dy=1-e^{-2\gamma'}=1-(e^{-\gamma'})^2=1-0.81=\mathbf{0.19}$.

</div>

## Your turn

!!! exam "Resit, June 2026 · 4b · 1 p"
    A wireless sensor measures the received signal envelope $X$. Under $H_0$ (no device present), $X \sim \text{Rayleigh}(\sigma_0)$. Under $H_1$ (device present), $X \sim \text{Rayleigh}(\sigma_1)$, with $\sigma_1 > \sigma_0 > 0$, both known. The Rayleigh pdf is $p(x \mid \sigma) = \frac{x}{\sigma^2} \exp\left(-\frac{x^2}{2\sigma^2}\right)$, $x \geq 0$.

    - Construct the likelihood-ratio test for a threshold $\eta$.
    - Discuss how the separation between $\sigma_0$ and $\sigma_1$ affects detection performance.

??? solution "Check your answer"
    **What is being asked?** Turn "the two PDFs, compared with the number $\eta$" into a simple rule on $x$ ("decide $H_1$ if $x>\gamma$"), then say what happens when $\sigma_0$ and $\sigma_1$ are close together or far apart. Same steps as [the recipe](#the-recipe).

    **Symbols in this question**

    | Symbol | Meaning |
    |---|---|
    | $X$ | the measured envelope; a Rayleigh variable is always $\ge 0$ |
    | $\sigma_0,\sigma_1$ | the Rayleigh scale: the bigger $\sigma$, the bigger the typical envelope ($\sigma_1\gt\sigma_0$) |
    | $\eta$ | the threshold on the **ratio** — the $\lambda$ of [the idea in one minute](#the-idea-in-one-minute); this exam calls it $\eta$ |
    | $\gamma$ | the threshold on **$x$** we have to find |

    **Step 1 · Ratio, with the $x$ cancelling.** $\mathcal H_1$ on top, $\mathcal H_0$ at the bottom, and we decide $H_1$ when the result is bigger than $\eta$:

    $$L(x)=\frac{p(x\mid H_1)}{p(x\mid H_0)}=\frac{\dfrac{x}{\sigma_1^2}\,e^{-x^2/(2\sigma_1^2)}}{\dfrac{x}{\sigma_0^2}\,e^{-x^2/(2\sigma_0^2)}}\ >\ \eta.$$

    The $x$ in front of both PDFs is the same, so it cancels. Two bookkeeping moves are left: dividing by $\frac{1}{\sigma_0^2}$ is multiplying by $\sigma_0^2$, and $\dfrac{e^{a}}{e^{b}}=e^{a-b}$ (subtract the exponents):

    $$L(x)=\frac{\sigma_0^2}{\sigma_1^2}\;e^{-\frac{x^2}{2\sigma_1^2}+\frac{x^2}{2\sigma_0^2}}=\frac{\sigma_0^2}{\sigma_1^2}\exp\!\Big(\frac{x^2}{2}\Big(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\Big)\Big),$$

    where the exponent was put over the common denominator $\sigma_0^2\sigma_1^2$:

    $$-\frac{x^2}{2\sigma_1^2}+\frac{x^2}{2\sigma_0^2}=\frac{x^2}{2}\Big(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\Big)=\frac{x^2}{2}\cdot\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}.$$

    **Step 2 · Log both sides.** $\ln$ is increasing, so $>$ stays $>$. Use $\ln(ab)=\ln a+\ln b$ and $\ln e^{u}=u$:

    $$\ln\frac{\sigma_0^2}{\sigma_1^2}+\frac{x^2}{2}\cdot\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}\ >\ \ln\eta.$$

    **Step 3 · Isolate $x^2$ (no flip).** Because $\sigma_1\gt\sigma_0$, the bracket $\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}$ is **positive**, so dividing by it later will **not** flip the inequality.

    Move the constant to the right: $\ln\frac{\sigma_0^2}{\sigma_1^2}=-\ln\frac{\sigma_1^2}{\sigma_0^2}$ (because $\ln(1/a)=-\ln a$), so adding $\ln\frac{\sigma_1^2}{\sigma_0^2}$ to both sides turns the right side into $\ln\eta+\ln\frac{\sigma_1^2}{\sigma_0^2}=\ln\!\Big(\eta\frac{\sigma_1^2}{\sigma_0^2}\Big)$:

    $$\frac{x^2}{2}\cdot\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}\ >\ \ln\!\Big(\eta\frac{\sigma_1^2}{\sigma_0^2}\Big).$$

    Now multiply by $2$ and divide by the bracket — dividing by a fraction is multiplying by its upside-down twin $\frac{\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}$:

    $$x^2\ >\ \frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\frac{\sigma_1^2}{\sigma_0^2}\Big).$$

    **Step 4 · Square root, and read the rule.** $x\ge 0$ and the square root is increasing, so still no flip:

    $$x\ >\ \gamma=\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\dfrac{\sigma_1^2}{\sigma_0^2}\Big)}.$$

    Sanity check: $\sigma_1\gt\sigma_0$ means $H_1$ is the **wider** curve, so it is the taller one for large $x$: big envelope → $H_1$. ✓ (If $\eta\,\sigma_1^2/\sigma_0^2\le 1$ the number inside the $\ln$ is $\le 1$, the root is not positive, and every $x$ decides $H_1$.)

    **Step 5 · The second part: how much $\sigma_0$ and $\sigma_1$ matter.** $P_{FA}$ is the area under the $H_0$ curve to the right of $\gamma$:

    $$P_{FA}=\int_\gamma^\infty\frac{x}{\sigma_0^2}e^{-x^2/(2\sigma_0^2)}\,dx=e^{-\gamma^2/(2\sigma_0^2)},$$

    where the substitution $u=\frac{x^2}{2\sigma_0^2}$, $du=\frac{x}{\sigma_0^2}dx$ turns the integral into $\int e^{-u}du=e^{-u}$. The same integral with $\sigma_1$ gives $P_D$, so

    $$P_D=e^{-\gamma^2/(2\sigma_1^2)}=\Big(e^{-\gamma^2/(2\sigma_0^2)}\Big)^{\sigma_0^2/\sigma_1^2}=P_{FA}^{\,\sigma_0^2/\sigma_1^2}.$$

    Numbers: $\sigma_1=2\sigma_0$ gives $P_D=P_{FA}^{1/4}$; at $P_{FA}=0.01$ that is $P_D=0.01^{0.25}=e^{\ln(0.01)/4}=e^{-1.151}=0.32$. With $\sigma_1=3\sigma_0$: $P_D=0.01^{1/9}=e^{-4.605/9}=e^{-0.512}=0.60$.
    So: the further apart $\sigma_0$ and $\sigma_1$, the less the two curves overlap and the more you detect for the same false-alarm rate (the ROC moves to the top-left corner). When $\sigma_1\to\sigma_0$ the exponent $\to 1$, $P_D\to P_{FA}$: no better than guessing.

    !!! answer "Answer"
        Decide $H_1$ if $x>\gamma=\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\dfrac{\sigma_1^2}{\sigma_0^2}\Big)}$.
        Here $P_{FA}=e^{-\gamma^2/(2\sigma_0^2)}$ and $P_D=e^{-\gamma^2/(2\sigma_1^2)}=P_{FA}^{\,\sigma_0^2/\sigma_1^2}$. The further apart $\sigma_0$ and $\sigma_1$, the less the curves overlap and the higher $P_D$ for the same $P_{FA}$. Try it in the widget above, tab Jun 2026.

!!! exam "Final exam, April 2024 · 4b · 1.5 p"

    $$\mathcal{H}_0: p(y) = \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}}\qquad \mathcal{H}_1: p(y) = \frac{1}{4} e^{-\frac{y}{2}},\qquad y > 0.$$

    Sketch the likelihoods. For a threshold $\gamma = 1$, indicate $P_{FA}$ and $P_M$, and calculate $P_D$ and $P_{FA}$. Use $Q(x) = \int_x^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} du$. No need for exact numerical values.

??? solution "Check your answer"
    **What is being asked?** Draw both curves, find the $y$ where one overtakes the other, and compute the two shaded areas.

    **First, the trap in the wording: which threshold is "$\gamma=1$"?** It is the threshold on the **likelihood ratio** (the $\lambda$ of [the idea in one minute](#the-idea-in-one-minute)): decide $\mathcal H_1$ when $\dfrac{p(y\mid\mathcal H_1)}{p(y\mid\mathcal H_0)}>1$, which simply means "decide the story whose curve is **higher**". It is **not** a value of $y$. (The exam reuses the letter: in the Rayleigh question above, $\gamma$ was a threshold on $x$.)

    **Step 1 · Sketch.** $\frac{1}{\sqrt{2\pi}}=0.3989\approx 0.40$ and $\frac14=0.25$. So the $\mathcal H_0$ curve starts at $0.40$ at $y=0$ and falls fast (the Gaussian tail $e^{-y^2/2}$), while the $\mathcal H_1$ curve starts at $0.25$ and falls slowly (the exponential $e^{-y/2}$). $\mathcal H_0$ is taller near $0$, $\mathcal H_1$ is taller far out: they cross exactly once.

    **Step 2 · The ratio $>1$, then log both sides.**

    $$\frac{\frac14\,e^{-y/2}}{\frac{1}{\sqrt{2\pi}}\,e^{-y^2/2}}\ >\ 1.$$

    Take $\ln$ of both sides (increasing, so $>$ stays $>$). One log per factor, using $\ln\frac{a}{b}=\ln a-\ln b$, $\ln e^{u}=u$ and $\ln 1=0$ — the two numbers on top give $\ln\frac14$, the $e$ on top gives $-\frac y2$, and the two at the bottom come with a minus sign ($-\ln\frac{1}{\sqrt{2\pi}}$ and $-\big(-\frac{y^2}{2}\big)=+\frac{y^2}{2}$):

    $$\ln\tfrac14-\tfrac y2-\ln\tfrac{1}{\sqrt{2\pi}}+\tfrac{y^2}{2}\ >\ 0.$$

    Clean the constants: $-\ln\frac{1}{\sqrt{2\pi}}=+\ln\sqrt{2\pi}$, and $\ln\frac14+\ln\sqrt{2\pi}=\ln\frac{\sqrt{2\pi}}{4}$ (because $\ln a+\ln b=\ln ab$):

    $$\frac{y^2}{2}-\frac y2+\ln\frac{\sqrt{2\pi}}{4}\ >\ 0.$$

    Numbers: $\sqrt{2\pi}=2.5066$, $\frac{2.5066}{4}=0.6267$, $\ln 0.6267=-0.4674$, so

    $$\frac{y^2}{2}-\frac y2-0.4674\ >\ 0.$$

    **Step 3 · Clear the halves.** Multiply by 2 (positive → no flip):

    $$y^2-y-0.9348\ >\ 0.$$

    **Step 4 · Solve the quadratic.** Set $y^2-y-0.9348=0$ and use $y=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ with $a=1$, $b=-1$, $c=-0.9348$:

    $$y=\frac{1\pm\sqrt{1+4(0.9348)}}{2}=\frac{1\pm\sqrt{4.739}}{2}=\frac{1\pm2.177}{2},$$

    ($\sqrt{4.739}=2.177$), so the two roots are $1.588$ and $-0.588$. Only $y>0$ exists in this problem, so the only threshold in range is $y_{th}=1.588$.

    **Step 5 · Which side decides $\mathcal H_1$?** The parabola $y^2-y-0.9348$ opens **upward** (the $y^2$ term is positive), so it is positive **outside** the roots: left of $-0.588$ and right of $1.588$. On $y>0$ that leaves $y>1.588$: decide $\mathcal H_1$ for $y>1.588$. It matches the sketch — far out, the slow exponential is the taller curve.

    **Step 6 · Shade.** "Decide $\mathcal H_1$" is the region to the **right** of 1.588. So $P_{FA}$ ($\mathcal H_0$ true, we say $\mathcal H_1$) is the area under the **$\mathcal H_0$** curve right of 1.588, and $P_M$ ($\mathcal H_1$ true, we say $\mathcal H_0$) is the area under the **$\mathcal H_1$** curve **left** of 1.588.

    **Step 7 · Integrate.** $P_{FA}$ first — that integral *is* the $Q$ the question hands you:

    $$P_{FA}=\int_{1.588}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-y^2/2}\,dy=Q(1.588)$$

    (≈ 0.056 if you look it up, but the exam says no number needed).

    For $P_D$: the derivative of $e^{-y/2}$ is $-\frac12 e^{-y/2}$, so $\frac14 e^{-y/2}$ integrates to $-\frac12 e^{-y/2}$:

    $$P_D=\int_{1.588}^{\infty}\frac14 e^{-y/2}\,dy=\Big[-\tfrac12 e^{-y/2}\Big]_{1.588}^{\infty}=0-\big(-\tfrac12 e^{-0.794}\big)=\tfrac12 e^{-0.794}=0.5\cdot 0.452=0.226$$

    ($1.588/2=0.794$, and $e^{-0.794}=0.452$). For completeness, $P_M=\int_0^{1.588}\frac14 e^{-y/2}dy=\frac12\big(1-e^{-0.794}\big)=0.274$.

    !!! trap "These densities are not normalised"
        As printed, each curve integrates to $\frac12$ on $y>0$ (they are two-sided curves cut in half), which is why $P_D+P_M=\frac12$ here and not 1. Use them as printed and say so. If you normalise (×2) all probabilities double ($P_{FA}=2Q(1.588)$, $P_D=e^{-0.794}$) and then $P_M=1-P_D$; the threshold $y_{th}=1.588$ is the same either way.

    !!! answer "Answer"
        Decide $\mathcal H_1$ if $y>1.588$. $P_{FA}=Q(1.588)$; $P_D=\frac12 e^{-0.794}\approx 0.23$; $P_M\approx 0.27$ (as printed). Sketch: the $\mathcal H_0$ curve is a half-bell starting at 0.40, the $\mathcal H_1$ curve a slow exponential starting at 0.25; shade $\mathcal H_0$ right of 1.588 ($P_{FA}$) and $\mathcal H_1$ left of it ($P_M$).

## The theory questions: test yourself

The multiple choice is not about calculating: the same dozen sentences come back every year with one word swapped. So first what the sentences actually mean, then the cards.

### Which trade do you pick? (Neyman–Pearson)

Neither error is free: move the threshold (the widget above) and one shaded area shrinks while the other grows. So a "best detector" has to declare **which** error it is willing to pay for. Two classical answers:

- **Neyman–Pearson (NP).** Decide how many false alarms you can live with ("a smoke alarm that beeps every day is useless": say at most 5 %), and among **all** the tests that keep that promise, catch as many as possible. In one line: ==fix $P_{FA}$, **maximise** $P_D$==.
- **Bayes** ([4.2](e4-bayes.md#the-theory-questions-test-yourself)). Put a price on each mistake and a prior on each hypothesis, and **minimise the average price** (the *risk*). Nothing is fixed.

Why fix $P_{FA}$ and not $P_D$? Under $\mathcal H_0$ there is only noise and its PDF is known, so $P_{FA}$ can be computed exactly and promised. Under $\mathcal H_1$ the signal (its strength, its shape) is often unknown, so no promise about $P_D$ could be kept.

!!! example "Tiny numbers"
    $\mathcal H_0:x\sim\mathcal N(0,1)$, $\mathcal H_1:x\sim\mathcal N(2,1)$ (first tab of the widget). Promise $P_{FA}=0.05$: that forces the threshold to $\gamma=1.645$, because the right tail of $\mathcal H_0$ beyond 1.645 is exactly 0.05. There the detector catches $P_D=Q(1.645-2)=Q(-0.355)=1-Q(0.355)=1-0.361=0.64$.
    Neyman–Pearson's claim: **no other rule whatsoever** keeps 5 % false alarms and catches more than 0.64. And the rule that does achieve it is the likelihood ratio test of this page (with the $\lambda$ that puts the threshold at 1.645) — that is the Neyman–Pearson lemma, and it is why every exam question starts from a ratio.

**How the MC is built.** Swap "maximise" for "minimise"; swap "fixes $P_{FA}$" for "fixes $P_D$"; or hand you the Bayes rule and call it NP. Check **which quantity is fixed** and **which verb**.

### The errors are unavoidable

The two PDFs **overlap**: a value like $x=1.5$ sits under both curves, so whatever you decide you might be wrong. ==No threshold makes $P_{FA}$ and $P_M$ zero together; every test only trades one for the other.== (A detector with both zero would mean the two stories never produce the same data — the PDFs would not overlap at all.)

**The matched filter** (a whole LRT in one line): a **known** signal $s_n$ buried in white Gaussian noise. The recipe gives

$$\sum_{n}x_n\,s_n\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda'$$

— multiply the data with the pattern, sample by sample, and add (**correlate**). Three facts the MC swaps: it **maximises the output SNR**; as a filter its impulse response is the **time-reversed** signal $h[n]=s[N-1-n]$ (writing $h[n]=s[n]$ is the classic wrong option); and with **correlated** noise you first whiten and then correlate (so "only for uncorrelated noise" is false).

**What the ratio collapses to.** Every LRT ends as "one number computed from the data, compared with a threshold". Which number depends only on what changes between $\mathcal H_0$ and $\mathcal H_1$:

| $\mathcal H_0$ vs $\mathcal H_1$ | decide $\mathcal H_1$ when |
|---|---|
| Gaussian, mean 0 vs mean $A>0$ (same $\sigma$) | $\bar x$ (or $\sum x_n$) **large** |
| Gaussian, same mean, $\sigma_1^2\gt\sigma_0^2$ | energy $\sum x_n^2$ **large** |
| Laplacian, $\mathcal H_1$ narrower | $\sum\lvert x_n\rvert$ **small** (the flip!) |
| Rayleigh, $\sigma_1\gt\sigma_0$ | $x$ **large** |
| known signal $s_n$ in white noise | $\sum x_n s_n$ **large** (matched filter) |

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| In the 2×2 table, the diagonal cells are the correct ones (true negative, true positive); the other two are the **miss** = false negative = **type II** error and the **false alarm** = false positive = **type I** error. | T | "Positive" means "we said $\mathcal H_1$". Nov 2022 4a is this table with the cells shuffled: answer (a). |
| Both hypotheses can generate the same observation $\mathbf x$, so a wrong decision cannot be avoided. | T | The PDFs overlap: an $x$ like 1.5 sits under both curves, so it could come from either story. Nov 2022 4a opens with exactly this sentence. |
| There is a threshold that makes $P_{FA}$ and $P_M$ both zero. | F | Push the threshold far right to kill the false alarms and $P_M$ goes to 1 (you never say $\mathcal H_1$). Only non-overlapping PDFs could do both — but then you would not need a test. |
| The Neyman–Pearson test fixes $P_{FA}$ and then **maximises** $P_D$. | T | Fix the false alarms you can live with, then catch as many as you can — the sentence just above. (Nov 2022 4b (b), Apr 2024 4a.) |
| The Neyman–Pearson test fixes $P_{FA}$ and then **minimises** $P_D$. | F | Same words, swapped verb: minimising $P_D$ means *catching as few as possible*. That is the classic wrong option. |
| The test that solves the Neyman–Pearson problem is a likelihood ratio test. | T | NP's lemma: thresholding $L(x)$ = "decide $\mathcal H_1$ when this $x$ is explained this much better by $\mathcal H_1$" is exactly what buys the highest $P_D$ for a given $P_{FA}$. |
| The likelihood ratio test needs the priors $P_0,P_1$. | F | The ratio is only the two PDFs, so the rule works without any prior. Priors enter the **Bayes** threshold $\lambda=P_0/P_1$ ([4.2](e4-bayes.md)), i.e. where the line is drawn, not how it is built. |
| Taking $\ln$ of the likelihood ratio changes the decisions of the test. | F | $\ln$ is strictly increasing: $a>b\Leftrightarrow\ln a>\ln b$, so exactly the same $x$'s land in "decide $\mathcal H_1$". The log only turns products into sums (algebra); it never moves the decision. |
| An ROC curve has $P_D$ on the vertical axis and $P_{FA}$ on the horizontal, and a good detector bows to the top-left corner. | T | It runs from $(0,0)$ (never say $\mathcal H_1$) to $(1,1)$ (always); the diagonal is guessing. |
| An ROC below the diagonal is caused by using a wrong $\sigma$ in your model. | F | A wrong $\sigma$ only flattens the curve. Below the diagonal means the decision is **flipped**: $\mathcal H_0/\mathcal H_1$ swapped in the ratio, $P_D$ computed with the CDF instead of the tail, or the two axes swapped (Practice exam 2021 1e: the wrong $\sigma$ is the one that *cannot* be the reason). |
| The matched filter maximises the output SNR for a known signal in white noise. | T | Giving the biggest weights to the biggest samples of the pattern squeezes the most signal out of the noise — no other linear filter does better (Cauchy–Schwarz). Jan 2022 4a (a). |
| The matched filter has impulse response $h[n]=s[n]$. | F | A convolution **flips** one of the signals, so to end up correlating $\sum x_ns_n$ the filter must contain the already flipped pattern $h[n]=s[N-1-n]$ (time-reversed). $h[n]=s[n]$ correlates with the pattern backwards. |
| The matched filter can only be applied when the noise samples are uncorrelated. | F | The *derivation* assumed white noise, but with correlated noise you whiten first (undo the correlation) and then correlate. "Assumed" ≠ "only works for". |
| To decide between two zero-mean Gaussians that differ only in their variance, the LRT compares the energy $\sum x_n^2$ with a threshold. | T | The "energy detector": more variance shows up as more energy (Practice exam 2021 4b, Nov 2019). |
| When $\mathcal H_1$ is the **narrower** PDF, the test decides $\mathcal H_1$ for **large** values of the statistic. | F | The narrow curve wins near the centre, so the rule flips: decide $\mathcal H_1$ when $\sum\lvert x_n\rvert$ is **small** (Nov 2022 4c). |

</div>

## Traps

!!! trap key "Where points are lost"
    - **Forgetting to flip** when you divide by a negative number. Then the whole rule points the wrong way.
    - **Wrong curve for the area**: $P_{FA}$ always uses $p(x\mid\mathcal H_0)$, $P_D$ and $P_M$ always use $p(x\mid\mathcal H_1)$.
    - **Shading the wrong side**: first decide where "decide $\mathcal H_1$" is (left or right of $\gamma$), then shade.
    - $N$ samples: the ratio is a **product**, its log a **sum** $\sum_n$. Do not drop the $N$ in front of constants ($2^N\to N\ln2$).
