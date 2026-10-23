# 1.4 Spectral factorisation

<div class="meta"><span class="hot">In 5 of the last 5 exams</span><span>0.25–0.75 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

"A random signal has PSD $P_x(e^{j\theta})=\dfrac{N}{A+B\cos\theta}$. Find the **innovation filter** $L(z)$ and the **noise variance** $\sigma_i^2$." Every time, the same shape. Sometimes also an MC: "the innovation filter must be **minimum phase**".

## The idea in one minute

- **White noise** $i[n]$: pure randomness, the same power $\sigma_i^2$ at every frequency (flat PSD).
- Pass it through a filter $L(z)$ and the output has PSD $\sigma_i^2\,|L(e^{j\theta})|^2$: the filter shapes the flat spectrum.
- **Spectral factorisation** = go backwards: from the PSD, find the filter and the noise power that made it.

For the exam the filter is always $L(z)=\dfrac{1}{1+a\,z^{-1}}$, and one identity does the work:

<div class="key" markdown>

$$\big|1+a\,e^{-j\theta}\big|^2=1+a^2+2a\cos\theta\qquad\Longrightarrow\qquad P_x=\frac{\sigma_i^2}{1+a^2+2a\cos\theta}$$

</div>

(Why: $|1+ae^{-j\theta}|^2=(1+ae^{-j\theta})(1+ae^{j\theta})=1+a^2+a(e^{j\theta}+e^{-j\theta})$, and $e^{j\theta}+e^{-j\theta}=2\cos\theta$.)

So we must write $A+B\cos\theta$ as $C\,(1+a^2+2a\cos\theta)$. The trick: the **ratio** $\frac{B}{A}$ must equal $\frac{2a}{1+a^2}$. Slide $a$ until the ratio matches the exam's $\frac{60}{61}$:

<div class="widget" data-w="pole" data-preset="factor"></div>

Two values of $a$ always give the same ratio: $a$ and $1/a$. Keep the one **inside the unit circle** ($|a|<1$): that makes the filter stable and **minimum phase**, which is what "innovation filter" requires.

## The recipe

!!! recipe key "Factorise $\dfrac{N}{A+B\cos\theta}$"
    1. **Match**: $C(1+a^2)=A$ and $2Ca=B$.
    2. **Divide** the two: $\dfrac{1+a^2}{2a}=\dfrac AB$ → the quadratic $B\,a^2-2A\,a+B=0$ → roots $a$ and $1/a$.
    3. **Keep $|a|<1$.** (If $B<0$, $a$ comes out negative.)
    4. $C=\dfrac{B}{2a}$, then $\sigma_i^2=\dfrac NC$.
    5. $L(z)=\dfrac1{1+a\,z^{-1}}$.

## Watch it once: April 2025 · 1e

!!! exam "Final exam, 13 April 2025 · 1e · 0.4 p"
    Random signal $x[n]$ has PSD $P_x(e^{j\theta}) = \dfrac{1}{61 + 60 \cos \theta}$. Find the spectral factorization of $x[n]$: the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$.

<div class="stepper" markdown>

**Step 1 · Match.** $C(1+a^2)=61$, $\ 2Ca=60$.

***

**Step 2 · Divide.** $\dfrac{1+a^2}{2a}=\dfrac{61}{60}$ → $60(1+a^2)=122a$ → $60a^2-122a+60=0$ → (÷2) $30a^2-61a+30=0$.
$a=\dfrac{61\pm\sqrt{61^2-4\cdot30\cdot30}}{60}=\dfrac{61\pm\sqrt{3721-3600}}{60}=\dfrac{61\pm11}{60}$, so $a=\frac{72}{60}=\frac65$ or $a=\frac{50}{60}=\frac56$.

***

**Step 3 · Keep the inside root.** $|\frac56|<1$ → $a=\frac56$. ($\frac65$ is its mirror outside the circle.)

***

**Step 4 · $C$ and $\sigma_i^2$.** $C=\dfrac{60}{2\cdot\frac56}=\dfrac{60}{5/3}=36$. Check: $36(1+\frac{25}{36})=36+25=61$ ✓. So $P_x=\dfrac{1}{36}\cdot\dfrac1{1+a^2+2a\cos\theta}$ and $\sigma_i^2=\dfrac1{36}$.

***

**Step 5 · Filter.** $L(z)=\dfrac{1}{1+\frac56z^{-1}}$.

</div>

## Your turn

!!! exam "Final exam, April 2024 · 1e · 0.4 p"
    A random signal $x[n]$ has PSD $P(e^{j\theta}) = \dfrac{7}{25 - 24 \cos(\theta)}$. Find the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$.

??? solution "Check your answer"
    $C(1+a^2)=25$, $2Ca=-24$. Divide: $\frac{1+a^2}{2a}=-\frac{25}{24}$ → $24a^2+50a+24=0$ → $12a^2+25a+12=0$ → $a=\frac{-25\pm\sqrt{625-576}}{24}=\frac{-25\pm7}{24}$: $-\frac34$ or $-\frac43$. Keep $a=-\frac34$. $C=\frac{-24}{2(-\frac34)}=16$ (check $16\cdot\frac{25}{16}=25$ ✓). $\sigma_i^2=\frac7{16}$.

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac34z^{-1}}$, $\quad\sigma_i^2=\dfrac7{16}$.

!!! exam "Final exam, 7 November 2022 · 1d · 0.75 p"
    $P_x(e^{j\theta}) = \dfrac{1}{\frac{5}{3} - \cos(\theta)}$. Find $\sigma_i^2$ and the innovation filter $L(z)$.

??? solution "Check your answer"
    $C(1+a^2)=\frac53$, $2Ca=-1$. Divide: $\frac{1+a^2}{2a}=-\frac53$ → $3a^2+10a+3=0$ → $a=\frac{-10\pm8}{6}$: $-\frac13$ or $-3$. Keep $-\frac13$. $C=\frac{-1}{-2/3}=\frac32$ (check $\frac32\cdot\frac{10}9=\frac53$ ✓). $\sigma_i^2=\frac{1}{3/2}=\frac23$.

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac13z^{-1}}$, $\quad\sigma_i^2=\dfrac23$.

!!! exam "Resit, June 2026 · 1e · 0.25 p"
    Which condition is required for a rational filter $H(z)$ to be the innovation filter obtained through spectral factorisation of a PSD? (a) minimum phase: all poles and zeros inside (or on) the unit circle. (b) maximum phase: all outside. (c) real impulse response with strict linear phase. (d) all-pass.

??? solution "Check your answer"
    !!! answer "Answer"
        **(a)** minimum phase. That is why we always keep $|a|<1$.

## Traps

!!! trap key "Where points are lost"
    - Keeping the root outside the circle ($\frac65$ instead of $\frac56$).
    - Sign: a **minus** cosine ($25-24\cos\theta$) gives a **negative** $a$, so $L=\frac1{1-\frac34z^{-1}}$.
    - Forgetting to divide by $C$: $\sigma_i^2=N/C$, not $N$.
    - Quick check at the end: $P(0)=\dfrac{\sigma_i^2}{(1+a)^2}$ must equal $\dfrac N{A+B}$.
