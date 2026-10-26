# 3.2 AR and MA models from $r[k]$

<div class="meta"><span class="hot">AR in 7 of 9 exams</span><span>MA(1) in 3</span><span>1–1.5 points</span><span>35 min</span></div>

<figure class="pod"><video src="video/pod_ep2_spectral.mp4" poster="video/pod_ep2_spectral.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 2, Spectral: correlogram, AR, MA</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

Needs [3.1 Correlogram](e3-corr.md) first.

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

## How to fight this section with the sheet

The exam gives $r[0], r[1], r[2]$ and says **"AR(1)"** / **"AR(2)"** / **"Yule–Walker"** / **"MA(1)"** → you open **boxes 3B, 3C, 3D** on your A4 sheet: one box per model, numbered steps, and each box ends with an example from a real exam already computed. The exam words pick the box: "first-order autoregressive" = 3B, "Yule–Walker" = 3C, "moving average" = 3D.

!!! sheet "Boxes 3B, 3C, 3D, exactly as printed on the sheet"
    ### 3B · AR(1)

    IF YOU SEE "AR(1)", "first-order autoregressive"

    1. $a=-\dfrac{r[1]}{r[0]}$
    2. $\sigma^2=r[0]+a\,r[1]$
    3. $P=\dfrac{\sigma^2}{1+a^2+2a\cos\theta}$ (check $|a|\lt1$ and $\sigma^2\gt0$, else a sign went wrong)

    *Apr25* $r=2,-\frac14$: $a=\frac18$, $\sigma^2=\frac{63}{32}$, $P=\frac{126}{65+16\cos\theta}$.

    ### 3C · AR(2) / Yule–Walker

    IF YOU SEE "AR(2)", "Yule–Walker", $r[0],r[1],r[2]$

    1. $D=r[0]^2-r[1]^2$
    2. $a_1=\dfrac{-r[1]\,(r[0]-r[2])}{D}$,  $a_2=\dfrac{r[1]^2-r[0]\,r[2]}{D}$
    3. $\sigma^2=r[0]+a_1r[1]+a_2r[2]$
    4. $P=\dfrac{\sigma^2}{1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta}$

    If they want the matrix: $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$.

    *Jun26* $3,2,1$: $D=5$, $a_1=-\frac45$, $a_2=\frac15$, $\sigma^2=\frac85$, $P=\frac{10}{5\cos^2\theta-12\cos\theta+8}$.

    ### 3D · MA(1)

    IF YOU SEE "MA(1)", "moving average"

    PSD: $P=r[0]+2r[1]\cos\theta$. Ignore $r[2]$ and beyond.
    If they ask for $b$ and $\sigma^2$: solve $b^2-\frac{r[0]}{r[1]}\,b+1=0$, keep the root between $-1$ and $1$; then $\sigma^2=\frac{r[1]}{b}$.

    *Apr25* $r=2,-\frac14$: $P=2-\frac12\cos\theta$.

## 1 · April 2025 · 3e, 3f — AR(1) and MA(1), both examples on the sheet

!!! exam "Final exam Q3, 13 April 2025 · 3e (0.5 p), 3f (0.5 p)"
    Suppose you have an estimate of the autocorrelation function of a random signal at lags $0, \pm 1, \pm 2$ as: $r[0] = 2, \quad r[\pm 1] = -\frac{1}{4}, \quad r[\pm 2] = -\frac{3}{16}$

    **3e** Model the signal as an AR(1) process, find the parameters of the model, and calculate the corresponding power spectral density in a parametric fashion. Express the obtained power spectral density $P_{AR}(e^{j\theta})$ as a function of cosines.

    **3f** Model the signal as an MA(1) process, find the parameters of the model, and calculate the corresponding power spectral density in a parametric fashion. Express the obtained power spectral density $P_{MA}(e^{j\theta})$ as a function of cosines.

!!! sheet "In the cheat sheet: box 3B (its *Apr25* line) and box 3D (its *Apr25* line) — this exam IS both examples"
    <div class="stepper" markdown>

    **Sheet step 1 · 3e = box 3B's three steps.**
    Step 1: $a=-\frac{r[1]}{r[0]}=-\frac{-1/4}{2}=\frac18$. Step 2: $\sigma^2=r[0]+a\,r[1]=2+\frac18(-\frac14)=\frac{63}{32}$. Step 3: $P=\frac{\sigma^2}{1+a^2+2a\cos\theta}=\frac{63/32}{(65+16\cos\theta)/64}=\frac{126}{65+16\cos\theta}$. The sheet's example line: *"$a=\frac18$, $\sigma^2=\frac{63}{32}$, $P=\frac{126}{65+16\cos\theta}$."*

    ***

    **Sheet step 2 · 3f = box 3D's PSD line.**
    *"PSD: $P=r[0]+2r[1]\cos\theta$. Ignore $r[2]$ and beyond."* → $P=2+2(-\frac14)\cos\theta=2-\frac12\cos\theta$. The sheet's example line: *"$P=2-\frac12\cos\theta$."* (For the PSD you don't even need $b$.)

    ***

    **Sheet step 3 · 3f parameters, only because they ask.**
    *"$b^2-\frac{r[0]}{r[1]}\,b+1=0$, keep the root between $-1$ and $1$"*: $\frac{r[0]}{r[1]}=-8$ → $b^2+8b+1=0$ → $b=-4\pm\sqrt{15}$ = $-0.127$ or $-7.87$ → keep $b\approx-0.127$. Then $\sigma^2=\frac{r[1]}{b}=\frac{-0.25}{-0.127}\approx1.97$.

    ***

    **Sheet check · the example lines.**
    Both *Apr25* lines under the boxes are this exam. The sheet's numbers ($\frac18$, $\frac{63}{32}$, $\frac{126}{65+16\cos\theta}$, $2-\frac12\cos\theta$) are the graded answers.

    </div>

!!! answer "Answer"
    3e: $a_1=\frac18$, $\sigma_i^2=\frac{63}{32}$, $P_{AR}=\dfrac{126}{65+16\cos\theta}$. 3f: $P_{MA}=2-\frac12\cos\theta$ ($b_1\approx-0.13$, $\sigma_i^2\approx1.97$).

## 2 · June 2026 · 3d — AR(2) / Yule–Walker

!!! exam "Resit Q4, June 2026 · 3d · 1 p"
    Consider a wide-sense stationary, real-valued random process $x[n]$ with $r_x[0] = 3, \ r_x[1] = 2, \ r_x[2] = 1$. You now wish to model this process parametrically using an Autoregressive (AR) model of order $p = 2$:

    $$x[n] = i[n] - a_1 x[n-1] - a_2 x[n-2]$$

    where $i[n]$ is zero-mean white noise with variance $\sigma_i^2$.

    - State the Yule-Walker equations for this AR(2) process in matrix form. [0.1]
    - Calculate the AR coefficients $a_1$ and $a_2$. [0.4]
    - Calculate the variance of the driving white noise $\sigma_i^2$. [0.2]
    - Write $\hat{P}_{AR}(e^{j\theta})$ as a function of $\cos(\theta)$. [0.3]

!!! sheet "In the cheat sheet: box 3C — the *Jun26* line is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · the matrix (the box prints it).**
    $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$ → $\begin{bmatrix}3&2\\2&3\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}2\\1\end{bmatrix}$. 0.1 p for copying it with the numbers.

    ***

    **Sheet step 2 · the two formulas (step 1–2 of the box).**
    $D=r[0]^2-r[1]^2=9-4=5$ — the sheet's example line: *"$D=5$"*. $a_1=\frac{-r[1](r[0]-r[2])}{D}=\frac{-2\cdot2}{5}=-\frac45$, $a_2=\frac{r[1]^2-r[0]r[2]}{D}=\frac{4-3}{5}=\frac15$.

    ***

    **Sheet step 3 · noise power (step 3 of the box).**
    $\sigma^2=r[0]+a_1r[1]+a_2r[2]=3+(-\frac45)(2)+(\frac15)(1)=\frac85$ — again the sheet's line.

    ***

    **Sheet step 4 · the PSD (step 4 of the box).**
    $P=\dfrac{\sigma^2}{1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta}$. With the numbers: denominator $=\frac{42-48\cos\theta+10\cos2\theta}{25}$, so $P=\frac{40}{42-48\cos\theta+10\cos2\theta}$. Only $\cos\theta$ wanted? The Part 3 header's rewrite *"$\cos2\theta=2\cos^2\theta-1$"* gives $P=\frac{10}{5\cos^2\theta-12\cos\theta+8}$ — the sheet's example line ends there.

    ***

    **Sheet check · the example line.**
    *"$D=5$, $a_1=-\frac45$, $a_2=\frac15$, $\sigma^2=\frac85$, $P=\frac{10}{5\cos^2\theta-12\cos\theta+8}$."* Four graded answers, all printed.

    </div>

!!! answer "Answer"
    Matrix as above; $a_1=-\frac45$, $a_2=\frac15$, $\sigma_i^2=\frac85$, $P_{AR}=\dfrac{10}{5\cos^2\theta-12\cos\theta+8}$ (equivalently $\dfrac{20}{21-24\cos\theta+5\cos2\theta}$).

## 3 · November 2022 · 3f, 3g — AR(1) then MA(1), no printed example

!!! exam "Final exam, 7 November 2022 · 3f, 3g · 0.75 p each"
    A process has $r[0]=1$, $r[1]=-\frac18$, $r[2]=-\frac{3}{32}$.

    **3f** Model $x[k]$ as an AR(1) signal and calculate $P_{AR1}(e^{j\theta})$.

    **3g** Model $x[k]$ as an MA(1) signal and calculate $P_{MA1}(e^{j\theta})$. Decimal numbers are fine.

!!! sheet "In the cheat sheet: boxes 3B and 3D, run the steps on these numbers"
    <div class="stepper" markdown>

    **Sheet step 1 · 3f = box 3B.**
    $a=-\frac{r[1]}{r[0]}=-\frac{-1/8}{1}=\frac18$. $\sigma^2=r[0]+a\,r[1]=1+\frac18(-\frac18)=\frac{63}{64}$. $P=\frac{\sigma^2}{1+a^2+2a\cos\theta}=\frac{63/64}{(65+16\cos\theta)/64}=\frac{63}{65+16\cos\theta}$.

    ***

    **Sheet step 2 · 3f check (box 3B step 3's parenthetical).**
    *"check $|a|<1$ and $\sigma^2>0$, else a sign went wrong"*: $\frac18<1$ ✓, $\frac{63}{64}>0$ ✓.

    ***

    **Sheet step 3 · 3g PSD = box 3D's first line.**
    *"PSD: $P=r[0]+2r[1]\cos\theta$. Ignore $r[2]$ and beyond."* → $1+2(-\frac18)\cos\theta=1-\frac14\cos\theta$.

    ***

    **Sheet step 4 · 3g parameters (they ask for the model).**
    $b^2-\frac{r[0]}{r[1]}b+1=0$: $\frac{1}{-1/8}=-8$ → $b^2+8b+1=0$ → $b=-4\pm\sqrt{15}$ → *keep the root between $-1$ and $1$"* → $b\approx-0.127$. $\sigma^2=\frac{r[1]}{b}=\frac{-0.125}{-0.127}\approx0.98$.

    ***

    **Sheet check · the example line.**
    Same boxes, same steps as Apr25 — only the numbers changed. If your method differs from the sheet's four steps, stop and realign.

    </div>

!!! answer "Answer"
    $P_{AR1}=\dfrac{63}{65+16\cos\theta}$; $P_{MA1}=1-\frac14\cos\theta$ ($b_1\approx-0.13$, $\sigma_i^2\approx0.98$).

## 4 · April 2024 · 3e — AR(2) with ugly fractions

!!! exam "Final exam Q3, April 2024 · 3e · 0.7 p"
    *(from 3b/3c: $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$.)* Model the signal as an AR(2) process. Find the model parameters.

!!! sheet "In the cheat sheet: box 3C, steps 1–3 (no PSD asked)"
    <div class="stepper" markdown>

    **Sheet step 1 · $D=r[0]^2-r[1]^2$.**
    $\frac{625}{256}-\frac{9}{16}=\frac{625-144}{256}=\frac{481}{256}$.

    ***

    **Sheet step 2 · the two formulas.**
    $a_1=\frac{-r[1](r[0]-r[2])}{D}=\frac{\frac34\cdot\frac{17}{16}}{481/256}=\frac{204}{481}\approx0.424$, $a_2=\frac{r[1]^2-r[0]r[2]}{D}=\frac{\frac{9}{16}-\frac{25}{32}}{481/256}=-\frac{56}{481}\approx-0.116$.

    ***

    **Sheet step 3 · $\sigma^2=r[0]+a_1r[1]+a_2r[2]$** $=1.5625+0.424(-0.75)+(-0.116)(0.5)\approx1.19$.

    ***

    **Sheet check · the example line.**
    The box's *Jun26* line is the same computation with friendlier numbers; the steps never change. Sanity check row 1 of the matrix: $\frac{25}{16}a_1-\frac34a_2=\frac34$ ✓.

    </div>

!!! answer "Answer"
    $a_1=\frac{204}{481}\approx0.424$, $a_2=-\frac{56}{481}\approx-0.116$, $\sigma_i^2\approx1.19$.

## Traps

!!! trap key "Where points are lost (each one is a step of the sheet you skipped)"
    - **Sign of $a$**: box 3B step 1 is $a=-\frac{r[1]}{r[0]}$ with the minus built in. A positive $r[1]$ gives a negative $a_1$. If you drop the minus, every later number flips.
    - The minus on the right of the Yule–Walker matrix (box 3C): $\mathbf R\mathbf a=-\mathbf r$. The matrix is worth 0.1 p — copy it from the sheet with the numbers in.
    - $\sigma^2=r[0]+a_1r[1]+a_2r[2]$ uses **plus** signs (box 3C step 3) — with the $a$'s you found, their own signs included.
    - MA(1): keeping the root outside the circle. Box 3D: *"keep the root between $-1$ and $1$"* — same rule as spectral factorisation.
    - Forgetting the box's own check: *"check $|a|<1$ and $\sigma^2>0$, else a sign went wrong"* (3B step 3).
    - Using $r[2]$ in the MA(1) PSD: box 3D says *"Ignore $r[2]$ and beyond"*.
    - Writing the AR(2) denominator from memory: box 3C step 4 has $2a_1(1+a_2)\cos\theta+2a_2\cos2\theta$ — the $(1+a_2)$ factor is easy to lose.
