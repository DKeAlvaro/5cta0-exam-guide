# 2.3 Bayesian estimation: MAP and MMSE

<p class="lead">In Bayesian estimation the unknown θ is itself random, with a <b>prior</b> distribution. Recent exams ask for a MAP almost every time, often with a prior that makes the algebra trivial (Beta, Gamma). MMSE shows up less often but is quick once you know the three integrals.</p>

## The idea, from zero

Before seeing data you already believe something about $\theta$: the **prior** $p(\theta)$. The data update that belief through Bayes' theorem (the same formula as in [1.1](p1-bayes.md)):

$$\underbrace{p(\theta\mid\mathbf x)}_{\text{posterior}}=\frac{\overbrace{p(\mathbf x\mid\theta)}^{\text{likelihood}}\ \overbrace{p(\theta)}^{\text{prior}}}{\underbrace{p(\mathbf x)}_{\text{evidence}=\int p(\mathbf x\mid\theta)p(\theta)d\theta}}\ \propto\ p(\mathbf x\mid\theta)\,p(\theta).$$

The posterior is everything you know about $\theta$ after the data. To give **one number**, choose a cost for being wrong and minimise its expected value (the **Bayes risk**):

| Cost of error $e=\theta-\hat\theta$ | Best estimate | Name |
|---|---|---|
| quadratic $e^2$ | **mean** of the posterior | MMSE (minimum mean square error) |
| absolute $\lvert e\rvert$ | median of the posterior | |
| uniform / "hit-or-miss" | **mode** (peak) of the posterior | MAP (maximum a posteriori) |

**MAP vs MLE.** MAP maximises likelihood × prior; MLE maximises the likelihood alone. With a flat prior they are equal. With lots of data the likelihood dominates and MAP moves towards the MLE.

**MAP vs MMSE.** Equal when the posterior is symmetric with one peak (e.g. Gaussian). Different otherwise: skewed or two-peaked posteriors (see the figures below).

!!! recipe "Recipe: MAP"
    1. Write $\ln p(\mathbf x\mid\theta)+\ln p(\theta)$ (or $\ln p(\theta\mid\mathbf x)$ if the posterior is given). The evidence $p(\mathbf x)$ does not depend on $\theta$: ignore it.
    2. Differentiate with respect to $\theta$, set to 0, solve.
    3. Check the solution lies inside the allowed range of $\theta$ (otherwise the max is at the boundary).

!!! recipe "Recipe: MMSE"
    1. You need the **normalised** posterior. If it is not given: posterior = likelihood × prior / (its integral over $\theta$).
    2. $\hat\theta_{MMSE}=\int\theta\,p(\theta\mid\mathbf x)\,d\theta$.
    3. The integrals are almost always of the form $\int_0^\infty\theta^n e^{-s\theta}d\theta=\frac{n!}{s^{n+1}}$.

!!! idea "Conjugate priors: the shortcut used in recent exams"
    If the prior has the same shape as the likelihood in $\theta$, the posterior has that shape too, and you just **add exponents**:

    - Likelihood $\propto\theta^{A}(1-\theta)^{B}$ (Bernoulli, binomial, negative binomial) + prior Beta($\alpha,\beta$) $\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$
      → posterior Beta($\alpha+A,\ \beta+B$), **mode** $=\dfrac{\alpha+A-1}{\alpha+\beta+A+B-2}$.
    - Likelihood $\propto\lambda^{S}e^{-n\lambda}$ (Poisson) + prior Gamma($\alpha,\beta$) $\propto\lambda^{\alpha-1}e^{-\beta\lambda}$
      → posterior Gamma($\alpha+S,\ \beta+n$), **mode** $=\dfrac{\alpha+S-1}{\beta+n}$.

---

## Exam questions: derivations

### June 2026 resit · 2c {#jun26-2c}

!!! exam "Resit Q4, June 2026 · 2c"
    A genomics researcher screens patients sequentially to recruit eligible participants for a trial. Each patient is independently eligible with unknown probability $\theta \in (0, 1)$. The researcher records the number of patients screened $X_i$ until exactly $k = 2$ eligible participants are found. This is modelled as

    $$X_i \sim \text{NegBin}(k, \theta), \quad k = 2 \text{ (known)},$$

    with PMF

    $$P(X = x \mid \theta) = \binom{x-1}{k-1} \theta^k (1-\theta)^{x-k}, \quad x = k, k+1, k+2, \dots$$

    The observed screening counts over five recruitment rounds are $x = \{3, 5, 4, 6, 4\}$. Assume a Beta prior on $\theta$:

    $$\theta \sim \text{Beta}(\alpha = 2, \beta = 3).$$

    - Write the likelihood function for $\theta$.
    - Derive the posterior distribution for $\theta$.
    - Compute the MAP estimate for $\theta$.

    Hint: A random variable $X$ is said to follow a Beta distribution with parameters $\alpha > 0$ and $\beta > 0$, denoted $X \sim \text{Beta}(\alpha, \beta)$, if its probability density function is

    $$p(x \mid \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1}, \quad 0 < x < 1,$$

    where the Beta function is defined as $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta).$

???+ solution "Solution"
    **Likelihood.** $n=5$ rounds, $k=2$, $\sum x_i=3+5+4+6+4=22$:

    $$L(\theta)=\prod_{i=1}^5\binom{x_i-1}{1}\theta^2(1-\theta)^{x_i-2}=\Big[\prod_i(x_i-1)\Big]\theta^{2n}(1-\theta)^{\sum x_i-2n}=360\,\theta^{10}(1-\theta)^{12}.$$

    ($\prod(x_i-1)=2\cdot4\cdot3\cdot5\cdot3=360$, a constant that does not matter.) In words: 10 eligible patients and 12 non-eligible ones were seen in total.

    **Posterior** ∝ likelihood × prior, with prior $\propto\theta^{1}(1-\theta)^{2}$:

    $$p(\theta\mid\mathbf x)\propto\theta^{10}(1-\theta)^{12}\cdot\theta^{1}(1-\theta)^{2}=\theta^{11}(1-\theta)^{14}\;\Rightarrow\;\theta\mid\mathbf x\sim\text{Beta}(12,\,15).$$

    Normalised: $p(\theta\mid\mathbf x)=\frac{1}{B(12,15)}\theta^{11}(1-\theta)^{14}$, $0<\theta<1$.

    **MAP:** $\frac{d}{d\theta}\big[11\ln\theta+14\ln(1-\theta)\big]=\frac{11}{\theta}-\frac{14}{1-\theta}=0\Rightarrow11(1-\theta)=14\theta\Rightarrow\hat\theta=\frac{11}{25}.$

    ![prior, likelihood and posterior](img/gen/p2_beta_post.svg)

    The MLE alone would be $10/22=0.455$. The prior Beta(2,3) leans towards smaller θ (its mean is 0.4), so it pulls the estimate slightly down.

    !!! answer "Answer"
        $L(\theta)\propto\theta^{10}(1-\theta)^{12}$; posterior Beta(12, 15); $\hat\theta_{MAP}=\dfrac{11}{25}=0.44$

### June 2026 resit · 2d {#jun26-2d}

!!! exam "Resit Q4, June 2026 · 2d"
    An environmental scientist monitors the number of pollution spikes recorded per day at an air quality monitoring station on the outskirts of a city. The daily spike count is modelled as $X_i \sim \text{Poisson}(\lambda)$, where $\lambda > 0$ is the unknown average number of pollution spikes per day. The observed counts over six days are $x = \{2, 4, 3, 5, 2, 4\}$. Assume a Gamma prior on $\lambda$ with pdf $p(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}$, $\lambda > 0$, $\alpha = 3$, $\beta = 2$.

    - Write the likelihood function for $\lambda$.
    - Derive the posterior distribution for $\lambda$.
    - Find the MAP estimate for $\lambda$.
    - Compare the MAP estimate with the MLE and explain the effect of the prior.

???+ solution "Solution"
    **Likelihood.** $n=6$, $\sum x_i=2+4+3+5+2+4=20$:

    $$L(\lambda)=\prod_{i=1}^6\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{20}e^{-6\lambda}}{\prod_i x_i!}\propto\lambda^{20}e^{-6\lambda}.$$

    **Posterior** ∝ $\lambda^{20}e^{-6\lambda}\cdot\lambda^{2}e^{-2\lambda}=\lambda^{22}e^{-8\lambda}$, i.e. **Gamma($\alpha'=23$, $\beta'=8$)**.

    **MAP:** $\frac{d}{d\lambda}\big[22\ln\lambda-8\lambda\big]=\frac{22}{\lambda}-8=0\Rightarrow\hat\lambda_{MAP}=\frac{22}{8}=2.75.$

    **MLE:** $\frac{d}{d\lambda}[20\ln\lambda-6\lambda]=0\Rightarrow\hat\lambda_{ML}=\frac{20}{6}=\bar x\approx3.33.$

    ![prior, likelihood and posterior](img/gen/p2_gamma_post.svg)

    **Effect of the prior.** The prior Gamma(3, 2) has mean $\alpha/\beta=1.5$ spikes/day, lower than the data suggest. It acts like **2 extra days** ($\beta=2$) with **2 extra spikes** ($\alpha-1=2$): $\hat\lambda_{MAP}=\frac{20+2}{6+2}$. So the MAP is pulled from 3.33 towards the prior belief (shrinkage). With more days of data the prior's weight shrinks and MAP → MLE.

    !!! answer "Answer"
        Posterior Gamma(23, 8); $\hat\lambda_{MAP}=2.75$, $\hat\lambda_{ML}=3.33$; the prior pulls the estimate down towards its own mean (1.5) and its influence fades as $n$ grows.

### April 2025 exam · 2d {#apr25-2d}

!!! exam "Final exam Q3, 13 April 2025 · 2d · 1 p"
    An experiment with binary outcomes Y/N has been independently repeated $N$ times and resulted in a dataset $\mathcal{D} = \{x_1, \dots, x_N\}$ in which $x_n \in \{Y, N\}$. Let $N_0$ and $N_1$ denote the number of obtained Ns and Ys, respectively. Furthermore, let $\theta$ denote the probability of obtaining a Y whereby the posterior distribution takes the form

    $$p(\theta | \mathcal{D}) = \theta^{\beta_1 - 1 + k_1 N_1} (1 - \theta)^{\beta_0 - 1 + k_0 N_0}.$$

    Derive the MAP estimate of $\theta$.

???+ solution "Solution"
    The posterior is already given, so go straight to step 1. Call the exponents $a=\beta_1-1+k_1N_1$ and $b=\beta_0-1+k_0N_0$ to keep it readable ($k_0,k_1$ are known positive constants).

    $$\ln p(\theta\mid\mathcal D)=a\ln\theta+b\ln(1-\theta)\quad\Rightarrow\quad\frac{a}{\theta}-\frac{b}{1-\theta}=0\quad\Rightarrow\quad a(1-\theta)=b\theta.$$

    !!! answer "Answer"
        $\hat\theta_{MAP}=\dfrac{a}{a+b}=\dfrac{\beta_1-1+k_1N_1}{\beta_1+\beta_0-2+k_1N_1+k_0N_0}$

### April 2024 exam · 2d {#apr24-2d}

!!! exam "Final exam Q3, April 2024 · 2d · 1.5 p"
    Consider the posterior distribution

    $$p(\theta | x) = \frac{\lambda(\theta)}{2} e^{-\frac{\lambda(\theta)}{2}x}, \quad x > 1$$

    where $\lambda(\cdot)$ is defined as the logistic sigmoid function

    $$\lambda(\theta) = \frac{1}{1+e^{-\theta}}.$$

    Derive the MAP for the parameter $\theta$. Hint: The derivative of the logistic sigmoid is $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

???+ solution "Solution"
    Identical structure to [April 2025 2c](p2-mle.md#apr25-2c) (MLE). Solve for $\lambda$, then invert the sigmoid.

    $$\ln p=\ln\lambda-\ln2-\frac x2\lambda,\qquad\frac{\partial\ln p}{\partial\theta}=(1-\lambda)-\frac x2\lambda(1-\lambda)=(1-\lambda)\Big(1-\frac{x}{2}\lambda\Big)=0.$$

    So $\lambda(\hat\theta)=\frac2x$, and $\hat\theta=\ln\frac{\lambda}{1-\lambda}=\ln\frac{2/x}{1-2/x}=\ln\frac{2}{x-2}$.

    Valid when $\frac2x<1$, i.e. $x>2$. For $1<x\le2$ the derivative stays positive: no finite maximum.

    !!! answer "Answer"
        $\hat\theta_{MAP}=\ln\dfrac{2}{x-2}=-\ln\!\left(\dfrac x2-1\right)$, for $x>2$

### November 2022 exam · 2f, 2g {#nov22-2f}

!!! exam "Final exam Q1, 7 November 2022 · 2f, 2g · 0.5 p each"
    Assume that the parameter $\theta \geq 0$ is a random variable that admits an exponential distribution with probability density function

    $$p(\theta) = ae^{-a\theta}.$$

    The conditional probability function of the observation $x \geq 0$ depends is

    $$p(x|\theta) = \theta e^{-\theta x}.$$

    Using Bayes' theorem, the posterior distribution for the parameter $\theta$ after observing $x$ is

    $$p(\theta|x) = \begin{cases} (x+a)^2 \theta e^{-(x+a)\theta} & \theta \geq 0, \\ 0, & \text{else.} \end{cases}$$

    **2f** Find the minimum-mean square error estimator. Hint: You can use the identity

    $$\int x^2 e^{-x} dx = -e^{-x}(x^2 + 2x + 2),$$

    which is obtained by using integration by parts twice.

    **2g** Find the maximum a posteriori estimator.

???+ solution "Solution"
    **2f (MMSE = posterior mean).** Write $s=x+a$:

    $$\hat\theta_{MMSE}=\int_0^\infty\theta\cdot s^2\theta e^{-s\theta}d\theta=s^2\int_0^\infty\theta^2e^{-s\theta}d\theta=s^2\cdot\frac{2}{s^3}=\frac{2}{x+a}.$$

    (With the hint: substitute $y=s\theta$; $\int_0^\infty y^2e^{-y}dy=\big[-e^{-y}(y^2+2y+2)\big]_0^\infty=2$.)

    **2g (MAP = posterior peak).**

    $$\frac{d}{d\theta}\big[\ln\theta-s\theta\big]=\frac1\theta-s=0\Rightarrow\hat\theta_{MAP}=\frac{1}{x+a}.$$

    ![posterior with MAP and MMSE](img/gen/p2_nov22_post.svg)

    The posterior is skewed to the right, so its mean lies right of its peak: MMSE = 2 × MAP here.

    !!! answer "Answer"
        2f: $\hat\theta_{MMSE}=\dfrac{2}{x+a}$  2g: $\hat\theta_{MAP}=\dfrac{1}{x+a}$

### Q3 2022-23 exam · 2f, 2g (mixture posterior) {#q3-23-2f}

!!! exam "Exam Q3 2022-23 · 2f, 2g (shown in the Part 2 review lecture)"
    For the posterior PDF

    $$p(\theta|x) = \frac{c}{\sqrt{2\pi}}\exp\left[-\frac{1}{2}(\theta - x)^2\right] + \frac{1-c}{\sqrt{2\pi}}\exp\left[-\frac{1}{2}(\theta + x)^2\right]$$

    **2f** Find the Bayesian MMSE estimator for $\theta$, in case $c = \frac{1}{2}$ and $c = \frac{3}{4}$.

    **Hint:** *Depending the way the solution is approached, the following integral might be useful.* $\int_{-\infty}^{\infty} x e^{-a(x-b)^2} = b \sqrt{\frac{\pi}{a}}, \ \text{Re}(a) > 0.$

    **2g** Provide a sketch of $p(\theta|x)$ for $c = \frac{1}{2}$ and $c = \frac{3}{4}$. Looking at the sketch, what is the MAP estimate in the two cases? You do not need to find it analytically.

    For this exercise, we restrict our attention to $|x| > 2$.

???+ solution "Solution"
    **Read the posterior:** two unit-variance Gaussian bumps, one at $+x$ with weight $c$ and one at $-x$ with weight $1-c$.

    **2f.** The mean of a mixture is the weighted mean of the bump centres:

    $$\hat\theta_{MMSE}=c\cdot x+(1-c)(-x)=x(2c-1).$$

    $c=\frac12\Rightarrow0$; $\quad c=\frac34\Rightarrow\frac x2$.

    **2g.** With $|x|>2$ the bumps barely overlap, so the peaks sit at $\pm x$:

    ![mixture posterior](img/gen/p2_mixture.svg)

    - $c=\frac12$: two equally high peaks → MAP $=\pm x$ (not unique). The MMSE (0) lands where the posterior is almost zero.
    - $c=\frac34$: the peak at $+x$ is three times taller → MAP $\approx x$.

    !!! answer "Answer"
        MMSE: $0$ ($c=\tfrac12$), $x/2$ ($c=\tfrac34$). MAP: $\pm x$ ($c=\tfrac12$), $x$ ($c=\tfrac34$). MMSE and MAP only agree for unimodal, symmetric posteriors.

### Q3 2022-23 exam · 2g, 2h (exponential posterior) {#q3-23-2h}

!!! exam "Exam Q3 2022-23 · 2g, 2h (shown in the Part 2 review lecture)"
    Suppose we have single observation of random variable $X$ which follows the following probability distribution conditioned on $\theta$: $p(x|\theta) = \frac{1}{x} e^{-\theta x}$, for $x > 0, \theta > 0$, and suppose that $\theta$ follows an exponential prior as $p(\theta) = \frac{1}{a} e^{-a\theta}$ with $a > 0$ a known value.

    Additionally, the following known integrals are given: $\int e^{cx} dx = \frac{1}{c} e^{cx}$, $\int x e^{cx} dx = \left( \frac{cx - 1}{c^2} \right) e^{cx}$, $\int x^2 e^{cx} dx = \left( \frac{x^2}{c} - \frac{2x}{c^2} + \frac{2}{c^3} \right) e^{cx}$.

    **2g** Compute the posterior distribution $p(\theta|x)$.

    **2h** Find the Bayesian minimum mean square error estimator.

???+ solution "Solution"
    **2g.** Bayes, with the evidence as the normalising integral. Everything that does not contain $\theta$ ($\frac1x$, $\frac1a$) cancels between numerator and denominator:

    $$p(\theta\mid x)=\frac{e^{-\theta x}e^{-a\theta}}{\int_0^\infty e^{-\theta(x+a)}d\theta}=\frac{e^{-\theta(x+a)}}{1/(x+a)}=(x+a)\,e^{-\theta(x+a)},\quad\theta>0.$$

    An exponential distribution with rate $x+a$.

    **2h.** Mean of an exponential = 1/rate:

    $$\hat\theta_{MMSE}=\int_0^\infty\theta(x+a)e^{-\theta(x+a)}d\theta=(x+a)\cdot\frac{1}{(x+a)^2}=\frac{1}{x+a}.$$

    !!! answer "Answer"
        $p(\theta\mid x)=(x+a)e^{-(x+a)\theta}$ for $\theta>0$; $\ \hat\theta_{MMSE}=\dfrac{1}{x+a}$

### January 2022 resit · 2f, 2g, 2h {#jan22-2f}

!!! exam "Resit, 24 January 2022 · 2f, 2g, 2h · 0.6 p each"
    Let $Y = X + N$ where $X$, and $N$ are independent random variables. $X$ takes the values +1 and -1 with equal probability, and $N$ is a zero-mean Gaussian random variable with variance $\sigma^2$, respectively.

    ![X plus N gives Y](img/exam/jan22-2f-block.jpg)

    **2f** Evaluate the aposteriori probabilities $P[X = 1|Y]$ and $P[X = -1|Y]$.

    **2g** Find the minimum mean square error estimate $\hat{X}_{\text{MMSE}}$ of $X$ given $Y$. If you were not able to solve f) you can use $P[X = 1|Y] = \frac{1}{e^{-\frac{y}{\sigma^2}} \left( e^{\frac{y}{\sigma^2}} + e^{-\frac{y}{\sigma^2}} \right)}$ and $P[X = -1|Y] = \frac{1}{e^{\frac{y}{\sigma^2}} \left( e^{\frac{y}{\sigma^2}} + e^{-\frac{y}{\sigma^2}} \right)}$. Useful identities: $\frac{e^{2u} - 1}{e^{2u} + 1} = \frac{e^u - e^{-u}}{e^u + e^{-u}} = \tanh(u)$

    **2h** Find the maximum a posterior estimator $\hat{X}_{\text{MAP}}$ of $X$ given the observation $Y$. More specifically, find a threshold value $y_{\text{th}}$ such that a decision on $X$ depends on whether or not this threshold value is exceeded or not. *Hint:* Recall that $X$ is a discrete random variable. Hence, $\hat{X}_{\text{MAP}} = \arg \max_{X \in \{1, -1\}} P[X|Y]$. To check which value of $X$ maximizes the a posterior probability, you simply can check the ratio of the a posterior probabilities.

???+ solution "Solution"
    **Reading the diagram:** a bit $X=\pm1$ is sent, Gaussian noise is added, you see $Y$. Given $X=1$, $Y\sim\mathcal N(1,\sigma^2)$; given $X=-1$, $Y\sim\mathcal N(-1,\sigma^2)$.

    **2f.** Bayes with two hypotheses and equal priors ½ (they cancel, and so do the Gaussian constants):

    $$P[X=1\mid y]=\frac{e^{-(y-1)^2/2\sigma^2}}{e^{-(y-1)^2/2\sigma^2}+e^{-(y+1)^2/2\sigma^2}},\qquad P[X=-1\mid y]=\frac{e^{-(y+1)^2/2\sigma^2}}{e^{-(y-1)^2/2\sigma^2}+e^{-(y+1)^2/2\sigma^2}}.$$

    Since $(y+1)^2-(y-1)^2=4y$, these simplify to $P[X=1\mid y]=\frac{1}{1+e^{-2y/\sigma^2}}$ and $P[X=-1\mid y]=\frac{1}{1+e^{2y/\sigma^2}}$.

    **2g.** For a discrete variable the posterior mean is a sum:

    $$\hat X_{MMSE}=(+1)P[X=1\mid y]+(-1)P[X=-1\mid y]=\frac{e^{-(y-1)^2/2\sigma^2}-e^{-(y+1)^2/2\sigma^2}}{e^{-(y-1)^2/2\sigma^2}+e^{-(y+1)^2/2\sigma^2}}=\frac{e^{2y/\sigma^2}-1}{e^{2y/\sigma^2}+1}=\tanh\!\left(\frac{y}{\sigma^2}\right).$$

    (Divide numerator and denominator by $e^{-(y+1)^2/2\sigma^2}$.) Note: the MMSE estimate is a number between −1 and 1, usually not ±1 itself.

    **2h.** Pick the value with the larger posterior:

    $$\frac{P[X=1\mid y]}{P[X=-1\mid y]}=e^{2y/\sigma^2}\ \underset{-1}{\overset{+1}{\gtrless}}\ 1\iff y\ \underset{-1}{\overset{+1}{\gtrless}}\ 0.$$

    !!! answer "Answer"
        2f: as above (sigmoids of $2y/\sigma^2$). 2g: $\hat X_{MMSE}=\tanh(y/\sigma^2)$. 2h: $\hat X_{MAP}=+1$ if $y>0$, $-1$ if $y<0$; $y_{th}=0$.

### November 2019 exam · 3c {#nov19-3c}

!!! exam "Written exam, 4 November 2019 · Exercise 3(c) · 1 p"
    *(Same likelihood as [3a](p2-mle.md#nov19-3a): i.i.d. $p(x;\theta)=\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}$.)*

    Now consider the case where $p(\theta)$ is also a random variable with PDF $p(\theta) = \lambda \exp[-\lambda\theta]$. Find the MAP estimator for the parameter $\theta$. The answer does **not** have to be in the form $\hat{\theta} = f(x, \lambda)$.

???+ solution "Solution"
    $$\ln p(\mathbf x\mid\theta)+\ln p(\theta)=\text{const}-2N\ln\theta-\frac{1}{2\theta^2}\sum x^2[n]+\ln\lambda-\lambda\theta$$

    $$\frac{\partial}{\partial\theta}:\quad-\frac{2N}{\theta}+\frac{1}{\theta^3}\sum x^2[n]-\lambda=0\;\Longleftrightarrow\;\lambda\theta^3+2N\theta^2-\sum x^2[n]=0.$$

    A cubic: no neat closed form needed (the question says so). Sanity check: with $\lambda\to0$ (flat prior) it gives back the MLE $\theta^2=\frac{1}{2N}\sum x^2$.

    !!! answer "Answer"
        $\hat\theta_{MAP}$ is the positive root of $\lambda\theta^3+2N\theta^2-\sum_n x^2[n]=0$

### January 2019 retake · 2b, 2c {#jan19-2b}

!!! exam "Written exam, 21 January 2019 · Exercise 2(b), 2(c) · 1 p each"
    *(Same model as [2a](p2-mle.md#jan19-2a): $p(x;\lambda)=\lambda e^{-\lambda x}$.)*

    (b) Additional information regarding $\lambda$ is provided in terms of a distribution

    $$p(\lambda) = \begin{cases} \frac{1}{2} & 0 \leq \lambda \leq 2 \\ 0 & \text{otherwise} \end{cases}$$

    Treat the distribution $p(x; \lambda)$ as a conditional distribution $p(x|\lambda)$ and determine the Bayesian minimum mean square estimator (MMSE) for $\lambda$. To do so, (1) first provide the formula to calculate the Bayesian MMSE, specifying each probability distribution explicitly; [0.7 pt.] (2) then, determine the Bayesian MMSE by solving the formula obtained in b1. [0.3 pt.]

    (c) Using the same information given above, find the maximum a-posteriori (MAP) estimator for $\lambda$. [1 pt.]

    Below some useful integrals: $\int f g' dx = fg - \int f' g dx$, $\int e^{ax} dx = \frac{1}{a} e^{ax}$, $\int x e^{ax} dx = \left( \frac{x}{a} - \frac{1}{a^2} \right) e^{ax}$, $\int x^2 e^{ax} dx = \left( \frac{x^2}{a} - \frac{2x}{a^2} + \frac{2}{a^3} \right) e^{ax}$

???+ solution "Solution"
    Like the official key, use one observation $x$ (for $N$ samples replace $\lambda$ by $\lambda^N$ and $x$ by $\sum x_i$).

    **(b1) The formula.**

    $$\hat\lambda_{MMSE}=\int_0^2\lambda\,p(\lambda\mid x)\,d\lambda,\qquad p(\lambda\mid x)=\frac{\lambda e^{-\lambda x}\cdot\frac12}{\int_0^2\lambda e^{-\lambda x}\cdot\frac12\,d\lambda},\ 0\le\lambda\le2.$$

    The $\frac12$ cancels: $\hat\lambda_{MMSE}=\dfrac{\int_0^2\lambda^2e^{-\lambda x}d\lambda}{\int_0^2\lambda e^{-\lambda x}d\lambda}$.

    **(b2) The integrals** (use the given ones with $a=-x$, from 0 to 2):

    $$\int_0^2\lambda e^{-\lambda x}d\lambda=\frac{1-e^{-2x}(1+2x)}{x^2},\qquad\int_0^2\lambda^2e^{-\lambda x}d\lambda=\frac{2-e^{-2x}(4x^2+4x+2)}{x^3}.$$

    Divide:

    $$\hat\lambda_{MMSE}=\frac{2}{x}\cdot\frac{1-e^{-2x}(2x^2+2x+1)}{1-e^{-2x}(1+2x)}=\frac2x\left(1-\frac{2x^2e^{-2x}}{1-e^{-2x}(1+2x)}\right).$$

    !!! trap "Official key is off by a factor 2"
        The key prints $x^2e^{-2x}$ inside the bracket instead of $2x^2e^{-2x}$. Numerical check at $x=0.7$: the true posterior mean is 1.166; the key's formula gives 2.011, which is impossible because $\lambda\le2$.

    **(c) MAP.** Posterior ∝ $\lambda^Ne^{-\lambda\sum x_i}$ on $[0,2]$. Derivative of the log: $\frac N\lambda-\sum x_i=0\Rightarrow\lambda=\frac{N}{\sum x_i}$, the same as the MLE, because a flat prior does not change where the peak is. The prior does cut the range off at 2, so if $N/\sum x_i>2$ the maximum is at the boundary.

    !!! answer "Answer"
        (b) $\hat\lambda_{MMSE}=\dfrac2x\left(1-\dfrac{2x^2e^{-2x}}{1-e^{-2x}(1+2x)}\right)$  (c) $\hat\lambda_{MAP}=\min\!\left(\dfrac{N}{\sum_i x_i},\,2\right)$ (key: $N/\sum x_i$)

---

## Exam questions: multiple choice

### June 2026 resit · 2a {#jun26-2a}

!!! exam "Resit Q4, June 2026 · 2a · 0.5 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) The MAP estimate always equals the posterior mean.
    - (b) As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior.
    - (c) The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution.

???+ solution "Solution"
    No official key is available for this paper, so here is the reasoning.

    - (a) False: MAP = posterior **mode**, MMSE = posterior **mean**. They differ for skewed or multimodal posteriors ([Nov 2022 2f/2g](#nov22-2f)).
    - (b) The usual intuition (the likelihood dominates for large $N$) is right, but "**regardless of the choice of prior**" is too strong: a prior that is zero around the true value (e.g. uniform on $[0,2]$ when the truth is 3, like [Jan 2019 2c](#jan19-2b)) keeps the MAP away from the MLE forever.
    - (c) True by definition: $\hat\theta_{MAP}=\arg\max p(\mathbf x\mid\theta)p(\theta)$ needs $p(\theta)$.

    !!! answer "Answer"
        **(c)** (most defensible; (b) fails because of "regardless of the prior")

### April 2025 exam · 2a {#apr25-2a}

!!! exam "Final exam Q3, 13 April 2025 · 2a · 0.5 p"
    Which of the following statements is FALSE?

    - a) The MLE is the argument maximising the likelihood.
    - b) The MMSE estimate results from minimising the square error.
    - c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

???+ solution "Solution"
    (c) is false: for a Gaussian (symmetric, unimodal) posterior, mean = mode, so MMSE = MAP.

    !!! answer "Answer"
        **(c)**

### April 2024 exam · 2b {#apr24-2b}

!!! exam "Final exam Q3, April 2024 · 2b · 0.5 p"
    Which of the following statements is TRUE?

    - (a) In Bayesian estimation, the minimum mean square error is the mean of the posterior PDF.
    - (b) In Bayesian estimation, the minimum mean square error is the maximum of the posterior PDF.
    - (c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

???+ solution "Solution"
    !!! answer "Answer"
        **(a)** MMSE = posterior **mean**

### January 2022 resit · 2d {#jan22-2d}

!!! exam "Resit, 24 January 2022 · 2d · 0.3 p"
    Which of the following statements about the Bayesian estimators is true?

    - (a) The minimum mean square error is the maximum of the aposterior PDF.
    - (b) The minimum mean square error is the mean of the aposterior PDF.
    - (c) The minimum mean square error estimator and the maximum aposterior estimator will always result in a different estimate.

???+ solution "Solution"
    !!! answer "Answer"
        **(b)**

### November 2022 exam · 2c {#nov22-2c}

!!! exam "Final exam Q1, 7 November 2022 · 2c · 0.25 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) Unlike classical estimators, Bayesian estimators do not incorporate prior knowledge about the unknown parameter.
    - (b) The Bayesian estimate is the estimate that minimizes the Bayes risk, i.e., $\hat{\theta} = \arg \min_{\hat{\theta}} \int \int C(e)p(\theta|\mathbf{x})d\theta p(\mathbf{x})d\mathbf{x}$.
    - (c) Minimizing Bayes Risk for the uniform error cost function results in the minimum mean square error estimator.

???+ solution "Solution"
    (a) Backwards: incorporating a prior is exactly what makes them Bayesian. (c) Uniform cost → **MAP**; quadratic cost → MMSE.

    !!! answer "Answer"
        **(b)**
