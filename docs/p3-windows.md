# 3.1 Signals, windows, zero padding

<p class="lead">Before estimating spectra you need three ideas: energy vs power signals, what cutting a signal to N samples (windowing) does to its spectrum, and why zero padding does <em>not</em> improve resolution. These are mostly multiple-choice and "final answer only" points.</p>

## Energy vs power signals

$$E_x=\int_{-\infty}^{\infty}|x(t)|^2dt\qquad\qquad P_x=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}|x(t)|^2dt$$

(for discrete time replace the integral by $\sum_n|x[n]|^2$).

- **Energy signal**: finite energy, $0<E_x<\infty$. Then its average power is **0**. Typical: pulses, decaying exponentials, anything that dies out.
- **Power signal**: finite non-zero average power, so $E_x=\infty$. Typical: **periodic** signals (sines, cosines, even if switched on at $t=0$) and stationary random signals.
- Neither: e.g. $e^{t}$ (grows forever).

Useful: a sine or cosine of amplitude $A$ has power $A^2/2$. Switched on only for $t\ge0$ it has $A^2/4$ (it is "on" half of the symmetric averaging window).

## Windowing: what observing only N samples does

In practice you only have $N$ samples. That is the same as multiplying the infinite signal by a **window** $w[n]$ that is 1 for $n=0,\dots,N-1$ (rectangular) and 0 elsewhere. Multiplication in time is convolution in frequency, so the spectrum you compute is the true spectrum **smeared by the window's spectrum** $W(e^{j\theta})$.

<figure markdown>
![Rectangular vs Hann window](img/gen/p3_windows.svg)
<figcaption>Left: spectra of two windows of the same length, in dB. The rectangular window has the narrowest main lobe but high side lobes (−13 dB). The Hann window has a wider main lobe but much lower side lobes (−32 dB). Right: a strong tone at 1.0 and a 34 dB weaker tone at 2.3. With the rectangular window the weak tone is buried in leakage; with Hann it shows up.</figcaption>
</figure>

The window spectrum has two parts, and each causes one problem:

| Part of $W(e^{j\theta})$ | Causes | What you see |
|---|---|---|
| **Main lobe width** | loss of **resolution** (smoothing) | two peaks closer than ≈ $2\pi/N$ merge into one; peaks get wider and lower |
| **Side-lobe height** | spectral **leakage** | power "leaks" to other frequencies; weak components get hidden; spurious peaks |

- **Longer window (larger $N$)** → narrower main lobe → **better resolution**. (For a rectangular window the side lobes stay at −13 dB, so the exams treat "increase $N$ to reduce leakage" as **false**.)
- **Smoother window** (triangular −27 dB, Hann −32 dB, Hamming) → **less leakage** but **wider main lobe** → *worse* resolution for the same $N$.

## DFT, FTD and zero padding

- **FTD** (Fourier transform for discrete-time signals): $X(e^{j\theta})=\sum_nx[n]e^{-jn\theta}$, a continuous function of $\theta$.
- **DFT** with $N$ points: the $N$-sample FTD **sampled** at $\theta_k=2\pi k/N$.
- **Zero padding** to $L>N$: append $L-N$ zeros and take an $L$-point DFT. This samples the **same** $N$-sample FTD at the finer spacing $2\pi k/L$. It interpolates and makes plots smoother, but it does **not** improve resolution: the main lobe width is still set by $N$ and the window.

<figure markdown>
![Zero padding](img/gen/p3_zeropad.svg)
<figcaption>Grey: the FTD of 16 samples of a cosine. Blue squares: the 16-point DFT. Red dots: the DFT after zero padding to 64. The red dots trace the grey curve more finely; the peak does not get narrower.</figcaption>
</figure>

!!! trap "Traps"
    - "Zero padding increases resolution" → **false**. It increases the *density of frequency samples*, nothing more.
    - "A triangular/Hann window gives higher resolution than rectangular" → **false** (wider main lobe). It gives *less leakage*.
    - Bias from windowing affects **both** deterministic and random signals. Variance is the extra problem of random signals.

---

## Exam questions

### April 2025 exam · 3a {#apr25-3a}

!!! exam "Final exam Q3, 13 April 2025 · 3a · 0.5 p"
    For each of the following signals, indicate whether they are energy or power signals, and provide their total energy and average power.

    ***Provide only the final answer. The workout will not be checked.***

    1. $x(t) = A \sin(\omega t)$, with $A, \omega$ being the fixed amplitude and frequency, respectively.
    2. $x[n] = e^{-n}$ for $n \geq 0$, and $x[n] = 0$ elsewhere.

???+ solution "Solution"
    **1.** Periodic → power signal. With $\sin^2=\frac{1-\cos2\omega t}{2}$, the cosine averages out:

    $$P=\lim_{T\to\infty}\frac{A^2}{T}\int_{-T/2}^{T/2}\frac{1-\cos(2\omega t)}{2}dt=\frac{A^2}{2},\qquad E=\infty.$$

    **2.** A decaying sequence → energy signal. Geometric series with ratio $e^{-2}$:

    $$E=\sum_{n=0}^\infty e^{-2n}=\frac{1}{1-e^{-2}}\approx1.157,\qquad P=0.$$

    !!! answer "Answer"
        1. Power signal: $E=\infty$, $P=A^2/2$. 2. Energy signal: $E=\frac{1}{1-e^{-2}}\approx1.16$, $P=0$.

### Q2 2023-24 resit · 3a {#q2-24-3a}

!!! exam "Resit Q2 2023-24 · 3a (shown in the Part 3 review lecture)"
    For the signals in the table below, please indicate whether they are energy or power signals, Note that $u(t)$ represents the unit step function.

    | Signal | Energy or Power? |
    |---|---|
    | $x(t) = e^{-t}u(t)$ | |
    | $x(t) = \cos(t)u(t)$ | |
    | $x(t) = 5 \text{ for } -2 \leq t \leq 2, \text{ zero elsewhere.}$ | |
    | $x(t) = 5e^{-2\lvert t\rvert}$ | |

???+ solution "Solution"
    - $e^{-t}u(t)$: $E=\int_0^\infty e^{-2t}dt=\frac12$ → energy.
    - $\cos(t)u(t)$: periodic for $t\ge0$, $E=\infty$, $P=\frac14$ → power.
    - rectangular pulse: $E=\int_{-2}^{2}25\,dt=100$ → energy.
    - $5e^{-2|t|}$: $E=2\int_0^\infty25e^{-4t}dt=\frac{25}{2}$ → energy.

    !!! answer "Answer"
        Energy · Power · Energy · Energy

### November 2022 exam · 3b {#nov22-3b}

!!! exam "Final exam Q1, 7 November 2022 · 3b · 0.25 p"
    In the context of windowing and zero-padding, which of the following statements is TRUE?

    - a) Given the same window length, a triangular window provides higher spectral resolution compared to a rectangular window.
    - b) When calculating the spectrum of a windowed signal, the main-lobe width of the window function determines spectral resolution, while the height of the side lobes determines spectral leakage.
    - c) When estimating the spectrum using a rectangular window, spectral leakage can be reduced by increasing the window length.
    - d) When calculating the Fourier transform of a N-sample discrete signal, extending the signal to a length L by zero padding is equivalent to sampling the L-sample Fourier Transform for Continuous time signal (FTD) at a step given by theta = k * 2pi / N

???+ solution "Solution"
    - (a) Triangular has a **wider** main lobe → *lower* resolution.
    - (b) Exactly the table above. ✓
    - (c) Marked false in the review: for a rectangular window the side lobes stay at −13 dB whatever $N$ is.
    - (d) Zero padding to $L$ samples the $N$-sample FTD at steps $2\pi k/L$, not $2\pi k/N$. ("FTD" is the transform for discrete-time signals; the "continuous" is a typo.)

    !!! answer "Answer"
        **(b)**

### January 2020 retake · 1c {#jan20-1c}

!!! exam "Retake exam, 20 January 2020 · Exercise 1(c) · 0.25 p"
    In the context of windowing, which one of the following statements is true:

    - A. The higher the side lobes of the window function, the worse the resolution of the spectral estimate.
    - B. The higher the side lobes of the window function, the smaller the effects of spectral leakage.
    - C. The wider the main lobe of the window function, the worse the resolution of the spectral estimate.
    - D. The wider the main lobe of the window function, the larger the effects of spectral leakage.

???+ solution "Solution"
    Main lobe ↔ resolution, side lobes ↔ leakage. Only C pairs them correctly and with the right direction.

    !!! answer "Answer"
        **C**

### January 2022 resit · 3a {#jan22-3a}

!!! exam "Resit, 24 January 2022 · 3a · 0.3 p"
    The infinitely-long discrete-time signal $x[n] = 20 \cos(2\pi \frac{f}{f_s} n)$, with $f = 25 \text{ Hz}$ and $f_s = 50 \text{ Hz}$, is windowed with a rectangular window of length $N$ to obtain the window signal $\tilde{x}[n]$. In the plots below, the following Fourier transforms are shown:

    1. The Fourier Transform for Discrete time signals (FTD) of $x[n]$
    2. The FTD of $\tilde{x}[n]$.
    3. The Discrete Fourier Transform (DFT) of $\tilde{x}[n]$ calculated for $N = 24$ and zero padding of $M = 12$ samples.
    4. The Discrete Fourier Transform (DFT) of $\tilde{x}[n]$ calculated for $N = 24$ with no zero padding.

    ![Four transforms A–D](img/exam/jan22-3a-ft.jpg)

    Which of the following is the correct association?

    - (a) 1B, 2D, 3A, 3C
    - (b) 1B, 2D, 3C, 4A
    - (c) 1C, 2A, 3D, 4B
    - (d) 1D, 2B, 3C, 4A

???+ solution "Solution"
    **How to read the plot.** Horizontal axis: frequency in Hz (−fs to fs). Vertical: magnitude, normalised so each cosine peak has height $20/2=10$. Four series: A blue squares, B orange solid line, C yellow circles, D purple dashed curve.

    1. An **infinite** cosine has only two frequencies → two infinitely thin spikes at ±25 Hz: the solid lines **B**.
    2. Cutting it to $N$ samples convolves each spike with the window's sinc → a **continuous** curve with main lobes and side lobes: the dashed curve **D**.
    3. A DFT gives **samples** of curve D. Without zero padding ($N=24$) the spacing is $50/24\approx2.08$ Hz. 25 Hz sits exactly on bin 12, and every other bin lands on a **zero** of the sinc. So you see one point at the peak and all others at 0: squares **A** → item 4.
    4. With zero padding to $24+12=36$ points, the spacing is $50/36\approx1.39$ Hz. Now the samples fall on the **side lobes**: circles **C** → item 3.

    This is also a nice picture of "zero padding does not add resolution": C and A are samples of the same curve D.

    !!! answer "Answer"
        **(b)** 1B, 2D, 3C, 4A
