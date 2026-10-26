---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet (v4 — beginner worked edition)</h1>

<p class="noprint">Complete exam coverage with expanded calculations. Print the supplied PDF at 100 %, one A4 sheet, both sides.</p>
<div class="cheat cheat4" markdown>
<div class="cheat-cols" markdown>

**START HERE · read the maths.** $\int_a^b f(x)\,dx$: only $x$ changes, from $a$ to $b$; every other letter is temporarily constant. Integrate to $F(x)$, then calculate $[F(x)]_a^b=F(b)-F(a)$ (**upper minus lower**). In $\int_c^d[\int_{a(y)}^{b(y)}f(x,y)\,dx]dy$, do the bracketed **inner $x$-integral first**, substitute its limits, then do the **outer $y$-integral**. $\sum_{n=1}^N$ = add the $N$ terms · $\prod$ = multiply them · $\bar x=\frac1N\sum x_n$ · $\propto$ = “equal apart from a constant”.
{: .how }

**Symbols.** $\theta$ = unknown parameter · $\hat\theta$ = estimate · $x[n]$ or $x_1,\ldots,x_N$ = data · $E[\cdot]$ = expected/long-run average · $\operatorname{Var}(x)=E[x^2]-E[x]^2$ · $r[k]$ = correlation $k$ steps apart · $P(\theta)$ = power spectral density (PSD) · $\sigma^2$ = noise variance · $Q(t)=P(Z\gt t)$ for standard Gaussian $Z$.
{: .how }

## PART 1 · Probability (1.5 p)

### 1A · Joint PDF: region, integrals, marginals

IF YOU SEE $p(x,y)$ with a region, or “find $c$”, “probability”, “marginal”, “conditional”, “independent”, “domain”
{: .see }

**Meaning.** $p(x,y)$ describes how likely the pair $(x,y)$ is. The **allowed region** (also called support/domain) is where the given formula applies; outside it, $p=0$. Integrating $p$ over the WHOLE allowed region must give 1—that is the reason “find $c$” works. **If asked for the probability of a condition:** shade only the part of the allowed region where that condition is also true, then integrate $p$ over the shaded part using the same slice method below. This answer is a probability; **do not set it equal to 1**.

**LIMITS — copy this procedure; do not guess.** For $dx\,dy$, $x$ is INNER and $y$ is OUTER. **(1)** Draw the allowed region and label each boundary equation. **(2)** Fix outer $y$ at one allowed value; draw a horizontal slice. **(3)** Where the slice enters/leaves the region gives the lower/upper $x$-limits; solve the boundary for $x$ if needed. These limits may contain $y$. **(4)** Sweep the slice across the whole region: the smallest/largest possible $y$ are numerical outer limits. For $dy\,dx$, swap every word $x\leftrightarrow y$ and use a vertical slice. Rectangle → constant limits; non-rectangle → at least one limit depends on the outer letter.

<svg class="regionpic" viewBox="0 0 170 122" role="img" aria-label="Triangle x plus y below 1 with horizontal integration slice"><path d="M28 98H157M28 98V8" fill="none" stroke="#222" stroke-width="1.5"/><path d="M28 98L28 18L118 98Z" fill="#fff1b8" stroke="#3b2f63" stroke-width="1.5"/><path d="M28 70H80" fill="none" stroke="#b3261e" stroke-width="2"/><circle cx="28" cy="70" r="2.5" fill="#b3261e"/><circle cx="80" cy="70" r="2.5" fill="#b3261e"/><text x="160" y="103" font-size="12">x</text><text x="17" y="10" font-size="12">y</text><text x="116" y="111" font-size="11">1</text><text x="14" y="20" font-size="11">1</text><text x="86" y="66" font-size="10">x=1−y</text><text x="34" y="65" font-size="10" fill="#b3261e">fixed y</text><text x="43" y="114" font-size="10">slice: 0≤x≤1−y</text></svg>

**FULL EXAMPLE (Apr25), no skipped steps.** $p(x,y)=cx+1$ on $x\ge0$, $y\ge0$, $x+y\lt1$. The boundaries meet at $(0,0),(1,0),(0,1)$; the sloped boundary is $y=1-x$, equivalently $x=1-y$. For $dx\,dy$, a horizontal slice has $0\le x\le1-y$, and slices cover $0\le y\le1$.

**A · Find $c$ (normalise).** Write the whole double integral before calculating:
<mark>$1=\int_{y=0}^{1}\left[\int_{x=0}^{1-y}(cx+1)\,dx\right]dy.$</mark>
**Inner, $x$ changes; $y,c$ are constants:**
$\int_0^{1-y}(cx+1)dx=\left[\frac{cx^2}{2}+x\right]_0^{1-y}=\frac c2(1-y)^2+(1-y)-0.$
**Outer, only $y$ remains.** Expand $(1-y)^2=1-2y+y^2$:
$1=\int_0^1\left[\frac c2(1-2y+y^2)+1-y\right]dy=\left[\frac c2\left(y-y^2+\frac{y^3}{3}\right)+y-\frac{y^2}{2}\right]_0^1.$
Substitute $y=1$, then subtract the value at $y=0$ (zero): $1=\frac c2(1-1+\frac13)+1-\frac12=\frac c6+\frac12$. Thus $\frac c6=\frac12\Rightarrow\boxed{c=3}$. **Check:** $c=3$ makes $p=3x+1\ge0$ throughout the triangle.

**B · Marginal = integrate away the OTHER variable.** For $p_X(x)$, use a vertical slice: fixed $x$, $0\le y\le1-x$; the region’s $x$-shadow is $0\le x\le1$:
$p_X(x)=\int_0^{1-x}(3x+1)dy=\left[3xy+y\right]_0^{1-x}=(3x+1)(1-x)=1+2x-3x^2,$
and $p_X(x)=0$ otherwise. **Check:** $\int_0^1(1+2x-3x^2)dx=[x+x^2-x^3]_0^1=1$.
Similarly $p_Y(y)=\int_0^{1-y}(3x+1)dx=\frac32(1-y)^2+(1-y)=\frac52-4y+\frac32y^2$ for $0\le y\le1$, $0$ otherwise.

**C · Conditional = joint ÷ marginal of the variable GIVEN.** <mark>$p(x\mid y)=p(x,y)/p_Y(y)$</mark>. Here $p(x\mid y)=\dfrac{3x+1}{\frac52-4y+\frac32y^2}$ for $0\le x\le1-y$ (with $0\le y\lt1$); outside, 0. For $p(y\mid x)$, divide by $p_X(x)$ instead. **Do not reuse the original two-variable range without saying which variable is fixed.**

**D · Independent?** Both must hold: **(1)** support is a rectangle (possibly infinite), **(2)** $p(x,y)=p_X(x)p_Y(y)$ everywhere. Here the triangle fails test 1 → **not independent**. Square example: $p=6x^2y$ on $[0,1]^2$ gives $p_X=3x^2$, $p_Y=2y$, whose product is $6x^2y$ → independent.

**Fast checks:** every pdf/marginal $\ge0$ and integrates to 1 on its stated domain · every probability lies in $[0,1]$ · conditional integrates to 1 over the remaining variable’s slice · polynomial rule $\int x^n dx=x^{n+1}/(n+1)$, $n\ne-1$.

### 1B · WSS / ergodic (multiple choice)

IF YOU SEE "WSS"/"wide-sense stationary"/"stationary", "ergodic", dice, random phase, random amplitude
{: .see }

**Definitions.** **WSS** requires BOTH: mean $m(t)=E[x(t)]$ is constant, and $r(t_1,t_2)=E[x(t_1)x(t_2)]$ depends only on the lag $\tau=t_1-t_2$. **Ergodic in the mean** = the time average of EACH realisation equals the ensemble mean $E[x(t)]$. Ensemble average = average across all possible signals at fixed $t$; time average = average along one recorded signal.

1. **Mean test:** calculate $E[x(t)]$; deterministic functions of $t$ stay, random letters become their means. If $t$ remains → not WSS; stop.
2. **Correlation test:** multiply $x(t_1)x(t_2)$, expand, then take $E$. Use $\cos a\cos b=\frac12[\cos(a+b)+\cos(a-b)]$ and $E[\cos(k+U)]=0$ for uniform phase $U$. If only $t_1-t_2$ remains → WSS. If $t_1+t_2$ or a separate $t$ remains → not WSS.
3. **Ergodic test — actually compare averages; do not use “random letter frozen” as a shortcut.** Compute $\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}x(t)dt$ (or the discrete sum) for one realisation and compare with step 1. For ergodicity in variance, repeat with $x^2$ and compare $E[x^2]$.

**Random phase, $x(t)=\cos(\omega t+U)$, $U$ uniform on $[0,2\pi)$:** $E[x(t)]=0$, so mean passes. $r=E[\cos(\omega t_1+U)\cos(\omega t_2+U)]=\frac12\cos(\omega(t_1-t_2))+\frac12E[\cos(\omega(t_1+t_2)+2U)]=\frac12\cos(\omega(t_1-t_2))$ → **WSS**. One realisation is still a cosine, whose long-time average is 0 → **ergodic in the mean**, even though its phase is fixed.

**Random amplitude, $x(t)=A$ for all $t$:** $E[x]=E[A]$ and $r=E[A^2]$ are constants → **WSS**. But one realisation has time average $A$, not generally $E[A]$ → **NOT ergodic in the mean**. Fresh independent dice/samples at every time → time average sees the full distribution → ergodic under the exam’s usual assumptions; streamed values uniform in $[-A,A]$ have mean 0.

**Vocabulary:** random process = set of possible signals; realisation = one recorded signal; random variable = one numerical outcome. Strict stationarity concerns whole distributions; WSS checks only mean and correlation.

### 1C · Spectral factorisation

IF YOU SEE $P(\theta)=\dfrac{\text{number}}{A+B\cos\theta}$ + "spectral factorisation"/"factorization", "innovation filter $L(z)$", "$\sigma_i^2$"
{: .see }

1. Read $A$ and $B$ off the denominator $A+B\cos\theta$ **with their signs** ($25-24\cos\theta$: $A=25$, $B=-24$). Two candidate roots $r=\dfrac{A\pm\sqrt{A^2-B^2}}{B}$: keep the one between $-1$ and $1$, call it $a$.
2. $C=\dfrac{B}{2a}$ (just a helper number).
3. <mark>$\sigma_i^2=\dfrac{\text{number on top}}{C}$, $L(z)=\dfrac{1}{1+a\,z^{-1}}$</mark>.
4. Check $|a|\lt1$ and $\sigma_i^2\gt0$ — a negative $\sigma_i^2$ means you kept the wrong root. Sanity: $\dfrac{\sigma_i^2}{1+a^2+2a\cos\theta}$ must give back the $P(\theta)$ you started from.

*Apr24, $P=\frac{7}{25-24\cos\theta}$:*<br>
**Step 1 — root:** $A=25$, $B=-24$, so $\sqrt{A^2-B^2}=\sqrt{625-576}=7$. Candidates: $\frac{25+7}{-24}=-\frac43$ and $\frac{25-7}{-24}=-\frac34$. Keep $a=-\frac34$ because it is between $-1$ and $1$.<br>
**Step 2 — helper $C$:** $C=\frac{B}{2a}=\frac{-24}{2(-3/4)}=\frac{-24}{-3/2}=16$.<br>
**Step 3 — answers:** $\sigma_i^2=\frac{\text{top}}C=\frac7{16}$ and $L(z)=\frac1{1+az^{-1}}=\boxed{\frac1{1-\frac34z^{-1}}}$.

Multiple choice "what must the innovation filter be?" → **minimum phase** (poles and zeros inside the unit circle — the label is the whole answer; Jun26 a).

### 1D · Expected value and the MC words

IF YOU SEE "expected value", "discrete or continuous", "exactly $k$ of $n$", "covariance", "contour plot"
{: .see }

- **Expected value = probability-weighted average.** Discrete: $E[x]=\sum_x x\,p(x)$. Continuous: $E[x]=\int x\,p(x)dx$ with the pdf’s ordinary domain limits. For $E[x^2]$, put $x^2p(x)$ inside instead. With two variables, use the explicit slice limits from 1A and integrate $x\,p(x,y)$ (or $y\,p(x,y)$ for $E[y]$). The pdf alone sums/integrates to 1, **not** to the mean. **Mode** = most likely value. **Variance** $\operatorname{Var}(x)=E[x^2]-(E[x])^2$; standard deviation $=\sqrt{\operatorname{Var}}$.
- **Discrete** = the values can be listed: "number of …", counts, dice, digits 0–255. **Continuous** = a measurement: time, distance, weight, money.
- **Rules:** $E[c\cdot z]=c\,E[z]$ · $E[c]=c$ · $E[z_1+z_2]=E[z_1]+E[z_2]$ — a constant factor comes out. Uniform $[a,b]$ → mean $\frac{a+b}2$ ($[-A,A]$ → 0).
- **"Exactly $k$ of $n$ tries"** (binomial): $C(n,k)\,p^k(1-p)^{n-k}$, $p$ = chance of one try, $C(n,k)=\frac{n(n-1)\cdots(n-k+1)}{k!}$. *e.g.* $n=4,k=2,p=0.3$: $C(4,2)=\frac{4\cdot3}{2\cdot1}=6$ → $6(0.3)^2(0.7)^2=0.2646$.
- **Covariance:** $\mathrm{Cov}(x,y)=E[xy]-E[x]E[y]$ · sign = whether one goes up when the other does · the number changes with units · correlation coefficient $=\mathrm{Cov}/(\sigma_x\sigma_y)$, always in $[-1,1]$. Independent → covariance 0; covariance 0 does **not always** prove independence. *Example:* $p(0,0)=p(1,1)=\frac12$: $E[x]=E[y]=E[xy]=\frac12$ → $\mathrm{Cov}=\frac12-\frac14=\frac14$.
- **Contour plot, bi-variate Gaussian:** covariance = the two corner (off-diagonal) entries of the covariance matrix: $0$ → ellipses aligned with the axes · **tilted** ellipses → covariance $\ne0$.
- **Definition MC / T/F:** $F(t)=P(x\le t)$ (the cumulative), so $F(-\infty)=0$, $F(\infty)=1$ · independent $=P(A\mid B)=P(A)$, the same as $P(A\cap B)=P(A)P(B)$ ($\cap$ = "both happen") · **disjoint** = they can never both happen, $P(A\cap B)=0$ (the opposite!) · Bayes $=$ conditional probability rearranged. A T/F list → the swap test of box 2D, any topic.

## PART 2 · Estimation (3–3.5 p)

### 2A · Maximum likelihood (MLE)

IF YOU SEE a pdf $p(x\mid\theta)$, samples $x_1..x_N$, "maximum likelihood", "derive the MLE", "find an estimator", "estimate of …"
{: .see }

For $N$ **iid** samples (independent, same pdf), $L(\theta)=\prod_{n=1}^Np(x_n\mid\theta)$: multiply one pdf by itself $N$ times, using $x_1,\ldots,x_N$. Maximise $\ln L$ instead; $\ln$ turns multiplication into addition and does not move the maximum.

1. **Log:** <mark>$\ell(\theta)=\ln L=\sum_n\ln p(x_n\mid\theta)$</mark>. Keep every term containing $\theta$. A constant term repeated for every sample becomes $N$ times that term.
2. **Differentiate with respect to $\theta$:** treat every $x_n$ as a known number; terms without $\theta$ vanish. Write $\ell'(\theta)$.
3. **Solve $\ell'(\theta)=0$**, respecting the parameter’s allowed range. Multiply through by denominators first if useful. The solution $\hat\theta$ is the MLE; if no stationary point exists, check allowed endpoints. A quick maximum check is $\ell''(\hat\theta)\lt0$ when applicable.

**How to take $\ln$ of a pdf:** write the pdf as $\frac{\text{above}}{\text{below}}\cdot e^{u}$ (it is pieces multiplied, some in a fraction). Then each piece becomes one term: a piece $a$ **above the line** → $+\ln a$ · a piece $b$ **below the line** → $-\ln b$ · $e^{u}$ → just $u$ (the $e$ disappears). Two pieces below the line split: $-\ln(2\theta)=-\ln 2-\ln\theta$. A power $\theta^k$ below the line → $-k\ln\theta$.
Derivatives: $\ln\theta\to\frac1\theta$ · $\theta^k\to k\theta^{k-1}$ · $\frac1\theta\to-\frac1{\theta^2}$ · $e^{c\theta}\to ce^{c\theta}$ · $\cos\theta\to-\sin\theta$ · $\sin\theta\to\cos\theta$.
Solving $=0$: multiply the equation by the denominators ($\theta^2$, $\theta$, …) first — that does not change the solution.
**Trap:** if the pdf only exists for $x$ up to something containing $\theta$ (uniform on $[0,\theta]$), these 3 steps are useless — $\hat\theta=\max_n x_n$, and **the CRLB does not exist**.
**Only if Fisher information / CRLB is asked:** CRLB is the lowest possible variance of an unbiased estimator; reaching it = efficient. **(1)** Take $\ln p$ for ONE sample. **(2)** Differentiate with respect to the unknown twice. **(3)** Put a minus in front and take the expectation: $i(\theta)=-E[\text{second derivative of }\ln p]$. If $x$ remains, replace it using the known $E[x]$. **(4)** For $N$ iid samples, $\mathcal I=N\,i(\theta)$ and $\boxed{CRLB=1/(N\,i(\theta))}$.
*Exponential example, $p=\lambda e^{-\lambda x}$:* $\ln p=\ln\lambda-\lambda x$ → first derivative $=1/\lambda-x$ → second derivative $=-1/\lambda^2$ → $i(\lambda)=-E[-1/\lambda^2]=1/\lambda^2$ → $CRLB=\lambda^2/N$.
**Shortcut values of $i$:** Gaussian mean, known variance $\sigma^2$: $1/\sigma^2$ · exponential rate $\lambda$: $1/\lambda^2$ · Bernoulli $\theta$: $1/[\theta(1-\theta)]$ · Rayleigh $p=\frac{x}{\theta^2}e^{-x^2/2\theta^2}$: $4/\theta^2$, hence CRLB $=\theta^2/(4N)$.

**Check your $\hat\theta$:** uniform $[0,\theta]$ → $\max_n x_n$ (the trap above) · exponential rate $\lambda$ → $1/\bar x$ · Poisson $\lambda$ → $\bar x$ · Bernoulli → $k/N$ ($k$ successes in $N$).

*Apr24, follow the three steps.* $p(x\mid\theta)=\tfrac{x}{2\theta}e^{-x^2/(2\theta)}$. One sample: $\ln p=\ln x-\ln2-\ln\theta-\tfrac{x^2}{2\theta}$. Therefore $\ell=\sum\ln x_n-N\ln2-N\ln\theta-\tfrac{\sum x_n^2}{2\theta}$. Differentiate: $\ell'=-\tfrac N\theta+\tfrac{\sum x_n^2}{2\theta^2}$. Set to 0 and multiply by $2\theta^2$: $-2N\theta+\sum x_n^2=0$ → $\boxed{\hat\theta=\tfrac1{2N}\sum x_n^2}$.

*Jun26* Gamma $\tfrac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$, $n$ patients: $\ln p=(k-1)\ln x-\tfrac x\theta-k\ln\theta-\ln\Gamma(k)$. Add all $n$ logs: $\ell=(k-1)\sum\ln x_i-\tfrac{\sum x_i}{\theta}-nk\ln\theta-n\ln\Gamma(k)$. Differentiate and drop terms without $\theta$: $\ell'=\tfrac{\sum x_i}{\theta^2}-\tfrac{nk}\theta=0$. Multiply by $\theta^2$: $\sum x_i-nk\theta=0$ → $\boxed{\hat\theta=\tfrac{\sum x_i}{nk}=\tfrac{\bar x}k}$.

**Sigmoid trick.** IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then convert with $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.

*Apr25, one observation:* $p=3\lambda e^{-4\lambda x/7}$ → $\ln p=\ln3+\ln\lambda-\tfrac{4\lambda x}7$ → derivative $\tfrac1\lambda-\tfrac{4x}7=0$ → $\tfrac1\lambda=\tfrac{4x}7$ → $\hat\lambda=\tfrac7{4x}$. Convert: $\hat\theta=-\ln(1/\hat\lambda-1)=-\ln(\tfrac{4x}7-1)$, valid when $x\gt\tfrac74$.

### 2B · MAP with a prior (Beta / Gamma)

IF YOU SEE "prior", "posterior", "MAP", "maximum a posteriori"/"a-posteriori", "MMSE"/"minimum mean square error", "Bayesian estimator", Beta, Gamma
{: .see }

**Central rule:** <mark>posterior $\propto$ likelihood $\times$ prior</mark>. **MAP** = parameter value at the posterior’s maximum; **MMSE** = posterior mean. Multiplicative constants not containing the unknown do not change MAP.

1. **Likelihood:** write each observation’s probability, keep only factors containing the unknown, multiply them; equal bases → add exponents.
2. **Multiply by the prior**, adding exponents again. Call the result $q(\theta)$. It may be unnormalised (its integral need not be 1).
3. Match $q$ to a row below: $A,B$ are the FINAL exponents after including every observation and the prior.

| Result looks like | Posterior | MAP | MMSE (mean) |
|---|---|---|---|
| $\theta^{A}(1-\theta)^{B}$ | Beta$(A{+}1,B{+}1)$ | $\frac{A}{A+B}$ | $\frac{A+1}{A+B+2}$ |
| $\lambda^{A}e^{-B\lambda}$ | Gamma$(A{+}1,B)$ | $\frac{A}{B}$ | $\frac{A+1}{B}$ |

Prior Beta$(a,b)$ = $\theta^{a-1}(1-\theta)^{b-1}$ (its mean $\frac a{a+b}$). Prior Gamma$(a,b)$ = $\lambda^{a-1}e^{-b\lambda}$ (mean $\frac ab$). The prior pulls the estimate towards that mean.
One observation $x$ gives: Poisson count → $\lambda^{x}e^{-\lambda}$ · "$k$-th success on trial $x$" → $\theta^k(1-\theta)^{x-k}$ · "$k$ successes in $n$ tries" → $\theta^k(1-\theta)^{n-k}$ · exponential → $\lambda e^{-\lambda x}$.

**If your result is not in the table:** MAP = the allowed $\theta$ where $q$ is largest; usually solve $\frac{d}{d\theta}\ln q=0$. MMSE = $\dfrac{\int\theta q(\theta)d\theta}{\int q(\theta)d\theta}$ using the allowed parameter limits. The denominator is required: it makes the posterior’s total probability 1. If the best point is outside the prior’s allowed interval, choose the nearest endpoint for MAP.

*Jun26-2c (Beta):* each observation contributes $\theta^2(1-\theta)^{x-2}$.<br>
**Step 1 — multiply the five likelihood factors:** $\theta$ powers add: $2+2+2+2+2=10$. The $(1-\theta)$ powers add: $(3-2)+(5-2)+(4-2)+(6-2)+(4-2)=12$. Likelihood $=\theta^{10}(1-\theta)^{12}$.<br>
**Step 2 — multiply the prior:** Beta(2,3) contributes $\theta^{2-1}(1-\theta)^{3-1}=\theta^1(1-\theta)^2$. Final powers: $q=\theta^{11}(1-\theta)^{14}$.<br>
**Step 3 — read the table with $A=11,B=14$:** MAP $=\tfrac{11}{11+14}=\tfrac{11}{25}=0.44$; MMSE $=\tfrac{12}{11+14+2}=\tfrac{12}{27}=0.444$.

*Jun26-2d (Gamma), Poisson observations $2,4,3,5,2,4$:*<br>
**Step 1 — likelihood:** $\lambda$ powers add: $2+4+3+5+2+4=20$. Six observations give six factors $e^{-\lambda}$, so likelihood $=\lambda^{20}e^{-6\lambda}$.<br>
**Step 2 — multiply prior Gamma(3,2):** prior $=\lambda^{3-1}e^{-2\lambda}=\lambda^2e^{-2\lambda}$. Add powers and exponential coefficients: $q=\lambda^{22}e^{-8\lambda}$.<br>
**Step 3 — read the table with $A=22,B=8$:** MAP $=\tfrac{22}8=2.75$; MMSE $=\tfrac{23}8=2.875$. Without the prior, MLE $=\tfrac{20}6=3.33$; the prior pulls toward its mean $\tfrac32$.

*Nov22:* unnormalised $q=\lambda e^{-(x+a)\lambda}$ → MAP $=1/(x+a)$; MMSE uses the normalising ratio $=2/(x+a)$ (fully integrated in Calculations). For a sigmoid parameter, use the conversion at the end of 2A.

### 2C · Least-squares line

IF YOU SEE points $(x,y)$ + "least squares"/"least-squares"/"LSE", "linear function", "fit a line"
{: .see }

1. Means $\bar x$ and $\bar y$ (bar = average).
2. Slope: <mark>$a=\tfrac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}$</mark>.
3. Intercept: <mark>$b=\bar y-a\bar x$</mark>. Answer: $y=ax+b$. Check: $x=\bar x$ must give $y=\bar y$.

*Apr25, points $(0,3),(2,4),(3,3)$:*<br>
**Step 1 — averages:** $\bar x=\tfrac{0+2+3}3=\tfrac53$ and $\bar y=\tfrac{3+4+3}3=\tfrac{10}3$.<br>
**Step 2 — subtract the average from EACH point:** $x-\bar x=(-\tfrac53,\tfrac13,\tfrac43)$ and $y-\bar y=(-\tfrac13,\tfrac23,-\tfrac13)$.<br>
**Step 3 — form the two sums:** numerator $=(-\tfrac53)(-\tfrac13)+(\tfrac13)(\tfrac23)+(\tfrac43)(-\tfrac13)=\tfrac{5+2-4}{9}=\tfrac13$. Denominator $=(-\tfrac53)^2+(\tfrac13)^2+(\tfrac43)^2=\tfrac{25+1+16}{9}=\tfrac{14}3$.<br>
**Step 4 — slope, then intercept:** $a=\tfrac{1/3}{14/3}=\tfrac1{14}$; $b=\bar y-a\bar x=\tfrac{10}3-\tfrac1{14}\tfrac53=\tfrac{45}{14}$. Therefore $\boxed{y=\tfrac1{14}x+\tfrac{45}{14}}$. Check: putting $x=\bar x$ gives $y=\bar y$.

Also: $x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$. $x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$ (noise = random wobble; fitting a constant by least squares is just its average).

**Beyond a straight line.** $J(\theta)=\sum_n(x[n]-s[n;\theta])^2$, $\hat\theta=\arg\min J$ (the $\theta$ making $J$ smallest) — write this when they ask "what kind of estimator". One amplitude $s[n]=Ah[n]$: $\hat A=\dfrac{\sum x[n]h[n]}{\sum h[n]^2}$ (*e.g.* $x=3,5$, $h=1,2$: $\hat A=\tfrac{3+10}{1+4}=2.6$). Linear model $x=\mathbf H\theta+w$: $\hat\theta=(\mathbf H^T\mathbf H)^{-1}\mathbf H^Tx$; the **error** $x-\mathbf H\hat\theta$ is orthogonal (perpendicular) to the columns of $\mathbf H$ (it is the error, **not** $\hat\theta$); weighted LS with $\mathbf W=\mathbf C_x^{-1}$ = **BLUE** (best linear unbiased estimator). Nonlinear: transform it (the $e^{\bar x}$ line), or iterate **Gauss–Newton** $\theta_{k+1}=\theta_k+(\mathbf G^T\mathbf G)^{-1}\mathbf G^T(x-s(\theta_k))$, $\mathbf G[:,i]=\frac{\partial s}{\partial\theta_i}$ — Newton–Raphson works too, "only Gauss–Newton" is **false**.

### 2D · Part 2 true / false

IF YOU SEE "which of the following statements" (in Part 2) about MLE, MAP, MMSE, Fisher, CRLB
{: .see }


**T/F method:** translate each option into an equation before deciding. A common false option is a true sentence with ONE word swapped: hunt *always · regardless · strictly · maximise/minimise · mean/maximum*. This is a warning sign, **not proof**; “always” is killed by one counterexample, and a true sentence needs no swap word.

| The fact (true) | The lie they print (false) |
|---|---|
| MMSE = **mean** of the posterior; MAP = **maximum** | the two swapped |
| MMSE = MAP for a symmetric one-peak posterior | "**always** different" / "always equal" |
| MAP = likelihood × prior, needs a prior (Jun26 c) | "MAP→MLE **regardless of** the prior" · "Bayesians skip priors" |
| Bayes estimate **minimises** the Bayes risk (Nov22 b) | "maximises" |
| Quadratic cost → MMSE; uniform cost → MAP | "uniform cost → MMSE" |
| MLE = argmax of the likelihood **over $\theta$** | "over $x$" · "only linear models" |
| MLE is **asymptotically** unbiased and efficient | "**always** reaches the CRLB" |
| Invariance: $\alpha=\psi(\theta)$ 1-to-1 → $\hat\theta=\psi^{-1}(\hat\alpha)$ (Jan22 c) | — |
| Fisher of $N$ iid (independent, same pdf) $=N\,i(\theta)$, $\mathcal I\ge0$; $\mathrm{Var}(\hat\theta)\ge\frac1{\mathcal I(\theta)}$ | "$\mathcal I$ strictly negative" · "$\ge\mathcal I(\theta)$" |
| CRLB $=\frac1{N i(\theta)}$ shrinks $\sim\frac1N$ (Jan22 b) | "**always** derivable" (no, if range of $x$ depends on $\theta$) |
| efficient = variance **equal to** the CRLB | "**below** the CRLB" |

Fisher info for "$x$ = signal($\theta$) + Gaussian noise $\sigma^2$": $\mathcal I=\frac1{\sigma^2}\sum\big(\frac{d\,\text{signal}}{d\theta}\big)^2$.

*Nov22* $A[\cos\theta,\sin\theta]$: **phase MLE** $=\arctan\frac{x_2}{x_1}$ (point the model vector at the data), $\mathcal I=\frac{A^2}{\sigma^2}$.

## PART 3 · Spectral estimation (3 p)

$r[k]$ = autocorrelation at lag $k$ (the given numbers; lag $k$ = $k$ steps apart). Rewrite cosines: $\cos2\theta=2\cos^2\theta-1$, $\cos3\theta=4\cos^3\theta-3\cos\theta$, $\cos\alpha\cos\beta=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2$ (to expand $\lvert L\rvert^2$ of box 1C).
{: .how }

**Draw it** — the question says "determine **and plot**", only the numbers are graded: $r[k]$ → vertical **stems** (one stick per lag) at the lags. $P(\theta)$ → compute the value at $\theta=0$ and at $\theta=\pi$, draw **one smooth curve** through those two heights and write them on the axis. Peak at $0$ = low-pass (low frequencies), peak at $\pi$ = high-pass, peak in between = band-pass.

### 3A · Correlogram

IF YOU SEE $r[0],r[1],r[2]\dots$ + "correlogram", "only these lags", "PSD as a function of $\cos\theta$", correlation values given
{: .see }

<mark>$P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos(2\theta)+2r[3]\cos(3\theta)+\cdots$</mark>. Stop at the largest given lag. **Why the 2?** Correlation at lag $+k$ equals correlation at lag $-k$; their two equal contributions combine into $2r[k]\cos(k\theta)$. The zero lag occurs only once, so **do not double $r[0]$**. From a data list, $\hat r[k]=\frac1N(\text{sum of products of values }k\text{ positions apart})$: use only pairs that both exist, but still divide by the full data length $N$. Reverse question ($P$ given): $r[0]$ = constant term; $r[k]$ = HALF the coefficient of $\cos(k\theta)$. Check your expression at $\theta=0$ (every cosine = 1) and $\theta=\pi$ (cosines alternate between $-1$ and $1$).

*Jun26* $3,2,1$: $3+4\cos\theta+2\cos2\theta=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$. *From data* $x=[1,2,3]$: $\hat r[0]=\tfrac{1+4+9}{3}=\tfrac{14}3$, $\hat r[1]=\tfrac{2+6}{3}=\tfrac83$ (only the 2 overlapping pairs), $\hat r[2]=\tfrac33=1$.

### 3B · AR(1)

IF YOU SEE "AR(1)", "first-order autoregressive"
{: .see }

Use the LEFT-side convention $x[n]+a\,x[n-1]=i[n]$ (equivalently $x[n]=-a\,x[n-1]+i[n]$), with white-noise variance $\sigma^2$. The sign of $a$ must match this equation.

1. <mark>$a=-\dfrac{r[1]}{r[0]}$</mark>
2. <mark>$\sigma^2=r[0]+a\,r[1]$</mark>
3. <mark>$P=\dfrac{\sigma^2}{1+a^2+2a\cos\theta}$</mark> (check $|a|\lt1$ and $\sigma^2\gt0$, else a sign went wrong)

*Apr25* $r[0]=2$, $r[1]=-\tfrac14$: $a=-\tfrac{-1/4}{2}=\tfrac18$ · $\sigma^2=2+\tfrac18(-\tfrac14)=\tfrac{63}{32}$ → $P=\tfrac{63/32}{1+\frac1{64}+\frac14\cos\theta}\cdot\tfrac{64}{64}=\tfrac{126}{65+16\cos\theta}$.

### 3C · AR(2) / Yule–Walker

IF YOU SEE "AR(2)", "Yule–Walker", $r[0],r[1],r[2]$
{: .see }

Convention: $x[n]+a_1x[n-1]+a_2x[n-2]=i[n]$. Substitute the three given correlations in order:

1. $D=r[0]^2-r[1]^2$ (shared denominator)
2. $a_1=\dfrac{-r[1]\,(r[0]-r[2])}{D}$,  $a_2=\dfrac{r[1]^2-r[0]\,r[2]}{D}$
3. $\sigma^2=r[0]+a_1r[1]+a_2r[2]$
4. $P=\dfrac{\sigma^2}{1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta}$

If they want the matrix (Yule–Walker = steps 1–2 in matrix form): $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$.

*Jun26* $r=3,2,1$: $D=3^2-2^2=5$ · $a_1=\tfrac{-2(3-1)}5=-\tfrac45$ · $a_2=\tfrac{2^2-3\cdot1}5=\tfrac15$ · $\sigma^2=3+(-\tfrac45)2+\tfrac15(1)=\tfrac85$ → step 4, then $\cos2\theta=2\cos^2\theta-1$ → $P=\tfrac{10}{5\cos^2\theta-12\cos\theta+8}$.

### 3D · MA(1)

IF YOU SEE "MA(1)", "moving average"
{: .see }

Model: $x[n]=i[n]+b\,i[n-1]$. PSD: $P=r[0]+2r[1]\cos\theta$ — it uses $r[0],r[1]$ only: ignore $r[2]$ and beyond.
If they ask for $b$ and $\sigma^2$: solve $b^2-\frac{r[0]}{r[1]}\,b+1=0$, keep the root between $-1$ and $1$; then $\sigma^2=\frac{r[1]}{b}$.

*Apr25* $r=2,-\tfrac14$: $P=2-\tfrac12\cos\theta$. $b,\sigma^2$ asked too: $b^2-\tfrac{r[0]}{r[1]}b+1=b^2+8b+1=0$ → $b=-4+\sqrt{15}=-0.127$ (the root with $\lvert b\rvert\lt1$), $\sigma^2=\tfrac{r[1]}{b}=\tfrac{4+\sqrt{15}}4=1.97$; check $r[0]=\sigma^2(1+b^2)=2$ ✓

### 3E · Model from an equation

IF YOU SEE $x[n]=\dots$ + "which kind of process", "calculate the autocorrelation of $x$"
{: .see }

**1 · Name the model by looking only at the right-hand side.** $i$ means input noise. Only noise terms → **MA**; the largest noise delay is $q$. Noise AND earlier $x$ terms → **ARMA**; the largest earlier-$x$ delay is $p$. Earlier $x$ terms with only $i[n]$ → **AR**: use 3B/3C. If asked from a PSD shape: sharp peaks → AR, deep nulls → MA, both → ARMA.

**2 · MA autocorrelation: copy coefficients, then multiply pairs.** For $x[n]=i[n]+b_1i[n-1]+b_2i[n-2]+\cdots$, write the coefficient list $(1,b_1,b_2,\ldots)$ and noise variance $\sigma^2$. $r[0]=\sigma^2(\text{sum of EVERY coefficient squared})$. $r[1]=\sigma^2(\text{sum of products of neighbouring coefficients})$. $r[2]=\sigma^2(\text{sum of products two positions apart})$, and so on. After the largest delay, $r[k]=0$.

*Apr24, every pair shown:* coefficients $(1,-\tfrac12,\tfrac14,-\tfrac12)$, $\sigma^2=1$.<br>
$r[0]=1^2+(-\tfrac12)^2+(\tfrac14)^2+(-\tfrac12)^2=\tfrac{25}{16}$.<br>
$r[1]=(1)(-\tfrac12)+(-\tfrac12)(\tfrac14)+(\tfrac14)(-\tfrac12)=-\tfrac34$.<br>
$r[2]=(1)(\tfrac14)+(-\tfrac12)(-\tfrac12)=\tfrac12$ · $r[3]=(1)(-\tfrac12)=-\tfrac12$.

**Backwards (coefficients asked from $r[k]$):** for MA(2), start at the largest lag: $b_2=r[2]/\sigma^2$; then $r[1]=\sigma^2b_1(1+b_2)$, so $b_1=r[1]/[\sigma^2(1+b_2)]$. Finally $r[0]=\sigma^2(1+b_1^2+b_2^2)$.

**3 · ARMA(1,1): move earlier $x$ to the LEFT.** Match $x[n]+\alpha x[n-1]=i[n]+\beta i[n-1]$; the signs come from this left-side form. Then $P=\sigma^2\dfrac{1+\beta^2+2\beta\cos\theta}{1+\alpha^2+2\alpha\cos\theta}$. If correlations are asked: $r[0]=\sigma^2\dfrac{1+\beta^2-2\alpha\beta}{1-\alpha^2}$, $r[1]=-\alpha r[0]+\beta\sigma^2$, and each following $r[k]$ is the previous one times $-\alpha$.<br>
*Nov22:* $x[n]=i[n]-i[n-1]+\tfrac34x[n-1]$ becomes $x[n]-\tfrac34x[n-1]=i[n]-i[n-1]$, so $\alpha=-\tfrac34$, $\beta=-1$. With $\sigma^2=\tfrac78$: numerator $=\tfrac78(1+1-2\cos\theta)$, denominator $=1+\tfrac9{16}-\tfrac32\cos\theta$ → $P=\dfrac{28(1-\cos\theta)}{25-24\cos\theta}$.

### 3F · Pick the plot

IF YOU SEE "which plot", "which figure", "plots A–D", "match the plot"
{: .see }

Work out each PSD at $\theta=0$ (all cosines $=1$) and at $\theta=\pi$ ($\cos\theta=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Pick the plot with those heights. Only a correlogram can go below 0.

*Apr25:* correlogram $1.13\to2.13$, MA $1.5\to2.5$, AR $1.56\to2.57$ (heights at $0\to\pi$) → plot D.
**Second type** (windowed cosine, DTFT vs DFT — the DTFT is the whole curve, the DFT is the dots on it): infinite cosine = **2 spikes** · windowed = **main lobe + side lobes** (one big bump + small ones) · DFT = **samples of that same curve** · zero padding = **more dots**, not more resolution.

### 3G · Welch / Bartlett count

IF YOU SEE "Welch"/"Bartlett"/"WOSA", $N$ samples, segment length $L$, overlap %, "how many segments"
{: .see }

**Convert overlap to a fraction first** (50 % → 0.5). Step/start spacing <mark>$D=L(1-\text{overlap})$</mark>. Segment starts are $0,D,2D,\ldots$; include a start only if its whole length-$L$ segment fits. Hence <mark>$K=\left\lfloor\frac{N-L}{D}\right\rfloor+1$</mark>. Bartlett = 0 overlap, so $K=\lfloor N/L\rfloor$. Ideal independent-segment variance ratio = $1/K$; real overlapping Welch segments are correlated, so reduction is less.

*Jun26* $N=1000$, $L=200$, 50 %: $D=200(1-0.5)=100$, $K=\tfrac{1000-200}{100}+1=9$ segments, ratio $\tfrac19$.

### 3H · Energy or power signal

IF YOU SEE "energy or power signal", "total energy", "average power"
{: .see }

- Dies out or has finite length → **energy signal**: $0\lt E=\sum_n\lvert x[n]\rvert^2\lt\infty$, average power $=0$.
- Repeats/never dies (sin, cos, nonzero constant, $\cos t\,u(t)$) → **power signal**: $E=\infty$, finite nonzero $P$ = time average of $|x|^2$. A sinusoid $A\sin(\omega t)$ or $A\cos(\omega t)$ has $P=A^2/2$.
- Continuous time: $E=\int_{-\infty}^{\infty}|x(t)|^2dt$; for a periodic signal, $P=\frac1T\int_{t_0}^{t_0+T}|x(t)|^2dt$ over ONE period $T$. Discrete periodic: $P=\frac1N\sum_{n=0}^{N-1}|x[n]|^2$.

*Apr25:* $A\sin\omega t$ → power $\tfrac{A^2}2$. $e^{-n}$ for $n\ge0$ → energy $\sum e^{-2n}=\tfrac1{1-e^{-2}}\approx1.16$ (use $\sum_{n\ge0}q^n=\tfrac1{1-q}$). *Continuous* $e^{-t}$, $t\ge0$: dies out → energy $\int_0^\infty e^{-2t}dt=\tfrac12$ (the $c=2$ line of the Calculations strip).

### 3I · Name the method

IF YOU SEE a table of descriptions to fill with method names, "name the method", bias/variance to match
{: .see }

| The description says… | Method |
|---|---|
| $\lvert\text{DFT}\rvert^2$ divided by $N$, whole signal | Periodogram |
| DFT of the estimated autocorrelation | Correlogram |
| DFT of the estimated autocorrelation, then truncate/window it at maximum lag $M\lt N$; “consistent” | Blackman–Tukey |
| NON-overlapping segments, average the periodograms | Bartlett |
| OVERLAPPING segments, average the periodograms | Welch (WOSA) |
| $\sigma^2\lvert B\rvert^2/\lvert A\rvert^2$, "linear random signal model" | Parametric (AR / MA / ARMA) |
| "averages periodograms" | Bartlett and Welch |

**How:** hunt ONE trigger word per description — even reworded, the trigger stays.

### 3J · Part 3 true / false

IF YOU SEE "which of the following statements" (in Part 3) about PSD, windows, periodogram, Welch
{: .see }


Same swap test as 2D — hunt: *improves/reduces · exactly · more/less · both/only · resolution↔leakage*.

| The fact (true) | The lie they print (false) |
|---|---|
| Periodogram is **not** consistent: bias $\to0$ but $\mathrm{Var}\{\hat P\}\approx P^2$ stays (Jun26 b) | "it is consistent" |
| Bias affects **both** deterministic and stochastic signals (Apr25 a) | "only stochastic" |
| Bartlett: variance $\propto\frac1K$, bias **up** (Nov22 a) | "variance drops by zero-padding" (it splits the data) |
| Welch (overlapping): variance drops **less** than $\frac1K$ | "exactly $\frac1K$" |
| Main-lobe width → resolution · side-lobe height → leakage (Nov22 b) | the two swapped |
| Windows (Hamming…) cut **leakage**; rectangular has best **resolution** | "a window improves resolution" · "triangular beats rectangular" |
| Zero-padding: more points (step $\frac{2\pi}L$), **no** better resolution | "improves resolution" |
| Window type does **not** change the periodogram's variance; leakage follows the window, not the record length | "longer data/window reduces leakage" |
| Periodogram and correlogram have the **same** bias | "periodogram has better bias" |

*Consistent* $=$ variance $\to0$ as $N\to\infty$. The periodogram's bias $\to0$ but $\mathrm{Var}\{\hat P\}\approx P^2$ stays put.

**AR order (Jun26-3e).** Bigger $p$ → residual error always goes down → risk: **overfitting** (fake peaks). Fix: **AIC** $=N\ln\hat\sigma^2+2p$ (also FPE, MDL): the error term falls, the penalty $2p$ grows → choose the $p$ with the smallest AIC. Any PSD can be approximated by an AR model of **high enough order**.

## PART 4 · Detection (2–2.5 p)

$H_0$ = nothing there, $H_1$ = something there. $P_{FA}$ = decide $H_1$ when $H_0$ is true (false alarm). $P_D$ = decide $H_1$ when $H_1$ is true. $P_M=1-P_D$ (miss).
{: .how }

### 4A · Likelihood-ratio test

IF YOU SEE two pdfs (one for $H_0$, one for $H_1$) + "binary hypothesis"/"hypothesis testing", "likelihood ratio test", "when accept $H_1$", threshold $\lambda,\gamma,\eta$, "$P_{FA}$"/"$P_D$"
{: .see }

1. Put $H_1$ ON TOP: <mark>$L(\mathbf x)=p(\mathbf x\mid H_1)/p(\mathbf x\mid H_0)$</mark>. For independent samples, multiply the per-sample ratios; equal exponentials combine by adding exponents. Cancel common factors.
2. Start with $L(\mathbf x)\gt\eta\Rightarrow$ decide $H_1$. Take $\ln$ on both sides (allowed because $\ln$ is increasing): $\ln L\gt\ln\eta$. Expand logs BEFORE isolating the statistic.
3. Isolate $x$, $\sum x_n$, $\sum|x_n|$, or $\sum x_n^2$. Multiplying/dividing by a negative flips $\gt$ to $\lt$; square roots need the stated domain.
4. **Check the decision side numerically:** choose one simple value on each side, evaluate $L$, and mark where $L\gt\eta$. Then compute error areas on those sides. Equality can be assigned either way for continuous pdfs (probability 0).

*Apr25* $\frac{6x^{11}}{3x^5}=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=0.68$.

*Jun26 Rayleigh:* $p(x\mid H_j)=\frac x{\sigma_j^2}e^{-x^2/(2\sigma_j^2)}$, $x\ge0$, $\sigma_1\gt\sigma_0$.<br>
**Step 1 — divide $p_1$ by $p_0$:** $x$ cancels, leaving $L=\frac{\sigma_0^2}{\sigma_1^2}\exp[\frac{x^2}{2}(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})]$.<br>
**Step 2 — use $L\gt\eta$ and take ln:** $\frac{x^2}{2}(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})\gt\ln(\eta\frac{\sigma_1^2}{\sigma_0^2})$.<br>
**Step 3 — isolate $x$:** the bracket is positive, so no inequality flip. Multiply by its reciprocal and take the positive square root: $\boxed{x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln(\eta\frac{\sigma_1^2}{\sigma_0^2})}}$. Larger separation between the pdfs → better detection.

*Apr24* Gaussian $\tfrac1{\sqrt{2\pi}}e^{-y^2/2}$ vs exponential $\tfrac14e^{-y/2}$, $\gamma=1$: the constant $\ln\tfrac{1/4}{1/\sqrt{2\pi}}=\ln\tfrac4{2.51}=-0.467$ → $-0.467+\tfrac{y^2}2-\tfrac y2\gt0$ → $y^2-y-0.934\gt0$ → root $y=\tfrac{1+\sqrt{1+3.74}}2=1.59$ → accept $H_1$ if $y\gt1.59$. $P_{FA}=Q(1.59)=0.056$, $P_D=\tfrac12e^{-0.795}=0.23$ (printed answer — that pdf is unnormalised, keep the $\tfrac12$).

*Nov22* $\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$.

**Probabilities.** $P_{FA}$ = area under the $H_0$ pdf where you decide $H_1$. $P_D$ = area under the $H_1$ pdf in the same place.<br>
Tail formulas: Gaussian $X\sim N(\mu,\sigma^2)$: $P(X\gt t)=Q((t-\mu)/\sigma)$; standard Gaussian $\mu=0,\sigma=1$ → $Q(t)$ · exponential $ce^{-cx}$, $x\ge0$: $P(X\gt t)=e^{-ct}$ and $P(X\lt t)=1-e^{-ct}$ · Rayleigh: $P(X\gt t)=e^{-t^2/(2\sigma^2)}$ · symmetric two tails $|X|\gt t$ → twice one tail. **Always use the distribution under the hypothesis named by the error:** $P_{FA}$ uses $H_0$; $P_D$ uses $H_1$.<br>
"Threshold for $P_{FA}=0.1$": set the $H_0$ area $=0.1$, solve for $t$. **Read $Q$ backwards:** with a Gaussian $H_0$ the $t$ with $Q(t)=0.1$ is $t=1.28$ (Numbers strip); then $P_D$ = area under the $H_1$ pdf from that same $t$ on.

*Nov22:* $1-e^{-t}=0.1$ → $t=-\ln0.9$; then $P_D=1-e^{-2t}=0.19$.

"Plot / indicate $P_{FA}$ and $P_M$": draw both pdfs and a vertical line at the threshold. Shade the $H_0$ curve on the "decide $H_1$" side → $P_{FA}$. Shade the $H_1$ curve on the "decide $H_0$" side → $P_M$. (Nov22: $H_1$ when $y\lt1$, so $P_{FA}$ = $H_0$ area left of 1, $P_M$ = $H_1$ area right of 1.)

**Gaussian with any $\sigma$.** $p(x)=\dfrac1{\sigma\sqrt{2\pi}}e^{-x^2/2\sigma^2}$ (mean 0). Two zero-mean Gaussians, $\sigma_1$ vs $\sigma_0$ (pe21-4b): $\ln L=N\ln\frac{\sigma_0}{\sigma_1}+\frac12\big(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\big)\sum_n x^2[n]$ → decide $H_1$ when $\sum_n x^2[n]$ is **big** = **energy detector** (bigger variance = more energy).<br>
**erf table** (printed with the question — pe21-4a). The printed formula $\frac12\big[1+\operatorname{erf}\frac{t-\mu}{\sigma\sqrt2}\big]$ gives $P(x\lt t)$, so $P(x\gt t)=1-\text{that}$. First compute $z=\frac{t-\mu}{\sigma}$, then read $\operatorname{erf}\frac{z}{\sqrt2}$ at the column $x=z$ ($x$ runs $-3$ to $3$; the value at $-z$ is minus the value at $z$).<br>
**Matched filter** (jan22-4a): correlate the data with the known signal $s[n]$ (FIR filter $h[n]=$ the **time-reversed** $s$) → biggest output SNR; "only for uncorrelated noise" is **false**.

### 4B · Priors and costs (Bayes)

IF YOU SEE priors $P(H_0),P(H_1)$, costs $C_{ij}$, "posterior", "Bayesian hypothesis test", "$P_M$" / "miss"
{: .see }

$C_{ij}$ = cost of deciding $i$ when $j$ is true. $C_{10}$ = false alarm cost, $C_{01}$ = miss cost. "Minimises the Bayes risk" = makes the total cost $C_{00}P(H_0)(1{-}P_{FA})+C_{10}P(H_0)P_{FA}+C_{11}P(H_1)P_D+C_{01}P(H_1)P_M$ as small as possible.

- Threshold <mark>$\eta=\dfrac{P(H_0)\,(C_{10}-C_{00})}{P(H_1)\,(C_{01}-C_{11})}$</mark>. Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$. Then do 4A with this $\eta$.<br>
  *Jun26-4c:* $\eta=\frac{0.9}{0.1}=9$ → put $\eta=9$ in the Rayleigh answer of 4A.
- **Posteriors given** → accept $H_1$ if $\dfrac{P(H_1\mid x)}{P(H_0\mid x)}\gt\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$.<br>
  *Apr25-4c:* $C_{01}=100\,C_{10}$ → right side $=0.01$. Posterior ratio $=5\gt0.01$ → accept $H_1$ → the student fails: **yes**.
- **"Where $p_1P_1=p_0P_0$"** ($p$ = the two pdfs, $P$ = the two priors) → write the equality and solve.<br>
  *Nov22:* $0.6\cdot2e^{-2y}=0.4\,e^{-y}$ → $e^{-y}=\frac13$ → $y=\ln3$; decide $H_1$ for $y\lt\ln3$. $P_{FA}=1-e^{-\ln3}=\frac23$, $P_M=e^{-2\ln3}=\frac19$.

### 4C · Part 4 true / false

IF YOU SEE "which of the following statements" (in Part 4) about hypothesis testing, $P_{FA}$, errors
{: .see }


Same swap test as 2D — the verb is the question: risk **min** · $P_D$ **max** · $P_e$ **min** ($P_e$ = total error $=P(H_0)P_{FA}+P(H_1)P_M$, equal costs) · $\eta$ goes **up** with $P(H_0)$, **down** with $P(H_1)$.

| The fact (true) | The lie they print (false) |
|---|---|
| Bayes detection **minimises** the Bayes risk | "maximises" |
| $C_{01}=C_{10}$, $C_{00}=C_{11}=0$ → minimises total error $P_e$ | *trap:* scaling all costs leaves $\eta$ unchanged |
| Equal priors + equal costs → maximum-likelihood rule | — |
| Higher $P(H_0)$ raises $\eta$ → harder to pick $H_1$ | "higher $P(H_1)$ raises $\eta$" (lowers — Jun26 c) |
| Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$ | "minimise $P_D$" · "fix $P_D$, max $P_{FA}$" |
| NP's solution is the LRT; the LRT itself needs **no** priors | "the LRT needs $P_0,P_1$" |
| $\ln$ of the ratio never changes the decisions | "changes the decisions" |
| Errors are unavoidable: the pdfs overlap | "a threshold kills both errors" |
| ROC = $P_D$ plotted against $P_{FA}$ as the threshold moves: up and right · diagonal = guessing · better = top-left | "below diagonal = wrong $\sigma$" (flipped) |
| miss = false negative = type II · false alarm = false positive = type I (Nov22) | labels swapped |

Matched filter & energy-detector sentences → the last blocks of 4A: time-reversed $s$ · "only for uncorrelated noise" **false** · $\sum x^2$ **big** · a narrow $H_1$ pdf → the sum comes out **small**.

## Calculations · the algebra under every answer

**Integrals.** These formulas are **printed in the question itself** (q3-23-2h, nov22-2f) — you copy them: $\int e^{cx}dx=\frac1ce^{cx}$ · $\int xe^{cx}dx=\frac{cx-1}{c^2}e^{cx}$ · $\int x^2e^{cx}dx=\big(\frac{x^2}{c}-\frac{2x}{c^2}+\frac{2}{c^3}\big)e^{cx}$ · $\int x^2e^{-x}dx=-e^{-x}(x^2+2x+2)$ (by parts twice) · $\int\cos u\,du=\sin u$ · $\int\sin u\,du=-\cos u$.
Evaluate $[F(x)]_a^b=F(b)-F(a)$: at $x=\infty$ only $e^{cx}$ with $c\lt0$ becomes 0, at $x=0$ every $x$ is 0 so only the plain number is left → $\int_0^\infty e^{-cx}dx=\frac1c$ · $\int_0^\infty xe^{-cx}dx=\frac1{c^2}$ · $\int_0^\infty x^2e^{-cx}dx=\frac2{c^3}$.<br>
*Nov22-2f:* MMSE $=\dfrac{\int_0^\infty\theta\cdot\theta e^{-(x+a)\theta}d\theta}{\int_0^\infty\theta e^{-(x+a)\theta}d\theta}=\dfrac{2/(x+a)^3}{1/(x+a)^2}=\dfrac2{x+a}$.

**$\ln$ and $e$.** $\ln(ab)=\ln a+\ln b$ · $\ln\frac ab=\ln a-\ln b$ · $\ln a^k=k\ln a$ · $\ln e^a=a$ · $e^{\ln a}=a$ · $e^ae^b=e^{a+b}$.<br>
Get the letter alone: $e^{ky}=A$ → $y=\frac{\ln A}{k}$ · $x^k=a$ → $x=a^{1/k}$ · $y=k\ln x$ → $x=e^{y/k}$.

**Derivatives.** $(c)'=0$ · $(\theta^k)'=k\theta^{k-1}$ · $(1/\theta)'=-1/\theta^2$ · $(\ln\theta)'=1/\theta$ · $(e^{u(\theta)})'=e^{u(\theta)}u'(\theta)$ · $[\ln f(\theta)]'=f'(\theta)/f(\theta)$ · $(uv)'=u'v+uv'$ · $\cos'\!=-\sin$, $\sin'\!=\cos$. Differentiating with respect to $\theta$ means all $x_n$ are constants.

**Sums.** $\sum_{n\ge0}q^n=\frac1{1-q}$ for $|q|\lt1$ · $\sum_n x_n=N\bar x$ · $\sum_n c=Nc$ · $\sum_n(x_n-\bar x)=0$ · $\sum_n(ax_n+b)=a\sum_nx_n+Nb$.

**Fractions & equations.** $\frac ab\pm\frac cd=\frac{ad\pm bc}{bd}$ · $\frac ab\div\frac cd=\frac{ad}{bc}$ · $\frac ab=\frac cd$ → $ad=bc$ · $ax^2+bx+c=0$ → $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ · multiplying by a negative flips $\gt$ into $\lt$ · $\lvert x\rvert\gt t$ = two cases.

**Numbers / Gaussian tail.** $\ln2=0.693$ · $\ln3=1.099$ · $\ln10=2.303$ · $e^{-2}=0.135$ · $\sqrt{2\pi}=2.5066$ · $Q(-t)=1-Q(t)$ · $Q(0)=0.5$ · $Q(1)=0.1587$ · $Q(1.28)=0.10$ · $Q(1.645)=0.05$ · $Q(1.96)=0.025$ · $Q(2.33)=0.01$. For a two-sided interval $\pm t$, central area $=1-2Q(t)$.

## Calculation rescue · when an algebra step stops you

**1 · Exponential integral: antiderivative, THEN limits.** To calculate $\int_0^\infty\theta e^{-b\theta}d\theta$ with $b\gt0$, use the $x e^{cx}$ formula above with $x=\theta$, $c=-b$: $\int\theta e^{-b\theta}d\theta=-e^{-b\theta}(\theta/b+1/b^2)$. At $\infty$, $e^{-b\theta}=0$, so the upper value is 0. At 0, the value is $-1/b^2$. Upper minus lower gives $\boxed{0-(-1/b^2)=1/b^2}$. Do not forget to subtract the lower value.
{: .rescue }

**2 · Where the Beta MAP formula comes from.** If $q=\theta^A(1-\theta)^B$, then $\ln q=A\ln\theta+B\ln(1-\theta)$. Differentiate: $A/\theta-B/(1-\theta)$. Set equal to 0: $A/\theta=B/(1-\theta)$ → $A(1-\theta)=B\theta$ → $A=(A+B)\theta$ → $\boxed{MAP=A/(A+B)}$. This is why you only need the final exponents in 2B.
{: .rescue }

**3 · Where the Gamma MAP formula comes from.** If $q=\lambda^Ae^{-B\lambda}$, then $\ln q=A\ln\lambda-B\lambda$. Differentiate: $A/\lambda-B$. Set to 0 → $A/\lambda=B$ → $A=B\lambda$ → $\boxed{MAP=A/B}$. MMSE is NOT the peak; use the table’s posterior mean $(A+1)/B$.
{: .rescue }

**4 · A negative power in an MLE derivative.** $\frac{d}{d\theta}[-\frac{S}{2\theta}]=\frac{d}{d\theta}[-\frac S2\theta^{-1}]=-\frac S2(-1)\theta^{-2}=\boxed{+\frac{S}{2\theta^2}}$. Here $S=\sum x_n^2$ is constant while differentiating with respect to $\theta$. The two minus signs cancel.
{: .rescue }

**5 · Solving an exponential threshold.** $e^{-ct}=a$ → take $\ln$: $-ct=\ln a$ → $\boxed{t=-\ln(a)/c}$. Example: $e^{-2t}=0.1$ → $-2t=\ln0.1=-2.303$ → $t=1.151$. If the equation has $e^{-ct}$ on the OTHER side, first isolate it by division.
{: .rescue }

**6 · Quadratic formula and choosing the MA root.** For $b^2+8b+1=0$, use $a=1,b_{quad}=8,c=1$: $b=\frac{-8\pm\sqrt{64-4}}2=-4\pm\sqrt{15}$. The two values are $-0.127$ and $-7.873$; MA(1) keeps $\boxed{-4+\sqrt{15}=-0.127}$ because $|b|\lt1$. Do not confuse the coefficient $b$ in the quadratic formula with the MA parameter.
{: .rescue }

**7 · AR(2): the jump from coefficients to the final PSD.** Jun26 has $a_1=-\tfrac45$, $a_2=\tfrac15$, $\sigma^2=\tfrac85$. Compute the denominator pieces separately: $1+a_1^2+a_2^2=1+\tfrac{16}{25}+\tfrac1{25}=\tfrac{42}{25}$ · $2a_1(1+a_2)=2(-\tfrac45)(\tfrac65)=-\tfrac{48}{25}$ · $2a_2=\tfrac25$. Therefore $P=\dfrac{8/5}{42/25-(48/25)\cos\theta+(2/5)\cos2\theta}$. Now replace $\cos2\theta=2\cos^2\theta-1$: constant $=\tfrac{42}{25}-\tfrac25=\tfrac{32}{25}$ and $\cos^2$ coefficient $=\tfrac45$. Multiplying top and bottom by 25 gives $\dfrac{40}{32-48\cos\theta+20\cos^2\theta}=\boxed{\dfrac{10}{8-12\cos\theta+5\cos^2\theta}}$.
{: .rescue }

**8 · Correlogram: the jump to a perfect square.** Let $c=\cos\theta$. For Jun26: $3+4c+2\cos2\theta=3+4c+2(2c^2-1)=3+4c+4c^2-2=\boxed{4c^2+4c+1=(2c+1)^2}$. A squared PSD is nonnegative, which is a useful check.
{: .rescue }

**9 · Sums with actual numbers.** For $x=[1,2,3]$, $N=3$ and $\bar x=(1+2+3)/3=2$. $\sum x_n^2=1^2+2^2+3^2=14$ · $\sum(x_n-\bar x)^2=(-1)^2+0^2+1^2=2$ · $\hat r[0]=14/3$ · $\hat r[1]=(1\cdot2+2\cdot3)/3=8/3$ · $\hat r[2]=(1\cdot3)/3=1$. The sums have fewer products as the lag grows, but the denominator stays $N=3$.
{: .rescue }

**10 · $P_{FA}$ and $P_D$: same decision region, different pdf.** Suppose you decide $H_1$ when $x\gt t$, with $p(x\mid H_0)=e^{-x}$ and $p(x\mid H_1)=2e^{-2x}$, $x\ge0$. Then $P_{FA}=\int_t^\infty e^{-x}dx=[-e^{-x}]_t^\infty=0-(-e^{-t})=e^{-t}$. Use the SAME limits under $H_1$: $P_D=\int_t^\infty2e^{-2x}dx=[-e^{-2x}]_t^\infty=e^{-2t}$. If $P_{FA}=0.1$, then $e^{-t}=0.1$ → $t=-\ln0.1=2.303$ and $P_D=e^{-2(2.303)}=0.01$. Do not integrate $H_1$ for $P_{FA}$.
{: .rescue }

**Final 10-second rescue.** Integral → integrate first, substitute upper and lower second · multiplication inside $\ln$ → addition outside · division inside $\ln$ → subtraction · derivative → letters other than the unknown are constants · multiplying an inequality by a negative → flip it · finish with a range/sign/probability check.

</div>
</div>
