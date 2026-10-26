# 1.4 Spectral factorisation

<div class="meta"><span class="hot">In 5 of the last 5 exams</span><span>0.25–0.75 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

- **White noise** $i[n]$: pure randomness, the same power $\sigma_i^2$ at every frequency (flat PSD).
- Pass it through a filter $L(z)$ and the output has PSD $\sigma_i^2\,|L(e^{j\theta})|^2$: the filter shapes the flat spectrum.
- **Spectral factorisation** = go backwards: from the PSD, find the filter and the noise power that made it.

For the exam the filter is always $L(z)=\dfrac{1}{1+a\,z^{-1}}$, and one identity does the work:

<div class="key" markdown>

$$\big|1+a\,e^{-j\theta}\big|^2=1+a^2+2a\cos\theta\qquad\Longrightarrow\qquad P_x=\frac{\sigma_i^2}{1+a^2+2a\cos\theta}$$

</div>

(Why: $|1+ae^{-j\theta}|^2=(1+ae^{-j\theta})(1+ae^{j\theta})=1+a^2+a(e^{j\theta}+e^{-j\theta})$, and $e^{j\theta}+e^{-j\theta}=2\cos\theta$.)

Two values of $a$ always give the same spectrum: $a$ and $1/a$. Keep the one **inside the unit circle** ($|a|<1$): that makes the filter stable and **minimum phase**, which is what "innovation filter" requires. Slide $a$ and watch the pole move:

<div class="widget" data-w="pole" data-preset="factor"></div>

## How to fight this section with the sheet

The exam prints $P(\theta)=\dfrac{\text{number}}{A+B\cos\theta}$ and says **"spectral factorisation"**, **"innovation filter $L(z)$"**, **"$\sigma_i^2$"** → you open **box 1C** on your A4 sheet. Four numbered steps, and two of the exams below are already worked out underneath them. You never need the identity above — just read $A$ and $B$ off the denominator.

!!! sheet "Box 1C, exactly as it is printed on the sheet"
    IF YOU SEE $P(\theta)=\dfrac{\text{number}}{A+B\cos\theta}$ + "spectral factorisation"/"factorization", "innovation filter $L(z)$", "$\sigma_i^2$"

    1. Read $A$ and $B$ off the denominator $A+B\cos\theta$ **with their signs** ($25-24\cos\theta$: $A=25$, $B=-24$). Two candidate roots $r=\dfrac{A\pm\sqrt{A^2-B^2}}{B}$: keep the one between $-1$ and $1$, call it $a$.
    2. $C=\dfrac{B}{2a}$.
    3. $\sigma_i^2=\dfrac{\text{number on top}}{C}$, $L(z)=\dfrac{1}{1+a\,z^{-1}}$.
    4. Check $|a|\lt1$ and $\sigma_i^2\gt0$ — a negative $\sigma_i^2$ means you kept the wrong root.

    *Apr24* $\frac{7}{25-24\cos\theta}$: $A=25$, $B=-24$, $\sqrt{625-576}=7$, $r=\frac{25\pm7}{-24}$ = $-\frac43$ or $-\frac34$ → $a=-\frac34$. $C=\frac{-24}{-3/2}=16$. So $\sigma_i^2=\frac7{16}$, $L=\frac1{1-\frac34z^{-1}}$.

    *Apr25* $\frac{1}{61+60\cos\theta}$: $r=\frac{61\pm11}{60}$ → $a=\frac56$, $C=36$, $\sigma_i^2=\frac1{36}$, $L=\frac1{1+\frac56z^{-1}}$.

    Multiple choice "what must the innovation filter be?" → **minimum phase**: all poles and zeros inside the unit circle (Jun26 a).

## 1 · April 2025 · 1e — the sheet works this one out under the steps

!!! exam "Final exam Q3, 13 April 2025 · 1e · 0.4 p"
    Random signal $x[n]$ has the following power spectral density:

    $$P_x(e^{j\theta}) = \frac{1}{61 + 60 \cos \theta}$$

    Find the spectral factorization of $x[n]$, that is, the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$.

!!! sheet "In the cheat sheet: box 1C — the *Apr25* line under the steps is this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · read $A$ and $B$ with their signs.**
    Denominator $61+60\cos\theta$ → $A=61$, $B=+60$. The sheet's own example line: *"$r=\frac{61\pm11}{60}$"* — note the $\sqrt{A^2-B^2}=\sqrt{3721-3600}=\sqrt{121}=11$.

    ***

    **Sheet step 2 · the two roots, keep the inside one.**
    $r=\frac{61+11}{60}=\frac{72}{60}=\frac65$ or $r=\frac{61-11}{60}=\frac{50}{60}=\frac56$. The sheet: *"keep the one between $-1$ and $1$"* → $a=\frac56$ (step 4 check: $|a|<1$ ✓).

    ***

    **Sheet step 3 · $C=\frac{B}{2a}$.**
    $C=\frac{60}{2\cdot\frac56}=\frac{60}{5/3}=36$ — exactly the sheet's *"$C=36$"*.

    ***

    **Sheet step 4 · $\sigma_i^2$ and $L(z)$.**
    $\sigma_i^2=\frac{\text{number on top}}{C}=\frac1{36}$, $L(z)=\frac{1}{1+\frac56z^{-1}}$ — the sheet prints both.

    ***

    **Sheet check · the example line.**
    Last two tokens of the *Apr25* line: *"$\sigma_i^2=\frac1{36}$, $L=\frac1{1+\frac56z^{-1}}$."* Same answer → 0.4 p.

    </div>

!!! answer "Answer"
    $L(z)=\dfrac{1}{1+\frac56z^{-1}}$, $\quad\sigma_i^2=\dfrac1{36}$

## 2 · April 2024 · 1e — the minus-cosine case (negative $a$)

!!! exam "Final exam Q3, April 2024 · 1e · 0.4 p"
    A random signal $x[n]$ has the power spectra density given by:

    $$P(e^{j\theta}) = \frac{7}{25 - 24 \cos(\theta)}.$$

    Find the spectral factorization of $x[n]$. In other words, find the coefficients of the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$, so that $x[n]$ can be expressed as the output of the innovation filter when white noise with variance $\sigma_i^2$ is given as input.

!!! sheet "In the cheat sheet: box 1C — the *Apr24* line is this exam, printed as the sign example"
    <div class="stepper" markdown>

    **Sheet step 1 · signs first.**
    The sheet's step 1 example is literally this denominator: *"$25-24\cos\theta$: $A=25$, $B=-24$"*. The minus is **in $B$**.

    ***

    **Sheet step 2 · roots.**
    $\sqrt{A^2-B^2}=\sqrt{625-576}=7$, so $r=\frac{25\pm7}{-24}=\frac{32}{-24}=-\frac43$ or $\frac{18}{-24}=-\frac34$. Sheet: *"keep the one between $-1$ and $1$"* → $a=-\frac34$ (the sheet prints the same two numbers).

    ***

    **Sheet step 3 · $C=\frac{B}{2a}=\frac{-24}{-3/2}=16$.** The sheet prints $C=16$.

    ***

    **Sheet step 4 · finish.**
    $\sigma_i^2=\frac{7}{16}$ (number on top is **7**, not 1), $L(z)=\frac{1}{1+a z^{-1}}=\frac{1}{1-\frac34z^{-1}}$ — the sheet's exact $L$. Check: $|a|=\frac34<1$ ✓, $\sigma_i^2>0$ ✓.

    ***

    **Sheet check · the example line.**
    *"$\sigma_i^2=\frac7{16}$, $L=\frac1{1-\frac34z^{-1}}$."* If your $L$ has a plus sign you lost the minus of $B$.

    </div>

!!! answer "Answer"
    $L(z)=\dfrac{1}{1-\frac34z^{-1}}$, $\quad\sigma_i^2=\dfrac7{16}$

## 3 · November 2022 · 1d — fractions, same four steps

!!! exam "Final exam Q1, 7 November 2022 · 1d · 0.75 p"
    A random signal $x[n]$ has power spectral density given by $P_x(e^{j\theta}) = \frac{1}{\frac{5}{3} - \cos(\theta)}$. Find the spectral factorization of $x[n]$. In other words, modeling $x[n]$ as the output of an LTI driven by white noise, find the variance of the input noise $\sigma_i^2$ and the innovation filter $L(z)$.

!!! sheet "In the cheat sheet: box 1C, the four steps (no printed example — run them yourself)"
    <div class="stepper" markdown>

    **Sheet step 1 · read off.**
    $\frac{5}{3}-\cos\theta$: the invisible number in front of $\cos\theta$ is $-1$ → $A=\frac53$, $B=-1$ *("with their signs")*.

    ***

    **Sheet step 2 · roots.**
    $\sqrt{A^2-B^2}=\sqrt{\frac{25}{9}-1}=\sqrt{\frac{16}{9}}=\frac43$. $r=\frac{\frac53\pm\frac43}{-1}=\frac{3}{-1}=-3$ or $\frac{1/3}{-1}=-\frac13$. Keep the one between $-1$ and $1$ → $a=-\frac13$.

    ***

    **Sheet step 3 · $C=\frac{B}{2a}=\frac{-1}{-2/3}=\frac32$,** then $\sigma_i^2=\frac{\text{number on top}}{C}=\frac{1}{3/2}=\frac23$ and $L(z)=\frac{1}{1-\frac13z^{-1}}$.

    ***

    **Sheet step 4 · the check.**
    $|a|=\frac13<1$ ✓ and $\sigma_i^2=\frac23>0$ ✓ (*"a negative $\sigma_i^2$ means you kept the wrong root"* — if you had kept $-3$, $C=\frac{-1}{-6}=\frac16$ and $\sigma_i^2=6$ with an unstable $L$: wrong root, same spectrum).

    </div>

!!! answer "Answer"
    $L(z)=\dfrac{1}{1-\frac13z^{-1}}$, $\quad\sigma_i^2=\dfrac23$

## 4 · January 2022 · 1d — read a factorisation someone else wrote down

!!! exam "Resit, 24 January 2022 · 1d · 0.3 p"
    Random signal $x[n]$ has power spectral density given by

    $$P_x(e^{j\theta}) = \frac{\frac{17}{8} - \cos(\theta)}{\frac{25}{16} - \frac{3}{2} \cos(\theta)},$$

    which is factorized as

    $$P_x(e^{j\theta}) = 2 \frac{(1 - \frac{1}{4}z^{-1})(1 - \frac{1}{4}z)}{(1 + \frac{3}{4}z^{-1})(1 + \frac{3}{4}z)}.$$

    Which of the following statements is true?

    - a) The provided factorization does not represent the spectral factorization of signal $x[n]$.
    - b) The innovation filter is given by $L(z^{-1}) = \frac{1 - \frac{1}{4}z}{1 + \frac{3}{4}z}$.
    - c) The innovation filter is given by $L(z) = \frac{1 - \frac{1}{4}z^{-1}}{1 + \frac{3}{4}z^{-1}}$.
    - d) The input variance is given by $\sigma_i^2 = 1/2$.

!!! sheet "In the cheat sheet: box 1C, steps 3–4 + the MC line (minimum phase)"
    <div class="stepper" markdown>

    **Sheet step 1 · the shape.**
    Box 1C writes the model as $P=\sigma_i^2\,L(z)\,L(z^{-1})$: the constant **in front** is $\sigma_i^2$, the factor in $z^{-1}$ is $L(z)$, the factor in $z$ is $L(z^{-1})$. Here: $\sigma_i^2=2$, $L(z)=\frac{1-\frac14z^{-1}}{1+\frac34z^{-1}}$.

    ***

    **Sheet step 2 · the MC line decides it.**
    *"Multiple choice "what must the innovation filter be?" → **minimum phase**: all poles and zeros inside the unit circle."* $L(z)$: zero at $\frac14$, pole at $-\frac34$ — both inside ✓. $L(z^{-1})$ (option b) puts them at $4$ and $-\frac43$ — outside ✗.

    ***

    **Sheet step 3 · read the options.**
    (b) is the maximum-phase twin → not the innovation filter. (c) is $L(z)$ with both roots inside → **true**. (d) reads the constant wrong: it is $2$, not $\frac12$ (step 3: $\sigma_i^2$ = the number in front). (a) is false — the factorisation is valid.

    ***

    **Sheet check · the example line.**
    The MC line's answer tag is "(Jun26 a)" = "minimum phase"; this question asks the same property one level deeper — same line of the sheet, applied to a given factorisation.

    </div>

!!! answer "Answer"
    **(c)** $L(z) = \dfrac{1 - \frac14z^{-1}}{1 + \frac34z^{-1}}$ (the printed PSD's denominator sign was garbled in the exam; the factorisation given is the consistent one).

## 5 · June 2026 · 1e — the definition MC

!!! exam "Resit Q4, June 2026 · 1e · 0.25 p"
    Which of the following conditions is required for a discrete-time rational filter $H(z)$ to be the innovation filter obtained through the spectral factorisation of a given Power Spectral Density $P_x(z)$?

    - (a) $H(z)$ must be a minimum-phase system, meaning all its poles and zeros must lie inside (or on) the unit circle.
    - (b) $H(z)$ must be a maximum-phase system, meaning all its poles and zeros must lie strictly outside the unit circle.
    - (c) $H(z)$ must have a purely real-valued impulse response with strict linear phase to avoid phase distortion.
    - (d) $H(z)$ must be an all-pass system to ensure that the power of the driving noise is perfectly preserved.

!!! sheet "In the cheat sheet: box 1C, the last line — and it names this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · read the printed line.**
    *"Multiple choice "what must the innovation filter be?" → **minimum phase**: all poles and zeros inside the unit circle (Jun26 a)."* The sheet tags this exact question with its answer: **(a)**.

    ***

    **Sheet step 2 · kill the others (why the sheet says "inside").**
    Step 1's rule (*"keep the one between $-1$ and $1$"*) exists because two roots give the same spectrum; the **inside** one is the stable, causal, invertible choice. (b) is the outside twin, (c) linear phase is unrelated, (d) all-pass would keep the PSD flat = white noise only.

    </div>

!!! answer "Answer"
    **(a)** minimum phase

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - Ignoring the sign of $B$: $25-24\cos\theta$ → $B=-24$ (*"with their signs"*) → $a=-\frac34$, $L=\frac1{1-\frac34z^{-1}}$. A plus in $L$ when the exam prints a minus cosine = step 1 skipped.
    - Keeping the root outside the circle ($\frac65$ instead of $\frac56$, $-3$ instead of $-\frac13$). Step 1: *"keep the one between $-1$ and $1$"*, step 4 re-checks $|a|<1$.
    - Forgetting to divide by $C$: step 3 is $\sigma_i^2=\frac{\text{number on top}}{C}$, not the number on top. Apr24: $\frac7{16}$, not $7$.
    - Negative $\sigma_i^2$ at the end = you kept the wrong root (step 4 says exactly that) — flip to the other root and redo.
    - Mixing up the roles when a factorisation is given: the constant in front is $\sigma_i^2$, the $z^{-1}$ factor is $L(z)$, the $z$ factor is $L(z^{-1})$ (Jan22 (d) trap).
    - Choosing $L(z^{-1})$ because it "looks like" the filter: the sheet's MC line requires **minimum phase** = both roots inside the unit circle.
