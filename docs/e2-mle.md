# 2.1 Maximum likelihood (MLE)

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>1 point</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

$\theta$ is a knob on the model. For each knob position, the model says how likely our data were. The **MLE** $\hat\theta$ is the knob position that makes **the data we actually saw** most likely.

"How likely the data were" = the product of the PDF heights at the data points (independent samples → multiply). Move the knob below: each red stick is one point's height, and the bottom curve adds up their logs.

<div class="widget" data-w="likelihood"></div>

The top of the bottom curve is where its slope is zero. That is the whole method: **write it, take the log, differentiate, set to 0**. We take the log because it turns the product into a sum (easy to differentiate) and does not move the top.

## How to fight this section with the sheet

The exam says **"derive the MLE"** → you open **box 2A** on your A4 sheet and do its 3 steps with the pdf they gave you. That is the whole method. Every question below is the same 3 steps on a different pdf — the steps never change, only the pdf does.

Each step below names **the sheet's term it uses**, term by term: which pieces sit above the line, which below, which rule turns each one into the next line. Press **Next step** to go one at a time — cover the step, do it yourself, then reveal it.

!!! sheet "Box 2A, exactly as it is printed on the sheet"
    **IF YOU SEE** a pdf $p(x\mid\theta)$, samples $x_1..x_N$, "maximum likelihood", "derive the MLE", "find an estimator", "estimate of …"

    1. Take $\ln$ of ONE sample's pdf, then put $\sum_n$ in front. That is $\ln L$. A term without $x_n$ gets multiplied by $N$.
    2. Differentiate with respect to $\theta$ (terms without $\theta$ disappear).
    3. Set it $=0$ and solve for $\theta$. That is $\hat\theta$.

    **How to take $\ln$ of a pdf:** write the pdf as $\frac{\text{above}}{\text{below}}\cdot e^{u}$ (it is pieces multiplied, some in a fraction). Then each piece becomes one term: a piece $a$ **above the line** → $+\ln a$ · a piece $b$ **below the line** → $-\ln b$ · $e^{u}$ → just $u$ (the $e$ disappears). Two pieces below the line split: $-\ln(2\theta)=-\ln 2-\ln\theta$. A power $\theta^k$ below the line → $-k\ln\theta$.

    Derivatives: $\ln\theta\to\frac1\theta$ · $\theta^k\to k\theta^{k-1}$ · $\frac1\theta\to-\frac1{\theta^2}$ · $e^{c\theta}\to ce^{c\theta}$ · $\cos\theta\to-\sin\theta$ · $\sin\theta\to\cos\theta$.
    Solving $=0$: multiply the equation by the denominators ($\theta^2$, $\theta$, …) first — that does not change the root.
    **Trap:** if the pdf only exists for $x$ up to something containing $\theta$ (uniform on $[0,\theta]$), these 3 steps are useless — $\hat\theta=\max_n x_n$, and **the CRLB does not exist**.
    **Fisher info / CRLB** from that same derivative: $i(\theta)=-\mathrm E\big[\frac{\partial^2\ln p}{\partial\theta^2}\big]$ for one sample; $N$ samples → $\mathcal I=N i(\theta)$; **CRLB** $=\frac{1}{N i(\theta)}$.
    **Known $i(\theta)$** — skip the derivation: Gaussian mean with variance $\sigma^2$: $\frac1{\sigma^2}$ · exponential rate $\lambda$: $\frac1{\lambda^2}$ · Bernoulli: $\frac1{\theta(1-\theta)}$ · Rayleigh $\frac{x}{\theta^2}e^{-x^2/2\theta^2}$: $\frac4{\theta^2}$ (so CRLB $=\frac{\theta^2}{4N}$).

    *Apr24* $\frac{x}{2\theta}e^{-x^2/2\theta}$: one sample gives $\ln x-\ln2-\ln\theta-\frac{x^2}{2\theta}$, so $\ln L=\sum\ln x_n-N\ln2-N\ln\theta-\frac{\sum x_n^2}{2\theta}$ → $-\frac N\theta+\frac{\sum x_n^2}{2\theta^2}=0$ → $\hat\theta=\frac1{2N}\sum x_n^2$.

    *Jun26* Gamma $\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$, $n$ patients: $-\frac{nk}\theta+\frac{\sum x_i}{\theta^2}=0$ → $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}k$. Meaning: average time per stage, so $k\hat\theta$ = the observed mean time.

    **Sigmoid trick.** IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then convert with $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.

    *Apr25* $3\lambda e^{-4\lambda x/7}$: $\frac1\lambda-\frac{4x}7=0$ → $\hat\lambda=\frac7{4x}$ → $\hat\theta=-\ln\!\big(\frac{4x}7-1\big)$, valid for $x\gt\frac74$.

One caution on the sheet's *Derivatives* line: read it item by item — it is **not** $\ln\theta\to\frac1{\theta^2}$, that is the *next* item ($\frac1\theta\to-\frac1{\theta^2}$).

What "above the line / below the line" means, on the pdf of exercise 1:

| the piece | where it sits | what its $\ln$ becomes |
|---|---|---|
| $x_n$ | above the line (it multiplies) | $+\ln x_n$ |
| $2\theta$ | below the line (it divides) | $-\ln 2-\ln\theta$ (the two pieces split) |
| $\theta^k$ | below the line | $-k\ln\theta$ |
| $e^{-x_n^2/2\theta}$ | the $e$ part | just the exponent: $-\frac{x_n^2}{2\theta}$ |

Two more sheet places you will need: the **Calculations** strip (bottom of the sheet) for the $\ln$/$e$ and fraction algebra, and **box 2D** for the true/false questions. Each exercise below tells you which one.

## 1 · April 2024 · 2c — the classic. Read this one with the sheet next to you

!!! exam "Final exam, April 2024 · 2c · 1 p"
    For the data vector $\mathbf{x} = \{x_1, \dots, x_N\}$ consisting of independent samples with probability density function

    $$p(x_n | \theta) = \frac{x_n}{2\theta} e^{-\frac{x_n^2}{2\theta}},$$

    derive the MLE for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A, every term named"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term** ("a piece above the line → $+\ln a$; a piece below → $-\ln b$; $e^{u}$ → $u$").
    One sample is $\frac{x_n}{2\theta}e^{-x_n^2/2\theta}$. Its three pieces:

    - $x_n$ — **above the line** → $+\ln x_n$
    - $2\theta$ — **below the line**, two pieces $2$ and $\theta$ → $-\ln 2-\ln\theta$ (they split — Calculations strip: $\ln\frac ab=\ln a-\ln b$)
    - $e^{-x_n^2/2\theta}$ — **the $e$ part** → just the exponent: $-\frac{x_n^2}{2\theta}$

    $$\ln p(x_n\mid\theta)=\ln x_n-\ln 2-\ln\theta-\frac{x_n^2}{2\theta}$$

    ***

    **Sheet step 2 · put $\sum_n$ in front** ("a term without $x_n$ gets multiplied by $N$").
    $\ln x_n$ keeps its $\sum_n$. The other three have no $x_n$ → they get $\times N$ (and $\sum_n$ of the last one pulls out $\sum x_n^2$):

    $$\ln L=\sum_n\ln x_n-N\ln 2-N\ln\theta-\frac{1}{2\theta}\sum_n x_n^2$$

    ***

    **Sheet step 3 · differentiate, term by term** ("terms without $\theta$ disappear", then the sheet's derivative rules).

    - $\sum_n\ln x_n$ — no $\theta$ → **disappears**
    - $-N\ln 2$ — no $\theta$ → **disappears**
    - $-N\ln\theta$ — rule $\ln\theta\to\frac1\theta$ → $-\frac N\theta$
    - $-\frac{1}{2\theta}\sum x_n^2$ — rule $\frac1\theta\to-\frac1{\theta^2}$ (minus times minus is plus) → $+\frac{1}{2\theta^2}\sum x_n^2$

    $$\frac{d}{d\theta}\ln L=-\frac N\theta+\frac{1}{2\theta^2}\sum_n x_n^2$$

    ***

    **Sheet step 4 · "Set it $=0$ and solve. Multiply by the denominators first."**
    The denominator is $\theta^2$ → multiply the whole equation by $\theta^2$:

    $$-N\theta+\frac12\sum_n x_n^2=0\quad\Longrightarrow\quad \hat\theta=\frac{1}{2N}\sum_n x_n^2$$

    ***

    **Sheet check · the box's steps.**
    You ended where step 3 says: the derivative $=0$, solved for $\theta$. The sheet's *Apr24* line runs the same three steps on this pdf and lands on the same $\hat\theta=\frac1{2N}\sum x_n^2$ — the steps are what you copy, not the line.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{2N}\sum_{n=1}^N x_n^2$

## 2 · Q1 2023 resit · 2b — same pdf, the 2 disappeared

!!! exam "Q1 2023 resit · 2b"
    For the data vector $\mathbf{x} = \{x_1, \dots x_N\}$ consisting of independent samples with probability density function

    $$p(\mathbf{x} | \theta) = \prod_{n=1}^N \frac{x_n}{\theta} e^{-\frac{x_n^2}{\theta}},$$

    derive the MLE for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A again — this is exercise 1 without the 2"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term.**
    The $\prod$ in front is just the exam writing the likelihood for you. One sample is $\frac{x_n}{\theta}e^{-x_n^2/\theta}$:

    - $x_n$ — **above the line** → $+\ln x_n$
    - $\theta$ — **below the line** → $-\ln\theta$
    - $e^{-x_n^2/\theta}$ — **the $e$ part** → $-\frac{x_n^2}{\theta}$

    $$\ln p(x_n\mid\theta)=\ln x_n-\ln\theta-\frac{x_n^2}{\theta}$$

    ***

    **Sheet step 2 · put $\sum_n$** ("a term without $x_n$ gets $\times N$").

    $$\ln L=\sum\ln x_n-N\ln\theta-\frac1\theta\sum x_n^2$$

    ***

    **Sheet step 3 · differentiate, term by term.**

    - $\sum\ln x_n$ — no $\theta$ → **disappears**
    - $-N\ln\theta$ — rule $\ln\theta\to\frac1\theta$ → $-\frac N\theta$
    - $-\frac1\theta\sum x_n^2$ — rule $\frac1\theta\to-\frac1{\theta^2}$ → $+\frac{1}{\theta^2}\sum x_n^2$

    $$\frac{d}{d\theta}\ln L=-\frac N\theta+\frac{1}{\theta^2}\sum x_n^2$$

    ***

    **Sheet step 4 · $=0$, multiply by $\theta^2$** (the sheet: clear the denominators first).
    $-N\theta+\sum x_n^2=0$.

    ***

    **Sheet check.**
    Compare with exercise 1. The only change is the missing 2 → the answer lost its 2.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{N}\sum_{n=1}^N x_n^2$

## 3 · Practice exam 2021 · 2b — the number in front never matters

!!! exam "Practice exam, October 2021 · 2b"
    For the data vector $\mathbf{x}$ consisting of independent samples with probability density function $p(x[n]) = \frac{x}{\theta} \exp\left(-\frac{x^2}{2\theta}\right)$, where $n = 0, 1, \dots, N-1$, find an estimator for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A — and the rule that saves you here"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term.**
    "Find an estimator" with a pdf and samples = derive the MLE = box 2A. One sample: $\frac{x_n}{\theta}e^{-x_n^2/2\theta}$:

    - $x_n$ — **above the line** → $+\ln x_n$
    - $\theta$ — **below the line** → $-\ln\theta$
    - $e^{-x_n^2/2\theta}$ — **the $e$ part** → $-\frac{x_n^2}{2\theta}$

    $$\ln p=\ln x_n-\ln\theta-\frac{x_n^2}{2\theta}$$

    ***

    **Sheet step 2 · put $\sum_n$** ("a term without $x_n$ gets $\times N$").

    $$\ln L=\sum\ln x_n-N\ln\theta-\frac{1}{2\theta}\sum x_n^2$$

    ***

    **Sheet step 3 · differentiate, term by term.**

    - $\sum\ln x_n$ — no $\theta$ → **disappears**
    - $-N\ln\theta$ — rule $\ln\theta\to\frac1\theta$ → $-\frac N\theta$
    - $-\frac{1}{2\theta}\sum x_n^2$ — rule $\frac1\theta\to-\frac1{\theta^2}$ → $+\frac{1}{2\theta^2}\sum x_n^2$

    $$\frac{d}{d\theta}\ln L=-\frac N\theta+\frac{1}{2\theta^2}\sum x_n^2$$

    ***

    **Sheet step 4 · $=0$, multiply by $\theta^2$.**
    $-N\theta+\frac12\sum x_n^2=0$.

    ***

    **Sheet check.**
    This is exercise 1 again (the $\frac12$ sits in the exponent in both). Numbers in front that do not contain $\theta$ never change the answer — the sheet's ln rules turn them into constants that vanish in step 3.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{2N}\sum_{n=0}^{N-1} x^2[n]$

## 4 · November 2019 · 3a — $\theta^2$, so $-2\ln\theta$

!!! exam "Written exam, November 2019 · 3a"
    The data $x[0], x[1], \dots, x[N-1]$ are observed, where $x[n]$'s are independent and identically distributed according to the PDF

    $$p(x; \theta) = \frac{x}{\theta^2} \exp \left[ -\frac{x^2}{2\theta^2} \right], \quad x \geq 0.$$

    (a) Find the maximum likelihood estimator for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A, the $\theta^k$ rule does the work"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term.**
    One sample: $\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}$:

    - $x$ — **above the line** → $+\ln x$
    - $\theta^2$ — **below the line, a power** → sheet rule "$\theta^k$ below → $-k\ln\theta$" with $k=2$ → $-2\ln\theta$
    - $e^{-x^2/(2\theta^2)}$ — **the $e$ part** → $-\frac{x^2}{2\theta^2}$

    $$\ln p=\ln x-2\ln\theta-\frac{x^2}{2\theta^2}$$

    ***

    **Sheet step 2 · put $\sum_n$** ("a term without $x_n$ gets $\times N$"; the $-2\ln\theta$ becomes $-2N\ln\theta$).

    $$\ln L=\sum\ln x_n-2N\ln\theta-\frac{1}{2\theta^2}\sum x_n^2$$

    ***

    **Sheet step 3 · differentiate, term by term.**

    - $\sum\ln x_n$ — no $\theta$ → **disappears**
    - $-2N\ln\theta$ — rule $\ln\theta\to\frac1\theta$ → $-\frac{2N}{\theta}$
    - $-\frac{1}{2\theta^2}\sum x_n^2$ — rule $\theta^k\to k\theta^{k-1}$ with $k=-2$ → $+\frac{1}{\theta^3}\sum x_n^2$

    $$-\frac{2N}{\theta}+\frac{1}{\theta^3}\sum x_n^2=0$$

    ***

    **Sheet step 4 · $=0$, clear the denominators, then get the letter alone.**
    Multiply by $\theta^3$ (the sheet: clear the denominators first): $-2N\theta^2+\sum x_n^2=0$ → $\theta^2=\frac{\sum x_n^2}{2N}$. The sheet's Calculations strip: "$x^k=a$ → $x=a^{1/k}$" → the square root. $\theta>0$, so the $+$ root.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\sqrt{\frac{1}{2N}\sum_{n=0}^{N-1} x^2[n]}$

## 5 · January 2019 retake · 2a — exponential, the easiest one

!!! exam "Retake, January 2019 · 2a"
    For the random variable $x$ with distribution

    $$p(x; \lambda) = \lambda e^{-\lambda x}$$

    find the maximum likelihood estimator for $\lambda$, given $N$ independent identically distributed observations $x_i, i \in \{0 : N - 1\}$.

!!! sheet "In the cheat sheet: box 2A (the unknown is called $\lambda$ — same box)"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term.**
    One sample: $\lambda e^{-\lambda x}$ — no fraction at all, so nothing sits below a line:

    - $\lambda$ — **above the line** → $+\ln\lambda$
    - $e^{-\lambda x}$ — **the $e$ part** → $-\lambda x$

    $$\ln p=\ln\lambda-\lambda x$$

    ***

    **Sheet step 2 · put $\sum_n$** (sheet's sum rule $\sum_n\lambda x_n=\lambda\sum x_n$).

    $$\ln L=N\ln\lambda-\lambda\sum x_i$$

    ***

    **Sheet step 3 · differentiate, term by term.**

    - $N\ln\lambda$ — rule $\ln\theta\to\frac1\theta$ (here the letter is $\lambda$) → $\frac N\lambda$
    - $-\lambda\sum x_i$ — rule $(c\,\theta)\to c$ → $-\sum x_i$

    $$\frac{d}{d\lambda}\ln L=\frac N\lambda-\sum x_i$$

    ***

    **Sheet step 4 · $=0$, multiply by $\lambda$.**
    $N-\lambda\sum x_i=0$ → $\hat\lambda=\frac{N}{\sum x_i}=\frac1{\bar x}$.

    ***

    **Sheet check.**
    This pdf also appears in box 2B ("one observation: exponential → $\lambda e^{-\lambda x}$") — there it is a prior/likelihood ingredient; here it is the whole question. Same shape, box 2A still applies.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\lambda_{ML}=\frac{N}{\sum_i x_i}=\frac{1}{\bar x}$

## 6 · June 2026 resit · 2b — Gamma, and "what does it tell us"

!!! exam "Resit, June 2026 · 2b · 1 p"
    Recovery times $X\sim\text{Gamma}(k,\theta)$, $k$ known, $\theta>0$ unknown, with pdf $p(x \mid \theta) = x^{k-1} e^{-x/\theta} / (\theta^k \Gamma(k))$, $x > 0$. Write the likelihood and log-likelihood for $x_1, \dots, x_n$, derive the MLE of $\theta$, and explain what it tells us.

!!! sheet "In the cheat sheet: box 2A, its own *Jun26* example line"
    <div class="stepper" markdown>

    **Sheet step 1 · take $\ln$ of ONE sample, term by term.**
    One sample: $\frac{x^{k-1}e^{-x/\theta}}{\theta^k\Gamma(k)}$ — four pieces:

    - $x^{k-1}$ — **above the line** → $+(k-1)\ln x$
    - $e^{-x/\theta}$ — **the $e$ part** → $-\frac x\theta$
    - $\theta^k$ — **below the line, a power** → sheet rule "$\theta^k$ below → $-k\ln\theta$" → $-k\ln\theta$
    - $\Gamma(k)$ — **below the line**, no $\theta$ → $-\ln\Gamma(k)$ (just a constant)

    $$\ln p=(k-1)\ln x-\frac x\theta-k\ln\theta-\ln\Gamma(k)$$

    ***

    **Sheet step 2 · put $\sum_n$** ("a term without $x_n$ gets $\times N$" — here $n$ samples).

    $$\ln L=(k-1)\sum\ln x_i-\frac1\theta\sum x_i-nk\ln\theta-n\ln\Gamma(k)$$

    ***

    **Sheet step 3 · differentiate, term by term.**

    - $(k-1)\sum\ln x_i$ and $-n\ln\Gamma(k)$ — no $\theta$ → **disappear**
    - $-\frac1\theta\sum x_i$ — rule $\frac1\theta\to-\frac1{\theta^2}$ → $+\frac{1}{\theta^2}\sum x_i$
    - $-nk\ln\theta$ — rule $\ln\theta\to\frac1\theta$ → $-\frac{nk}{\theta}$

    $$\frac{d}{d\theta}\ln L=\frac{1}{\theta^2}\sum x_i-\frac{nk}{\theta}$$

    ***

    **Sheet step 4 · $=0$, multiply by $\theta^2$.**
    $\sum x_i-nk\theta=0$ → $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}{k}$.

    ***

    **Sheet check · the meaning line.**
    The sheet's *Jun26* line says it in one sentence: a Gamma variable has mean $k\theta$, so $\hat\theta$ = average recovery time per stage, and $k\hat\theta$ = the observed mean time.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{\sum x_i}{nk}=\frac{\bar x}{k}$ — average recovery time divided by the number of stages $k$

## 7 · April 2025 · 2c — sigmoid, use the trick at the bottom of box 2A

!!! exam "Final exam, 13 April 2025 · 2c · 1 p"
    Consider the likelihood $p(x|\theta) = 3\lambda(\theta)e^{-4\frac{\lambda(\theta)x}{7}}, \ x > 1$, where $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$ (logistic sigmoid). Derive the MLE for $\theta$. Hint: $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

!!! sheet "In the cheat sheet: box 2A · Sigmoid trick"
    <div class="stepper" markdown>

    **Sheet step 0 · the trick.**
    The sheet says: **IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.** Do exactly that — ignore the $\theta$ until the last line.

    ***

    **Sheet step 1 · take $\ln$, term by term (the unknown is $\lambda$).**
    One sample: $3\lambda e^{-4\lambda x/7}$:

    - $3$ — **above the line**, no $\lambda$ → $\ln 3$ (a constant)
    - $\lambda$ — **above the line** → $+\ln\lambda$
    - $e^{-4\lambda x/7}$ — **the $e$ part** → $-\frac{4x}{7}\lambda$

    $$\ln p=\ln 3+\ln\lambda-\frac{4x}{7}\lambda$$

    ***

    **Sheet step 2 · differentiate in $\lambda$, term by term.**

    - $\ln 3$ — no $\lambda$ → **disappears**
    - $\ln\lambda$ — rule $\ln\theta\to\frac1\theta$ → $\frac1\lambda$
    - $-\frac{4x}7\lambda$ — rule $(c\,\theta)\to c$ → $-\frac{4x}7$

    $$\frac{d}{d\lambda}\ln p=\frac1\lambda-\frac{4x}7$$

    ***

    **Sheet step 3 · $=0$, multiply by $\lambda$** → $1-\frac{4x}7\lambda=0$ → $\hat\lambda=\frac{7}{4x}$.

    ***

    **Sheet step 4 · the sheet's conversion formula.**
    $\hat\theta=-\ln\!\big(\frac{1}{\hat\lambda}-1\big)=-\ln\!\big(\frac{4x}{7}-1\big)$.

    ***

    **Sheet check · the range.**
    The Calculations strip: "$\ln$ of a positive number" → $\frac{4x}7-1>0$ → $x>\frac74$. (If you differentiate in $\theta$ with the hint, the extra factor $\lambda(1-\lambda)$ is never 0, so you land on the same answer — the sheet's trick just avoids that mess.)

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=-\ln\!\left(\frac{4x}{7}-1\right)$, valid for $x>\frac74$

## 8 · January 2025 resit · 2b — one observation, and the letters are the data

!!! exam "Resit, January 2025 · 2b"
    Assume that

    $$p(\mu, \sigma, \theta | \rho) = \frac{1}{2\pi(1-\theta^2)^{1/2}} \exp\left(-\frac{\mu^2\rho^2 - 2\rho\mu\sigma\theta + \sigma^2\rho^2}{2(1-\theta^2)}\right)$$

    Determine the maximum likelihood estimate of $\rho$ for a single observation of $\mu, \sigma, \theta$.

    (*Note: $\rho$ is the unknown parameter; $\mu, \sigma, \theta$ are the observed data.*)

!!! sheet "In the cheat sheet: box 2A — the unknown is $\rho$, everything else is a number"
    <div class="stepper" markdown>

    **Sheet step 0 · read who is the unknown.**
    This one looks scary because of the letters. Follow the sheet literally: the unknown is $\rho$, so every term without $\rho$ disappears in step 3 — $\mu,\sigma,\theta$ are just data, treat them as numbers.

    ***

    **Sheet step 1 · take $\ln$, term by term.**
    One sample: $\frac{1}{2\pi(1-\theta^2)^{1/2}}\cdot e^{-\frac{\mu^2\rho^2-2\rho\mu\sigma\theta+\sigma^2\rho^2}{2(1-\theta^2)}}$:

    - $\frac{1}{2\pi(1-\theta^2)^{1/2}}$ — a fraction, but **no $\rho$ anywhere in it** → it is a constant (it will disappear in step 3)
    - $e^{-(\dots)}$ — **the $e$ part** → just the exponent, with its minus: $-\frac{\mu^2\rho^2-2\rho\mu\sigma\theta+\sigma^2\rho^2}{2(1-\theta^2)}$

    $$\ln p=\text{const}-\frac{\mu^2\rho^2-2\rho\mu\sigma\theta+\sigma^2\rho^2}{2(1-\theta^2)}$$

    ***

    **Sheet step 2 · put $\sum_n$.**
    One observation only → $N=1$, nothing to sum. Same line as above.

    ***

    **Sheet step 3 · differentiate in $\rho$, term by term.**
    The bottom $2(1-\theta^2)$ is a number (no $\rho$) and stays put. Only the top changes, piece by piece (rules $\theta^k\to k\theta^{k-1}$ and $(c\,\theta)\to c$):

    - $\mu^2\rho^2$ → $2\mu^2\rho$
    - $-2\rho\mu\sigma\theta$ → $-2\mu\sigma\theta$
    - $\sigma^2\rho^2$ → $2\sigma^2\rho$

    $$\frac{d}{d\rho}\ln p=-\frac{2\mu^2\rho-2\mu\sigma\theta+2\sigma^2\rho}{2(1-\theta^2)}$$

    ***

    **Sheet step 4 · $=0$, clear the denominators.**
    Multiply by $2(1-\theta^2)$ (the sheet: clear the denominators first): $2\rho(\mu^2+\sigma^2)-2\mu\sigma\theta=0$.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\rho_{ML}=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}$

## 9 · November 2022 · 2d — the model is the sheet's phase family, and the steps prove it

!!! exam "Final exam, November 2022 · 2d · 1 p"
    Consider the observation

    $$\mathbf{x} = A \begin{bmatrix} \cos(\theta) \\ \sin(\theta) \end{bmatrix} + \mathbf{w},$$

    where $\mathbf{w}$ is white Gaussian noise with variance $\sigma^2$. The pdf of the observation is

    $$p(\mathbf{x}; \theta) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{1}{2\sigma^2} \left((x_1 - A \cos(\theta))^2 + (x_2 - A \sin(\theta))^2\right)\right)$$

    Find the maximum likelihood estimator of the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2D, last line"
    <div class="stepper" markdown>

    **Sheet step 0 · look at box 2D first.**
    Box 2D has the rule for this whole family: *"Fisher info for $x$ = signal($\theta$) + Gaussian noise $\sigma^2$"* plus the phase case *"$A[\cos\theta,\sin\theta]$: **phase MLE** $=\arctan\frac{x_2}{x_1}$ (point the model vector at the data)"*. Your model *is* that family, so the rule gives $\hat\theta=\arctan\frac{x_2}{x_1}$ — and steps 1–3 below derive it, in case the exam changes the model.

    ***

    **Sheet step 1 · take $\ln$, term by term (if you want to see why).**

    - $\frac{1}{2\pi\sigma^2}$ — a constant, no $\theta$ → **disappears**
    - $e^{-\frac{1}{2\sigma^2}(\dots)}$ — **the $e$ part** → $-\frac{1}{2\sigma^2}\big((x_1-A\cos\theta)^2+(x_2-A\sin\theta)^2\big)$

    Maximising $\ln p$ = minimising that square.

    ***

    **Sheet step 2 · expand the square** (expand: $(a-b)^2=a^2-2ab+b^2$, and $\cos^2\theta+\sin^2\theta=1$).
    $x_1^2+x_2^2+A^2-2A(x_1\cos\theta+x_2\sin\theta)$. The only $\theta$ part is $-2A(x_1\cos\theta+x_2\sin\theta)$, so you must **maximise** $x_1\cos\theta+x_2\sin\theta$.

    ***

    **Sheet step 3 · maximise $x_1\cos\theta+x_2\sin\theta$.**
    It is biggest when the direction $[\cos\theta,\sin\theta]$ points the same way as the data $(x_1,x_2)$: $\cos\theta=\frac{x_1}{\sqrt{x_1^2+x_2^2}}$, $\sin\theta=\frac{x_2}{\sqrt{x_1^2+x_2^2}}$ → $\tan\theta=\frac{x_2}{x_1}$ → $\hat\theta=\arctan\frac{x_2}{x_1}$, exactly what box 2D's phase rule said.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\arctan\frac{x_2}{x_1}$ (box 2D's phase rule; steps 1–3 derive it)

## 10 · November 2022 · 2b — true/false, read the row

!!! exam "Final exam, November 2022 · 2b · 0.5 p"
    Which of the following statements about the maximum likelihood estimator is TRUE?

    - (a) The maximum likelihood estimator always achieves the Cramér-Rao lower bound.
    - (b) The maximum likelihood estimator can only be found for special estimation problems, such as linear signal models.
    - (c) The maximum likelihood estimator is asymptotically unbiased.

!!! sheet "In the cheat sheet: box 2D, three rows"
    <div class="stepper" markdown>

    **Sheet step 1 · the row "MLE always reaches the CRLB / only for linear models" → F.**
    That one row kills **(a)** and **(b)** in a single look (this is what the sheet means: one row covers both distractors).

    ***

    **Sheet step 2 · the row "MLE is asymptotically unbiased" → T (Nov22 c).**
    The sheet's row is the fact itself; the exam only rewords it.

    </div>

!!! answer "Answer"
    **(c)**

## 11 · January 2022 resit · 2b — true/false, the invariance row

!!! exam "Resit, January 2022 · 2b · 0.5 p"
    Which of the following statements about the maximum likelihood estimator is true?

    - (a) The maximum likelihood estimate is the value of $x$ that maximizes the likelihood function.
    - (b) For large sample sizes, the maximum likelihood estimate is uniformly distributed, i.e., $\hat{\theta}_{ML} \sim \text{Uniform}(-a, a)$ where $a = \mathcal{I}^{-1}(\theta)$.
    - (c) For a transformed parameter $\alpha = \psi(\theta)$, where $\psi(\cdot)$ is a one-to-one mapping, the maximum likelihood estimate $\hat{\theta}_{ML}$ can be obtained as $\hat{\theta}_{ML} = \psi^{-1}(\hat{\alpha}_{ML})$.

!!! sheet "In the cheat sheet: box 2D"
    <div class="stepper" markdown>

    **Sheet step 1 · (a) vs the row "MLE maximises the likelihood over $\theta$" → T ("over $x$": F).**
    **(a)** says "the value of $x$" → **F**. This row is written exactly for this distractor.

    ***

    **Sheet step 2 · (c) vs the row "MLE of $\alpha=\psi(\theta)$: $\hat\theta=\psi^{-1}(\hat\alpha)$" → T (Jan22 c).**
    That is **(c)** word for word.

    ***

    **Sheet step 3 · (b) is not on the sheet as a row.**
    But the sheet says the MLE is asymptotically unbiased and its variance sits at $\frac1{\mathcal I}$ — a uniform distribution is not that. And "one-to-one" is the same condition as the sigmoid trick in box 2A.

    </div>

!!! answer "Answer"
    **(c)**

## 12 · January 2019 retake · 1b — which box is which

!!! exam "Retake, January 2019 · 1b"
    Which expression describes the maximum likelihood estimator?

    - A. $\hat{\theta} = \arg \min_{\theta} \sum_{n=1}^N (x[n] - s[n; \theta])^2$
    - B. $\hat{\theta} = \arg \min_{\hat{\theta}} \int (\hat{\theta} - \theta)^2 p(x|\theta) dx$
    - C. $\hat{\theta} = \arg \max_{\theta} p(\theta|x)$
    - D. $\hat{\theta} = \arg \max_{\theta} p(x|\theta)$

!!! sheet "In the cheat sheet: it is a 'which box' question — match each option to a box"
    <div class="stepper" markdown>

    **Sheet step 1 · A and B are least squares / MMSE, not MLE.**
    **A** = minimise a squared error over data points → **box 2C** (least squares). **B** = minimise a squared error averaged over the pdf → **MMSE**, box 2B's table ("MMSE = the mean of the posterior; minimises squared error").

    ***

    **Sheet step 2 · C is MAP.**
    $p(\theta\mid x)$ is the **posterior** → **MAP**, box 2B ("MAP needs a prior").

    ***

    **Sheet step 3 · D is the box 2A row.**
    $p(x\mid\theta)$ is the likelihood, and the sheet's row says it: *"MLE maximises the likelihood over $\theta$"*. The likelihood is $p(\text{data}\mid\theta)=p(x\mid\theta)$.

    </div>

!!! answer "Answer"
    **D**

## Traps

!!! trap "Where points are lost (each one is a line of the sheet you skipped)"
    - Forgetting the $-N\ln\theta$ that comes from the $\frac1\theta$ in front (sheet: "a piece $b$ below the line → $-\ln b$"). It is half of the answer.
    - Wrong sign on $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$ — minus times minus gives a **plus** in the derivative (sheet's derivative list).
    - Leaving the denominators in when solving $=0$ and then messing up the algebra. The sheet says: **multiply by the denominators first**.
    - Writing only the final formula on a "derive" question. The sheet's 3 steps are the 3 things the grader pays for.
    - Sigmoid questions: differentiate in $\lambda$, not in $\theta$ (sheet's Sigmoid trick), and write the $x>\frac74$-style range at the end.
    - $\theta^2$ in the pdf (Nov19) → $-2\ln\theta$, not $-2\theta$ (sheet: "$\theta^k$ below the line → $-k\ln\theta$").
