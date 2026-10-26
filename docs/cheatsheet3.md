---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet (v3)</h1>

<p class="noprint">Same content as <a href="cheatsheet/">v1</a>, but every word is defined the first time it appears. Print at the same settings.</p>
<div class="cheat cheat3" markdown>
<div class="cheat-cols" markdown>

**Symbols, once.** $\theta$ = the unknown to estimate · $\hat\theta$ = your estimate ("theta hat") · $x[n]$, $x_1..x_N$ = the data ($N$ = how many) · $\bar x$ = its average · $E[\cdot]$ = average (expected value) · $r[k]$ = autocorrelation, lag $k$ · $P(\theta)$ = the spectrum · $Q(t)$ = area right of $t$ under the standard bell (Numbers strip).
{: .how }

## PART 1 · Probability (1.5 p)

### 1A · Joint PDF $p(x,y)$

IF YOU SEE a joint PDF/PMF $p(x,y)$ on a region + "find $c$" / "marginal" / "conditional" / "independent" / "domain"
{: .see }

**pdf** = probabilities drawn as a curve (continuous) · **pmf** = probabilities as a list (discrete) · **region** = the $x$–$y$ area where $p$ is given. Draw the region first: **every integral below takes its limits (the $a,b$ of $\int_a^b$) from that picture**, never from the formula.

- **"Find $c$"** → integrate $p$ over the whole region, set the result $=1$, solve for $c$.<br>
  **Limits in 4 moves.** (1) Choose the order $dx\,dy$ = inner $x$, outer $y$ (the other order works too). (2) Freeze the outer letter at one value. (3) Inner limits: "from where to where can the inner letter move now?" — they may contain the outer letter ($x$ from $0$ to $1-y$). (4) Outer limits: the full range of the frozen letter, always plain numbers ($y$ from $0$ to $1$). Rectangle → both limits are numbers, order free. Triangle/wedge → one limit is an expression in the other letter. Limits can be $\infty$ (Jun24): $e^{-\infty}=0$.<br>
  *Apr25:* $cx+1$ on the triangle $x,y\ge0$, $x+y\lt1$ — the whole integral is worked out below.
- **"Marginal $p_X(x)$"** → integrate the OTHER letter away: $p_X(x)=\int p(x,y)\,dy$, inner limits as in move 3. Range of $x$ = the region's shadow on the $x$ axis; write it and "0 otherwise".<br>
  *Jun26:* $6x^2y$ on the square $0\le x,y\le1$: $p_X=\int_0^1 6x^2y\,dy=3x^2$ for $0\le x\le1$. Same way $p_Y=2y$.
- **"Conditional $p(x\mid y)$"** → $p(x,y)$ divided by $p_Y(y)$; state the ranges ($y$ over its shadow, $x$ over the slice at that $y$).<br>
  *Apr24:* $p=2$ on $0\le y\le x\le1$: $p_Y=\int_y^1 2\,dx=2(1-y)$ → $p(x\mid y)=\frac1{1-y}$ for $y\le x\le1$.
- **"Independent?"** → YES only if the region is a rectangle AND $p(x,y)=p_X(x)\cdot p_Y(y)$.<br>
  *Jun26:* square, and $3x^2\cdot2y=6x^2y$ → independent. A triangle region → never independent.

**Worked example — the *Apr25* region, all four tasks on it.** $p(x,y)=cx+1$ on $x,y\ge0$, $x+y\lt1$: a **triangle**, corners $(0,0),(1,0),(0,1)$, sloped side $y=1-x$.<br>
**Step 0 · picture → integral.** Order $dx\,dy$ (inner $x$). **Freeze the outer letter**: draw a horizontal line at one $y$ through the triangle. Where it **enters** the region = lower inner limit, where it **leaves** = upper one: enters at $x=0$, leaves at the sloped side $x=1-y$ → $\int_0^{1-y}$. Then the frozen letter sweeps its whole shadow → $\int_0^1$. Enter, leave, sweep — nothing else.<br>
**1 "find $c$":** $\int_0^1\!\int_0^{1-y}(cx+1)\,dx\,dy=1$. Inner $dx$ with $y$ as a plain number: $\big[\tfrac{cx^2}{2}+x\big]_0^{1-y}=\tfrac{c(1-y)^2}{2}+(1-y)$ — top minus bottom, at the bottom all $x=0$ (**still holding $y$ is normal**). Outer $dy$: $\int_0^1(1-y)dy=\big[y-\tfrac{y^2}{2}\big]_0^1=\tfrac12$ · $\int_0^1\tfrac{(1-y)^2}{2}dy=\big[-\tfrac{(1-y)^3}{6}\big]_0^1=\tfrac16$ → $\tfrac c6+\tfrac12=1$ → $c=3$. Rules: $\int x^n dx=\tfrac{x^{n+1}}{n+1}$, $\int(a-y)^n dy=-\tfrac{(a-y)^{n+1}}{n+1}$, top minus bottom.<br>
**2 "marginal":** same move, swap the letters: freeze $x$ → $y$ enters at $0$, leaves at $1-x$ → $p_X(x)=\int_0^{1-x}(3x+1)\,dy=(3x+1)(1-x)$, $0\le x\le1$.<br>
**3 "conditional":** divide by the marginal of the letter you keep: $p_Y(y)=\int_0^{1-y}(3x+1)dx=\tfrac32(1-y)^2+(1-y)$ → $p(x\mid y)=\tfrac{3x+1}{\frac32(1-y)^2+(1-y)}$ for $0\le x\le1-y$.<br>
**4 "independent?":** triangle, not a rectangle → **no**, no computation.

### 1B · WSS / ergodic (multiple choice)

IF YOU SEE "WSS"/"wide-sense stationary"/"stationary", "ergodic", dice, random phase, random amplitude
{: .see }

**WSS** = the mean is constant AND the autocorrelation depends only on the lag $\tau=t_1-t_2$ (the gap between the two times), not on $t$ · **Ergodic** = averaging ONE signal over time gives the same as averaging over all signals. The exam hands you **a process to test** — no list to look it up: run the 3 tests:

1. **Mean.** $E[x(t)]$, box 1E rules (constants come out; uniform $[a,b]$ → $\frac{a+b}2$). The $t$ has to cancel → constant. Still moves with $t$ → **not WSS**, stop.
2. **Correlation.** $r(t_1,t_2)=E[x(t_1)x(t_2)]$ — expand the product ($\cos\alpha\cos\beta$), average the random letters away (box 1E). Only $(t_1-t_2)$ survives → **WSS**; a lone $t$ or $t_1+t_2$ survives → **not WSS**.
3. **Ergodic in the mean.** Freeze ONE realisation (one recorded signal), take its long-time average, compare with test 1's mean. Fresh randomness at **every** time (random phase, dice, a stream of numbers) → the realisation sees every value → **yes**. One random letter frozen for **all** time (random amplitude $A$) → time averaging cannot remove it → **no**. "in the variance" too → same rule on $x^2$.

*Worked, random phase $\cos(t+U)$:* $E[\cos(t+U)]=0$ — a uniform phase averages a whole turn to 0 → constant ✓. $r=E[\cos(t_1{+}U)\cos(t_2{+}U)]=\frac12\cos(t_1-t_2)$ ✓ → **WSS**, and one realisation $\cos(t+u)$ has long-time average $0=$ the mean → **ergodic in the mean**.
*Worked, random amplitude $A\cos t$:* $E[A\cos t]=E[A]\cos t$ moves with $t$ → **not WSS**, stop. *Dice rolled forever:* fresh roll every time → **ergodic in mean AND variance**. *Numbers uniform in $[-A,A]$ streamed:* mean $\frac{-A+A}2=0$ whatever $A$ is (test 1), each realisation sweeps the whole range → **ergodic, mean 0**.

**Words (Jan22-1b):** *random process* = the whole **set** of signals · one recording = a **realisation** · one number = a random **variable**. "Is this set of pictures WSS?" → **yes** only if the statistics do not shift from picture to picture. Definition MC: the option repeating the WSS line **word for word**.

### 1C · Spectral factorisation

IF YOU SEE $P(\theta)=\dfrac{\text{number}}{A+B\cos\theta}$ + "spectral factorisation"/"factorization", "innovation filter $L(z)$", "$\sigma_i^2$"
{: .see }

1. Read $A$ and $B$ off the denominator $A+B\cos\theta$ **with their signs** ($25-24\cos\theta$: $A=25$, $B=-24$). Two candidate roots $r=\dfrac{A\pm\sqrt{A^2-B^2}}{B}$: keep the one between $-1$ and $1$, call it $a$.
2. $C=\dfrac{B}{2a}$ (just a helper number).
3. $\sigma_i^2=\dfrac{\text{number on top}}{C}$, $L(z)=\dfrac{1}{1+a\,z^{-1}}$.
4. Check $|a|\lt1$ and $\sigma_i^2\gt0$ — a negative $\sigma_i^2$ means you kept the wrong root. Sanity: $\dfrac{\sigma_i^2}{1+a^2+2a\cos\theta}$ must give back the $P(\theta)$ you started from.

*Apr24* $\frac{7}{25-24\cos\theta}$: $A=25$, $B=-24$, $\sqrt{625-576}=7$, $r=\frac{25\pm7}{-24}$ = $-\frac43$ or $-\frac34$ → $a=-\frac34$. $C=\frac{-24}{-3/2}=16$. So $\sigma_i^2=\frac7{16}$, $L=\frac1{1-\frac34z^{-1}}$.

*Apr25* $\frac{1}{61+60\cos\theta}$: $\sqrt{61^2-60^2}=11$, $r=\frac{61\pm11}{60}$ → $a=\frac56$, $C=\frac{60}{2(5/6)}=36$, $\sigma_i^2=\frac1{36}$, $L=\frac1{1+\frac56z^{-1}}$. Check: $\frac{1/36}{1+\frac{25}{36}+2\frac56\cos\theta}=\frac1{61+60\cos\theta}$ ✓

Multiple choice "what must the innovation filter be?" → **minimum phase** (poles and zeros inside the unit circle — the label is the whole answer; Jun26 a).

### 1D · Bayes word problems (counts)

IF YOU SEE groups (machines, scanners, students, patients) with counts or shares + "what is the probability that…" / "if it is found to be…, which group"
{: .see }

1. **Total**: counts given → sum them. Only % → pretend total $=1000$.
2. Items in group $k=$ share$_k\times$total.
3. **Pick "bad"** = the event asked, or the one after "given / if / found to be / has / tested positive". Asked **NOT** pass when a pass rate is given → bad rate $=1-$pass rate.
4. Bad$_k=$ bad rate$_k\times$items$_k$.
5. $P(\text{bad})=\tfrac{\sum_k \text{bad}_k}{\text{total}}$.
6. $P(k\mid\text{bad})=\tfrac{\text{bad}_k}{\sum_k \text{bad}_k}$ — **divide by the pile of bad, not by the total.**

Wording: defective, fail, NOT pass, positive, infected, "actually present" → **bad** · "false positive 3 %" = 3 % **of the healthy** · "detects 95 % when present" = 95 % of the ill · "99 % accurate" = both groups classified right · "mixed at random" = step 5.

*Jun26* 40/35/25 %, defect 2/4/5 % (per 1000: 400/350/250 items → bad$_k$ = 8/14/12.5): bad $=0.4(0.02)+0.35(0.04)+0.25(0.05)=0.0345$; $M_2$ given bad $=\frac{0.35\cdot0.04}{0.0345}=0.41$.

### 1E · Expected value and the MC words

IF YOU SEE "expected value", "discrete or continuous", "exactly $k$ of $n$", "covariance", "contour plot"
{: .see }

- **$E[x]$** $=\sum_x x\,p(x)$ (discrete) $=\int x\,p(x)\,dx$ (continuous) = the **weighted average of the outcomes** (the probabilities are the weights) = the long-run mean. "Integral/sum of the pmf itself" $=1$, **not** $E$. "highest probability / most common" = the **mode**.
- **Discrete** = the values can be listed: "number of …", counts, dice, digits 0–255. **Continuous** = a measurement: time, distance, weight, money.
- **Rules:** $E[c\cdot z]=c\,E[z]$ · $E[c]=c$ · $E[z_1+z_2]=E[z_1]+E[z_2]$ — a constant factor comes out. Uniform $[a,b]$ → mean $\frac{a+b}2$ ($[-A,A]$ → 0).
- **"Exactly $k$ of $n$ tries"** (binomial): $C(n,k)\,p^k(1-p)^{n-k}$, $p$ = chance of one try, $C(n,k)=\frac{n(n-1)\cdots(n-k+1)}{k!}$. *e.g.* $n=4,k=2,p=0.3$: $C(4,2)=\frac{4\cdot3}{2\cdot1}=6$ → $6(0.3)^2(0.7)^2=0.2646$.
- **Covariance:** $\mathrm{Cov}(x,y)=E[xy]-E[x]E[y]$ · sign = whether one goes up when the other does · the number changes with the units (cm→m) · its $\pm1$-bounded version = correlation coefficient. *e.g.* $p(0,0)=p(1,1)=\frac12$: $E[x]=E[y]=E[xy]=\frac12$ → $\mathrm{Cov}=\frac12-\frac14=\frac14$ (both move together → positive).
- **Contour plot, bi-variate Gaussian:** covariance = the two corner (off-diagonal) entries of the covariance matrix: $0$ → ellipses aligned with the axes · **tilted** ellipses → covariance $\ne0$.
- **Definition MC / T/F:** $F(t)=P(x\le t)$ (the cumulative), so $F(-\infty)=0$, $F(\infty)=1$ · independent $=P(A\mid B)=P(A)$, the same as $P(A\cap B)=P(A)P(B)$ ($\cap$ = "both happen") · **disjoint** = they can never both happen, $P(A\cap B)=0$ (the opposite!) · Bayes $=$ conditional probability rearranged. A T/F list → the swap test of box 2D, any topic.

## PART 2 · Estimation (3–3.5 p)

### 2A · Maximum likelihood (MLE)

IF YOU SEE a pdf $p(x\mid\theta)$, samples $x_1..x_N$, "maximum likelihood", "derive the MLE", "find an estimator", "estimate of …"
{: .see }

1. Take $\ln$ of ONE sample's pdf, then put $\sum_n$ in front. That is $\ln L$ ($L$ = likelihood = all the pdfs multiplied). A term with no $x_n$ in it (a $\ln 2$, a $\ln\theta$) comes back once per sample → it gets multiplied by $N$.
2. Differentiate with respect to $\theta$ (terms without $\theta$ disappear).
3. Set it $=0$ and solve for $\theta$. That is $\hat\theta$ (the estimate of $\theta$). ($\ln$ is safe: it turns the product into a sum, and it peaks at the same place.)

**How to take $\ln$ of a pdf:** write the pdf as $\frac{\text{above}}{\text{below}}\cdot e^{u}$ (it is pieces multiplied, some in a fraction). Then each piece becomes one term: a piece $a$ **above the line** → $+\ln a$ · a piece $b$ **below the line** → $-\ln b$ · $e^{u}$ → just $u$ (the $e$ disappears). Two pieces below the line split: $-\ln(2\theta)=-\ln 2-\ln\theta$. A power $\theta^k$ below the line → $-k\ln\theta$.
Derivatives: $\ln\theta\to\frac1\theta$ · $\theta^k\to k\theta^{k-1}$ · $\frac1\theta\to-\frac1{\theta^2}$ · $e^{c\theta}\to ce^{c\theta}$ · $\cos\theta\to-\sin\theta$ · $\sin\theta\to\cos\theta$.
Solving $=0$: multiply the equation by the denominators ($\theta^2$, $\theta$, …) first — that does not change the solution.
**Trap:** if the pdf only exists for $x$ up to something containing $\theta$ (uniform on $[0,\theta]$), these 3 steps are useless — $\hat\theta=\max_n x_n$, and **the CRLB does not exist**.
**Fisher info / CRLB** from that same derivative: $i(\theta)=-\mathrm E\big[\frac{\partial^2\ln p}{\partial\theta^2}\big]$ for one sample; $N$ samples → $\mathcal I=N i(\theta)$; **CRLB** $=\frac1{N i(\theta)}$ — the smallest variance any unbiased estimator can get (the floor). Reach the floor = **efficient**.
**Computing $i(\theta)$ in 3 lines** (exponential rate, $p=\lambda e^{-\lambda x}$): $\ln p=\ln\lambda-\lambda x$ → $\partial_\lambda=\frac1\lambda-x$ → $\partial^2_\lambda=-\frac1{\lambda^2}$ → $i=-\mathrm E\big[-\frac1{\lambda^2}\big]=\frac1{\lambda^2}$ (no $x$ left, so the average does nothing) → CRLB $=\frac{\lambda^2}N$. If an $x$ survives the second derivative, average it out with $\mathrm E[x]$.
**Known $i(\theta)$** — skip the derivation: Gaussian mean with variance $\sigma^2$: $\frac1{\sigma^2}$ · exponential rate $\lambda$: $\frac1{\lambda^2}$ · Bernoulli: $\frac1{\theta(1-\theta)}$ · Rayleigh $\frac{x}{\theta^2}e^{-x^2/2\theta^2}$: $\frac4{\theta^2}$ (so CRLB $=\frac{\theta^2}{4N}$).

**Check your $\hat\theta$:** uniform $[0,\theta]$ → $\max_n x_n$ (the trap above) · exponential rate $\lambda$ → $1/\bar x$ · Poisson $\lambda$ → $\bar x$ · Bernoulli → $k/N$ ($k$ successes in $N$).

*Apr24* $\tfrac{x}{2\theta}e^{-x^2/2\theta}$: one sample gives $\ln x-\ln2-\ln\theta-\tfrac{x^2}{2\theta}$, so $\ln L=\sum\ln x_n-N\ln2-N\ln\theta-\tfrac{\sum x_n^2}{2\theta}$ → $-\tfrac N\theta+\tfrac{\sum x_n^2}{2\theta^2}=0$ → $\hat\theta=\tfrac1{2N}\sum x_n^2$.

*Jun26* Gamma $\tfrac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$, $n$ patients: one sample → $\ln p=(k-1)\ln x-\tfrac x\theta-k\ln\theta$ → $\ln L=(k-1)\sum\ln x_i-\tfrac{\sum x_i}{\theta}-nk\ln\theta$ → $\partial_\theta=\tfrac{\sum x_i}{\theta^2}-\tfrac{nk}\theta=0$ → $\hat\theta=\tfrac{\sum x_i}{nk}=\tfrac{\bar x}k$. Meaning: average time per stage, so $k\hat\theta$ = the observed mean time.

**Sigmoid trick.** IF YOU SEE $\lambda=\frac1{1+e^{-\theta}}$: treat $\lambda$ as the unknown, find $\hat\lambda$, then convert with $\hat\theta=-\ln\!\big(\frac1{\hat\lambda}-1\big)$.

*Apr25* $3\lambda e^{-4\lambda x/7}$: $\frac1\lambda-\frac{4x}7=0$ → $\hat\lambda=\frac7{4x}$ → $\hat\theta=-\ln\!\big(\frac{4x}7-1\big)$, valid for $x\gt\frac74$.

### 2B · MAP with a prior (Beta / Gamma)

IF YOU SEE "prior", "posterior", "MAP", "maximum a posteriori"/"a-posteriori", "MMSE"/"minimum mean square error", "Bayesian estimator", Beta, Gamma
{: .see }

1. Likelihood: write each observation's probability, keep only the parts with $\theta$, multiply them all (exponents add).
2. Multiply by the prior (exponents add again). Drop numbers without $\theta$.
3. Read the shape and use the table:

| Result looks like | Posterior | MAP | MMSE (mean) |
|---|---|---|---|
| $\theta^{A}(1-\theta)^{B}$ | Beta$(A{+}1,B{+}1)$ | $\frac{A}{A+B}$ | $\frac{A+1}{A+B+2}$ |
| $\lambda^{A}e^{-B\lambda}$ | Gamma$(A{+}1,B)$ | $\frac{A}{B}$ | $\frac{A+1}{B}$ |

Prior Beta$(a,b)$ = $\theta^{a-1}(1-\theta)^{b-1}$ (its mean $\frac a{a+b}$). Prior Gamma$(a,b)$ = $\lambda^{a-1}e^{-b\lambda}$ (mean $\frac ab$). The prior pulls the estimate towards that mean.
One observation $x$ gives: Poisson count → $\lambda^{x}e^{-\lambda}$ · "$k$-th success on trial $x$" → $\theta^k(1-\theta)^{x-k}$ · "$k$ successes in $n$ tries" → $\theta^k(1-\theta)^{n-k}$ · exponential → $\lambda e^{-\lambda x}$.

**Posterior not in the table?** Do it by hand: **MAP** $=\arg\max_\theta p(\theta\mid x)$ = the peak ($\arg\max$ = the $\theta$ at the top) · **MMSE** $=\int\theta\,p(\theta\mid x)\,d\theta$ = its mean (use the Calculations integrals).
**Prior with a range** (uniform on $[a,b]$): cut the parameter's range to $[a,b]$ first — the posterior is only $\propto$ the likelihood inside $[a,b]$; if the peak would land outside, the MAP is the nearest endpoint $a$ or $b$.

*Jun26-2c:* $\theta^2(1-\theta)^{x-2}$ with $x=3,5,4,6,4$: $\theta$ exponent $2$ five times $=10$, $(1-\theta)$ exponents sum $12$ → $\theta^{10}(1-\theta)^{12}$. Prior Beta(2,3) adds $\theta^1(1-\theta)^2$ → $\theta^{11}(1-\theta)^{14}$ → Beta(12,15), MAP $=\tfrac{11}{25}=0.44$, MMSE $=\tfrac{12}{27}=0.444$.

*Jun26-2d:* Poisson, $x=2,4,3,5,2,4$: $\lambda$ exponents add to $20$, six $e^{-\lambda}$ give $e^{-6\lambda}$ → $\lambda^{20}e^{-6\lambda}$. Prior Gamma(3,2) adds $\lambda^2e^{-2\lambda}$ → $\lambda^{22}e^{-8\lambda}$ → Gamma(23,8), MAP $=\frac{22}8=2.75$. MLE $=\frac{20}6=3.33$: the prior pulls towards its own mean $\frac32$.

*Apr25-2d:* posterior already given as $\theta^{a}(1-\theta)^{b}$ → MAP $=\frac a{a+b}$.

*Nov22:* posterior $\lambda e^{-(x+a)\lambda}$ → MAP $\frac1{x+a}$, MMSE $\frac2{x+a}$.

*Apr24-2d (sigmoid):* posterior $\frac\lambda2e^{-\lambda x/2}$ → $\frac1\lambda-\frac x2=0$ → $\lambda=\frac2x$ → $\hat\theta=-\ln\!\big(\frac x2-1\big)$, $x\gt2$.

### 2C · Least-squares line

IF YOU SEE points $(x,y)$ + "least squares"/"least-squares"/"LSE", "linear function", "fit a line"
{: .see }

1. Means $\bar x$ and $\bar y$ (bar = average).
2. Slope $a=\tfrac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}$.
3. $b=\bar y-a\bar x$. Answer: $y=ax+b$. Check: $x=\bar x$ must give $y=\bar y$.

*Apr25* $(0,3),(2,4),(3,3)$: $\bar x=\tfrac{0+2+3}3=\tfrac53$, $\bar y=\tfrac{3+4+3}3=\tfrac{10}3$. Diffs $x-\bar x$: $-\tfrac53,\tfrac13,\tfrac43$ · $y-\bar y$: $-\tfrac13,\tfrac23,-\tfrac13$ → $\sum(x-\bar x)(y-\bar y)=\tfrac{5+2-4}{9}=\tfrac13$, $\sum(x-\bar x)^2=\tfrac{25+1+16}{9}=\tfrac{14}3$ → slope $a=\tfrac{1/3}{14/3}=\tfrac1{14}$, $b=\tfrac{10}3-\tfrac1{14}\cdot\tfrac53=\tfrac{45}{14}$ → $y=\tfrac1{14}x+\tfrac{45}{14}$ (check $x=\bar x$ gives $y=\bar y$ ✓).

Also: $x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$. $x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$ (noise = random wobble; fitting a constant by least squares is just its average).

**Beyond a straight line.** $J(\theta)=\sum_n(x[n]-s[n;\theta])^2$, $\hat\theta=\arg\min J$ (the $\theta$ making $J$ smallest) — write this when they ask "what kind of estimator". One amplitude $s[n]=Ah[n]$: $\hat A=\dfrac{\sum x[n]h[n]}{\sum h[n]^2}$ (*e.g.* $x=3,5$, $h=1,2$: $\hat A=\tfrac{3+10}{1+4}=2.6$). Linear model $x=\mathbf H\theta+w$: $\hat\theta=(\mathbf H^T\mathbf H)^{-1}\mathbf H^Tx$; the **error** $x-\mathbf H\hat\theta$ is orthogonal (perpendicular) to the columns of $\mathbf H$ (it is the error, **not** $\hat\theta$); weighted LS with $\mathbf W=\mathbf C_x^{-1}$ = **BLUE** (best linear unbiased estimator). Nonlinear: transform it (the $e^{\bar x}$ line), or iterate **Gauss–Newton** $\theta_{k+1}=\theta_k+(\mathbf G^T\mathbf G)^{-1}\mathbf G^T(x-s(\theta_k))$, $\mathbf G[:,i]=\frac{\partial s}{\partial\theta_i}$ — Newton–Raphson works too, "only Gauss–Newton" is **false**.

### 2D · Part 2 true / false

IF YOU SEE "which of the following statements" (in Part 2) about MLE, MAP, MMSE, Fisher, CRLB
{: .see }


**Kill any T/F with the swap test.** A FALSE option is a TRUE sentence with ONE word swapped: hunt *always · regardless · strictly · maximise/minimise · mean↔maximum*. No swap word → TRUE. Paraphrase? Match the idea, not the words.

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

$P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta$. Stop at the last lag given. $r[0]$ is NOT doubled. From data: $\hat r[k]=\frac1N\sum_n x[n]x[n-k]$. Other way round ($P(\theta)$ given, $r[k]$ asked): $r[0]$ = the plain constant term, $r[k]$ = **half** the coefficient of $\cos k\theta$. Instant check: $P(0)=r[0]+2r[1]+2r[2]+\dots$ (all $+$), $P(\pi)=r[0]-2r[1]+2r[2]-\dots$ (signs alternate) — two heights to compare against your curve.

*Jun26* $3,2,1$: $3+4\cos\theta+2\cos2\theta=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$. *From data* $x=[1,2,3]$: $\hat r[0]=\tfrac{1+4+9}{3}=\tfrac{14}3$, $\hat r[1]=\tfrac{2+6}{3}=\tfrac83$ (only the 2 overlapping pairs), $\hat r[2]=\tfrac33=1$.

*Apr24* $\frac{25}{16},-\frac34,\frac12,-\frac12$: $\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$.

### 3B · AR(1)

IF YOU SEE "AR(1)", "first-order autoregressive"
{: .see }

Model: $x[n]=a\,x[n-1]+i[n]$ ($i$ = white noise). The minus in step 1 = moving $x[n-1]$ to the left.

1. $a=-\dfrac{r[1]}{r[0]}$
2. $\sigma^2=r[0]+a\,r[1]$
3. $P=\dfrac{\sigma^2}{1+a^2+2a\cos\theta}$ (check $|a|\lt1$ and $\sigma^2\gt0$, else a sign went wrong)

*Apr25* $r[0]=2$, $r[1]=-\tfrac14$: $a=-\tfrac{-1/4}{2}=\tfrac18$ · $\sigma^2=2+\tfrac18(-\tfrac14)=\tfrac{63}{32}$ → $P=\tfrac{63/32}{1+\frac1{64}+\frac14\cos\theta}\cdot\tfrac{64}{64}=\tfrac{126}{65+16\cos\theta}$.

### 3C · AR(2) / Yule–Walker

IF YOU SEE "AR(2)", "Yule–Walker", $r[0],r[1],r[2]$
{: .see }

1. $D=r[0]^2-r[1]^2$
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

- The right side names the type ($i$ = the noise coming in): only $i[n],i[n-1],\dots$ → **MA($q$)**, $q$ = biggest noise delay · noise **and** past outputs $x[n-k]$ → **ARMA($p,q$)**, $p$ = biggest $x$ delay (bring $x[n-k]$ left first: $x[n]+\alpha x[n-1]=i[n]+\beta i[n-1]$) · $x[n-k]$ but noise only as $i[n]$ → **AR($p$)**: use 3B/3C. From the shape of $P(\theta)$: sharp **peaks** → AR, deep **nulls** → MA, both → ARMA.
- MA autocorrelation: write the list $1,b_1,b_2,\dots$ and use $r[k]=\sigma^2\sum_m b_m b_{m+k}$ with $b_0=1$ (pairs sitting $k$ apart in the list). Zero after lag $q$. So $r[0]$ = $\sigma^2\times$ sum of the squares ($r[0]=\sigma^2(1+b_1^2+b_2^2+\dots)$); $r[1]$ = each one times its right-hand neighbour ($1\cdot b_1+b_1b_2+\dots$); $r[2]$ = skip one ($1\cdot b_2+b_1b_3+\dots$).<br>
  **Backwards** — $r[k]$ given, the coefficients asked (Jan22 MA(2)): go from the **biggest lag down** — the biggest lag has a single product, so $b_q=r[q]/\sigma^2$; then the next lag has one letter left free. MA(2), $\sigma_i^2=1$: $b_2=r[2]$, then $r[1]=b_1(1+b_2)$ → $b_1$; the correlogram needs $r[0]=\sigma^2(1+b_1^2+b_2^2)$ (sum of the squares).<br>
  *Apr24* $1,-\frac12,\frac14,-\frac12$ (MA(3), $\sigma^2=1$): $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$, $r[1]=-\frac12-\frac18-\frac18=-\frac34$, $r[2]=\frac14+\frac14=\frac12$, $r[3]=-\frac12$.
- ARMA(1,1) written as $x[n]+\alpha x[n-1]=i[n]+\beta i[n-1]$: $P=\sigma^2\dfrac{1+\beta^2+2\beta\cos\theta}{1+\alpha^2+2\alpha\cos\theta}$. Its $r[k]$: $r[0]=\sigma^2\frac{1+\beta^2-2\alpha\beta}{1-\alpha^2}$, $r[1]=-\alpha r[0]+\beta\sigma^2$, then every extra lag multiplies by $-\alpha$.<br>
  *Nov22* $x[k]=i[k]-i[k-1]+\frac34x[k-1]$, $\sigma^2=\frac78$ given: $\alpha=-\frac34$, $\beta=-1$ → $P=\frac{28(1-\cos\theta)}{25-24\cos\theta}$.

### 3F · Pick the plot

IF YOU SEE "which plot", "which figure", "plots A–D", "match the plot"
{: .see }

Work out each PSD at $\theta=0$ (all cosines $=1$) and at $\theta=\pi$ ($\cos\theta=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Pick the plot with those heights. Only a correlogram can go below 0.

*Apr25:* correlogram $1.13\to2.13$, MA $1.5\to2.5$, AR $1.56\to2.57$ (heights at $0\to\pi$) → plot D.
**Second type** (windowed cosine, DTFT vs DFT — the DTFT is the whole curve, the DFT is the dots on it): infinite cosine = **2 spikes** · windowed = **main lobe + side lobes** (one big bump + small ones) · DFT = **samples of that same curve** · zero padding = **more dots**, not more resolution.

### 3G · Welch / Bartlett count

IF YOU SEE "Welch"/"Bartlett"/"WOSA", $N$ samples, segment length $L$, overlap %, "how many segments"
{: .see }

Step $D=L\times(1-\text{overlap})$. Segments $K=\frac{N-L}{D}+1$ (round $K$ down to a whole number). Bartlett (no overlap): $K=\frac NL$. Variance ratio $=\frac1K$ **if the segments are independent** (what the exam assumes — *Jun26* → $\frac19$); real Welch overlap shares samples → the drop is **less** than $\frac1K$ (3J).

*Jun26* $N=1000$, $L=200$, 50 %: $D=200(1-0.5)=100$, $K=\tfrac{1000-200}{100}+1=9$ segments, ratio $\tfrac19$.

### 3H · Energy or power signal

IF YOU SEE "energy or power signal", "total energy", "average power"
{: .see }

- Dies out or has finite length → **energy**: $E=\sum\lvert x\rvert^2$ is finite, power $=0$.
- Never dies out (sin, cos, constant, $\cos t\,u(t)$) → **power**: $P$ = time average of $\lvert x\rvert^2$, energy $=\infty$.
- Time-continuous ($t$) → $\sum$ becomes $\int dt$: $E=\int\lvert x\rvert^2dt$, $P=\frac1T\int_0^T\lvert x\rvert^2dt$.

*Apr25:* $A\sin\omega t$ → power $\tfrac{A^2}2$. $e^{-n}$ for $n\ge0$ → energy $\sum e^{-2n}=\tfrac1{1-e^{-2}}\approx1.16$ (use $\sum_{n\ge0}q^n=\tfrac1{1-q}$). *Continuous* $e^{-t}$, $t\ge0$: dies out → energy $\int_0^\infty e^{-2t}dt=\tfrac12$ (the $c=2$ line of the Calculations strip).

### 3I · Name the method

IF YOU SEE a table of descriptions to fill with method names, "name the method", bias/variance to match
{: .see }

| The description says… | Method |
|---|---|
| $\lvert\text{DFT}\rvert^2$ divided by $N$, whole signal | Periodogram |
| DFT of the estimated autocorrelation | Correlogram |
| …plus a window of length $M$ (shorter than the lags) on the autocorrelation; "consistent" | Blackman–Tukey |
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

1. $L(x)=\dfrac{p(x\mid H_1)}{p(x\mid H_0)}$. Cancel what appears on top and bottom. $N$ samples → multiply them ($e^ae^b=e^{a+b}$).
2. Decide $H_1$ if $L\gt$ threshold. Take $\ln$ of both sides.
3. Get $x$ alone. Multiplying or dividing by a negative number flips $\gt$ into $\lt$.
4. Check the side: put a small and a large $x$ into $L$. Where $L$ comes out bigger than the threshold, that side is "decide $H_1$".

*Apr25* $\frac{6x^{11}}{3x^5}=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=0.68$.

*Jun26 Rayleigh* $\frac x{\sigma^2}e^{-x^2/2\sigma^2}$ ($\sigma_1\gt\sigma_0$): the $x$ in front cancels → accept $H_1$ if $x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\big(\eta\frac{\sigma_1^2}{\sigma_0^2}\big)}$. Bigger gap between $\sigma_0,\sigma_1$ → the pdfs overlap less → more $P_D$ for the same $P_{FA}$ (better ROC).

*Apr24* Gaussian $\tfrac1{\sqrt{2\pi}}e^{-y^2/2}$ vs exponential $\tfrac14e^{-y/2}$, $\gamma=1$: the constant $\ln\tfrac{1/4}{1/\sqrt{2\pi}}=\ln\tfrac4{2.51}=-0.467$ → $-0.467+\tfrac{y^2}2-\tfrac y2\gt0$ → $y^2-y-0.934\gt0$ → root $y=\tfrac{1+\sqrt{1+3.74}}2=1.59$ → accept $H_1$ if $y\gt1.59$. $P_{FA}=Q(1.59)=0.056$, $P_D=\tfrac12e^{-0.795}=0.23$ (printed answer — that pdf is unnormalised, keep the $\tfrac12$).

*Nov22* $\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$.

**Probabilities.** $P_{FA}$ = area under the $H_0$ pdf where you decide $H_1$. $P_D$ = area under the $H_1$ pdf in the same place.<br>
Tails: Gaussian $N(0,1)$ (mean 0, variance 1): $P(x\gt t)=Q(t)$ = the area right of $t$ (Numbers strip) · exponential $ce^{-cx}$: $P(x\gt t)=e^{-ct}$ · Rayleigh: $P(x\gt t)=e^{-t^2/2\sigma^2}$ · two tails $\lvert x\rvert\gt t$ → double.<br>
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

- Threshold $\eta=\dfrac{P(H_0)\,(C_{10}-C_{00})}{P(H_1)\,(C_{01}-C_{11})}$. Equal error costs and 0 for correct → $\eta=\frac{P(H_0)}{P(H_1)}$. Then do 4A with this $\eta$.<br>
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

Trap (Apr25-4b): "which statement is FALSE" where all three look true → as printed **all three are true** (official: no false one). Check the verbs: risk **min** · $P_D$ **max** · $P_e$ **min**.

## Calculations · the algebra under every answer

**Integrals.** These formulas are **printed in the question itself** (q3-23-2h, nov22-2f) — you copy them: $\int e^{cx}dx=\frac1ce^{cx}$ · $\int xe^{cx}dx=\frac{cx-1}{c^2}e^{cx}$ · $\int x^2e^{cx}dx=\big(\frac{x^2}{c}-\frac{2x}{c^2}+\frac{2}{c^3}\big)e^{cx}$ · $\int x^2e^{-x}dx=-e^{-x}(x^2+2x+2)$ (by parts twice) · $\int\cos u\,du=\sin u$ · $\int\sin u\,du=-\cos u$.
Evaluate $[F(x)]_a^b=F(b)-F(a)$: at $x=\infty$ only $e^{cx}$ with $c\lt0$ becomes 0, at $x=0$ every $x$ is 0 so only the plain number is left → $\int_0^\infty e^{-cx}dx=\frac1c$ · $\int_0^\infty xe^{-cx}dx=\frac1{c^2}$ · $\int_0^\infty x^2e^{-cx}dx=\frac2{c^3}$.<br>
*Nov22-2f:* MMSE $=\dfrac{\int_0^\infty\theta\cdot\theta e^{-(x+a)\theta}d\theta}{\int_0^\infty\theta e^{-(x+a)\theta}d\theta}=\dfrac{2/(x+a)^3}{1/(x+a)^2}=\dfrac2{x+a}$.

**$\ln$ and $e$.** $\ln(ab)=\ln a+\ln b$ · $\ln\frac ab=\ln a-\ln b$ · $\ln a^k=k\ln a$ · $\ln e^a=a$ · $e^{\ln a}=a$ · $e^ae^b=e^{a+b}$.<br>
Get the letter alone: $e^{ky}=A$ → $y=\frac{\ln A}{k}$ · $x^k=a$ → $x=a^{1/k}$ · $y=k\ln x$ → $x=e^{y/k}$.

**Sums.** $\sum_{n\ge0}q^n=\frac1{1-q}$ for $|q|\lt1$ · $\sum_n x_n=N\bar x$ · $\sum_n c=Nc$.

**Fractions & equations.** $\frac ab\pm\frac cd=\frac{ad\pm bc}{bd}$ · $\frac ab\div\frac cd=\frac{ad}{bc}$ · $\frac ab=\frac cd$ → $ad=bc$ · $ax^2+bx+c=0$ → $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ · multiplying by a negative flips $\gt$ into $\lt$ · $\lvert x\rvert\gt t$ = two cases.

**Numbers.** $\ln2=0.693$ · $\ln3=1.099$ · $\ln10=2.303$ · $e^{-2}=0.135$ · $\sqrt{2\pi}=2.51$ · $Q(1.28)=0.10$ · $Q(1.645)=0.05$ · $Q(1.96)=0.025$ · $Q(2.33)=0.01$.

</div>
</div>
