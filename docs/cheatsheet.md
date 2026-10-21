---
hide:
  - navigation
  - toc
---

# A4 cheat sheet

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This page prints as a dense A4 (Ctrl/Cmd + P → A4, scale "fit", margins minimal; it fits on two sides). Better still: copy it by hand and add your own traps, writing it is half the studying.</p>

<div class="cheat" markdown>
<div class="cheat-cols" markdown>

<div markdown>
## 1 · Probability & signals

**Total prob.** $P(B)=\sum_iP(B\mid A_i)P(A_i)$ · **Bayes** $P(A_k\mid B)=\frac{P(B\mid A_k)P(A_k)}{P(B)}$
"pass 85 %" → defect 0.15 · priors from counts: divide by total.
**Independent:** $P(A\mid B)=P(A)$, $P(A\cap B)=P(A)P(B)$; disjoint ≠ independent; $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
</div>

<div markdown>
**RVs.** discrete = countable (counts); continuous = measurements, averages. $E[X]=\sum xp(x)$ (weighted avg, long-run mean). $\text{Var}=E[X^2]-\mu^2$. Cov: sign = direction, unbounded, unit-dependent; $\rho\in[-1,1]$. Binomial $\binom nkp^k(1-p)^{n-k}$. Exponential memoryless.
**Joint PDF:** draw region → limits. Normalise $\iint p=1$. Marginal $p_X=\int p\,dy$ (y over region at that x). Conditional $p_{X\mid Y}=p_{XY}/p_Y$ on the slice. Independent ⇔ factorises **and** rectangle. Diagonal cov → axis-aligned ellipses; tilted ⇒ cov ≠ 0.
</div>

<div markdown>
**WSS:** constant mean + $r(t_1,t_2)$ depends on lag only. **Ergodic:** time avg of 1 realisation = ensemble avg (needs stationarity). Something drawn once per realisation (amplitude $A$) ⇒ not ergodic in what depends on it. i.i.d. dice ⇒ ergodic mean & var. $\cos(t+U)$: WSS, ergodic; $A\cos t$: not WSS.
$\cos\alpha\cos\beta=\frac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$.
**Autocorr:** $r[-l]=r[l]$, $r[0]\ge|r[l]|$, PSD $\ge0$. White: $\sigma^2\delta[l]$. $\hat r_{xy}[l]=\frac1N\sum x[n]y[n-l]$.
</div>

<div markdown>
**Spectral factorisation.** $P_y=|H|^2P_x$; $P=\sigma_i^2L(z)L(z^{-1})$, $L$ causal, stable, **min phase**, $l[0]=1$.
$(1\mp az^{-1})(1\mp az)=(1+a^2)\mp2a\cos\theta$; $\cos\theta=\frac{z+z^{-1}}2$.
$\alpha\mp\beta\cos\theta$: $C(1+a^2)=\alpha$, $2Ca=\beta$ → roots $a,1/a$ → keep $|a|<1$ → $C=\beta/2a$. $\sigma_i^2=C_n/C_d$. Check at $\theta=0$.
</div>

<div markdown>
## 2 · Estimation

**MLE:** $\ln L=\sum\ln p(x_n;\theta)$ → $\partial_\theta=0$ → solve → check $\partial^2<0$. Asympt. unbiased, efficient, Gaussian $\mathcal N(\theta,I^{-1})$; invariance $\widehat{g(\theta)}=g(\hat\theta)$; maximise over **θ**, not x.
Rayleigh $\frac x\theta e^{-x^2/2\theta}$ → $\frac1{2N}\sum x^2$; $\frac{x}{\theta^2}e^{-x^2/2\theta^2}$ → $\sqrt{\cdot}$ of that; exp. $\lambda e^{-\lambda x}$ → $1/\bar x$; Gamma(k,θ) → $\bar x/k$.
Sigmoid $\lambda(\theta)$: $\lambda'=\lambda(1-\lambda)$; solve for λ, $\theta=\ln\frac{\lambda}{1-\lambda}$, need $0<\lambda<1$.
</div>

<div markdown>
**CRLB:** $I=-E[\partial^2\ln p]=E[(\partial\ln p)^2]>0$; $\text{Var}\ge1/I$; i.i.d. $I=N\,i(\theta)$; efficient = equals bound; equality ⇔ $\partial\ln p=I(\theta)(g(\mathbf x)-\theta)$. **Not valid if support depends on θ** (regularity). Rayleigh $E[x^2]=2\sigma^2$.
</div>

<div markdown>
**Bayes:** post ∝ lik × prior. **MMSE = mean**, MAP = mode (uniform cost), median (abs). MMSE=MAP for symmetric unimodal. $\int_0^\infty\theta^ne^{-s\theta}d\theta=\frac{n!}{s^{n+1}}$.
Beta(α,β)+$\theta^A(1-\theta)^B$ → Beta(α+A, β+B), mode $\frac{\alpha+A-1}{\alpha+\beta+A+B-2}$.
Gamma(α,β)+Poisson ($\lambda^Se^{-n\lambda}$) → Gamma(α+S, β+n), mode $\frac{\alpha+S-1}{\beta+n}$, MLE $S/n$.
Binary $X=\pm1$ + Gaussian: MMSE $\tanh(y/\sigma^2)$, MAP sign(y).
</div>

<div markdown>
**LS:** $\min\sum(x-s(\theta))^2$, no noise pdf. $\hat\theta=(H^TH)^{-1}H^Tx$; error ⟂ col(H); need $N\ge K$; BLUE: $W=C_x^{-1}$. Line: $(\sum x^2)a+(\sum x)b=\sum xy$, $(\sum x)a+nb=\sum y$. Nonlinear: transform ($\alpha=\ln\theta$ → $\hat\theta=e^{\bar x}$), else Gauss–Newton.
</div>

<div markdown>
## 3 · Spectral estimation

**Energy** $E<\infty$, $P=0$ (pulses). **Power** $0\lt P<\infty$, $E=\infty$ (periodic: $A^2/2$; $\cos t\,u(t)$: 1/4).
**Window:** main lobe → **resolution** (≈2π/N); side lobes → **leakage**. Rect: narrowest lobe, −13 dB; triang −27, Hann −32 (less leakage, worse resolution). Longer N → better resolution. **Zero padding**: samples FTD at $2\pi k/L$, no extra resolution. DFT = FTD at $2\pi k/N$.
</div>

<div markdown>
**Raw periodogram** $\frac1N|\text{DFT}|^2$ = **correlogram** (biased $\hat r$): asympt. unbiased (triangular smoothing), Var ≈ $P^2$ → not consistent.
**Bartlett:** K non-overlapping, Var ≈ $P^2/K$, bias↑ (resol. 2π/M). **Welch:** overlap + window, Var↓ but not 1/K, bias less than Bartlett; $K=\frac{N-L}{D}+1$. **BT:** window $\hat r$, Var ∝ 1/N → consistent.
</div>

<div markdown>
**Models** (minus sign on a's!): MA $x=i+\sum b_ki[n-k]$; AR $x=i-\sum a_kx[n-k]$. $P=\sigma^2|B|^2/|A|^2$. $|1+ce^{-j\theta}|^2=1+c^2+2c\cos\theta$; $|1+a_1e^{-j\theta}+a_2e^{-2j\theta}|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos2\theta$; $\cos2\theta=2\cos^2\theta-1$.
MA(q): $r[l]=\sigma^2\sum b_kb_{k-l}$, 0 for $|l|>q$. AR(1): $r[l]=\frac{\sigma^2}{1-a^2}(-a)^{|l|}$.
ARMA(1,1) $x=i+bi[n-1]-ax[n-1]$: $r_0=\sigma^2(1+b(b-a))-ar_1$, $r_1=\sigma^2b-ar_0$, $r_l=-ar_{l-1}$.
</div>

<div markdown>
**Chain.** Correlogram $r_0+2\sum r_k\cos k\theta$ (may go <0).
**YW:** Toeplitz$[r]\,[1,a_1..a_p]^T=[\sigma^2,0..0]^T$. AR(1): $a_1=-r_1/r_0$, $\sigma^2=r_0+a_1r_1$. AR(2): $r_0a_1+r_1a_2=-r_1$, $r_1a_1+r_0a_2=-r_2$, $\sigma^2=r_0+a_1r_1+a_2r_2$.
**MA(1):** $r_1b^2-r_0b+r_1=0$, keep $|b|<1$, $\sigma^2=r_1/b$, **PSD $=r_0+2r_1\cos\theta$**.
**Pick plot:** evaluate at θ = 0 and π; AR/MA never < 0.
**Order:** residual var ↓ always (overfit); AIC $=N\ln\hat\sigma^2+2P$, FPE $=\frac{N+P}{N-P}\hat\sigma^2$ → min. Any PSD ≈ AR of high order.
</div>

<div markdown>
## 4 · Detection

| decide ↓ / true → | $H_0$ | $H_1$ |
|---|---|---|
| $H_0$ | TN | miss (II) |
| $H_1$ | FA (I) | detect |

$P_{FA}=\int_{X_1}p(x|H_0)$, $P_D=\int_{X_1}p(x|H_1)$, $P_M=1-P_D$. **NP:** fix $P_{FA}$, max $P_D$ → LRT. ROC: $P_D$ vs $P_{FA}$, above diagonal; swaps → below.
</div>

<div markdown>
**LRT:** $\frac{p(x|H_1)}{p(x|H_0)}\gtrless\lambda$; i.i.d. → products; ln; isolate data term; **÷ negative flips H₀/H₁**. λ=1 → curves cross.
Mean shift → $\bar x$ big. Var ↑ → $\sum x^2$ big. Narrower Laplace → $\sum|x|$ small. Exp $\lambda_1>\lambda_0$ → x small. Rayleigh σ↑ → x big ($P_{FA}=e^{-\gamma^2/2\sigma_0^2}$, $P_D=P_{FA}^{\sigma_0^2/\sigma_1^2}$).
Gauss vs $\frac14e^{-|y|/2}$: $|y|>1.588$, $P_D=0.45$, $P_{FA}=2Q=0.11$.
</div>

<div markdown>
**Tails:** $P(X>t)=Q(\frac{t-\mu}{\sigma})$; $Q(0)=.5$, $Q(1)=.159$, $Q(2)=.023$, $Q(3)=.0013$; $Q=\frac12[1-\text{erf}(z/\sqrt2)]$. Exp: $\int_a^b\lambda e^{-\lambda x}=e^{-\lambda a}-e^{-\lambda b}$.
**Bayes:** $\lambda=\frac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$, $C_{ij}$ = decide i, truth j. 0/1 costs → $P_0/P_1$, min $P_e$; equal priors → ML. Posteriors: $H_1$ iff $C_{01}P(H_1|x)>C_{10}P(H_0|x)$. $P_0$↑ → λ↑.
**Matched filter:** $\sum x_ns_n\gtrless\sigma^2\ln\lambda+\frac12\sum s_n^2$; $h[n]=s[N-1-n]$; max SNR; correlated noise → prewhiten.
</div>

</div>
</div>
