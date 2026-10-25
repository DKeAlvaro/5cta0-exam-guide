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
    **What is being asked?** Write $P=\dfrac{7}{25-24\cos\theta}$ in the shape $\dfrac{\sigma_i^2}{1+a^2+2a\cos\theta}$, and read off $L(z)=\dfrac{1}{1+az^{-1}}$ and $\sigma_i^2$.

    **Step 1 · Match the shape.** We need $25-24\cos\theta=C\,(1+a^2+2a\cos\theta)$ for some $C$ and $a$: then $P=\dfrac{7}{C(1+a^2+2a\cos\theta)}=\dfrac{7/C}{1+a^2+2a\cos\theta}$, which is the wanted shape with $\sigma_i^2=7/C$. Compare the constant part and the cosine part:

    $$C(1+a^2)=25,\qquad 2Ca=-24$$

    (the minus sign is because the exam prints $-24\cos\theta$).

    **Step 2 · Divide to eliminate $C$.** $\dfrac{C(1+a^2)}{2Ca}=\dfrac{25}{-24}$ → $\dfrac{1+a^2}{2a}=-\dfrac{25}{24}$.

    **Step 3 · Clear the denominators.** Multiply by $24\cdot 2a$: $24(1+a^2)=-25\cdot 2a$ → $24a^2+50a+24=0$ → (everything ÷ 2) $12a^2+25a+12=0$.

    **Step 4 · Quadratic formula.** $a=\dfrac{-25\pm\sqrt{25^2-4\cdot12\cdot12}}{2\cdot12}=\dfrac{-25\pm\sqrt{625-576}}{24}=\dfrac{-25\pm7}{24}$: $a=-\dfrac{18}{24}=-\dfrac34$ or $a=-\dfrac{32}{24}=-\dfrac43$.

    **Step 5 · Keep the root inside the unit circle.** $|-\frac34|=0.75<1$ ✓, $|-\frac43|=1.33>1$ ✗. So $a=-\frac34$ and $L(z)=\dfrac{1}{1-\frac34 z^{-1}}$ (the minus in front of $\frac34z^{-1}$ is the negative $a$).

    **Step 6 · $C$, then $\sigma_i^2$.** $C=\dfrac{-24}{2a}=\dfrac{-24}{-3/2}=16$. Check: $16\big(1+\frac{9}{16}\big)=16+9=25$ ✓. And $\sigma_i^2=\dfrac{N}{C}=\dfrac{7}{16}$ (not $\frac{7}{1}$: the $C$ must go).

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac34z^{-1}}$, $\quad\sigma_i^2=\dfrac7{16}$.

!!! exam "Final exam, 7 November 2022 · 1d · 0.75 p"
    $P_x(e^{j\theta}) = \dfrac{1}{\frac{5}{3} - \cos(\theta)}$. Find $\sigma_i^2$ and the innovation filter $L(z)$.

??? solution "Check your answer"
    **What is being asked?** Same as the previous exercise: $P=\dfrac{1}{\frac53-\cos\theta}$ → $\dfrac{\sigma_i^2}{1+a^2+2a\cos\theta}$.

    **Step 1 · Match.** $\frac53-\cos\theta=C(1+a^2+2a\cos\theta)$, so $C(1+a^2)=\frac53$ and $2Ca=-1$ (the cosine comes with $-1$).

    **Step 2 · Divide.** $\dfrac{1+a^2}{2a}=-\dfrac53$ → $3(1+a^2)=-10a$ → $3a^2+10a+3=0$.

    **Step 3 · Quadratic.** $a=\dfrac{-10\pm\sqrt{100-36}}{6}=\dfrac{-10\pm8}{6}$: $-\dfrac13$ or $-3$.

    **Step 4 · Keep $|a|<1$.** $|-\frac13|<1$ ✓, $|-3|>1$ ✗ → $a=-\frac13$, $L(z)=\dfrac{1}{1-\frac13z^{-1}}$.

    **Step 5 · $C$ and $\sigma_i^2$.** $C=\dfrac{-1}{2a}=\dfrac{-1}{-2/3}=\frac32$ (check: $\frac32\big(1+\frac19\big)=\frac32\cdot\frac{10}9=\frac53$ ✓). Then $\sigma_i^2=\dfrac{N}{C}=\dfrac{1}{3/2}=\frac23$.

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac13z^{-1}}$, $\quad\sigma_i^2=\dfrac23$.

!!! exam "Resit, June 2026 · 1e · 0.25 p"
    Which condition is required for a rational filter $H(z)$ to be the innovation filter obtained through spectral factorisation of a PSD? (a) minimum phase: all poles and zeros inside (or on) the unit circle. (b) maximum phase: all outside. (c) real impulse response with strict linear phase. (d) all-pass.

??? solution "Check your answer"
    **What is being asked?** Which property must the factor $H(z)$ have to count as *the* innovation filter?

    **Step 1 · Why one answer is forced.** A PSD can be written as $\sigma_i^2|H|^2$ in many ways (the mirror root $a$ vs $1/a$ gives the same $|H|^2$), so without a rule there would be no unique answer. The rule the course takes: **minimum phase** — all poles and zeros inside (or on) the unit circle. Then $H$ is stable and causal and has a stable inverse, which is what "innovations" (white input) needs.

    **Step 2 · Kill the others.** (b) maximum phase is the mirror choice, outside the circle. (c) linear phase is a filter-design wish, unrelated. (d) all-pass means $|H|$ is flat, so the PSD would be flat too — only white noise.

    !!! answer "Answer"
        **(a)** minimum phase. That is why we always keep $|a|<1$.

## Traps

!!! trap key "Where points are lost"
    - Keeping the root outside the circle ($\frac65$ instead of $\frac56$).
    - Sign: a **minus** cosine ($25-24\cos\theta$) gives a **negative** $a$, so $L=\frac1{1-\frac34z^{-1}}$.
    - Forgetting to divide by $C$: $\sigma_i^2=N/C$, not $N$.
    - Quick check at the end: $P(0)=\dfrac{\sigma_i^2}{(1+a)^2}$ must equal $\dfrac N{A+B}$.
