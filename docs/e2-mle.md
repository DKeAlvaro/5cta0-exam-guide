# 2.1 Maximum likelihood (MLE)

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>1 point</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## How to fight this section with the sheet

The exam says **"derive the MLE"** → you open **box 2A** on your A4 sheet and do its 3 steps with the pdf they gave you. That is the whole method. Every question below is the same box with a different pdf, so read one solution with the sheet in your hand and the rest are copies.

!!! sheet "Box 2A, exactly as it is printed on the sheet"
    **IF YOU SEE** a pdf $p(x\mid\theta)$, samples $x_1..x_N$, "maximum likelihood", "derive the MLE"

    1. Take $\ln$ of ONE sample's pdf, then put $\sum_n$ in front. That is $\ln L$. A term without $x_n$ gets multiplied by $N$.
    2. Differentiate with respect to $\theta$ (terms without $\theta$ disappear).
    3. Set it $=0$ and solve for $\theta$. That is $\hat\theta$.

    **How to take $\ln$ of a pdf:** a factor on top → $+\ln(\text{it})$; a factor on the bottom → $-\ln(\text{it})$; $\theta^k$ on the bottom → $-k\ln\theta$; $e^{\text{stuff}}$ → just "stuff" (the $e$ disappears).

    **Derivatives:** $\ln\theta\to\frac1\theta$ · $\frac1\theta\to-\frac1{\theta^2}$ · $\theta^k\to k\theta^{k-1}$ · $e^{c\theta}\to ce^{c\theta}$.

    **Solving $=0$:** multiply the equation by the denominators ($\theta^2$, $\theta$, …) first — that does not change the root.

    **Sigmoid trick** (bottom of box 2A): IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.

Two more sheet places you will need: the **Calculations** strip (bottom of the sheet) for the $\ln$/$e$ and fraction algebra, and **box 2D** for the true/false questions. Each exercise below tells you which one.

## 1 · April 2024 · 2c — the classic. Read this one with the sheet next to you

!!! exam "Final exam, April 2024 · 2c · 1 p"
    For the data vector $\mathbf{x} = \{x_1, \dots, x_N\}$ consisting of independent samples with probability density function

    $$p(x_n | \theta) = \frac{x_n}{2\theta} e^{-\frac{x_n^2}{2\theta}},$$

    derive the MLE for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A, steps 1–3"
    **Sheet step 1** · "Take $\ln$ of ONE sample's pdf, then put $\sum_n$ in front."
    One sample is $\frac{x_n}{2\theta}e^{-x_n^2/2\theta}$. Take it apart with the sheet's ln rules: $x_n$ on top → $+\ln x_n$; $2\theta$ on the bottom → $-\ln(2\theta)=-\ln 2-\ln\theta$ (rule: $\ln\frac ab=\ln a-\ln b$, in the Calculations strip); $e^{\text{stuff}}$ → just "stuff" $=-\frac{x_n^2}{2\theta}$:

    $$\ln p(x_n\mid\theta)=\ln x_n-\ln 2-\ln\theta-\frac{x_n^2}{2\theta}$$

    Now put $\sum_n$ in front. The sheet says "a term without $x_n$ gets multiplied by $N$" → the two constants $\ln 2$ and $\ln\theta$ come out as $N\ln 2$ and $N\ln\theta$:

    $$\ln L=\sum_n\ln x_n-N\ln 2-N\ln\theta-\frac{1}{2\theta}\sum_n x_n^2$$

    **Sheet step 2** · "Differentiate (terms without $\theta$ disappear)."
    $\sum\ln x_n$ and $-N\ln2$ have no $\theta$ → gone. Then the sheet's derivative rules: $\ln\theta\to\frac1\theta$ and $\frac1\theta\to-\frac1{\theta^2}$ (and minus times minus is plus):

    $$\frac{d}{d\theta}\ln L=-\frac N\theta+\frac{1}{2\theta^2}\sum_n x_n^2$$

    **Sheet step 3** · "Set it $=0$ and solve. Multiply by the denominators first."
    Multiply the whole equation by $\theta^2$:

    $$-N\theta+\frac12\sum_n x_n^2=0\quad\Longrightarrow\quad \hat\theta=\frac{1}{2N}\sum_n x_n^2$$

    **Sheet check:** the example line at the bottom of box 2A (*Apr24* … $\hat\theta=\frac1{2N}\sum x_n^2$) is this exact question, and it gives the same. If your line looks like the sheet's line, you have the points.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{2N}\sum_{n=1}^N x_n^2$

## 2 · Q1 2023 resit · 2b — same pdf, the 2 disappeared

!!! exam "Q1 2023 resit · 2b"
    For the data vector $\mathbf{x} = \{x_1, \dots x_N\}$ consisting of independent samples with probability density function

    $$p(\mathbf{x} | \theta) = \prod_{n=1}^N \frac{x_n}{\theta} e^{-\frac{x_n^2}{\theta}},$$

    derive the MLE for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A again — this is exercise 1 without the 2"
    The $\prod$ in front is just the exam writing the likelihood for you: one sample is $\frac{x_n}{\theta}e^{-x_n^2/\theta}$. Same three steps:

    **Step 1.** $\ln$ of one sample: $\ln x_n-\ln\theta-\frac{x_n^2}{\theta}$. With $\sum_n$: $\ln L=\sum\ln x_n-N\ln\theta-\frac1\theta\sum x_n^2$ (the sheet: terms without $x_n$ get $\times N$).

    **Step 2.** $\frac{d}{d\theta}\ln L=-\frac N\theta+\frac{1}{\theta^2}\sum x_n^2$ (sheet rules $\ln\theta\to\frac1\theta$, $\frac1\theta\to-\frac1{\theta^2}$).

    **Step 3.** $=0$, multiply by $\theta^2$: $-N\theta+\sum x_n^2=0$.

    **Sheet check:** compare with exercise 1. The only change is the missing 2 → the answer lost its 2.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{N}\sum_{n=1}^N x_n^2$

## 3 · Practice exam 2021 · 2b — the number in front never matters

!!! exam "Practice exam, October 2021 · 2b"
    For the data vector $\mathbf{x}$ consisting of independent samples with probability density function $p(x[n]) = \frac{x}{\theta} \exp\left(-\frac{x^2}{2\theta}\right)$, where $n = 0, 1, \dots, N-1$, find an estimator for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A — and the rule that saves you here"
    "Find an estimator" with a pdf and samples = derive the MLE = box 2A. One sample: $\frac{x_n}{\theta}e^{-x_n^2/2\theta}$.

    **Step 1.** $\ln x_n-\ln\theta-\frac{x_n^2}{2\theta}$ → $\ln L=\sum\ln x_n-N\ln\theta-\frac{1}{2\theta}\sum x_n^2$.

    **Step 2.** $-\frac N\theta+\frac{1}{2\theta^2}\sum x_n^2$.

    **Step 3.** $=0$, multiply by $\theta^2$: $-N\theta+\frac12\sum x_n^2=0$.

    **Sheet check:** this is exercise 1 again (the $\frac12$ sits in the exponent in both). Numbers in front that do not contain $\theta$ never change the answer — the sheet's ln rules turn them into constants that vanish in step 2.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{1}{2N}\sum_{n=0}^{N-1} x^2[n]$

## 4 · November 2019 · 3a — $\theta^2$, so $-2\ln\theta$

!!! exam "Written exam, November 2019 · 3a"
    The data $x[0], x[1], \dots, x[N-1]$ are observed, where $x[n]$'s are independent and identically distributed according to the PDF

    $$p(x; \theta) = \frac{x}{\theta^2} \exp \left[ -\frac{x^2}{2\theta^2} \right], \quad x \geq 0.$$

    (a) Find the maximum likelihood estimator for the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2A, the $\theta^k$ rule does the work"
    **Step 1.** The sheet: "$\theta^k$ on the bottom → $-k\ln\theta$", here $k=2$ → $-2\ln\theta$. So $\ln x_n-2\ln\theta-\frac{x_n^2}{2\theta^2}$, and

    $$\ln L=\sum\ln x_n-2N\ln\theta-\frac{1}{2\theta^2}\sum x_n^2$$

    **Step 2.** Sheet derivatives: $\ln\theta\to\frac1\theta$ (so $-2N\ln\theta\to-\frac{2N}{\theta}$) and $\frac{1}{\theta^2}\to-\frac{2}{\theta^3}$ (the $\theta^k$ rule backwards), so $-\frac{1}{2\theta^2}\sum x_n^2\to+\frac{1}{\theta^3}\sum x_n^2$:

    $$-\frac{2N}{\theta}+\frac{1}{\theta^3}\sum x_n^2=0$$

    **Step 3.** Multiply by $\theta^3$ (the sheet: clear the denominators first): $-2N\theta^2+\sum x_n^2=0$ → $\theta^2=\frac{\sum x_n^2}{2N}$. The sheet's "get the letter alone" rule ($x^k=a\Rightarrow x=a^{1/k}$, Calculations strip) gives the square root. $\theta>0$ so take the $+$ root.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\sqrt{\frac{1}{2N}\sum_{n=0}^{N-1} x^2[n]}$

## 5 · January 2019 retake · 2a — exponential, the easiest one

!!! exam "Retake, January 2019 · 2a"
    For the random variable $x$ with distribution

    $$p(x; \lambda) = \lambda e^{-\lambda x}$$

    find the maximum likelihood estimator for $\lambda$, given $N$ independent identically distributed observations $x_i, i \in \{0 : N - 1\}$.

!!! sheet "In the cheat sheet: box 2A (the unknown is called $\lambda$ — same box)"
    **Step 1.** $\ln$ of one sample: $\lambda$ on top → $+\ln\lambda$; $e^{-\lambda x}$ → just $-\lambda x$. So $\ln L=N\ln\lambda-\lambda\sum x_i$ (the sheet: $\sum_n\lambda x_n=\lambda\sum x_n$).

    **Step 2.** $\frac N\lambda-\sum x_i$.

    **Step 3.** $=0$, multiply by $\lambda$: $N-\lambda\sum x_i=0$.

    **Sheet check:** this pdf also appears in box 2B ("one observation: exponential → $\lambda e^{-\lambda x}$") — there it is a prior/likelihood ingredient; here it is the whole question. Same shape, box 2A still applies.

!!! answer "Answer"
    $\displaystyle\hat\lambda_{ML}=\frac{N}{\sum_i x_i}=\frac{1}{\bar x}$

## 6 · June 2026 resit · 2b — Gamma, and "what does it tell us"

!!! exam "Resit, June 2026 · 2b · 1 p"
    Recovery times $X\sim\text{Gamma}(k,\theta)$, $k$ known, $\theta>0$ unknown, with pdf $p(x \mid \theta) = x^{k-1} e^{-x/\theta} / (\theta^k \Gamma(k))$, $x > 0$. Write the likelihood and log-likelihood for $x_1, \dots, x_n$, derive the MLE of $\theta$, and explain what it tells us.

!!! sheet "In the cheat sheet: box 2A, its own *Jun26* example line"
    **Step 1.** The sheet's ln rules piece by piece: $x^{k-1}$ on top → $+(k-1)\ln x$; $e^{-x/\theta}$ → $-\frac x\theta$; $\theta^k$ on the bottom → $-k\ln\theta$; $\Gamma(k)$ on the bottom → $-\ln\Gamma(k)$ (a constant). Sum over $n$ samples:

    $$\ln L=(k-1)\sum\ln x_i-\frac1\theta\sum x_i-nk\ln\theta-n\ln\Gamma(k)$$

    **Step 2.** Only two terms have $\theta$: $\frac{d}{d\theta}\big(-\frac1\theta\sum x_i\big)=+\frac{1}{\theta^2}\sum x_i$ and $\frac{d}{d\theta}(-nk\ln\theta)=-\frac{nk}{\theta}$.

    **Step 3.** $=0$, multiply by $\theta^2$: $\sum x_i-nk\theta=0$ → $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}{k}$.

    **Meaning** (the sheet's *Jun26* line says it in one sentence): a Gamma variable has mean $k\theta$, so $\hat\theta$ = average recovery time per stage, and $k\hat\theta$ = the observed mean time.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\frac{\sum x_i}{nk}=\frac{\bar x}{k}$ — average recovery time divided by the number of stages $k$

## 7 · April 2025 · 2c — sigmoid, use the trick at the bottom of box 2A

!!! exam "Final exam, 13 April 2025 · 2c · 1 p"
    Consider the likelihood $p(x|\theta) = 3\lambda(\theta)e^{-4\frac{\lambda(\theta)x}{7}}, \ x > 1$, where $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$ (logistic sigmoid). Derive the MLE for $\theta$. Hint: $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

!!! sheet "In the cheat sheet: box 2A · Sigmoid trick"
    The sheet says: **IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.** Do exactly that — ignore the $\theta$ until the last line.

    **Step 1 with $\lambda$.** $\ln$ of $3\lambda e^{-4\lambda x/7}$: $\ln 3+\ln\lambda-\frac{4x}{7}\lambda$ (the sheet: $e^{\text{stuff}}$ → just "stuff").

    **Step 2 with $\lambda$.** $\frac{d}{d\lambda}\ln\lambda=\frac1\lambda$, and $\frac{d}{d\lambda}\big(-\frac{4x}7\lambda\big)=-\frac47x$ (a constant times $\lambda$).

    **Step 3.** $\frac1\lambda-\frac{4x}7=0$, multiply by $\lambda$: $1-\frac{4x}7\lambda=0$ → $\hat\lambda=\frac{7}{4x}$.

    **Now the sheet's conversion formula.** $\hat\theta=-\ln\!\big(\frac{1}{\hat\lambda}-1\big)=-\ln\!\big(\frac{4x}{7}-1\big)$.

    **Range check** (the Calculations strip: "$\ln$ of a positive number"): $\frac{4x}7-1>0$ → $x>\frac74$.

    (If you differentiate in $\theta$ with the hint, the extra factor $\lambda(1-\lambda)$ is never 0, so you land on the same answer — the sheet's trick just avoids that mess.)

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=-\ln\!\left(\frac{4x}{7}-1\right)$, valid for $x>\frac74$

## 8 · January 2025 resit · 2b — one observation, and the letters are the data

!!! exam "Resit, January 2025 · 2b"
    Assume that

    $$p(\mu, \sigma, \theta | \rho) = \frac{1}{2\pi(1-\theta^2)^{1/2}} \exp\left(-\frac{\mu^2\rho^2 - 2\rho\mu\sigma\theta + \sigma^2\rho^2}{2(1-\theta^2)}\right)$$

    Determine the maximum likelihood estimate of $\rho$ for a single observation of $\mu, \sigma, \theta$.

    (*Note: $\rho$ is the unknown parameter; $\mu, \sigma, \theta$ are the observed data.*)

!!! sheet "In the cheat sheet: box 2A — the unknown is $\rho$, everything else is a number"
    This one looks scary because of the letters. Follow the sheet literally: the unknown is $\rho$, so in step 2 every term without $\rho$ disappears — $\mu,\sigma,\theta$ are just data, treat them as numbers.

    **Step 1.** $\ln$ of the pdf: the front factor has no $\rho$ → a constant. The exponent comes down as it is:

    $$\ln p=\text{const}-\frac{\mu^2\rho^2-2\rho\mu\sigma\theta+\sigma^2\rho^2}{2(1-\theta^2)}$$

    **Step 2.** Differentiate in $\rho$ (the denominator $2(1-\theta^2)$ is a number and stays put; only the top changes):

    $$\frac{d}{d\rho}\ln p=-\frac{2\mu^2\rho-2\mu\sigma\theta+2\sigma^2\rho}{2(1-\theta^2)}$$

    **Step 3.** $=0$, multiply by $2(1-\theta^2)$ (the sheet: clear the denominators first): $2\rho(\mu^2+\sigma^2)-2\mu\sigma\theta=0$.

!!! answer "Answer"
    $\displaystyle\hat\rho_{ML}=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}$

## 9 · November 2022 · 2d — the sheet gives you the answer outright

!!! exam "Final exam, November 2022 · 2d · 1 p"
    Consider the observation

    $$\mathbf{x} = A \begin{bmatrix} \cos(\theta) \\ \sin(\theta) \end{bmatrix} + \mathbf{w},$$

    where $\mathbf{w}$ is white Gaussian noise with variance $\sigma^2$. The pdf of the observation is

    $$p(\mathbf{x}; \theta) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{1}{2\sigma^2} \left((x_1 - A \cos(\theta))^2 + (x_2 - A \sin(\theta))^2\right)\right)$$

    Find the maximum likelihood estimator of the parameter $\theta$.

!!! sheet "In the cheat sheet: box 2D, last line"
    The sheet prints this exact model: *"Fisher info for $x$ = signal($\theta$) + Gaussian noise: … Nov22 $A[\cos\theta,\sin\theta]$ → $\mathcal I=\frac{A^2}{\sigma^2}$, and MLE $\hat\theta=\arctan\frac{x_2}{x_1}$."* So the answer is already on your sheet.

    **If you want to see it with box 2A anyway:** $\ln p=\text{const}-\frac{1}{2\sigma^2}\big((x_1-A\cos\theta)^2+(x_2-A\sin\theta)^2\big)$. Maximising $\ln p$ = minimising that square. Expand it (the Calculations strip has the rules; here it is just $(a-b)^2$): $x_1^2+x_2^2+A^2-2A(x_1\cos\theta+x_2\sin\theta)$. The only $\theta$ part is $-2A(x_1\cos\theta+x_2\sin\theta)$, so you must **maximise** $x_1\cos\theta+x_2\sin\theta$. That happens when the direction $[\cos\theta,\sin\theta]$ points the same way as the data $(x_1,x_2)$: $\cos\theta=\frac{x_1}{\sqrt{x_1^2+x_2^2}}$, $\sin\theta=\frac{x_2}{\sqrt{x_1^2+x_2^2}}$ → $\tan\theta=\frac{x_2}{x_1}$.

!!! answer "Answer"
    $\displaystyle\hat\theta_{ML}=\arctan\frac{x_2}{x_1}$ (the sheet's line, verbatim)

## 10 · November 2022 · 2b — true/false, read the row

!!! exam "Final exam, November 2022 · 2b · 0.5 p"
    Which of the following statements about the maximum likelihood estimator is TRUE?

    - (a) The maximum likelihood estimator always achieves the Cramér-Rao lower bound.
    - (b) The maximum likelihood estimator can only be found for special estimation problems, such as linear signal models.
    - (c) The maximum likelihood estimator is asymptotically unbiased.

!!! sheet "In the cheat sheet: box 2D, three rows"
    - *"MLE always reaches the CRLB / only for linear models"* → **F**. That one row kills **(a)** and **(b)** in a single look (this is what the sheet means: one row covers both distractors).
    - *"MLE is asymptotically unbiased"* → **T (Nov22 c)**. The sheet even tags the row with this exam.

!!! answer "Answer"
    **(c)**

## 11 · January 2022 resit · 2b — true/false, the invariance row

!!! exam "Resit, January 2022 · 2b · 0.5 p"
    Which of the following statements about the maximum likelihood estimator is true?

    - (a) The maximum likelihood estimate is the value of $x$ that maximizes the likelihood function.
    - (b) For large sample sizes, the maximum likelihood estimate is uniformly distributed, i.e., $\hat{\theta}_{ML} \sim \text{Uniform}(-a, a)$ where $a = \mathcal{I}^{-1}(\theta)$.
    - (c) For a transformed parameter $\alpha = \psi(\theta)$, where $\psi(\cdot)$ is a one-to-one mapping, the maximum likelihood estimate $\hat{\theta}_{ML}$ can be obtained as $\hat{\theta}_{ML} = \psi^{-1}(\hat{\alpha}_{ML})$.

!!! sheet "In the cheat sheet: box 2D"
    - *"MLE maximises the likelihood over $\theta$"* → **T ("over $x$": F)**. **(a)** says "the value of $x$" → **F**. This row is written exactly for this distractor.
    - *"MLE of $\alpha=\psi(\theta)$: $\hat\theta=\psi^{-1}(\hat\alpha)$"* → **T (Jan22 c)**. That is **(c)** word for word.
    - **(b)** is not on the sheet as a row, but the sheet says the MLE is asymptotically unbiased and its variance sits at $\frac1{\mathcal I}$ — a uniform distribution is not that. And "one-to-one" is the same condition as the sigmoid trick in box 2A.

!!! answer "Answer"
    **(c)**

## 12 · January 2019 retake · 1b — which box is which

!!! exam "Retake, January 2019 · 1b"
    Which expression describes the maximum likelihood estimator?

    - A. $\hat{\theta} = \arg \min_{\theta} \sum_{n=1}^N (x[n] - s[n; \theta])^2$
    - B. $\hat{\theta} = \arg \min_{\hat{\theta}} \int (\hat{\theta} - \theta)^2 p(x|\theta) dx$
    - C. $\hat{\theta} = \arg \max_{\theta} p(\theta|x)$
    - D. $\hat{\theta} = \arg \max_{\theta} p(x|\theta)$

!!! sheet "In the cheat sheet: it is a 'which box' question"
    Match each option to a box of the sheet:

    - **A** = minimise a squared error over data points → **box 2C** (least squares).
    - **B** = minimise a squared error averaged over the pdf → **MMSE**, box 2B's table ("MMSE = the mean of the posterior; minimises squared error").
    - **C** = maximise $p(\theta\mid x)$ = the posterior → **MAP**, box 2B ("MAP needs a prior").
    - **D** = maximise $p(x\mid\theta)$ = the likelihood over $\theta$ → **box 2A**. The sheet's row says it: *"MLE maximises the likelihood over $\theta$"*. The likelihood is $p(\text{data}\mid\theta)=p(x\mid\theta)$.

!!! answer "Answer"
    **D**

## Why this works (read once)

$\theta$ is a knob on the model. For each knob position, the model says how likely your data were: the product of the pdf heights at the data points. The **MLE** is the knob position that makes the data you actually saw most likely. The top of that curve is where its slope is zero — that is why the sheet says *differentiate and set to 0*. We take the $\ln$ first because it turns the product into a sum (easy to differentiate) and does not move the top.

<div class="widget" data-w="likelihood"></div>

## Traps

!!! trap "Where points are lost (each one is a line of the sheet you skipped)"
    - Forgetting the $-N\ln\theta$ that comes from the $\frac1\theta$ in front (sheet: "a factor on the bottom → $-\ln(\text{it})$"). It is half of the answer.
    - Wrong sign on $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$ — minus times minus gives a **plus** in the derivative (sheet's derivative list).
    - Leaving the denominators in when solving $=0$ and then messing up the algebra. The sheet says: **multiply by the denominators first**.
    - Writing only the final formula on a "derive" question. The sheet's 3 steps are the 3 things the grader pays for.
    - Sigmoid questions: differentiate in $\lambda$, not in $\theta$ (sheet's Sigmoid trick), and write the $x>\frac74$-style range at the end.
    - $\theta^2$ in the pdf (Nov19) → $-2\ln\theta$, not $-2\theta$ (sheet: "$\theta^k$ on the bottom → $-k\ln\theta$").
