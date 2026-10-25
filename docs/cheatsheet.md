---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet</h1>

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This sheet fills both sides: Ctrl/Cmd + P → A4, margins minimal, untick "headers and footers", scale 100 %. Better still: copy it by hand — writing it is half the studying.</p>
<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## 1.2 · Joint PDF: $c$, marginal, conditional, independent

**Use this** when two variables $X,Y$ come with a joint function $p(x,y)$: a formula (continuous, integrate) or a table (discrete, add). A single variable's PDF belongs to 2.1. Plain counts per group are not this recipe.

Here $p(x,y)$ is the joint PDF (or PMF for a table), and "0 otherwise" means it is zero outside the given region.

**Discrete or continuous?** A variable is **discrete** when you can list its outcomes: a table of probabilities, counts of people, a die, "the number of …". Then you **add**. It is **continuous** when it can take any value in a range: time, length, weight, a voltage, "between 0 and 1". Then you **integrate**. The question gives a table or a list of values → discrete; it gives a formula with $x,y$ over intervals → continuous. (A count like "6 of 8 free throws" is binomial: $P(k \text{ of } n)=\binom nk p^k(1-p)^{n-k}$, with $\binom nk$ = "n choose k" from the exam formula list.)

**Expected value** $E[g(X)]$ = the average of $g$ over the distribution: $\sum_x g(x)p(x)$ when discrete, $\int g(x)p(x)\,dx$ when continuous. $E[X]$ is the balance point of the pdf.

**First, draw the region where $p\ne0$** in the $(x,y)$ plane and read every limit from it: for a fixed $x$, the inner integral runs from the lower boundary curve of the region up to the upper one (the $x$-values *inside* the drawn region), and the outer integral runs over the full span of the other variable. Tiny integral crib: $\int y\,dy=\frac{y^2}{2}$, $\int y^2\,dy=\frac{y^3}{3}$, $\int e^{ky}\,dy=\frac{1}{k}e^{ky}$.

**Recipe**

1. **Find $c$ (normalisation).** The total probability must be 1, because $X,Y$ take some value for sure. Integrate $p$ over the region: inner $\int dx$ from one edge of the region to the other (for fixed $y$), then outer $\int dy$ over the rest. Set the result $=1$ and solve for $c$.

2. **Marginal.** $p_X(x)=\int p(x,y)\,dy$: fix $x$ and integrate $y$ over all its values, because $Y$ may be anything and we only ask about $X$. Likewise $p_Y(y)=\int p\,dx$. Write the domain where it is non-zero, and "0 otherwise". For a PMF table, $p_X(x)$ is the **sum of the row** $X=x$ over all $Y$ columns, same reason with sums.

3. **Conditional.** $p_{X\mid Y}(x\mid y)=\dfrac{p(x,y)}{p_Y(y)}$, where $p_Y(y)$ is the marginal of $Y$. Fixing $Y=y$ keeps one slice of the joint; dividing by the slice's total mass $p_Y(y)$ rescales it so it integrates to 1 in $x$. Domain: the $x$-values of the slice, and the $y$ with $p_Y(y)>0$.

4. **Independent** iff (a) the region is a **rectangle** (the $x$-limits do not depend on $y$) and (b) $p(x,y)=p_X(x)\,p_Y(y)$ at every point. Multiply the two marginals and compare with $p$. Fail either → dependent. Rectangle matters because if the limits depend on $y$, knowing $Y$ restricts $X$.

**Worked examples, one per type**

When the exam says "find the constant $c$", the total probability must be 1: do step 1. *apr25-1c:* $p=cx+1$ on $x,y\ge0$, $x+y<1$. The region is a triangle. For fixed $y\in[0,1)$, $x$ runs from 0 to $1-y$, because $x<1-y$. Inner integral: $\int_0^{1-y}(cx+1)\,dx=c\frac{(1-y)^2}{2}+(1-y)$. Outer: $\int_0^1\frac{(1-y)^2}{2}dy=\frac16$ and $\int_0^1(1-y)dy=\frac12$, so the total is $\frac c6+\frac12$. Set it to 1: $\frac c6=\frac12$, so $c=3$.

When the exam says "marginal PDF, indicate its domain", do step 2 and write the domain; when it says "justify independence", do step 4. *jun26-1c:* $p=6x^2y$ on $0\le x\le1$, $0\le y\le1$. For fixed $x$, $y$ runs over $[0,1]$: $p_X(x)=\int_0^1 6x^2y\,dy=6x^2\cdot\frac{1}{2}=3x^2$, domain $0\le x\le1$. Independence: the region is the square $[0,1]^2$, a rectangle. Also $p_Y(y)=\int_0^1 6x^2y\,dx=6y\cdot\frac13=2y$. Then $p_X p_Y=3x^2\cdot2y=6x^2y=p$ everywhere → **independent**.

When the exam says "conditional PDF, domain", it needs the marginal first: do step 2, then step 3, and write the domain. *apr24-1c:* $p=2$ on $0\le y\le x\le1$. For fixed $y$, $x$ runs from $y$ to 1, so $p_Y(y)=\int_y^1 2\,dx=2(1-y)$ for $0\le y\le1$. Then $p_{X\mid Y}(x\mid y)=\frac{2}{2(1-y)}=\frac{1}{1-y}$ for $y\le x\le1$. Domain also needs $y<1$, since $p_Y(1)=0$ cannot divide.

## 1.3 · WSS and ergodic
Words: $X(t)$ = random process, a family of signals. $E[\cdot]$ = average over the random part ($U$, $A$, or the die roll), with $t$ kept fixed. $r[\tau]$ = autocorrelation at lag $\tau$ (correlation of the signal with a copy of itself shifted by $\tau$ steps).

**How the exam words pick the part.** When the question asks whether the process is "wide-sense stationary" (or "WSS"), do part A. When it asks whether it is "ergodic in the mean", "ergodic (mean)" or just "ergodic", do part B (part A first: B needs A's constant mean). When an option says "ergodic in both mean and variance", check the mean with B and the variance with D; on the dice questions the key answer has always been that option.

**A. WSS.** Do steps 1 and 2 for each process. Both must pass.
1. Compute the mean $E[X(t)]$. If $t$ is still in the answer → not WSS and not ergodic. Otherwise the mean is a constant. (Why: WSS needs a constant mean.)
2. Compute $E[X(t)X(t+\tau)]$, the correlation between times $t$ and $t+\tau$. If $t$ is still there → not WSS. If only $\tau$ is left → WSS yes. (Why: the correlation must depend only on the shift, not on the starting time.)

**B. Ergodic in the mean.** Only if A.1 gave a constant mean. If not, answer "not ergodic" at once.
1. Fix ONE draw ($U$, $A$, or one die). Average that single signal over time $t$: for a formula in $t$, the average over one full cycle of a sine or cosine is 0, and constants stay as they are (so $\cos(t+U)$ averages to 0 whatever $U$ is); for a die or a sum, the average is the plain mean of its values over many rolls, e.g. $(1+2+3+4+5+6)/6=3.5$.
2. If this time average equals $E[X]$ for every draw → ergodic yes. If it differs from draw to draw → not ergodic. (Why: one long signal then reveals the ensemble mean.)

**D. Ergodic in the variance.** Same test as B but for the spread: compute the variance of one fixed draw over time and compare it with $\operatorname{Var}[X]=E[X^2]-(E[X])^2$, computed over the draws. Equal for every draw → ergodic in the variance too. (For the fair die both are the variance of one roll, so yes.)

**C. Worked examples, one per type.**

*Type 1, "WSS and ergodic in the mean", $X(t)=\cos(t+U)$, $U\sim$ Uniform$(0,2\pi)$ (apr24, process 1).* $U$ is a random phase, any angle between 0 and $2\pi$ equally likely.
- Step A.1: over one full cosine cycle the positive halves cancel the negative halves, so $E[X(t)]=0$. No $t$ left → constant mean 0.
- Step A.2: we need $E[\cos(t+U)\cos(t+\tau+U)]$. The exam gives the product-to-sum identity $\cos\alpha\cos\beta=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2$. We choose $\alpha=t+U$ and $\beta=t+\tau+U$ because they are exactly the two cosines' angles; that choice makes $\alpha-\beta=-\tau$ (the lag we want, with no $t$ and no $U$ in it) and $\alpha+\beta=2t+\tau+2U$ (everything else). So $r[\tau]=\frac12\cos\tau+\frac12\cos(2t+\tau+2U)$. The first term has no random part and survives the average. The second contains $2U$: when $U$ runs over $0$ to $2\pi$, $2U$ runs over two full cycles, and a cosine over any whole number of cycles averages to 0. So $r[\tau]=\frac12\cos\tau$, no $t$ left → WSS **yes**.
- Step B: one fixed $U$ gives the single signal $\cos(t+U)$. Its time average is the average of a cosine over its cycles = 0, for every $U$, and $E[X]=0$ too → ergodic **yes**.
- Table row 1: WSS Yes, Ergodic Yes.

*Type 4, fair dice (apr25, jan22).* Mean of one die: $(1+2+3+4+5+6)/6=21/6=3.5$, not 0. One die rolled many times has a long-run average of its own face values = $(1+2+3+4+5+6)/6=3.5$ too, the same as the mean → ergodic in the mean. The long-run spread of one die's rolls equals the spread of one roll → ergodic in the variance as well (part D). Key answer: option "ergodic in both mean and variance" (apr25 (b), jan22 (b)).

## 1.4 · Spectral factorisation

**Use this recipe** when the power spectrum $P(e^{j\theta})$ is a ratio of cosine expressions (no time-domain pdf is given; a pdf given means 1.2 / 2.1 instead).

**Names:** $\theta$ = frequency angle in radians; $z=e^{j\theta}$ = point on the unit circle; $z^{-1}$ = one-sample delay; $N,M$ = constants of the top, $A,B$ = constants of the bottom; $p,q$ = generic constants of one cosine factor; $r$ = a root; $a,b$ = filter coefficients; $C,D$ = scaling constants; $\sigma_i^2$ = noise variance; $L$ = causal filter.

**Tool and why it works.** The goal is to split one cosine factor $p+q\cos\theta$ into two mirror factors $\frac{q}{2r}(1+rz^{-1})(1+rz)$. Why it works: multiply the two brackets out, $(1+rz^{-1})(1+rz)=1+r(z+z^{-1})+r^2$, and on the unit circle $z=e^{j\theta}$ gives $z+z^{-1}=2\cos\theta$ (Euler: $e^{j\theta}+e^{-j\theta}=2\cos\theta$). So the product is $r\left(r+\frac1r+2\cos\theta\right)$, which matches $p+q\cos\theta$ once $r+\frac1r=\frac{2p}{q}$.

**Finding $r$ (the step the examples hide).** Multiply $r+\frac1r=\frac{2p}{q}$ by $r$: it becomes the quadratic $r^2-\frac{2p}{q}r+1=0$, whose two roots are $r=\dfrac{p\pm\sqrt{p^2-q^2}}{q}$ (quadratic formula with $a=1$, $b=-2p/q$, $c=1$; the $\sqrt{p^2-q^2}$ comes from $\sqrt{b^2-4ac}$). The two roots multiply to 1, so one is inside the unit circle and one outside.

**Keep the root with $|r|<1$**, and throw the other away: only the inside-root makes $(1+rz^{-1})$ have its zero inside the unit circle, which is what "causal and minimum phase" means (the filter's coefficients die out instead of blowing up).

**Recipe**
1. Bottom $A+B\cos\theta$: take $p=A$, $q=B$, keep the root with $|a|<1$ as $a$. Then $C=\frac{q}{2a}$. Why: by the tool, the bottom equals $C(1+az^{-1})(1+az)$.
2. Top $N+M\cos\theta$: same with $p=N$, $q=M$, giving $b$ and $D$. If $M=0$ there is no cosine to factor: no $b$, and $D=N$.
3. So $P=\frac DC\cdot\frac{(1+bz^{-1})(1+bz)}{(1+az^{-1})(1+az)}$. Keep only the $z^{-1}$ parts for $L$, because $L$ must be causal (the $z$ parts are the mirror image, not causal). Why $\sigma_i^2=\frac DC$: white noise of variance $\sigma_i^2$ filtered by $L$ gives $\sigma_i^2|L|^2$, so the constant in front is the variance.
4. Answer: $\sigma_i^2=\frac DC$ and $L(z)=\frac{1+bz^{-1}}{1+az^{-1}}$ (if $M=0$: $L=\frac{1}{1+az^{-1}}$).

**How the exam words pick the task.** When the question asks to "find the spectral factorisation" and then $L(z)$ and $\sigma_i^2$, do steps 1–4 and write both answers. When it asks "which of the following is the spectral factorisation?", do steps 1–4 once anyway, then pick the option with the same numbers; reject any option whose $L$ contains the root outside the unit circle. When it asks "which condition must the innovation filter satisfy?", the answer is **minimum phase**: all its poles and zeros lie inside the unit circle (reject "maximum phase" and "all-pass").

**Example A** ("find the spectral factorisation", April 2024, $P=\frac{7}{25-24\cos\theta}$, no cosine on top)
Bottom: $A=25$, $B=-24$, so $p=25$, $q=-24$. Then $p^2-q^2=625-576=49$ and $\sqrt{49}=7$. The two roots of the formula are $\frac{p\pm\sqrt{p^2-q^2}}{q}=\frac{25+7}{-24}=-\frac43$ and $\frac{25-7}{-24}=-\frac34$. Only $-\frac34$ has $|r|<1$, so $a=-\frac34$ and $C=\frac{q}{2a}=\frac{-24}{2(-3/4)}=\frac{-24}{-3/2}=16$.
Top: no cosine, so $D=N=7$ and no $b$.
Answer: $\sigma_i^2=\frac{7}{16}$ and $L(z)=\frac{1}{1-\frac34z^{-1}}$ (since $1+az^{-1}$ with $a=-\frac34$ is $1-\frac34z^{-1}$).

## 2.1 · Maximum likelihood (MLE)

**Use this recipe** when a pdf $p(x\mid\theta)$ of the data is given and the question asks for the estimate $\hat\theta$. **Not this one**: if a prior or a posterior appears, that is MAP (see MC below); if the question asks for a least-squares fit, that is not MLE.

*Words the "not this one" line uses.* A **prior** $p(\theta)$ = what you believe about $\theta$ *before* seeing data. A **posterior** $p(\theta\mid x)$ = what you believe *after* seeing the data $x$. **MAP** = the $\theta$ where the posterior peaks (2.2). **Least squares** = choose $\theta$ to minimise the total squared gap between data and model (2.3), no pdf needed.

**Symbols.** $\theta$ = the unknown parameter we estimate. $\hat\theta$ ("theta hat") = our estimate. $x_n$ = the $n$-th observed sample, $n=1,\dots,N$. $N$ = number of samples. $\ln$ = natural log. $L$ = likelihood = joint pdf of all samples, read as a function of $\theta$. $\sum$ = add over all samples. $\bar x=\frac1N\sum x_n$ = sample mean.

**Recipe**

1. Likelihood and log-likelihood. $L=\prod_{n=1}^N p(x_n\mid\theta)$: samples are independent, so the joint density is the product of single densities. $\ln L=\sum_n\ln p(x_n\mid\theta)$: ln is increasing, so the $\theta$ that maximises $L$ also maximises $\ln L$, and sums are easier to differentiate. (If the question only says "write the likelihood and log-likelihood", stop here.)
2. Differentiate $\ln L$ with respect to $\theta$. Only $\theta$ varies, so a term without $\theta$ (e.g. $\ln x$) is a constant with derivative 0. A term without $n$ appears in all $N$ terms of the sum, so it counts $N$ times.
3. Set the derivative to 0: a maximum of a smooth curve is where its slope is zero. Multiply by $\theta^2$ to clear fractions; legal because $\theta>0$. Solve for $\hat\theta$.

**Worked examples** (each line says what the number is)

**A. Gamma with known $k$ (jun26-2b).** Here $x_i$ = recovery days of patient $i$, $n$ patients, $k$ = known number of stages, $\theta$ = unknown average time per stage. The question is asked in three shapes: "write the likelihood and log-likelihood" wants step 1 only; "derive the MLE for $\theta$" wants steps 1–3; "explain what the MLE tells us" wants the meaning paragraph at the end.

1. Each patient's factor has $\theta^{-k}$; $n$ patients give $\theta^{-nk}$. $\ln L=\sum_i(k-1)\ln x_i-nk\ln\theta-\frac{\sum_i x_i}{\theta}-n\ln\Gamma(k)$. The first and last terms have no $\theta$.
2. $\frac{d\ln L}{d\theta}=-\frac{nk}\theta+\frac{\sum_i x_i}{\theta^2}$ ($-nk\ln\theta$ gives $-\frac{nk}\theta$; $-\frac{\sum x_i}\theta$ gives $+\frac{\sum x_i}{\theta^2}$).
3. Times $\theta^2$: $-nk\theta+\sum x_i=0$, so $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}k$.

Meaning: $\hat\theta=\bar x/k$ is the estimated average time per stage. The Gamma mean is $k\theta$, so $k\hat\theta=\bar x$: the fitted mean recovery equals the observed mean.

**E. Unknown $\rho$, single observation (jan25-2b).** Here the $\theta$ inside the pdf is a *given* correlation number, not the parameter. $\mu,\sigma,\theta$ = observed data; $N=1$, so no sum.

1. The prefactor $\frac1{2\pi\sqrt{1-\theta^2}}$ does not contain $\rho$, so it is constant. Exponent: $\mu^2\rho^2+\sigma^2\rho^2=(\mu^2+\sigma^2)\rho^2$, so $\ln p=\text{const}-\frac{(\mu^2+\sigma^2)\rho^2-2\mu\sigma\theta\rho}{2(1-\theta^2)}$.
2. $\frac{d\ln p}{d\rho}=-\frac{2(\mu^2+\sigma^2)\rho-2\mu\sigma\theta}{2(1-\theta^2)}$.
3. The factor $-\frac1{2(1-\theta^2)}$ is nonzero (since $|\theta|<1$), so set the bracket to 0: $(\mu^2+\sigma^2)\rho=\mu\sigma\theta$, so $\hat\rho=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}$.

**G. Sigmoid (apr25-2c).** $\lambda(\theta)=\frac1{1+e^{-\theta}}$ is a number in $(0,1)$. Do NOT expand $\lambda(\theta)$: find $\hat\lambda$ first, then convert. $p=3\lambda e^{-4\lambda x/7}$, $x>1$.

1. $\ln p=\ln3+\ln\lambda-\frac{4x}7\lambda$.
2. $\frac{d\ln p}{d\lambda}=\frac1\lambda-\frac{4x}7$.
3. $\frac1{\hat\lambda}=\frac{4x}7$, so $\hat\lambda=\frac7{4x}$.
4. Sigmoid is one-to-one, so invert it: $1+e^{-\theta}=\frac1\lambda$ → $e^{-\theta}=\frac{1-\lambda}\lambda$ → $\hat\theta=\ln\frac{\hat\lambda}{1-\hat\lambda}$. With $\hat\lambda=\frac7{4x}$: $\frac{7/(4x)}{(4x-7)/(4x)}=\frac7{4x-7}$, so $\hat\theta=\ln\frac7{4x-7}=-\ln\left(\frac{4x}7-1\right)$.

Valid only for $x>\frac74$: otherwise $\hat\lambda\ge1$, and a sigmoid never reaches 1.

**MC (no algebra, pick the TRUE one)**

- jan22-2b, answer **(c)**, "transform the parameter": the MLE is **invariant** — if the question rewrites the unknown as $\alpha=\psi(\theta)$, you may solve for $\hat\alpha$ with this same recipe and then map back with $\hat\theta=\psi^{-1}(\hat\alpha)$ (e.g. $\alpha=\ln\theta$ → $\hat\theta=e^{\hat\alpha}$). Any option saying you must re-derive from scratch, or that the estimate changes with the parametrisation, is false.
- nov22-2b, answer **(c)**: ML is asymptotically unbiased (the bias fades as $N$ grows). "Unbiased for any $N$" is false; "consistent" is true.

## 2.2 · MAP with a prior

Symbols: $\theta$ (or $\lambda$) is the unknown parameter. $x$ is the observed data. $L(\theta)$ is the likelihood, the probability of the data as a function of $\theta$. $p(\theta|x)$ is the posterior, the density of $\theta$ after seeing the data. Bayes' rule gives posterior $\propto$ likelihood $\times$ prior. The sign $\propto$ means "equal up to a constant that does not contain $\theta$". Such constants cannot move a peak, so MAP never needs them.

**How the exam words name the estimator.** When the question says "MAP", "maximum a posteriori" or "most probable value", it wants the **peak of the posterior**: $\hat\theta_{MAP}=\arg\max_\theta p(\theta|x)$ — this needs a prior, since without one there is no posterior. When it says "MMSE", "minimum mean square error", "posterior mean" or "the average of $\theta$", it wants the **average under the posterior**: $\hat\theta_{MMSE}=\int\theta\,p(\theta|x)\,d\theta$ (a sum if $\theta$ is discrete). When it says "MLE", it wants the peak of the likelihood $L$ alone, with no prior at all.

**How the question picks the recipe.** If it gives a Beta or Gamma prior together with a standard PMF/pdf likelihood (see the crib), use recipe A from step 1. If the posterior is *already* written as $\theta^A(1-\theta)^B$ or $\lambda^Ae^{-B\lambda}$, the work of steps 1–3 is done for you: jump to step 4 for MAP or step 5 for MMSE. If the posterior contains a function of $\theta$ (a sigmoid, $e^{\theta}$) or the prior is not Beta/Gamma, use recipe B.

**Standard likelihoods crib** (what each observation contributes to $L$)
- "exactly $k$ successes in $n$ tries" → binomial: $\binom nk\theta^k(1-\theta)^{n-k}$.
- "the $k$-th success happens on trial $x$" → $\theta^k(1-\theta)^{x-k}$ (e.g. $k=2$: $\theta^2(1-\theta)^{x-2}$).
- "count of events per unit time, rate $\lambda$" → Poisson: $\dfrac{\lambda^{x}e^{-\lambda}}{x!}$ (its log is $x\ln\lambda-\lambda-\ln x!$).
- "waiting time $x$, rate $\lambda$" → exponential: $\lambda e^{-\lambda x}$.
- "Gaussian data, mean $\mu(\theta)$, variance $\sigma^2$" → $\dfrac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2}$.

**Recipe A: conjugate prior (Beta or Gamma)**

A Beta($\alpha,\beta$) prior has pdf $\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$ — a prior for a **probability** $\theta$ in $(0,1)$. A Gamma($\alpha,\beta$) prior has pdf $\propto\lambda^{\alpha-1}e^{-\beta\lambda}$, where $\beta$ is a rate — a prior for a **positive rate** $\lambda$. Use the numbers the question gives. A **uniform prior** is flat: $p(\theta)$ = constant on its range and 0 outside, so it contributes nothing to the product except the range (a MAP answer may then hit the range's edge).

1. Likelihood $L=\prod_i P(x_i|\theta)$. Multiply the probabilities of the $n$ observations because they are independent. Drop factors without $\theta$, such as $\binom{x-1}{k-1}$ or $1/x_i!$, because they do not move the peak. Add exponents of equal bases: $\theta^a\theta^b=\theta^{a+b}$.
2. Multiply by the prior, by Bayes' rule. Add the exponents again.
3. Name the posterior. $\theta^A(1-\theta)^B$ is Beta($A+1,B+1$). $\lambda^Ae^{-B\lambda}$ is Gamma(shape $A+1$, rate $B$). The $+1$ is there because a Beta($a,b$) pdf has exponents $a-1$ and $b-1$.
4. MAP. Beta type: $\hat\theta=\frac{A}{A+B}$, from setting the derivative of $A\ln\theta+B\ln(1-\theta)$ to zero. Gamma type: $\hat\lambda=\frac AB$, from $A/\lambda-B=0$.
5. MMSE = mean of the posterior. Beta type: $\frac{A+1}{A+B+2}$. Gamma type: $\frac{A+1}{B}$.
6. MLE: step 1 only, then the same peak formula with no prior exponents.

*Example, exam says "write the likelihood, derive the posterior, compute MAP" (jun26-2c).* Each patient's screening count has PMF $\theta^2(1-\theta)^{x-2}$, because the $k=2$ successes give $\theta^2$ and the $x-2$ failures give $(1-\theta)^{x-2}$. There are $n=5$ rounds with $x=3,5,4,6,4$, so $\sum x=3+5+4+6+4=22$.
- Step 1: the $\theta$ exponent is $2$ per round, so $2\times5=10$. The $(1-\theta)$ exponent is $\sum(x-2)=22-2\times5=12$. So $L\propto\theta^{10}(1-\theta)^{12}$. This answers "write the likelihood".
- Step 2: the prior Beta(2,3) is $\propto\theta^1(1-\theta)^2$. Multiplying gives $\theta^{10+1}(1-\theta)^{12+2}=\theta^{11}(1-\theta)^{14}$, so $A=11$, $B=14$.
- Step 3: posterior Beta($A+1,B+1$) = Beta(12,15). This answers "derive the posterior".
- Step 4: $\hat\theta_{MAP}=\frac{11}{11+14}=\frac{11}{25}=0.44$. This answers "compute MAP".

**Recipe B: posterior with a function of $\theta$ (no conjugate form)**

*Example, exam says "derive the MAP for $\theta$" (apr24-2d).* The posterior is $\frac{\lambda}{2}e^{-\lambda x/2}$, where $\lambda=\frac1{1+e^{-\theta}}$ is the logistic sigmoid of $\theta$.
1. Take the log of the posterior, since $\ln$ is increasing and turns the product into a sum: $\ln p=\ln\lambda-\frac{\lambda x}{2}+\text{const}$.
2. Differentiate with the chain rule, using $\lambda'=\lambda(1-\lambda)$ from the hint: $\lambda'\left(\frac1\lambda-\frac x2\right)=0$.
3. $\lambda'>0$ always, because the sigmoid is strictly increasing, so it cannot be zero. Therefore $\frac1\lambda=\frac x2$, i.e. $\lambda=\frac2x$.
4. Invert the sigmoid. $\frac1{1+e^{-\theta}}=\frac2x$ gives $e^{-\theta}=\frac x2-1$, so $\hat\theta=-\ln\left(\frac x2-1\right)=\ln\frac{2}{x-2}$. This needs $x>2$, so that $\lambda=2/x$ lies in $(0,1)$.

**Other posteriors you may meet**
- **Normalising constant.** If the posterior is written as $\frac{1}{g(x)}h(\theta,x)$ with a factor $g$ that does not contain $\theta$ (a number like $x+a$, a Gamma function, an integral over $\theta$), that factor only rescales the curve. For **MAP** drop it: it cannot move the peak. For **MMSE** you cannot drop it — the posterior must integrate to 1 before you average, so keep it and integrate.
- **Two-bump (mixture) posterior.** If $p(\theta\mid x)=w\,f_1(\theta)+(1-w)f_2(\theta)$ with two named bumps, then MMSE (the mean) is the weighted sum of the bumps' means: $w\,\mu_1+(1-w)\,\mu_2$. MAP is at the bump with the larger $w\times$(height).
- **$\theta$ takes only a few values** (e.g. $\theta\in\{+1,-1\}$). Then Bayes is a table, not an integral: $P(\theta\mid x)=\dfrac{p(x\mid\theta)P(\theta)}{\sum_{\theta'}p(x\mid\theta')P(\theta')}$. MAP = the value with the biggest entry; MMSE $=\sum_\theta \theta\,P(\theta\mid x)$. (For $\pm1$ with probabilities $q$ and $1-q$: MMSE $=q-(1-q)$.)
- **MSE with a threshold.** When the question compares two values (e.g. "decide $\pm1$ from $y$"), the estimate is the posterior mean rounded to the nearest allowed value; the cut is where the two posterior probabilities are equal.

**MC bullets (the reason is given where it is not obvious)**
- "MMSE is the mean of the posterior": TRUE. "MMSE is the maximum of the posterior": FALSE. The maximum is MAP.
- "MAP always equals the posterior mean" (jun26-2a-type): FALSE. They are equal only for one symmetric bump, e.g. a Gaussian posterior.
- "MMSE and MAP always give different estimates" (apr25-2a, apr24-2b, jan22-2d): FALSE, for the same reason. They can be equal, and they are equal for one symmetric bump.
- "MAP depends on the likelihood and the prior and cannot be computed without a prior": TRUE.
- "Bayesian estimators do not use prior knowledge": FALSE. That is the point of Bayesian estimation.
- "The Bayes estimate minimises Bayes risk, the average cost": TRUE.

Answer letters: jun26-2a = c, apr25-2a = c, apr24-2b = a, jan22-2d = b, nov22-2c = b.

## 2.3 · Least squares
Symbols: $x[n]$ = observed data sample number $n$; $s[n]$ = what the model predicts for sample $n$; $w[n]$ = noise; $\theta$ (theta) = unknown parameter(s) to estimate; $\hat\theta$ = the estimate; $J$ = cost, the total squared gap between data and model. Least squares (LS) = choose the unknowns that make $J$ smallest.

**Recipe A · straight line $y=ax+b$.** When the exam says "find the linear function having least squares error", the model is a straight line and you want its slope and intercept: use recipe A.
1. Compute $\bar x$ = mean of the x-values and $\bar y$ = mean of the y-values. The best line passes through $(\bar x,\bar y)$, which is why step 4 works.
2. Deviations $dx=x_n-\bar x$, $dy=y_n-\bar y$ for each point. Centering removes $b$ from the slope equation.
3. $a=\dfrac{\sum dx\,dy}{\sum dx^2}$ (minimising $J$ over $a$ gives this).
4. $b=\bar y-a\bar x$ (the line passes through $(\bar x,\bar y)$).

Worked (apr25-2b, points $(0,3),(2,4),(3,3)$):
- x-values 0, 2, 3: $\bar x=(0+2+3)/3=5/3$. y-values 3, 4, 3: $\bar y=10/3$.
- $dx$: $0-\tfrac53=-\tfrac53$; $2-\tfrac53=\tfrac13$; $3-\tfrac53=\tfrac43$.
- $dy$: $3-\tfrac{10}3=-\tfrac13$; $4-\tfrac{10}3=\tfrac23$; $3-\tfrac{10}3=-\tfrac13$.
- $\sum dx\,dy=\tfrac59+\tfrac29-\tfrac49=\tfrac39=\tfrac13$.
- $\sum dx^2=\tfrac{25}9+\tfrac19+\tfrac{16}9=\tfrac{42}9=\tfrac{14}3$.
- $a=\tfrac{1/3}{14/3}=\tfrac1{14}\approx0.071$.
- $b=\tfrac{10}3-\tfrac1{14}\cdot\tfrac53=\tfrac{140}{42}-\tfrac5{42}=\tfrac{135}{42}=\tfrac{45}{14}\approx3.21$.
- Final answer, the line the question asks for: $y=\tfrac1{14}x+\tfrac{45}{14}$.

**Recipe B · closed form, avoid nonlinear optimisation.** When the exam says "closed-form" or "avoid the nonlinear optimization", it wants an exact formula instead of an iteration: use recipe B. It works when $s=g(\theta)$ and $g$ is invertible (e.g. $\ln$, $e^{\cdot}$).
1. Write $\alpha=g(\theta)$. The cost in $\alpha$ is an ordinary sum of squares, so it is solvable directly (step 2). Why: a one-to-one relabelling keeps the best fit the same.
2. Solve LS for $\alpha$ with recipe C. For $x[n]=\alpha+w[n]$ the answer is $\hat\alpha=\bar x$.
3. Map back: $\hat\theta=g^{-1}(\hat\alpha)$ (the inverse undoes step 1).

Worked (q3-23-2d, $x[n]=\ln\theta+w[n]$, $n=0,\dots,N-1$): put $\alpha=\ln\theta$, so $x[n]=\alpha+w[n]$. LS gives $\hat\alpha=\bar x=\tfrac1N\sum_{n=0}^{N-1}x[n]$, the mean of all $N$ samples. Map back: $\hat\theta=e^{\hat\alpha}=\exp\big(\tfrac1N\sum x[n]\big)$. Answer: yes, closed form, the exp of the sample mean.

**Recipe C · signal linear in one amplitude $A$.** Use when $s[n]=A\,h[n]$ with $h[n]$ known (e.g. $h=e^{\phi n}$, or $h=1$ for a constant). Not for $\phi$ and $A$ both unknown -> D.
1. $J=\sum(x[n]-A\,h[n])^2$, the cost.
2. Set $dJ/dA=0$: $\sum h[n](x[n]-A\,h[n])=0$ (the best fit makes the gap orthogonal to $h$).
3. $\hat A=\dfrac{\sum x[n]h[n]}{\sum h[n]^2}$. Constant $h=1$ gives $\hat A=\bar x$.

Worked (jan20-4b, $s[n]=Ae^{\phi n}$, $\phi$ known): here $h[n]=e^{\phi n}$. Step 2: $\sum e^{\phi n}(x[n]-Ae^{\phi n})=0$. Step 3, using $e^{\phi n}e^{\phi n}=e^{2\phi n}$: $\hat A=\sum x[n]e^{\phi n}\big/\sum e^{2\phi n}$. This is the closed form in $\phi$ and the data that the question asks for.

**Recipe D · nonlinear model, $\phi$ and $A$ both unknown.** When the exam says "write the cost function", only D1 is asked. When it says "Gauss-Newton", "iterative" or "one iteration", do D2–D4.
1. Cost with $\theta=[\phi\ A]^T$ (a column of unknowns; $^T$ = transpose, just makes it a column): $J=\sum(x[n]-Ae^{\phi n})^2$.
2. Matrix $G$ holds the partial derivatives of $s$ per sample $n$: column 1 $\partial s/\partial\phi = nAe^{\phi n}$, column 2 $\partial s/\partial A=e^{\phi n}$. Why: Gauss-Newton replaces the curve by its straight-line approximation at the current guess.
3. Start from a guess $\theta_0$.
4. Iterate: $\theta_{k+1}=\theta_k+(G^TG)^{-1}G^T\big(x-s(\theta_k)\big)$, with $G$ and $s(\theta_k)$ evaluated at the current guess $\theta_k$ (index $k$ = iteration number). Why: solving the linear LS for the correction moves the guess toward the minimum; repeat until it stops changing.

**Facts and MC traps**
- The error $x-H\hat\theta$ is perpendicular to every column of $H$. FALSE: "error lies in the column space of $H$".
- WLS with $W=C_x^{-1}$ is the best linear unbiased estimator (BLUE): TRUE.
- Nonlinear: separating into linear + nonlinear LS, or transforming to a linear problem, can give a closed form: TRUE.
- Nonlinear: "only Gauss-Newton works, not Newton-Raphson" is FALSE; both work.
- Needs at least as many data as unknowns, not exactly as many (fewer data: $H^TH$ cannot be inverted).

## 2.4 · CRLB

**Words.** $\theta$ = the unknown number we want to estimate. $p(x;\theta)$ = probability density of the data $x$ when the true value is $\theta$ (the ";" means $\theta$ is fixed, not random). $N$ = number of samples. $\hat\theta$ = estimator, a formula on the data that gives a guess. $E$ = average over the random data. $\operatorname{Var}$ = spread of $\hat\theta$ over repeated experiments. $\ln$ = natural log. Unbiased = $E[\hat\theta]=\theta$ on average. MVUE = unbiased estimator with the smallest variance. MLE = maximum-likelihood estimator. CRLB = Cramér-Rao lower bound, the smallest variance an unbiased estimator can have. $\mathcal I(\theta)$ = Fisher information for all $N$ samples; $i(\theta)$ = for one sample.

**Facts and T/F traps.**
- $i(\theta)=-E[\frac{d^2}{d\theta^2}\ln p]\ge0$. It is non-negative because $\ln p$ peaks at the best $\theta$, so its average curvature is negative and its negative is positive. "Strictly negative" is FALSE.
- N i.i.d. samples: $\mathcal I=N\,i(\theta)$ is TRUE. Why: $\ln$ of a product of independent densities is a sum, and sums of second derivatives and averages add.
- Bound: $\operatorname{Var}(\hat\theta)\ge 1/\mathcal I$, never $\ge\mathcal I$ (swapped-formula trap). Why: more information means sharper data, so less variance: the bound is the reciprocal.
- "Always derivable" is FALSE: it needs Recipe D. The bound applies to unbiased estimators only.
- "Variance lower than CRLB means efficient" is FALSE. Unbiased estimators cannot go below the bound; efficient means exactly equal to it.

**Recipe A: pdf $p(x;\theta)$ is written out.** Use for "derive Fisher information" or "CRLB for the MLE" when a density is given. For "$x$ = signal + noise" use B.
1. Take $\ln p$. Why: the formula is written with the log-density.
2. Differentiate twice w.r.t. $\theta$. Why: the formula needs the curvature of $\ln p$.
3. Negate, then take $E$ over $x$. Why: averaging removes the random $x$, leaving a function of $\theta$.
4. $\mathcal I=N\,i$. Why: N independent samples.
5. Bound $=1/\mathcal I$. Why: Cramér-Rao inequality for unbiased estimators.

**Example (Nov 2019 3b).** One sample has $p=\frac{x}{\theta^2}e^{-x^2/2\theta^2}$, $x\ge0$. Question: "Find the CRLB for the MLE."
Step 1: $\ln p=\ln x-2\ln\theta-\frac{x^2}{2\theta^2}$. The log of a product is a sum, and $\ln e^{y}=y$.
Step 2: first derivative $-\frac{2}{\theta}+\frac{x^2}{\theta^3}$; second derivative $\frac{2}{\theta^2}-\frac{3x^2}{\theta^4}$ (since $\theta^{-3}$ differentiates to $-3\theta^{-4}$).
Step 3: negate: $-\frac{2}{\theta^2}+\frac{3x^2}{\theta^4}$. Take $E$: $E[x^2]=\int_0^\infty x^2\frac{x}{\theta^2}e^{-x^2/2\theta^2}dx=2\theta^2$ (substitute $u=x^2$). The $\theta$ terms are constants, so they stay: $-\frac{2}{\theta^2}+\frac{3\cdot2\theta^2}{\theta^4}=-\frac{2}{\theta^2}+\frac{6}{\theta^2}=\frac{4}{\theta^2}$. So $i=4/\theta^2$.
Step 4: N samples: $\mathcal I=N\cdot\frac{4}{\theta^2}=\frac{4N}{\theta^2}$.
Step 5: bound $=\frac{1}{\mathcal I}=\frac{\theta^2}{4N}$. This is the answer to "CRLB for the MLE".

**Recipe B: $x$ = signal($\theta$) + white Gaussian noise $w$ with variance $\sigma^2$.** Use when the model is written as a mean plus noise (Nov 2022 2e), not as a density.
1. Write each sample's mean $\mu_n(\theta)$ and its derivative $\mu_n'$. Why: the signal carries $\theta$.
2. $\mathcal I=\sum_n(\mu_n')^2/\sigma^2$. Why: for Gaussian noise, the expectation in A reduces to $\mu'^2/\sigma^2$, because the noise averages to zero ($E[x-\mu]=0$).
3. Simplify the sum with $\sin^2+\cos^2=1$.

**Example (Nov 2022 2e).** $\mathbf x=A[\cos\theta,\sin\theta]^T+\mathbf w$, so sample 1 has mean $\mu_1=A\cos\theta$ and sample 2 has $\mu_2=A\sin\theta$.
Step 1: $\mu_1'=-A\sin\theta$ (derivative of $\cos$ is $-\sin$) and $\mu_2'=A\cos\theta$.
Step 2: $\mathcal I=\frac{(-A\sin\theta)^2+(A\cos\theta)^2}{\sigma^2}$. Squaring removes the minus sign.
Step 3: $=\frac{A^2(\sin^2\theta+\cos^2\theta)}{\sigma^2}=\frac{A^2}{\sigma^2}$. This answers "derive $\mathcal I(\theta)$".

**Recipe C: MVUE given, find the pdf.** Use for "given the MVUE ... find $p(\mathbf x;\theta)$, use the MVUE condition". The data $x[n]$ are i.i.d. with noise variance $\sigma^2$.
1. Find $\sigma^2$ from the given variance. Why: the mean of N samples has variance $\sigma^2/N$. Example: $\operatorname{Var}(\hat\theta)=\frac{1}{N^2}\cdot N\sigma^2=\frac{\sigma^2}{N}$; matching $A^2/N$ gives $\sigma^2=A^2$.
2. $\mathcal I=1/\operatorname{Var}(\hat\theta)=N/A^2$. Why: an MVUE hits the bound.
3. MVUE condition: $\frac{\partial\ln p}{\partial\theta}=\mathcal I(\hat\theta-\theta)$. Why: this equality holds exactly when the estimator reaches the bound.
4. Substitute $N\hat\theta=\sum_n x[n]$: $\frac{N}{A^2}(\hat\theta-\theta)=\frac{1}{A^2}\sum_n(x[n]-\theta)$. Why: $N\theta=\sum_n\theta$, so $\theta$ moves inside the sum.
5. Integrate over $\theta$. The hint $\int(x+a)dx=\frac12(x+a)^2$ with $a=-x$ gives $\int(x-\theta)d\theta=-\frac12(x-\theta)^2$. So $\ln p=-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2+g(\mathbf x)$, where $g$ depends on the data only, not on $\theta$.
6. Exponentiate and fix the constant: $p=(2\pi A^2)^{-N/2}\exp\!\big(-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2\big)$. Why: $p$ must integrate to 1 over the data; each sample's Gaussian term integrates to $\sqrt{2\pi A^2}$, and the N independent samples give $(2\pi A^2)^{N/2}$.

**Recipe D: "check whether the CRLB can be derived".** Use when the density is nonzero only on a range that depends on $\theta$.
1. Find the support: the set of $x$ where $p>0$.
2. If the edges of the support move with $\theta$, the CRLB is NOT possible. Why: the proof differentiates an integral over a fixed range of $x$; moving edges break this (regularity violated).
3. Otherwise derive with A.

**Example (Jan 2022 2e).** $p=\frac{2}{\theta}x$ for $0\le x\le\theta$. If $\theta=2$, data lie in $[0,2]$; if $\theta=3$, in $[0,3]$. The range changes with $\theta$, so the answer is "not possible: the support depends on $\theta$."

**How the exam words pick the recipe.** "Derive $\mathcal I$" or "find the CRLB" with a density written out → recipe A. The same question but with a model "signal + noise" instead of a density → recipe B. "Given the MVUE, find the pdf" → recipe C. "Can the CRLB be derived? Justify." → recipe D. "Which statement is TRUE/FALSE" → the facts and traps list above.

**Example (Q1 2023 2a, "exactly one FALSE").** (a) $N$ i.i.d. gives $N\,i$: TRUE (sums add). (b) "Var $\ge\mathcal I$": FALSE, the bound is $1/\mathcal I$. (c) "strictly positive": doubtful, since $\mathcal I=0$ when $p$ does not depend on $\theta$. The key marks (b).

## 2.5 · MC words

Symbols: $\theta$ (theta) = the unknown parameter we want; $\hat\theta$ = its estimate computed from data $x$; $N$ = number of observations; $p(x;\theta)$ = probability density of the data for a given $\theta$; $\mathcal I(\theta)$ = Fisher information of all $N$ observations, $i(\theta)$ = for one observation; $E[\cdot]$ = average; Var = variance; CRLB = Cramér–Rao lower bound.

**Theory words the true/false options use**
- **Bayes' rule:** $P(A\mid B)=\dfrac{P(B\mid A)P(A)}{P(B)}$. Read: update the chance of $A$ after seeing $B$, by scaling with how likely $B$ is under $A$.
- **Law of total probability:** $P(B)=\sum_k P(B\mid A_k)P(A_k)$: split into all groups, weigh each group's chance of $B$ by the group's share, and add.
- **Union:** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ ("A or B", the overlap counted twice, so subtract it once). If $A$ and $B$ cannot happen together, $P(A\cup B)=P(A)+P(B)$.
- **CDF** $F(x)=P(X\le x)$: the accumulated probability up to $x$. For a continuous pdf, $F(x)=\int_{-\infty}^x p(u)\,du$, and $P(a<X\le b)=F(b)-F(a)$.
- **Relative frequency:** the fraction of trials landing in an event after many repetitions; it approaches the probability.

**Facts to check statements against**
- Unbiased: $E[\hat\theta]=\theta$ (the average estimate is right).
- Efficient: unbiased AND Var $=$ CRLB. Going below the bound is impossible, so "below the bound = efficient" is false.
- CRLB $=1/\mathcal I(\theta)$, NOT $\mathcal I$. $\mathcal I\ge 0$ (an average of a second derivative, so never negative). $N$ iid observations: $\mathcal I=N\,i(\theta)$, so CRLB $=1/(N i)$ falls as $1/N$. Exam wording trap (jan22-2a): an option saying the bound "decreases linearly with $N$" is marked TRUE — they mean "keeps decreasing as $N$ grows, like $1/N$". If instead an option claims the bound is *proportional* to $N$, that is FALSE.
- MLE = $\arg\max_\theta p(x;\theta)$, the value that makes the data most likely. Asymptotically unbiased: true. Always reaching the CRLB: false (only for large $N$). Computable in general models by maximising.
- Bayes: $\theta$ has a prior $p(\theta)$, so Bayes estimators use the prior ("do not use prior" is false). Squared error cost gives MMSE = posterior mean $E[\theta|x]$. Uniform cost gives MAP = posterior maximum. "MMSE is the posterior max" is false. "MMSE and MAP always differ" is false: they coincide for a symmetric bell posterior. Only for large $N$ does the data dominate the prior, so MAP approaches MLE. "Regardless of the prior" is false.

**How the exam words pick the recipe.** When the question is a statement with options (a)(b)(c) to judge, use recipe A. When it asks you to compute a formula or a number from a likelihood $p(x|\lambda)$ and a prior $p(\lambda)$, use recipe B.

**Recipe A: true/false statements**
1. Find the topic word (MLE, CRLB/Fisher, MMSE/MAP). Why: each option tests one fact of one topic.
2. Compare each option with the facts above and mark T/F. Why: distractors swap one word ($\ge\mathcal I$ vs $\ge 1/\mathcal I$, mean vs max, "always").
3. Read the phrasing: "Which is TRUE?" → pick the one true option. "Which is FALSE? (exactly one)" → pick the one false option, the others are true. "always / regardless / any" → look for a counterexample, usually false.

Example A1 (apr24-2a, CRLB): $N=10$ iid observations, each with $i(\theta)=2$. Then $\mathcal I=10\cdot 2=20$ (N iid observations add information), and the bound is $1/20=0.05$. Option "Var $\ge\mathcal I$" says Var $\ge 20$: false, since the bound is $0.05$.

Example A2 (apr25-2a, MMSE vs MAP): posterior is a bell centred at 1. Its mean is 1 (balance point) and its max is 1 (peak). They are equal, so "always different" is false (apr25 (c), apr24-2b (c)).

**Recipe B: MMSE and MAP from a likelihood and prior (jan19-2b)**
Given: $p(x|\lambda)=\lambda e^{-\lambda x}$ for $x\ge0$ (exponential model, $\lambda$ = rate, $x$ = observed value) and prior $p(\lambda)=\tfrac12$ on $[0,2]$.
1. Bayes' rule: $p(\lambda|x)=\dfrac{p(x|\lambda)\,p(\lambda)}{\int p(x|u)p(u)\,du}$. Why: posterior = likelihood times prior, divided by the total so it integrates to 1.
2. MMSE $=E[\lambda|x]=\int_0^2\lambda\,p(\lambda|x)\,d\lambda$. Why: squared cost gives the posterior mean. When the exam says "provide the formula, specifying each distribution", write steps 1–2 with $p(x|\lambda)$ and $p(\lambda)$ spelled out, and do not evaluate the integrals.
3. The $\tfrac12$ is the same top and bottom, so it cancels: posterior $\propto\lambda e^{-\lambda x}$ on $[0,2]$.
4. Numerator $\int_0^2\lambda^2e^{-\lambda x}d\lambda$, denominator $\int_0^2\lambda e^{-\lambda x}d\lambda$. Use the given integrals with $a=-x$, evaluate at 2 and subtract the value at 0 (a definite integral is $F(2)-F(0)$). When the exam says "solve the formula from b1", it wants these two integrals evaluated and the fraction simplified.
5. Result: $\hat\lambda_{MMSE}=\dfrac{2}{x}\cdot\dfrac{1-(1+2x+2x^2)e^{-2x}}{1-(1+2x)e^{-2x}}$.
6. MAP = $\arg\max_\lambda p(\lambda|x)$. When the exam says "find the MAP", do this step. The denominator of step 1 does not depend on $\lambda$, so drop it (a constant cannot move the peak). Take the log: $\ln\lambda-\lambda x$, derivative $1/\lambda-x=0$, so $\lambda=1/x$. The prior is zero above 2, so the peak cannot lie past 2 — cap the answer: $\hat\lambda_{MAP}=\min(1/x,\,2)$.

## Checks, sign rules & maths crib
- Probabilities lie in $[0,1]$; $\iint p=1$; a PSD never goes negative (a *correlogram estimate* may); $P_{FA}$ uses the $H_0$ curve.
- Dividing an inequality by a negative **flips** it.
- Roots of the AR/factorisation quadratics come in pairs $a$ and $1/a$: always keep $|a|\lt1$, $|b|\lt1$ (that is what "minimum phase" wants).
- $x[n]=i[n]-a_1x[n-1]-\dots$ with $r[1]>0$ gives a **negative** $a_1$; a minus sign in front of $\cos\theta$ gives a negative $a$.
- Round only at the very end.
- **Derivatives you need:** $\frac{d}{d\theta}\theta^n=n\theta^{n-1}$ (so $\frac{d}{d\theta}\frac1{\theta}=-\frac1{\theta^2}$ and $\frac{d}{d\theta}\frac1{\theta^2}=-\frac2{\theta^3}$); $\frac{d}{d\theta}\ln\theta=\frac1\theta$; $\frac{d}{d\theta}e^{k\theta}=ke^{k\theta}$; $\frac{d}{d\theta}\cos\theta=-\sin\theta$; $\frac{d}{d\theta}\sin\theta=\cos\theta$. A constant times $\theta$ differentiates to the constant; a term without $\theta$ differentiates to 0.
- **Quadratic formula:** $ax^2+bx+c=0$ has roots $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$. For $b^2-4ac>0$ there are two real roots; pick the one inside the allowed range (for filter/MAR coefficients that is $|x|<1$).
- **Log and exp rules:** $\ln(ab)=\ln a+\ln b$; $\ln\frac ab=\ln a-\ln b$; $\ln e^a=a$; $\ln a^b=b\ln a$; $e^ae^b=e^{a+b}$; $\frac{e^a}{e^b}=e^{a-b}$. Handy values: $\ln2=0.693$, $\ln3=1.099$, $\ln10=2.303$, so $\ln0.5=-0.693$, $\ln0.9=-0.105$, $\ln20=3.0$, $\ln0.1=-2.303$.
- **Geometric series:** $\sum_{n=0}^\infty q^n=\frac1{1-q}$ for $|q|<1$ (used for energy of decaying signals).
- **Gaussian tail:** for $x\sim N(0,1)$, $P(x>t)=Q(t)$; $Q(1.28)=0.10$, $Q(1.645)=0.05$, $Q(2.33)=0.01$, $Q(0)=0.5$. For $N(\mu,\sigma^2)$ standardise first: $Q\!\left(\frac{t-\mu}{\sigma}\right)$.


## 3.1 · Correlogram + pick the plot

**Symbols.** $r[k]$ = autocorrelation at lag $k$: how much the signal resembles itself $k$ steps later; $r[0]$ = its variance (no shift). $r[-k]=r[k]$ (symmetry). $\theta$ = frequency in radians, from $0$ (slowest) to $\pi$ (fastest alternation). $\hat P(\theta)$ = estimated power spectral density (power per frequency). $c=\cos\theta$ (shorthand). $i[n]$ = white noise input (zero mean, uncorrelated in time); its variance is $\sigma^2$ (written $\sigma_i^2$ in exams). $a_k$ = AR weights on past outputs, $b$ = MA weight, $p$ = AR order, $q$ = MA order, $N$ = data length.

**How the exam words pick the recipe.** When the question says "correlogram", "non-parametric", "using only the given lags" or "as a function of $\cos\theta$", it wants the PSD built from the $r[k]$ alone → recipe 1. When it names "AR(1)" → recipe 2; "AR(2)" or "Yule-Walker" → recipe 3. When it says "MA(1)", "MA($q$)" or "approximate as MA" → recipe 4. When it asks "which plot/figure/option matches" → recipe 5. When it asks for the "order $p$", about "residual" error or a model-selection "criterion" → recipe 6.

**1. Correlogram (uses only the given lags)**

1. Write the given lags. Lags not given, or "$r=0$ for $|k|>q$", are zero, so drop them. Why: the correlogram sums only the known lags.
2. Write $\hat P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$ and stop at the last nonzero lag. Why: the PSD is the Fourier transform of $r$; $r[k]$ and $r[-k]$ pair up into $2r[k]\cos k\theta$, while lag 0 has no partner, so it is not doubled.
3. For a function of $c$: $\cos2\theta=2c^2-1$, $\cos3\theta=4c^3-3c$ (multiple-angle identities), then collect powers of $c$.

Worked story (jun26-3c, "as function of $\cos\theta$"): $r[0]=3$, $r[1]=2$, $r[2]=1$, zero beyond lag 2. So we stop at lag 2: $\hat P=3+2\cdot2\cos\theta+2\cdot1\cos2\theta=3+4\cos\theta+2\cos2\theta$. Step 3: $2\cos2\theta=2(2c^2-1)=4c^2-2$, so $\hat P=3+4c+4c^2-2=4c^2+4c+1=(2c+1)^2$.

**2. AR(1)** (use when a model is named; not for a plain correlogram)

Model: $x[n]+a_1x[n-1]=i[n]$: today = $-a_1\times$ yesterday + new noise. Yule-Walker equations come from multiplying by $x[n-k]$ and taking expectations; $i[n]$ is uncorrelated with the past, so its term vanishes.

1. $a_1=-r[1]/r[0]$. Why: the lag-1 equation is $r[1]=-a_1r[0]$.
2. $\sigma^2=r[0]+a_1r[1]$. Why: the variance the past cannot predict is the noise variance.
3. $\hat P=\sigma^2/(1+2a_1\cos\theta+a_1^2)$. Why: this is $\sigma^2/|1+a_1e^{-j\theta}|^2$ expanded.

Worked story (apr25-3e, $r[0]=2$, $r[1]=-\tfrac14$): $a_1=-(-\tfrac14)/2=\tfrac18$. $\sigma^2=2+\tfrac18\cdot(-\tfrac14)=2-\tfrac1{32}=\tfrac{63}{32}$. Denominator: $1+\tfrac{2}{8}c+\tfrac1{64}=\tfrac{65+16c}{64}$, so $\hat P=\tfrac{63}{32}\cdot\tfrac{64}{65+16c}=\tfrac{126}{65+16c}$.

**3. AR(2)**

1. Yule-Walker in matrix form: $\begin{pmatrix}r[0]&r[1]\\r[1]&r[0]\end{pmatrix}\begin{pmatrix}a_1\\a_2\end{pmatrix}=-\begin{pmatrix}r[1]\\r[2]\end{pmatrix}$. Why: the lag-1 and lag-2 equations, with $r[-1]=r[1]$.
2. Solve it: $D=r[0]^2-r[1]^2$, $a_1=-r[1](r[0]-r[2])/D$, $a_2=(r[1]^2-r[0]r[2])/D$.
3. $\sigma^2=r[0]+a_1r[1]+a_2r[2]$ (same reason as AR(1)).
4. $\hat P=\sigma^2/(1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta)$. Why: expanding $|1+a_1e^{-j\theta}+a_2e^{-2j\theta}|^2$.

Worked story (jun26-3d, $r=3,2,1$): the equations are $3a_1+2a_2=-2$ and $2a_1+3a_2=-1$. $D=9-4=5$, $a_1=-2(3-1)/5=-\tfrac45$, $a_2=(4-3)/5=\tfrac15$. $\sigma^2=3+(-\tfrac45)(2)+\tfrac15(1)=\tfrac85$. Denominator in $c$: $1+\tfrac{16}{25}+\tfrac1{25}-\tfrac{48}{25}c+\tfrac25(2c^2-1)=\tfrac{4(5c^2-12c+8)}{25}$, so $\hat P=\tfrac{10}{5c^2-12c+8}$.

**4. MA(1)** (key fact: MA($q$) autocorrelation is zero beyond lag $q$, so the correlogram over lags $0..q$ is already the exact MA PSD)

Model: $x[n]=i[n]+b\,i[n-1]$. Let $\rho=r[1]/r[0]$.

1. Only if parameters are asked: $\rho=b/(1+b^2)$, solve the quadratic in $b$, keep the root with $|b|<1$ (the usual invertible choice).
2. $\sigma^2=r[0]/(1+b^2)$. Why: $r[0]=\sigma^2(1+b^2)$.
3. $\hat P=r[0]+2r[1]\cos\theta$. Why: step 1 of recipe 1 with lags $0..q$ only.

Worked story (jan20-3b, $r[0]=\tfrac1{21}$, $r[1]=\tfrac2{105}$): $\rho=\tfrac{2/105}{1/21}=\tfrac25$. Then $b/(1+b^2)=\tfrac25$ gives $2b^2-5b+2=0$, $b=\tfrac{5\pm3}{4}\in\{2,\tfrac12\}$. Keep $b=\tfrac12$ ($|b|<1$). $\sigma^2=\tfrac{1/21}{5/4}=\tfrac4{105}$. PSD $=\tfrac1{21}+\tfrac4{105}\cos\theta$, identical to the correlogram in 3(a): that answers "how does this relate?" (the given $r$ is exactly an MA(1) autocorrelation).

**5. Pick the plot** (curves: correlogram, AR, MA)

1. Compute each PSD at $\theta=0$ ($c=1$, all cosines $=1$) and at $\theta=\pi$ ($c=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Why: two endpoints separate the curves quickly; you do not need the whole shape.
2. Match these heights to the plot. The plot with the matching heights is the answer.

Apr25-3g: correlogram $1.125$ at $0$, $2.125$ at $\pi$; MA(1) $1.5$ and $2.5$; AR(1) $1.56$ and $2.57$. All three start at $1.1$–$1.6$ and end at $2.1$–$2.6$: key plot D.

Trap: the correlogram may dip below 0; a true PSD never does.

**6. AR order and model selection** (jun26-3e, theory)

- Residual variance $\sigma^2$ never rises as $p$ grows; it falls. The risk is overfitting: the model fits noise and shows spurious peaks.
- Criteria against this: $\text{AIC}=N\ln\hat\sigma^2+2p$. Why: the first term falls with a better fit, the $2p$ penalty grows with the number of parameters; pick the order that minimises the sum.
- Any spectrum, even one with deep nulls from an MA, is approximated by an AR model of high enough order (AR($\infty$) in theory).

## 3.2 · AR / MA from $r[k]$

**Symbols.** $x[n]$: the random signal at time $n$. $i[n]$: the innovation, a fresh, unpredictable white-noise input (zero mean, variance $\sigma_i^2$) that drives the signal. $r[k]$: autocorrelation at lag $k$ (how many steps apart the two samples are), $r[k]=E\{x[n]x[n-k]\}$, with $r[-k]=r[k]$. $\theta$: frequency angle ($\theta=0$ is the slowest, $\theta=\pi$ the fastest). $c=\cos\theta$. $P$: power spectral density (PSD), the power per frequency. $p$: AR order, $q$: MA order. $a_1,a_2$: AR coefficients. $b$: MA coefficient. $\alpha,\beta$: ARMA coefficients. $N$: data length.

**How to choose the recipe.** First look at what the question gives. It gives $r[k]$ numbers or a PSD formula → recipe A. It gives a model (a difference equation or a transfer function $H(z)$) → recipes B–E. It gives a plot to identify → recipe F. It asks a true/false or "what happens as $p$ grows" → recipe H. Then read the model itself: if the equation has only noise terms $i[n], i[n-1],\dots$ on the right, it is an MA and $q$ is the largest delay; if past values of $x$ appear on the right, it is an AR and $p$ is the largest $x$-delay; if both appear, it is an ARMA($p,q$).

**How the exam words pick the recipe.** When the question says "correlogram", "non-parametric" or "using only the given lags", it wants the PSD built from the $r[k]$ numbers alone → recipe A. When it says "model as AR(1)" → recipe B. When it says "AR(2)" or "Yule–Walker matrix" → recipe C. When it says "model as MA(1)/MA(2)" or "find $a,b$" → recipe D. When it gives a difference equation and asks "which kind of model" or "the autocorrelation of $x$" → recipe E. When it says "express as a function of cosines", rewrite every multiple angle with $\cos2\theta=2c^2-1$ and $\cos3\theta=4c^3-3c$, then collect powers of $c$. When it hints "the MA autocorrelation is finite", that means the lags beyond $q$ are zero, so stop writing terms at lag $q$.

**A. Correlogram (PSD from $r[k]$).**
1. Keep the lags up to the last one given, drop the rest. Why: the question says they are zero (or "use only these").
2. $P=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$. Why: $e^{jk\theta}+e^{-jk\theta}=2\cos k\theta$, and the lag $-k$ term equals the lag $+k$ term.
3. Write in $c$ with the formulas above.

Example jun26-3c: $r[0]=3$, $r[1]=2$, $r[2]=1$, zero beyond. Step 2: the lag-1 term is $2\cdot2\cos\theta=4\cos\theta$, the lag-2 term is $2\cdot1\cos2\theta=2\cos2\theta$, so $P=3+4\cos\theta+2\cos2\theta$. Step 3: $2\cos2\theta=2(2c^2-1)=4c^2-2$, so $P=3+4c+4c^2-2=4c^2+4c+1=(2c+1)^2$. This is the answer to 3c.

**B. AR(1).** Use for one coefficient.
1. $a_1=-\dfrac{r[1]}{r[0]}$. Why: multiply $x[n]+a_1x[n-1]=i[n]$ by $x[n-1]$ and take expectations; the right side is zero because $i[n]$ is new, so it is uncorrelated with the past.
2. $\sigma_i^2=r[0]+a_1r[1]$. Why: same equation times $x[n]$; the right side gives $\sigma_i^2$ because $i[n]$ is the new part of $x[n]$.
3. $P=\dfrac{\sigma_i^2}{1+a_1^2+2a_1c}$. Why: $|1+a_1e^{-j\theta}|^2=1+a_1^2+2a_1\cos\theta$.

Example apr25-3e: $r[0]=2$, $r[1]=-\frac14$. Step 1: $a_1=-\frac{-1/4}{2}=\frac18$. Step 2: $\sigma_i^2=2+\frac18\cdot(-\frac14)=2-\frac1{32}=\frac{63}{32}$. Step 3: $1+a_1^2=\frac{65}{64}$ and $2a_1=\frac14$, so $P=\dfrac{63/32}{65/64+c/4}$. Multiply top and bottom by 64: $P=\dfrac{126}{65+16c}$. This is the answer to 3e.

**C. AR(2).** Use for two coefficients, given $r[0],r[1],r[2]$.
1. Yule–Walker in matrix form: $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$. Why: multiply $x[n]+a_1x[n-1]+a_2x[n-2]=i[n]$ by $x[n-1]$ and by $x[n-2]$, take expectations; the right side is zero (new noise vs. past).
2. $D=r[0]^2-r[1]^2$ (determinant), $a_1=\dfrac{-r[1](r[0]-r[2])}{D}$, $a_2=\dfrac{r[1]^2-r[0]r[2]}{D}$. Why: Cramer's rule solves two equations in two unknowns.
3. $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$. Why: the same equation times $x[n]$, the right side gives $\sigma_i^2$.
4. $P=\dfrac{\sigma_i^2}{1+a_1^2+a_2^2+2(a_1+a_1a_2)c+2a_2(2c^2-1)}$. Why: $|1+a_1e^{-j\theta}+a_2e^{-2j\theta}|^2$ expanded, then $\cos2\theta=2c^2-1$.

Example jun26-3d: $r[0]=3$, $r[1]=2$, $r[2]=1$. Step 1: $D=9-4=5$. Step 2: $a_1=\dfrac{-2(3-1)}{5}=-\frac45$, $a_2=\dfrac{4-3}{5}=\frac15$. Check: $3(-\frac45)+2(\frac15)=-2=-r[1]$. Step 3: $\sigma_i^2=3+(-\frac45)(2)+\frac15(1)=3-\frac85+\frac15=\frac85$. Step 4: $a_1+a_1a_2=-\frac{24}{25}$, so the denominator is $\frac{42}{25}-\frac{48}{25}c+\frac25(2c^2-1)=\frac{20c^2-48c+32}{25}=\frac{4(5c^2-12c+8)}{25}$, and $P=\frac85\cdot\frac{25}{4(5c^2-12c+8)}=\dfrac{10}{5c^2-12c+8}$. This is the answer to 3d.

**D. MA(1) and MA(2) from $r$.** Use when asked to find $b$ (or $a,b$). Unknown: $b$, and $\sigma_i^2$ when not given.

MA(1): $x[n]=i[n]+b\,i[n-1]$. Why the formulas: $r[0]$ pairs each coefficient with itself, $r[1]$ pairs neighbours, so $r[0]=\sigma_i^2(1+b^2)$, $r[1]=\sigma_i^2b$.
1. $u=\dfrac{r[0]}{r[1]}$ (a helper, not the order). Why: dividing kills $\sigma_i^2$, leaving $u=\dfrac{1+b^2}{b}$.
2. $b^2-ub+1=0$, so $b=\dfrac{u\pm\sqrt{u^2-4}}{2}$.
3. Keep the root with $|b|<1$. Why: the two roots multiply to 1, so exactly one qualifies; that is the invertible model.
4. $\sigma_i^2=\dfrac{r[1]}{b}$.
5. $P=r[0]+2r[1]c$. Why: $\sigma_i^2(1+b^2+2bc)$ is the same thing. Use only lags 0 and 1 even if more are given, because the MA(1) model says the rest are zero.

Example apr25-3f: $r[0]=2$, $r[1]=-\frac14$ (ignore $r[2]=-\frac3{16}$). Step 1: $u=\dfrac{2}{-1/4}=-8$. Step 2: $b=\dfrac{-8\pm\sqrt{64-4}}{2}=-4\pm\sqrt{15}$, about $-0.127$ or $-7.87$. Step 3: keep $b\approx-0.13$. Step 4: $\sigma_i^2=\dfrac{-1/4}{-0.127}\approx1.97$. Step 5: $P=2-\frac12c$. Check: $1.97(1+0.016-0.254c)\approx2-0.5c$. This is the answer to 3f.

MA(2): $x[n]=i[n]+a\,i[n-1]+b\,i[n-2]$. Why: lag 2 has one pair ($1\cdot b$), lag 1 has two pairs ($1\cdot a$ and $a\cdot b$), so $r[2]=\sigma_i^2b$, $r[1]=\sigma_i^2a(1+b)$.
1. $b=\dfrac{r[2]}{\sigma_i^2}$.
2. $a=\dfrac{r[1]}{\sigma_i^2(1+b)}$.
3. $r[0]=\sigma_i^2(1+a^2+b^2)$ if $r[0]$ is not given. If the question says "unit variance noise" (or the key answers use $\sigma_i^2=1$), then $\sigma_i^2=1$ and $r[0]=1+a^2+b^2$ directly. If instead $r[0]$ is given, turn the formula around: $\sigma_i^2=r[0]/(1+a^2+b^2)$.

**E. Model type and $r[\tau]$ from a difference equation (ARMA).**
Model type: count which terms appear. Only $i$ with delays → MA(largest delay). $x$ on the right too → ARMA($p$,$q$) with $p$ the largest $x$-delay and $q$ the largest $i$-delay.

MA($q$) autocorrelation: $r[l]=\sigma_i^2\times$(sum of products of coefficients $l$ places apart), zero beyond $q$.

Example apr24-3c: $x[n]=i[n]-\frac12i[n-1]+\frac14i[n-2]-\frac12i[n-3]$ is MA(3) (largest delay 3). Coefficients $1,-\frac12,\frac14,-\frac12$; $\sigma_i^2$ not given, take 1 as the key does. $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$. $r[1]=1(-\frac12)+(-\frac12)(\frac14)+(\frac14)(-\frac12)=-\frac34$. $r[2]=1\cdot\frac14+(-\frac12)(-\frac12)=\frac12$. $r[3]=1(-\frac12)=-\frac12$, and $r=0$ for $|l|\ge4$.

ARMA(1,1): write $x[n]=i[n]+\beta\,i[n-1]-\alpha\,x[n-1]$ and read $\beta$ and $\alpha$ (the sign of $\alpha$ flips). Also $H(z)=\dfrac{1+\beta z^{-1}}{1+\alpha z^{-1}}$ reads off the same way. Then:
1. $P=\sigma_i^2\dfrac{1+\beta^2+2\beta c}{1+\alpha^2+2\alpha c}$. Why: $|1+\beta e^{-j\theta}|^2$ over $|1+\alpha e^{-j\theta}|^2$.
2. $d=\beta-\alpha$, $r[0]=\sigma_i^2\left(1+\dfrac{d^2}{1-\alpha^2}\right)$, $r[l]=\sigma_i^2(-\alpha)^{l-1}\left(d-\dfrac{\alpha d^2}{1-\alpha^2}\right)$ for $l\ge1$. Why: the MA weights of $x$ are $1$ then $(-\alpha)^{j-1}d$, and lag products are geometric sums.

**F. Plot matching.** Do not judge shapes. Compute the height at $\theta=0$ ($c=1$) and at $\theta=\pi$ ($c=-1$), then match.
- apr25: correlogram $1.125$ at 0, $2.125$ at $\pi$ (from $2-\frac12c-\frac38\cos2\theta$); AR(1) $\frac{126}{81}\approx1.56$ and $\frac{126}{49}\approx2.57$; MA(1) $1.5$ and $2.5$. Key: option (a) = Plot D.

**H. Theory and true/false.**
- Residual error variance never rises as $p$ grows (more parameters fit at least as well). Risk: overfitting, the model fits the noise and creates spurious peaks.
- Fix: AIC $=N\ln\hat\sigma^2+2p$ (MDL, FPE similar). First term = fit quality, $2p$ = penalty per parameter. Choose the order with the minimum: the error keeps falling slowly, the penalty grows linearly.
- Any spectrum, even one with deep MA nulls, is approximated by an AR model of high enough order (AR($\infty$) in theory).

## 3.3 · Periodogram, Bartlett, Welch, windows

Symbols: $N$ = number of samples in the data record. $P$ = true PSD value. $r[k]$ = autocorrelation at lag $k$ (similarity of the signal with itself $k$ samples later). $\hat r$ = estimate of $r$. $\theta$ = normalised angle frequency. $K$ = number of segments averaged. $M$ = window or segment length. $L$ = DFT length.

**Estimators: idea, bias, variance** (use this list to fill any table)
- **Periodogram**: $\frac1N|\text{DFT of data}|^2$, one segment of all $N$ samples. Variance $\approx P^2$, does not shrink with $N$, so not consistent. Asymptotically unbiased.
- **Correlogram**: DFT of $\hat r[k]$, lags up to $N-1$. Same bias and variance as the periodogram.
- **Bartlett**: $K$ **non-overlapping** segments of length $M=N/K$, periodograms averaged. Variance $\approx P^2/K$. Bias larger for shorter $M$ (resolution $\approx2\pi/M$).
- **Welch (WOSA)**: $K$ **overlapping, windowed** segments, averaged. Variance below the periodogram but above Bartlett: neighbouring segments share samples, so they are correlated and the $1/K$ gain is lost. Bias above the periodogram, below Bartlett (segments are longer).
- **Blackman–Tukey (BT)**: window $\hat r[k]$ with a short lag window $M<L$, then DFT. Consistent: variance $\to0$. Bias grows for shorter $M$.
- **Parametric (AR/MA/ARMA)**: $P(e^{j\theta})=\sigma^2|B|^2/|A|^2$. $\sigma^2$ = noise variance, $A$ and $B$ = model polynomials.

**Recipe A: Welch count and variance ratio** (jun26-3b: $N=1000$, $L=200$, 50% overlap). Use when the question gives $N$, $L$ and overlap and asks for $K$ or a variance ratio.
1. Overlap in samples = overlap% $\times L$, the samples two neighbours share. Story: 50% of 200 is 100 shared samples.
2. Step $D=L-\text{overlap}$, the distance between segment starts. $D=200-100=100$.
3. $K=\frac{N-L}{D}+1$. Segments start at 0, 100, 200, ... and the last must end by sample $N$. Story: after the first start, 800 samples remain, each step moves 100, so $800/100=8$ more starts. Total $K=8+1=9$. This answers "how many segments".
4. Variance ratio: $K$ independent periodograms, each with variance $P^2$, averaged give variance $P^2/K$ (an average of $K$ independent items has $1/K$ of the variance). Ratio $=1/K=1/9\approx0.11$. This answers the variance line.

**Recipe B: energy or power** (apr25-3a, q2-24-3a). Use when a signal $x(t)$ or $x[n]$ is given. Not for PSD estimators.
1. Does the signal die out (go to 0) or have finite length? Yes: **energy**, because the energy $E$ (total of $|x|^2$ over all time) is finite only if the signal fades. No (constant, sine, cos, $\cos t\,u(t)$ keep oscillating): **power**, because $E$ would be infinite, so use the average power $\bar P$ instead.
2. Energy $E=\sum|x[n]|^2$ (integral for $t$). Power $\bar P$ = average of $|x|^2$ over time.

Story (energy): $x[n]=e^{-n}$ for $n\ge0$ decays, so energy. $E=\sum_{n=0}^{\infty}e^{-2n}$. Each term is $q^n$ with $q=e^{-2}\approx0.135$, a geometric series worth $\frac1{1-q}=\frac1{0.865}\approx1.16$. Since $E$ is finite, $\bar P=0$ (finite energy spread over infinite time). Answers item 2 of apr25-3a.

**Recipe C: match a description to a method** (apr25-3c, apr24-3a, nov19-1c). Use when a description is given and you name the method(s). Several can fit; repeats allowed. Read the description and find its one deciding word:
- The record is cut into **non-overlapping** segments and their periodograms are averaged → **Bartlett**. The segments **overlap** → **Welch** (WOSA). The single word overlap / non-overlap decides between the two.
- The description says: DFT of the estimated autocorrelation, and a **window** of length $M<L$ is applied to that estimate → **Blackman–Tukey** (the applied window is what makes it not a plain correlogram).
- The description says: modulus squared of the DFT, divided by $N$ → **periodogram**. It says DFT of $\hat r$ and mentions no window → **correlogram**.
- The description gives a model with $|B|^2/|A|^2$ → **parametric** (AR/MA/ARMA).

Story (apr25-3c): row 1 says non-overlapping and averaging periodograms, so Bartlett. Row 5 has the same words but "overlapping", so Welch. The single word decides.

**Recipe D: which statement is TRUE** (apr25-3b, nov22-3a, jan20-1b, jan19-1c). Use for options a–d about bias, variance, Bartlett, Welch.
1. Pick the claim in each option and check it against the list above.
2. Reject an option if any part is false, even if the first part is true.
3. Some questions have several true options.

Story (nov22-3a): (a) Bartlett, variance $\propto1/K$ (true), bias increases (true): TRUE. (b) WOSA with $1/K$: false, overlap correlates segments. (c) bias decreases: false, shorter segments raise bias. Answer (a).

**Recipe E: windows and zero-padding** (nov22-3b, jan20-1c). Use for lobes, leakage, padding.
- Main-lobe width sets **resolution** (wide = worse). Side-lobe height sets **leakage** (high = worse). Rectangular window: narrowest main lobe, highest side lobes. Longer window: narrower lobe.
- Zero-padding $N$ samples to length $L$: the DFT samples the same curve at $L$ points, step $2\pi/L$. Denser dots, no better resolution.

Story (nov22-3b, option d): padding to $L$ samples samples at step $2\pi/L$, not $2\pi/N$, so false. Answer (b).

**Recipe F: AR order $p$** (jun26-3e). Use for AR model order and criteria.
1. The residual error (variance $\sigma^2$) always falls as $p$ grows, so it cannot choose $p$. Too high $p$ = **overfitting**: the model fits noise and creates spurious peaks.
2. Use AIC $=N\ln\hat\sigma^2+2p$ or FPE $=\frac{N+p}{N-p}\hat\sigma^2$. The first term is the error (falls with $p$), the $2p$ is a penalty (rises with $p$). Compute for each $p$ and take the minimum: beyond it the penalty grows faster than the error falls.
3. Any PSD is approximated by an AR model of **high enough order**.

**Traps (true/false)**
- False: longer data cuts leakage (it narrows lobes; leakage is set by side lobes). False: a window improves resolution (rectangular is best there). False: Bartlett zero-pads (it splits the record). False: a window changes the periodogram's variance (it changes bias).
- True: bias affects both deterministic and stochastic signals.

## 4.1 · Likelihood-ratio test

**Use this recipe when** the question gives the full pdf (a formula in $x$) of the observation under both hypotheses and asks for a decision rule, a cut, or $P_{FA}$, $P_D$. One sample or $N$ samples both work.

**Symbols in plain words**
- $x$: the number you measure. $x_n$: sample number $n$ (the $n$-th measurement), $n=0,\dots,N-1$. $N$: how many samples you have.
- $\mathcal H_0$: "nothing there" (null hypothesis). $\mathcal H_1$: "signal there" (alternative).
- $p(x\mid\mathcal H_i)$: the pdf (height of the curve) of $x$ if hypothesis $i$ is true.
- $L$: likelihood ratio = height of the $\mathcal H_1$ curve ÷ height of the $\mathcal H_0$ curve at your $x$.
- $\lambda$, $\eta$ or $\gamma$ (letters vary): the **bar**, a number given in the question. If an $L$-test says "threshold $\gamma=1$", that is the bar on $L$, not a cut in $x$.
- **cut** ($x_{th}$, $\gamma'$, $y_{th}$): the value of $x$ where $L$ equals the bar. Your decision flips at the cut.
- $P_{FA}$: probability of false alarm = $P(\text{decide }\mathcal H_1\mid \mathcal H_0\text{ true})$ = $\mathcal H_0$ area in the "decide $\mathcal H_1$" region.
- $P_D$: probability of detection = $\mathcal H_1$ area in the same region. $P_M=1-P_D$ (missed detection) = the rest of the $\mathcal H_1$ curve.
- $Q(t)$: area under the standard Gaussian (mean 0, std 1) to the right of $t$.

**Reading the exam arrows.** $\overset{\mathcal H_1}{\underset{\mathcal H_0}{\gtrless}}$: decide $\mathcal H_1$ when the quantity is bigger. $\underset{\mathcal H_1}{\overset{\mathcal H_0}{\gtrless}}$ (nov22 uses this): decide $\mathcal H_1$ when it is smaller. The side of the sign tells you the hypothesis.

**Recipe**
1. Write $L=\frac{(\mathcal H_1\text{ formula})}{(\mathcal H_0\text{ formula})}$ with the numbers in. For $N$ independent samples the joint pdf is the product of single-sample pdfs, so $L$ is the product of the $N$ single-sample ratios.
2. Simplify with legal algebra: $x^a/x^b=x^{a-b}$; $e^a/e^b=e^{a-b}$; $\prod_n e^{-|x_n|}=e^{-\sum_n|x_n|}$ (exponents add); $c\cdot c\cdots c=c^N$; equal factors top and bottom cancel.
3. Compare with the bar: $L\gt\lambda$. Take $\ln$ of both sides: legal because $\ln$ is increasing, so the direction ">" survives. Use $\ln e^a=a$, $\ln c^N=N\ln c$, $\ln\frac1a=-\ln a$.
4. Isolate $x$ (or $x^2$, or $\sum x_n^2$) by moving constants across. Multiplying or dividing by a **negative** number flips ">" to "<" (because the order of numbers reverses when you flip their sign).
5. Check the direction: put one $x$ on each side into the original $L$. If $L\gt$ bar there, that side is $\mathcal H_1$. This catches sign mistakes.
6. Probabilities: $P_{FA}$ = integral of the $\mathcal H_0$ pdf over the decide-$\mathcal H_1$ region; $P_D$ = same integral for $\mathcal H_1$. If the region is $|x|\gt\gamma$ it has two tails: multiply by 2 when the curves are symmetric, because each tail has the same area.

**Type 1 · two power-law pdfs, one sample, bar given (apr25 4a).** When the exam asks "for what value of $x$ should $\mathcal H_1$ be accepted?", it wants the cut on $x$: do steps 1–4 and read the final inequality.
- Here $p(x\mid\theta)=k_1\theta x^{k_2\theta-1}$, with $k_1=1$, $k_2=2$. $\theta$ is the unknown parameter; $\theta_0=3$ under $\mathcal H_0$ and $\theta_1=6$ under $\mathcal H_1$.
- Step 1: under $\mathcal H_0$, $1\cdot3\cdot x^{2\cdot3-1}=3x^5$. Under $\mathcal H_1$, $1\cdot6\cdot x^{2\cdot6-1}=6x^{11}$. So $L=\frac{6x^{11}}{3x^5}=2x^6$ ($x^{11}/x^5=x^6$).
- Step 3: bar $\lambda=0.2$, so $2x^6\gt0.2$.
- Step 4: divide by 2 (positive, no flip): $x^6\gt0.1$, so $x\gt0.1^{1/6}$. Since $\ln0.1=-2.303$, $\ln x\gt-2.303/6=-0.384$, $x\gt e^{-0.384}=0.68$.
- Answer: $\mathcal H_1$ is accepted for $0.68\lt x\lt1$.

**Type 2 · two one-sided pdfs (Gaussian vs exponential), bar $\gamma=1$ (apr24 4b, jan22 4b/4c).** When the exam says "for threshold $\gamma=1$ calculate $P_D$ and $P_{FA}$", the bar on $L$ is given and you must find the cut first and then the two tail areas: do steps 1–6. Here $y$ is the observation, $\mathcal H_0$: $\frac1{\sqrt{2\pi}}e^{-y^2/2}$, $\mathcal H_1$: $\frac14e^{-y/2}$, $y\gt0$.
- Step 1: $L=\frac{\frac14e^{-y/2}}{\frac1{\sqrt{2\pi}}e^{-y^2/2}}=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}$. The constant is $2.507/4=0.627$.
- Step 3: $L\gt1$. Take $\ln$: $\ln0.627=-0.467$, so $-0.467+\frac{y^2}2-\frac y2\gt0$.
- Step 4: multiply by 2 (positive): $y^2-y-0.934\gt0$. The cut solves $y^2-y-0.934=0$: $y=\frac{1\pm\sqrt{1+3.738}}2=\frac{1\pm2.177}2$. The positive root is $y_{th}=1.59$.
- Step 5: at $y=0$, $L=0.627\lt1$ → $\mathcal H_0$. At $y=3$, $L=0.627e^{4.5-1.5}=0.627\cdot20.1=12.6\gt1$ → $\mathcal H_1$. So decide $\mathcal H_1$ for $y\gt1.59$.
- Step 6: $P_{FA}=\int_{1.59}^\infty\frac1{\sqrt{2\pi}}e^{-y^2/2}dy=Q(1.59)=0.0559\approx0.056$ (read from the table). $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac14\cdot2e^{-0.795}=\frac12\cdot0.452=0.226\approx0.23$. $P_M=1-0.23=0.77$.

**Type 3 · Rayleigh pdfs with two scales (jun26 4b, q1-23 4c/4d).** Pdf $\frac{x}{\sigma^2}e^{-x^2/2\sigma^2}$, where $\sigma$ is the scale. Read $\sigma^2$ from the exponent: $e^{-x^2/8}$ means $2\sigma^2=8$, so $\sigma^2=4$.
- Worked numbers (q1-23): $\mathcal H_0$: $xe^{-x^2/2}$, so $\sigma_0^2=1$. $\mathcal H_1$: $\frac x4e^{-x^2/8}$, so $\sigma_1^2=4$. Bar $\lambda=1$.
- Step 1: $L=\frac{\frac x4e^{-x^2/8}}{xe^{-x^2/2}}$. The $x$ top and bottom cancel (equal factors). The exponents subtract: $-\frac{x^2}8+\frac{x^2}2=\frac{3x^2}8$. So $L=\frac14e^{3x^2/8}$.
- Step 3: $L\gt1$; $\ln$: $\ln\frac14+\frac{3x^2}8\gt0$, so $\frac{3x^2}8\gt\ln4=1.386$.
- Step 4: $x^2\gt\frac83\cdot1.386=3.70$, so $x\gt\lambda'=1.92$.
- Step 6: $P_{FA}=P(x\gt1.92\mid\mathcal H_0)=e^{-1.92^2/2}=e^{-1.84}\approx0.16$ (Rayleigh: area right of $t$ is $e^{-t^2/2\sigma^2}$). $P_M=P(x\lt1.92\mid\mathcal H_1)=1-e^{-1.92^2/8}=1-e^{-0.46}\approx0.37$.

**Type 4 · Laplace pdfs, $N$ samples (nov22 4c/4d/4e).** Pdfs $\frac12e^{-|x|}$ and $e^{-2|x|}$. When the exam says "show that the test takes the form $\sum|x_n|\lessgtr\gamma'$ and find $\gamma'$", it wants the algebra of steps 1–4 and the value of $\gamma'$ at the end.
- Step 1: per sample, $\frac{e^{-2|x_n|}}{\frac12e^{-|x_n|}}=2e^{-|x_n|}$. Multiplying $N$ such factors gives $2^N e^{-\sum_n|x_n|}$.
- Step 3: $2^Ne^{-\sum|x_n|}\gt\lambda$; $\ln$: $N\ln2-\sum|x_n|\gt\ln\lambda$.
- Step 4: multiply by $-1$ → flip: $\sum_n|x_n|\lt N\ln2-\ln\lambda=\gamma'$. Decide $\mathcal H_1$ when the sum is smaller than $\gamma'$.

**Type 5 · symbolic scales and two-sided pdfs** (jun26 4b, jan22 4b/4c, pe21 4b).
- **Symbolic scales, no numbers.** Do the same steps with the letters in place: for the Rayleigh pair $\frac{x}{\sigma_0^2}e^{-x^2/2\sigma_0^2}$ vs $\frac{x}{\sigma_1^2}e^{-x^2/2\sigma_1^2}$, the $x$'s cancel and the exponents subtract, so $L=\frac{\sigma_0^2}{\sigma_1^2}e^{\frac{x^2}{2}\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)}$. Then $L>\eta$ gives, after $\ln$ and rearranging, $x^2>\dfrac{2\ln\left(\eta\,\sigma_1^2/\sigma_0^2\right)}{\frac1{\sigma_0^2}-\frac1{\sigma_1^2}}$, i.e. the cut is $x>\sqrt{\text{that}}$. Keep every letter until the last line.
- **Two Gaussians with different variances.** Same idea: $\ln$ of the ratio gives a quadratic in $x$; solve it with the quadratic formula of the crib and keep the root on the side the arrow says.
- **$|y|$ pdfs (the signal sits on the whole line).** If a pdf is written with $|y|$, solve the algebra for $y>0$ as usual, then **mirror** the cut: decide $\mathcal H_1$ for $|y|>y_{th}$ (or $|y|<y_{th}$, whichever the check of step 5 says). The two tails double the probability, as in the trap below.
- **$\ln$ of anything else** ($\ln4\lambda$, $\ln\frac{\sigma_0^2}{\sigma_1^2}$, $\ln0.9$): split it with the log rules of the crib ($\ln(ab)=\ln a+\ln b$, $\ln(a/b)=\ln a-\ln b$), then use the crib's values or the calculator.

**Other exam phrasings, and what they want**
- When the exam says "derive the log-likelihood ratio test", do steps 1–4 with $\ln$ and end by writing the final sum (or $x$) and its inequality.
- When it says "roughly plot the pdfs and mark the threshold" — "likelihoods" here means the two pdfs $p(x\mid\mathcal H_0)$ and $p(x\mid\mathcal H_1)$ — draw both curves and mark the cut where they cross ($L=1$).
- When it says "indicate $P_{FA}$ and $P_M$ in the plot", shade the $\mathcal H_0$ area that falls on the decide-$\mathcal H_1$ side, and the $\mathcal H_1$ area on the wrong side of the cut.
- When it says "for $P_{FA}=0.1$ calculate the threshold", invert step 6: find the cut from the $P_{FA}$ area first, then read the decision off it.
- When it says "show the LR can be written as $x\lessgtr\lambda'$", do steps 1–4 only and stop at the inequality; $\lambda'$ is the cut.

**Traps**
- $\ln$ never flips the direction; only multiplying or dividing by a negative does.
- A table of $P(0\le x\le k\sigma)$ (the area between 0 and $k$) equals $0.5-Q(k)$, and $P(x\le k)=1-Q(k)$; this is the "0.5 −" step when the exam gives such a table instead of $Q$.
- If the question gives no arrow and no "greater than" wording, say your assumption out loud: decide $\mathcal H_1$ where $L$ is bigger (the standard rule), then compute the tails for that side.
- $P_D\gt P_{FA}$ for any useful test; if you get $P_D\lt P_{FA}$, you have the decision direction backwards (step 5).
- $P_M=1-P_D$, not $1-P_{FA}$.
- Symmetric $|x|\gt\gamma$: two tails, so double each area.

## 4.2 · Bayesian detection

**Symbols.** $H_0$ = null hypothesis (nothing sent), $H_1$ = alternative (signal sent). $P_0,P_1$ = priors: the chance of $H_0$ and of $H_1$ before looking at the data. $C_{ij}$ = cost of deciding $i$ when $j$ is true: $C_{10}$ = false alarm cost, $C_{01}$ = miss cost, $C_{00},C_{11}$ = cost of a correct decision (usually 0). $p_0(x),p_1(x)$ = probability density of the data $x$ under $H_0$ and under $H_1$. $\lambda$ (lambda) = threshold on the likelihood ratio $p_1/p_0$. $y$ = scalar test statistic, $\gamma''$ = its threshold value. $P_D$ = probability of detection (decide $H_1$ when $H_1$ is true), $P_{FA}$ = probability of false alarm (decide $H_1$ when $H_0$ is true), $P_M$ = probability of miss $=1-P_D$. $P_e$ = total error probability.

**Recipe A · priors and costs given, densities given (Bayes likelihood-ratio test).**
Use this when the question gives $P_0,P_1$, costs, and the densities $p_0,p_1$. Use recipe B if it gives posteriors instead.

1. Compute $\lambda=\frac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$. Why: deciding $H_1$ has average cost $C_{10}P_0p_0+C_{11}P_1p_1$, deciding $H_0$ has $C_{00}P_0p_0+C_{01}P_1p_1$; picking the smaller one minimises the Bayes risk (average cost), and this is the threshold it gives.
2. If correct costs are 0 and both errors cost the same, $\lambda=P_0/P_1$. If the priors are also equal, $\lambda=1$, which is the maximum-likelihood rule.
3. Decide $H_1$ when $p_1(x)/p_0(x)>\lambda$. Why: step 1 already contains the priors and costs, so compare only the likelihood ratio.
4. Put $\lambda$ as $\eta$ into the threshold formula of the matching test (e.g. the Rayleigh threshold of 4.1). Why: that formula was derived for a likelihood-ratio threshold $\eta$.

*Example (jun26-4c).* Priors $P_0=0.9$, $P_1=0.1$; errors cost the same, correct costs 0. Step 2: $\lambda=P_0/P_1=0.9/0.1=9$. Step 4: with $\eta=9$ the Rayleigh threshold is $x>\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{9\sigma_1^2}{\sigma_0^2}}$. This expression is the answer to "when should the sensor accept $H_1$" (x = the measured value).

**Recipe B · posteriors given.**
Use this when the question gives $P(H_0|x)$, $P(H_1|x)$ or a ratio of them ("posterior is 5 times smaller").

1. Form $P(H_1|x)/P(H_0|x)$. Why: the posterior already contains priors and likelihoods, so no $p_1/p_0$ is needed.
2. Decide $H_1$ if this ratio $>\frac{C_{10}-C_{00}}{C_{01}-C_{11}}$. Why: same cost rule as recipe A, with the priors already absorbed.

*Example (apr25-4c).* $C_{01}=100C_{10}$, $C_{11}=C_{00}=0$, so the right side is $\frac{C_{10}}{100C_{10}}=0.01$. The $H_0$ posterior is 5 times smaller than the $H_1$ posterior, so $P(H_1|x)/P(H_0|x)=5$. Since $5>0.01$, decide $H_1$. The question asks "should the student fail": the student fails when $H_1$ is accepted, so **yes**.

**Recipe C · threshold where weighted densities meet ($\gamma''$).**
Use this when asked for the value $y$ where $p_1P_1=p_0P_0$.

*Example (nov22-4f):* $p_0=e^{-y}$, $p_1=2e^{-2y}$, $P_0=0.4$, $P_1=0.6$.

1. Write equality: $2e^{-2y}\cdot0.6=e^{-y}\cdot0.4$. Why: the question defines the threshold as this equality.
2. Divide both sides by $e^{-y}$ (allowed, it is positive). Since $e^{-2y}/e^{-y}=e^{-y}$, we get $1.2e^{-y}=0.4$.
3. So $e^{-y}=0.4/1.2=\frac13$.
4. Take logs: $y=\ln3\approx1.10$.
5. Direction: for small $y$, $e^{-y}>\frac13$, so $p_1P_1>p_0P_0$, which means $H_1$. Decide $H_1$ when $y<\ln3$.

**Recipe D · miss and false alarm from tails (exponential densities).**
Use this when the question asks $P_M$ and $P_{FA}$ for the test of recipe C. $P_{FA}$ integrates $H_0$'s density over the region where you decide $H_1$; $P_M$ integrates $H_1$'s density over the region where you decide $H_0$.

For a density $ce^{-cy}$ ($y\ge0$), integrating gives $P(y>a)=e^{-ca}$ and $P(y<a)=1-e^{-ca}$.

*Example (nov22-4g), continuing recipe C.*

1. $P_{FA}=P(y<\ln3;H_0)$, $H_0$ has $c=1$: $1-e^{-\ln3}=1-\frac13=\frac23$.
2. $P_M=P(y>\ln3;H_1)$, $H_1$ has $c=2$: $e^{-2\ln3}=(\frac13)^2=\frac19$.

**Recipe F · decoding the 2×2 table (rows = decision, columns = truth).**
- Decide $H_0$, truth $H_0$: true negative (correct).
- Decide $H_0$, truth $H_1$: miss, false negative, type II error.
- Decide $H_1$, truth $H_0$: false alarm, false positive, type I error.
- Decide $H_1$, truth $H_1$: detection, true positive.

**Multiple-choice rules (4.2).**
- Bayes **minimises** the Bayesian risk (average cost). "Maximised" is false.
- Equal costs for the two errors (1, 10, any equal non-zero value) with correct costs 0 minimise $P_e$. Why: then the cost ratio is 1 and $\lambda=P_0/P_1$ only depends on priors.
- Neyman–Pearson: fix $P_{FA}$, then **maximise** $P_D$ (priors not needed). "Minimise $P_D$" is false.
- Priors: higher $P_0$ raises $\lambda$, harder to decide $H_1$. Higher $P_1$ lowers $\lambda=P_0/P_1$, easier to decide $H_1$. "Higher $P_1$ raises the threshold" is false.

**How the exam words pick the recipe.** When the question asks "when should the sensor accept $H_1$" and gives priors and densities, use recipe A, steps 1–4. When it asks "should the student fail" and gives posteriors and costs, use recipe B. When it asks for "the value of $y$ where $p_1P_1=p_0P_0$" or "find $\gamma''$", use recipe C. When it asks for "the probability of miss and false alarm" with exponential densities, use recipe D on top of C. When it asks "which statement is TRUE/FALSE", check the multiple-choice rules above.

</div>
</div>
