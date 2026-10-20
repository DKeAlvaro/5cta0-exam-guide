# 1.4 Spectral factorisation (the innovation filter)

<p class="lead">In every exam since 2022 you get a power spectral density written with cosines and must find the filter $L(z)$ and noise variance $\sigma_i^2$ that produce it. It is a mechanical 5-minute procedure worth 0.25–0.75 p. One idea decides it: <b>pick the root inside the unit circle</b>.</p>

## The idea, from zero

**White noise** $i[n]$ is a sequence of uncorrelated random numbers with zero mean and variance $\sigma_i^2$. Its PSD is flat: every frequency has the same power $\sigma_i^2$.

If you pass a random signal through a linear filter $H(z)$, its spectrum gets multiplied by the squared magnitude of the filter:

$$P_y(e^{j\theta})=|H(e^{j\theta})|^2\,P_x(e^{j\theta}).$$

So white noise through a filter $L(z)$ gives a "coloured" signal with PSD $\sigma_i^2|L(e^{j\theta})|^2$. The **innovation representation** says: almost any WSS signal can be seen as white noise through a filter. Finding that filter from the PSD is **spectral factorisation**:

$$P_x(z)=\sigma_i^2\,L(z)\,L(z^{-1}),\qquad z=e^{j\theta}.$$

**Why "pick inside the unit circle".** The PSD only knows $|L|^2$. A factor $(1-az^{-1})$ and a factor $(1-a^{-1}z^{-1})$ give the same magnitude shape (up to a constant), so there are always two candidates. The convention that makes the answer unique: $L(z)$ is **causal, stable and minimum phase** (all poles **and** zeros inside the unit circle), and its first impulse-response sample is $l[0]=1$. Minimum phase also guarantees that the inverse $1/L(z)$, the whitening filter that turns $x[n]$ back into $i[n]$, is stable.

<figure markdown>
![Choosing the root inside the unit circle](img/gen/p1_unit_circle.svg)
<figcaption>April 2024 1e: the equations give $a=3/4$ or $a=4/3$. Same $|L|^2$ shape, but only the pole inside the unit circle gives a stable, minimum-phase innovation filter.</figcaption>
</figure>

## The recipe

The key identity (from the [toolbox](toolbox.md#5-complex-exponentials-needed-for-every-psd)):

$$(1-az^{-1})(1-az)=1+a^2-a(z+z^{-1})=\underbrace{(1+a^2)}_{\text{constant}}-\underbrace{2a}_{\text{cos coeff.}}\cos\theta .$$

With a **plus** sign, $(1+az^{-1})(1+az)=(1+a^2)+2a\cos\theta$.

!!! recipe "Recipe: spectral factorisation of $P(e^{j\theta})=\dfrac{\alpha_n\pm\beta_n\cos\theta}{\alpha_d\pm\beta_d\cos\theta}$"
    Do numerator and denominator separately. For "$\alpha\pm\beta\cos\theta$":

    1. Match it to $C\big[(1+a^2)\pm2a\cos\theta\big]$:
       $\quad C(1+a^2)=\alpha,\qquad 2Ca=\beta.$
    2. Divide the two equations to remove $C$: $\dfrac{1+a^2}{2a}=\dfrac{\alpha}{\beta}$, i.e. $a^2-\dfrac{2\alpha}{\beta}a+1=0$. The two roots are $a$ and $1/a$.
    3. **Keep the root with $|a|<1$.**
    4. $C=\beta/(2a)$.
    5. With $C_n,b$ from the numerator and $C_d,a$ from the denominator:
       $$\sigma_i^2=\frac{C_n}{C_d},\qquad L(z)=\frac{1\pm bz^{-1}}{1\pm az^{-1}}$$
       using the same sign as the cosine term (minus cos ↔ minus in $L$).
    6. **Check** at $\theta=0$: $\sigma_i^2\,\frac{(1\pm b)^2}{(1\pm a)^2}$ must equal $P(e^{j0})$.

!!! trap "Traps"
    - $\cos\theta=\frac{z+z^{-1}}{2}$: the coefficient of $z$ is **half** the cosine coefficient. Writing $60\cos\theta$ as $60(z+z^{-1})$ is the classic mistake.
    - A constant numerator (e.g. 1 or 7) gives $b=0$, $C_n=$ that constant.
    - $L(z^{-1})$ (poles outside the circle) is the *maximum-phase* twin, never the answer.

---

## Exam questions

### April 2025 exam · 1e {#apr25-1e}

!!! exam "Final exam Q3, 13 April 2025 · 1e · 0.4 p"
    Random signal $x[n]$ has the following power spectral density:

    $$P_x(e^{j\theta}) = \frac{1}{61 + 60 \cos \theta}$$

    Find the spectral factorization of $x[n]$, that is, the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$.

???+ solution "Solution"
    **Numerator** is the constant 1: $C_n=1$, no zero.

    **Denominator** $61+60\cos\theta$ has a **plus** sign, so match it with $C_d(1+az^{-1})(1+az)=C_d(1+a^2)+2C_da\cos\theta$:

    $$C_d(1+a^2)=61,\qquad 2C_da=60\;\Rightarrow\;C_da=30.$$

    Divide: $\dfrac{1+a^2}{a}=\dfrac{61}{30}\Rightarrow30a^2-61a+30=0\Rightarrow a=\dfrac{61\pm11}{60}=\dfrac65\text{ or }\dfrac56.$

    Keep $a=\frac56$ (inside the unit circle). Then $C_d=30/a=36$.

    $$\sigma_i^2=\frac{C_n}{C_d}=\frac1{36},\qquad L(z)=\frac{1}{1+\frac56z^{-1}}.$$

    **Check** $\theta=0$: $\frac{1/36}{(1+5/6)^2}=\frac{1/36}{121/36}=\frac1{121}$ and $\frac1{61+60}=\frac1{121}$ ✓

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1+\frac56z^{-1}}$, $\quad\sigma_i^2=\dfrac1{36}$

### April 2024 exam · 1e {#apr24-1e}

!!! exam "Final exam Q3, April 2024 · 1e · 0.4 p"
    A random signal $x[n]$ has the power spectra density given by:

    $$P(e^{j\theta}) = \frac{7}{25 - 24 \cos(\theta)}.$$

    Find the spectral factorization of $x[n]$. In other words, find the coefficients of the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$, so that $x[n]$ can be expressed as the output of the innovation filter when white noise with variance $\sigma_i^2$ is given as input.

???+ solution "Solution"
    Numerator: $C_n=7$. Denominator, **minus** sign: $C_d(1+a^2)=25$, $2C_da=24\Rightarrow C_da=12$.

    $$\frac{1+a^2}{a}=\frac{25}{12}\Rightarrow12a^2-25a+12=0\Rightarrow a=\frac{25\pm7}{24}=\frac43\text{ or }\frac34.$$

    Keep $a=\frac34$; $C_d=12/a=16$.

    $$\sigma_i^2=\frac{7}{16},\qquad L(z)=\frac{1}{1-\frac34z^{-1}}.$$

    Check $\theta=0$: $\frac{7/16}{(1/4)^2}=7$ and $\frac{7}{25-24}=7$ ✓. So $x[n]$ is an AR(1) process: $x[n]=\frac34x[n-1]+i[n]$.

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac34z^{-1}}$, $\quad\sigma_i^2=\dfrac7{16}$

### November 2022 exam · 1d {#nov22-1d}

!!! exam "Final exam Q1, 7 November 2022 · 1d · 0.75 p"
    A random signal $x[n]$ has power spectral density given by $P_x(e^{j\theta}) = \frac{1}{\frac{5}{3} - \cos(\theta)}$. Find the spectral factorization of $x[n]$. In other words, modeling $x[n]$ as the output of an LTI driven by white noise, find the variance of the input noise $\sigma_i^2$ and the innovation filter $L(z)$.

???+ solution "Solution"
    Numerator $C_n=1$. Denominator: $C_d(1+a^2)=\frac53$, $2C_da=1$.

    $$\frac{1+a^2}{2a}=\frac53\Rightarrow3a^2-10a+3=0\Rightarrow a=3\text{ or }\frac13.$$

    Keep $a=\frac13$, so $C_d=\frac{1}{2a}=\frac32$ and $\sigma_i^2=\frac{1}{3/2}=\frac23$.

    $$P_x(z)=\frac23\cdot\frac{1}{1-\frac13z^{-1}}\cdot\frac{1}{1-\frac13z}$$

    Check $\theta=0$: $\frac{2/3}{(2/3)^2}=\frac32$ and $\frac{1}{5/3-1}=\frac32$ ✓

    !!! answer "Answer"
        $L(z)=\dfrac{1}{1-\frac13z^{-1}}$, $\quad\sigma_i^2=\dfrac23$

### January 2024 resit · 1f {#jan24-1f}

!!! exam "Resit January 2024 · 1f · 0.25 p (shown in the Part 1 review lecture)"
    A random signal has the following power spectral density:

    $$P(e^{j\theta}) = \frac{10+6\cos(\theta)}{17-8\cos(\theta)}$$

    Which of the following is the spectral factorization of $P(e^{j\theta})$?

    - (a) $L(z) = \frac{1+3z^{-1}}{1-4z^{-1}}$, and $\sigma_i^2 = 1$
    - (b) $L(z) = \frac{1+3z^{-1}}{1-\frac{1}{4}z^{-1}}$, and $\sigma_i^2 = \frac{1}{16}$
    - (c) $L(z) = \frac{1+\frac{1}{3}z^{-1}}{1-\frac{1}{4}z^{-1}}$, and $\sigma_i^2 = \frac{9}{16}$
    - (d) $L(z) = \frac{1+\frac{1}{3}z^{-1}}{1-4z^{-1}}$, and $\sigma_i^2 = 9$

???+ solution "Solution"
    **Fast way (MC):** all four options produce the same PSD. Only one has every pole and zero inside the unit circle: (c), with zero $-\frac13$ and pole $\frac14$.

    **Full way:** numerator $10+6\cos\theta$: $C_n(1+b^2)=10$, $C_nb=3\Rightarrow3b^2-10b+3=0\Rightarrow b=\frac13$, $C_n=9$. Denominator $17-8\cos\theta$: $C_d(1+a^2)=17$, $C_da=4\Rightarrow4a^2-17a+4=0\Rightarrow a=\frac14$, $C_d=16$. So $\sigma_i^2=\frac9{16}$.

    !!! answer "Answer"
        **(c)**

!!! trap "Slide typo"
    The "extra exercise" in the 2026-27 Part 1 review deck ends with $L(z)=\frac{1-\frac14z^{-1}}{1-\frac13z^{-1}}$: numerator and denominator swapped and a sign flipped. The correct factorisation is option (c) above.

### January 2022 resit · 1d {#jan22-1d}

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

???+ solution "Solution"
    (The printed factorisation was garbled by the conversion; above is what it means. The official clarification: the denominator should be $\frac{25}{16}+\frac32\cos\theta$, otherwise the sign does not match the factorisation.)

    Read the factorisation as $\sigma_i^2L(z)L(z^{-1})$ with $\sigma_i^2=2$, $L(z)=\frac{1-\frac14z^{-1}}{1+\frac34z^{-1}}$: zero at $\frac14$, pole at $-\frac34$, both inside the unit circle, so this is the minimum-phase factor.

    - (b) $L(z^{-1})$ has its zero and pole outside the circle (maximum phase).
    - (d) the constant in front is $\sigma_i^2=2$, not $\frac12$.

    !!! answer "Answer"
        **(c)**

### June 2026 resit · 1e {#jun26-1e}

!!! exam "Resit Q4, June 2026 · 1e · 0.25 p"
    Which of the following conditions is required for a discrete-time rational filter $H(z)$ to be the innovation filter obtained through the spectral factorisation of a given Power Spectral Density $P_x(z)$?

    - (a) $H(z)$ must be a minimum-phase system, meaning all its poles and zeros must lie inside (or on) the unit circle.
    - (b) $H(z)$ must be a maximum-phase system, meaning all its poles and zeros must lie strictly outside the unit circle.
    - (c) $H(z)$ must have a purely real-valued impulse response with strict linear phase to avoid phase distortion.
    - (d) $H(z)$ must be an all-pass system to ensure that the power of the driving noise is perfectly preserved.

???+ solution "Solution"
    The innovation filter is causal, stable and **minimum phase**. (The reader excludes poles *on* the circle; the "(or on)" refers to zeros, which may sit on it, e.g. the zero at $z=1$ in [Nov 2022 3d](p3-autocorr.md#nov22-3c).) An all-pass filter has a flat $|H|^2$, so it could never shape a spectrum.

    !!! answer "Answer"
        **(a)** minimum phase
