# 3.2 AR and MA models from $r[k]$

<div class="meta"><span class="hot">AR in 7 of 9 exams</span><span>MA(1) in 3</span><span>1–1.5 points</span><span>35 min</span></div>

<figure class="pod"><video src="video/pod_ep2_spectral.mp4" poster="video/pod_ep2_spectral.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 2, Spectral: correlogram, AR, MA</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [3.1 Correlogram](e3-corr.md) first.

## What the exam asks

Same $r[0], r[1], r[2]$ as in 3.1, then: "**model the signal as an AR(1) / AR(2) process**: find the parameters and the PSD", and sometimes "**now as an MA(1)**". This is the biggest mechanical chunk of Part 3.

## The idea in one minute

A **model** is a recipe that makes the signal out of white noise $i[n]$ (pure randomness, flat spectrum, power $\sigma_i^2$):

| model | recipe | in words |
|---|---|---|
| AR(1) | $x[n]=-a_1x[n-1]+i[n]$ | today = a bit of yesterday + new noise |
| AR(2) | $x[n]=-a_1x[n-1]-a_2x[n-2]+i[n]$ | today = a bit of the last two days + noise |
| MA(1) | $x[n]=i[n]+b_1\,i[n-1]$ | today = today's noise + a bit of yesterday's noise |

(The minus signs in AR are the course's convention. Keep them, or every sign flips.)

**Fitting** = choosing the numbers $a_1, a_2, b_1, \sigma_i^2$ so the model has exactly the $r[k]$ you were given. Once you have them, the PSD comes from a fixed formula. For AR(1) it is $\dfrac{\sigma_i^2}{1+a_1^2+2a_1\cos\theta}$; play with $a_1$ (called $a$ below) to see what shape it makes:

<div class="widget" data-w="pole" data-a="0.8"></div>

## The recipes

!!! recipe key "AR(1)"

    $$a_1=-\frac{r[1]}{r[0]},\qquad \sigma_i^2=r[0]+a_1r[1],\qquad P_{AR}(e^{j\theta})=\frac{\sigma_i^2}{1+a_1^2+2a_1\cos\theta}.$$

!!! recipe key "AR(2): Yule–Walker"
    1. **Equations** (this is what "state the Yule–Walker equations in matrix form" wants):

    $$\begin{bmatrix}r[0]&r[1]\\ r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\ a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\ r[2]\end{bmatrix}$$

    2. **Solve** the 2×2 (with $D=r[0]^2-r[1]^2$):

    $$a_1=\frac{-r[1]\,(r[0]-r[2])}{D},\qquad a_2=\frac{r[1]^2-r[0]\,r[2]}{D}.$$

    3. **Noise power**: $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$.
    4. **PSD**: $P_{AR}=\dfrac{\sigma_i^2}{|A|^2}$ with

    $$|A|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos2\theta.$$

!!! recipe key "MA(1)"
    The model must give $r[0]=\sigma_i^2(1+b_1^2)$ and $r[1]=\sigma_i^2b_1$.
    1. Divide them: $\dfrac{1+b_1^2}{b_1}=\dfrac{r[0]}{r[1]}$ → a quadratic $b_1^2-\dfrac{r[0]}{r[1]}b_1+1=0$.
    2. It has two roots, $b$ and $1/b$: **keep the one with $|b_1|<1$**.
    3. $\sigma_i^2=r[1]/b_1$.
    4. PSD: $P_{MA}=r[0]+2r[1]\cos\theta$. (Yes: the correlogram cut after lag 1. You do not even need $b_1$ for it.)

??? idea "Where the $|A|^2$ formula comes from (only if you are curious)"
    $|A|^2=A\cdot\overline A=(1+a_1e^{-j\theta}+a_2e^{-2j\theta})(1+a_1e^{j\theta}+a_2e^{2j\theta})$. Multiply out and group: constants $1+a_1^2+a_2^2$; the $e^{\pm j\theta}$ terms give $(a_1+a_1a_2)(e^{j\theta}+e^{-j\theta})=2(a_1+a_1a_2)\cos\theta$; the $e^{\pm2j\theta}$ terms give $2a_2\cos2\theta$. For AR(1) set $a_2=0$: $1+a_1^2+2a_1\cos\theta$.

## Watch it once: June 2026 · 3d (AR(2))

!!! exam "Resit, June 2026 · 3d · 1 p"
    $r_x[0] = 3, \ r_x[1] = 2, \ r_x[2] = 1$. Model the process as AR(2): $x[n] = i[n] - a_1 x[n-1] - a_2 x[n-2]$, $i[n]$ zero-mean white noise with variance $\sigma_i^2$.
    - State the Yule-Walker equations in matrix form. [0.1]
    - Calculate $a_1$ and $a_2$. [0.4]
    - Calculate $\sigma_i^2$. [0.2]
    - Write $\hat{P}_{AR}(e^{j\theta})$ as a function of $\cos(\theta)$. [0.3]

<div class="stepper" markdown>

**Step 1 · Equations.**

$$\begin{bmatrix}3&2\\2&3\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}2\\1\end{bmatrix}$$

***

**Step 2 · Solve.** $D=3^2-2^2=5$.
$a_1=\dfrac{-2\,(3-1)}{5}=-\dfrac45$, $\quad a_2=\dfrac{2^2-3\cdot1}{5}=\dfrac15$.
Check in the first row: $3(-\frac45)+2(\frac15)=-\frac{12}5+\frac25=-2$ ✓.

***

**Step 3 · Noise power.** $\sigma_i^2=3+(-\frac45)(2)+(\frac15)(1)=3-\frac85+\frac15=\dfrac85$.

***

**Step 4 · $|A|^2$.**
Constant: $1+\frac{16}{25}+\frac1{25}=\frac{42}{25}$.
$\cos\theta$: $2(a_1+a_1a_2)=2(-\frac45-\frac4{25})=-\frac{48}{25}$.
$\cos2\theta$: $2a_2=\frac25=\frac{10}{25}$.
So $|A|^2=\frac{42-48\cos\theta+10\cos2\theta}{25}$.

***

**Step 5 · PSD.** $P_{AR}=\dfrac{8/5}{|A|^2}=\dfrac{40}{42-48\cos\theta+10\cos2\theta}=\dfrac{20}{21-24\cos\theta+5\cos2\theta}$.
With $\cos2\theta=2\cos^2\theta-1$ (only $\cos\theta$ left): $\dfrac{10}{5\cos^2\theta-12\cos\theta+8}$.

</div>

## Watch it once more: April 2025 · 3e, 3f (AR(1) and MA(1))

!!! exam "Final exam, 13 April 2025 · 3e (0.5 p), 3f (0.5 p)"
    $r[0] = 2, \quad r[\pm 1] = -\frac{1}{4}, \quad r[\pm 2] = -\frac{3}{16}$.
    **3e** Model the signal as an AR(1) process, find the parameters and the PSD $P_{AR}(e^{j\theta})$ as a function of cosines.
    **3f** Model the signal as an MA(1) process, find the parameters and the PSD $P_{MA}(e^{j\theta})$ as a function of cosines.

<div class="stepper" markdown>

**Step 1 · AR(1) coefficient.** $a_1=-\dfrac{r[1]}{r[0]}=-\dfrac{-1/4}{2}=\dfrac18$.

***

**Step 2 · AR(1) noise power.** $\sigma_i^2=r[0]+a_1r[1]=2+\frac18(-\frac14)=2-\frac1{32}=\dfrac{63}{32}$.

***

**Step 3 · AR(1) PSD.** $1+a_1^2+2a_1\cos\theta=1+\frac1{64}+\frac14\cos\theta=\frac{65+16\cos\theta}{64}$.
$P_{AR}=\dfrac{63/32}{(65+16\cos\theta)/64}=\dfrac{126}{65+16\cos\theta}$.

***

**Step 4 · MA(1) coefficient.** $\dfrac{r[0]}{r[1]}=\dfrac{2}{-1/4}=-8$, so $b_1^2+8b_1+1=0$, $b_1=\dfrac{-8\pm\sqrt{64-4}}{2}=-4\pm\sqrt{15}$.
That is $-0.127$ or $-7.87$. Keep $|b_1|<1$: $b_1\approx-0.127$.

***

**Step 5 · MA(1) noise and PSD.** $\sigma_i^2=r[1]/b_1=\frac{-0.25}{-0.127}\approx1.97$.
$P_{MA}=r[0]+2r[1]\cos\theta=2-0.5\cos\theta$.

</div>

## Your turn

!!! exam "Final exam, 7 November 2022 · 3f, 3g · 0.75 p each"
    A process has $r[0]=1$, $r[1]=-\frac18$, $r[2]=-\frac{3}{32}$.
    **3f** Model $x[k]$ as an AR(1) signal and calculate $P_{AR1}(e^{j\theta})$.
    **3g** Model $x[k]$ as an MA(1) signal and calculate $P_{MA1}(e^{j\theta})$. Decimal numbers are fine.

??? solution "Check your answer"
    **AR(1).** $a_1=-\frac{-1/8}{1}=\frac18$; $\sigma_i^2=1+\frac18(-\frac18)=\frac{63}{64}$; denominator $1+\frac1{64}+\frac14\cos\theta=\frac{65+16\cos\theta}{64}$.

    **MA(1).** $\frac{r[0]}{r[1]}=-8$ again, so $b_1\approx-0.127$; $\sigma_i^2=\frac{-0.125}{-0.127}\approx0.98$; $P=1+2(-\frac18)\cos\theta$.

    !!! answer "Answer"
        $P_{AR1}=\dfrac{63}{65+16\cos\theta}$; $\quad P_{MA1}\approx1-0.25\cos\theta$ ($b_1\approx-0.13$, $\sigma_i^2\approx0.98$).

!!! exam "Final exam, April 2024 · 3e · 0.7 p"
    $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$. Model the signal as an AR(2) process. Find the model parameters.

??? solution "Check your answer"
    $D=\frac{625}{256}-\frac{9}{16}=\frac{625-144}{256}=\frac{481}{256}$.
    $a_1=\frac{-(-\frac34)(\frac{25}{16}-\frac12)}{D}=\frac{\frac34\cdot\frac{17}{16}}{481/256}=\frac{51/64}{481/256}=\frac{204}{481}$.
    $a_2=\frac{\frac9{16}-\frac{25}{16}\cdot\frac12}{D}=\frac{\frac{18-25}{32}}{481/256}=\frac{-7/32}{481/256}=-\frac{56}{481}$.
    $\sigma_i^2=\frac{25}{16}+\frac{204}{481}(-\frac34)+(-\frac{56}{481})(\frac12)\approx1.5625-0.3181-0.0582=1.19$.

    !!! answer "Answer"
        $a_1=\frac{204}{481}\approx0.424$, $a_2=-\frac{56}{481}\approx-0.116$, $\sigma_i^2\approx1.19$.

## Traps

!!! trap key "Where points are lost"
    - **Sign of $a$**: with the course convention $x[n]=-a_1x[n-1]+\dots$, $a_1=-r[1]/r[0]$. A positive $r[1]$ gives a negative $a_1$.
    - The minus on the right of Yule–Walker: $\mathbf R\mathbf a=-\mathbf r$.
    - $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$ uses **plus** signs (with the $a$'s you found, signs included).
    - MA(1): keep the root **inside** the unit circle, $|b_1|<1$.
