# 2.1 Maximum likelihood (MLE)

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>1 point</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

"Here is a PDF $p(x\mid\theta)$ with an unknown number $\theta$ in it. You have samples $x_1,\dots,x_N$ (independent). **Derive the MLE of $\theta$**." It is always the same four steps; only the PDF changes.

## The idea in one minute

$\theta$ is a knob on the model. For each knob position, the model says how likely our data were. The **MLE** $\hat\theta$ is the knob position that makes **the data we actually saw** most likely.

"How likely the data were" = the product of the PDF heights at the data points (independent samples → multiply). Move the knob below: each red stick is one point's height, and the bottom curve adds up their logs.

<div class="widget" data-w="likelihood"></div>

The top of the bottom curve is where its slope is zero. That is the whole method: **write it, take the log, differentiate, set to 0**. We take the log because it turns the product into a sum (easy to differentiate) and does not move the top.

## The recipe

!!! recipe key "MLE in 4 steps"
    1. **Likelihood**: $L(\theta)=\prod_{n=1}^N p(x_n\mid\theta)$.
    2. **Log**: $\ln L(\theta)=\sum_n\ln p(x_n\mid\theta)$. Split it into simple pieces.
    3. **Differentiate** with respect to $\theta$ and set $\frac{d}{d\theta}\ln L=0$.
    4. **Solve** for $\theta$. That is $\hat\theta_{ML}$.

!!! idea "The only rules you need"
    | log rules | derivative rules (in $\theta$) |
    |---|---|
    | $\ln(ab)=\ln a+\ln b$ | $\frac{d}{d\theta}\ln\theta=\frac1\theta$ |
    | $\ln\frac ab=\ln a-\ln b$ | $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$ |
    | $\ln e^{u}=u$ | $\frac{d}{d\theta}(c\,\theta)=c$ |
    | $\ln x^k=k\ln x$ | anything without $\theta$ → 0 |
    | $\sum_n c=Nc$ | chain: $\frac{d}{d\theta}\ln f(\theta)=\frac{f'(\theta)}{f(\theta)}$ |

## Watch it once: April 2024 · 2c

!!! exam "Final exam, April 2024 · 2c · 1 p"
    For the data vector $\mathbf{x} = \{x_1, \dots, x_N\}$ consisting of independent samples with probability density function

    $$p(x_n | \theta) = \frac{x_n}{2\theta} e^{-\frac{x_n^2}{2\theta}},$$

    derive the MLE for the parameter $\theta$.

<div class="stepper" markdown>

**Step 1 · Likelihood.** $L(\theta)=\displaystyle\prod_{n=1}^N\frac{x_n}{2\theta}e^{-x_n^2/(2\theta)}$.

***

**Step 2 · Log, piece by piece.** For one sample: $\ln\frac{x_n}{2\theta}e^{-x_n^2/(2\theta)}=\ln x_n-\ln2-\ln\theta-\dfrac{x_n^2}{2\theta}$.
Sum over $n$ (constants get multiplied by $N$):

$$\ln L=\sum_n\ln x_n-N\ln2-N\ln\theta-\frac{1}{2\theta}\sum_n x_n^2.$$

***

**Step 3 · Differentiate.** First two pieces have no $\theta$ → 0. $-N\ln\theta\to-\frac N\theta$. $-\frac1{2\theta}\sum x_n^2\to+\frac{1}{2\theta^2}\sum x_n^2$ (because $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$, and minus times minus is plus).

$$-\frac N\theta+\frac{1}{2\theta^2}\sum_n x_n^2=0.$$

***

**Step 4 · Solve.** Multiply by $\theta^2$: $-N\theta+\frac12\sum x_n^2=0$, so

$$\hat\theta_{ML}=\frac{1}{2N}\sum_{n=1}^N x_n^2.$$

</div>

## Watch it once more: June 2026 · 2b

!!! exam "Resit, June 2026 · 2b · 1 p"
    Recovery times $X\sim\text{Gamma}(k,\theta)$, $k$ known, $\theta>0$ unknown, with pdf $p(x \mid \theta) = x^{k-1} e^{-x/\theta} / (\theta^k \Gamma(k))$, $x > 0$. Write the likelihood and log-likelihood for $x_1, \dots, x_n$, derive the MLE of $\theta$, and explain what it tells us.

<div class="stepper" markdown>

**Step 1–2 · Log of one sample.** $\ln p(x_i\mid\theta)=(k-1)\ln x_i-\dfrac{x_i}{\theta}-k\ln\theta-\ln\Gamma(k)$.
Sum: $\ln L=(k-1)\sum\ln x_i-\dfrac1\theta\sum x_i-nk\ln\theta-n\ln\Gamma(k)$.

***

**Step 3 · Differentiate.** $\dfrac{1}{\theta^2}\sum x_i-\dfrac{nk}{\theta}=0$.

***

**Step 4 · Solve.** Multiply by $\theta^2$: $\sum x_i-nk\theta=0$, so $\hat\theta_{ML}=\dfrac{\sum x_i}{nk}=\dfrac{\bar x}{k}$.
Meaning: a Gamma variable has mean $k\theta$, so the MLE says "average recovery time divided by the number of stages $k$".

</div>

## Your turn

!!! exam "Final exam, 13 April 2025 · 2c · 1 p"
    Consider the likelihood $p(x|\theta) = 3\lambda(\theta)e^{-4\frac{\lambda(\theta)x}{7}}, \ x > 1$, where $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$ (logistic sigmoid). Derive the MLE for $\theta$. Hint: $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

??? solution "Check your answer"
    **What is being asked?** One sample $x$ with $p(x\mid\theta)=3\lambda(\theta)e^{-\frac47\lambda(\theta)x}$ and $\lambda(\theta)=\frac{1}{1+e^{-\theta}}$ (the logistic sigmoid). Find the $\theta$ that makes this $x$ most likely.

    **Step 0 · The trick: solve for $\lambda$ first.** $\theta$ only appears through $\lambda$, and $\lambda(\theta)$ is one-to-one (it goes from 0 to 1 as $\theta$ goes from $-\infty$ to $+\infty$). So the best $\lambda$ gives the best $\theta$: the MLE is *invariant* (also in the [recipe's trap list](#traps)).

    **Step 1 · Log.** $\ln p=\ln\!\big(3\lambda e^{-\frac47\lambda x}\big)=\ln3+\ln\lambda-\frac{4x}{7}\lambda$, using $\ln(ab)=\ln a+\ln b$ and $\ln e^{u}=u$.

    **Step 2 · Differentiate in $\lambda$.** $\frac{d}{d\lambda}\ln\lambda=\frac1\lambda$, and $\frac{d}{d\lambda}\big(-\frac{4x}{7}\lambda\big)=-\frac{4x}{7}$ (a constant times $\lambda$). Set to 0:

    $$\frac1\lambda-\frac{4x}{7}=0\ \Longrightarrow\ \hat\lambda=\frac{7}{4x}.$$

    (If you differentiate in $\theta$ directly with the hint, the chain rule gives $\big(\frac1\lambda-\frac{4x}7\big)\lambda(1-\lambda)=0$: the same answer, plus the extra factor $\lambda(1-\lambda)$ which is never 0.)

    **Step 3 · Back to $\theta$.** $\dfrac{1}{1+e^{-\theta}}=\dfrac{7}{4x}$. Flip both fractions: $1+e^{-\theta}=\dfrac{4x}{7}$ → $e^{-\theta}=\dfrac{4x}{7}-1$. Take $\ln$: $-\theta=\ln\!\big(\frac{4x}{7}-1\big)$, so $\theta=-\ln\!\big(\frac{4x}{7}-1\big)$.

    **Step 4 · When is this allowed?** The $\ln$ needs a positive number: $\frac{4x}{7}-1>0$ → $x>\frac74$.

    !!! answer "Answer"
        $\hat\theta_{ML}=-\ln\!\left(\dfrac{4x}{7}-1\right)$, valid for $x>\frac74$ (the log needs a positive number).

## Traps

!!! trap key "Where points are lost"
    - Forgetting the $-N\ln\theta$ (or $-nk\ln\theta$) that comes from the $\frac1\theta$ in front. It is half of the answer.
    - Sign of $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$.
    - Writing only the final formula on a "derive" question: show all four steps, each one earns points.
    - Sigmoid questions: solve for $\lambda$ first, then $\theta=-\ln(\frac1\lambda-1)$.
