# 2.2 MAP with a prior

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>1–1.5 points (often twice per paper)</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [2.1 MLE](e2-mle.md) first: the MAP borrows its $\ln$ and derivative rules from box 2A.

## The idea in one minute

The MLE only listens to the data. The **MAP** also listens to what you believed **before** the data, the **prior** $p(\theta)$. Bayes' rule mixes them:

$$\underbrace{p(\theta\mid x)}_{\text{posterior}}\ \propto\ \underbrace{p(x\mid\theta)}_{\text{likelihood}}\times\underbrace{p(\theta)}_{\text{prior}}$$

($\propto$ = "proportional to": we drop every factor without $\theta$, it does not move the top.) The **MAP** is the top of the posterior. The **MMSE** is the *mean* of the posterior — a different number, and box 2D has a true/false row written exactly to catch people who mix them up.

With the usual exam priors (Beta, Gamma) the multiplication is trivial: **exponents add**. Change the prior and the amount of data:

<div class="widget" data-w="posterior"></div>

Notice: with little data the MAP sits between the prior and the MLE; press **×4 data** and it walks onto the MLE.

## How to fight this section with the sheet

The exam says **"prior", "posterior", "MAP", "maximum a posteriori", "MMSE"** → you open **box 2B** on your A4 sheet and do its 3 steps with the probabilities they gave you. That is the whole method. Every question below is the same box with a different prior, so read one solution with the sheet in your hand and the rest are copies.

Each step below names **the sheet's term it uses**, term by term: which pieces of the probability you keep, which you throw away, which table row you read at the end. Press **Next step** to go one at a time — cover the step, do it yourself, then reveal it.

!!! sheet "Box 2B, exactly as it is printed on the sheet"
    **IF YOU SEE** "prior", "posterior", "MAP", "maximum a posteriori"/"a-posteriori", "MMSE"/"minimum mean square error", "Bayesian estimator", Beta, Gamma

    1. **Likelihood**: write each observation's probability, keep only the parts with $\theta$, multiply them all (exponents add).
    2. **Multiply by the prior** (exponents add again). Drop numbers without $\theta$.
    3. **Read the shape and use the table**:

    | Result looks like | Posterior | MAP | MMSE (mean) |
    |---|---|---|---|
    | $\theta^{A}(1-\theta)^{B}$ | Beta$(A{+}1,B{+}1)$ | $\frac{A}{A+B}$ | $\frac{A+1}{A+B+2}$ |
    | $\lambda^{A}e^{-B\lambda}$ | Gamma$(A{+}1,B)$ | $\frac{A}{B}$ | $\frac{A+1}{B}$ |

    Prior Beta$(a,b)$ = $\theta^{a-1}(1-\theta)^{b-1}$. Prior Gamma$(a,b)$ = $\lambda^{a-1}e^{-b\lambda}$.

    One observation $x$ gives: Poisson count → $\lambda^{x}e^{-\lambda}$ · "$k$-th success on trial $x$" → $\theta^k(1-\theta)^{x-k}$ · "$k$ successes in $n$ tries" → $\theta^k(1-\theta)^{n-k}$ · exponential → $\lambda e^{-\lambda x}$.

What each line of the box means, word by word:

| the sheet says | what you actually do |
|---|---|
| "write each observation's probability" | copy the PMF/PDF the exam gives you for **one** day, patient or trial |
| "keep only the parts with $\theta$" | $\binom{x-1}{k-1}$, $x!$, $\Gamma(k)$, $\frac1x$, $\frac12$ … anything without the unknown → throw it away |
| "multiply them all (exponents add)" | $\theta^2\cdot\theta^2\cdot\theta^2\cdot\theta^2\cdot\theta^2=\theta^{10}$; $e^{-\lambda}\!\cdot\! e^{-\lambda}\!\cdot\! e^{-\lambda}\!\cdot\! e^{-\lambda}\!\cdot\! e^{-\lambda}\!\cdot\! e^{-\lambda}=e^{-6\lambda}$ |
| "Multiply by the prior (exponents add again)" | prior $\theta^{a-1}(1-\theta)^{b-1}$ puts $a-1$ on top of the $\theta$ exponent and $b-1$ on top of the $(1-\theta)$ exponent |
| "Read the shape and use the table" | the two exponents you just wrote **are** the table's $A$ and $B$ — nothing else |
| "MAP" | the **top** (highest point) of the posterior |
| "MMSE (mean)" | the **average** of the posterior — a different number (box 2D has a row about exactly this) |

Two more sheet places you will need. **Box 2A** ([2.1](e2-mle.md)) does the algebra whenever the posterior is *not* a Beta or a Gamma: take $\ln$, differentiate, set $=0$. **Box 2D** answers the "which statement is true" questions about MAP and MMSE. The **Calculations** strip (bottom of the sheet) covers the integrals when they ask for the MMSE and the posterior is not a standard shape.

## 1 · June 2026 · 2d — Poisson + Gamma. Read this one with the sheet next to you

!!! exam "Resit, June 2026 · 2d"
    An environmental scientist monitors the number of pollution spikes recorded per day at an air quality monitoring station on the outskirts of a city. The daily spike count is modelled as $X_i \sim \text{Poisson}(\lambda)$, where $\lambda > 0$ is the unknown average number of pollution spikes per day. The observed counts over six days are $x = \{2, 4, 3, 5, 2, 4\}$. Assume a Gamma prior on $\lambda$ with pdf $p(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}$, $\lambda > 0$, $\alpha = 3$, $\beta = 2$.

    - Write the likelihood function for $\lambda$.
    - Derive the posterior distribution for $\lambda$.
    - Find the MAP estimate for $\lambda$.
    - Compare the MAP estimate with the MLE and explain the effect of the prior.

!!! sheet "In the cheat sheet: box 2B, every line used"
    <div class="stepper" markdown>

    **Sheet step 1 · "write each observation's probability"** (the sheet's one-observation list: *"Poisson count → $\lambda^{x}e^{-\lambda}$"*).
    One day with $x_i$ spikes gives $P(x_i\mid\lambda)=\dfrac{\lambda^{x_i}e^{-\lambda}}{x_i!}$. The $\frac1{x_i!}$ has **no $\lambda$** in it, so by the box's "keep only the parts with $\theta$" it goes. What stays: $\lambda^{x_i}e^{-\lambda}$.

    ***

    **Sheet step 2 · "multiply them all (exponents add)"** (Calculations strip: $e^ae^b=e^{a+b}$).
    Six days, $x=\{2,4,3,5,2,4\}$:

    - the $\lambda$ powers add their exponents: $2+4+3+5+2+4=20$ → $\lambda^{20}$
    - six copies of $e^{-\lambda}$ give $e^{-6\lambda}$

    $$L(\lambda)\propto\lambda^{20}e^{-6\lambda}$$

    That is the first thing they ask for ("write the likelihood"). With the numbers left in: $L(\lambda)=\prod_i\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}$.

    ***

    **Sheet step 3 · "Multiply by the prior (exponents add again)"** (sheet's line: *"Prior Gamma$(a,b)$ = $\lambda^{a-1}e^{-b\lambda}$"*).
    $\alpha=3$, $\beta=2$ → $\lambda^{3-1}e^{-2\lambda}=\lambda^{2}e^{-2\lambda}$. Add the exponents of matching bases:

    $$p(\lambda\mid x)\propto\lambda^{20+2}\,e^{-(6+2)\lambda}=\lambda^{22}e^{-8\lambda}$$

    ***

    **Sheet step 4 · "Read the shape and use the table".**
    $\lambda^{A}e^{-B\lambda}$ with $A=22$, $B=8$ — the second table row. Read it one column at a time:

    | table column | gives |
    |---|---|
    | Posterior | Gamma$(A{+}1,B)$ = **Gamma(23, 8)** |
    | MAP | $\dfrac{A}{B}=\dfrac{22}{8}=\mathbf{2.75}$ |
    | MMSE (mean) | $\dfrac{A+1}{B}=\dfrac{23}{8}=2.875$ (not asked, but the column is right there) |

    ***

    **Sheet step 5 · "Compare with the MLE".**
    The MLE is the same rule on $L$ **alone** (no prior): $\lambda^{20}e^{-6\lambda}$ has $A=20$, $B=6$ → $\hat\lambda_{ML}=\frac AB=\frac{20}{6}=3.33$.
    The prior is Gamma(3, 2), whose own mean is $\frac{\alpha}{\beta}=\frac32=1.5$ — **below** 3.33, so it pulls the answer down from 3.33 to 2.75.

    ***

    **Sheet check · the example line.**
    The line at the bottom of box 2B (*Jun26-2d:* … MAP $=\frac{22}8=2.75$, MLE $=\frac{20}6=3.33$) is this exact question. If your line looks like the sheet's line, you have the points.

    </div>

!!! answer "Answer"
    $L(\lambda)\propto\lambda^{20}e^{-6\lambda}$ · posterior **Gamma(23, 8)** · $\hat\lambda_{MAP}=\dfrac{22}{8}=2.75$ · $\hat\lambda_{ML}=3.33$: the prior (mean $1.5$) pulls the estimate down, and its effect fades as the number of days grows.

## 2 · June 2026 · 2c — NegBin + Beta: the bracket on top is a number, drop it

!!! exam "Resit, June 2026 · 2c"
    A genomics researcher screens patients sequentially to recruit eligible participants for a trial. Each patient is independently eligible with unknown probability $\theta \in (0, 1)$. The researcher records the number of patients screened $X_i$ until exactly $k = 2$ eligible participants are found. This is modelled as

    $$X_i \sim \text{NegBin}(k, \theta), \quad k = 2 \text{ (known)},$$

    with PMF

    $$P(X = x \mid \theta) = \binom{x-1}{k-1} \theta^k (1-\theta)^{x-k}, \quad x = k, k+1, k+2, \dots$$

    The observed screening counts over five recruitment rounds are $x = \{3, 5, 4, 6, 4\}$. Assume a Beta prior on $\theta$:

    $$\theta \sim \text{Beta}(\alpha = 2, \beta = 3).$$

    - Write the likelihood function for $\theta$.
    - Derive the posterior distribution for $\theta$.
    - Compute the MAP estimate for $\theta$.

!!! sheet "In the cheat sheet: box 2B — this is exercise 1 with $\theta$ instead of $\lambda$"
    <div class="stepper" markdown>

    **Sheet step 1 · "write each observation's probability", and drop what has no $\theta$.**
    The sheet's list says: *"$k$-th success on trial $x$" → $\theta^k(1-\theta)^{x-k}$*. That matches this PMF with $k=2$.
    The bracket $\binom{x-1}{k-1}=\binom{x-1}{1}=x-1$ is a **number** built from $x$ only → *"Drop numbers without $\theta$"*. One patient stays as: $\theta^{2}(1-\theta)^{x-2}$.

    ***

    **Sheet step 2 · "multiply them all (exponents add)".**
    Five rounds, $x=\{3,5,4,6,4\}$:

    - $\theta^2$ five times → $\theta^{2\cdot5}=\theta^{10}$
    - $(1-\theta)$ exponents add: $(3-2)+(5-2)+(4-2)+(6-2)+(4-2)=1+3+2+4+2=12$

    (Check with $\sum x_i=3+5+4+6+4=22$ and $2\cdot5=10$: $22-10=12$ ✓.)

    $$L(\theta)\propto\theta^{10}(1-\theta)^{12}$$

    ***

    **Sheet step 3 · "Multiply by the prior (exponents add again)"** (sheet: *"Prior Beta$(a,b)$ = $\theta^{a-1}(1-\theta)^{b-1}$"*).
    $\alpha=2$, $\beta=3$ → $\theta^{2-1}(1-\theta)^{3-1}=\theta^{1}(1-\theta)^{2}$. Add:

    $$p(\theta\mid x)\propto\theta^{10+1}(1-\theta)^{12+2}=\theta^{11}(1-\theta)^{14}$$

    ***

    **Sheet step 4 · "Read the shape and use the table".**
    $\theta^{A}(1-\theta)^{B}$ with $A=11$, $B=14$ — the first table row:

    | table column | gives |
    |---|---|
    | Posterior | Beta$(A{+}1,B{+}1)$ = **Beta(12, 15)** |
    | MAP | $\dfrac{A}{A+B}=\dfrac{11}{11+14}=\dfrac{11}{25}=\mathbf{0.44}$ |
    | MMSE (mean) | $\dfrac{A+1}{A+B+2}=\dfrac{12}{27}\approx0.444$ |

    ***

    **Sheet check · the $+1$s.**
    The table writes the posterior as Beta$(A{+}1,B{+}1)$ and the MAP as $\frac A{A+B}$. So the **exponents** 11 and 14 are what you plug in — not the Beta parameters 12 and 15. Beta(12, 15) means $\theta^{11}(1-\theta)^{14}$, exactly what you wrote in step 3.
    For comparison, the MLE (box 2A on $L$ alone) is $\frac{nk}{\sum x_i}=\frac{10}{22}=0.455$; the prior's own mean is $\frac25=0.4$, so it pulls down slightly.

    </div>

!!! answer "Answer"
    $L(\theta)\propto\theta^{10}(1-\theta)^{12}$ · posterior **Beta(12, 15)** · $\hat\theta_{MAP}=\dfrac{11}{25}=0.44$

## 3 · April 2025 · 2d — the posterior is already given, so start at the table

!!! exam "Final exam, 13 April 2025 · 2d · 1 p"
    An experiment with binary outcomes Y/N has been independently repeated $N$ times and resulted in a dataset $\mathcal{D} = \{x_1, \dots, x_N\}$ in which $x_n \in \{Y, N\}$. Let $N_0$ and $N_1$ denote the number of obtained Ns and Ys, respectively. Furthermore, let $\theta$ denote the probability of obtaining a Y whereby the posterior distribution takes the form

    $$p(\theta | \mathcal{D}) = \theta^{\beta_1 - 1 + k_1 N_1} (1 - \theta)^{\beta_0 - 1 + k_0 N_0}.$$

    Derive the MAP estimate of $\theta$.

!!! sheet "In the cheat sheet: box 2B, step 3 only"
    <div class="stepper" markdown>

    **Sheet step 0 · notice what they gave you.**
    Steps 1 and 2 of the box (build the likelihood, multiply by the prior) are **already done** — the exam hands you the posterior. Jump straight to *"Read the shape and use the table"*.

    ***

    **Sheet step 1 · name the two exponents.**
    $\theta^{A}(1-\theta)^{B}$ with

    $$A=\beta_1-1+k_1N_1,\qquad B=\beta_0-1+k_0N_0.$$

    ($N_1$ Ys each contribute one $\theta$, $N_0$ Ns each contribute one $(1-\theta)$; the $\beta$'s came from the Beta prior.)

    ***

    **Sheet step 2 · read the MAP column.**
    First table row, MAP column: $\dfrac{A}{A+B}$. Fill $A$ and $B$ back in:

    $$\hat\theta_{MAP}=\frac{\beta_1-1+k_1N_1}{(\beta_1-1+k_1N_1)+(\beta_0-1+k_0N_0)}$$

    ***

    **Sheet step 3 · tidy the bottom.**
    $(\beta_1-1)+(\beta_0-1)=\beta_1+\beta_0-2$ (Calculations strip: collect the letters):

    $$\hat\theta_{MAP}=\frac{\beta_1-1+k_1N_1}{\beta_1+\beta_0-2+k_1N_1+k_0N_0}$$

    ***

    **Sheet check · if you forget the table.**
    Box 2A always works: $\ln p=A\ln\theta+B\ln(1-\theta)$ → $\frac A\theta-\frac B{1-\theta}=0$ → $A(1-\theta)=B\theta$ → $\theta=\frac A{A+B}$. That is the table's MAP column, derived.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{MAP}=\frac{A}{A+B}=\dfrac{\beta_1-1+k_1N_1}{\beta_1+\beta_0-2+k_1N_1+k_0N_0}$

## 4 · April 2024 · 2d — the unknown is hidden inside a sigmoid

!!! exam "Final exam, April 2024 · 2d · 1.5 p"
    Consider the posterior distribution

    $$p(\theta | x) = \frac{\lambda(\theta)}{2} e^{-\frac{\lambda(\theta)}{2}x}, \quad x > 1$$

    where $\lambda(\cdot)$ is defined as the logistic sigmoid function

    $$\lambda(\theta) = \frac{1}{1+e^{-\theta}}.$$

    Derive the MAP for the parameter $\theta$. Hint: The derivative of the logistic sigmoid is $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

!!! sheet "In the cheat sheet: box 2B for the words, box 2A for the work"
    <div class="stepper" markdown>

    **Sheet step 0 · box 2B says MAP = the top; box 2A's Sigmoid trick says how to find it.**
    The sheet: *"IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$."* Same trick as [2.1, exercise 7](e2-mle.md#7-april-2025-2c-sigmoid-use-the-trick-at-the-bottom-of-box-2a) — there it was a likelihood, here it is a posterior. **MAP = top of the posterior** is the only thing that changed.

    ***

    **Sheet step 1 · take $\ln$, term by term** (box 2A: *"a piece above the line → $+\ln a$; a piece below → $-\ln b$; $e^{u}$ → $u$"*).
    One piece: $\frac{\lambda}{2}e^{-\frac{\lambda x}{2}}$:

    - $\lambda$ — **above the line** → $+\ln\lambda$
    - $2$ — **below the line** → $-\ln 2$ (a constant, it dies in step 2)
    - $e^{-\frac{\lambda x}{2}}$ — **the $e$ part** → $-\frac x2\lambda$

    $$\ln p=\ln\lambda-\ln 2-\frac x2\lambda$$

    ***

    **Sheet step 2 · differentiate in $\lambda$** (rules $\ln\theta\to\frac1\theta$ and $(c\,\theta)\to c$):

    $$\frac{d}{d\lambda}\ln p=\frac1\lambda-\frac x2$$

    ***

    **Sheet step 3 · $=0$, multiply by $\lambda$** (box 2A: clear the denominators first):
    $1-\frac x2\lambda=0$ → $\hat\lambda=\dfrac2x$.

    ***

    **Sheet step 4 · the sheet's conversion formula.**
    $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)=-\ln\!\big(\frac x2-1\big)$.

    ***

    **Sheet check · the range.**
    The Calculations strip: "$\ln$ of a **positive** number" → $\frac x2-1>0$ → $x>2$. (The exam's hint about $\frac{\partial\lambda}{\partial\theta}=\lambda(1-\lambda)$ gives the same: that factor is never 0, so it cannot change the top.)

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{MAP}=-\ln\!\left(\frac x2-1\right)=\ln\frac{2}{x-2}$, valid for $x>2$

## 5 · November 2022 · 2f and 2g — MAP and MMSE of the *same* posterior

!!! exam "Final exam, November 2022 · 2f, 2g · 0.5 p each"
    Assume that the parameter $\theta \geq 0$ is a random variable that admits an exponential distribution with probability density function

    $$p(\theta) = ae^{-a\theta}.$$

    The conditional probability function of the observation $x \geq 0$ is

    $$p(x|\theta) = \theta e^{-\theta x}.$$

    Using Bayes' theorem, the posterior distribution for the parameter $\theta$ after observing $x$ is

    $$p(\theta|x) = \begin{cases} (x+a)^2 \theta e^{-(x+a)\theta} & \theta \geq 0, \\ 0, & \text{else.} \end{cases}$$

    **2f** Find the minimum-mean square error estimator. Hint: You can use the identity $\int x^2 e^{-x} dx = -e^{-x}(x^2 + 2x + 2)$, which is obtained by using integration by parts twice.

    **2g** Find the maximum a posteriori estimator.

!!! sheet "In the cheat sheet: box 2B table + box 2D rows"
    <div class="stepper" markdown>

    **Sheet step 1 · keep the $\theta$ parts.**
    The posterior is $(x+a)^2\cdot\theta\cdot e^{-(x+a)\theta}$. The $(x+a)^2$ has **no $\theta$** → *"Drop numbers without $\theta$"*. What stays:

    $$p(\theta\mid x)\propto\theta^{1}e^{-(x+a)\theta}$$

    ***

    **Sheet step 2 · "Read the shape and use the table".**
    $\lambda^{A}e^{-B\lambda}$ with $A=1$ and $B=x+a$ (the second row). Read **both** answer columns — the two sub-questions are exactly the two columns:

    | table column | gives | sub-question |
    |---|---|---|
    | MAP | $\dfrac AB=\dfrac{1}{x+a}$ | **2g** |
    | MMSE (mean) | $\dfrac{A+1}{B}=\dfrac{2}{x+a}$ | **2f** |

    ***

    **Sheet step 3 · sanity check with box 2D.**
    The row *"MMSE = the **mean** of the posterior"* and *"MAP = the maximum"*: the mean is twice the top here, so they are **different numbers** — as expected for a lopsided posterior.

    ***

    **Sheet step 4 · if they make you integrate (2f's hint).**
    MMSE $=E[\theta\mid x]=\dfrac{\int_0^\infty \theta\cdot p(\theta\mid x)\,d\theta}{\int_0^\infty p(\theta\mid x)\,d\theta}$, and the Calculations strip has the finished integrals: $\int_0^\infty \theta e^{-c\theta}d\theta=\frac1{c^2}$, $\int_0^\infty \theta^2 e^{-c\theta}d\theta=\frac2{c^3}$. With $c=x+a$:

    $$\hat\theta_{MMSE}=\frac{2/(x+a)^3}{1/(x+a)^2}=\frac{2}{x+a}$$

    (That is the sheet's *Nov22-2f* example line, printed at the bottom of the **Calculations** strip.)

    </div>

!!! answer "Answer"
    **2f** $\displaystyle\hat\theta_{MMSE}=\frac{2}{x+a}$ · **2g** $\displaystyle\hat\theta_{MAP}=\frac{1}{x+a}$

## 6 · Q3 2022-23 · 2g and 2h — the exponent is $0$, so the top sits at the edge

!!! exam "Q3 2022-23 exam · 2g, 2h"
    Suppose we have a single observation of random variable $X$ which follows the following probability distribution conditioned on $\theta$: $p(x|\theta) = \frac{1}{x} e^{-\theta x}$, for $x > 0, \theta > 0$, and suppose that $\theta$ follows an exponential prior as $p(\theta) = \frac{1}{a} e^{-a\theta}$ with $a > 0$ a known value.

    Additionally, the following known integrals are given: $\int e^{cx} dx = \frac{1}{c} e^{cx}$, $\int x e^{cx} dx = \left( \frac{cx - 1}{c^2} \right) e^{cx}$, $\int x^2 e^{cx} dx = \left( \frac{x^2}{c} - \frac{2x}{c^2} + \frac{2}{c^3} \right) e^{cx}$.

    **2g** Compute the posterior distribution $p(\theta|x)$.

    **2h** Find the Bayesian minimum mean square error estimator.

!!! sheet "In the cheat sheet: box 2B, the $A=0$ case"
    <div class="stepper" markdown>

    **Sheet step 1 · likelihood × prior, keep the $\theta$ parts.**
    $\frac1x e^{-\theta x}$ (the $\frac1x$ has no $\theta$ → drop) times $\frac1a e^{-a\theta}$ (drop $\frac1a$):

    $$p(\theta\mid x)\propto e^{-\theta x}e^{-a\theta}=e^{-(x+a)\theta}$$

    using the Calculations strip: $e^ae^b=e^{a+b}$.

    ***

    **Sheet step 2 · read the shape — it is the table's second row with $A=0$.**
    $\lambda^{A}e^{-B\lambda}$ with $A=0$ (there is no $\theta$ in front at all) and $B=x+a$:

    | table column | gives |
    |---|---|
    | Posterior | Gamma$(0{+}1,\ x+a)$ = Gamma$(1,x+a)$ = Exponential$(x+a)$ |
    | MAP | $\dfrac AB=\dfrac{0}{x+a}=0$ |
    | MMSE (mean) | $\dfrac{A+1}{B}=\dfrac{1}{x+a}$ |

    ***

    **Sheet step 3 · 2g wants the posterior written out, so normalise.**
    $p(\theta\mid x)=C\,e^{-(x+a)\theta}$ for $\theta>0$. Fix $C$ by making the area 1 (Calculations: $\int_0^\infty e^{-c\theta}d\theta=\frac1c$): $C\cdot\frac1{x+a}=1$ → $C=x+a$.

    $$p(\theta\mid x)=(x+a)e^{-(x+a)\theta},\qquad \theta>0$$

    (Longer route, same answer: $p(x)=\int_0^\infty\frac1x e^{-\theta x}\frac1a e^{-a\theta}d\theta=\frac1{ax(x+a)}$, so $p(\theta\mid x)=\frac{p(x\mid\theta)p(\theta)}{p(x)}=(x+a)e^{-(x+a)\theta}$.)

    ***

    **Sheet step 4 · 2h = the MMSE column.**
    $\hat\theta_{MMSE}=\dfrac{1}{x+a}$. Box 2D: *"MMSE = the **mean** of the posterior"* — and the mean of an Exponential$(x+a)$ is $\frac1{x+a}$ ✓.

    ***

    **Sheet check · where did the MAP go?**
    The table says MAP $=0$: the curve $e^{-(x+a)\theta}$ only falls, so its highest point is at the left edge $\theta=0$. The question does not ask for it here — but this is exactly why $A=0$ is worth recognising.

    </div>

!!! answer "Answer"
    **2g** $p(\theta\mid x)=(x+a)e^{-(x+a)\theta}$ for $\theta>0$ · **2h** $\displaystyle\hat\theta_{MMSE}=\frac{1}{x+a}$

## 7 · Q3 2022-23 · 2f and 2g — two bumps, so the mean and the maximum come apart

*(This is the one posterior that is **not** a single bump. It is where the box 2D rows "MMSE = the mean" and "MAP = the maximum" stop agreeing — and exams ask about that.)*

!!! exam "Q3 2022-23 exam · 2f, 2g"
    For the posterior PDF

    $$p(\theta|x) = \frac{c}{\sqrt{2\pi}}\exp\left[-\frac{1}{2}(\theta - x)^2\right] + \frac{1-c}{\sqrt{2\pi}}\exp\left[-\frac{1}{2}(\theta + x)^2\right]$$

    **2f** Find the Bayesian MMSE estimator for $\theta$, in case $c = \frac{1}{2}$ and $c = \frac{3}{4}$.

    **2g** Provide a sketch of $p(\theta|x)$ for $c = \frac{1}{2}$ and $c = \frac{3}{4}$. Looking at the sketch, what is the MAP estimate in the two cases? You do not need to find it analytically.

    For this exercise, we restrict our attention to $|x| > 2$.

!!! sheet "In the cheat sheet: box 2D, the two rows people confuse"
    <div class="stepper" markdown>

    **Sheet step 0 · read the shape of the posterior first.**
    Two Gaussian bumps: $\frac{c}{\sqrt{2\pi}}e^{-\frac12(\theta-x)^2}$ is a standard Gaussian **centred at $+x$**, weight $c$; the other is centred at $-x$, weight $1-c$. (Completing the square is not needed — they are already written as Gaussians.)

    ***

    **Sheet step 1 · MMSE = the mean (box 2D row).**
    The mean of a weighted mixture is the weighted mean of the pieces' means:

    $$\hat\theta_{MMSE}=c\cdot x+(1-c)\cdot(-x)=(2c-1)x$$

    - $c=\frac12$: $(2\cdot\frac12-1)x=\mathbf 0$
    - $c=\frac34$: $(2\cdot\frac34-1)x=\mathbf{\dfrac x2}$

    ***

    **Sheet step 2 · MAP = the maximum (the other box 2D row: "MMSE = the maximum" is **F** — that is the MAP).**
    Read it off the sketch, no algebra:

    - $c=\frac12$: the two bumps are the **same height**, so both tops are the maximum → $\hat\theta_{MAP}=\mathbf{\pm x}$
    - $c=\frac34$: the bump at $+x$ is taller → $\hat\theta_{MAP}=\mathbf{+x}$

    ***

    **Sheet check · the row that earns the point.**
    MMSE $=0$ while MAP $=\pm x$ for $c=\frac12$: the two estimators are **not** "always different" (box 2D: F) and not "always equal" (also F). They agree only for a single symmetric bump.

    </div>

!!! answer "Answer"
    **2f** MMSE $=(2c-1)x$: $0$ for $c=\frac12$, $\ \dfrac x2$ for $c=\frac34$ · **2g** MAP $=\pm x$ for $c=\frac12$ (both tops equal), $\ +x$ for $c=\frac34$

## 8 · January 2022 · 2f, 2g, 2h — the unknown is $+1$ or $-1$

!!! exam "Resit, January 2022 · 2f, 2g, 2h"
    Let $Y = X + N$ where $X$ and $N$ are independent random variables. $X$ takes the values +1 and -1 with equal probability, and $N$ is a zero-mean Gaussian random variable with variance $\sigma^2$.

    **2f** Evaluate the aposteriori probabilities $P[X = 1|Y]$ and $P[X = -1|Y]$.

    **2g** Find the minimum mean square error estimate $\hat{X}_{\text{MMSE}}$ of $X$ given $Y$. Useful identities: $\frac{e^{2u} - 1}{e^{2u} + 1} = \frac{e^u - e^{-u}}{e^u + e^{-u}} = \tanh(u)$

    **2h** Find the maximum a posterior estimator $\hat{X}_{\text{MAP}}$ of $X$ given the observation $Y$. More specifically, find a threshold value $y_{\text{th}}$ such that a decision on $X$ depends on whether or not this threshold value is exceeded or not. *Hint:* Recall that $X$ is a discrete random variable. Hence, $\hat{X}_{\text{MAP}} = \arg \max_{X \in \{1, -1\}} P[X|Y]$. To check which value of $X$ maximizes the a posterior probability, you simply can check the ratio of the a posterior probabilities.

!!! sheet "In the cheat sheet: box 2D says WHAT to compute; box 2B's table does not fit here"
    <div class="stepper" markdown>

    **Sheet step 0 · notice the shape.**
    The unknown $X$ is **discrete** ($+1$ or $-1$), so the Beta/Gamma table does not apply. But box 2D tells you exactly what each estimator is: **MAP = the largest posterior**, **MMSE = the mean of the posterior**. Everything else is Bayes' rule and one $e^ae^b=e^{a+b}$.

    ***

    **Sheet step 1 · weights (box 2B: "write each observation's probability, keep only the parts with the unknown").**
    If $X=s$, then $Y\sim N(s,\sigma^2)$, so $p(y\mid X=s)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(y-s)^2}{2\sigma^2}}$. Both $X$ values have prior $\frac12$, and the common factor $\frac{1}{\sqrt{2\pi}\sigma}\cdot\frac12$ cancels in the division. Weights:

    $$w_s=e^{-\frac{(y-s)^2}{2\sigma^2}},\qquad P[X=s\mid y]=\frac{w_s}{w_1+w_{-1}}$$

    ***

    **Sheet step 2 · 2f: divide by the sum.**
    $\frac{w_1}{w_{-1}}=e^{-\frac{(y-1)^2-(y+1)^2}{2\sigma^2}}=e^{-\frac{-4y}{2\sigma^2}}=e^{2y/\sigma^2}$ (expand $(y\mp1)^2=y^2\mp2y+1$).
    So, writing $u=\dfrac{y}{\sigma^2}$:

    $$P[X=1\mid y]=\frac{1}{1+e^{-2u}},\qquad P[X=-1\mid y]=\frac{1}{1+e^{2u}}$$

    Both are sigmoid curves in $y$ — the exam prints these two formulas after the question (its second one has a sign typo: the denominator should carry $e^{+u}$, not $e^{-u}$).

    ***

    **Sheet step 3 · 2g: MMSE = the mean** (box 2D row), and the identity they gave you:

    $$\hat X_{MMSE}=1\cdot P[X=1\mid y]+(-1)\cdot P[X=-1\mid y]=P_1-P_{-1}=\frac{1-e^{-2u}}{1+e^{-2u}}=\tanh(u)$$

    $$\hat X_{MMSE}=\tanh\!\left(\frac{y}{\sigma^2}\right)$$

    ***

    **Sheet step 4 · 2h: MAP = the larger of the two** (box 2D row), following their hint to take the ratio:
    $P_1>P_{-1}\iff e^{2y/\sigma^2}>1\iff 2y/\sigma^2>0\iff y>0$. So $\hat X_{MAP}=+1$ for $y>0$ and $-1$ for $y<0$: the threshold is $\mathbf{y_{th}=0}$.

    </div>

!!! answer "Answer"
    **2f** $P[X=1\mid y]=\dfrac{1}{1+e^{-2y/\sigma^2}}$, $P[X=-1\mid y]=\dfrac{1}{1+e^{2y/\sigma^2}}$ · **2g** $\hat X_{MMSE}=\tanh\!\dfrac{y}{\sigma^2}$ · **2h** $\hat X_{MAP}=+1$ if $y>0$ else $-1$, so $y_{th}=0$

## 9 · November 2019 · 3c — a cubic: the exam lets you stop at the equation

!!! exam "Written exam, November 2019 · 3c"
    *(Same likelihood as 3a: i.i.d. $p(x;\theta)=\dfrac{x}{\theta^2}e^{-x^2/(2\theta^2)}$, $N$ samples.)*

    Now consider the case where $p(\theta)$ is also a random variable with PDF $p(\theta) = \lambda \exp[-\lambda\theta]$. Find the MAP estimator for the parameter $\theta$. The answer does **not** have to be in the form $\hat{\theta} = f(x, \lambda)$.

!!! sheet "In the cheat sheet: box 2B step 2 + box 2A steps 1–3"
    <div class="stepper" markdown>

    **Sheet step 1 · add the prior to the log-likelihood** (box 2B: *"Multiply by the prior. Drop numbers without $\theta$"*).
    The prior $\lambda e^{-\lambda\theta}$ contributes $\ln\lambda-\lambda\theta$; $\ln\lambda$ has no $\theta$ → drop. So the posterior's $\ln$ is the [2.1 exercise 4](e2-mle.md#4-november-2019-3a-theta2-so-2lntheta) log-likelihood **plus $-\lambda\theta$**:

    $$\ln p(\theta\mid x)=\text{const}-2N\ln\theta-\frac{1}{2\theta^2}\sum_n x_n^2-\lambda\theta$$

    ***

    **Sheet step 2 · differentiate in $\theta$** (box 2A's derivative list):
    $-2N\ln\theta\to-\frac{2N}\theta$ · $-\frac{1}{2\theta^2}\sum x_n^2\to+\frac{1}{\theta^3}\sum x_n^2$ (rule $\theta^k\to k\theta^{k-1}$ with $k=-2$) · $-\lambda\theta\to-\lambda$ (rule $(c\,\theta)\to c$).

    $$-\frac{2N}\theta+\frac{1}{\theta^3}\sum_n x_n^2-\lambda=0$$

    ***

    **Sheet step 3 · clear the denominators** (box 2A: *"multiply by the denominators first"*).
    Multiply by $\theta^3$:

    $$-2N\theta^2+\sum_n x_n^2-\lambda\theta^3=0\qquad\Longrightarrow\qquad \lambda\theta^3+2N\theta^2-\sum_n x_n^2=0$$

    ***

    **Sheet step 4 · and here the sheet runs out — on purpose.**
    A cubic has no formula on the sheet. Read the last sentence of the question again: *"The answer does **not** have to be in the form $\hat\theta=f(x,\lambda)$."* That sentence is your permission to stop. Say: **the MAP is the positive root of that cubic** (the negative roots are impossible, $\theta>0$).

    </div>

!!! answer "Answer"
    $\hat\theta_{MAP}$ = the positive root of $\ \lambda\theta^3+2N\theta^2-\displaystyle\sum_{n}x_n^2=0$

## 10 · January 2019 · 2b and 2c — a flat prior, so the range is what matters

!!! exam "Retake, January 2019 · 2b, 2c"
    *(Same model as 2a: $p(x;\lambda)=\lambda e^{-\lambda x}$, $N$ independent observations $x_i$.)*

    (b) Additional information regarding $\lambda$ is provided in terms of a distribution

    $$p(\lambda) = \begin{cases} \frac{1}{2} & 0 \leq \lambda \leq 2 \\ 0 & \text{otherwise} \end{cases}$$

    Treat the distribution $p(x; \lambda)$ as a conditional distribution $p(x|\lambda)$ and determine the Bayesian minimum mean square estimator (MMSE) for $\lambda$. To do so, (1) first provide the formula to calculate the Bayesian MMSE, specifying each probability distribution explicitly; (2) then, determine the Bayesian MMSE by solving the formula obtained in b1.

    (c) Using the same information given above, find the maximum a-posteriori (MAP) estimator for $\lambda$.

    Below some useful integrals: $\int f g' dx = fg - \int f' g dx$, $\int e^{ax} dx = \frac{1}{a} e^{ax}$, $\int x e^{ax} dx = \left( \frac{x}{a} - \frac{1}{a^2} \right) e^{ax}$, $\int x^2 e^{ax} dx = \left( \frac{x^2}{a} - \frac{2x}{a^2} + \frac{2}{a^3} \right) e^{ax}$

!!! sheet "In the cheat sheet: box 2B + box 2A + the Calculations integrals (this is the heavy one)"
    <div class="stepper" markdown>

    **Sheet step 1 · likelihood × prior.**
    Box 2B's one-observation line: *"exponential → $\lambda e^{-\lambda x}$"*. $N$ observations → $\lambda^{N}e^{-\lambda\sum_i x_i}$.
    The prior is the constant $\tfrac12$ — *"Drop numbers without $\theta$"* — **but keep its range**: $0\le\lambda\le2$.

    $$p(\lambda\mid x)\propto\lambda^{N}e^{-\lambda\sum_i x_i},\qquad 0\le\lambda\le2$$

    ***

    **Sheet step 2 · (c) MAP = the top of that, inside the range.**
    Box 2A on the $\lambda$ part: $N\ln\lambda-\lambda\sum x_i$ → $\frac N\lambda-\sum x_i=0$ → $\hat\lambda=\dfrac{N}{\sum_i x_i}=\dfrac1{\bar x}$.
    **Now check the range** — this is the step the prior added: if $\frac1{\bar x}>2$, the curve is still climbing at $\lambda=2$ and the top is at the edge. So the safe answer is

    $$\hat\lambda_{MAP}=\min\!\left(\frac{N}{\sum_i x_i},\,2\right)$$

    (The answer key writes just $\frac{N}{\sum_i x_i}$ — same thing whenever the data mean is above $\frac12$.)

    ***

    **Sheet step 3 · (b1) the MMSE formula** (box 2D: *"MMSE = the mean of the posterior"*):

    $$\hat\lambda_{MMSE}=E[\lambda\mid x]=\frac{\int_0^2 \lambda\,p(\lambda\mid x)\,d\lambda}{\int_0^2 p(\lambda\mid x)\,d\lambda} =\frac{\int_0^2 \lambda^{N+1}e^{-\lambda S}\,d\lambda}{\int_0^{2} \lambda^{N}e^{-\lambda S}\,d\lambda},\qquad S=\sum_i x_i$$

    (The constant $\frac12$ of the prior cancels top and bottom — that is why "drop numbers" is legal.)

    ***

    **Sheet step 4 · (b2) integrate** with the integrals printed in the question (they are on the sheet's **Calculations** strip too).
    For one observation ($N=1$, $S=x$), with $a=-x$ in their $\int x^2e^{ax}dx$ and $\int xe^{ax}dx$:

    $$\int_0^2\lambda^{2}e^{-x\lambda}d\lambda=\frac{2}{x^3}-e^{-2x}\!\left(\frac4x+\frac4{x^2}+\frac2{x^3}\right),\qquad \int_0^{2}\lambda e^{-x\lambda}d\lambda=\frac1{x^2}-e^{-2x}\!\left(\frac2x+\frac1{x^2}\right)$$

    Divide top by bottom (Calculations: $\frac ab\div\frac cd=\frac{ad}{bc}$) and simplify:

    $$\hat\lambda_{MMSE}=\frac2x\left(1-\frac{2x^2e^{-2x}}{1-e^{-2x}(1+2x)}\right)$$

    ***

    **Sheet check.**
    The limits $0$ to $2$ are what make this ugly; with $0$ to $\infty$ the same two integrals give the clean $\frac2x$. This question is worth 2 points and has not come back since — learn the *setup* of step 3, not the final fraction.

    </div>

!!! answer "Answer"
    **(c)** $\displaystyle\hat\lambda_{MAP}=\min\!\left(\frac{N}{\sum_i x_i},\,2\right)$ · **(b)** $\displaystyle\hat\lambda_{MMSE}=\frac{\int_0^2 \lambda\,p(\lambda\mid x)\,d\lambda}{\int_0^2 p(\lambda\mid x)\,d\lambda}$, which for one observation evaluates to $\dfrac2x\Big(1-\dfrac{2x^2e^{-2x}}{1-e^{-2x}(1+2x)}\Big)$

## 11 · June 2026 · 2a — true/false, read the row

!!! exam "Resit, June 2026 · 2a"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) The MAP estimate always equals the posterior mean.
    - (b) As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior.
    - (c) The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution.

!!! sheet "In the cheat sheet: box 2D, three rows"
    <div class="stepper" markdown>

    **Sheet step 1 · (c) is on the sheet verbatim.**
    Row *"MAP depends on likelihood and prior; needs a prior"* → **T (Jun26 c)**. The sheet even tags the row with this exam.

    ***

    **Sheet step 2 · (b) is the row written to trap you.**
    *"MAP → MLE for many samples "regardless of the prior"* → **F**. The word "regardless" is what kills it.

    ***

    **Sheet step 3 · (a) vs the rows "MMSE = the mean of the posterior" and "MMSE = MAP always differ → F".**
    MAP equals the posterior **mean** only when the posterior is a single symmetric bump — not "always". So (a) is **F** too.

    </div>

!!! answer "Answer"
    **(c)**

## 12 · April 2025 · 2a — same rows, but this time pick the FALSE one

!!! exam "Final exam, 13 April 2025 · 2a · 0.5 p"
    Which of the following statements is FALSE?

    - a) The MLE is the argument maximising the likelihood.
    - b) The MMSE estimate results from minimising the square error.
    - c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

!!! sheet "In the cheat sheet: box 2D, two rows"
    <div class="stepper" markdown>

    **Sheet step 1 · read the question's word: FALSE.**
    Two statements are true and one is false. Check each against a row.

    ***

    **Sheet step 2 · (a) is true** — row *"MLE maximises the likelihood over $\theta$"* → T. (Over $x$ would be F — that distractor is in [2.1, exercise 11](e2-mle.md#11-january-2022-resit-2b-truefalse-the-invariance-row).)

    ***

    **Sheet step 3 · (b) is true** — row *"MMSE = the mean of the posterior; minimises squared error"* → T.

    ***

    **Sheet step 4 · (c) is the false one** — row *"MMSE and MAP **always** give different estimates"* → **F (same for a symmetric posterior)**. Exercise 7 above is the picture of why.

    </div>

!!! answer "Answer"
    **(c)**

## 13 · April 2024 · 2b and January 2022 · 2d — the same question, the letters shuffled

!!! exam "Final exam, April 2024 · 2b · 0.5 p"
    Which of the following statements is TRUE?

    - (a) In Bayesian estimation, the minimum mean square error is the mean of the posterior PDF.
    - (b) In Bayesian estimation, the minimum mean square error is the maximum of the posterior PDF.
    - (c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

!!! exam "Resit, January 2022 · 2d · 0.3 p"
    Which of the following statements about the Bayesian estimators is true?

    - (a) The minimum mean square error is the maximum of the aposterior PDF.
    - (b) The minimum mean square error is the mean of the aposterior PDF.
    - (c) The minimum mean square error estimator and the maximum aposterior estimator will always result in a different estimate.

!!! sheet "In the cheat sheet: box 2D, one row — read the sentence, not the letter"
    <div class="stepper" markdown>

    **Sheet step 1 · the row is: *"MMSE = the **mean** of the posterior; minimises squared error"* → T, and *"MMSE = the maximum of the posterior"* → F (that is MAP).**
    The two papers print the same three sentences in a **different order**. Find the sentence, then write down its letter.

    ***

    **Sheet step 2 · April 2024.**
    "is the mean of the posterior" is sentence **(a)** → answer **(a)**.

    ***

    **Sheet step 3 · January 2022.**
    "is the mean of the aposterior" is sentence **(b)** → answer **(b)**. ("Aposterior" = "a posteriori", same thing.)

    ***

    **Sheet check · the third sentence.**
    "*always* result in a different estimate" → F both times (box 2D row), and exercise 7 is the counter-example.

    </div>

!!! answer "Answer"
    April 2024 → **(a)** · January 2022 → **(b)**

## 14 · November 2022 · 2c — the Bayes risk row

!!! exam "Final exam, November 2022 · 2c · 0.25 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) Unlike classical estimators, Bayesian estimators do not incorporate prior knowledge about the unknown parameter.
    - (b) The Bayesian estimate is the estimate that minimizes the Bayes risk, i.e., $\hat{\theta} = \arg \min_{\hat{\theta}} \int \int C(e)p(\theta|\mathbf{x})d\theta p(\mathbf{x})d\mathbf{x}$.
    - (c) Minimizing Bayes Risk for the uniform error cost function results in the minimum mean square error estimator.

!!! sheet "In the cheat sheet: box 2D, three rows"
    <div class="stepper" markdown>

    **Sheet step 1 · (b) is on the sheet verbatim.**
    Row *"Bayes estimate minimises the Bayes risk"* → **T (Nov22 b)**.

    ***

    **Sheet step 2 · (a) is the row *"Bayesian estimators do not use prior knowledge"* → F.**
    The prior is exactly what makes them Bayesian.

    ***

    **Sheet step 3 · (c) is the row *"Uniform cost → MMSE"* → F (uniform → MAP).**
    Squared-error cost gives the MMSE; uniform (0/1) cost gives the MAP. That is the same pair of rows as exercises 5 and 7.

    </div>

!!! answer "Answer"
    **(b)**

## Traps

!!! trap "Where points are lost (each one is a line of the sheet you skipped)"
    - Reading the **Beta/Gamma parameters** off the exponents without adding 1. Exponent $11$ means Beta$(12,15)$; but the MAP formula $\frac A{A+B}$ wants the **exponents** $11$ and $14$ (sheet: "Read the shape and use the table").
    - Forgetting to multiply by the prior at all. Likelihood alone gives the **MLE**; "MAP" always needs the prior (box 2D row).
    - Gamma is written with a **rate**: prior $\lambda^{\alpha-1}e^{-\beta\lambda}$ → MAP $=\frac{\alpha-1}{\beta}$, not $(\alpha-1)\beta$.
    - Keeping a factor with no $\theta$ in it ($\binom{x-1}{k-1}$, $x!$, $\frac12$, $\frac1x$) and then differentiating it as if it mattered. *"Drop numbers without $\theta$"*. **But** never drop the **range** a prior imposes (January 2019: $0\le\lambda\le2$).
    - Mixing up the two estimators: **MAP = the maximum**, **MMSE = the mean**. Two exams ask exactly that, and one asks for the FALSE one.
    - "Compare the MAP with the MLE" → give the **direction** of the pull (towards the prior's own mean: $\frac\alpha\beta$ for Gamma, $\frac{a}{a+b}$ for Beta) and say that it **fades** as the number of observations grows.
    - Sigmoid: differentiate in $\lambda$, then convert with $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$ (box 2A's trick), and write the range $x>2$ at the end.
