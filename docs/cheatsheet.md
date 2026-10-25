---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet</h1>

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This sheet fills both sides: Ctrl/Cmd + P → A4, margins minimal, untick "headers and footers", scale 100 %. Better still: copy it by hand — writing it is half the studying.</p>
<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## 1.1 · Bayes word problems (counts)
Count items:

1. Pretend **1000** items (**1 000 000** if tiny, like 0.0005). Given counts (18, 22, 15)? Use them.
2. Items$_k$ = share$_k$ × total.
3. Bad$_k$ = bad-rate$_k$ × items$_k$. Given *good* rate? bad $=1-$good. "Bad" = the event asked (pass, +, …).
4. $P(\text{bad})$ = (sum of bad$_k$) / total.
5. $P(k\mid\text{bad})$ = bad$_k$ / (sum of bad), not / total.

*Machines* 40/35/25 %, defective 2/4/5 %: 400/350/250 → bad 8, 14, 12.5 → pile 34.5. $P(D)=\frac{34.5}{1000}=0.0345$; $P(M_2\mid D)=\frac{14}{34.5}=0.41$.

*Disease* 0.0005, "99 % accurate" = right for 99 % of ill **and** healthy: 500 ill → 495 $+$; 999 500 healthy → 1 % = 9995 $+$. "Ill if positive" (exam may print "Provide Pr[TB]" = this) $=\frac{495}{495+9995}=0.047$ (not the prior 0.0005). Rates 1.8 %, 95 %, false + 3 %: 18 ill→17.1; 982 healthy→29.46; $\frac{17.1}{46.56}=0.37$.

*Table*: $P(\text{F}\mid\text{psych})$ = F-psych / whole psych column; $P(\text{eng})$ = eng column / grand total.

*Lifetime* $P(T\ge t)$ = alive at $t$. Alive at 2, dies in year 3: $1-\frac{e^{-3/5}}{e^{-2/5}}=1-e^{-1/5}=0.18$.

Independent ⇔ $P(A\mid B)=P(A)$ ⇔ $P(A\cap B)=P(A)P(B)$; $P(A\cap B)=0$ is *disjoint*. $P(A\text{ or }B)=P(A)+P(B)$ only if disjoint (50 %+25 % ≠ 75 %). Exam "Bayes theorem is obtained from the total law of probability and the conditional probability" → F. True: CDF 0 at $-\infty$, 1 at $\infty$; frequency → pmf. $E[X]=\sum x\,p(x)$. False: Wiener FIR 1-step prediction → AR (all-pole) spectral estimation, not MA.

## 1.2 · Joint PDF: $c$, marginal, conditional, independent
Draw the region where $p\ne0$; read limits off it.
1. **$c$**: total integral $=1$. Inner $\int dx$ (edge to edge), outer $\int dy$; $c\cdot$number$=1$.
2. **Marginal** $p_X=\int p\,dy$, $p_Y=\int p\,dx$ + domain, "0 otherwise". PMF table: **add** the row ($p_X$) or column.
3. **Conditional** $p_{X\mid Y}=p(x,y)/p_Y(y)$.
4. **Independent** ⇔ rectangle **and** $p=p_Xp_Y$.

$\int_a^b x^n dx=\frac{b^{n+1}-a^{n+1}}{n+1}$; $\int_a^\infty e^{-kx}dx=\frac{e^{-ka}}{k}$.

*Square* $6x^2y$: $p_X=6x^2\int_0^1y\,dy=3x^2$; $p_Y=2y$; product $=p$ → independent.
*Triangle* $cx+1$, $x{+}y{<}1$: $\int_0^{1-y}dx=\frac c2(1-y)^2+(1-y)$; $\int_0^1dy$: $\frac c6+\frac12=1$, $c=3$.
*Triangle* $2$, $y\le x\le1$: $p_Y=2(1-y)$; $p_{X\mid Y}=\frac1{1-y}$, $y\le x\le1$.
*Exp* $ce^{-x-y}$, $0\le y\le x$: $\int_y^\infty e^{-x}dx=e^{-y}$; $\int_0^\infty e^{-2y}dy=\frac12$; $c=2$.
*PMF* $X{=}0$: $\frac{4+6+3}{24}=\frac{13}{24}$.

**Concepts**
- Discrete = counted (dice, 4s, applicants, days, pixel, phone no.); continuous = measured (time, distance, weight, average).
- Expected value $E[X]=\sum x\,p(x)$ = weighted average = **mean value over an infinite number of observations**. Wrong: highest probability, most common, largest, simple/geometric average.
- Binomial $\binom nk p^k(1-p)^{n-k}$; $n{=}8,k{=}6,p{=}.8$: $28\cdot.262144\cdot.04=.2936$.
- Gaussian contours, diagonal Cov (zeros off-diagonal): circle or ellipse with axes along $x,y$ OK. "NOT possible" → the **tilted** ellipse plot (needs Cov$\ne0$).
- Random process: family of signals; one picture = one realization.

## 1.3 · WSS and ergodic
$E[\cdot]$ = average over the random ingredient ($U$, $A$, the die).

1. **Mean** $E[X(t)]$ contains $t$ → **not WSS, not ergodic**.
2. **Autocorr** $E[X(t)X(t+\tau)]$ has no $t$ → **WSS**.
3. **Ergodic (mean)**: fix one draw, average over time. Same for every draw and $=E$ → yes; still contains $A$ → no.
4. Uniform on $-A..A$: mean $0$ for every $A$ → "ergodic, mean 0".

$\cos(t+U)$: mean 0, $r=\frac12\cos\tau$ → **WSS yes, ergodic yes**. $A\cos t$, $A\sim\mathcal N(1,2)$: $E[X]=\cos t$ → **WSS no, ergodic no**.

WSS = constant mean + autocorr depends only on lag. Fair dice: ergodic in mean and variance, mean 3.5 (not 0).

**"Legitimate autocorr"** (plots): keep plots with $r[l]=r[-l]$ AND $r[0]\ge|r[l]|$; pick the option listing exactly those.
**Cross-corr** $r_{xy}[\tau]$: shift $y$ by $\tau$, multiply overlaps, add, ÷ $N$ samples. Do $\tau=0$ first, drop options that differ; keep signs. E.g. $x=[1,1,1,0]$, $y=[1,3,3,5]$: shift 0 → $(1+3+3+0)/4=7/4$. No exact option → closest.

## 1.4 · Spectral factorisation
$P=\frac{N+M\cos\theta}{A+B\cos\theta}$ ($M=0$ if no cosine on top). Want $L=\frac{1+bz^{-1}}{1+az^{-1}}$ (no $b$ if $M=0$), $\sigma_i^2$.

**Tool** for $p+q\cos\theta$: $r=\frac{p\pm\sqrt{p^2-q^2}}{q}$ (roots $r$, $1/r$); **keep $|r|\lt1$**; $K=\frac{q}{2r}$.

1. Bottom ($p=A,q=B$) → $a,C$. Top ($p=N,q=M$) → $b,D$ ($M=0$: $D=N$).
2. $\sigma_i^2=\frac DC$, $L=\frac{1+bz^{-1}}{1+az^{-1}}$.

Ex. $\frac{10+6\cos\theta}{17-8\cos\theta}$: bottom $\frac{17\pm15}{-8}$ → $-4,-\frac14$: $a=-\frac14$, $C=\frac{-8}{-1/2}=16$. Top $\frac{10\pm8}{6}$ → $3,\frac13$: $b=\frac13$, $D=\frac{6}{2/3}=9$. $\sigma_i^2=\frac9{16}$, $L=\frac{1+\frac13z^{-1}}{1-\frac14z^{-1}}$.

Ex. $\frac1{61+60\cos\theta}$: $\frac{61\pm11}{60}$ → $a=\frac56$, $C=36$, $\sigma_i^2=\frac1{36}$.

Given $c\frac{(1+bz^{-1})(1+bz)}{(1+az^{-1})(1+az)}$, $|a|,|b|\lt1$: $\sigma_i^2=c$, $L(z)$ = the $z^{-1}$ factors.

Innovation filter = **minimum phase**: poles and zeros inside the unit circle.

## 2.1 · Maximum likelihood (MLE)
Exam says "derive the MLE", "determine the maximum likelihood estimate", "find an estimator for $\theta$" (pdf given) → steps 1–3. $\hat\theta=\arg\max_\theta p(x\mid\theta)$. One-to-one $\alpha=\psi(\theta)$: find $\hat\alpha$, then $\hat\theta=\psi^{-1}(\hat\alpha)$. Large $N$: asymptotically unbiased.
1. $L=\prod_n p(x_n\mid\theta)$, $\ln L=\sum_n\ln p(x_n\mid\theta)$. $\ln(ab)=\ln a+\ln b$, $\ln\frac ab=\ln a-\ln b$, $\ln x^k=k\ln x$, $\ln e^u=u$.
2. Differentiate: $\ln\theta\to\frac1\theta$, $\frac c\theta\to-\frac c{\theta^2}$, $\frac c{\theta^2}\to-\frac{2c}{\theta^3}$, $c\theta\to c$, no $\theta$ (e.g. $\ln x$) → 0. Term without $n$ summed $N$ times → $\times N$.
3. Set $=0$, multiply by $\theta^2$ (or $\theta^3$), solve. If $\theta^2=s$: $\hat\theta=\sqrt s$.

**Ex.** $\frac{x}{2\theta}e^{-x^2/2\theta}$ (same if prefactor is $\frac x\theta$): $\sum(\ln x-\ln2-\ln\theta-\frac{x^2}{2\theta})$ → $-\frac N\theta+\frac{\sum x^2}{2\theta^2}=0$ → $\times\theta^2$ → $\hat\theta=\frac{\sum x^2}{2N}$. Exponent $-x^2/\theta$: $\frac{\sum x^2}N$.
**Ex.** $\frac{x}{\theta^2}e^{-x^2/2\theta^2}$: $-\frac{2N}\theta+\frac{\sum x^2}{\theta^3}=0$ → $\hat\theta=\sqrt{\sum x^2/2N}$. $\lambda e^{-\lambda x}$: $\frac N\lambda-\sum x=0$ → $\frac N{\sum x}$.
**Ex.** Gamma $\frac{x^{k-1}e^{-x/\theta}}{\theta^k\Gamma(k)}$, $k$ known: $\frac{\sum x}{\theta^2}-\frac{nk}\theta=0$ → $\hat\theta=\frac{\sum x}{nk}=\frac{\bar x}k$ (mean ÷ $k$ stages).
**Unknown squared** (e.g. $\rho$): exponent $\to-a\rho^2+b\rho$ → $-2a\rho+b=0$ → $\rho=\frac b{2a}$ (shared denominators cancel).
**Angle:** expand $(x_1-A\cos\theta)^2+(x_2-A\sin\theta)^2$; $\cos^2+\sin^2=1$ is const; rest → $-x_1\sin\theta+x_2\cos\theta=0$ → $\hat\theta=\tan^{-1}\frac{x_2}{x_1}$.
**Sigmoid** $\lambda=\frac1{1+e^{-\theta}}$: don't expand; solve $\frac{d\ln p}{d\lambda}=0$, then $\theta=\ln\frac\lambda{1-\lambda}$. $3\lambda e^{-4\lambda x/7}$: $\frac1\lambda-\frac{4x}7=0$ → $\lambda=\frac7{4x}$ → $\theta=\ln\frac7{4x-7}$; needs $x\gt\frac74$.

## 2.2 · MAP with a prior
Posterior ∝ likelihood × prior. MAP = peak (needs a prior), MMSE = mean ("MMSE is the mean of the posterior" TRUE, "= maximum" FALSE); equal only for one symmetric bump ("always different" FALSE). Bayes risk = expected cost; minimising it: squared cost → MMSE, 0/1 or "uniform" cost → MAP.
1. $L=\prod_i P(x_i\mid\theta)$, drop factors without $\theta$, write ∝. Same base → add exponents.
2. Prior: Beta$(\alpha,\beta)$ = $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ · Gamma$(\alpha,\beta)$ = $\lambda^{\alpha-1}e^{-\beta\lambda}$, mean $\frac\alpha\beta$.
3. Multiply → $\theta^A(1-\theta)^B$ = Beta$(A{+}1,B{+}1)$, or $\lambda^Ae^{-B\lambda}$ = Gamma$(A{+}1,B)$. Normalised: $A{=}0$: $Be^{-B\lambda}$; $A{=}1$: $B^2\lambda e^{-B\lambda}$.
4. MAP: $\frac A{A+B}$ · $\frac AB$ ($A,B$ = the exponents, e.g. $\beta_1-1+k_1N_1$). Gamma MMSE = mean $\frac{A+1}B$. MLE = same rule on $L$ alone.

**Ex.** NegBin $k=2$, $x=\{3,5,4,6,4\}$: $n=5$, $\sum x=22$. $L\propto\theta^{10}(1-\theta)^{12}$; prior Beta(2,3) = $\theta(1-\theta)^2$; posterior $\theta^{11}(1-\theta)^{14}$ = Beta(12,15); MAP $=\frac{11}{25}=0.44$.

**Ex.** Poisson, $x=\{2,4,3,5,2,4\}$: $n=6$, $\sum x=20$. $L\propto\lambda^{20}e^{-6\lambda}$; prior Gamma(3,2) = $\lambda^2e^{-2\lambda}$; posterior $\lambda^{22}e^{-8\lambda}$; MAP $=\frac{22}8=2.75$, MLE $=\frac{20}6=3.33$. Prior mean 1.5 < MLE → pulls down; more data → prior fades.

**Ex.** Prior $ae^{-a\theta}$, $p(x|\theta)=\theta e^{-\theta x}$: product $\theta e^{-(x+a)\theta}$, $A=1$, $B=x+a$: MAP $\frac1{x+a}$, MMSE $\frac2{x+a}$. If $p(x|\theta)=\frac1xe^{-\theta x}$: $A=0$ → $(x+a)e^{-(x+a)\theta}$, MMSE $\frac1{x+a}$.

**Ex.** $\frac\lambda2e^{-\lambda x/2}$, $\lambda=\frac1{1+e^{-\theta}}$: ln, differentiate; chain factor $\lambda'=\lambda(1-\lambda)>0$: $\lambda'(\frac1\lambda-\frac x2)=0$ → $\lambda=\frac2x$. Then $1+e^{-\theta}=\frac x2$, $\hat\theta=-\ln(\frac x2-1)$, $x>2$.

**Mixture** of bumps at $\pm x$, weights $c,1-c$: MMSE $=(2c{-}1)x$; MAP = centre of taller bump ($c=\frac12$: $\pm x$).

**Discrete** $X=\pm1$, $Y=X+N$: $w_s=e^{-(y-s)^2/2\sigma^2}$; $P[s|y]=\frac{w_s}{w_1+w_{-1}}$ (divide by the sum) $=\frac1{1+e^{\mp2y/\sigma^2}}$ for $s=\pm1$. MMSE $=P_1-P_{-1}=\tanh\frac y{\sigma^2}$. MAP: $\frac{P_1}{P_{-1}}=e^{2y/\sigma^2}>1$ ⇔ $y>0$ → $+1$; $y_{th}=0$.

## 2.3 · Least squares
Line $y=ax+b$: $dx=x_n-\bar x$, $dy=y_n-\bar y$; $a=\frac{\sum dx\,dy}{\sum dx^2}$, $b=\bar y-a\bar x$. Ex. $(0,3),(2,4),(3,3)$: $a=\frac{1/3}{14/3}=\frac1{14}$, $b=\frac{10}3-\frac1{14}\frac53=\frac{45}{14}$.
Kind of estimator = LS, cost $J=\sum(x[n]-s[n])^2$. If $s[n]=A\,h[n]$: $\hat A=\frac{\sum x[n]h[n]}{\sum h[n]^2}$ ($Ae^{\phi n}$: $h=e^{\phi n}$; constant: $h=1$ → $\bar x$).
**Closed form / avoid non linear optimization:** $s=g(\theta)$ invertible: LS for $\alpha=g(\theta)$, then $\hat\theta=g^{-1}(\hat\alpha)$. Ex. $x=\ln\theta+w$: $\hat\theta=e^{\bar x}$.
**Linear** $x=H\theta+w$: $\hat\theta=(H^TH)^{-1}H^Tx$. Error $\perp$ columns of $H$ ($\hat\theta$ is not). Needs $\ge$ as many data as unknowns. WLS $W=C_x^{-1}$ = BLUE: TRUE.
**Nonlinear:** separating into linear+nonlinear LS, or transforming to linear → TRUE. Gauss-Newton and Newton-Raphson both work. $\theta_{k+1}=\theta_k+(G^TG)^{-1}G^T(x-s(\theta_k))$, $G$ = columns $\partial s/\partial\theta_i$; $\theta=[\phi\ A]^T$: $nAe^{\phi n}$, $e^{\phi n}$.

## 2.4 · CRLB
$i(\theta)=-E[\frac{d^2}{d\theta^2}\ln p]\ge0$ (1 sample); $N$ iid: $\mathcal I=Ni$ TRUE. Unbiased: Var $\ge1/\mathcal I$ (never $\ge\mathcal I$), bound $\propto1/N$ = "decreases linearly with $N$" TRUE. "Always derivable", "strictly +/−" FALSE.
Steps: $\ln p$; differentiate twice; negate, take $E$. Ex $p=\frac x{\theta^2}e^{-x^2/2\theta^2}$: 2nd deriv $\frac2{\theta^2}-\frac{3x^2}{\theta^4}$, $E[x^2]=2\theta^2$ ⇒ $i=\frac4{\theta^2}$, bound $\frac{\theta^2}{4N}$.
Gaussian mean $\mu(\theta)$, var $\sigma^2$: $\mathcal I=\sum(\mu')^2/\sigma^2$; $\mu=A(\cos\theta,\sin\theta)$: $\mu'=A(-\sin,\cos)$, $\sum=A^2$ ⇒ $A^2/\sigma^2$.
MVUE=unbiased+min var, hits bound: $\frac d{d\theta}\ln p=\mathcal I(\hat\theta-\theta)$, $\mathcal I=1/$Var; mean of $N$: Var$=\sigma^2/N$. $\int(x-\theta)d\theta=-\frac12(x-\theta)^2$ ⇒ $p=(2\pi\sigma^2)^{-N/2}e^{-\sum(x-\theta)^2/2\sigma^2}$.
Support of $x$ depends on $\theta$ ⇒ no CRLB.

## 2.5 · MC words
Unbiased $E[\hat\theta]=\theta$ · consistent $\hat\theta\to\theta$ as $N\to\infty$ · efficient: unbiased + Var = CRLB (below the bound is impossible) · MLE = argmax of likelihood; asymptotically unbiased, not always efficient; $\alpha=\psi(\theta)$ one-to-one: $\hat\theta=\psi^{-1}(\hat\alpha)$ · Fisher $\mathcal I>0$; $N$ iid: $N\,i(\theta)$; Var $\ge1/\mathcal I$ (not $\ge\mathcal I$), CRLB falls as $1/N$ · Bayes: prior, minimises risk; squared cost → MMSE = posterior **mean**; uniform cost → MAP = posterior **max**; "always different/equal" is false · MAP needs a prior; only for large $N$ MAP→MLE ("for any prior" is false).

## Checks & sign rules
- Probabilities lie in $[0,1]$; $\iint p=1$; a PSD never goes negative (a *correlogram estimate* may); $P_{FA}$ uses the $H_0$ curve.
- Dividing an inequality by a negative **flips** it.
- Roots of the AR/factorisation quadratics come in pairs $a$ and $1/a$: always keep $|a|\lt1$, $|b|\lt1$ (that is what "minimum phase" wants).
- $x[n]=i[n]-a_1x[n-1]-\dots$ with $r[1]>0$ gives a **negative** $a_1$; a minus sign in front of $\cos\theta$ gives a negative $a$.
- Round only at the very end.

</div>
</div>

<div class="pagebreak"></div>

<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## 3.1 · Correlogram + pick the plot
You get $r[0],r[1],\dots$ = autocorrelation at lag 0, 1, … ($r[-k]=r[k]$); $\theta$ from 0 to $\pi$. "Correlogram method" = one cosine per given lag, stop at the last lag:

$$\hat P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta$$


$r[0]$ alone, others **doubled**; lag not given or "$r=0$ for $|k|>q$" = dropped. "MA($q$)" = lags $0..q$ only. "As function of $\cos\theta$": $c=\cos\theta$, $\cos2\theta=2c^2-1$. $r=3,2,1$: $3+4c+2(2c^2-1)=4c^2+4c+1$.
- MA(2) $x=i+a\,i[n-1]+b\,i[n-2]$, variance 1, given $r[1],r[2]$: $b=r[2]$, $a=r[1]/(1+b)$, $r[0]=1+a^2+b^2$.

**Pick the plot** (curves: correlogram, AR, MA): compute each at $\theta=0$ (all cos $=1$) and $\pi$ ($\cos\theta=-1$, $\cos2\theta=1$, $\cos3\theta=-1$); match heights.
- MA(1) curve $=r_0+2r_1\cos\theta$.
- AR(1): $a_1=-r_1/r_0$, $\sigma^2=r_0+a_1r_1$, $P(0)=\sigma^2/(1+a_1)^2$, $P(\pi)=\sigma^2/(1-a_1)^2$, $P=\sigma^2/(1+2a_1\cos\theta+a_1^2)$.
- AR(2): $D=r_0^2-r_1^2$, $a_1=-r_1(r_0-r_2)/D$, $a_2=(r_1^2-r_0r_2)/D$, $\sigma^2=r_0+a_1r_1+a_2r_2$, $P(0)=\sigma^2/(1+a_1+a_2)^2$, $P(\pi)=\sigma^2/(1-a_1+a_2)^2$.
- $r=2,-\frac14,-\frac3{16}$: corr $2-\frac12\cos\theta-\frac38\cos2\theta$: 1.125, 2.125; MA(1): 1.5, 2.5; AR(1) $a_1=\frac18$, $\sigma^2=\frac{63}{32}$: 1.56, 2.57.

Correlogram may dip below 0; true PSD never.

## 3.2 · AR / MA from $r[k]$
Only $i[n-k]$ on the right (delay $\le q$) → **MA($q$)**; only past $x$ → **AR($p$)**; both → ARMA. $i[n]$ white, variance $\sigma_i^2$. AR form: $x[n]=i[n]-a_1x[n-1]-a_2x[n-2]$ (**minus**). $c=\cos\theta$. $\rho[\tau]$ = $r[\tau]$.

**Correlogram:** $P=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$ to the last given lag (exam "MA($q$)", "finite number of lags": stop at lag $q$, drop the rest). "As a function of $\cos\theta$": $\cos2\theta=2c^2-1$, $\cos3\theta=4c^3-3c$. $r=3,2,1$: $3+4\cos\theta+2\cos2\theta=4c^2+4c+1$.

**MA autocorr:** coefficients $1,b_1,\dots$; $r[l]=\sigma_i^2\times$(sum of products of coefficients $l$ places apart); 0 beyond $q$. $1,-\frac12,\frac14,-\frac12$: $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$, $r[1]=-\frac12-\frac18-\frac18=-\frac34$, $r[2]=\frac14+\frac14=\frac12$, $r[3]=-\frac12$. "Find $a,b$" of MA(2) from $r[1],r[2]$, $\sigma_i^2=1$: $b=r[2]$, $a=r[1]/(1+b)$.

**AR(1):** $a_1=-\frac{r[1]}{r[0]}$; $\sigma_i^2=r[0]+a_1r[1]$; $P=\frac{\sigma_i^2}{1+a_1^2+2a_1c}$. $r=2,-\frac14$: $a_1=\frac18$, $\sigma_i^2=\frac{63}{32}$, $P=\frac{126}{65+16c}$.

**AR(2):** Yule–Walker $\begin{bmatrix}r[0]&r[1]\\ r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\ a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\ r[2]\end{bmatrix}$. $D=r[0]^2-r[1]^2$, $a_1=\frac{-r[1](r[0]-r[2])}{D}$, $a_2=\frac{r[1]^2-r[0]r[2]}{D}$, $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$, $P=\frac{\sigma_i^2}{1+a_1^2+a_2^2+2(a_1+a_1a_2)c+2a_2\cos2\theta}$.
$r=3,2,1$: $D=5$, $a_1=-\frac45$, $a_2=\frac15$, $\sigma_i^2=\frac85$, $P=\frac{10}{5c^2-12c+8}$.
$r=1,.7,.5$: $D=.51$, $a_1=\frac{-.7\cdot.5}{.51}=-.686$, $a_2=\frac{.49-.5}{.51}=-.0196$, $\sigma_i^2=1-.480-.010=.510$.

**MA(1):** $p=\frac{r[0]}{r[1]}$, $b=\frac{p\pm\sqrt{p^2-4}}2$, keep $|b|\lt1$; $\sigma_i^2=r[1]/b$; $P=r[0]+2r[1]c$. $r=2,-\frac14$: $p=-8$, $b=-4+\sqrt{15}\approx-0.13$, $\sigma_i^2\approx1.97$. $p=\frac52$: $\sqrt{6.25-4}=1.5$, $b=\frac{2.5\pm1.5}2=2$ or $\frac12$ → $\frac12$, $\sigma_i^2=\frac4{105}$. If $r[2]=0$ the MA(1) $P$ equals the correlogram.

**ARMA** $x=i+\beta i[n-1]-\alpha x[n-1]$, or filter $H(z)=\frac{1+\beta z^{-1}}{1+\alpha z^{-1}}$ on $i$ (read $\beta,\alpha$ off; $\frac{1-\frac23z^{-1}}{1-\frac12z^{-1}}$: $\beta=-\frac23,\alpha=-\frac12$). $d=\beta-\alpha$: $P=\sigma_i^2\frac{1+\beta^2+2\beta c}{1+\alpha^2+2\alpha c}$; $r[0]=\sigma_i^2(1+\frac{d^2}{1-\alpha^2})$, $r[l]=\sigma_i^2(-\alpha)^{l-1}(d-\frac{\alpha d^2}{1-\alpha^2})$, $l\ge1$. $\beta=-1,\alpha=-\frac34,\sigma_i^2=\frac78$: $P=\frac{28(1-c)}{25-24c}$, $r[0]=1$, $r[1]=-\frac18$, each next lag $\times\frac34$. $\beta=-\frac23,\alpha=-\frac12,\sigma_i^2=1$: $d=-\frac16$, $r[0]=\frac{28}{27}$, $r[1]=-\frac4{27}$, lags $\times\frac12$.

**Theory.** Higher $p$: residual error always falls; risk = overfitting (fits noise). AIC $=N\ln\hat\sigma^2+2p$ (or MDL/FPE): error + penalty per parameter, pick minimum. Any spectrum (even MA nulls) ≈ AR of high enough order. True/false: MA $r$ has lags $0..q$ ($q+1$ values, "length $q$" ✗); models compress data ✓; ARMA $R$ diagonal ✗; MA Yule–Walker is non-linear ✓. Plot pick: compute $P$ at $c=1$, $c=-1$, match heights.

## 3.3 · Periodogram, Bartlett, Welch, windows
- **periodogram**: $\frac1N|\text{DFT of data}|^2$ = **correlogram** (DFT of $\hat r[k]$, lags up to $N-1$). Variance $\approx P^2$, not consistent. Bias: smoothed by triangular window, asymptotically unbiased.
- **Bartlett**: **non-overlapping** segments (length $M=N/K$), average periodograms: variance $\approx P^2/K$, bias up (shorter $M$ = more bias, resolution $\approx2\pi/M$).
- **Welch** (=WOSA): **overlapping windowed** segments, average: variance below periodogram but **larger** than Bartlett (correlated segments, not $1/K$); bias above raw, below Bartlett (longer segments).
- **Blackman–Tukey**: window $\hat r[k]$ ($M\lt L$), DFT; consistent, variance $\to0$; bias up for shorter $M$.
- **parametric**: AR/MA/ARMA, $P=\sigma_i^2|B|^2/|A|^2$.

Consistent: BT, Bartlett/Welch ($K\to\infty$). FT of $r$: correlogram, BT. Averages periodograms: Bartlett, Welch. "Bias $\propto P^2$": none.
Table ("complete the table"): write idea + bias + variance as above.

**Welch:** $D=L-$overlap; $K=\frac{N-L}{D}+1$; variance ratio $\frac1K$. $N=1000,L=200$, 50%: $D=100$, $K=\frac{800}{100}+1=9$, ratio $\frac19\approx0.11$.

**Energy/power:** dies out or finite length → **energy** ($P=0$); never dies out (const, sin, cos, even $\cos t\,u(t)$) → **power** ($E=\infty$). $A\sin\omega t$: $P=\frac{A^2}2$. $e^{-n}$, $n\ge0$: $E=\frac1{1-e^{-2}}\approx1.16$. $e^{-t}u(t)$, box, $5e^{-2|t|}$: energy.

**Windows:** main-lobe width → resolution (wide = worse). Side-lobe height → leakage (high = worse). Rectangular: narrowest lobe, highest side lobes. Longer window: narrower lobe.
Zero-padding: more dots of the same FTD, **no** better resolution. Plots: inf. cos = 2 spikes; windowed FTD = smooth; padded DFT = dense dots; unpadded = few dots. Jan22 plots: spikes B, smooth D, dense C, few A → (b).

**False:** longer data cuts leakage · window improves resolution · Bartlett zero-pads · periodogram beats correlogram · window changes variance. **True:** bias hits deterministic and stochastic signals.

**AR order $p$:** error always drops with $p$ → **overfitting**. **AIC** $=N\ln\hat\sigma^2+2p$, **FPE** $=\frac{N+p}{N-p}\hat\sigma^2$: error + penalty, pick min. Any PSD ≈ AR of **high enough order**.

## 4.1 · Likelihood-ratio test
$L=\frac{p(x|H_1)}{p(x|H_0)}$ = height of the $H_1$ curve ÷ height of the $H_0$ curve at your data. Decide $H_1$ if $L\gt\lambda$ (the bar, given; also $\eta$, $\gamma$). The **cut** = the $x$ where $L=\lambda$.

1. $L$ = ($H_1$ formula)/($H_0$ formula), numbers plugged in. $N$ samples → multiply the $N$ ratios.
2. Simplify: $x^a/x^b=x^{a-b}$, $e^ae^b=e^{a+b}$ (so $\prod_n e^{-|x_n|}=e^{-\sum|x_n|}$), $c\cdot c\cdots c=c^N$, equal factors cancel.
3. $L\gt\lambda$; ln both sides: $\ln e^a=a$, $\ln c^N=N\ln c$, $\ln(ab)=\ln a+\ln b$, $\ln\frac1a=-\ln a$.
4. Move constants across, isolate $x$ (or $x^2$, $\sum x^2$). Divide by a negative → flip $\gt$ to $\lt$.
5. Check: put one $x$ from each side into $L$.
6. $P_{FA}$ = $H_0$ area over the "decide $H_1$" region; $P_D$ = $H_1$ area there; $P_M=1-P_D$. Region $|x|\gt\gamma$ = two tails → ×2 (curves symmetric).

**A.** $p=k_1\theta x^{k_2\theta-1}$, $0\lt x\lt1$, $\theta_0=3,\theta_1=6$, $\lambda=0.2$, $k_1=1,k_2=2$: $3x^5$ vs $6x^{11}$; $L=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=0.68$.

**B.** $H_0:\frac1{\sqrt{2\pi}}e^{-y^2/2}$, $H_1:\frac14e^{-y/2}$, bar 1. $L=0.627e^{y^2/2-y/2}\gt1$; ln: $-0.467+\frac{y^2}2-\frac y2\gt0$; ×2: $y^2-y-0.934\gt0$; $y=\frac{1+\sqrt{1+4\cdot0.934}}2=1.59$. $P_{FA}=Q(1.59)=0.056$; $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac12e^{-0.795}=0.23$. With $|y|$ (all $y$): same cut $|y|\gt1.59$, double the areas.
Integrals: $\int ke^{-ay}=-\frac kae^{-ay}$; $\int_0^g ke^{-ay}dy=\frac ka(1-e^{-ag})$; $\int_g^\infty ke^{-ay}dy=\frac kae^{-ag}$.

**C (Rayleigh).** $p=\frac x{\sigma^2}e^{-x^2/2\sigma^2}$, $\sigma_1\gt\sigma_0$, bar $\eta$. $L=\frac{\sigma_0^2}{\sigma_1^2}e^{\frac{x^2}2(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})}\gt\eta$ → $x\gt\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{\eta\sigma_1^2}{\sigma_0^2}}$. $P_{FA}=e^{-\gamma^2/2\sigma_0^2}$, $P_D=P_{FA}^{\sigma_0^2/\sigma_1^2}$: $\sigma$'s further apart (exam: "separation") → smaller exponent → higher $P_D$ at same $P_{FA}$. Read $\sigma^2$ from $e^{-x^2/(2\sigma^2)}$: $e^{-x^2/8}$ → $\sigma^2=4$.

**D (Laplace, N samples).** $H_0:\frac12e^{-|x|}$, $H_1:e^{-2|x|}$: per sample $2e^{-|x|}$; $L=2^Ne^{-\sum|x_n|}\gt\lambda$; ln: $N\ln2-\sum|x_n|\gt\ln\lambda$ → ×(−1): decide $H_1$ if $\sum|x_n|\lt\gamma'=N\ln2-\ln\lambda$. For $N=1$, $y=|x|$: $H_0:e^{-y}$, $H_1:2e^{-2y}$, $H_1$ for $y\lt\gamma'$: $P_{FA}=1-e^{-\gamma'}$, $P_D=1-e^{-2\gamma'}$. $P_{FA}=0.1$: $e^{-\gamma'}=0.9$, $\gamma'=-\ln0.9=0.105$, $P_D=1-0.9^2=0.19$.

**E (exponential).** $\lambda_0e^{-\lambda_0x}$ vs $\lambda_1e^{-\lambda_1x}$, $\lambda_1\gt\lambda_0$: $L=\frac{\lambda_1}{\lambda_0}e^{-(\lambda_1-\lambda_0)x}\gt1$ → $x\lt x_{th}=\frac{\ln(\lambda_1/\lambda_0)}{\lambda_1-\lambda_0}$ ($\lambda_1=2,\lambda_0=0.1$: $3.0/1.9=1.58$). $P_D=1-e^{-\lambda_1x_{th}}$, $P_{FA}=1-e^{-\lambda_0x_{th}}$. Find $\lambda_1$ for $P_{FA}=P_{FA}^*$, $P_D=P_D^*$: $x_{th}=-\ln(1-P_{FA}^*)/\lambda_0$, then $\lambda_1=-\ln(1-P_D^*)/x_{th}$. **ROC** = plot ($P_{FA}$, $P_D$) as the threshold slides: (0,0)→(1,1), above the diagonal; more separation → closer to top-left.

**F (Gaussian variances, N samples).** $p=\frac1{\sqrt{2\pi}\sigma}e^{-x^2/2\sigma^2}$, $\sigma_1\gt\sigma_0$: $L=(\frac{\sigma_0}{\sigma_1})^Ne^{\frac12(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})\sum x_n^2}\gt\eta$; ln: $N\ln\frac{\sigma_0}{\sigma_1}+\frac12(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})\sum x_n^2\gt\ln\eta$ → decide $H_1$ if $\sum x_n^2$ is big. One sample: $|x|\gt\gamma$, $P_{FA}=2Q(\gamma/\sigma_0)$, $P_D=2Q(\gamma/\sigma_1)$. E.g. $\sigma_1=3\sigma_0$, $\gamma=\sigma_1$: $2Q(3)=0.003$, $2Q(1)=0.32$.

**Q(t)** = standard Gaussian area right of $t$: $Q(0)=0.5$, $Q(1)=0.159$, $Q(2)=0.023$, $Q(3)=0.0013$; $Q(-t)=1-Q(t)$. General Gaussian: $Q(\frac{t-\mu}\sigma)$. $P_{FA}=\alpha$ → $\gamma=\mu_0+\sigma_0Q^{-1}(\alpha)$: $Q^{-1}(.10)=1.28$, $(.05)=1.645$, $(.025)=1.96$, $(.01)=2.33$.

## 4.2 · Bayesian detection
Same LRT, bar from priors and costs. $P_0,P_1$ = chances of $H_0,H_1$ before measuring. $C_{ij}$ = cost of deciding $i$ when $j$ is true ($C_{10}$ false alarm, $C_{01}$ miss).

$$\lambda=\frac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$$


Correct cost 0, errors equal → $\lambda=P_0/P_1$. Equal priors too → $\lambda=1$ (max likelihood).
**Ex D.** Rayleigh, $P_0=0.9,P_1=0.1$: $\lambda=9$. Accept $H_1$ if $x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{9\sigma_1^2}{\sigma_0^2}}$ (the 4.1 Rayleigh threshold with $\eta=9$).
**Posteriors given:** decide $H_1$ if $\frac{P(H_1|x)}{P(H_0|x)}\gt\frac{C_{10}-C_{00}}{C_{01}-C_{11}}$. Ex: $C_{01}=100C_{10}$ → right $0.01$; $H_0$ posterior 5× smaller → left $5$; $5\gt0.01$ → $H_1$.
**Ex F.** $p_0=e^{-y}$, $p_1=2e^{-2y}$, $P_0=.4,P_1=.6$. Threshold: $2e^{-2y}(.6)=e^{-y}(.4)$. Divide by $e^{-y}$ ($e^{-2y}/e^{-y}=e^{-y}$): $1.2e^{-y}=.4$ → $e^{-y}=\frac13$ → $y=\ln3\approx1.10$ ($e^{-y}=1/k$ ⇒ $y=\ln k$). Small $y$ favours $H_1$ → decide $H_1$ if $y<\ln3$. Density $ce^{-cy}$: $P(y>a)=e^{-ca}$, $P(y<a)=1-e^{-ca}$; $e^{-c\ln3}=(\frac13)^c$. $P_{FA}=P(y<\ln3;H_0)=1-\frac13=\frac23$. $P_M=P(y>\ln3;H_1)=(\frac13)^2=\frac19$.
**Gaussian $P_D,P_{FA}$** ($\sigma=1$, $x=y_{th}-\mu$, $\mu=0$ for $H_0$): $P=1-0.5(1+\text{erf}(x/\sqrt2))$, erf from table, erf$(-x)=-$erf$(x)$. E.g. $y_{th}=1,\mu=1$: $x=0$ → $P_D=0.5$. Bigger $\mu$ → higher ROC curve.
**True/false.** Bayes **minimises** risk; costs 0/equal (1, 10, any) → min $P_e$. Neyman-Pearson: fixed $P_{FA}$, **max** $P_D$. Bigger $P_1$ → smaller $\lambda$ → easier $H_1$. Check each verb; if all read correct, answer "none is false". Matched filter: max output SNR, $h[n]=s[N-1-n]$ (flipped).
**2×2 table** (rows decide, cols true): decide $H_0$/true $H_1$ = miss (type II, false negative); decide $H_1$/true $H_0$ = false alarm (type I, false positive); correct ones = true negative ($H_0$), detection/true positive ($H_1$).

**ROC.** $P_D$ (vertical) vs $P_{FA}$ (horizontal), all thresholds: above the diagonal ($P_D\gt P_{FA}$). *Below* = $H_0/H_1$ swapped in $L$; CDF instead of its complement ($P_D=P(y\gt\gamma)$); or $P_D,P_{FA}$ swapped. Wrong $\sigma$: changes height, never direction. **t-statistic** $t=\frac{\hat\mu-\mu_0}{\hat\sigma/\sqrt N}$: big $|t|$ = evidence against $H_0$; larger $N$ / smaller $\hat\sigma$ → bigger $|t|$; $t$ random. "Smaller $t$ = less likely $H_0$" is FALSE.

</div>
</div>
