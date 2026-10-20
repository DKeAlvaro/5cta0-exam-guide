# 0 · From zero: signals, frequency, spectra

<p class="lead">This chapter assumes <b>nothing</b>. Every other page of the guide uses the words and formulas defined here. If a step anywhere else in the guide confuses you, the reason is on this page. Read it slowly; it is the only page where being slow matters. The rest of the guide only asks you to <i>use</i> these ideas, never to re-derive them.</p>

!!! idea "How to read this page"
    Each section goes: **plain words → tiny concrete example with real numbers → the formula → what the exam expects you to do with it.** If you already know a section, skip it. If a word is underlined like this: *[sample]*, tap/hover it for a one-line definition.

---

## 0.1 What a signal is

**Plain words.** A signal is just *a number that changes over time*. The voltage on a microphone cable, the temperature in a room, the daily closing price of a stock. That is all "signal" means. The course never deals with anything more exotic than that.

There are two kinds, and the notation tells you which one you are looking at:

| Kind | Written | Time index | Meaning |
|---|---|---|---|
| **Continuous-time** | $x(t)$ | $t$ is any real number | the physical, real-world signal (voltage that exists at every instant) |
| **Discrete-time** | $x[n]$ | $n = \dots,-1,0,1,2,\dots$ only integers | a **list of numbers**: one measurement per time step |

Two notation rules that look like pedantry but will save you points:

1. **Round brackets = continuous** ($x(t)$), **square brackets = discrete** ($x[n]$). The exam uses this consistently. If you see $x[n]$ you are summing ($\sum$); if you see $x(t)$ you are integrating ($\int$).
2. $n$ is a *count* (0, 1, 2, …), so nothing "happens between" $n=3$ and $n=4$.

**Sampling** is how you get the second kind from the first: you measure $x(t)$ once every $T_s$ seconds and throw away everything in between.

$$x[n] = x(nT_s),\qquad T_s=\frac{1}{f_s}\ \text{seconds between samples}$$

$f_s$ is the **sample rate** in Hz (samples per second). Example: audio at $f_s=50$ Hz means you keep one number every $1/50=0.02$ s. The exam loves to give you $f_s$ because the *digital* frequency of a tone depends on it (next section).

!!! trap "The exam's favourite corner"
    A discrete signal can only wiggle as fast as "up, down, up, down" ($+1,-1,+1,-1,\dots$). Anything faster is *impossible* to represent with one sample per step. That fastest wiggle corresponds to half the sample rate.

---

## 0.2 Sine, cosine, frequency

**Plain words.** $\sin$ and $\cos$ describe smooth, repeating wiggles. They repeat every $2\pi \approx 6.28$ units of their argument. A tone is one of these wiggles with an amplitude (how tall) and a frequency (how fast).

Continuous-time version:

$$x(t) = A\sin(\omega t) \;=\; A\sin(2\pi f t)$$

| Symbol | Name | Unit | Meaning |
|---|---|---|---|
| $A$ | amplitude | volts (whatever $x$ measures) | how tall the wiggle is |
| $f$ | frequency | **Hz** = cycles per second | how many full wiggles per second |
| $\omega$ | angular frequency | rad/s | same thing as $f$, in "radians per second": $\omega = 2\pi f$ |
| $T=1/f$ | period | s | time for one full wiggle |

**Why $\omega = 2\pi f$?** One full cycle is $2\pi$ radians. Doing $f$ cycles per second means the angle $2\pi f t$ grows by $2\pi$ every $1/f$ seconds. Both notations appear in exams ($A\sin(\omega t)$ and $A\sin(2\pi f t)$ are the *same signal*).

**Discrete version.** For $x[n]$ the angle is $\theta n$, with $\theta$ measured in **radians per sample**:

$$x[n] = A\cos(\theta n),\qquad \theta = 2\pi\frac{f}{f_s}\ \text{(radians per sample)}$$

and $\theta$ always lives between $-\pi$ and $\pi$ (outside that range the same wiggle comes back — you cannot tell fast wiggles from slow ones once they are sampled).

**Tiny worked example (this exact one is an exam question).** $f=25$ Hz sampled at $f_s=50$ Hz:

$$\theta = 2\pi\cdot\frac{25}{50} = \pi \qquad\Rightarrow\qquad x[n]=\cos(\pi n) = (-1)^n = 1,-1,1,-1,\dots$$

So a 25 Hz tone sampled 50 times per second is the fastest possible wiggle: it lands exactly on $\theta=\pi$, the top of the range. Nice to have in your head: **$f = f_s/2$ is the fastest digital wiggle** (the *Nyquist* frequency).

!!! example "What the exam asks about this"
    - Convert between $\omega$ and $f$ ($\omega = 2\pi f$).
    - Given $f$ and $f_s$, compute $\theta = 2\pi f/f_s$.
    - Recognise $A\sin(\omega t)$ as *periodic* (this decides energy vs power, section 0.5 → page 3.1).

---

## 0.3 Complex numbers and $e^{j\theta}$

**Plain words.** You do not need to like complex numbers. You only need one fact, and then one formula. The fact: **the exam writes cosines as complex exponentials because it makes the algebra shorter.** That is the entire reason. Nothing deeper.

**The fact.** $j$ is the symbol for $\sqrt{-1}$ (engineers write $j$, mathematicians write $i$; same thing). A complex number is a pair $(a,b)$ written $a+jb$, and it can be drawn as an arrow in a plane: $a$ to the right, $b$ up.

| Notation | Read as | Value |
|---|---|---|
| $z = a+jb$ | "z" | the number: right $a$, up $b$ |
| $j$ | "j" | $\sqrt{-1}$, so $j^2=-1$ |
| $z^*=a-jb$ | "z conjugate" | same number mirrored down |
| $\lvert z\rvert=\sqrt{a^2+b^2}$ | "magnitude of z" | the length of the arrow |
| $e^{j\theta}$ | "e to the j theta" | the arrow of length 1 at angle $\theta$ |

**The formula (Euler).** The arrow of length 1 at angle $\theta$ is exactly $\cos\theta + j\sin\theta$:

$$e^{j\theta}=\cos\theta+j\sin\theta,\qquad \lvert e^{j\theta}\rvert = 1$$

From it, adding and subtracting the two mirror images kills the sine part:

$$e^{j\theta}+e^{-j\theta}=2\cos\theta \qquad\Longrightarrow\qquad \boxed{\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2}}$$

and subtracting kills the cosine part: $e^{j\theta}-e^{-j\theta}=2j\sin\theta$.

**Why anyone bothers.** $\cos(\theta)$ is awkward to multiply and to raise to powers; $e^{j\theta}$ is trivial ($e^{j\theta}e^{j\phi}=e^{j(\theta+\phi)}$). So the course rewrites every tone as two complex exponentials, does easy algebra, and converts back. You will see $e^{-j k\theta}$ appear inside sums everywhere in Part 3 — it is just "a cosine in disguise".

**Squared magnitude, the thing you actually compute.** For any complex $w$, $\lvert w\rvert^2 = w\,w^*$. Example that appears on literally every spectral-estimation exam:

$$\lvert 1+ae^{-j\theta}\rvert^2=(1+ae^{-j\theta})(1+ae^{+j\theta}) = 1+a^2+a(e^{j\theta}+e^{-j\theta}) = 1+a^2+2a\cos\theta$$

which is a **real** number (no $j$ left), and that is why the answer always ends up as a formula in $\cos\theta$. Full details in the [Toolbox](toolbox.md#5-complex-exponentials-needed-for-every-psd).

---

## 0.4 The three calculations you keep meeting

### Integrals and sums: "how much in total"

- $\displaystyle\int_a^b f(t)\,dt$ = the **area** under $f(t)$ between $a$ and $b$. Used when time is continuous ($x(t)$).
- $\displaystyle\sum_{n=0}^{N-1} f[n]$ = **add up** the values $f[0]+f[1]+\dots+f[N-1]$. Used when time is discrete ($x[n]$).

They are the same idea ("total up a quantity over time"); one for smooth time, one for counted time. **$\sum$ goes with square brackets, $\int$ goes with round brackets.**

Worked example you will need on page 3.1:

$$\int_0^\infty e^{-2t}\,dt = \left[\frac{e^{-2t}}{-2}\right]_0^\infty = \frac{e^{-\infty}}{-2}-\frac{e^{0}}{-2} = 0-\Big(-\frac12\Big)=\frac12 .$$

Rules used (both in the [Toolbox](toolbox.md#4-the-integrals-that-keep-coming-back)): $\int e^{at}dt = e^{at}/a$, and $e^{-\infty}=0$.

### Limits: "what happens if you keep going forever"

$$\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}\dots dt$$

reads: "average over a window of length $T$, then let that window grow without bound". It is a *procedure*, not a scary object: compute the average for a window of length $T$, then see what value that average settles on as $T$ gets huge.

**The one limit fact you need:** for any fixed number $c$,

$$\lim_{T\to\infty}\frac{c}{T}=0 .$$

This single fact is why "finite energy ⟹ average power is zero" (page 3.1) and why "a cosine averaged over infinitely many periods gives exactly half its peak-square" (next).

### The geometric series: "add up a shrinking list"

$$\sum_{n=0}^{\infty} r^n = 1 + r + r^2 + \dots = \frac{1}{1-r}\qquad\text{for } \lvert r\rvert < 1$$

Where it comes from: the finite sum is $1+r+\dots+r^N = \dfrac{1-r^{N+1}}{1-r}$ (multiply by $(1-r)$ and watch everything cancel). If $\lvert r\rvert<1$ then $r^{N+1}\to 0$, leaving $\frac{1}{1-r}$.

**Worked example (an exam answer, exactly):** $E=\sum_{n=0}^\infty e^{-2n}$ is a geometric series with $r=e^{-2}\approx0.135$:

$$E = \frac{1}{1-e^{-2}} = \frac{1}{1-0.1353} = \frac{1}{0.8647}\approx 1.1565 .$$

### Trig identities: the two that appear in every energy calculation

Start from $\cos(2\alpha) = 1-2\sin^2\alpha$ and rearrange:

$$\boxed{\sin^2\alpha = \frac{1-\cos(2\alpha)}{2}}\qquad\qquad \boxed{\cos^2\alpha = \frac{1+\cos(2\alpha)}{2}}$$

Why these matter: energy and power formulas contain $x(t)^2$, and squaring a sine gives you $\sin^2$, which the identity splits into **a constant ($\tfrac12$) plus a wiggle at double frequency ($\cos 2\alpha$)**. The constant is what survives averaging; the wiggle averages to zero. That is the whole trick behind "$P = A^2/2$".

---

## 0.5 Spectrum: what a Fourier transform tells you

**Plain words.** Any signal can be described as "a mixture of pure tones of different frequencies". The **spectrum** of a signal is the recipe: *how much of each frequency is in there*. A tone at 250 Hz and nothing else has a spectrum with a single bump at 250 Hz. Two tones = two bumps. Noise = a flat smear over all frequencies.

The **Fourier transform** is the machine that turns "signal vs time" into "recipe vs frequency". It is a *change of description*, nothing is lost or added — same signal, different label on the horizontal axis.

| Name | Symbol | Input | Output | Used for |
|---|---|---|---|---|
| **FTD** (Fourier transform for discrete-time signals) | $X(e^{j\theta}) = \sum_n x[n]\,e^{-jn\theta}$ | the whole infinite list $x[n]$ | a **continuous curve** in $\theta\in[-\pi,\pi]$ | theory; what the true spectrum *is* |
| **DFT** (discrete Fourier transform) | $X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}$ | your **$N$ recorded samples** | **$N$ numbers** | what a computer can actually compute |

Three things worth memorising about this pair:

1. **The FTD is a curve, the DFT is a list of $N$ numbers that samples that curve.** The exam draws both in the same figure and asks you to match them (that is question 3a of January 2022).
2. **$\theta$ is "frequency" in radians per sample**, and $\theta = 2\pi f/f_s$, so $\theta=\pi$ ↔ $f = f_s/2$ (the fastest wiggle, section 0.2).
3. A pure, never-ending cosine of amplitude $A$ has exactly **two** infinitely thin spikes in its spectrum, at $\theta = \pm\theta_0$, each of height $\propto A/2$. Two, because $\cos\theta = \tfrac12(e^{j\theta}+e^{-j\theta})$: one spike for each of the two complex exponentials. This is why every spectrum picture of a cosine shows a peak on the left *and* one mirrored on the right.

**DFT bins.** The $N$ DFT values sit at evenly spaced frequencies. The spacing is

$$\text{bin width} = \frac{f_s}{N}\ \text{Hz}.$$

Example: $f_s = 50$ Hz and $N = 24$ samples → $\frac{50}{24}\approx 2.08$ Hz apart. The $k$-th number $X[k]$ is "how much of the tone at frequency $k\cdot 2.08$ Hz is present". *Bin* = one of those $N$ frequency slots.

**Decibels (dB).** Spectra figures are drawn on a log scale: $\lvert X\rvert_{\text{dB}} = 20\log_{10}\lvert X\rvert$. So 0 dB = height 1, −20 dB = height 0.1, −40 dB = height 0.01. When a figure says "the weak tone is 34 dB below the strong one", it means its amplitude is about $10^{-34/20}\approx 0.02$ times the big one. dB exists purely so you can see tiny and huge things in the same plot.

---

## 0.6 Word book (everything else the guide says without warning)

| Word | What it means here |
|---|---|
| **tone / component** | one pure cosine (a single-frequency wiggle) inside a signal |
| **periodic** | repeats forever: $x(t+T)=x(t)$ for some fixed $T$ (sines, cosines, any repeating pattern) |
| **stationary** | "random, but its statistical properties (mean, power) do not change over time" — the random-signal version of "same forever" |
| **lag $l$** | how much you shift a signal before comparing it with itself ($l$ samples back) |
| **autocorrelation $r[l]$** | "how similar is the signal to itself $l$ steps later", on average. $r[0]$ = average power |
| **PSD** (power spectral density) | the spectrum for random signals: how the *power* is spread over frequencies |
| **convolution** | "smear one thing with another". Multiplying signals in time = smearing (convolving) their spectra. You never compute one by hand in this course; you only use the *consequence* |
| **main lobe** | the big central bump of a window's spectrum (page 3.1) |
| **side lobes** | the smaller ripples left and right of the main lobe (page 3.1) |
| **resolution** | ability to see two nearby tones as two separate peaks |
| **leakage** | power of one tone showing up at wrong frequencies, hiding weaker tones |
| **bias** | an estimator is biased if it is wrong *on average* (systematically) |
| **variance** | how much an estimator jumps around between different datasets |
| **MLE / MAP / MMSE** | three recipes for guessing a number from data (Part 2) |
| **hypothesis $\mathcal H_0/\mathcal H_1$** | "$\mathcal H_0$ = nothing is there", "$\mathcal H_1$ = the signal/event is there" (Part 4) |
| **$P_{FA}$ / $P_D$** | probability of false alarm / probability of detection (Part 4) |

---

## Where to go next

- Doing **Part 3** (start with [3.1 Signals, windows, zero padding](p3-windows.md)): sections 0.1, 0.2, 0.4, 0.5 of this page are everything you need.
- Doing **Part 2** (estimation): section 0.4 (derivatives + logs → [Toolbox](toolbox.md#2-logs-and-exponentials)) and the word book.
- Doing **Part 1** (probability) or **Part 4** (detection): the word book, plus [1.2 Random variables & joint PDFs](p1-rv.md) which builds probability from zero.

*[signal]: a number that changes over time, e.g. a voltage or a measurement per second.
*[sample]: one recorded number of a discrete-time signal, $x[n]$ at a given integer $n$.
*[sample rate]: $f_s$, how many numbers per second are recorded; $T_s = 1/f_s$ seconds apart.
*[Hz]: hertz, cycles per second.
*[tone]: a single pure cosine/sine wiggle at one frequency.
*[spectrum]: the recipe of how much of each frequency a signal contains.
*[FTD]: Fourier transform for discrete-time signals, $X(e^{j\theta})=\sum_n x[n]e^{-jn\theta}$: a continuous curve over frequency.
*[DFT]: discrete Fourier transform: the $N$ numbers you compute from $N$ samples; samples of the FTD.
*[bin]: one of the $N$ evenly spaced frequency slots of a DFT; width $f_s/N$ Hz.
*[dB]: decibel, a logarithmic scale for magnitudes: $20\log_{10}|X|$.
*[convolution]: smearing one function with another; multiplying in time equals convolving in frequency.
*[PSD]: power spectral density: how a random signal's power is spread over frequency.
