# 2.4 Estimation: the theory questions

<div class="meta"><span class="hot">In 6 of the last 6 exams</span><span>0.5 point each</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep4_quiz.mp4" poster="video/pod_ep4_quiz.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 4, Rapid-fire true or false</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [2.1 MLE](e2-mle.md) and [2.2 MAP](e2-map.md).

## What the exam asks

One multiple-choice question per paper, "which statement is TRUE / FALSE", built from the same dozen sentences. Several have appeared **word for word** two or three times. Learn the words below, then do the cards.

## The words, in one line each

| word | meaning |
|---|---|
| estimator $\hat\theta$ | a recipe that turns the data into a guess for $\theta$ |
| unbiased | on average it is right: $E[\hat\theta]=\theta$ |
| asymptotically unbiased | unbiased when $N\to\infty$ |
| consistent | gets arbitrarily close to $\theta$ as $N\to\infty$ |
| Fisher information $\mathcal I(\theta)$ | how much the data tell you about $\theta$. Always $\ge0$. For $N$ independent samples: $\mathcal I=N\,i(\theta)$ |
| CRLB (Cramér–Rao lower bound) | no unbiased estimator has variance below $\dfrac{1}{\mathcal I(\theta)}$. So it shrinks like $\frac1N$ |
| efficient | an unbiased estimator whose variance **equals** the CRLB |
| prior / posterior | belief about $\theta$ before / after seeing the data |
| MAP | top (mode) of the posterior |
| MMSE | **mean** of the posterior; minimises the mean squared error |
| Bayes risk | expected cost; Bayesian estimators **minimise** it |

<div class="key" markdown>

**The three that come back the most**

- MMSE = the **mean** of the posterior. MAP = the **maximum** of the posterior. They are equal when the posterior is symmetric with one peak (e.g. Gaussian), so they do **not** "always differ".
- Fisher information of $N$ i.i.d. samples $=N\,i(\theta)$, and the bound is $\text{Var}\ge\dfrac1{\mathcal I(\theta)}$ (one over, not $\ge\mathcal I$).
- The MLE is **asymptotically** unbiased (and asymptotically efficient, Gaussian). It does not "always" reach the CRLB.

</div>

## Test yourself

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| In Bayesian estimation, the MMSE estimate is the mean of the posterior PDF. | T | April 2024 2b, January 2022 2d. |
| In Bayesian estimation, the MMSE estimate is the maximum of the posterior PDF. | F | That is the MAP. |
| The MMSE and the MAP estimator always give a different estimate. | F | Same for a symmetric single-peak posterior (Gaussian). April 2025 2a: this was the FALSE one. |
| The MAP estimate always equals the posterior mean. | F | Only for symmetric posteriors. |
| The MAP estimate depends on both the likelihood and the prior. | T | June 2026 2a. |
| As $N$ grows, the MAP converges to the MLE regardless of the prior. | F | "Regardless" kills it: a prior that is zero at the true value can never be overruled. |
| The Fisher information of $N$ i.i.d. observations is $N\,i(\theta)$. | T | Nov 2022 2a, April 2024 2a. |
| The variance of any unbiased estimator is bounded below by the Fisher information: $\text{Var}(\hat\theta)\ge\mathcal I(\theta)$. | F | Bounded by $1/\mathcal I(\theta)$. |
| The Fisher information is strictly negative. | F | It is $\ge0$ (it is a variance / minus an expected second derivative of a peak). |
| For i.i.d. observations the CRLB decreases with the number of observations. | T | It is $\frac{1}{N\,i(\theta)}$. January 2022 2a. |
| The CRLB can always be derived. | F | Not when the range of $x$ depends on $\theta$ (e.g. $0\le x\le\theta$): January 2022 2e. |
| An estimator whose variance is lower than the CRLB is called efficient. | F | Efficient = variance **equal to** the CRLB. Lower is impossible for unbiased estimators. |
| The MLE is asymptotically unbiased. | T | Nov 2022 2b. |
| The MLE always achieves the CRLB. | F | Only asymptotically ($N\to\infty$). |
| The MLE can only be found for linear signal models. | F | It works for any model you can write a likelihood for. |
| If $\alpha=\psi(\theta)$ is one-to-one, then $\hat\theta_{ML}=\psi^{-1}(\hat\alpha_{ML})$. | T | Invariance of the MLE. January 2022 2b. You used it in the sigmoid question. |
| The MLE is the argument that maximises the likelihood. | T | Definition. (Not "the value of $x$" that maximises it: it is a value of $\theta$.) |
| Bayesian estimators minimise the Bayes risk. | T | Nov 2022 2c. |
| Bayesian estimators, unlike classical ones, do not use prior knowledge. | F | The prior is exactly what makes them Bayesian. |

</div>

## If they ask you to compute the CRLB

Rare since 2022, but the recipe is short:

!!! recipe "CRLB in 3 steps"
    1. Log of one sample: $\ln p(x\mid\theta)$.
    2. Second derivative in $\theta$, then take minus its expected value: $i(\theta)=-E\big[\frac{\partial^2}{\partial\theta^2}\ln p(x\mid\theta)\big]$.
    3. $\text{CRLB}=\dfrac{1}{N\,i(\theta)}$. First check that the range of $x$ does not depend on $\theta$; if it does, say "not possible".
