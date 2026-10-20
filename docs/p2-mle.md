# 2.1 Maximum likelihood (MLE)

<p class="lead">"Derive the MLE" is in almost every exam and is worth 0.5–1 p each time. It is always the same four steps. The only things that change are the PDF and the algebra at the end.</p>

## The idea, from zero

**Estimation** = guessing an unknown number $\theta$ (a mean, a rate, an angle) from noisy data $x_1,\dots,x_N$. An **estimator** $\hat\theta=g(x_1,\dots,x_N)$ is a recipe that turns data into a guess. Because the data is random, $\hat\theta$ is a random variable too, so it has:

- a **bias** $E[\hat\theta]-\theta$ (is it right on average?). *Unbiased* means bias = 0. *Asymptotically unbiased*: bias → 0 as $N\to\infty$.
- a **variance** $\operatorname{Var}[\hat\theta]$ (how much it jumps around). *Consistent*: it converges to the true $\theta$ as $N\to\infty$.

**The likelihood.** Take the PDF of the data, $p(\mathbf x;\theta)$, plug in the numbers you actually observed, and read it as a function of $\theta$. That is the likelihood $L(\theta)$. It says how well each candidate $\theta$ explains what you saw. The **maximum likelihood estimate** is the $\theta$ that explains the data best:

$$\hat\theta_{ML}=\arg\max_\theta\ p(\mathbf x;\theta).$$

For independent samples the joint PDF is a product, and the log turns it into a sum:

$$\ln L(\theta)=\sum_{n=1}^N\ln p(x_n;\theta).$$

<figure markdown>
![Likelihood and log-likelihood peak at the same place](img/gen/p2_mle_idea.svg)
<figcaption>Likelihood (left) and log-likelihood (right) for 12 Gamma samples. The log changes the shape but not the location of the peak, and the peak is the MLE.</figcaption>
</figure>

!!! recipe "Recipe: MLE in 4 steps (+1 check)"
    1. **Likelihood**: $L(\theta)=\prod_n p(x_n;\theta)$ (independent samples).
    2. **Log**: $\ln L=\sum_n\ln p(x_n;\theta)$. Expand with $\ln(ab)=\ln a+\ln b$, $\ln e^u=u$. Terms without $\theta$ can be dropped.
    3. **Differentiate** with respect to $\theta$.
    4. **Set to 0 and solve** for $\theta$. Put a hat on it.
    5. *(Check)* second derivative < 0 at the solution → maximum. Mention it in one line.

**Properties you get asked about (MC):**

- MLE is **asymptotically unbiased**, **asymptotically efficient** (variance → CRLB) and **asymptotically Gaussian**: $\hat\theta\sim\mathcal N(\theta,\mathcal I^{-1}(\theta))$ for large $N$.
- If an efficient estimator exists, the MLE finds it.
- It does **not** always reach the CRLB for finite $N$, and it is **not** limited to linear models.
- **Invariance:** the MLE of $\alpha=g(\theta)$ is $g(\hat\theta_{ML})$. So you can estimate a convenient parameter and transform back.

!!! trap "Traps"
    - The MLE maximises over the **parameter** $\theta$, not over the data $x$.
    - Normalising constants that do not contain $\theta$ (like $\Gamma(k)$, $\binom{x-1}{k-1}$) disappear when you differentiate. Do not waste time on them.
    - Constants that **do** contain $\theta$ (like $1/\theta^k$, $\lambda(\theta)$) must stay in.

---

## Exam questions: derivations

### June 2026 resit · 2b {#jun26-2b}

!!! exam "Resit Q4, June 2026 · 2b · 1 p"
    A hospital administrator records the recovery time $X$ (in days) for patients following a routine surgical procedure. Recovery times are modelled as

    $$X \sim \text{Gamma}(k, \theta),$$

    where $k > 0$ is a *known* shape parameter and $\theta > 0$ is the unknown scale parameter (average recovery contribution per stage). The Gamma pdf is

    $$p(x \mid \theta) = x^{k-1} e^{-x/\theta} / (\theta^k \Gamma(k)), \quad x > 0.$$

    - Write the likelihood and log-likelihood functions for $\theta$ given observations $x_1, \dots, x_n$.
    - Derive the maximum likelihood estimator (MLE) for $\theta$.
    - Explain what the MLE tells us about patient recovery at the hospital.

???+ solution "Solution"
    **1. Likelihood** (independent patients):

    $$L(\theta)=\prod_{i=1}^n\frac{x_i^{k-1}e^{-x_i/\theta}}{\theta^k\Gamma(k)}=\frac{\left(\prod_i x_i\right)^{k-1}}{\Gamma(k)^n}\;\theta^{-nk}\;e^{-\frac1\theta\sum_i x_i}.$$

    **2. Log-likelihood:**

    $$\ln L(\theta)=(k-1)\sum_i\ln x_i-n\ln\Gamma(k)-nk\ln\theta-\frac1\theta\sum_i x_i.$$

    **3. Derivative** (only the last two terms contain $\theta$):

    $$\frac{\partial\ln L}{\partial\theta}=-\frac{nk}{\theta}+\frac{1}{\theta^2}\sum_i x_i.$$

    **4. Set to 0:** multiply by $\theta^2$: $-nk\theta+\sum_ix_i=0$, so

    $$\hat\theta_{ML}=\frac{1}{nk}\sum_{i=1}^n x_i=\frac{\bar x}{k}.$$

    **Check:** $\frac{\partial^2\ln L}{\partial\theta^2}=\frac{nk}{\theta^2}-\frac{2\sum x_i}{\theta^3}$; at $\hat\theta$ this is $\frac{nk}{\hat\theta^2}-\frac{2nk}{\hat\theta^2}=-\frac{nk}{\hat\theta^2}<0$ → maximum.

    **Interpretation.** A Gamma($k,\theta$) variable is like $k$ consecutive stages, each lasting on average $\theta$ days, so the mean recovery time is $E[X]=k\theta$. The MLE sets $k\hat\theta=\bar x$: the fitted model reproduces the **observed average recovery time**, and $\hat\theta=\bar x/k$ is the estimated average number of days each recovery stage takes at this hospital. A larger $\hat\theta$ means slower recovery. (The estimate is unbiased, since $E[\bar x]=k\theta$, and gets more precise as more patients are recorded.)

    !!! answer "Answer"
        $\hat\theta_{ML}=\dfrac{1}{nk}\displaystyle\sum_{i=1}^n x_i=\dfrac{\bar x}{k}$ (mean recovery time divided by the number of stages)

### April 2025 exam · 2c {#apr25-2c}

!!! exam "Final exam Q3, 13 April 2025 · 2c · 1 p"
    Consider the likelihood

    $$p(x|\theta) = 3\lambda(\theta)e^{-4\frac{\lambda(\theta)x}{7}}, \quad x > 1$$

    where $\lambda(\cdot)$ is defined as the logistic sigmoid function

    $$\lambda(\theta) = \frac{1}{1+e^{-\theta}}.$$

    Derive the MLE for the parameter $\theta$. Hint: The derivative of the logistic sigmoid is $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

???+ solution "Solution"
    **Think first.** $\theta$ only enters through $\lambda$. So the plan: get an equation for $\lambda$, solve it, then convert back to $\theta$ with the inverse sigmoid $\theta=\ln\frac{\lambda}{1-\lambda}$.

    **Log:** $\ln p=\ln3+\ln\lambda(\theta)-\frac47\lambda(\theta)x$.

    **Derivative** (chain rule, $\lambda'=\lambda(1-\lambda)$):

    $$\frac{\partial\ln p}{\partial\theta}=\frac{\lambda'}{\lambda}-\frac47x\lambda'=(1-\lambda)-\frac47x\lambda(1-\lambda)=(1-\lambda)\Big(1-\frac47x\lambda\Big).$$

    **Set to 0.** $1-\lambda=0$ would need $\theta\to\infty$, so the stationary point is

    $$\lambda(\hat\theta)=\frac{7}{4x}.$$

    **Back to $\theta$:** $\frac{\lambda}{1-\lambda}=\frac{7/(4x)}{1-7/(4x)}=\frac{7}{4x-7}$, so

    $$\hat\theta_{ML}=\ln\frac{7}{4x-7}=-\ln\!\left(\frac{4x}{7}-1\right).$$

    **When does it exist?** A sigmoid is always between 0 and 1, so we need $\frac7{4x}<1$, i.e. $x>\frac74$. For $1<x\le\frac74$ the derivative is positive everywhere and the likelihood keeps increasing ($\hat\theta\to\infty$), as the orange curve shows:

    ![log-likelihood vs theta](img/gen/p2_sigmoid.svg)

    !!! answer "Answer"
        $\hat\theta_{ML}=-\ln\!\left(\dfrac{4x}{7}-1\right)$, valid for $x>7/4$

### April 2024 exam · 2c {#apr24-2c}

!!! exam "Final exam Q3, April 2024 · 2c"
    For the data vector $\mathbf{x} = \{x_1, \dots, x_N\}$ consisting of independent samples with probability density function

    $$p(x_n | \theta) = \frac{x_n}{2\theta} e^{-\frac{x_n^2}{2\theta}},$$

    derive the MLE for the parameter $\theta$.

???+ solution "Solution"
    $$\ln L(\theta)=\sum_n\ln x_n-N\ln(2\theta)-\frac{1}{2\theta}\sum_n x_n^2$$

    $$\frac{\partial\ln L}{\partial\theta}=-\frac N\theta+\frac{1}{2\theta^2}\sum_n x_n^2=0\quad\Rightarrow\quad\hat\theta=\frac{1}{2N}\sum_{n=1}^N x_n^2.$$

    ($\ln(2\theta)=\ln2+\ln\theta$, so its derivative is $1/\theta$.) Second derivative at $\hat\theta$: $\frac{N}{\hat\theta^2}-\frac{2N}{\hat\theta^2}<0$ ✓.

    !!! answer "Answer"
        $\hat\theta_{ML}=\dfrac{1}{2N}\displaystyle\sum_{n=1}^N x_n^2$

### January 2025 resit · 2b {#jan25-2b}

!!! exam "Resit January 2025 · 2b · 1 p (shown in the Part 2 review lecture)"
    Assume that

    $$p(\mu, \sigma, \theta | \rho) = \frac{1}{2\pi(1-\theta^2)^{1/2}} \exp\left(-\frac{\mu^2\rho^2 - 2\rho\mu\sigma\theta + \sigma^2\rho^2}{2(1-\theta^2)}\right)$$

    Determine the maximum likelihood estimate of $\rho$ for a single observation of $\mu, \sigma, \theta$.

    *Note: $\rho$ is the unknown parameter here; $\mu, \sigma, \theta$ are the observed data (a single realization of each).*

???+ solution "Solution"
    **Don't be thrown by the letters.** Here $\mu,\sigma,\theta$ are just *numbers you observed*, and $\rho$ is the unknown. Same 4 steps.

    $$\ln p=-\ln(2\pi)-\tfrac12\ln(1-\theta^2)-\frac{(\mu^2+\sigma^2)\rho^2-2\mu\sigma\theta\rho}{2(1-\theta^2)}$$

    $$\frac{\partial\ln p}{\partial\rho}=-\frac{2(\mu^2+\sigma^2)\rho-2\mu\sigma\theta}{2(1-\theta^2)}=0\quad\Rightarrow\quad\hat\rho=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}.$$

    Second derivative $-\frac{\mu^2+\sigma^2}{1-\theta^2}<0$ when $|\theta|<1$ (needed anyway for the PDF to exist) → maximum.

    !!! answer "Answer"
        $\hat\rho_{ML}=\dfrac{\mu\sigma\theta}{\mu^2+\sigma^2}$

### Q1 2023 resit · 2b {#q1-23-2b}

!!! exam "Resit Q1 2023 · 2b (shown in the Part 2 review lecture)"
    For the data vector $\mathbf{x} = \{x_1, \dots x_N\}$ consisting of independent samples with probability density function

    $$p(\mathbf{x} | \theta) = \prod_{n=1}^N \frac{x_n}{\theta} e^{-\frac{x_n^2}{\theta}},$$

    derive the MLE for the parameter $\theta$.

???+ solution "Solution"
    $$\ln L=\sum_n\ln x_n-N\ln\theta-\frac1\theta\sum_nx_n^2,\qquad\frac{\partial\ln L}{\partial\theta}=-\frac N\theta+\frac{1}{\theta^2}\sum_nx_n^2=0$$

    $$\hat\theta=\frac1N\sum_{n=1}^Nx_n^2.$$

    Compare with April 2024: the only difference is the factor 2 in the exponent, and it shows up as the factor 2 in the answer.

    !!! answer "Answer"
        $\hat\theta_{ML}=\dfrac1N\displaystyle\sum_{n=1}^N x_n^2$

### November 2022 exam · 2d {#nov22-2d}

!!! exam "Final exam Q1, 7 November 2022 · 2d · 0.5 p"
    Consider the observation

    $$\mathbf{x} = A \begin{bmatrix} \cos(\theta) \\ \sin(\theta) \end{bmatrix} + \mathbf{w},$$

    where $\mathbf{w}$ is white Gaussian noise. The probability density function of the observation is

    $$p(\mathbf{x}; \theta) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{1}{2\sigma^2} \left((x_1 - A \cos(\theta))^2 + (x_2 - A \sin(\theta))^2\right)\right)$$

    Find the maximum likelihood estimator of the parameter $\theta$.

???+ solution "Solution"
    **Picture it:** the true point sits on a circle of radius $A$ at angle $\theta$; noise moves it a bit. The best guess for the angle should be the angle of the observed point.

    $$\ln p=-\ln(2\pi\sigma^2)-\frac{1}{2\sigma^2}\Big(x_1^2+x_2^2-2A(x_1\cos\theta+x_2\sin\theta)+A^2\underbrace{(\cos^2\theta+\sin^2\theta)}_{=1}\Big)$$

    $$\frac{\partial\ln p}{\partial\theta}=\frac{A}{\sigma^2}\big(-x_1\sin\theta+x_2\cos\theta\big)=0\;\Rightarrow\;\tan\theta=\frac{x_2}{x_1}.$$

    So $\hat\theta=\tan^{-1}(x_2/x_1)$, taken **in the quadrant of the point $(x_1,x_2)$** (the other solution, $+\pi$, is the minimum of the likelihood).

    !!! answer "Answer"
        $\hat\theta_{ML}=\tan^{-1}\!\left(\dfrac{x_2}{x_1}\right)$ (the angle of the observed vector)

### Practice exam 2021 · 2b {#pe21-2b}

!!! exam "Practice exam, 28 October 2021 · 2b · 1 p"
    For the data vector $\mathbf{x}$ consisting of independent samples with probability density function $p(x[n]) = \frac{x}{\theta} \exp\left(-\frac{x^2}{2\theta}\right)$, where $n = 0, 1, \dots, N-1$, find an estimator for the parameter $\theta$.

???+ solution "Solution"
    "Find an estimator" → use the MLE.

    $$\ln L=\sum\ln x[n]-N\ln\theta-\frac{1}{2\theta}\sum x^2[n],\qquad\frac{\partial\ln L}{\partial\theta}=-\frac N\theta+\frac{1}{2\theta^2}\sum x^2[n]=0$$

    !!! answer "Answer"
        $\hat\theta=\dfrac{1}{2N}\displaystyle\sum_{n=0}^{N-1}x^2[n]$

### November 2019 exam · 3a {#nov19-3a}

!!! exam "Written exam, 4 November 2019 · Exercise 3(a) · 1 p"
    The data $x[0], x[1], \dots, x[N-1]$ are observed, where $x[n]$'s are independent and identically distributed according to the PDF

    $$p(x; \theta) = \frac{x}{\theta^2} \exp \left[ -\frac{x^2}{2\theta^2} \right], \quad x \geq 0.$$

    (a) Find the maximum likelihood estimator for the parameter $\theta$.

???+ solution "Solution"
    Same Rayleigh family, but now the parameter is squared inside.

    $$\ln L=\sum\ln x[n]-2N\ln\theta-\frac{1}{2\theta^2}\sum x^2[n],\qquad\frac{\partial\ln L}{\partial\theta}=-\frac{2N}{\theta}+\frac{1}{\theta^3}\sum x^2[n]=0$$

    So $\theta^2=\frac{1}{2N}\sum x^2[n]$. (By invariance this is the square root of the previous answer, as expected.)

    !!! answer "Answer"
        $\hat\theta_{ML}=\sqrt{\dfrac{1}{2N}\displaystyle\sum_{n=0}^{N-1}x^2[n]}$

### January 2019 retake · 2a {#jan19-2a}

!!! exam "Written exam, 21 January 2019 · Exercise 2(a) · 1 p"
    For the random variable $x$ with distribution

    $$p(x; \lambda) = \lambda e^{-\lambda x}$$

    find the maximum likelihood estimator for $\lambda$, given $N$ independent identically distributed observations $x_i, i \in \{0 : N - 1\}$.

???+ solution "Solution"
    $$\ln L=N\ln\lambda-\lambda\sum_ix_i,\qquad\frac{\partial\ln L}{\partial\lambda}=\frac N\lambda-\sum_ix_i=0$$

    Makes sense: the mean of an exponential is $1/\lambda$, so $\hat\lambda=1/\bar x$.

    !!! answer "Answer"
        $\hat\lambda_{ML}=\dfrac{N}{\sum_i x_i}=\dfrac1{\bar x}$

---

## Exam questions: multiple choice

### November 2022 exam · 2b {#nov22-2b}

!!! exam "Final exam Q1, 7 November 2022 · 2b · 0.25 p"
    Which of the following statements about the maximum likelihood estimator is TRUE?

    - (a) The maximum likelihood estimator always achieves the Cramér-Rao lower bound.
    - (b) The maximum likelihood estimator can only be found for special estimation problems, such as linear signal models.
    - (c) The maximum likelihood estimator is asymptotically unbiased.

???+ solution "Solution"
    (a) only **asymptotically** (or when an efficient estimator exists). (b) the MLE works for any model you can write a PDF for.

    !!! answer "Answer"
        **(c)**

### January 2022 resit · 2b {#jan22-2b}

!!! exam "Resit, 24 January 2022 · 2b · 0.3 p"
    Which of the following statements about the maximum likelihood estimator is true?

    - (a) The maximum likelihood estimate is the value of $x$ that maximizes the likelihood function.
    - (b) For large sample sizes, the maximum likelihood estimate is uniformly distributed, i.e., $\hat{\theta}_{ML} \sim \text{Uniform}(-a, a)$ where $a = \mathcal{I}^{-1}(\theta)$.
    - (c) For a transformed parameter $\alpha = \psi(\theta)$, where $\psi(\cdot)$ is a one-to-one mapping, the maximum likelihood estimate $\hat{\theta}_{ML}$ can be obtained as $\hat{\theta}_{ML} = \psi^{-1}(\hat{\alpha}_{ML})$ where $\psi^{-1}(\cdot)$ is the inverse mapping of $\psi(\cdot)$ and $\hat{\alpha}_{ML}$ is the maximum likelihood estimate of the transformed parameter $\alpha$, respectively.

???+ solution "Solution"
    (a) maximises over the **parameter**, not over $x$. (b) asymptotically it is **Gaussian**, $\mathcal N(\theta,\mathcal I^{-1}(\theta))$. (c) is the invariance property.

    !!! answer "Answer"
        **(c)**

### January 2019 retake · 1b {#jan19-1b}

!!! exam "Written exam, 21 January 2019 · Exercise 1(b) · 0.5 p"
    Which expression describes the maximum likelihood estimator?

    - A. $\hat{\theta} = \arg \min_{\theta} \sum_{n=1}^N (x[n] - s[n; \theta])^2$
    - B. $\hat{\theta} = \arg \min_{\hat{\theta}} \int (\hat{\theta} - \theta)^2 p(x|\theta) dx$
    - C. $\hat{\theta} = \arg \max_{\theta} p(\theta|x)$
    - D. $\hat{\theta} = \arg \max_{\theta} p(x|\theta)$

???+ solution "Solution"
    A is **least squares**, B is a squared-error (MMSE-type) criterion, C maximises the **posterior** (MAP). The MLE maximises the **likelihood** $p(x\mid\theta)$.

    !!! answer "Answer"
        **D**
