# 2.2 MAP with a prior

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>1–1.5 points (often twice per paper)</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [2.1 MLE](e2-mle.md) first.

## What the exam asks

Either **(a)** "data model + a prior on $\theta$: write the likelihood, derive the posterior, compute the MAP (and compare with the MLE)", or **(b)** "here is the posterior $p(\theta\mid x)$, derive the MAP". June 2026 had two of these, worth 2 points together.

## The idea in one minute

The MLE only listens to the data. The **MAP** also listens to what you believed **before** the data, the **prior** $p(\theta)$. Bayes' rule mixes them:

$$\underbrace{p(\theta\mid x)}_{\text{posterior}}\ \propto\ \underbrace{p(x\mid\theta)}_{\text{likelihood}}\times\underbrace{p(\theta)}_{\text{prior}}$$

($\propto$ = "proportional to": we drop every factor without $\theta$, it does not move the top.) The **MAP** is the top of the posterior. With the usual exam priors (Beta, Gamma) the multiplication is trivial: **exponents add**. Change the prior and the amount of data:

<div class="widget" data-w="posterior"></div>

Notice: with little data the MAP sits between the prior and the MLE; press **×4 data** and it walks onto the MLE.

## The recipe

!!! recipe key "MAP in 4 steps"
    1. **Likelihood**: multiply the PMFs/PDFs of all samples and keep only the $\theta$ parts. You get something like $\theta^{(\text{number})}(1-\theta)^{(\text{number})}$ or $\lambda^{\sum x}e^{-n\lambda}$.
    2. **Times the prior** (again only the $\theta$ parts). Same base → **add the exponents**.
    3. **Name the posterior**: $\theta^{a-1}(1-\theta)^{b-1}$ is Beta$(a,b)$; $\lambda^{a-1}e^{-b\lambda}$ is Gamma$(a,b)$. (Read off $a$ by adding 1 to the exponent.)
    4. **MAP = the top** (mode): Beta: $\dfrac{a-1}{a+b-2}$. Gamma: $\dfrac{a-1}{b}$. If you forget these: take $\ln$, differentiate, set to 0, exactly like the MLE.

??? idea "Where the Beta top comes from"
    $\ln[\theta^{A}(1-\theta)^{B}]=A\ln\theta+B\ln(1-\theta)$. Derivative: $\frac A\theta-\frac B{1-\theta}=0$ → $A(1-\theta)=B\theta$ → $\theta=\frac{A}{A+B}$. With $A=a-1$, $B=b-1$: $\frac{a-1}{a+b-2}$.
    Gamma: $\ln[\lambda^{A}e^{-b\lambda}]=A\ln\lambda-b\lambda$ → $\frac A\lambda-b=0$ → $\lambda=\frac Ab=\frac{a-1}{b}$.

## Watch it once: June 2026 · 2d (Poisson + Gamma)

!!! exam "Resit, June 2026 · 2d"
    Daily pollution spike counts $X_i \sim \text{Poisson}(\lambda)$; observed $x = \{2, 4, 3, 5, 2, 4\}$. Gamma prior $p(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}$ with $\alpha = 3$, $\beta = 2$.

    Write the likelihood, derive the posterior, find the MAP, compare it with the MLE and explain the effect of the prior.

<div class="stepper" markdown>

**Step 1 · Likelihood.** Poisson: $P(x\mid\lambda)=\dfrac{\lambda^{x}e^{-\lambda}}{x!}$. Six days, multiply:
$L(\lambda)=\prod_i\dfrac{\lambda^{x_i}e^{-\lambda}}{x_i!}\propto\lambda^{\sum x_i}e^{-6\lambda}=\lambda^{20}e^{-6\lambda}$ (since $2+4+3+5+2+4=20$).

***

**Step 2 · Times the prior.** $\lambda^{3-1}e^{-2\lambda}=\lambda^2e^{-2\lambda}$. Add exponents:
$p(\lambda\mid x)\propto\lambda^{20+2}e^{-(6+2)\lambda}=\lambda^{22}e^{-8\lambda}$.

***

**Step 3 · Name it.** $\lambda^{a-1}e^{-b\lambda}$ with $a-1=22$, $b=8$: **Gamma(23, 8)**.

***

**Step 4 · MAP and MLE.** MAP $=\dfrac{a-1}{b}=\dfrac{22}{8}=\mathbf{2.75}$. MLE (data only) $=\dfrac{\sum x_i}{n}=\dfrac{20}{6}=3.33$.
The prior has mean $\alpha/\beta=1.5$, so it **pulls the estimate down** from 3.33 to 2.75. With more days of data the prior counts less and MAP → MLE.

</div>

## Your turn

!!! exam "Resit, June 2026 · 2c"
    Patients are screened until $k = 2$ eligible ones are found; $X_i \sim \text{NegBin}(k, \theta)$ with PMF $P(X = x \mid \theta) = \binom{x-1}{k-1} \theta^k (1-\theta)^{x-k}$. Observed $x = \{3, 5, 4, 6, 4\}$. Prior $\theta \sim \text{Beta}(\alpha = 2, \beta = 3)$, i.e. $p(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$.

    Write the likelihood, derive the posterior, compute the MAP.

??? solution "Check your answer"
    **What is being asked?** Likelihood × prior → posterior → its top (the MAP).

    **Step 1 · One sample.** $P(X=x\mid\theta)=\binom{x-1}{k-1}\theta^{k}(1-\theta)^{x-k}$ with $k=2$: $\binom{x-1}{1}\theta^{2}(1-\theta)^{x-2}$. The binomial coefficient $\binom{x-1}{1}=x-1$ is just a number with **no $\theta$**, so it disappears (we only keep the $\theta$ parts).

    **Step 2 · Five samples, exponents add.** Multiply the five likelihoods: $\theta$ gets exponent $2\times5=10$, and $(1-\theta)$ gets $\sum_i(x_i-2)=\sum x_i-2\cdot5=22-10=12$. So $L\propto\theta^{10}(1-\theta)^{12}$.

    **Step 3 · Times the prior.** Beta(2, 3): $p(\theta)\propto\theta^{2-1}(1-\theta)^{3-1}=\theta^{1}(1-\theta)^{2}$. Add the exponents (same base):

    $$p(\theta\mid x)\propto\theta^{10+1}(1-\theta)^{12+2}=\theta^{11}(1-\theta)^{14}.$$

    **Step 4 · Name it.** $\theta^{a-1}(1-\theta)^{b-1}$ with $a-1=11$, $b-1=14$: **Beta(12, 15)**.

    **Step 5 · Top of the posterior.** Beta top $=\dfrac{a-1}{a+b-2}=\dfrac{11}{11+14}=\dfrac{11}{25}=0.44$.

    !!! answer "Answer"
        Posterior Beta(12, 15); $\hat\theta_{MAP}=\frac{12-1}{12+15-2}=\frac{11}{25}=0.44$. (This is exactly the widget's starting position.)

!!! exam "Final exam, 13 April 2025 · 2d · 1 p"
    A binary experiment is repeated $N$ times; $N_1$ = number of Ys, $N_0$ = number of Ns, $\theta$ = probability of a Y. The posterior is $p(\theta | \mathcal{D}) = \theta^{\beta_1 - 1 + k_1 N_1} (1 - \theta)^{\beta_0 - 1 + k_0 N_0}$. Derive the MAP estimate of $\theta$.

??? solution "Check your answer"
    **What is being asked?** The posterior is already given: find the $\theta$ on its top.

    **Step 1 · Name the exponents.** $p(\theta\mid\mathcal D)=\theta^{A}(1-\theta)^{B}$ with $A=\beta_1-1+k_1N_1$ and $B=\beta_0-1+k_0N_0$. ($N_1$ Ys each contribute one $\theta$, $N_0$ Ns each one $(1-\theta)$.)

    **Step 2 · Log.** $\ln p=A\ln\theta+B\ln(1-\theta)$.

    **Step 3 · Differentiate.** $\frac{A}{\theta}-\frac{B}{1-\theta}=0$ (using $\frac{d}{d\theta}\ln\theta=\frac1\theta$ and $\frac{d}{d\theta}\ln(1-\theta)=-\frac1{1-\theta}$).

    **Step 4 · Solve.** $A(1-\theta)=B\theta$ → $A=(A+B)\theta$ → $\theta=\dfrac{A}{A+B}$. Fill $A$ and $B$ back in.

    !!! answer "Answer"
        $\hat\theta_{MAP}=\dfrac{\beta_1-1+k_1N_1}{\beta_1+\beta_0-2+k_1N_1+k_0N_0}$

!!! exam "Final exam, April 2024 · 2d · 1.5 p"
    Posterior $p(\theta | x) = \frac{\lambda(\theta)}{2} e^{-\frac{\lambda(\theta)}{2}x}, \ x > 1$, with $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$. Derive the MAP for $\theta$. Hint: $\frac{\partial \lambda}{\partial \theta} = \lambda(1 - \lambda)$.

??? solution "Check your answer"
    **What is being asked?** The posterior is given with the parameter hidden inside $\lambda(\theta)=\frac{1}{1+e^{-\theta}}$. Same structure as the sigmoid MLE in [2.1](e2-mle.md#your-turn).

    **Step 1 · Best $\lambda$ first.** $\theta$ only appears through $\lambda$, and $\lambda(\theta)$ is one-to-one, so maximise in $\lambda$ and convert at the end.

    **Step 2 · Log.** $\ln p=\ln\!\big(\tfrac{\lambda}{2}e^{-\frac{\lambda x}{2}}\big)=\ln\lambda-\ln2-\dfrac{x}{2}\lambda$.

    **Step 3 · Differentiate.** $\dfrac1\lambda-\dfrac x2=0$ → $\hat\lambda=\dfrac2x$.

    **Step 4 · Back to $\theta$.** $\dfrac{1}{1+e^{-\theta}}=\dfrac2x$ → $1+e^{-\theta}=\dfrac x2$ → $e^{-\theta}=\dfrac x2-1$ → $\theta=-\ln\!\big(\dfrac x2-1\big)$. The $\ln$ needs $\frac x2-1>0$, i.e. $x>2$.

    !!! answer "Answer"
        $\hat\theta_{MAP}=-\ln\!\left(\dfrac x2-1\right)=\ln\dfrac{2}{x-2}$, for $x>2$.

## Traps

!!! trap key "Where points are lost"
    - Naming the family: exponent $11$ means Beta parameter $12$ (add 1). Then the top is $\frac{a-1}{a+b-2}$, which uses the exponents again.
    - Gamma: the exam writes $e^{-\beta\lambda}$ (a **rate**). Top $=\frac{a-1}{b}$, not $(a-1)b$.
    - "Compare with the MLE": always say **which way** the prior pulls and that its effect **fades** as $n$ grows.
