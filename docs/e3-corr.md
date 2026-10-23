# 3.1 Correlogram and "pick the plot"

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>0.4–0.5 p, +0.25 for the plot</span><span>20 min</span></div>

<figure class="pod"><video src="video/pod_ep2_spectral.mp4" poster="video/pod_ep2_spectral.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 2, Spectral: correlogram, AR, MA</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

"Here are a few autocorrelation values $r[0]$, $r[\pm1]$, $r[\pm2]$. Compute the **correlogram** estimate of the power spectral density, as a function of cosines." Then often: "which plot shows your PSD?" This is the easiest half point of the exam.

## The idea in one minute

Two words first:

- **Autocorrelation** $r[k]$: how much the signal looks like itself shifted by $k$ samples. $r[0]$ is its power. $r[-k]=r[k]$ always.
- **PSD** (power spectral density) $P(e^{j\theta})$: how the power is spread over frequency $\theta$, from $\theta=0$ (slow, constant) to $\theta=\pi$ (fastest possible: $+,-,+,-$).

The correlogram is just "add up the $r[k]$ as waves":

$$P(e^{j\theta})=\sum_k r[k]\,e^{-jk\theta}.$$

Each pair $\pm k$ gives $r[k]e^{-jk\theta}+r[k]e^{jk\theta}=2r[k]\cos k\theta$ (because $e^{ju}+e^{-ju}=2\cos u$). So:

<div class="key" markdown>

$$\hat P_{corr}(e^{j\theta})=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta+\dots$$

</div>

Watch it being built term by term (June 2026 numbers):

<div class="widget" data-w="corr" data-preset="jun26"></div>

## The recipe

!!! recipe key "Correlogram + pick the plot"
    1. Write $r[0]+2r[1]\cos\theta+2r[2]\cos2\theta$ (one term per given lag, **$r[0]$ not doubled**).
    2. Plug in the numbers. That is the answer: "a function of cosines".
    3. **Pick the plot**: evaluate at the two ends. $\theta=0$: every $\cos=1$, so $P(0)=r[0]+2r[1]+2r[2]$. $\theta=\pi$: $\cos\pi=-1$, $\cos2\pi=+1$, so $P(\pi)=r[0]-2r[1]+2r[2]$. Find the plot with those end values.

## Watch it once: June 2026 · 3c

!!! exam "Resit, June 2026 · 3c · 0.5 p"
    A WSS, real-valued random process $x[n]$ has estimated autocorrelation values $r_x[0] = 3, \ r_x[1] = 2, \ r_x[2] = 1$. Calculate the non-parametric correlogram estimate $\hat{P}_{Corr}(e^{j\theta})$ using only the given lags (assume $r_x[k] = 0$ for $|k| > 2$), as a function of $\cos(\theta)$.

<div class="stepper" markdown>

**Step 1 · Template.** $\hat P=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta$.

***

**Step 2 · Numbers.** $\hat P=3+2\cdot2\cos\theta+2\cdot1\cos2\theta=\mathbf{3+4\cos\theta+2\cos2\theta}$.

***

**Step 3 · Only if they insist on "function of $\cos\theta$" only.** Use $\cos2\theta=2\cos^2\theta-1$: $3+4\cos\theta+4\cos^2\theta-2=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$. Both forms are correct.

***

**Step 4 · Sanity check.** $P(0)=3+4+2=9$ and $P(\pi)=3-4+2=1$. A PSD can never be negative: $(2\cos\theta+1)^2\ge0$ ✓.

</div>

## Your turn

!!! exam "Final exam, 13 April 2025 · 3d (0.5 p) and 3g (0.25 p)"
    $r[0] = 2, \quad r[\pm 1] = -\frac{1}{4}, \quad r[\pm 2] = -\frac{3}{16}$.
    **3d** Use the correlogram method to calculate the PSD. Express $P_{corr}(e^{j\theta})$ as a function of cosines.
    **3g** (after also fitting AR(1) and MA(1), see [3.2](e3-arma.md)) Which plot shows the correct PSDs?
    ![Plots A–D](img/exam/apr25-3g.jpg)
    (a) Plot D (b) Plot C (c) Plot B (d) Plot A

??? solution "Check your answer"
    $P_{corr}=2+2(-\frac14)\cos\theta+2(-\frac3{16})\cos2\theta=2-\frac12\cos\theta-\frac38\cos2\theta$.
    Ends: $P(0)=2-0.5-0.375=1.125$, $P(\pi)=2+0.5-0.375=2.125$. So it **rises** from about 1.1 to about 2.1. The AR(1) and MA(1) fits of 3.2 also rise (1.56 → 2.57 and 1.5 → 2.5). Press play below to see all three.

    <div class="widget" data-w="corr" data-preset="apr25"></div>

    !!! answer "Answer"
        3d: $P_{corr}=2-\frac12\cos\theta-\frac38\cos2\theta$. 3g: the plot where all three curves rise with those end values: **(a) Plot D**.

!!! exam "Final exam, April 2024 · 3d · 0.4 p"
    $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$, $r[\pm3]=-\frac12$. Using the correlogram method, give an estimate of the PSD as a function of cosines.

??? solution "Check your answer"
    Four lags, so four terms: $\frac{25}{16}+2(-\frac34)\cos\theta+2(\frac12)\cos2\theta+2(-\frac12)\cos3\theta$.

    !!! answer "Answer"
        $P_{corr}=\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$.

## Traps

!!! trap key "Where points are lost"
    - Doubling $r[0]$. Only the $\pm k$ pairs get the 2.
    - Forgetting the 2 on the others ($r[1]\cos\theta$ instead of $2r[1]\cos\theta$).
    - Writing $\cos^2\theta$ when you mean $\cos2\theta$. They are different things.
    - For the plot: check both ends, not just one. Curves that look alike at $\theta=0$ often differ at $\pi$.
