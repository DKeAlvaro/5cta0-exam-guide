# 3.3 Periodogram, Bartlett, Welch and the theory questions

<div class="meta"><span class="hot">In 8 of 9 exams</span><span>0.25–1 point</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep4_quiz.mp4" poster="video/pod_ep4_quiz.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 4, Rapid-fire true or false</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

Multiple choice ("which statement is TRUE"), a **matching table** (which estimator does what), a quick **"how many Welch segments"** count, and once an **energy vs power** signal. All of it is a small set of facts. Learn the facts, then do the cards at the bottom until you get them all right.

## The methods in one table

The task is always the same: from $N$ measured samples, estimate the PSD (how the power is spread over frequency).

<div class="key" markdown>

| method | what it does | the catch |
|---|---|---|
| **Periodogram** | $\frac1N\lvert\text{DFT of the }N\text{ samples}\rvert^2$ | very noisy, and **more data does not make it calmer** (variance does not go to 0: *not consistent*) |
| **Correlogram** | DFT of the estimated $r[k]$ ([3.1](e3-corr.md)) | same problems as the periodogram |
| **Bartlett** | cut the data into $K$ **non-overlapping** pieces, periodogram of each, **average** | variance ÷ $K$, but each piece is shorter → worse resolution, more bias |
| **Welch** (= WOSA) | like Bartlett but pieces **overlap** and each is **windowed** | more pieces from the same data |
| **Blackman–Tukey** | estimate $r[k]$, multiply it by a window of $M\lt L$ lags, then DFT | smoother; consistent |
| **Parametric** (AR, MA, ARMA) | fit a model ([3.2](e3-arma.md)), PSD from its formula | good only if the model fits |

</div>

<figure class="anim"><video class="anim" src="video/periodogram_average.mp4" poster="video/periodogram_average.jpg" muted loop playsinline controls preload="none"></video><figcaption><b>Animation: the problem and the fix.</b> First $N$ grows from 64 to 4096: the periodogram gets denser, not calmer. Then the same samples are cut into $K=4,16,64$ pieces whose periodograms are averaged (Bartlett): the curve settles onto the true value 1. The price is coarser frequency resolution.</figcaption></figure>

## Counting Welch segments

Segment length $L$, overlap means each new segment starts $D$ samples after the previous one ($D=L$ with no overlap, $D=L/2$ with 50 %). Watch the segments being laid down:

<div class="widget" data-w="welch"></div>

!!! recipe key "Segments and variance"
    $$K=\frac{N-L}{D}+1,\qquad \frac{\text{Var(average of }K)}{\text{Var(one periodogram)}}\approx\frac1K\ \ \text{(if the segments are independent)}.$$

**June 2026 · 3b** ($N=1000$, $L=200$, 50 % overlap, *final answer only*): $D=100$, $K=\frac{800}{100}+1=\mathbf 9$, ratio $\mathbf{1/9}\approx0.11$.

## Windows and zero padding

Recording only $N$ samples = multiplying the signal by a **window**. In the spectrum, every pure tone then becomes a copy of the window's spectrum: a **main lobe** (a hump) plus **side lobes** (ripples).

<div class="key" markdown>

- **Main lobe width → resolution.** Narrow main lobe = two close tones can be told apart.
- **Side lobe height → leakage.** High side lobes = power leaks to other frequencies and can bury a weak tone.
- **Rectangular** window (just cutting): narrowest main lobe (best resolution) but highest side lobes (most leakage). **Hamming, Hann, triangular**: lower side lobes, wider main lobe.
- **Longer window** (more samples) → narrower main lobe → better resolution. It does **not** lower the side lobes of a rectangular window.
- **Zero padding** (adding zeros before the DFT) only gives **more dots on the same curve**. It does **not** improve resolution.

</div>

<figure class="anim"><video class="anim" src="video/windowing.mp4" poster="video/windowing.jpg" muted loop playsinline controls preload="none"></video><figcaption><b>Animation: windowing.</b> A strong tone plus a tone 100 times weaker. As $N$ grows the main lobe narrows, but the rectangular window's side lobes stay high and bury the weak tone. Switching to a Hann window lowers the side lobes and the weak tone appears; its main lobe is wider.</figcaption></figure>

<figure class="anim"><video class="anim" src="video/zero_pad.mp4" poster="video/zero_pad.jpg" muted loop playsinline controls preload="none"></video><figcaption><b>Animation: zero padding.</b> 16 real samples followed by more and more zeros. The DFT dots get denser but never leave the same grey curve. Only more <i>real</i> samples (green, at the end) make the peak narrower.</figcaption></figure>

## Energy or power signal (April 2025 · 3a)

- **Energy** $E=\sum_n|x[n]|^2$ (or $\int|x(t)|^2dt$): the total.
- **Power** $P$ = energy per unit time, averaged over all time.
- Finite energy → **energy signal**, and then $P=0$. Infinite energy but finite power → **power signal**.

| signal | type | $E$ | $P$ |
|---|---|---|---|
| $A\sin(\omega t)$ (goes on forever) | power | $\infty$ | $\frac{A^2}{2}$ (average of $\sin^2$ is $\frac12$) |
| $e^{-n}$ for $n\ge0$ | energy | $\sum_{n\ge0}e^{-2n}=\frac1{1-e^{-2}}\approx1.157$ (geometric series with ratio $e^{-2}$) | $0$ |

<figure class="anim"><video class="anim" src="video/energy_power.mp4" poster="video/energy_power.jpg" muted loop playsinline controls preload="none"></video><figcaption><b>Animation: the two formulas, live.</b> A window grows. Top right: the energy inside it. A dying signal (blue) levels off; a tone (red) keeps climbing. Bottom right: energy divided by the window length, the power. Blue sinks to 0; red settles on $\frac{A^2}{2}$.</figcaption></figure>

## Model order (June 2026 · 3e)

- Raising the AR order $p$ **always lowers** the residual error on your data. The risk is **overfitting**: the model starts fitting the noise (spurious peaks).
- **AIC** (Akaike) $=N\ln\hat\sigma^2+2p$, or **FPE**, add a penalty that grows with $p$: choose the $p$ where the criterion is smallest.
- Any spectrum (even an MA one with deep nulls) can be approximated by an AR model **of high enough order**.

## Test yourself

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| The periodogram is not a consistent estimator: its variance does not go to 0 as $N\to\infty$. | T | June 2026 3a. More data gives more dots, not calmer dots. |
| Increasing the data length decreases spectral leakage. | F | It narrows the main lobe (resolution). Side lobes, i.e. leakage, depend on the window **shape**. |
| A Hamming window improves the frequency resolution (main lobe width). | F | It lowers side lobes (less leakage) but **widens** the main lobe: worse resolution. |
| Bartlett's method lowers the variance by zero-padding. | F | By **averaging** periodograms of segments. |
| Zero padding before the DFT improves the ability to separate two close peaks. | F | Only denser sampling of the same curve. Resolution needs more real data. |
| Main lobe width sets the resolution; side lobe height sets the leakage. | T | Nov 2022 3b. |
| Given the same length, a triangular window gives higher resolution than a rectangular one. | F | Rectangular has the narrowest main lobe. |
| Bias in the spectral estimate affects both deterministic and stochastic signals. | T | April 2025 3b. Windowing smears any spectrum. |
| The window type affects both bias and variance of the raw periodogram. | F | It changes the bias (smearing), not the variance of the raw periodogram. |
| Bartlett with $K$ segments: variance ÷ $K$, but bias increases. | T | Nov 2022 3a. Shorter segments = more smearing. |
| Bartlett with $K$ segments: variance ÷ $K$ and the bias also decreases. | F | Bias gets worse, not better. |
| Welch = averaging periodograms of **overlapping** (windowed) segments. | T | Bartlett = non-overlapping. |
| Blackman–Tukey = DFT of the windowed autocorrelation estimate. | T | April 2025 3c, line 4. |
| Raising the AR order keeps lowering the residual error, so the highest order is best. | F | Overfitting. Use AIC/FPE. |

</div>

!!! exam "Final exam, 13 April 2025 · 3c · 0.5 p (matching table)"
    1. Non-overlapping segments, average their periodograms. 2. $\frac1N|\text{N-point DFT}|^2$. 3. Model $\sigma_i^2\left|\frac{1+\sum b_qe^{-jq\theta}}{1+\sum a_pe^{-jp\theta}}\right|^2$. 4. DFT of the estimated autocorrelation after a window of length $M\lt L$. 5. Overlapping segments, average their periodograms.

??? solution "Check your answer"
    !!! answer "Answer"
        1 Bartlett · 2 Periodogram · 3 ARMA (parametric) · 4 Blackman–Tukey · 5 Welch
