---
hide:
  - toc
---

# Battle kit · every exam question, solved with your A4 sheet

<p class="lead">Every exam question from 2019 to 2026, one line each: <b>which box of the <a href="cheatsheet.md">A4 sheet</a> to open</b> → the box's steps with the exam's numbers → <b>the answer</b>. No theory. Print the sheet, sit down with a paper, and when a question blocks you, find it here.</p>

!!! recipe "How to fight with this"
    1. Read the question. Find its line below (they are in exam order).
    2. The bold **box X** is the box to open on your A4 sheet. Do what the box says — the line below shows the same steps with this exam's numbers.
    3. Stuck at a step? Go to the **Calculations** strip at the bottom of the sheet (integrals, $\ln$, sums, fractions).
    4. Check the **answer** in bold at the end of the line. Wrong? Re-read the box's trap.

    Questions the sheet deliberately does not carry (Bayes word problems, Wiener, Gauss–Newton, MVUE→pdf) say **not on the sheet** — those come with a one-liner or just the answer.

## June 2026 · resit (closest to Monday's format)

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.2 p · **not on the sheet** (Bayes word problem) | independent $\Leftrightarrow P(A\mid B)=P(A)$ → **(d)** |
| **1b** · 0.3 p · **not on the sheet** (Bayes) | $P(A\mid B)=\frac{P(A)P(B\mid A)}{P(B)}$, fill the tree, divide → **0.0345; 0.41** |
| **1c** · 0.5 p · **box 1A** | $p=6x^2y$ on $0\le x,y\le1$. Marginal: $p_X=\int_0^1 6x^2y\,dy=3x^2$ on $[0,1]$ (and $0$ otherwise), $p_Y=2y$. Independent? Region is a rectangle **and** $3x^2\cdot2y=6x^2y$ → **yes, independent** |
| **1d** · 0.25 p · **box 1B** | WSS = constant mean + autocorrelation depends only on $\tau$ → **(b)** |
| **1e** · 0.25 p · **box 1C** (last line) | innovation filter must be **minimum phase** (poles and zeros inside the unit circle) → **(a)** |
| **2a** · 0.5 p · **box 2D** | theory MC: match each sentence with the T/F table — "MAP needs a prior" is **T** → **(c)** |
| **2b** · 1 p · **box 2A** | Gamma pdf, $n$ patients: $\ln$ one sample $=(k-1)\ln x-\frac{x}\theta-k\ln\theta-\ln\Gamma(k)$; sum; differentiate: $-\frac{nk}\theta+\frac{\sum x_i}{\theta^2}=0$ (multiply by $\theta^2$ first) → $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}k$. Meaning: $k\hat\theta$ = observed mean time |
| **2c** · **box 2B** | NegBin, $k=2$, five patients $x=3,5,4,6,4$: each gives $\theta^2(1-\theta)^{x-2}$ → multiply: $\theta^{10}(1-\theta)^{12}$. Prior Beta(2,3) adds $\theta^1(1-\theta)^2$ → $\theta^{11}(1-\theta)^{14}$ → Beta(12,15) → MAP $=\frac{11}{25}=$ **0.44** |
| **2d** · **box 2B** | Poisson, six days $x=2,4,3,5,2,4$: $\lambda$'s add to $20$, six $e^{-\lambda}$ give $e^{-6\lambda}$. Prior Gamma(3,2) adds $\lambda^2e^{-2\lambda}$ → $\lambda^{22}e^{-8\lambda}$ → Gamma(23,8) → MAP $=\frac{22}8=$ **2.75**, MLE $=\frac{20}6=$ **3.33** (prior pulls towards its mean $\frac32$) |
| **3a** · 0.25 p · **box 3J** | "periodogram is consistent" is **F**: the variance does not go to 0 as $N\to\infty$ → **(b)** |
| **3b** · 0.5 p · **box 3G** | $N=1000$, $L=200$, 50 %: $D=100$, $K=\frac{1000-200}{100}+1=9$ segments, variance ratio $=\frac1K=$ **1/9** |
| **3c** · 0.5 p · **box 3A** | $r=3,2,1$: $3+2(2)\cos\theta+2(1)\cos2\theta=3+4\cos\theta+2\cos2\theta=(2\cos\theta+1)^2$ |
| **3d** · 1 p · **box 3C** | $r=3,2,1$: $D=r[0]^2-r[1]^2=5$; $a_1=-\frac45$, $a_2=\frac15$; $\sigma^2=r[0]+a_1r[1]+a_2r[2]=\frac85$; $P=\frac{10}{5\cos^2\theta-12\cos\theta+8}$ |
| **3e** · 0.75 p · **box 3J** (AR order) | bigger $p$ → error always down → **overfitting** (fake peaks). Fix: **AIC** $=N\ln\hat\sigma^2+2p$ (also FPE, MDL) → pick the smallest. Any PSD can be approximated by an AR model of **high enough order** |
| **4a** · 0.5 p · **box 4C** | theory MC, FALSE statement: check each against the table (higher $P(H_1)$ *lowers* $\eta$) → **(c)** |
| **4b** · 1 p · **box 4A** (Rayleigh) | the $x$ in front cancels: $L=\frac{\sigma_0^2}{\sigma_1^2}e^{\frac{x^2}2\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)}\gt\eta$ → accept $H_1$ if $x\gt\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\!\left(\eta\frac{\sigma_1^2}{\sigma_0^2}\right)}$. Bigger gap $\sigma_1-\sigma_0$ → less overlap → **better ROC** |
| **4c** · 1 p · **box 4B** | priors $0.9/0.1$, equal costs → $\eta=\frac{P(H_0)}{P(H_1)}=9$ → plug $\eta=9$ into the 4b threshold |
{: .battle }

## April 2025 · final

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.3 p · **not on the sheet** (Bayes) | CT scanners: tree + $\frac{P(A)P(B\mid A)}{P(B)}$ → **0.18; 0.22** |
| **1b** · 0.25 p | expected value: $E[X]=\sum x\,p(x)$ or $\int x\,p(x)dx$ → **(d)** |
| **1c** · 0.3 p · **box 1A** | $cx+1$ on the triangle $x,y\ge0$, $x+y\lt1$. **Limits in 4 moves:** order $dx\,dy$, freeze $y$: $x$ from $0$ to $1-y$, then $y$ from $0$ to $1$ → $\int_0^1\!\int_0^{1-y}(cx+1)\,dx\,dy=\frac c6+\frac12=1$ → $c=$ **3** |
| **1d** · 0.25 p · **box 1B** | dice / random phase → table row: WSS **yes**, ergodic **yes** → **(b)** |
| **1e** · 0.4 p · **box 1C** | $\frac1{61+60\cos\theta}$: $A=61$, $B=60$, $\sqrt{61^2-60^2}=11$, $r=\frac{61\pm11}{60}=1.2$ or $\frac56$ → keep $ · r → \lt1$: $a=\frac56$; $C=\frac{B}{2a}=36$; $\sigma_i^2=\frac1{C}=\frac1{36}$; $L=\frac{1}{1+\frac56z^{-1}}$ |
| **2a** · 0.5 p · **box 2D** | theory MC, FALSE statement → **(c)** |
| **2b** · 1 p · **box 2C** | $(0,3),(2,4),(3,3)$: $\bar x=\frac53$, $\bar y=\frac{10}3$; slope $a=\frac{1/3}{14/3}=\frac1{14}$; $b=\bar y-a\bar x=\frac{45}{14}$ → $y=\frac1{14}x+\frac{45}{14}$ (check: $x=\bar x$ gives $y=\bar y$) |
| **2c** · 1 p · **box 2A** (sigmoid) | $3\lambda e^{-4\lambda x/7}$: $\ln L$ → $\frac1\lambda-\frac{4x}7=0$ → $\hat\lambda=\frac7{4x}$; convert: $\hat\theta=-\ln\!\left(\frac{4x}7-1\right)$, valid for $x\gt\frac74$ |
| **2d** · 1 p · **box 2B** | posterior already given as $\theta^{a}(1-\theta)^{b}$ → MAP $=\frac{a}{a+b}$ |
| **3a** · 0.5 p · **box 3H** | $A\sin\omega t$ never dies → power $\frac{A^2}2$; $e^{-n}$ dies → energy $\sum e^{-2n}=\frac1{1-e^{-2}}=1.1565$ (Calculations: $\sum q^n=\frac1{1-q}$) |
| **3b** · 0.25 p · **box 3J** | theory MC, TRUE statement ("bias affects deterministic and stochastic signals") → **(a)** |
| **3c** · 0.5 p · **box 3I** | description table → periodogram / correlogram / Blackman–Tukey / Bartlett / Welch / parametric, as in the box |
| **3d** · 0.5 p · **box 3A** | $r[0]=2,\ r[\pm1]=-\frac14,\ r[\pm2]=-\frac3{16}$: $2+2(-\frac14)\cos\theta+2(-\frac3{16})\cos2\theta=2-\frac12\cos\theta-\frac38\cos2\theta$ |
| **3e** · 0.5 p · **box 3B** | same $r$: $a=-\frac{r[1]}{r[0]}=\frac18$; $\sigma^2=r[0]+ar[1]=2-\frac1{32}=\frac{63}{32}$; $P=\frac{\sigma^2}{1+a^2+2a\cos\theta}=\frac{126}{65+16\cos\theta}$ |
| **3f** · 0.5 p · **box 3D** | MA(1) PSD $=r[0]+2r[1]\cos\theta=2-\frac12\cos\theta$ (ignore $r[2]$) |
| **3g** · 0.25 p · **box 3F** | heights at $\theta=0$ and $\pi$: correlogram $1.13\to2.13$, MA $1.5\to2.5$, AR $1.56\to2.57$ → plot D → **(a)** |
| **4a** · 0.5 p · **box 4A** | $\frac{6x^{11}}{3x^5}=2x^6\gt0.2$ → $x^6\gt0.1$ → $x\gt0.1^{1/6}=$ **0.68** (Calculations: $x^k=a\Rightarrow x=a^{1/k}$) |
| **4b** · 0.5 p · **box 4C** | "which statement is FALSE": (a) Bayes minimises the risk **T**, (b) equal costs $\to$ minimises total error **T**, (c) Neyman–Pearson fixes $P_{FA}$ and maximises $P_D$ **T** → all true as printed, key says **none is false** (say so and justify) |
| **4c** · 1 p · **box 4B** | $C_{01}=100\,C_{10}$ → threshold $\frac{C_{10}-C_{00}}{C_{01}-C_{11}}=0.01$; posterior ratio $=5\gt0.01$ → accept $H_1$ → the student **fails: yes** |
{: .battle }

## April 2024 · final

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.25 p · **not on the sheet** (Bayes) | exponential lifetime + total probability → **(d) 0.18** |
| **1b** · 0.25 p · **not on the sheet** (Bayes) | TB test: $\frac{P(\text{inf})P(+\mid\text{inf})}{P(+)}$ → **0.047** |
| **1c** · 0.3 p · **box 1A** | $p=2$ on $0\le y\le x\le1$. Marginal: freeze $y$, $x$ runs $y\to1$: $p_Y=\int_y^1 2\,dx=2(1-y)$ for $0\le y\le1$. Conditional: $p(x\mid y)=\frac{2}{2(1-y)}=\frac1{1-y}$ for $y\le x\le1$ |
| **1d** · 0.3 p · **box 1B** | table fill: random phase $\cos(t+U)$ → **yes/yes**; random amplitude $A\cos t$ → **no/no** |
| **1e** · 0.4 p · **box 1C** | $\frac7{25-24\cos\theta}$: $\sqrt{25^2-24^2}=7$, $r=\frac{25\pm7}{-24}=-\frac43$ or $-\frac34$ → $a=-\frac34$; $C=\frac{-24}{-3/2}=16$; $\sigma_i^2=\frac7{16}$; $L=\frac1{1-\frac34z^{-1}}$ |
| **2a** · 0.5 p · **box 2D** | Fisher MC: check "Fisher info of $N$ iid samples $=N\,i(\theta)$" (T), "$\mathrm{Var}\ge\mathcal I$" (F: it is $\ge\frac1{\mathcal I}$) → **(c)** |
| **2b** · 0.5 p · **box 2D** | "MMSE = the **mean** of the posterior" is **T**; "MMSE = the maximum" is **F** (that is MAP) → **(a)** |
| **2c** · 1 p · **box 2A** | $\frac{x}{2\theta}e^{-x^2/2\theta}$: one sample $\ln x-\ln2-\ln\theta-\frac{x^2}{2\theta}$ → $\ln L=\sum\ln x_n-N\ln2-N\ln\theta-\frac{\sum x_n^2}{2\theta}$ → $-\frac N\theta+\frac{\sum x_n^2}{2\theta^2}=0$ (clear denominators) → $\hat\theta=\frac1{2N}\sum x_n^2$ |
| **2d** · 1.5 p · **box 2B** (sigmoid) | posterior $\frac\lambda2e^{-\lambda x/2}$: $\frac1\lambda-\frac x2=0$ → $\lambda=\frac2x$ → $\hat\theta=-\ln\!\left(\frac x2-1\right)$, $x\gt2$ |
| **3a** · 0.9 p · **box 3I** | description table → method names (periodogram, correlogram, Blackman–Tukey, Bartlett, Welch, parametric) |
| **3b** · 0.1 p · **box 3E** | only $i[n],i[n-1],i[n-2],i[n-3]$ on the right → **MA(3)** |
| **3c** · 0.5 p · **box 3E** | coefficients $1,-\frac12,\frac14,-\frac12$, $\sigma^2=1$: $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$; $r[1]=-\frac12-\frac18-\frac18=-\frac34$; $r[2]=\frac14+\frac14=\frac12$; $r[3]=-\frac12$ |
| **3d** · 0.4 p · **box 3A** | $\frac{25}{16}+2(-\frac34)\cos\theta+2(\frac12)\cos2\theta+2(-\frac12)\cos3\theta=\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$ |
| **3e** · 0.7 p · **box 3C** | $r=\frac{25}{16},-\frac34,\frac12$: $D=\frac{481}{256}$; $a_1=-\frac{r[1](r[0]-r[2])}{D}=\frac{204}{481}$; $a_2=\frac{r[1]^2-r[0]r[2]}{D}=-\frac{56}{481}$; $\sigma^2=r[0]+a_1r[1]+a_2r[2]\approx$ **1.19** |
| **3f** · 0.4 p · **box 3F** | heights at $\theta=0$ and $\pi$ → plot B → **(c)** |
| **4a** · 0.5 p · **box 4C** | theory MC, TRUE statement → **(b)** |
| **4b** · 1.5 p · **box 4A** | Gaussian $\frac1{\sqrt{2\pi}}e^{-y^2/2}$ vs exponential $\frac14e^{-y/2}$, $\gamma=1$: $L=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}\gt1$; $\ln$: $-0.467+\frac{y^2}2-\frac y2\gt0$ → $y^2-y-0.934\gt0$ (quadratic formula, Calculations) → root $1.59$ → accept $H_1$ if $y\gt$ **1.588**. $P_{FA}=Q(1.59)=$ **0.056**, $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac12e^{-0.795}=$ **0.23** |
{: .battle }

## November 2022 · final

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.25 p · **not on the sheet** (Bayes) | total probability over the cases → **(c) 0.63** |
| **1b** · 0.25 p · **box 1A** (PMF version) | joint **table**: marginal = sum each row. Common denominator 24: $\frac16+\frac14+\frac18=\frac{4+6+3}{24}=\frac{13}{24}$, row 2: $\frac{11}{24}$ → **(b)** |
| **1c** · 0.25 p · **box 1B** | $A\cos t$ with random $A$: table row "random amplitude" → not WSS, not ergodic → **(d)** per key |
| **1d** · 0.75 p · **box 1C** | $\frac{1}{5/3-\cos\theta}$: $A=\frac53$, $B=1$, $\sqrt{\frac{25}9-1}=\frac43$, $r=\frac53\pm\frac43=3$ or $\frac13$ → $a=\frac13$; $C=\frac{1}{2/3}=\frac32$; $\sigma_i^2=\frac1C=\frac23$; $L=\frac1{1-\frac13z^{-1}}$ |
| **2a** · 0.25 p · **box 2D** | Fisher MC → **(a)** |
| **2b** · 0.25 p · **box 2D** | "MLE maximises the likelihood over $\theta$" is T; "over $x$" is F → **(c)** |
| **2c** · 0.25 p · **box 2D** | "Bayes estimate minimises the Bayes risk" is **T** → **(b)** |
| **2d** · 0.5 p · **box 2D** (last line) | signal $A[\cos\theta,\sin\theta]$ + noise: MLE $\hat\theta=\arctan\frac{x_2}{x_1}$ |
| **2e** · 0.5 p · **box 2D** (Fisher line) | $\mathcal I=\frac1{\sigma^2}\sum\left(\frac{d\,\text{signal}}{d\theta}\right)^2=\frac{A^2}{\sigma^2}$ |
| **2f** · 0.5 p · **Calculations** | posterior $\theta e^{-(x+a)\theta}$ (normalised: $(x+a)^2\theta e^{-(x+a)\theta}$). MMSE = ratio of the $\int_0^\infty$ integrals: $\frac{2/(x+a)^3}{1/(x+a)^2}=\frac2{x+a}$ |
| **2g** · 0.5 p · **box 2B** | MAP = peak of $\theta e^{-(x+a)\theta}$: derivative gives $1-(x+a)\theta=0$ → $\frac1{x+a}$ |
| **3a** · 0.25 p · **box 3J** | "Bartlett: variance drops like $\frac1K$ but bias increases" is **T** → **(a)** |
| **3b** · 0.25 p · **box 3J** | "main-lobe width → resolution; side-lobe height → leakage" is **T** → **(b)** |
| **3c** · 0.15 p · **box 3E** | $x[k]=i[k]-i[k-1]+\frac34x[k-1]$: old $x$ **and** $i$'s on the right → **ARMA(1,1)** |
| **3d** · 0.35 p · **box 3E** (ARMA) | $\alpha=-\frac34$, $\beta=-1$, $\sigma^2=\frac78$: $P=\sigma^2\frac{1+\beta^2+2\beta\cos\theta}{1+\alpha^2+2\alpha\cos\theta}=\frac{28(1-\cos\theta)}{25-24\cos\theta}$ |
| **3e** · 0.5 p · **box 3E** (ARMA $r[k]$) | $r[0]=\sigma^2\frac{1+\beta^2-2\alpha\beta}{1-\alpha^2}=1$; $r[1]=-\alpha r[0]+\beta\sigma^2=-\frac18$; $r[k]=(-\alpha)^{k-1}r[1]=(-\frac18)(\frac34)^{k-1}$ → $r[0]=$ **1**, $r[l]=$ $-\frac18\left(\frac34\right)^{\lvert l\rvert-1}$ |
| **3f** · 0.75 p · **box 3B** | $r[0]=1$, $r[1]=-\frac18$: $a=\frac18$, $\sigma^2=1-\frac1{64}=\frac{63}{64}$ → $P=\frac{63}{65+16\cos\theta}$ |
| **3g** · 0.75 p · **box 3D** | $P=r[0]+2r[1]\cos\theta=1-\frac14\cos\theta$ |
| **4a** · 0.25 p · **box 4A** (error table) | decide $H_0$ & true $H_1$ = miss / type II … → **(a)** |
| **4b** · 0.25 p · **box 4C** | Neyman–Pearson: fix $P_{FA}$, **maximise** $P_D$ → **(b)** |
| **4c** · 0.5 p · **box 4A** | $\frac12e^{-\lvert x\rvert}$ vs $e^{-2\lvert x\rvert}$, $N$ samples: $L=2^Ne^{-\sum\lvert x_n\rvert}\gt\lambda$ → accept $H_1$ if $\sum\lvert x_n\rvert\lt N\ln2-\ln\lambda$ |
| **4d** · 0.25 p · **box 4A** (plot line) | draw both pdfs + a vertical line at the threshold; $H_1$ when $y\lt1$ → $P_{FA}=H_0$ area **left** of 1, $P_M=H_1$ area **right** of 1 |
| **4e** · 0.5 p · **box 4A** (probabilities) | $P_{FA}=0.1$: $1-e^{-t}=0.1$ → $t=-\ln0.9=$ **0.105**; then $P_D=1-e^{-2t}=$ **0.19** |
| **4f** · 0.5 p · **box 4B** ("where $p_1P_1=p_0P_0$") | $0.6\cdot2e^{-2y}=0.4e^{-y}$ → $e^{-y}=\frac13$ → $y=\ln3=$ **1.099**; decide $H_1$ for $y\lt\ln3$ |
| **4g** · 0.5 p · **box 4A** (tails) | $P_{FA}=1-e^{-\ln3}=\frac23$; $P_M=e^{-2\ln3}=\frac19$ |
{: .battle }

## January 2022 · resit

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.3 p · **not on the sheet** (Bayes) | employees + Bayes → **(c) 0.26** |
| **1b** · 0.3 p | "pictures as a process" MC: a random variable is a mapping from outcomes to numbers → **(b)** |
| **1c** · 0.3 p · **box 1B** | dice / ergodic → table row → **(b)** |
| **1d** · 0.3 p · **box 1C** | factorisation MC: minimum-phase filter, $ · r → \lt1$ root → **(c)** |
| **2a** · 0.3 p · **box 2D** | CRLB MC: "$\mathrm{Var}(\hat\theta)\ge\frac1{\mathcal I}$", "$\mathcal I\ge0$", "CRLB $\sim\frac1N$" → **(b)** |
| **2b** · 0.3 p · **box 2D** | "MLE of $\alpha=\psi(\theta)$ is $\hat\theta=\psi^{-1}(\hat\alpha)$" is **T** (invariance) → **(c)** |
| **2c** · 0.3 p · **box 2C** | least-squares MC → **(a)** |
| **2d** · 0.3 p · **box 2D** | MMSE MC ("MMSE = mean of the posterior" is T) → **(b)** |
| **2e** · 0.5 p · **box 2D** | "CRLB can always be derived" is **F**: not if the range of $x$ depends on $\theta$ → **no**, the support depends on $\theta$ |
| **2f** · 0.6 p · **not on the sheet** | posteriors of $\pm1$: complete the square in the exponent → both are **sigmoid** curves |
| **2g** · 0.6 p · **not on the sheet** | MMSE of that posterior: integral → $\tanh(y/\sigma^2)$ |
| **2h** · 0.6 p | MAP: the posterior is symmetric around $0$ → threshold $y_{th}=$ **0** |
| **3a** · 0.3 p · **not on the sheet** | match Fourier-transform plots (old format) → **(b) 1B 2D 3C 4A** |
| **3b** · 1 p · **box 3E** (read MA backwards) | $x[n]=i[n]+ai[n-1]+bi[n-2]$, $\sigma^2=1$, $r[\pm1]=-\frac{15}{16}$, $r[\pm2]=\frac14$: $r[2]=b=\frac14$; $r[1]=a(1+b)$ → $a=\frac{-15/16}{5/4}=-\frac34$ |
| **3c** · 1 p · **box 3A** | $r[0]=1+a^2+b^2=\frac{13}8$ → $\frac{13}8+2(-\frac{15}{16})\cos\theta+2(\frac14)\cos2\theta=\frac{13}8-\frac{15}8\cos\theta+\frac12\cos2\theta$ |
| **3d** · 1 p · **box 3B** | $a=-\frac{r[1]}{r[0]}=\frac{15}{26}$; $\sigma^2=r[0]+ar[1]=\frac{451}{416}$ → $P=\frac{5863}{7208+6240\cos\theta}$ (big fractions — the exam warns you) |
| **4a** · 0.3 p | matched-filter MC → **(a)** |
| **4b** · 0.7 p · **box 4A** | Gaussian vs Laplace: take $\ln$, quadratic, two-sided region → $\lvert y\rvert\gt$ **1.588** |
| **4c** · 1 p · **box 4A** (tails) | $P_{FA}=2Q(1.588)=$ **0.11**, $P_D=e^{-0.794}=$ **0.45** (as printed the curves are cut in half — say which convention you use) |
{: .battle }

## October 2021 · practice exam

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.5 p · **not on the sheet** (Bayes) | virus test → **(b) 37 %** |
| **1b** · 0.5 p | covariance MC: $\mathrm{Cov}=E[XY]-E[X]E[Y]$ → **(d)** |
| **1c** · 0.5 p | expected value MC → **(b)** |
| **1d** · 0.5 p | binomial MC: $\binom nk p^k(1-p)^{n-k}$ → **(d) 0.2936** |
| **1e** · 0.5 p · **box 4C** | ROC below the diagonal = hypotheses swapped or pdfs swapped → **(a)** |
| **1f** · 0.5 p · **not on the sheet** | $t$-statistic MC → **(c)** |
| **2a** · 1 p · **not on the sheet** | pdf from an MVUE (old format) → **Gaussian, mean $\theta$, variance $A^2$** |
| **2b** · 1 p · **box 2A** | same shape as Apr24-2c: $\ln$, differentiate, clear denominators → $\frac1{2N}\sum x^2$ |
| **3a** · 0.75 p · **box 3E** (ARMA $r[k]$) | $H(z)=\frac{1-\frac23z^{-1}}{1-\frac12z^{-1}}$ → $\alpha=-\frac12$, $\beta=-\frac23$, $\sigma^2=1$: $r[0]=\frac{28}{27}$; $r[1]=-\alpha r[0]+\beta\sigma^2=-\frac4{27}$; $r[k]=(\frac12)^{k-1}r[1]$ → $\frac{28}{27}$; $-\frac4{27}\left(\frac12\right)^{\lvert l\rvert-1}$ |
| **3b** · 0.75 p · **box 3B** | $r[0]=\frac{28}{27}$, $r[1]=-\frac4{27}$: $a=\frac17$, $\sigma^2=\frac{64}{63}$ → $P=\frac{32/9}{25/7+\cos\theta}$ |
| **3c** · 0.5 p · **box 3A** | MA(1) cut: $\frac{28}{27}+2(-\frac4{27})\cos\theta=\frac{28}{27}-\frac8{27}\cos\theta$ |
| **4a** · 1 p · **box 4A** + **Numbers** | Gaussian tails with the $\mathrm{erf}$ table → table |
| **4b** · 1 p · **box 4A** | unknown variance → the likelihood ratio becomes an **energy detector** ($\sum x_n^2$ vs a threshold) |
{: .battle }

## January 2020 · retake

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.25 p | valid autocorrelations MC: $r[-k]=r[k]$, $\lvert r[k]\rvert\le r[0]$ → **A** (only $r_B$) |
| **1b** · 0.25 p · **box 3G/3I** | Welch = overlapping segments, average the periodograms → **D** |
| **1c** · 0.25 p · **box 3J** | windowing MC (window lowers leakage, not resolution) → **C** |
| **1d** · 0.25 p | expected value MC → **B** |
| **2** · 2 p · **not on the sheet** (Bayes) | car painting: total probability + Bayes → **0.819; 0.18** |
| **3** · 2 p · **box 3A** + **box 3D** | $r[0]=\frac1{21}$, $r[\pm1]=\frac2{105}$, else 0: correlogram $=\frac1{21}+\frac4{105}\cos\theta$; MA(1) is $r[0]+2r[1]\cos\theta$ → **the same** |
| **4** · 2.5 p · **box 2C** | least-squares line (means, slope, intercept); **Gauss–Newton not on the sheet** → see page |
| **5** · 2.5 p · **box 4A** + **4B** | exponential LRT: take $\ln$, cut at $x_{th}$, then pick $\lambda$ for the wanted $P_D$ → **$x_{th}=1.58$; $\lambda_1=2.19$** |
{: .battle }

## November 2019 · written exam

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 1 p | cross-correlation MC: $r_{xy}[k]$ peaks where the signals align → **B** (shifted by 3) |
| **1b** · 0.5 p | true/false list → check each against boxes **2D / 3J / 4C** → **F F T T F** |
| **1c** · 1.5 p · **box 3I** | description table → method names |
| **2** · 2 p · **box 3A** + **box 3C** | $r=1,\,0.7,\,0.5,\,0.3,\,0$: correlogram $=1+1.4\cos\theta+\cos2\theta+0.6\cos3\theta$; AR(2): $D=r[0]^2-r[1]^2=0.51$, $a_1=-\frac{r[1](r[0]-r[2])}{D}=-0.686$, $a_2=\frac{r[1]^2-r[0]r[2]}{D}=-0.020$, $\sigma^2=r[0]+a_1r[1]+a_2r[2]=0.51$ |
| **3a** · 1 p · **box 2A** | pdf $\frac{x}{\theta^2}e^{-x^2/2\theta^2}$: $\ln x-2\ln\theta-\frac{x^2}{2\theta^2}$ → $-\frac{2N}\theta+\frac{\sum x^2}{\theta^3}=0$ → $\hat\theta=\sqrt{\frac1{2N}\sum x^2}$ |
| **3b** · 1 p · **box 2D** (Fisher) | CRLB for that model → $\frac{\theta^2}{4N}$ |
| **3c** · 1 p · **box 2B** | MAP = peak of the posterior: differentiate the $\ln$ posterior (a cubic) → cubic |
| **4** · 2 p · **box 4A** (two tails) | variance detection: $\lvert x\rvert\gt t$ → double the tail; $\sum x_n^2$ rule → **0.318, 0.004** |
{: .battle }

## January 2019 · retake

| Question | Box → solve it like this → answer |
|---|---|
| **1a** · 0.5 p | discrete random variables MC (PMF sums to 1, values countable) → **B, C** |
| **1b** · 0.5 p · **box 2A** | MLE expression MC: write $\ln L$ and differentiate → **D** |
| **1c** · 0.5 p · **box 3I/3J** | non-parametric estimation MC → **A, C** |
| **1d** · 0.5 p · **box 3E** | signal models MC (which equation is AR / MA / ARMA) → **C, D** |
| **2a** · 1 p · **box 2A** | $\lambda e^{-\lambda x}$: $\ln L=N\ln\lambda-\lambda\sum x_i$ → $\frac N\lambda-\sum x_i=0$ → $\hat\lambda=\frac{N}{\sum x_i}$ |
| **2b, 2c** · 2 p · **not on the sheet** | MMSE & MAP with a uniform prior (integral work) → see page (**the key has a typo**) |
| **3** · 2.5 p · **box 4A** + **erf table** | Gaussian LRT with the erf table → **0.5 / 0.159 …** |
| **4** · 2.5 p · **not on the sheet** | Wiener filter (old topic) → **$(1,2)$, 0; $(-1,0)$, $\frac43$** |
{: .battle }

## Questions from other exams (2023–2025 resits)

| Question | Box → solve it like this → answer |
|---|---|
| Jan 2025 resit **1a** | not on the sheet · table probabilities: count / total, then conditional = row / column total → **0.72; 0.335** |
| Jan 2025 resit **1b** | not on the sheet · Gaussian contour MC: equal density = ellipse around the mean → **C** |
| Jan 2025 resit **2b** | **box 2A** · one observation, $\ln p$ = const $-\frac{\mu^2\rho^2-2\rho\mu\sigma\theta+\sigma^2\rho^2}{2(1-\theta^2)}$; differentiate w.r.t. $\rho$, set 0: $\rho(\mu^2+\sigma^2)=\mu\sigma\theta$ → $\hat\rho=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}$ |
| Jun 2024 resit **1b** | not on the sheet · discrete vs continuous definitions MC → **C D C D C** |
| Jun 2024 resit **1c** | **box 1A** · $ce^{-x}e^{-y}$ on $0\le y\le x\lt\infty$: freeze $x$, $y$ from $0$ to $x$ → $\int_0^\infty\!\int_0^x ce^{-x}e^{-y}\,dy\,dx=c\int_0^\infty e^{-x}(1-e^{-x})dx=c\cdot\frac12=1$ → $c=$ **2** → **(d)** |
| Jan 2024 resit **1f** | **box 1C** · factorisation MC → **(c)** |
| Q2 2023-24 resit **3a** | **box 3H** · dies out → energy; never dies → power → **E P E E** |
| Q3 2023 resit **2c** | **box 2C** · LS MC: BLUE = best linear unbiased estimator → **(c)** |
| Q1 2023 resit **2a** | **box 2D** · Fisher MC, FALSE statement ("Fisher information is negative" is F) → **(b)** |
| Q1 2023 resit **2b** | **box 2A** · pdf $\frac{x_n}\theta e^{-x_n^2/\theta}$: $-\frac N\theta+\frac{\sum x_n^2}{\theta^2}=0$ → $\hat\theta=\frac1N\sum x_n^2$ |
| Q1 2023 resit **4c, 4d** | **box 4A** (Rayleigh) · same recipe as Jun26-4b with the exam's numbers → $x\gt$ **1.92** |
| Q3 2022-23 **2d** | **box 2C** · $x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$ → $e^{\bar x}$ |
| Q3 2022-23 **2f, 2g** | not on the sheet · mixture posterior (integral work) → MMSE $x(2c-1)$; MAP $\pm x$ / $x$ |
| Q3 2022-23 **2g, 2h** | **Calculations** · posterior $\propto e^{-(x+a)\theta}$: MMSE $=\frac{\int_0^\infty\theta e^{-(x+a)\theta}d\theta}{\int_0^\infty e^{-(x+a)\theta}d\theta}=\frac{1/c^2}{1/c}$ → MMSE $\frac1{x+a}$ |
{: .battle }

## If the question matches nothing

1. Write the box that is closest and plug the exam's numbers into its formulas — partial points are given for a formula with numbers in it.
2. Detection question? Write $L=\frac{p(x\mid H_1)}{p(x\mid H_0)}$, take $\ln$, solve for $x$. That is always worth something.
3. "True / false"? Quote the sheet's T/F table row. The exam recycles those exact sentences.
