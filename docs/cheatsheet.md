---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet</h1>

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This sheet fills both sides: Ctrl/Cmd + P → A4, margins minimal, untick "headers and footers", scale 100–115 %. Better still: copy it by hand — writing it is half the studying.</p>

<div class="cheat" markdown>
<div class="cheat-cols" markdown>

<div markdown>
## 1.1 · Bayes word problems
*"Machines make 40/35/25 %, defect rates 1/2/4 %" · "99 % accurate test, rare disease" · "which machine made it?"* — count people/items, don't start from formulas:

1. Pretend there are **1000** items (1 000 000 when a probability is tiny, e.g. 0.0005).
2. **Split by source**: count$_k$ = share$_k$ × 1000 → 400 / 350 / 250.
3. **Bad per source**: bad$_k$ = rate$_k$ × count$_k$ → 4 / 7 / 10. (They often give the *good* rate: bad $=1-$good.)
4. $P(\text{bad})$ = (bad$_A$+bad$_B$+bad$_C$)/1000 $=21/1000$.
5. $P(\text{source }k\mid\text{bad})$ = bad$_k$ / **pile of bad** $=10/21$ — divide by the pile (21), never by 1000.

**Medical test, same recipe.** 1 in 1000 ill, test 99 % right both ways, 100 000 people: 100 ill → 99 test $+$; 99 900 healthy → **999** test $+$ too. $P(\text{ill}\mid+)=99/1098\approx0.09$ — the healthy pile always dominates.

**Symbols:** $P(B)=\sum_i P(B\mid A_i)P(A_i)$ · $P(A_k\mid B)=\frac{P(B\mid A_k)P(A_k)}{P(B)}$ · "pass 85 %" = defect 0.15 · priors from counts: divide by the total.

**"Given it survived"** (memoryless): $P(T\ge t)=e^{-t/5}$, worked 2 years, breaks in year 3? $P(2\le T\lt 3\mid T\ge2)=\frac{e^{-2/5}-e^{-3/5}}{e^{-2/5}}=1-e^{-1/5}\approx 0.18$.

**Independent?** $P(A\mid B)=P(A)$ ⇔ $P(A\cap B)=P(A)P(B)$; "disjoint" ($P(A\cap B)=0$) is the **opposite**. $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
</div>

<div markdown>
## 1.2 · Joint PDF: $c$, marginal, conditional, independent
*"The joint PDF is $p(x,y)=c\,(\dots)$ on the region below"*

1. **Draw the region.** Corners and boundary lines — every limit below comes from this drawing.
2. **Find $c$**: $\iint p=1$. Inner integral along a slice (limits from the drawing), outer over all slice positions.
3. **Marginal** $p_Y(y)=\int p(x,y)\,dx$, $x$ across the slice at height $y$. Write the domain: "for $0\le y\le1$, 0 otherwise".
4. **Conditional** $p_{X\mid Y}(x\mid y)=\dfrac{p(x,y)}{p_Y(y)}$; domain = the slice.
5. **Independent** ⇔ $p(x,y)=p_X(x)p_Y(y)$ everywhere. Quick test: region is a **rectangle** *and* formula splits as (only $x$)·(only $y$). A triangle is never independent.

**Only integral rule needed.** $\int_a^b x^n dx=\big[\frac{x^{n+1}}{n+1}\big]_a^b$ = top − bottom; anything without the integration variable comes out in front: $\int_0^1 6x^2y\,dy=6x^2\cdot\frac12$.

**e.g.** $p=cx$ on $0\le y\le x\le1$: $\iint=c\int_0^1 x^2 dx=c/3$ → $c=3$; $p_X(x)=\int_0^x 3x\,dy=3x^2$; $p(y\mid x)=\frac{3x}{3x^2}=\frac1x$ = uniform on the slice.

Traps: forgetting "0 otherwise"; outer limits as a fixed number instead of the region.
</div>

<div markdown>
## 1.3 · WSS and ergodic
*"Is the process wide-sense stationary? Ergodic in the mean?"*

1. **Mean**: $E[X(t)]$ (average over the random part $U$, $A$, …). Depends on $t$ → **not WSS**, not ergodic. Stop.
2. **Autocorrelation** $E[X(t)X(t+\tau)]$: depends only on $\tau$ → **WSS**.
3. **Ergodic in the mean**: freeze the random part (one realisation = one row) and average over time. Every row gives the same number as step 1 → **ergodic**; if the answer still contains the draw (like $A$) → **not**.

**Known answers.** $\cos(t+U)$, $U$ uniform: WSS + ergodic · $A\cos t$, random $A$: $r$ depends on $A^2$ → not even WSS · i.i.d. dice: ergodic mean and variance.

**Autocorr facts.** $r[-l]=r[l]$ · $|r[l]|\le r[0]$ · $r[0]$ = average power · white noise: $r[0]=\sigma_i^2$, else 0 · $\cos\alpha\cos\beta=\frac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$ · $\hat r_{xy}[l]=\frac1N\sum_n x[n]y[n-l]$.
</div>

<div markdown>
## 1.4 · Spectral factorisation
*"Write $P=\dfrac{N}{A+B\cos\theta}$ as $\sigma_i^2 L(z)L(z^{-1})$"*

Match $C(1+az^{-1})(1+az)=C(1+a^2+2a\cos\theta)$ against $A+B\cos\theta$:

1. **Match**: $C(1+a^2)=A$, $2Ca=B$.
2. **Divide**: $\frac{1+a^2}{2a}=\frac AB$ → $B a^2-2A a+B=0$ → roots $a$ and $1/a$.
3. **Keep $|a|\lt1$** (if $B<0$, $a$ comes out negative — correct).
4. $C=\frac{B}{2a}$, then $\sigma_i^2=\frac NC$ (**not** $N$!).
5. $L(z)=\dfrac{1}{1+a z^{-1}}$ — one over the denominator's factor.

**Check** at $\theta=0$: must give $P(0)=\frac{N}{A+B}$. *e.g.* $N/(2+\cos\theta)$: $a^2-4a+1=0$ → $a=2-\sqrt3\approx0.268$, $C=\frac1{2a}$, $\sigma_i^2=N/C$.

Identities: $(1+az^{-1})(1+az)=(1+a^2)+2a\cos\theta$ · $\cos\theta=\frac{z+z^{-1}}2$ · a **minus** cosine gives a **negative** $a$.
</div>

<div markdown>
## 2.1 · Maximum likelihood (MLE)
*"Derive the ML estimator of $\theta$"* — write all four steps, each earns points:

1. **Likelihood**: $L(\theta)=\prod_{n=1}^N p(x_n\mid\theta)$ — multiply the PDFs.
2. **Log**: $\ln L(\theta)=\sum_n \ln p(x_n\mid\theta)$ — split into simple pieces.
3. **Differentiate** in $\theta$, set $\frac{d}{d\theta}\ln L=0$.
4. **Solve** for $\theta$ = $\hat\theta_{ML}$.

| log rules | derivatives in $\theta$ |
|---|---|
| $\ln(ab)=\ln a+\ln b$ | $\frac{d}{d\theta}\ln\theta=\frac1\theta$ |
| $\ln\frac ab=\ln a-\ln b$ | $\frac{d}{d\theta}\frac1\theta=-\frac1{\theta^2}$ |
| $\ln e^{u}=u$ | $\frac{d}{d\theta}(c\theta)=c$ |
| $\ln x^k=k\ln x$ | anything without $\theta$ → 0 |
| $\sum_n c=Nc$ | $\frac{d}{d\theta}\ln f=\frac{f'}{f}$ |

**Worked (exponential $\lambda e^{-\lambda x}$):** $\ln L=N\ln\lambda-\lambda\sum x$ → $\frac N\lambda-\sum x=0$ → $\hat\lambda=\frac{N}{\sum x}=\frac1{\bar x}$.

**Common answers.** Rayleigh $\frac x\theta e^{-x^2/2\theta}$ → $\hat\theta=\frac1{2N}\sum x^2$ (version $\frac x{\theta^2}e^{-x^2/2\theta^2}$ → square root of that) · Gamma($k,\theta$), $k$ known → $\hat\theta=\bar x/k$ · Sigmoid $\lambda(\theta)=\frac1{1+e^{-\theta}}$: solve for $\lambda$ first ($\hat\lambda$ = fraction of 1s), then $\hat\theta=\ln\frac{\hat\lambda}{1-\hat\lambda}$.

Traps: the $\frac1\theta$ in front gives $-N\ln\theta$ — half the answer · maximise over $\theta$, **not** over $x$ · "derive" ≠ write the final formula only.
</div>

<div markdown>
## 2.2 · MAP with a prior
*"Find the MAP estimate given the prior …"*

1. **Likelihood**: multiply PMFs/PDFs, keep only the $\theta$ parts → $\theta^{A}(1-\theta)^{B}$ or $\lambda^{\sum x}e^{-n\lambda}$.
2. **Times the prior** (only $\theta$ parts again). Same base → **add exponents**.
3. **Name it**: $\theta^{a-1}(1-\theta)^{b-1}$ = **Beta**$(a,b)$; $\lambda^{a-1}e^{-b\lambda}$ = **Gamma**$(a,b)$. Add 1 to the exponent to read $a$: exponent 11 → $a=12$!
4. **MAP = the top** (mode): Beta $\frac{a-1}{a+b-2}$ · Gamma $\frac{a-1}{b}$. Forget? $\ln$, differentiate, $=0$: $A\ln\theta+B\ln(1-\theta)$ → $\frac A\theta-\frac B{1-\theta}=0$ → $\theta=\frac{A}{A+B}$.

**Words.** posterior ∝ likelihood × prior · MMSE = posterior **mean**, MAP = **mode** (equal for symmetric unimodal) · median under absolute cost · $\int_0^\infty \theta^n e^{-s\theta}d\theta=\frac{n!}{s^{n+1}}$ · Beta$+\theta^A(1-\theta)^B$ → Beta$(\alpha+A,\beta+B)$.

**"Compare with the MLE"**: say **which way** the prior pulls and that it **fades** as $n$ grows.

Traps: exponent 11 → Beta **12** · Gamma top $=\frac{a-1}{b}$, **not** $(a-1)b$.
</div>

<div markdown>
## 2.3 · Least-squares line
*"Fit $y=ax+b$ in the least-squares sense"* (no noise PDF needed)

1. **Means**: $\bar x=\frac1N\sum x_n$, $\bar y=\frac1N\sum y_n$.
2. **Slope**: $a=\dfrac{\sum_n (x_n-\bar x)(y_n-\bar y)}{\sum_n (x_n-\bar x)^2}$.
3. **Intercept**: $b=\bar y-a\bar x$ — the line always passes $(\bar x,\bar y)$.

Given sums instead of data: $(\sum x^2)a+(\sum x)b=\sum xy$ and $(\sum x)a+Nb=\sum y$.

**General LS** ($K$ unknowns, $s=H\theta$): $\hat\theta=(H^TH)^{-1}H^Tx$; need $N\ge K$; error $x-H\hat\theta$ ⊥ columns of $H$. Nonlinear: transform ($\alpha=\ln\theta$ → $\hat\theta=e^{\bar x}$), else Gauss–Newton.
</div>

</div>
</div>

<div class="pagebreak"></div>

<div class="cheat" markdown>
<div class="cheat-cols" markdown>

<div markdown>
## 3.1 · Correlogram + pick the plot
*"Express the PSD estimate as a function of cosines" · "which plot is correct?"*

1. $\hat P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$ — one term per given lag, **$r[0]$ NOT doubled**.
2. Plug the numbers in. That is the "function of cosines" answer.
3. **Pick the plot** by its end values: $\theta=0$, all $\cos=1$ → $P(0)=r_0+2r_1+2r_2$; $\theta=\pi$, $\cos\pi=-1$, $\cos2\pi=+1$ → $P(\pi)=r_0-2r_1+2r_2$. Match **both** — curves agreeing at 0 often differ at $\pi$.

$\hat P$ may go **below 0** (only an estimate); a true PSD never can.
</div>

<div markdown>
## 3.2 · AR / MA from $r[k]$
Sign convention: $x[n]=i[n]-a_1x[n-1]-\dots$ (**minus** on the $a$'s); $P=\sigma_i^2\frac{|B|^2}{|A|^2}$.

**AR(1):** $a_1=-\frac{r[1]}{r[0]}$, $\ \sigma_i^2=r[0]+a_1r[1]$, $\ P=\dfrac{\sigma_i^2}{1+a_1^2+2a_1\cos\theta}$.

**AR(2)** (Yule–Walker):
1. "State the YW equations in matrix form" = $\begin{bmatrix}r[0]&r[1]\\ r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\ a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\ r[2]\end{bmatrix}$.
2. Solve with $D=r[0]^2-r[1]^2$: $a_1=\frac{-r[1](r[0]-r[2])}{D}$, $a_2=\frac{r[1]^2-r[0]r[2]}{D}$.
3. $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$.
4. $P=\frac{\sigma_i^2}{|A|^2}$, $\ |A|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos2\theta$.

**MA(1)** — the model gives $r[0]=\sigma_i^2(1+b_1^2)$, $r[1]=\sigma_i^2b_1$:
1. Divide: $b_1^2-\frac{r[0]}{r[1]}b_1+1=0$ → roots $b$ and $1/b$ → **keep $|b_1|\lt1$**.
2. $\sigma_i^2=r[1]/b_1$.
3. $P_{MA}=r[0]+2r[1]\cos\theta$ — the correlogram cut after lag 1; you don't need $b_1$ for it.

**Signatures (theory).** MA($q$): $r[l]=0$ for $|l|>q$ · AR(1): $r[l]=\frac{\sigma_i^2}{1-a^2}(-a)^{|l|}$ · ARMA: $r$ decays, never hits 0 · any PSD ≈ AR of high order · $|1+ce^{-j\theta}|^2=1+c^2+2c\cos\theta$ · $\cos2\theta=2\cos^2\theta-1$.
</div>

<div markdown>
## 3.3 · Periodogram, Bartlett, Welch, windows
From $N$ samples estimate the PSD — **match the method:**

| method | what you do | the catch |
|---|---|---|
| periodogram | $\frac1N\lvert\text{DFT}\rvert^2$ | noisy; more data ≠ calmer (not consistent) |
| correlogram | DFT of $\hat r[k]$ | same problems |
| Bartlett | $K$ **non-overlapping** pieces, average | variance ÷$K$, worse resolution |
| Welch | pieces **overlap** + windowed | more pieces; variance not quite ÷$K$ |
| Blackman–Tukey | window $\hat r[k]$ ($M\lt L$ lags) → DFT | consistent |
| parametric | fit AR/MA → formula | good only if the model fits |

**Welch segments.** $L$ = length, $D$ = step ($D=L$ none, $D=L/2$ at 50 %): $K=\frac{N-L}{D}+1$, variance ratio $\approx\frac1K$. *e.g.* $N=1000$, $L=200$, 50 %: $D=100$ → $K=9$ → $1/9$.

**Windows.** Main lobe = **resolution** ($\approx2\pi/N$); side lobes = **leakage**. Rectangular: narrowest lobe, worst leakage ($-13$ dB); triangular $-27$, Hann $-32$ (less leakage, wider lobe). Longer $N$ → better resolution, side lobes unchanged. **Zero padding** = more dots on the same curve, **no** extra resolution.

**Energy or power.** Finite $E=\sum_n|x[n]|^2$ → energy signal, $P=0$ ($e^{-n}$: $E=\frac1{1-e^{-2}}\approx1.16$). Infinite $E$, finite $P$ → power signal ($A\sin\omega t$ forever: $P=A^2/2$; $\cos t\,u(t)$: $P=1/4$).

**Order.** Raising $p$ always lowers residual error but overfits; AIC $=N\ln\hat\sigma^2+2p$, FPE $=\frac{N+p}{N-p}\hat\sigma^2$ → smallest wins.
</div>

<div markdown>
## 4.1 · Likelihood-ratio test (LRT)
*"Construct the LRT" · "show the test takes the form …" · "find the threshold" · "shade $P_{FA}$/$P_D$"*

Ratio of the two curve heights vs the **bar** $\lambda$ (exam writes $\eta$): $\ \dfrac{p(x\mid\mathcal H_1)}{p(x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda$. Bigger ratio → say $\mathcal H_1$. The number they **give** = the bar; solving $L=\lambda$ for $x$ gives the **cut** $\gamma$ they **ask** for.

1. **Ratio**: write it, cancel what you can. $N$ independent samples → both PDFs are products → the ratio is a product.
2. **Log both sides** ($\ln$ keeps the direction): $\ln(ab)=\ln a+\ln b$, $\ln e^u=u$, $\ln x^k=k\ln x$. Constant$^N$ → $N\ln$ constant!
3. **Isolate the data term** ($x$, $\sum x_n$, $\sum x_n^2$, $\sum|x_n|$). Multiply/divide by a **negative** → **flip** $\gtrless$.
4. **Write the rule**: "decide $\mathcal H_1$ if $x>\gamma$" ($\gamma$ in terms of $\lambda$). Which way? Plug one value each side into the ratio: the side beating $\lambda$ is the $\mathcal H_1$ side. Ratio decreasing in $x$ → points **left** ($y<\gamma$).
5. **Errors** on the decide-$\mathcal H_1$ zone $X_1$: $P_{FA}=\int_{X_1}p(x\mid\mathcal H_0)$ (under the **$\mathcal H_0$** curve), $P_D=\int_{X_1}p(x\mid\mathcal H_1)$, $P_M=1-P_D$.

**Which statistic pops out.** Mean shift → $\bar x$ big · bigger variance → $\sum x^2$ big · narrower Laplace → $\sum|x_n|$ **small** · exponential with larger rate → $x$ **small**.

**Worked.** $\mathcal N(0,1)$ vs $\mathcal N(1,1)$: $e^{x-1/2}>\lambda$ → $x>\frac12+\ln\lambda=\gamma$; $P_{FA}=Q(\gamma)$, $P_D=Q(\gamma-1)$.

**Gaussian tail** $P(X>t)=Q\!\big(\frac{t-\mu}{\sigma}\big)$: $Q(0)=.5$, $Q(1)=.159$, $Q(2)=.023$, $Q(3)=.0013$; $Q^{-1}(.10)=1.28$, $Q^{-1}(.05)=1.645$, $Q^{-1}(.025)=1.96$, $Q^{-1}(.01)=2.33$. Given $P_{FA}=\alpha$: $\gamma=\mu_0+\sigma_0Q^{-1}(\alpha)$, then $P_D=Q\!\big(\frac{\gamma-\mu_1}{\sigma_1}\big)$.

**Integrals.** $\int_a^b\lambda e^{-\lambda x}dx=e^{-\lambda a}-e^{-\lambda b}$ · $\int ke^{-ay}dy=-\frac ka e^{-ay}$ (front $k$ kills the exponent's $a$: $\int 2e^{-2y}dy=-e^{-2y}$) · $[F]_a^b=$ top − bottom · $e^{-a\ln b}=1/b^a$ · $e^{-\infty}=0$.
</div>

<div markdown>
## 4.2 · Bayesian detection, ROC, matched filter
*"Priors and costs given, construct the test"* — same LRT, the bar comes from money: $\lambda=\dfrac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$, where $C_{ij}$ = cost of deciding $\mathcal H_i$ when $\mathcal H_j$ is true ($C_{10}$ = false alarm, $C_{01}$ = miss, $C_{00}=C_{11}=0$ nearly always).

1. Compute $\lambda$.
2. Run 4.1 with it: ratio → log → isolate data → rule "decide $\mathcal H_1$ if $\dots\gtrless\gamma$".
3. Given **posteriors**: decide $\mathcal H_1$ if $\frac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}>\frac{C_{10}-C_{00}}{C_{01}-C_{11}}$ (priors already inside).

**Specials.** 0/1 costs → $\lambda=P_0/P_1$ (min $P_e$) · 0/1 + equal priors → $\lambda=1$: pick the taller curve · $P_0$ up → $\lambda$ up → harder to say $\mathcal H_1$ · misses 100× worse → $\lambda=P_0/(100P_1)$.

**Neyman–Pearson** (other way to set the bar): fix $P_{FA}=\alpha$, maximise $P_D$ → same ratio, $\lambda$ tuned so $P_{FA}=\alpha$. **ROC** = $P_D$ vs $P_{FA}$, above the diagonal (swap hypotheses → below); $\lambda=1$ is where the two PDF curves cross.

**Matched filter** (known $s_n$ in white noise): decide $\mathcal H_1$ if $\sum_n x_ns_n\gtrless\sigma^2\ln\lambda+\frac12\sum_ns_n^2$; $h[n]=s[N-1-n]$; maximises SNR; correlated noise → prewhiten.

Traps: the $\lambda(\theta)=\frac1{1+e^{-\theta}}$ of 2.1/2.2 is a **different lambda** (a model parameter) · keep the $N$ in front of constants ($2^N\to N\ln2$).
</div>

<div markdown>
## Detection: the pair they love (Rayleigh)
*"Two Rayleigh PDFs, decide …"* — taller tail = bigger $x$ points to $\mathcal H_1$: decide $\mathcal H_1$ if $x>\gamma$.

$P_{FA}=e^{-\gamma^2/2\sigma_0^2}$ · $P_D=e^{-\gamma^2/2\sigma_1^2}=P_{FA}^{\sigma_0^2/\sigma_1^2}$ · threshold from the ratio: $\gamma=\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\!\Big(\eta\dfrac{\sigma_1^2}{\sigma_0^2}\Big)}$ with $\eta$ = the bar ($P_0/P_1$ at 0/1 costs).
</div>

<div markdown>
## 2.4 · CRLB (when they ask for the bound)
*"Compute the Cramér–Rao lower bound" · "is the estimator efficient?"*

1. **Log of one sample**: $\ln p(x\mid\theta)$.
2. **Fisher information**: $i(\theta)=-E\big[\frac{\partial^2}{\partial\theta^2}\ln p\big]$ (also $=E\big[(\frac{\partial}{\partial\theta}\ln p)^2\big]$); $N$ independent samples → $\mathcal I=N\,i(\theta)$.
3. **CRLB** $=\dfrac{1}{N\,i(\theta)}$: every unbiased estimator has $\text{Var}\ge$ this.

First check: the range of $x$ must **not** depend on $\theta$ — if it does, "the bound does not apply". **Efficient** = unbiased *and* variance equals the bound. The MLE is **asymptotically** unbiased and efficient, $\hat\theta\approx\mathcal N(\theta,1/\mathcal I)$ — asymptotically, not always. Invariance: $\widehat{g(\theta)}=g(\hat\theta)$. Rayleigh: $E[x^2]=2\sigma^2$.
</div>

<div markdown>
## Theory MC: one line each
They swap **one word** ("maximised" ↔ "minimised", "always" ↔ "asymptotically") — read the verb and the direction.

- unbiased $E[\hat\theta]=\theta$ · consistent: $\hat\theta\to\theta$ as $N\to\infty$ · efficient: variance **equals** the CRLB.
- Fisher information $\ge0$; $N$ samples → $N\,i(\theta)$; bound is $\frac1{\mathcal I}$ (one over, not $\ge\mathcal I$).
- MMSE = posterior **mean**, MAP = **mode**; equal for a symmetric one-peaked posterior — not "always different".
- Bayes minimises the expected cost (Bayes risk); NP fixes $P_{FA}$ and maximises $P_D$; the LRT is both.
- $r[0]\ge|r[l]|$, PSD $\ge0$ (but the *estimated* correlogram may go negative); $r[0]$ = average power.
- Periodogram: **not consistent** (variance → $P^2$, not 0); Bartlett: variance ÷$K$, resolution $2\pi/M$; BT: consistent; more data never calms the raw periodogram.
- Zero padding never improves resolution; rectangular window: best resolution, most leakage; wider main lobe = worse resolution.
- Spectral factorisation needs $L$ causal, stable, **minimum phase**, $l[0]=1$ — the $|a|\lt1$ choice.
</div>

<div markdown>
## Checks & sign rules (use everywhere)
- **Ends**: $\theta=0,\pi$ (all $\cos=\pm1$); $y=0,\infty$; probabilities in $[0,1]$; PSD never negative; $\iint p=1$.
- **Signs**: dividing an inequality by a negative **flips** it · $x[n]=-a_1x[n-1]+\dots$ with $r[1]>0$ gives $a_1<0$ · a **minus** cosine gives a **negative** $a$.
- **Roots come in pairs** $a$ and $1/a$: keep $|a|\lt1$, $|b|\lt1$.
- **Round only at the very end** — intermediate rounding wrecks "final answer only" questions.
</div>

</div>
</div>
