# 3.4 The correlogram → AR → MA chain

<p class="lead">This is the single most valuable page of the guide. Since 2019 almost every exam gives you a few autocorrelation values and asks for the same chain: <b>correlogram PSD</b>, then an <b>AR model by Yule–Walker</b>, often an <b>MA(1) model</b>, and recently <b>"which plot is right?"</b>. Around 2 points, fully mechanical.</p>

## The three estimates from the same numbers

You are given $r[0]$, $r[\pm1]$, sometimes $r[\pm2]$, $r[\pm3]$.

### 1. Correlogram (non-parametric)

Assume $r[l]=0$ beyond the given lags and take the Fourier transform. Pair $l$ with $-l$ using $e^{jl\theta}+e^{-jl\theta}=2\cos l\theta$:

$$\boxed{\hat P_{corr}(e^{j\theta})=r[0]+2\sum_{k\ge1}r[k]\cos(k\theta)}$$

It can dip **below zero** if the true autocorrelation does not really stop there. A real PSD never does.

### 2. AR($p$) by Yule–Walker (parametric)

Model $x[n]=i[n]-a_1x[n-1]-\dots-a_px[n-p]$. The Yule–Walker equations, in the course's matrix form:

$$\begin{bmatrix}r[0]&r[1]&\cdots&r[p]\\r[1]&r[0]&\cdots&r[p-1]\\\vdots&&\ddots&\vdots\\r[p]&r[p-1]&\cdots&r[0]\end{bmatrix}\begin{bmatrix}1\\a_1\\\vdots\\a_p\end{bmatrix}=\begin{bmatrix}\sigma_i^2\\0\\\vdots\\0\end{bmatrix}$$

**How to solve it:** rows 2 to $p+1$ only contain the $a$'s, so solve those first. Then row 1 gives the noise variance: $\sigma_i^2=r[0]+a_1r[1]+\dots+a_pr[p]$.

| Order | Coefficients | Noise variance |
|---|---|---|
| AR(1) | $a_1=-\dfrac{r[1]}{r[0]}$ | $\sigma_i^2=r[0]+a_1r[1]$ |
| AR(2) | solve $\begin{cases}r[0]a_1+r[1]a_2=-r[1]\\r[1]a_1+r[0]a_2=-r[2]\end{cases}$ | $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$ |

Then

$$\hat P_{AR}(e^{j\theta})=\frac{\sigma_i^2}{|1+a_1e^{-j\theta}+a_2e^{-j2\theta}|^2},\qquad|1+a_1e^{-j\theta}|^2=1+a_1^2+2a_1\cos\theta,$$

$$|1+a_1e^{-j\theta}+a_2e^{-j2\theta}|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos2\theta.$$

(The same numbers come out of the 1-step linear predictor / Wiener filter: $\mathbf w=-\mathbf a$ and the minimum error is $\sigma_i^2$. The review slides show both methods.)

### 3. MA(1) (parametric)

Model $x[n]=i[n]+b\,i[n-1]$. Match two equations:

$$\sigma_i^2(1+b^2)=r[0],\qquad\sigma_i^2b=r[1]\quad\Rightarrow\quad r[1]\,b^2-r[0]\,b+r[1]=0.$$

The two roots are $b$ and $1/b$. **Keep $|b|<1$** (minimum phase, like spectral factorisation), then $\sigma_i^2=r[1]/b$.

!!! idea "Shortcut that saves minutes"
    Expand the MA(1) PSD: $\sigma_i^2|1+be^{-j\theta}|^2=\sigma_i^2(1+b^2)+2\sigma_i^2b\cos\theta=r[0]+2r[1]\cos\theta$.
    **The MA(1) PSD is just the correlogram truncated at lag 1.** You still have to give $b$ and $\sigma_i^2$ if they are asked, but you can write the PSD immediately, exactly, without the rounding errors of $b\approx-0.13$.

!!! recipe "Recipe: the whole chain"
    1. **Correlogram:** $r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$
    2. **AR($p$):** write the matrix; solve the $a$'s from rows 2…; $\sigma_i^2$ from row 1; plug into $\sigma_i^2/|A(e^{j\theta})|^2$ and expand.
    3. **MA(1):** quadratic in $b$, keep $|b|<1$, $\sigma_i^2=r[1]/b$; PSD $=r[0]+2r[1]\cos\theta$.
    4. **Which plot?** Evaluate every curve at $\theta=0$ and $\theta=\pm\pi$ (where $\cos\theta=\pm1$). Remove plots where an AR/MA curve goes negative. Done.
    5. **"As a function of $\cos\theta$ only":** replace $\cos2\theta=2\cos^2\theta-1$.

## Reading PSD plots

<figure markdown>
![AR peaks, MA dips, correlogram wiggles](img/gen/p3_shapes.svg)
<figcaption>Horizontal axis: normalised frequency $\theta$ from $-\pi$ to $\pi$. A PSD of a real signal is symmetric, so only $0\ldots\pi$ really matters. $\theta=0$ is DC, $\theta=\pm\pi$ the fastest possible oscillation. AR(1) with $a_1<0$ (i.e. $x[n]=0.8x[n-1]+\dots$, a smooth slow signal) peaks at 0; $a_1>0$ peaks at $\pi$. MA spectra are smooth and can touch 0. A truncated correlogram can wiggle and even go below zero.</figcaption>
</figure>

---

## Exam questions

### June 2026 resit · 3c, 3d {#jun26-3c}

!!! exam "Resit Q4, June 2026 · 3c (0.5 p), 3d (1 p)"
    Consider a wide-sense stationary, real-valued random process $x[n]$ whose first three autocorrelation values have been estimated as:

    $$r_x[0] = 3, \quad r_x[1] = 2, \quad r_x[2] = 1$$

    **3c** Calculate the non-parametric correlogram estimate of the power spectral density, $\hat{P}_{Corr}(e^{j\theta})$, using only the given autocorrelation lags. Assume $r_x[k] = 0$ for $|k| > 2$. Derive $\hat{P}_{Corr}(e^{j\theta})$ as a function of $\cos(\theta)$.

    **3d** You now wish to model this process parametrically using an Autoregressive (AR) model of order $p = 2$:

    $$x[n] = i[n] - a_1 x[n-1] - a_2 x[n-2]$$

    where $i[n]$ is zero-mean white noise with variance $\sigma_i^2$.

    - State the Yule-Walker equations for this AR(2) process in matrix form. [0.1]
    - Calculate the AR coefficients $a_1$ and $a_2$. [0.4]
    - Calculate the variance of the driving white noise $\sigma_i^2$. [0.2]
    - Based on your estimated parameters, write the expression for the parametric power spectral density estimate $\hat{P}_{AR}(e^{j\theta})$. Express it as a function of $\cos(\theta)$. [0.3]

???+ solution "Solution"
    **3c.**

    $$\hat P_{corr}=3+2\cdot2\cos\theta+2\cdot1\cos2\theta=3+4\cos\theta+2\cos2\theta.$$

    As a function of $\cos\theta$ only ($\cos2\theta=2\cos^2\theta-1$):

    $$\hat P_{corr}(e^{j\theta})=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2.$$

    **3d. Yule–Walker in matrix form:**

    $$\begin{bmatrix}3&2&1\\2&3&2\\1&2&3\end{bmatrix}\begin{bmatrix}1\\a_1\\a_2\end{bmatrix}=\begin{bmatrix}\sigma_i^2\\0\\0\end{bmatrix}$$

    **Coefficients** from rows 2 and 3:

    $$\begin{cases}2+3a_1+2a_2=0\\1+2a_1+3a_2=0\end{cases}\Rightarrow\begin{cases}3a_1+2a_2=-2\\2a_1+3a_2=-1\end{cases}\Rightarrow a_1=\frac{-6+2}{5}=-\frac45,\quad a_2=\frac{-3+4}{5}=\frac15.$$

    **Noise variance** from row 1: $\sigma_i^2=3+2a_1+1\cdot a_2=3-\frac85+\frac15=\frac85$.

    **PSD:**

    $$|A|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos2\theta=\frac{42}{25}-\frac{48}{25}\cos\theta+\frac25\cos2\theta=\frac{4}{25}\big(5\cos^2\theta-12\cos\theta+8\big)$$

    $$\hat P_{AR}(e^{j\theta})=\frac{8/5}{\frac{4}{25}(5\cos^2\theta-12\cos\theta+8)}=\frac{10}{5\cos^2\theta-12\cos\theta+8}.$$

    Sanity checks: at $\theta=0$, $\hat P_{AR}=10$ and $\hat P_{corr}=9$; at $\theta=\pi$, $0.4$ and $1$. Both are low-pass, as expected from the positive, slowly decaying $r$.

    ![correlogram vs AR(2)](img/gen/p3_jun26.svg)

    !!! answer "Answer"
        3c: $\hat P_{corr}=3+4\cos\theta+2\cos2\theta=(2\cos\theta+1)^2$.
        3d: $a_1=-\frac45$, $a_2=\frac15$, $\sigma_i^2=\frac85$, $\hat P_{AR}=\dfrac{10}{5\cos^2\theta-12\cos\theta+8}$.

### June 2026 resit · 3e {#jun26-3e}

!!! exam "Resit Q4, June 2026 · 3e · 0.75 p"
    You are given a finite data record of length $N$ and you decide to estimate its power spectral density by fitting an Autoregressive (AR) model of order $p$.

    1. Suppose you evaluate the quality of your fitted model by strictly looking at the variance of the residual error (the difference between the data and the prediction). As you increase the model order $p$, what will happen to this residual error, and what is the primary risk of choosing an excessively high order $p$? [0.25]
    2. Name at least one specific model selection criteria discussed in the course that are designed to prevent the issue identified in question 1. Briefly explain the mathematical mechanism it uses to do so. [0.25]
    3. It is a known property that any arbitrary power spectrum (even one originating from an MA process containing deep spectral nulls) can be approximated using strictly an AR model. What is required to achieve this? [0.25]

???+ solution "Solution"
    ![residual variance vs AIC](img/gen/p3_order.svg)

    1. The residual variance $\hat\sigma_p^2$ **keeps decreasing** (never increases) as $p$ grows: a bigger model can always fit the data at least as well. The risk is **overfitting**: the model starts fitting the noise of this particular record. You get spurious peaks and a spectrum that does not generalise.
    2. **Akaike's information criterion** $\text{AIC}(P)=N\ln\hat\sigma_P^2+2P$ (or the corrected AICc, or the **final prediction error** $\text{FPE}(P)=\frac{N+P}{N-P}\hat\sigma_P^2$), with $P=p+1$ parameters. The first term falls as the model gets better; the **penalty** $2P$ grows with the number of parameters. Pick the order with the **minimum** criterion.
    3. A **sufficiently high AR order** (in theory $p\to\infty$). An MA process can be written as an infinite-order AR, since $1/B(z)$ expanded is an infinite series for a minimum-phase $B$. In practice that means a high $p$, and enough data ($N\gg p$) to estimate it.

    !!! answer "Answer"
        1. Decreases monotonically; risk = overfitting (fitting noise, spurious peaks). 2. AIC $=N\ln\hat\sigma^2+2P$ (or FPE/AICc): error term + complexity penalty, choose the minimum. 3. A high enough AR order (AR(∞) in theory).

### April 2025 exam · 3d, 3e, 3f, 3g {#apr25-3d}

!!! exam "Final exam Q3, 13 April 2025 · 3d (0.5 p), 3e (0.5 p), 3f (0.5 p), 3g (0.25 p)"
    Suppose you have an estimate of the autocorrelation function of a random signal at lags $0, \pm 1, \pm 2$ as: $r[0] = 2, \quad r[\pm 1] = -\frac{1}{4}, \quad r[\pm 2] = -\frac{3}{16}$

    **3d** Use the correlogram method to calculate the power spectral density in a non-parametric fashion. Express the obtained power spectral density $P_{corr}(e^{j\theta})$ as a function of cosines.

    **3e** Model the signal as an AR(1) process, find the parameters of the model, and calculate the corresponding power spectral density in a parametric fashion. Express the obtained power spectral density $P_{AR}(e^{j\theta})$ as a function of cosines.

    **3f** Model the signal as an MA(1) process, find the parameters of the model, and calculate the corresponding power spectral density in a parametric fashion. Express the obtained power spectral density $P_{MA}(e^{j\theta})$ as a function of cosines.

    **3g** Given the plots in the figure below, which option represents the correct power spectral densities, as found in 3d, 3e, and 3f?

    ![Plots A–D](img/exam/apr25-3g.jpg)

    - (a) Plot D
    - (b) Plot C
    - (c) Plot B
    - (d) Plot A

???+ solution "Solution"
    **3d.**

    $$P_{corr}=2+2\left(-\tfrac14\right)\cos\theta+2\left(-\tfrac3{16}\right)\cos2\theta=2-\tfrac12\cos\theta-\tfrac38\cos2\theta.$$

    **3e. AR(1):**

    $$\begin{bmatrix}2&-\frac14\\-\frac14&2\end{bmatrix}\begin{bmatrix}1\\a_1\end{bmatrix}=\begin{bmatrix}\sigma_i^2\\0\end{bmatrix}\Rightarrow-\tfrac14+2a_1=0\Rightarrow a_1=\tfrac18,\qquad\sigma_i^2=2-\tfrac14\cdot\tfrac18=\tfrac{63}{32}.$$

    $$P_{AR}=\frac{63/32}{1+\frac1{64}+\frac14\cos\theta}=\frac{63/32}{\frac{65+16\cos\theta}{64}}=\frac{126}{65+16\cos\theta}.$$

    **3f. MA(1):** $\sigma_i^2(1+b^2)=2$, $\sigma_i^2b=-\frac14$. Divide: $\frac{b}{1+b^2}=-\frac18\Rightarrow b^2+8b+1=0\Rightarrow b=-4\pm\sqrt{15}$. Keep $b=-4+\sqrt{15}\approx-0.127$ (the other root, $-7.87$, is outside the unit circle). $\sigma_i^2=\frac{-1/4}{b}\approx1.968$.

    $$P_{MA}=1.968\,|1-0.127e^{-j\theta}|^2=r[0]+2r[1]\cos\theta=2-0.5\cos\theta.$$

    **3g. Pick the plot.** Evaluate at the two ends:

    | | $\theta=0$ | $\theta=\pm\pi$ |
    |---|---|---|
    | $P_{corr}$ | $2-0.5-0.375=1.125$ | $2+0.5-0.375=2.125$ |
    | $P_{AR}$ | $126/81=1.56$ | $126/49=2.57$ |
    | $P_{MA}$ | $1.5$ | $2.5$ |

    Plot A has $P_{corr}<0$ at 0 and C has AR/MA negative → out. B has everything ≈0.8–0.9 at 0 → out. **D** matches: corr ≈ 1.1 at 0 and ≈ 2.1 at ±π, AR and MA almost on top of each other going from ≈ 1.5 to ≈ 2.5.

    ![our own plot](img/gen/p3_apr25.svg)

    !!! answer "Answer"
        3d: $2-\frac12\cos\theta-\frac38\cos2\theta$. 3e: $a_1=\frac18$, $\sigma_i^2=\frac{63}{32}$, $P_{AR}=\frac{126}{65+16\cos\theta}$. 3f: $b_1\approx-0.13$, $\sigma_i^2\approx1.97$, $P_{MA}\approx2-0.5\cos\theta$. 3g: **(a) Plot D**.

### April 2024 exam · 3d, 3e, 3f {#apr24-3d}

!!! exam "Final exam Q3, April 2024 · 3d (0.4 p), 3e (0.7 p), 3f (0.4 p)"
    *(Signal from [3b/3c](p3-autocorr.md#apr24-3b): $x[n]=i[n]-\frac12i[n-1]+\frac14i[n-2]-\frac12i[n-3]$, so $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$, $r[\pm3]=-\frac12$.)*

    **3d** Using the correlogram method, give an estimate of the power spectral density. Express it as a function of cosines.

    **3e** Now model the signal as AR(2) process. Find the model parameters and the power spectral density,

    **3f** Which of the following figures gives the correct plots for $P_{corr}(e^{j\theta})$ (calculated in d) and of $P_{AR}(e^{j\theta})$ (calculated in e) ? If you cannot find the correct answer, please sketch $P_{corr}(e^{j\theta})$ and $P_{AR}(e^{j\theta})$ in the plot below.

    <div class="grid3" markdown>
    ![A](img/exam/apr24-3f-A.jpg)
    ![B](img/exam/apr24-3f-B.jpg)
    ![C](img/exam/apr24-3f-C.jpg)
    ![D](img/exam/apr24-3f-D.jpg)
    </div>

    (a) C  (b) A  (c) B  (d) D

???+ solution "Solution"
    **3d.**

    $$P_{corr}=\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta.$$

    For an MA(3) process the autocorrelation really is zero beyond lag 3, so this is also the **true** PSD of the signal.

    **3e. AR(2)** from rows 2–3 of Yule–Walker (multiply by 16 to clear fractions):

    $$\begin{cases}\frac{25}{16}a_1-\frac34a_2=\frac34\\-\frac34a_1+\frac{25}{16}a_2=-\frac12\end{cases}\Rightarrow\begin{cases}25a_1-12a_2=12\\-12a_1+25a_2=-8\end{cases}\qquad\det=625-144=481$$

    $$a_1=\frac{12\cdot25-12\cdot8}{481}=\frac{204}{481}\approx0.424,\qquad a_2=\frac{25(-8)+12\cdot12}{481}=-\frac{56}{481}\approx-0.116$$

    $$\sigma_i^2=r[0]+a_1r[1]+a_2r[2]=\frac{25}{16}-\frac34(0.424)+\frac12(-0.116)\approx1.186$$

    $$P_{AR}(e^{j\theta})=\frac{1.186}{|1+0.424e^{-j\theta}-0.116e^{-j2\theta}|^2}\approx\frac{1.186}{1.193+0.750\cos\theta-0.233\cos2\theta}.$$

    **3f. Pick the plot.**

    | | $\theta=0$ | $\theta=\pm\pi$ |
    |---|---|---|
    | $P_{corr}$ | $\frac{25}{16}-\frac32+1-1=0.06$ | $\frac{25}{16}+\frac32+1+1=5.06$ |
    | $P_{AR}$ | $1.186/1.710=0.69$ | $1.186/0.211=5.6$ |

    A: corr ≈ 2 at 0 and ≈ 7 at π, no. C: peak at 0, wrong shape. D: the AR curve goes **negative**, impossible. **B** matches: corr ≈ 0 at 0 and ≈ 5 at π; AR ≈ 0.7 and ≈ 5.6.

    ![our own plot](img/gen/p3_apr24.svg)

    !!! answer "Answer"
        3d: $\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$. 3e: $a_1=\frac{204}{481}$, $a_2=-\frac{56}{481}$, $\sigma_i^2\approx1.19$. 3f: **(c) plot B**.

### November 2022 exam · 3f, 3g {#nov22-3f}

!!! exam "Final exam Q1, 7 November 2022 · 3f (0.75 p), 3g (0.75 p)"
    *(Process from [3c–3e](p3-autocorr.md#nov22-3c): ARMA(1,1) with $r[0]=1$, $r[l]=-\frac18(\frac34)^{|l|-1}$.)*

    **3f** Try to model $x[k]$ as a AR(1) signal and calculate the corresponding power spectral density $P_{AR1}(e^{j\theta})$.

    **3g** Try to model $x[k]$ as a MA(1) signal and calculate the corresponding power spectral density $P_{MA1}(e^{j\theta})$. You can approximate the model parameters and the resulting PSD expression by using decimal numbers.

???+ solution "Solution"
    Use $r[0]=1$, $r[1]=-\frac18$.

    **3f.** $a_1=-\frac{r[1]}{r[0]}=\frac18$, $\sigma_i^2=1-\frac18\cdot\frac18=\frac{63}{64}$.

    $$P_{AR1}=\frac{63/64}{1+\frac1{64}+\frac14\cos\theta}=\frac{63}{65+16\cos\theta}.$$

    **3g.** $\frac{b}{1+b^2}=-\frac18\Rightarrow b^2+8b+1=0\Rightarrow b=-4+\sqrt{15}\approx-0.13$; $\sigma_i^2=\frac{r[1]}{b}\approx0.98$.

    $$P_{MA1}\approx0.98\,|1-0.13e^{-j\theta}|^2=r[0]+2r[1]\cos\theta=1-0.25\cos\theta.$$

    **Extra question from the review:** with only 3 lags ($r[\pm2]=-\frac3{32}$), the correlogram is $1-\frac14\cos\theta-\frac3{16}\cos2\theta$.

    ![true vs estimates](img/gen/p3_nov22.svg)

    The true PSD is exactly 0 at $\theta=0$ (zero on the unit circle). None of the low-order estimates can reproduce that deep notch: AR models can only make peaks, and MA(1)/correlogram with 2–3 lags are too smooth. (Jun 2026 3e.3: you would need a very high AR order.)

    !!! answer "Answer"
        3f: $a_1=\frac18$, $\sigma_i^2=\frac{63}{64}$, $P_{AR1}=\frac{63}{65+16\cos\theta}$. 3g: $b_1\approx-0.13$, $\sigma_i^2\approx0.98$, $P_{MA1}\approx1-0.25\cos\theta$.

### January 2022 resit · 3c, 3d {#jan22-3c}

!!! exam "Resit, 24 January 2022 · 3c (1 p), 3d (1 p)"
    *(MA(2) process from [3b](p3-autocorr.md#jan22-3b): $x[n]=i[n]+ai[n-1]+bi[n-2]$, unit variance, $r[\pm1]=-\frac{15}{16}$, $r[\pm2]=\frac14$.)*

    **3c** Calculate the power spectral density of $x[n]$ using the correlogram method. If you were not able to solve question 3b, you may use the following parameters $a = \frac{1}{4}$ and $b = \frac{5}{4}$ for $x[n]$. Please express the power spectral density as a function of $\cos(\theta)$. **Hint:** The autocorrelation of a MA process is of finite length.

    **3d** Now assume that $x[n]$ can be modeled as generated by an AR(1) process. Find the AR model parameters and the power spectral density of the AR(1) process (expressed as a function of $\cos(\theta)$). If you were not able to solve question 3b, you may use the following parameters $a = \frac{1}{4}$ and $b = \frac{5}{4}$ for $x[n]$. **Hint:** Some parameters may results in fractions with large numbers.

???+ solution "Solution"
    **3c.** The missing lag: $r[0]=1+a^2+b^2=1+\frac9{16}+\frac1{16}=\frac{13}8$. For an MA(2) the autocorrelation stops at lag 2, so the correlogram is exact:

    $$P(e^{j\theta})=\frac{13}8-\frac{15}8\cos\theta+\frac12\cos2\theta.$$

    **3d.** $a_1=-\frac{r[1]}{r[0]}=\frac{15/16}{13/8}=\frac{15}{26}$, $\ \sigma_i^2=\frac{13}8-\frac{15}{16}\cdot\frac{15}{26}=\frac{451}{416}\approx1.084$.

    $$P_{AR}=\frac{451/416}{1+\frac{225}{676}+\frac{15}{13}\cos\theta}=\frac{451/416}{\frac{901}{676}+\frac{15}{13}\cos\theta}=\frac{5863}{7208+6240\cos\theta}.$$

    (With the fallback values $a=\frac14$, $b=\frac54$: $r=[\frac{21}8,\frac9{16},\frac54]$, $P_{corr}=\frac{21}8+\frac98\cos\theta+\frac52\cos2\theta$, $a_1=-\frac3{14}$, $\sigma_i^2=\frac{561}{224}$, $P_{AR}=\frac{3927}{1640-672\cos\theta}$.)

    ![correlogram vs AR(1)](img/gen/p3_jan22.svg)

    !!! answer "Answer"
        3c: $\frac{13}8-\frac{15}8\cos\theta+\frac12\cos2\theta$. 3d: $a_1=\frac{15}{26}$, $\sigma_i^2=\frac{451}{416}$, $P_{AR}=\dfrac{5863}{7208+6240\cos\theta}$.

### Practice exam 2021 · 3b, 3c {#pe21-3b}

!!! exam "Practice exam, 28 October 2021 · 3b (0.75 p), 3c (0.5 p)"
    *(Signal from [3a](p3-autocorr.md#pe21-3a): $\rho[0]=\frac{28}{27}$, $\rho[1]=-\frac4{27}$, $\rho[\tau]=(\frac12)^{|\tau|-1}\rho[1]$.)*

    **3b** Now suppose you model the random signal as generated by a AR(1) process. 1. Find the AR model parameters. 2. Obtain the power spectral density function $P_{AR1}(e^{j\theta})$ from the AR(1) model and provide a sketch.

    **3c** Now suppose that you approximate the random signal as generated by a MA(1) process. 1. use the correlogram method to calculate the power spectral density $P_{\text{corrMA1}}(e^{j\theta})$ from the autocorrelation function calculated in 3a. **There is no need to calculate the MA model parameters.** 2. Provide a sketch of the $P_{\text{corrMA1}}(e^{j\theta})$. You may draw this sketch on top of the plot obtained in 3b. **Hint:** For an MA process, the number of autocorrelation lags different than zero is finite and related to the order of the MA process.

???+ solution "Solution"
    **3b.** $a_1=-\frac{-4/27}{28/27}=\frac17$, $\sigma_i^2=\frac{28}{27}-\frac17\cdot\frac4{27}=\frac{64}{63}$.

    $$P_{AR1}=\frac{64/63}{1+\frac1{49}+\frac27\cos\theta}=\frac{32/9}{\frac{25}7+\cos\theta}.$$

    Sketch values: $0.78$ at $\theta=0$, $1.00$ at $\pm\frac\pi2$, $1.38$ at $\pm\pi$ (a gentle high-pass).

    **3c.** MA(1) → only lags $0,\pm1$:

    $$P_{corr,MA1}=\frac{28}{27}-\frac{8}{27}\cos\theta$$

    $0.74$ at 0, $1.04$ at $\pm\frac\pi2$, $1.33$ at $\pm\pi$: almost on top of the AR(1) curve.

    ![AR(1), correlogram and true ARMA](img/gen/p3_pe21.svg)

    !!! answer "Answer"
        3b: $a_1=\frac17$, $\sigma_i^2=\frac{64}{63}$, $P_{AR1}=\dfrac{32/9}{25/7+\cos\theta}$. 3c: $P=\frac{28}{27}-\frac8{27}\cos\theta$.

### January 2020 retake · Exercise 3 {#jan20-3}

!!! exam "Retake exam, 20 January 2020 · Exercise 3 · 0.8 p + 1.2 p"
    Let $x[n]$ be a random process whose auto-correlation is given by

    $$r_x[l] = \begin{cases} 1/21 & l = 0 \\ 2/105 & l = \pm 1 \\ 0 & \text{else} \end{cases}$$

    - (a) Determine and plot the correlogram power spectrum estimate. [0.8 pt]
    - (b) Assume that $x[n]$ can be modeled by an MA(1) random process. Determine and plot its spectrum estimate. How does this relate to the spectrum estimate obtained in 3(a)? Motivate your answer. [1.2 pt]

???+ solution "Solution"
    **(a)** $P_{corr}=\frac1{21}+\frac{4}{105}\cos\theta$: $\frac{9}{105}\approx0.086$ at $\theta=0$, $\frac1{105}\approx0.0095$ at $\pm\pi$ (low-pass).

    **(b)** $\frac{b}{1+b^2}=\frac{2/105}{1/21}=\frac25\Rightarrow2b^2-5b+2=0\Rightarrow b=\frac12$ (or 2, rejected). $\sigma_i^2=\frac{2/105}{1/2}=\frac4{105}$.

    $$P_{MA}=\frac4{105}\left|1+\tfrac12e^{-j\theta}\right|^2=\frac4{105}\left(\tfrac54+\cos\theta\right)=\frac1{21}+\frac4{105}\cos\theta.$$

    **Same curve.** The autocorrelation is zero beyond lag 1, which is exactly the MA(1) structure, and the MA(1) parameters reproduce $r[0]$ and $r[1]$ exactly. So both methods describe the same autocorrelation and give the same PSD.

    ![same curve](img/gen/p3_jan20.svg)

    !!! answer "Answer"
        (a) $\frac1{21}+\frac4{105}\cos\theta$. (b) $b=\frac12$, $\sigma_i^2=\frac4{105}$, identical PSD (the given $r$ is exactly an MA(1) autocorrelation).

### November 2019 exam · Exercise 2 {#nov19-2}

!!! exam "Written exam, 4 November 2019 · Exercise 2 · 1 p + 1 p"
    Let $x[n]$ be a random process whose correlation is estimated. The values for the first five lags are $r_x[0] = 1$, $r_x[\pm 1] = 0.7$, $r_x[\pm 2] = 0.5$, $r_x[\pm 3] = 0.3$, and $r_x[\pm 4] = 0$.

    - (a) Determine and plot the correlogram power spectrum estimate. [1 pt.]
    - (b) Assume that $x[n]$ is modeled by an AR(2) model. Determine and plot its spectrum estimate. [1 pt.]

???+ solution "Solution"
    **(a)** $P_{cor}=1+1.4\cos\theta+\cos2\theta+0.6\cos3\theta$; $4.0$ at $\theta=0$.

    **(b)** $\begin{cases}a_1+0.7a_2=-0.7\\0.7a_1+a_2=-0.5\end{cases}$, $\det=0.51$: $a_1=\frac{-0.7+0.35}{0.51}=-0.686$, $a_2=\frac{-0.5+0.49}{0.51}=-0.0196$.

    $\sigma_i^2=1+0.7a_1+0.5a_2=1-0.4804-0.0098=0.5098.$

    $$P_{AR2}=\frac{0.5098}{|1-0.686e^{-j\theta}-0.0196e^{-j2\theta}|^2},\qquad P_{AR2}(0)=\frac{0.5098}{0.294^2}\approx5.9.$$

    ![correlogram vs AR(2)](img/gen/p3_nov19.svg)

    !!! answer "Answer"
        (a) $1+1.4\cos\theta+\cos2\theta+0.6\cos3\theta$. (b) $a_1=-0.686$, $a_2=-0.0196$, $\sigma_i^2=0.510$ (the key prints 0.5089, a typo).

### January 2019 retake · Exercise 4 (Wiener filter) {#jan19-4}

!!! exam "Written exam, 21 January 2019 · Exercise 4 · 1.25 p + 1.25 p"
    In this exercise you need to design an optimal FIR Wiener filter with two coefficients $w_0$ and $w_1$ for the situation depicted in Figure 1, for which the following relationship holds $\hat{e}[k] = w[k] * h[k] * x[k] = w[k] * g[k]$.

    ![Figure 1](img/exam/jan19-4-wiener.jpg)

    The measured signal is AR(1) and can be described by the following difference equation: $x[k] = i[k] + \frac{1}{2}x[k-1]$. The innovation signal $i[k]$ is a white noise sequence with zero mean and variance $E\{i^2[k]\} = \sigma_i^2 = \frac{1}{4}$. The reference signal $e[k]$ has zero mean and variance $E\{e^2[k]\} = \sigma_e^2 = \frac{7}{3}$. This reference signal is correlated with the measured signal $x[k]$, which is expressed by the cross correlation $E\{e[k]x[k-\tau]\} = \rho_{ex}[\tau]$ from which we know the following values: $\rho_{ex}[0] = \frac{2}{3}$, $\rho_{ex}[1] = \frac{5}{6}$ and $\rho_{ex}[2] = \frac{5}{12}$.

    (a) Now we have $H(z) = 1$. Calculate the optimal coefficients $w_0$ en $w_1$ and the minimal error $J_{min}$. [1.25 pt.]

    (b) Now we have $H(z) = 1 - 2z^{-1}$. Do the same as in (a). Note that now $\hat{e}[k] = w[k] * h[k] * x[k] = w[k] * g[k]$, and the input-output cross correlation is $\rho_{eg}[\tau] = E\{e[k]g[k-\tau]\}$ [1.25 pt.]

???+ solution "Solution"
    **Reading the diagram:** a 2-tap FIR filter ($w_0$ on $x[k]$, $w_1$ on $x[k-1]$) followed by $H(z)$ tries to reproduce $e[k]$. The Wiener solution solves the **normal equations** $\mathbf R\mathbf w=\mathbf r_{e\cdot}$ and the error is $J_{min}=\sigma_e^2-\mathbf w^T\mathbf r_{e\cdot}$ (reader §13.1). This is old material (2019) and the reader now calls Wiener filtering "beyond the scope", except as the AR predictor.

    **Autocorrelation of $x$** (AR(1), $a=-\frac12$): $r_x[0]=\frac{\sigma_i^2}{1-1/4}=\frac13$, $r_x[1]=\frac16$, $r_x[2]=\frac1{12}$.

    **(a)** $\begin{bmatrix}\frac13&\frac16\\\frac16&\frac13\end{bmatrix}\begin{bmatrix}w_0\\w_1\end{bmatrix}=\begin{bmatrix}\frac23\\\frac56\end{bmatrix}\Rightarrow\begin{cases}2w_0+w_1=4\\w_0+2w_1=5\end{cases}\Rightarrow w_0=1,\ w_1=2.$

    $J_{min}=\frac73-\left(1\cdot\frac23+2\cdot\frac56\right)=0$.

    **(b)** Filter the input first: $g[k]=x[k]-2x[k-1]$.

    - $r_g[l]=5r_x[l]-2r_x[l-1]-2r_x[l+1]$: $r_g[0]=\frac53-\frac46=1$, $r_g[1]=\frac56-\frac23-\frac16=0$.
    - $\rho_{eg}[\tau]=\rho_{ex}[\tau]-2\rho_{ex}[\tau+1]$: $\rho_{eg}[0]=\frac23-\frac53=-1$, $\rho_{eg}[1]=\frac56-\frac56=0$.

    $\begin{bmatrix}1&0\\0&1\end{bmatrix}\mathbf w=\begin{bmatrix}-1\\0\end{bmatrix}\Rightarrow w_0=-1,\ w_1=0$, $\ J_{min}=\frac73-(-1)(-1)=\frac43$.

    !!! answer "Answer"
        (a) $w_0=1$, $w_1=2$, $J_{min}=0$. (b) $w_0=-1$, $w_1=0$, $J_{min}=\frac43$.
