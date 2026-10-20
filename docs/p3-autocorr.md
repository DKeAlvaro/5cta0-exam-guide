# 3.3 Autocorrelation and PSD of AR, MA and ARMA models

<p class="lead">Often the exam gives a difference equation (or a filter $H(z)$) driven by white noise and asks: which model is it, what is its PSD, what is its autocorrelation? This page is the "forward" direction: model → $r[l]$ and $P(e^{j\theta})$. The next page goes backwards: $r[l]$ → model.</p>

## The three models

White noise $i[n]$ (zero mean, variance $\sigma_i^2$) goes into a filter. The course writes:

| Model | Difference equation | $H(z)$ | PSD |
|---|---|---|---|
| **MA($q$)** | $x[n]=i[n]+b_1i[n-1]+\dots+b_qi[n-q]$ | $B(z)=1+\sum b_kz^{-k}$ | $\sigma_i^2\lvert B(e^{j\theta})\rvert^2$ |
| **AR($p$)** | $x[n]=i[n]-a_1x[n-1]-\dots-a_px[n-p]$ | $\dfrac{1}{A(z)}=\dfrac{1}{1+\sum a_kz^{-k}}$ | $\dfrac{\sigma_i^2}{\lvert A(e^{j\theta})\rvert^2}$ |
| **ARMA($p,q$)** | both | $\dfrac{B(z)}{A(z)}$ | $\sigma_i^2\dfrac{\lvert B(e^{j\theta})\rvert^2}{\lvert A(e^{j\theta})\rvert^2}$ |

!!! trap "The sign convention"
    The $a_k$ are defined with a **minus** in the difference equation. So $x[n]=i[n]+\frac34x[n-1]$ means $a_1=-\frac34$ and $A(z)=1-\frac34z^{-1}$. Get this wrong and every later number is wrong.

**How to tell which model it is:** past **inputs** $i[n-k]$ → MA part (zeros). Past **outputs** $x[n-k]$ → AR part (poles). Both → ARMA. Count the largest delay of each for the orders.

## Autocorrelation: the direct method

Multiply the difference equation by $x[n-l]$ and take expectations. Two facts do all the work:

1. **Future noise is uncorrelated with the past signal:** $E\{i[n]\,x[n-l]\}=0$ for $l\ge1$.
2. $E\{i[n]\,x[n]\}=\sigma_i^2$, and in general $E\{i[n-k]\,x[n]\}=\sigma_i^2h[k]$ ($h$ = impulse response).

**MA($q$)**: the autocorrelation is the noise variance times the "overlap" of the coefficient list with a shifted copy of itself, and it **stops after lag $q$**:

$$r[l]=\sigma_i^2\sum_{k=|l|}^{q}b_kb_{k-|l|}\quad(b_0=1),\qquad r[l]=0\text{ for }|l|>q.$$

**AR(1)** $x[n]=i[n]-a\,x[n-1]$: $\ r[l]=\dfrac{\sigma_i^2}{1-a^2}(-a)^{|l|}$, decaying forever.

**ARMA(1,1)** $x[n]=i[n]+b\,i[n-1]-a\,x[n-1]$: with $h[0]=1$, $h[1]=b-a$,

$$r[0]=\sigma_i^2\big(1+b(b-a)\big)-a\,r[1],\qquad r[1]=\sigma_i^2b-a\,r[0],\qquad r[l]=-a\,r[l-1]\ (l\ge2).$$

Two equations, two unknowns ($r[0], r[1]$), then a geometric tail. This is the reader's ARMA formula (13.26) written out for $p=q=1$.

!!! recipe "Recipe: model → PSD"
    1. Read off $b_k$ and $a_k$ (watch the sign!).
    2. $P(e^{j\theta})=\sigma_i^2\frac{|1+b_1e^{-j\theta}|^2}{|1+a_1e^{-j\theta}|^2}$ and expand each factor with $|1+ce^{-j\theta}|^2=1+c^2+2c\cos\theta$.
    3. Clean up the fractions (multiply numerator and denominator by the same number).

---

## Exam questions

### April 2024 exam · 3b, 3c {#apr24-3b}

!!! exam "Final exam Q3, April 2024 · 3b (0.1 p), 3c (0.5 p)"
    A random signal is described by the following difference equation:

    $$x[n] = i[n] - \frac{1}{2}i[n-1] + \frac{1}{4}i[n-2] - \frac{1}{2}i[n-3].$$

    **3b** Which kind of signal model does this signal represent?

    **3c** Calculate the autocorrelation function of $x[n]$

???+ solution "Solution"
    **3b.** Only past inputs, the largest delay is 3 → **MA(3)** with $b=[1,-\frac12,\frac14,-\frac12]$.

    **3c.** The noise variance is not given, so take $\sigma_i^2=1$ (otherwise multiply everything by $\sigma_i^2$). Slide the coefficient list over itself:

    | lag | products | $r[l]$ |
    |---|---|---|
    | 0 | $1+\frac14+\frac1{16}+\frac14$ | $\frac{25}{16}$ |
    | ±1 | $1(-\frac12)+(-\frac12)(\frac14)+(\frac14)(-\frac12)$ | $-\frac34$ |
    | ±2 | $1(\frac14)+(-\frac12)(-\frac12)$ | $\frac12$ |
    | ±3 | $1(-\frac12)$ | $-\frac12$ |
    | $\lvert l\rvert\ge4$ | — | 0 |

    !!! answer "Answer"
        3b: MA(3). 3c: $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$, $r[\pm3]=-\frac12$, 0 otherwise ($\sigma_i^2=1$).

    These lags are used again in [3d–3f](p3-chain.md#apr24-3d).

### November 2022 exam · 3c, 3d, 3e {#nov22-3c}

!!! exam "Final exam Q1, 7 November 2022 · 3c (0.15 p), 3d (0.35 p), 3e (0.5 p)"
    The random signal $x[k]$ is described by the following difference equation:

    $$x[k] = i[k] - i[k - 1] + \frac{3}{4}x[k - 1],$$

    with $i[k]$ the innovation signal (zero mean and $\sigma_i^2 = 7/8$).

    **3c** Which kind of process does $x[k]$ represents?

    **3d** Calculate the power spectral density $P_x(e^{j\theta})$ of $x[k]$.

    **3e** Calculate the autocorrelation $r[\tau]$ of $x[k]$.

???+ solution "Solution"
    **3c.** One past input and one past output → **ARMA(1,1)**, with $b_1=-1$ and $a_1=-\frac34$ (sign convention!).

    **3d.**

    $$P_x(e^{j\theta})=\frac78\cdot\frac{|1-e^{-j\theta}|^2}{|1-\frac34e^{-j\theta}|^2}=\frac78\cdot\frac{2-2\cos\theta}{\frac{25}{16}-\frac32\cos\theta}=\frac{28(1-\cos\theta)}{25-24\cos\theta}.$$

    Note $P=0$ at $\theta=0$: the zero sits on the unit circle at $z=1$, so the process has no DC power.

    **3e.** $b=-1$, $a=-\frac34$, so $h[1]=b-a=-\frac14$.

    $$r[0]=\tfrac78\big(1+(-1)(-\tfrac14)\big)+\tfrac34r[1]=\tfrac{35}{32}+\tfrac34r[1],\qquad r[1]=\tfrac78(-1)+\tfrac34r[0].$$

    Substitute the second into the first: $r[0]=\frac{35}{32}-\frac{21}{32}+\frac9{16}r[0]\Rightarrow\frac7{16}r[0]=\frac7{16}\Rightarrow r[0]=1$, and $r[1]=-\frac78+\frac34=-\frac18$. After lag 1 only the AR part acts: $r[l]=\frac34r[l-1]$.

    !!! answer "Answer"
        3c: ARMA(1,1). 3d: $P_x=\dfrac{28(1-\cos\theta)}{25-24\cos\theta}$. 3e: $r[0]=1$, $r[l]=-\frac18\left(\frac34\right)^{|l|-1}$ for $|l|\ge1$.

    (I checked these with a 400 000-sample simulation: $\hat r[0]=0.997$, $\hat r[1]=-0.126$, $\hat r[2]=-0.095$ vs $-3/32=-0.094$.) The rest of this exercise (3f, 3g) is [on the next page](p3-chain.md#nov22-3f).

### Practice exam 2021 · 3a {#pe21-3a}

!!! exam "Practice exam, 28 October 2021 · 3a · 0.75 p"
    Calculate the autocorrelation function of the random signal $x[k]$ that is generated by filtering innovation $i[k]$ (white noise sequence with zero mean and variance $\sigma_i^2 = 1$) with the filter

    $$H(z) = \frac{(1 - \frac{2}{3}z^{-1})}{(1 - \frac{1}{2}z^{-1})}$$

???+ solution "Solution"
    **Filter → difference equation:** $X(z)(1-\frac12z^{-1})=I(z)(1-\frac23z^{-1})$, so $x[k]=i[k]-\frac23i[k-1]+\frac12x[k-1]$. ARMA(1,1) with $b=-\frac23$, $a=-\frac12$, $h[1]=b-a=-\frac16$ (the review slides get $h[1]$ by long division: $\frac{1-\frac23z^{-1}}{1-\frac12z^{-1}}=1-\frac16z^{-1}-\dots$).

    $$r[0]=1+\big(-\tfrac23\big)\big(-\tfrac16\big)+\tfrac12r[1]=\tfrac{10}9+\tfrac12r[1],\qquad r[1]=-\tfrac23+\tfrac12r[0].$$

    $r[0]=\frac{10}9-\frac13+\frac14r[0]\Rightarrow\frac34r[0]=\frac79\Rightarrow r[0]=\frac{28}{27}$, $\ r[1]=-\frac23+\frac{14}{27}=-\frac4{27}$, then $r[l]=\frac12r[l-1]$.

    **PSD** (asked in the review): $P(e^{j\theta})=\dfrac{\frac{13}9-\frac43\cos\theta}{\frac54-\cos\theta}$.

    !!! answer "Answer"
        $r[0]=\frac{28}{27}$, $r[l]=-\frac{4}{27}\left(\frac12\right)^{|l|-1}$ for $|l|\ge1$

### January 2022 resit · 3b {#jan22-3b}

!!! exam "Resit, 24 January 2022 · 3b · 1 p"
    A real MA(2) process has difference equation given by $x[n] = i[n] + ai[n - 1] + bi[n - 2]$, with $i[n]$ white noise process (zero mean and unit variance). The parameters $a$ and $b$ are real. The following lags of the autocorrelation are known

    $$r_x[\tau] = E\{x[n]x[n-\tau]\} = \begin{cases} -\frac{15}{16} & \text{for } \tau = \pm 1, \\ \frac{1}{4} & \text{for } \tau = \pm 2 \end{cases}$$

    Based on the given lags of the autocorrelation function, calculate the parameters $a$ and $b$.

???+ solution "Solution"
    MA(2) with $\sigma_i^2=1$, coefficients $[1,a,b]$:

    - $r[2]=1\cdot b=b=\frac14$ (the outermost overlap: first × last).
    - $r[1]=1\cdot a+a\cdot b=a(1+b)=-\frac{15}{16}\Rightarrow a=\frac{-15/16}{5/4}=-\frac34$.

    Start from the largest lag: it has a single product, so it gives one coefficient directly.

    !!! answer "Answer"
        $a=-\frac34$, $b=\frac14$

### January 2019 retake · 1d {#jan19-1d}

!!! exam "Written exam, 21 January 2019 · Exercise 1(d) · 0.5 p (1 or 2 answers correct)"
    In the context of linear random signal models, which ones of the following statements are true?

    - A. The autocorrelation function of a moving-average (MA) model with $Q$ zeros is a finite sequence of length $Q$.
    - B. The autocorrelation matrix of an ARMA model is diagonal.
    - C. Assuming a moving-average model (MA), parametric spectral estimation by the Yule-walker method requires resolution of non-linear equations.
    - D. Linear signal models can be used for data compression.

???+ solution "Solution"
    - A ✗: non-zero for $|l|\le Q$, so length $2Q+1$.
    - B ✗: only white noise has a diagonal autocorrelation matrix.
    - C ✓: the MA equations contain products $b_kb_{k-l}$ (see MA(1) on the next page: a quadratic).
    - D ✓: a few model parameters describe a long signal.

    !!! answer "Answer"
        **C and D**
