# 2.2 CRLB & Fisher information

<p class="lead">The Cramér–Rao lower bound says how good <em>any</em> unbiased estimator can possibly be. Exams ask three things: a multiple choice on the definitions (this one repeats almost word for word), "compute the Fisher information / CRLB", and "can you even compute the CRLB here?" (no, if the support depends on θ).</p>

## The idea, from zero

Some data are more informative about $\theta$ than others. If the log-likelihood is a **sharp peak**, a small change in $\theta$ makes the data much less likely, so the data pins $\theta$ down well. If it is **flat**, many values of $\theta$ explain the data equally well. The **Fisher information** measures that sharpness (the curvature of the log-likelihood):

$$\mathcal I(\theta)=-E\!\left[\frac{\partial^2\ln p(\mathbf x;\theta)}{\partial\theta^2}\right]=E\!\left[\left(\frac{\partial\ln p(\mathbf x;\theta)}{\partial\theta}\right)^2\right]\ \ (>0).$$

**Cramér–Rao lower bound.** For every unbiased estimator,

$$\operatorname{Var}[\hat\theta]\ \ge\ \frac{1}{\mathcal I(\theta)}.$$

More information → smaller bound. Facts that get tested:

- For $N$ i.i.d. observations, $\mathcal I(\theta)=N\,i(\theta)$, with $i(\theta)$ the information of a single observation. So the bound $\frac{1}{N\,i(\theta)}$ **decreases as $1/N$**.
- The bound is the **reciprocal** of the information, not the information itself.
- An unbiased estimator whose variance **equals** the bound is **efficient**. Nothing unbiased can go below it.
- Equality holds iff the score can be written as $\frac{\partial\ln p}{\partial\theta}=\mathcal I(\theta)\,\big(g(\mathbf x)-\theta\big)$; then $g(\mathbf x)$ is the efficient estimator.
- **Regularity condition:** the theorem needs $E\!\left[\frac{\partial\ln p}{\partial\theta}\right]=0$, i.e. you can swap $\frac{d}{d\theta}$ and $\int dx$. This **fails when the support of $p(x;\theta)$ depends on $\theta$** (e.g. $0\le x\le\theta$). Then the CRLB cannot be derived.

!!! recipe "Recipe: compute the CRLB"
    1. Log-likelihood $\ln p(\mathbf x;\theta)$ (sum over samples).
    2. Differentiate **twice** with respect to $\theta$.
    3. Take the expected value: replace every data term by its mean ($E[x_n]$, $E[x_n^2]$, …). The exam often gives these as a hint.
    4. $\mathcal I(\theta)=-E[\cdot]$, $\ \text{CRLB}=1/\mathcal I(\theta)$.

---

## Exam questions: computations

### November 2022 exam · 2e {#nov22-2e}

!!! exam "Final exam Q1, 7 November 2022 · 2e · 0.5 p"
    *(Same model as [2d](p2-mle.md#nov22-2d): $\mathbf x=A[\cos\theta,\ \sin\theta]^T+\mathbf w$, white Gaussian noise with variance $\sigma^2$.)*

    Derive the Fisher information $\mathcal{I}(\theta)$. **Hint:** The expected values of $x_1$ and $x_2$ are $A \cos(\theta)$ and $A \sin(\theta)$, respectively.

???+ solution "Solution"
    From 2d: $\frac{\partial\ln p}{\partial\theta}=\frac{A}{\sigma^2}(-x_1\sin\theta+x_2\cos\theta)$. Differentiate again:

    $$\frac{\partial^2\ln p}{\partial\theta^2}=\frac{A}{\sigma^2}(-x_1\cos\theta-x_2\sin\theta).$$

    Expected value with the hint:

    $$\mathcal I(\theta)=-E[\cdot]=\frac{A}{\sigma^2}\big(A\cos^2\theta+A\sin^2\theta\big)=\frac{A^2}{\sigma^2}.$$

    Interpretation: the angle is easier to estimate when the circle is big ($A$) compared to the noise ($\sigma$). The CRLB is $\sigma^2/A^2$.

    !!! answer "Answer"
        $\mathcal I(\theta)=\dfrac{A^2}{\sigma^2}$

### November 2019 exam · 3b {#nov19-3b}

!!! exam "Written exam, 4 November 2019 · Exercise 3(b) · 1 p"
    *(Same model as [3a](p2-mle.md#nov19-3a): i.i.d. $p(x;\theta)=\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}$, $x\ge0$.)*

    (b) Find the Cramer-Rao Lower Bound for the MLE.

???+ solution "Solution"
    From 3a: $\frac{\partial\ln L}{\partial\theta}=-\frac{2N}{\theta}+\frac{1}{\theta^3}\sum x^2[n]$.

    $$\frac{\partial^2\ln L}{\partial\theta^2}=\frac{2N}{\theta^2}-\frac{3}{\theta^4}\sum x^2[n].$$

    For this (Rayleigh) PDF $E[x^2]=2\theta^2$ (toolbox table), so

    $$E\!\left[\frac{\partial^2\ln L}{\partial\theta^2}\right]=\frac{2N}{\theta^2}-\frac{3N\cdot2\theta^2}{\theta^4}=-\frac{4N}{\theta^2}\quad\Rightarrow\quad\mathcal I(\theta)=\frac{4N}{\theta^2}.$$

    (If you don't remember $E[x^2]$: $\int_0^\infty x^2\frac{x}{\theta^2}e^{-x^2/2\theta^2}dx=2\theta^2$ with the substitution $u=x^2/2\theta^2$.)

    !!! answer "Answer"
        $\operatorname{Var}(\hat\theta)\ge\dfrac{\theta^2}{4N}$ (the key writes $\hat\theta^2/4N$, i.e. the bound evaluated at the estimate)

### Practice exam 2021 · 2a {#pe21-2a}

!!! exam "Practice exam, 28 October 2021 · 2a · 1 p"
    Given the minimum variance unbiased estimator (MVUE) $\hat{\theta} = \sum_{n=0}^{N-1} x[n]/N$ with variance $\sigma_{\hat{\theta}}^2 = A^2/N$, find the probability density function (PDF) $p(\mathbf{x}; \theta)$ for the data vector $\mathbf{x}$ that consists of data points $x[n]$, $n \in \{0, 1, \dots, N-1\}$. Use the MVUE condition and show the derivation of the PDF. Assume independent identically distributed noise samples act on the signal model that generates the data samples.

    **Hint:** Use this trick if needed: $\int (x+a)dx = x^2/2 + ax + b$ and $b$ can be chosen as $b = a^2/2$ to obtain $\int (x+a)dx = 0.5(x+a)^2$.

???+ solution "Solution"
    **Think first.** This is the CRLB run backwards. The estimator is efficient (it reaches the bound), so its variance *is* $1/\mathcal I$, and the score must have the equality form. Integrate the score and you get the log-PDF.

    1. Efficient ⇒ $\operatorname{Var}=1/\mathcal I(\theta)$ ⇒ $\mathcal I(\theta)=\frac{N}{A^2}$.
    2. Equality condition with $g(\mathbf x)=\bar x$:

        $$\frac{\partial\ln p}{\partial\theta}=\frac{N}{A^2}(\bar x-\theta)=\frac{1}{A^2}\sum_{n=0}^{N-1}\big(x[n]-\theta\big).$$

    3. Integrate over $\theta$ (hint: $\int(x[n]-\theta)\,d\theta=-\frac12(x[n]-\theta)^2+\text{const}$):

        $$\ln p(\mathbf x;\theta)=-\frac{1}{2A^2}\sum_{n=0}^{N-1}(x[n]-\theta)^2+C.$$

    4. Exponentiate and choose the constant so that it integrates to 1 (it is a product of $N$ Gaussians):

        $$p(\mathbf x;\theta)=\frac{1}{(2\pi A^2)^{N/2}}\exp\!\left(-\frac{1}{2A^2}\sum_{n=0}^{N-1}(x[n]-\theta)^2\right).$$

    So the data model is $x[n]=\theta+w[n]$ with $w[n]$ i.i.d. $\mathcal N(0,A^2)$: a constant in white Gaussian noise.

    !!! answer "Answer"
        $p(\mathbf x;\theta)=(2\pi A^2)^{-N/2}\exp\!\left(-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2\right)$

### January 2022 resit · 2e {#jan22-2e}

!!! exam "Resit, 24 January 2022 · 2e · 0.5 p"
    Let

    $$p(x; \theta) = \begin{cases} \frac{2}{\theta}x, & \text{for } 0 \leq x \leq \theta, \\ 0, & \text{else} \end{cases}$$

    be the probability density function of an observation $X$. Check whether or not it is possible to derive the Cramer Rao lower bound. In case it is possible, derive the Cramer Rao lower bound. If it is not possible, justify why.

???+ solution "Solution"
    **Look at the support first:** $0\le x\le\theta$. The range of $x$ depends on $\theta$, which is exactly the case where the regularity condition fails.

    (The official clarification corrects the PDF to $\frac{2}{\theta^2}x$, so that it integrates to 1.) Check:

    - $\frac{d}{d\theta}\int_0^\theta p\,dx=\frac{d}{d\theta}1=0$,
    - $\int_0^\theta\frac{\partial p}{\partial\theta}dx=\int_0^\theta-\frac{4x}{\theta^3}dx=-\frac2\theta\ne0$.

    Differentiation and integration cannot be swapped (by Leibniz's rule the moving upper limit adds a boundary term), so $E[\partial\ln p/\partial\theta]\neq0$.

    !!! answer "Answer"
        **Not possible:** the support depends on $\theta$, so the regularity condition is violated and the CRLB does not apply.

---

## Exam questions: multiple choice

### November 2022 exam · 2a {#nov22-2a}

!!! exam "Final exam Q1, 7 November 2022 · 2a · 0.25 p"
    Which of the following statements about the Fisher information $\mathcal{I}(\theta)$ is TRUE?

    - (a) The Fisher information for $N$ identical and independent distributed observations is $Ni(\theta)$, where $i(\theta)$ is the Fisher information for a single observation.
    - (b) The variance of any unbiased estimator is lower bounded by the Fisher information, i.e., $\text{Var}(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - (c) The Fisher information $\mathcal{I}(\theta)$ is strictly negative.

???+ solution "Solution"
    (b) the bound is $1/\mathcal I$. (c) it is the expected *square* of the score, so it is positive.

    !!! answer "Answer"
        **(a)**

### April 2024 exam · 2a {#apr24-2a}

!!! exam "Final exam Q3, April 2024 · 2a · 0.5 p"
    Which of the following statements is TRUE?

    - a) The variance of any unbiased estimator is lower bounded by the Fisher information, i.e., $Var(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - b) The Fisher information is strictly negative.
    - c) The Fisher information for $N$ identical and independently distributed observations is $N i(\theta)$, where $i(\theta)$ is the Fisher information for a single observation.

???+ solution "Solution"
    Same three statements as Nov 2022, shuffled.

    !!! answer "Answer"
        **(c)**

### Q1 2023 resit · 2a {#q1-23-2a}

!!! exam "Resit Q1 2023 · 2a (shown in the Part 2 review lecture)"
    Which of the following statements is FALSE? (exactly one)

    - (a) The Fisher information for $N$ i.i.d. observations is $N \cdot i(\theta)$, where $i(\theta)$ is the Fisher information for a single observation.
    - (b) The variance of any unbiased estimator satisfies $\text{Var}(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - (c) The Fisher information is strictly positive.

???+ solution "Solution"
    Same family, but now asking for the **false** one. Read the question word!

    !!! answer "Answer"
        **(b)** (the bound is $1/\mathcal I(\theta)$)

### January 2022 resit · 2a {#jan22-2a}

!!! exam "Resit, 24 January 2022 · 2a · 0.3 p"
    Which of the following statements about the Cramer Rao lower bound is true?

    - (a) The Cramer Rao lower bound can always be derived.
    - (b) For identical and independent distributed observations, the Cramer Rao lower bound decreases linearly with the number of observations.
    - (c) An estimator whose variance is lower than the Cramer Rao lower bound is called efficient.

???+ solution "Solution"
    (a) Only when the regularity conditions hold (see 2e). (b) $\text{CRLB}=\frac{1}{N\,i(\theta)}$ shrinks as $1/N$, which the key calls "decreases linearly". (c) Efficient = variance **equal** to the bound; below it is impossible.

    !!! answer "Answer"
        **(b)**
