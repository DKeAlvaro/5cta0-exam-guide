---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet</h1>

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This sheet fills both sides: print <code>cheatsheet.pdf</code> at 100 %, or Ctrl/Cmd + P → A4, margins minimal, untick "headers and footers", scale 83 %.</p>
<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## PART 1 · Probability (1.5 p)

### 1A · Joint PDF $p(x,y)$

IF YOU SEE a formula $p(x,y)$ on a region + "find $c$" / "marginal" / "conditional" / "independent"
{: .see }

First draw the region on $x$–$y$ axes: **every integral below takes its limits from that picture**, never from the formula.

- **"Find $c$"** → integrate $p$ over the whole region, set the result $=1$, solve for $c$.<br>
  **Limits in 4 moves.** (1) Choose the order $dx\,dy$ = inner $x$, outer $y$ (the other order works too). (2) Freeze the outer letter at one value. (3) Inner limits: "from where to where can the inner letter move now?" — they may contain the outer letter ($x$ from $0$ to $1-y$). (4) Outer limits: the full range of the frozen letter, always plain numbers ($y$ from $0$ to $1$). Rectangle → both limits are numbers, order free. Triangle/wedge → one limit is an expression in the other letter.<br>
  *Apr25:* $cx+1$ on the triangle $x,y\ge0$, $x+y\lt1$: $\int_0^1\!\int_0^{1-y}(cx+1)\,dx\,dy=\frac c6+\frac12=1$ → $c=3$.
- **"Marginal $p_X(x)$"** → integrate the OTHER letter away: $p_X(x)=\int p(x,y)\,dy$, inner limits as in move 3. Range of $x$ = the region's shadow on the $x$ axis; write it and "0 otherwise".<br>
  *Jun26:* $6x^2y$ on the square $0\le x,y\le1$: $p_X=\int_0^1 6x^2y\,dy=3x^2$ for $0\le x\le1$. Same way $p_Y=2y$.
- **"Conditional $p(x\mid y)$"** → $p(x,y)$ divided by $p_Y(y)$; state the ranges ($y$ over its shadow, $x$ over the slice at that $y$).<br>
  *Apr24:* $p=2$ on $0\le y\le x\le1$: $p_Y=\int_y^1 2\,dx=2(1-y)$ → $p(x\mid y)=\frac1{1-y}$ for $y\le x\le1$.
- **"Independent?"** → YES only if the region is a rectangle AND $p(x,y)=p_X(x)\cdot p_Y(y)$.<br>
  *Jun26:* square, and $3x^2\cdot2y=6x^2y$ → independent. A triangle region → never independent.

Integral: $\int x^n\,dx=\frac{x^{n+1}}{n+1}$; plug in the top limit minus the bottom limit.

### 1B · WSS / ergodic (multiple choice)

IF YOU SEE "wide-sense stationary", "ergodic", dice, random phase, random amplitude
{: .see }

- **WSS** = the mean is constant AND the autocorrelation depends only on the lag $\tau$ (not on $t$). Jun26: pick the option saying exactly this.
- **Ergodic** = averaging ONE signal over time gives the same as averaging over all signals.

| The process | WSS? | Ergodic? |
|---|---|---|
| $\cos(t+U)$, $U$ uniform $0..2\pi$ (random phase) | yes | yes |
| $A\cos t$, $A$ random (random amplitude) | no | no |
| Many fair dice, each rolled forever | yes | yes, in mean AND variance |
| Numbers uniform in $[-A,A]$, $A$ random (Nov22) | yes, mean 0 | key: ergodic, mean 0 → (d) |

### 1C · Spectral factorisation

IF YOU SEE $P(\theta)=\dfrac{\text{number}}{A+B\cos\theta}$ + "spectral factorisation", "innovation filter $L(z)$", "$\sigma_i^2$"
{: .see }

1. Two candidate roots: $r=\dfrac{A\pm\sqrt{A^2-B^2}}{B}$. Keep the one between $-1$ and $1$. Call it $a$.
2. $C=\dfrac{B}{2a}$.
3. Answer: $\sigma_i^2=\dfrac{\text{number on top}}{C}$ and $L(z)=\dfrac{1}{1+a\,z^{-1}}$.
4. Check: $|a|\lt1$ and $\sigma_i^2\gt0$ — a negative $\sigma_i^2$ means you kept the wrong root.

*Apr24* $\frac{7}{25-24\cos\theta}$: $A=25$, $B=-24$, $\sqrt{625-576}=7$, $r=\frac{25\pm7}{-24}$ = $-\frac43$ or $-\frac34$ → $a=-\frac34$. $C=\frac{-24}{-3/2}=16$. So $\sigma_i^2=\frac7{16}$, $L=\frac1{1-\frac34z^{-1}}$.

*Apr25* $\frac{1}{61+60\cos\theta}$: $r=\frac{61\pm11}{60}$ → $a=\frac56$, $C=36$, $\sigma_i^2=\frac1{36}$, $L=\frac1{1+\frac56z^{-1}}$.

Multiple choice "what must the innovation filter be?" → **minimum phase**: all poles and zeros inside the unit circle (Jun26 a).

## PART 2 · Estimation (3–3.5 p)

### 2A · Maximum likelihood (MLE)

IF YOU SEE a pdf $p(x\mid\theta)$, samples $x_1..x_N$, "maximum likelihood", "derive the MLE"
{: .see }

1. Take $\ln$ of ONE sample's pdf, then put $\sum_n$ in front. That is $\ln L$. A term without $x_n$ gets multiplied by $N$.
2. Differentiate with respect to $\theta$ (terms without $\theta$ disappear).
3. Set it $=0$ and solve for $\theta$. That is $\hat\theta$.

**How to take $\ln$ of a pdf:** split it into pieces that multiply, and turn each piece into a plus/minus term: a factor on top → $+\ln(\text{it})$; a factor on the bottom → $-\ln(\text{it})$; $\theta^k$ on the bottom → $-k\ln\theta$; $e^{\text{stuff}}$ → just "stuff" (the $e$ disappears).
Derivatives: $\ln\theta\to\frac1\theta$ · $\frac1\theta\to-\frac1{\theta^2}$ · $\theta^k\to k\theta^{k-1}$ · $e^{c\theta}\to ce^{c\theta}$.
Solving $=0$: multiply the equation by the denominators ($\theta^2$, $\theta$, …) first — that does not change the root.

*Apr24* $\frac{x}{2\theta}e^{-x^2/2\theta}$: one sample gives $\ln x-\ln2-\ln\theta-\frac{x^2}{2\theta}$, so $\ln L=\sum\ln x_n-N\ln2-N\ln\theta-\frac{\sum x_n^2}{2\theta}$ → $-\frac N\theta+\frac{\sum x_n^2}{2\theta^2}=0$ → $\hat\theta=\frac1{2N}\sum x_n^2$.

*Jun26* Gamma $\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$, $n$ patients: $-\frac{nk}\theta+\frac{\sum x_i}{\theta^2}=0$ → $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}k$. Meaning: average time per stage, so $k\hat\theta$ = the observed mean time.

**Sigmoid trick.** IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then convert with $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.

*Apr25* $3\lambda e^{-4\lambda x/7}$: $\frac1\lambda-\frac{4x}7=0$ → $\hat\lambda=\frac7{4x}$ → $\hat\theta=-\ln\!\big(\frac{4x}7-1\big)$, valid for $x\gt\frac74$.

### 2B · MAP with a prior (Beta / Gamma)

IF YOU SEE "prior", "posterior", "MAP", "maximum a posteriori", Beta, Gamma
{: .see }

1. Likelihood: write each observation's probability, keep only the parts with $\theta$, multiply them all (exponents add).
2. Multiply by the prior (exponents add again). Drop numbers without $\theta$.
3. Read the shape and use the table:

| Result looks like | Posterior | MAP | MMSE (mean) |
|---|---|---|---|
| $\theta^{A}(1-\theta)^{B}$ | Beta$(A{+}1,B{+}1)$ | $\frac{A}{A+B}$ | $\frac{A+1}{A+B+2}$ |
| $\lambda^{A}e^{-B\lambda}$ | Gamma$(A{+}1,B)$ | $\frac{A}{B}$ | $\frac{A+1}{B}$ |

Prior Beta$(a,b)$ = $\theta^{a-1}(1-\theta)^{b-1}$. Prior Gamma$(a,b)$ = $\lambda^{a-1}e^{-b\lambda}$.
One observation $x$ gives: Poisson count → $\lambda^{x}e^{-\lambda}$ · "$k$-th success on trial $x$" → $\theta^k(1-\theta)^{x-k}$ · "$k$ successes in $n$ tries" → $\theta^k(1-\theta)^{n-k}$ · exponential → $\lambda e^{-\lambda x}$.

*Jun26-2c:* $\theta^2(1-\theta)^{x-2}$ with $x=3,5,4,6,4$. Multiply the 5: the $\theta$ exponent is $2$ five times $=10$; the $(1-\theta)$ exponent is $(3-2)+(5-2)+(4-2)+(6-2)+(4-2)=12$ → $\theta^{10}(1-\theta)^{12}$ (likelihood). Prior Beta(2,3) adds $\theta^{2-1}(1-\theta)^{3-1}=\theta^1(1-\theta)^2$ → $\theta^{11}(1-\theta)^{14}$ → posterior Beta(12,15), MAP $=\frac{11}{25}=0.44$.

*Jun26-2d:* Poisson, $x=2,4,3,5,2,4$. Each day gives $\lambda^{x}e^{-\lambda}$: the $\lambda$ exponents add to $20$, the six $e^{-\lambda}$ give $e^{-6\lambda}$ → $\lambda^{20}e^{-6\lambda}$. Prior Gamma(3,2) adds $\lambda^{3-1}e^{-2\lambda}=\lambda^2e^{-2\lambda}$ → $\lambda^{22}e^{-8\lambda}$ → Gamma(23,8), MAP $=\frac{22}8=2.75$. MLE $=\frac{20}6=3.33$: the prior pulls the estimate towards its own mean $\frac32$.

*Apr25-2d:* posterior already given as $\theta^{a}(1-\theta)^{b}$ → MAP $=\frac a{a+b}$.

*Nov22:* posterior $\lambda e^{-(x+a)\lambda}$ → MAP $\frac1{x+a}$, MMSE $\frac2{x+a}$.

*Apr24-2d (sigmoid):* posterior $\frac\lambda2e^{-\lambda x/2}$ → $\frac1\lambda-\frac x2=0$ → $\lambda=\frac2x$ → $\hat\theta=-\ln\!\big(\frac x2-1\big)$, $x\gt2$.

### 2C · Least-squares line

IF YOU SEE points $(x,y)$ + "least squares", "linear function"
{: .see }

1. Means $\bar x$ and $\bar y$.
2. Slope $a=\dfrac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}$.
3. $b=\bar y-a\bar x$. Answer: $y=ax+b$. Check: $x=\bar x$ must give $y=\bar y$.

*Apr25* $(0,3),(2,4),(3,3)$: $\bar x=\frac53$, $\bar y=\frac{10}3$, $a=\frac{1/3}{14/3}=\frac1{14}$, $b=\frac{45}{14}$ → $y=\frac1{14}x+\frac{45}{14}$.

Also: $x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$. $x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$.

### 2D · Part 2 true / false


| Statement | T / F |
|---|---|
| MMSE = the **mean** of the posterior; minimises squared error | T |
| MMSE = the maximum of the posterior | F (that is MAP) |
| MMSE and MAP **always** give different estimates | F (same for a symmetric posterior) |
| MAP always equals the posterior mean | F |
| MAP depends on likelihood and prior; needs a prior | T (Jun26 c) |
| MAP → MLE for many samples "regardless of the prior" | F |
| Bayesian estimators do not use prior knowledge | F |
| Bayes estimate minimises the Bayes risk | T (Nov22 b) |
| Uniform cost → MMSE | F (uniform → MAP) |
| MLE maximises the likelihood over $\theta$ | T ("over $x$": F) |
| MLE is asymptotically unbiased | T (Nov22 c) |
| MLE always reaches the CRLB / only for linear models | F |
| MLE of $\alpha=\psi(\theta)$: $\hat\theta=\psi^{-1}(\hat\alpha)$ | T (Jan22 c) |
| Fisher info of $N$ iid samples $=N\,i(\theta)$ | T |
| $\mathrm{Var}(\hat\theta)\ge\mathcal I(\theta)$ | F (it is $\ge\frac1{\mathcal I}$) |
| Fisher information is strictly negative | F (it is $\ge0$) |
| CRLB can always be derived | F (not if the range of $x$ depends on $\theta$) |
| Variance below the CRLB = efficient | F (efficient = equal to it) |
| CRLB decreases as $N$ grows ($\sim\frac1N$) | T |

Fisher info for "$x$ = signal($\theta$) + Gaussian noise $\sigma^2$": $\mathcal I=\frac1{\sigma^2}\sum\big(\frac{d\,\text{signal}}{d\theta}\big)^2$.

*Nov22* $A[\cos\theta,\sin\theta]$ → $\mathcal I=\frac{A^2}{\sigma^2}$, and MLE $\hat\theta=\arctan\frac{x_2}{x_1}$.

## PART 3 · Spectral estimation (3 p)

$r[k]$ = autocorrelation at lag $k$ (the given numbers). Rewrite cosines: $\cos2\theta=2\cos^2\theta-1$, $\cos3\theta=4\cos^3\theta-3\cos\theta$.
{: .how }

### 3A · Correlogram

IF YOU SEE $r[0],r[1],r[2]\dots$ + "correlogram", "only these lags", "PSD as a function of $\cos\theta$"
{: .see }

$P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta$. Stop at the last lag given. $r[0]$ is NOT doubled.

*Jun26* $3,2,1$: $3+4\cos\theta+2\cos2\theta=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$.

*Apr24* $\frac{25}{16},-\frac34,\frac12,-\frac12$: $\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$.

### 3B · AR(1)

IF YOU SEE "AR(1)", "first-order autoregressive"
{: .see }

1. $a=-\dfrac{r[1]}{r[0]}$
2. $\sigma^2=r[0]+a\,r[1]$
3. $P=\dfrac{\sigma^2}{1+a^2+2a\cos\theta}$ (check $|a|\lt1$ and $\sigma^2\gt0$, else a sign went wrong)

*Apr25* $r=2,-\frac14$: $a=\frac18$, $\sigma^2=\frac{63}{32}$, $P=\frac{126}{65+16\cos\theta}$.

### 3C · AR(2) / Yule–Walker

IF YOU SEE "AR(2)", "Yule–Walker", $r[0],r[1],r[2]$
{: .see }

1. $D=r[0]^2-r[1]^2$
2. $a_1=\dfrac{-r[1]\,(r[0]-r[2])}{D}$,  $a_2=\dfrac{r[1]^2-r[0]\,r[2]}{D}$
3. $\sigma^2=r[0]+a_1r[1]+a_2r[2]$
4. $P=\dfrac{\sigma^2}{1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta}$

If they want the matrix: $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$.

*Jun26* $3,2,1$: $D=5$, $a_1=-\frac45$, $a_2=\frac15$, $\sigma^2=\frac85$, $P=\frac{10}{5\cos^2\theta-12\cos\theta+8}$.

### 3D · MA(1)

IF YOU SEE "MA(1)", "moving average"
{: .see }

PSD: $P=r[0]+2r[1]\cos\theta$. Ignore $r[2]$ and beyond.
If they ask for $b$ and $\sigma^2$: solve $b^2-\frac{r[0]}{r[1]}\,b+1=0$, keep the root between $-1$ and $1$; then $\sigma^2=\frac{r[1]}{b}$.

*Apr25* $r=2,-\frac14$: $P=2-\frac12\cos\theta$.

### 3E · Model from an equation

IF YOU SEE $x[n]=\dots$ + "which kind of process", "autocorrelation of $x$"
{: .see }

- Only $i[n],i[n-1],\dots$ on the right → **MA($q$)**, $q$ = biggest delay. Old $x[n-k]$ on the right too → **ARMA($p,q$)**, $p$ = biggest $x$ delay.
- MA autocorrelation: list the coefficients $1,b_1,b_2,\dots$. $r[k]=\sigma^2\times$(sum of products of coefficients that are $k$ places apart). Zero after lag $q$. So $r[0]$ = sum of the squares; $r[1]$ = each one times its right-hand neighbour ($1\cdot b_1+b_1b_2+\dots$); $r[2]$ = skip one ($1\cdot b_2+b_1b_3+\dots$).<br>
  *Apr24* $1,-\frac12,\frac14,-\frac12$ (MA(3), $\sigma^2=1$): $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$, $r[1]=-\frac12-\frac18-\frac18=-\frac34$, $r[2]=\frac14+\frac14=\frac12$, $r[3]=-\frac12$.
- ARMA(1,1) written as $x[n]+\alpha x[n-1]=i[n]+\beta i[n-1]$: $P=\sigma^2\dfrac{1+\beta^2+2\beta\cos\theta}{1+\alpha^2+2\alpha\cos\theta}$.<br>
  *Nov22* $x[k]=i[k]-i[k-1]+\frac34x[k-1]$: $\alpha=-\frac34$, $\beta=-1$, $\sigma^2=\frac78$ → $P=\frac{28(1-\cos\theta)}{25-24\cos\theta}$.

### 3F · Pick the plot

IF YOU SEE "which plot", "which figure"
{: .see }

Work out each PSD at $\theta=0$ (all cosines $=1$) and at $\theta=\pi$ ($\cos\theta=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Pick the plot with those heights. Only a correlogram can go below 0.

*Apr25:* correlogram $1.13\to2.13$, MA $1.5\to2.5$, AR $1.56\to2.57$ → plot D.

### 3G · Welch / Bartlett count

IF YOU SEE $N$ samples, segment length $L$, overlap %
{: .see }

Step $D=L\times(1-\text{overlap})$. Segments $K=\frac{N-L}{D}+1$ (round the fraction down). Variance ratio vs one periodogram $=\frac1K$. Bartlett (no overlap): $K=\frac NL$.

*Jun26* $N=1000$, $L=200$, 50 %: $D=100$, $K=9$, ratio $\frac19$.

### 3H · Energy or power signal

IF YOU SEE "energy or power signal"
{: .see }

- Dies out or has finite length → **energy**: $E=\sum\lvert x\rvert^2$ is finite, power $=0$.
- Never dies out (sin, cos, constant, $\cos t\,u(t)$) → **power**: $P$ = time average of $\lvert x\rvert^2$, energy $=\infty$.
- Time-continuous ($t$) → $\sum$ becomes $\int dt$: $E=\int\lvert x\rvert^2dt$, $P=\frac1T\int_0^T\lvert x\rvert^2dt$.

*Apr25:* $A\sin\omega t$ → power $\frac{A^2}2$. $e^{-n}$ for $n\ge0$ → energy $\sum e^{-2n}=\frac1{1-e^{-2}}\approx1.16$ (use $\sum_{n\ge0}q^n=\frac1{1-q}$).

### 3I · Name the method

IF YOU SEE a table of descriptions to fill with method names
{: .see }

| The description says… | Method |
|---|---|
| $\lvert\text{DFT}\rvert^2$ divided by $N$, whole signal | Periodogram |
| DFT of the estimated autocorrelation | Correlogram |
| …plus a window of length $M\lt L$ on the autocorrelation; "consistent" | Blackman–Tukey |
| NON-overlapping segments, average the periodograms | Bartlett |
| OVERLAPPING segments, average the periodograms | Welch (WOSA) |
| $\sigma^2\lvert B\rvert^2/\lvert A\rvert^2$, "linear random signal model" | Parametric (AR / MA / ARMA) |
| "averages periodograms" | Bartlett and Welch |

### 3J · Part 3 true / false


| Statement | T / F |
|---|---|
| Periodogram NOT consistent: variance does not go to 0 as $N\to\infty$ | T (Jun26 b) |
| Bias affects deterministic and stochastic signals | T (Apr25 a) |
| Bartlett: variance drops like $\frac1K$, but bias increases | T (Nov22 a) |
| Welch/WOSA: variance drops exactly $\frac1K$ | F (overlapping segments are correlated) |
| Main-lobe width → resolution; side-lobe height → leakage | T (Nov22 b) |
| A window (Hamming…) improves resolution | F (it lowers leakage; rectangular = best resolution) |
| Triangular window: better resolution than rectangular | F |
| Longer data or window reduces leakage | F |
| Zero-padding improves resolution | F (only more points, step $\frac{2\pi}L$) |
| Bartlett reduces variance by zero-padding | F (it splits the data) |
| Window type changes the periodogram's variance | F |
| Periodogram better bias than correlogram | F (they are the same) |

**AR order (Jun26-3e).** Bigger $p$ → residual error always goes down → risk: **overfitting** (fake peaks). Fix: **AIC** $=N\ln\hat\sigma^2+2p$ (also FPE, MDL): the error term falls, the penalty $2p$ grows → choose the $p$ with the smallest AIC. Any PSD can be approximated by an AR model of **high enough order**.

## PART 4 · Detection (2–2.5 p)

$H_0$ = nothing there, $H_1$ = something there. $P_{FA}$ = decide $H_1$ when $H_0$ is true (false alarm). $P_D$ = decide $H_1$ when $H_1$ is true. $P_M=1-P_D$ (miss).
{: .how }

### 4A · Likelihood-ratio test

IF YOU SEE two pdfs (one for $H_0$, one for $H_1$) + "likelihood ratio test", "when accept $H_1$", threshold $\lambda,\gamma,\eta$
{: .see }

1. $L(x)=\dfrac{p(x\mid H_1)}{p(x\mid H_0)}$. Cancel what appears on top and bottom. $N$ samples → multiply them ($e^ae^b=e^{a+b}$).
2. Decide $H_1$ if $L\gt$ threshold. Take $\ln$ of both sides.
3. Get $x$ alone. Multiplying or dividing by a negative number flips $\gt$ into $\lt$.
4. Check the side: put a small and a large $x$ into $L$. Where $L$ comes out bigger than the threshold, that side is "decide $H_1$".

*Apr25* $\frac{6x^{11}}{3x^5}=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=0.68$.

*Jun26 Rayleigh* $\frac x{\sigma^2}e^{-x^2/2\sigma^2}$ ($\sigma_1\gt\sigma_0$): the $x$ in front cancels, so $L=\frac{\sigma_0^2}{\sigma_1^2}\,e^{\frac{x^2}2\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)}\gt\eta$ → accept $H_1$ if

$$x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\Big(\eta\,\frac{\sigma_1^2}{\sigma_0^2}\Big)}$$

Bigger gap between $\sigma_0$ and $\sigma_1$ → the pdfs overlap less → more $P_D$ for the same $P_{FA}$ (better ROC).

*Apr24* $\frac1{\sqrt{2\pi}}e^{-y^2/2}$ vs $\frac14e^{-y/2}$, $\gamma=1$: $L=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}\gt1$; take $\ln$: $-0.467+\frac{y^2}2-\frac y2\gt0$ → $y^2-y-0.934\gt0$ → root $y=\frac{1+\sqrt{1+3.74}}2=1.59$ → accept $H_1$ if $y\gt1.59$. $P_{FA}=Q(1.59)=0.056$, $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac12e^{-0.795}=0.23$.

*Nov22* $\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$.

**Probabilities.** $P_{FA}$ = area under the $H_0$ pdf where you decide $H_1$. $P_D$ = area under the $H_1$ pdf in the same place.<br>
Tails: Gaussian $N(0,1)$: $P(x\gt t)=Q(t)$ (table) · exponential $ce^{-cx}$: $P(x\gt t)=e^{-ct}$ · Rayleigh: $P(x\gt t)=e^{-t^2/2\sigma^2}$ · two tails $\lvert x\rvert\gt t$ → double.<br>
"Threshold for $P_{FA}=0.1$": set the $H_0$ area $=0.1$, solve for $t$.

*Nov22:* $1-e^{-t}=0.1$ → $t=-\ln0.9$; then $P_D=1-e^{-2t}=0.19$.

"Plot / indicate $P_{FA}$ and $P_M$": draw both pdfs and a vertical line at the threshold. Shade the $H_0$ curve on the "decide $H_1$" side → $P_{FA}$. Shade the $H_1$ curve on the "decide $H_0$" side → $P_M$. (Nov22: $H_1$ when $y\lt1$, so $P_{FA}$ = $H_0$ area left of 1, $P_M$ = $H_1$ area right of 1.)

### 4B · Priors and costs (Bayes)

IF YOU SEE priors $P(H_0),P(H_1)$, costs $C_{ij}$, "posterior"
{: .see }

$C_{ij}$ = cost of deciding $i$ when $j$ is true. $C_{10}$ = false alarm cost, $C_{01}$ = miss cost.

- Threshold $\eta=\dfrac{P(H_0)\,(C_{10}-C_{00})}{P(H_1)\,(C_{01}-C_{11})}$. Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$. Then do 4A with this $\eta$.<br>
  *Jun26-4c:* $\eta=\frac{0.9}{0.1}=9$ → put $\eta=9$ in the Rayleigh answer of 4A.
- **Posteriors given** → accept $H_1$ if $\dfrac{P(H_1\mid x)}{P(H_0\mid x)}\gt\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$.<br>
  *Apr25-4c:* $C_{01}=100\,C_{10}$ → right side $=0.01$. Posterior ratio $=5\gt0.01$ → accept $H_1$ → the student fails: **yes**.
- **"Where $p_1P_1=p_0P_0$"** → write the equality and solve.<br>
  *Nov22:* $0.6\cdot2e^{-2y}=0.4\,e^{-y}$ → $e^{-y}=\frac13$ → $y=\ln3$; decide $H_1$ for $y\lt\ln3$. $P_{FA}=1-e^{-\ln3}=\frac23$, $P_M=e^{-2\ln3}=\frac19$.

### 4C · Part 4 true / false


| Statement | T / F |
|---|---|
| Bayes detection **minimises** the Bayes risk (average cost) | T ("maximises": F) |
| $C_{01}=C_{10}$ (1, 10, any equal value), $C_{00}=C_{11}=0$ → minimises total error probability | T |
| Equal priors + equal costs → maximum-likelihood rule | T |
| Higher $P(H_0)$ raises $\eta$ → harder to pick $H_1$ | T |
| Higher $P(H_1)$ raises $\eta$ | F (it lowers it) — Jun26 c |
| Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$ | T ("minimise": F) |
| ROC = $P_D$ against $P_{FA}$; diagonal = guessing; better → top-left | T |

Error table (rows = decision, columns = truth): decide $H_0$ & true $H_0$ = true negative · decide $H_0$ & true $H_1$ = miss, false negative, type II · decide $H_1$ & true $H_0$ = false alarm, false positive, type I · decide $H_1$ & true $H_1$ = detection, true positive (Nov22 a).

## Calculations · the algebra under every answer

**Integrals.** The exam hands these out (q3-23-2h, nov22-2f): $\int e^{cx}dx=\frac1ce^{cx}$ · $\int xe^{cx}dx=\frac{cx-1}{c^2}e^{cx}$ · $\int x^2e^{cx}dx=\big(\frac{x^2}{c}-\frac{2x}{c^2}+\frac{2}{c^3}\big)e^{cx}$ · $\int x^2e^{-x}dx=-e^{-x}(x^2+2x+2)$ (by parts twice).
Evaluate $[F(x)]_a^b=F(b)-F(a)$: at $x=\infty$ only $e^{cx}$ with $c\lt0$ becomes 0, at $x=0$ only the plain number survives → $\int_0^\infty e^{-cx}dx=\frac1c$ · $\int_0^\infty xe^{-cx}dx=\frac1{c^2}$ · $\int_0^\infty x^2e^{-cx}dx=\frac2{c^3}$.<br>
*Nov22-2f:* MMSE $=\dfrac{\int_0^\infty\theta\cdot\theta e^{-(x+a)\theta}d\theta}{\int_0^\infty\theta e^{-(x+a)\theta}d\theta}=\dfrac{2/(x+a)^3}{1/(x+a)^2}=\dfrac2{x+a}$.

**$\ln$ and $e$.** $\ln(ab)=\ln a+\ln b$ · $\ln\frac ab=\ln a-\ln b$ · $\ln a^k=k\ln a$ · $\ln e^a=a$ · $e^{\ln a}=a$ · $e^ae^b=e^{a+b}$.<br>
Unchain the unknown: $e^{ky}=A$ → $y=\frac{\ln A}{k}$ · $x^k=a$ → $x=a^{1/k}$ · $y=k\ln x$ → $x=e^{y/k}$.<br>
*Nov22:* $e^{-y}=\frac13$ → $y=\ln3=1.099$. *Apr25:* $x^6=0.1$ → $x=0.1^{1/6}=0.68$.

**Sums.** $\sum_{n\ge0}q^n=\frac1{1-q}$ for $|q|\lt1$ · $\sum_n x_n=N\bar x$ · $\sum_n c=Nc$.<br>
*Apr25:* $\sum_{n\ge0}e^{-2n}=\frac1{1-0.135}=1.1565$.

**Fractions & equations.** $\frac ab\pm\frac cd=\frac{ad\pm bc}{bd}$ · $\frac ab\div\frac cd=\frac{ad}{bc}$ · $\frac ab=\frac cd$ → $ad=bc$ · $ax^2+bx+c=0$ → $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ · multiplying by a negative flips $\gt$ into $\lt$ · $\lvert x\rvert\gt t$ = two cases.<br>
*Apr25-2C:* $\frac{1/3}{14/3}=\frac1{14}$. *Nov22-1b:* $\frac16+\frac14+\frac18=\frac{4+6+3}{24}=\frac{13}{24}$ (common denominator 24).

**Cosines.** $\cos\alpha\cos\beta=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2$ (Nov22 hands it out in the exam).

## Numbers

$\ln2=0.693$ · $\ln3=1.099$ · $\ln4=1.386$ · $\ln10=2.303$ · $\ln0.9=-0.105$ · $e^{-1}=0.368$ · $e^{-2}=0.135$ · $\sqrt{2\pi}=2.51$ · $Q(1.28)=0.10$ · $Q(1.645)=0.05$ · $Q(1.96)=0.025$ · $Q(2.33)=0.01$ · $Q(0)=0.5$.

</div>
</div>
