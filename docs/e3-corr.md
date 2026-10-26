# 3.1 Correlogram and "pick the plot"

<div class="meta"><span class="hot">In 7 of 9 exams</span><span>0.4–0.5 p, +0.25 for the plot</span><span>20 min</span></div>

<figure class="pod"><video src="video/pod_ep2_spectral.mp4" poster="video/pod_ep2_spectral.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 2, Spectral: correlogram, AR, MA</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

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

## How to fight this section with the sheet

The exam gives numbers $r[0],r[1],r[2],\dots$ and says **"correlogram"**, **"only these lags"**, **"PSD as a function of $\cos\theta$"** → you open **box 3A** on your A4 sheet: one formula line and two of the exams below already computed. Then **"which plot"** → the **Draw it** line at the top of the Part 3 band: evaluate the curve at $\theta=0$ and $\theta=\pi$ and match the two heights.

!!! sheet "Box 3A + the Part 3 header lines, exactly as printed on the sheet"
    $r[k]$ = autocorrelation at lag $k$ (the given numbers). Rewrite cosines: $\cos2\theta=2\cos^2\theta-1$, $\cos3\theta=4\cos^3\theta-3\cos\theta$, $\cos\alpha\cos\beta=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2$ (to expand $\lvert L\rvert^2$).

    **Draw it** — the question says "determine **and plot**", only the numbers are graded: $r[k]$ → vertical **stems** at the lags. $P(\theta)$ → compute the value at $\theta=0$ and at $\theta=\pi$, draw **one smooth curve** through those two heights and write them on the axis. Peak at $0$ = low-pass, peak at $\pi$ = high-pass, peak in between = band-pass.

    ### 3A · Correlogram

    IF YOU SEE $r[0],r[1],r[2]\dots$ + "correlogram", "only these lags", "PSD as a function of $\cos\theta$", correlation values given

    $P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta$. Stop at the last lag given. $r[0]$ is NOT doubled. From data: $\hat r[k]=\frac1N\sum_n x[n]x[n-k]$.

    *Jun26* $3,2,1$: $3+4\cos\theta+2\cos2\theta=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$.

    *Apr24* $\frac{25}{16},-\frac34,\frac12,-\frac12$: $\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$.

## 1 · June 2026 · 3c — three lags (the sheet works this one out)

!!! exam "Resit Q4, June 2026 · 3c · 0.5 p"
    Consider a wide-sense stationary, real-valued random process $x[n]$ whose first three autocorrelation values have been estimated as:

    $$r_x[0] = 3, \quad r_x[1] = 2, \quad r_x[2] = 1$$

    Calculate the non-parametric correlogram estimate of the power spectral density, $\hat{P}_{Corr}(e^{j\theta})$, using only the given autocorrelation lags. Assume $r_x[k] = 0$ for $|k| > 2$. Derive $\hat{P}_{Corr}(e^{j\theta})$ as a function of $\cos(\theta)$.

!!! sheet "In the cheat sheet: box 3A — the *Jun26* line is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · write the formula line.**
    *"$P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+2r[3]\cos3\theta$. Stop at the last lag given."* The last given lag is 2 → stop after the $\cos2\theta$ term. *"$r[0]$ is NOT doubled."*

    ***

    **Sheet step 2 · plug in.**
    $3+2\cdot2\cos\theta+2\cdot1\cos2\theta=3+4\cos\theta+2\cos2\theta$ — the sheet's *Jun26* line starts exactly like this.

    ***

    **Sheet step 3 · the second form (because they said "as a function of $\cos\theta$").**
    The header line gives the rewrite: *"$\cos2\theta=2\cos^2\theta-1$"* → $3+4\cos\theta+2(2\cos^2\theta-1)=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$. The sheet prints this whole chain.

    ***

    **Sheet check · the example line.**
    *"$3+4\cos\theta+2\cos2\theta=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2$."* Both forms are accepted; the sheet gives both.

    </div>

!!! answer "Answer"
    $\hat P_{Corr}=3+4\cos\theta+2\cos2\theta$ $\;(=4\cos^2\theta+4\cos\theta+1=(2\cos\theta+1)^2)$

## 2 · April 2025 · 3d and 3g — correlogram + pick the plot

!!! exam "Final exam Q3, 13 April 2025 · 3d (0.5 p), 3g (0.25 p)"
    Suppose you have an estimate of the autocorrelation function of a random signal at lags $0, \pm 1, \pm 2$ as: $r[0] = 2, \quad r[\pm 1] = -\frac{1}{4}, \quad r[\pm 2] = -\frac{3}{16}$

    **3d** Use the correlogram method to calculate the power spectral density in a non-parametric fashion. Express the obtained power spectral density $P_{corr}(e^{j\theta})$ as a function of cosines.

    **3g** Given the plots in the figure below, which option represents the correct power spectral densities, as found in 3d, 3e, and 3f?

    ![Plots A–D](img/exam/apr25-3g.jpg)

    - (a) Plot D
    - (b) Plot C
    - (c) Plot B
    - (d) Plot A

!!! sheet "In the cheat sheet: box 3A's formula line + the Draw it line of the Part 3 header"
    <div class="stepper" markdown>

    **Sheet step 1 · 3d: the formula line.**
    $r[0]+2r[1]\cos\theta+2r[2]\cos2\theta$ with the numbers: $2+2(-\frac14)\cos\theta+2(-\frac{3}{16})\cos2\theta=2-\frac12\cos\theta-\frac38\cos2\theta$.

    ***

    **Sheet step 2 · 3g: the Draw it line.**
    *"$P(\theta)$ → compute the value at $\theta=0$ and at $\theta=\pi$."* At $\theta=0$ every cosine is $1$: $P(0)=2-\frac12-\frac38=1.125$. At $\theta=\pi$: $\cos\pi=-1$, $\cos2\pi=+1$ (the header's rewrite: $\cos2\theta$ at $\theta=\pi$ is $\cos2\pi=1$): $P(\pi)=2+\frac12-\frac38=2.125$.

    ***

    **Sheet step 3 · match the two heights.**
    *"draw one smooth curve through those two heights"* — the correlogram curve **rises** from ≈1.1 to ≈2.1. The AR(1) and MA(1) fits of the same numbers (3e/3f, [3.2](e3-arma.md)) also rise ($1.56\to2.57$ and $1.5\to2.5$). The right plot is the one whose three curves end at those heights:

    <div class="widget" data-w="corr" data-preset="apr25"></div>

    ***

    **Sheet check · the shape words.**
    *"Peak at $0$ = low-pass, peak at $\pi$ = high-pass."* All three curves here are higher at $\pi$ → high-pass-ish shapes; a plot showing them flat or falling cannot be right.

    </div>

!!! answer "Answer"
    3d: $P_{corr}=2-\frac12\cos\theta-\frac38\cos2\theta$. 3g: **(a) Plot D** (all three curves rise to ≈2.1 at $\pi$).

## 3 · April 2024 · 3d — four lags

!!! exam "Final exam Q3, April 2024 · 3d · 0.4 p"
    *(Signal from 3b/3c: $x[n]=i[n]-\frac12i[n-1]+\frac14i[n-2]-\frac12i[n-3]$, so $r[0]=\frac{25}{16}$, $r[\pm1]=-\frac34$, $r[\pm2]=\frac12$, $r[\pm3]=-\frac12$.)*

    Using the correlogram method, give an estimate of the PSD as a function of cosines.

!!! sheet "In the cheat sheet: box 3A — the *Apr24* line is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · formula, all four lags.**
    The formula line ends at $+2r[3]\cos3\theta$ and says *"Stop at the last lag given"* — here the last lag is 3, so use every term.

    ***

    **Sheet step 2 · plug in.**
    $\frac{25}{16}+2(-\frac34)\cos\theta+2(\frac12)\cos2\theta+2(-\frac12)\cos3\theta=\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$.

    ***

    **Sheet check · the example line.**
    *"$\frac{25}{16},-\frac34,\frac12,-\frac12$: $\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$."* The sheet prints this exam's answer as its example.

    ***

    **Sheet step 3 · if they also say "and plot".**
    The Draw it line: $r[k]$ → *"vertical stems at the lags"* ($\frac{25}{16},-\frac34,\frac12,-\frac12$ at $k=0,\pm1,\pm2,\pm3$), and for $P(\theta)$: $P(0)=\frac{25}{16}-\frac32+1-1=\frac1{16}$, $P(\pi)=\frac{25}{16}+\frac32+1+1=\frac{81}{16}$ — one smooth curve through those two heights.

    </div>

!!! answer "Answer"
    $P_{corr}=\frac{25}{16}-\frac32\cos\theta+\cos2\theta-\cos3\theta$ (end values $\frac1{16}$ at $0$, $\frac{81}{16}$ at $\pi$).

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - Doubling $r[0]$. The formula line says *"$r[0]$ is NOT doubled"* — only the $\pm k$ pairs get the 2.
    - Forgetting the 2 on the others ($r[1]\cos\theta$ instead of $2r[1]\cos\theta$). Read the formula line, not your memory.
    - Not stopping at the last given lag — extra terms you invent are wrong (*"Stop at the last lag given"*).
    - Writing $\cos^2\theta$ when you mean $\cos2\theta$. The header's rewrite list is one-directional: $\cos2\theta=2\cos^2\theta-1$.
    - For the plot: check **both** ends (the Draw it line computes both $\theta=0$ and $\theta=\pi$). Curves that look alike at $0$ often differ at $\pi$.
    - Drawing a smooth histogram-like sketch of $r[k]$ instead of *"vertical stems at the lags"* — if the question says "plot $r[k]$", it is stems.
