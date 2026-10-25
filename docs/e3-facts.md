# 3.3 Periodogram, Bartlett, Welch and the theory questions

<div class="meta"><span class="hot">In 8 of 9 exams</span><span>0.25–1 point</span><span>30 min</span></div>

<figure class="pod"><video src="video/pod_ep2_spectra.mp4" poster="video/pod_ep2_spectra.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 2</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

The **periodogram** is the obvious thing: take the DFT of the data, take $|\cdot|^2$, divide by $N$. It is a good estimate of the shape of the spectrum and a **bad** estimate of its height, because its variance does not shrink when you collect more data. That is the single fact half of these questions are about.

Every other method is a way of averaging to kill that variance: **Bartlett** splits the data into non-overlapping chunks, **Welch** does the same but overlapping and windowed, **Blackman–Tukey** windows the autocorrelation instead. Averaging kills variance but **costs bias** — that trade is the other half.

## How to fight this section with the sheet

This page is not one recipe, it is **five boxes**: 3F, 3G, 3H, 3I, 3J. Read the first words of the question and it tells you which one to open.

| the question starts with | open |
|---|---|
| "how many segments $K$", "overlap … %", "ratio of the variance" | **box 3G** |
| "energy or power signal", "total energy", "average power" | **box 3H** |
| "fill in the table", "which PSD estimator", "name the method" | **box 3I** |
| "which plot", "which figure", "match the plot" | **box 3F** |
| "which of the following statements" | **box 3J** |

!!! sheet "Boxes 3F–3J, exactly as they are printed on the sheet"
    **3F · Pick the plot.** Work out each PSD at $\theta=0$ (all cosines $=1$) and at $\theta=\pi$ ($\cos\theta=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Pick the plot with those heights. Only a correlogram can go below 0.

    **3G · Welch / Bartlett count.** Step $D=L\times(1-\text{overlap})$. Segments $K=\dfrac{N-L}{D}+1$ (round the fraction down). Variance ratio vs one periodogram $=\dfrac1K$. Bartlett (no overlap): $K=\dfrac NL$.

    *Jun26* $N=1000$, $L=200$, 50 %: $D=100$, $K=9$, ratio $\frac19$.

    **3H · Energy or power signal.**
    - Dies out or has finite length → **energy**: $E=\sum\lvert x\rvert^2$ is finite, power $=0$.
    - Never dies out (sin, cos, constant, $\cos t\,u(t)$) → **power**: $P$ = time average of $\lvert x\rvert^2$, energy $=\infty$.
    - Time-continuous ($t$) → $\sum$ becomes $\int dt$: $E=\int\lvert x\rvert^2dt$, $P=\frac1T\int_0^T\lvert x\rvert^2dt$.

    *Apr25:* $A\sin\omega t$ → power $\frac{A^2}2$. $e^{-n}$ for $n\ge0$ → energy $\sum e^{-2n}=\frac1{1-e^{-2}}\approx1.16$.

    **3I · Name the method.**

    | The description says… | Method |
    |---|---|
    | $\lvert\text{DFT}\rvert^2$ divided by $N$, whole signal | Periodogram |
    | DFT of the estimated autocorrelation | Correlogram |
    | …plus a window of length $M\lt L$ on the autocorrelation; "consistent" | Blackman–Tukey |
    | NON-overlapping segments, average the periodograms | Bartlett |
    | OVERLAPPING segments, average the periodograms | Welch (WOSA) |
    | $\sigma^2\lvert B\rvert^2/\lvert A\rvert^2$, "linear random signal model" | Parametric (AR / MA / ARMA) |
    | "averages periodograms" | Bartlett and Welch |

    **3J · Part 3 true / false.**

    | Statement | T / F |
    |---|---|
    | Periodogram NOT consistent: variance does not go to 0 as $N\to\infty$ | T (Jun26 b) |
    | Bias affects deterministic and stochastic signals | T (Apr25 a) |
    | Bartlett: variance drops like $\frac1K$, but bias increases | T (Nov22 a) |
    | Welch/WOSA: variance drops exactly $\frac1K$ | F (overlapping segments are correlated) |
    | Main-lobe width → resolution; side-lobe height → leakage | T (Nov22 b) |
    | A window (Hamming…) improves resolution | F (it lowers leakage; rectangular = best resolution) |
    | Triangular window: better resolution than rectangular | F |
    | Longer data or window reduces leakage | F |
    | Zero-padding improves resolution | F (only more points, step $\frac{2\pi}L$) |
    | Bartlett reduces variance by zero-padding | F (it splits the data) |
    | Window type changes the periodogram's variance | F |
    | Periodogram better bias than correlogram | F (they are the same) |

    **AR order (Jun26-3e).** Bigger $p$ → residual error always goes down → risk: **overfitting** (fake peaks). Fix: **AIC** $=N\ln\hat\sigma^2+2p$ (also FPE, MDL): the error term falls, the penalty $2p$ grows → choose the $p$ with the smallest AIC. Any PSD can be approximated by an AR model of **high enough order**.

Two more sheet places you will need: the **Numbers** strip for $e^{-2}=0.135$ and $\sqrt{2\pi}$, and the **Calculations** strip for $\sum_{n\ge0}q^n=\frac1{1-q}$. Both appear in the energy questions.

## 1 · June 2026 · 3b — the Welch count. Read this one with the sheet next to you

!!! exam "Resit, June 2026 · 3b · 0.5 p"
    You are given a data record of $N = 1000$ samples. You want to estimate the power spectral density using Welch's method to reduce the variance of your estimate. You choose a segment length of $L = 200$ samples and an overlap of 50%.

    **Please provide only the final answer. The workout will not be checked.**

    1. How many segments $K$ will be averaged? [0.25]
    2. With the simplifying assumption that the segments are statistically independent, what is the ratio of the variance of your Welch estimate to the variance of a single standard periodogram of length $L$? [0.25]

!!! sheet "In the cheat sheet: box 3G, both lines"
    <div class="stepper" markdown>

    **Sheet step 1 · "Step $D=L\times(1-\text{overlap})$."**
    $L=200$, overlap $=50\%=0.5$:

    $$D=200\times(1-0.5)=200\times0.5=100$$

    $D$ is how far the window jumps between segments: 200 long, but only 100 new samples each time.

    ***

    **Sheet step 2 · "Segments $K=\dfrac{N-L}{D}+1$."**
    $$K=\frac{1000-200}{100}+1=\frac{800}{100}+1=8+1=\mathbf 9$$

    Sanity: segments start at samples 0, 100, 200, …, 800 — that is 9 starts, and the last one runs 800…999 ✓.

    ***

    **Sheet step 3 · "Variance ratio vs one periodogram $=\dfrac1K$."**
    $$\frac{\mathrm{Var}_{Welch}}{\mathrm{Var}_{single}}=\frac19\approx\mathbf{0.11}$$

    ***

    **Sheet check.**
    The sheet prints this exact question as its *Jun26* line. Also: "round the fraction down" only matters if $\frac{N-L}{D}$ is not a whole number — here it is.

    </div>

!!! answer "Answer"
    1. $K=9$ · 2. ratio $=\dfrac19\approx 0.11$

## 2 · April 2025 · 3a — energy or power

!!! exam "Final exam, 13 April 2025 · 3a · 0.5 p"
    For each of the following signals, indicate whether they are energy or power signals, and provide their total energy and average power.

    ***Provide only the final answer. The workout will not be checked.***

    1. $x(t) = A \sin(\omega t)$, with $A, \omega$ being the fixed amplitude and frequency, respectively.
    2. $x[n] = e^{-n}$ for $n \geq 0$, and $x[n] = 0$ elsewhere.

!!! sheet "In the cheat sheet: box 3H + the Calculations strip"
    <div class="stepper" markdown>

    **Sheet step 1 · the box's first question: does it die out?**
    $A\sin(\omega t)$ oscillates forever → "Never dies out (sin, cos, constant…)" → **power**. $e^{-n}$ for $n\ge0$ shrinks to 0 → **energy**.

    ***

    **Sheet step 2 · signal 1: "Time-continuous ($t$) → $\int dt$".**
    Power = time average of $|x|^2$ over one period $T=\frac{2\pi}{\omega}$:

    $$P=\frac1T\int_0^T A^2\sin^2(\omega t)\,dt=\frac{A^2}{2}$$

    (The average of $\sin^2$ over a full period is $\frac12$.) Energy $=\infty$ — that is what "power signal" means.

    ***

    **Sheet step 3 · signal 2: "Energy: $E=\sum|x|^2$ is finite".**
    $$E=\sum_{n=0}^{\infty}\big(e^{-n}\big)^2=\sum_{n\ge0}\big(e^{-2}\big)^{n}$$
    The Calculations strip: $\sum_{n\ge0}q^n=\frac1{1-q}$ for $|q|\lt1$, with $q=e^{-2}=0.1353$ (Numbers strip):

    $$E=\frac{1}{1-e^{-2}}=\frac{1}{1-0.1353}=\frac{1}{0.8647}=1.1565\approx\mathbf{1.16}$$

    Power $=0$ — that is what "energy signal" means.

    ***

    **Sheet check · the sheet's example line.**
    *Apr25:* "$A\sin\omega t$ → power $\frac{A^2}2$. $e^{-n}$ for $n\ge0$ → energy $\sum e^{-2n}=\frac1{1-e^{-2}}\approx1.16$" — identical.

    </div>

!!! answer "Answer"
    1. **Power**: $E=\infty$, $P=\dfrac{A^2}{2}$ · 2. **Energy**: $E=\dfrac{1}{1-e^{-2}}\approx 1.16$, $P=0$

## 3 · Q2 2023-24 · 3a — the same rule, four signals in a table

!!! exam "Q2 2023-24 resit · 3a"
    For the signals in the table below, please indicate whether they are energy or power signals, Note that $u(t)$ represents the unit step function.

    | Signal | Energy or Power? |
    |---|---|
    | $x(t) = e^{-t}u(t)$ | |
    | $x(t) = \cos(t)u(t)$ | |
    | $x(t) = 5 \text{ for } -2 \leq t \leq 2, \text{ zero elsewhere.}$ | |
    | $x(t) = 5e^{-2\lvert t\rvert}$ | |

!!! sheet "In the cheat sheet: box 3H, one bullet per row"
    <div class="stepper" markdown>

    **Row 1 · $e^{-t}u(t)$** — dies out as $t\to\infty$ → **energy**. (The $u(t)$ only switches it on at $t=0$; it still decays.)

    ***

    **Row 2 · $\cos(t)u(t)$** — the sheet lists this one by name: *"Never dies out (sin, cos, constant, $\cos t\,u(t)$)"* → **power**. The step function starts it, but it then oscillates for ever with constant amplitude.

    ***

    **Row 3 · $5$ on $-2\le t\le2$, zero elsewhere** — "has finite length" → **energy**. ($E=\int_{-2}^{2}25\,dt=100$ if they ask for the number.)

    ***

    **Row 4 · $5e^{-2|t|}$** — dies out on both sides → **energy**.

    ***

    **Sheet check · the trap.**
    $u(t)$ does **not** turn a signal into a power signal on its own. What matters is whether $|x|^2$ has finite total area.

    </div>

!!! answer "Answer"
    Energy · Power · Energy · Energy

## 4 · April 2025 · 3c — name the method, one answer per row

!!! exam "Final exam, 13 April 2025 · 3c · 0.5 p"
    In the table below, fill in to which power spectral density (PSD) estimator each statement is referring. **Note: only one answer is correct for each statement.**

    | Statement | PSD-estimator |
    |---|---|
    | 1. PSD is estimated by dividing the total signal length in different non-overlapping segments, and averaging the periodograms obtained on each segement. | |
    | 2. PSD is estimated by calculating the modulus squared of the N-point DFT of the random signal, and dividing by the signal length N. | |
    | 3. PSD is estimated by using a model of the form $P(e^{j\theta}) = \sigma_i^2 \left\lvert \frac{1 + \sum_q b_q e^{-jq\theta}}{1 + \sum_p a_p e^{-jp\theta}} \right\rvert^2$ | |
    | 4. PSD is estimated by calculating the L-point DFT of the estimated autocorrelation function of the signal (L=number of lags), after applying a window of length M\lt L to the autocorrelation function. | |
    | 5. PSD is estimated by dividing the total signal length in different overlapping segments, and averaging the periodograms obtained on each segment. | |

!!! sheet "In the cheat sheet: box 3I, the row that matches"
    <div class="stepper" markdown>

    **Sheet step 1 · row 1 — "NON-overlapping segments, average the periodograms"** → **Bartlett**.
    The word "non-overlapping" is the whole discriminator.

    ***

    **Sheet step 2 · row 2 — "$\lvert\text{DFT}\rvert^2$ divided by $N$, whole signal"** → **Periodogram**.

    ***

    **Sheet step 3 · row 3 — "$\sigma^2\lvert B\rvert^2/\lvert A\rvert^2$"** → **Parametric (AR / MA / ARMA)**.
    The exam's $\sigma_i^2\big\lvert\frac{1+\sum b_q e^{-jq\theta}}{1+\sum a_p e^{-jp\theta}}\big\rvert^2$ is exactly $\sigma^2|B|^2/|A|^2$.

    ***

    **Sheet step 4 · row 4 — "…plus a window of length $M\lt L$ on the autocorrelation"** → **Blackman–Tukey**.
    "DFT of the estimated autocorrelation" alone would be the correlogram; the extra lag window is what makes it Blackman–Tukey.

    ***

    **Sheet step 5 · row 5 — "OVERLAPPING segments, average the periodograms"** → **Welch (WOSA)**.

    </div>

!!! answer "Answer"
    1 Bartlett · 2 Periodogram · 3 ARMA (parametric) · 4 Blackman–Tukey · 5 Welch (WOSA)

## 5 · April 2024 · 3a — the same table, but several answers allowed

!!! exam "Final exam, April 2024 · 3a · 0.9 p"
    Indicate which spectral estimation method(s) fit each of the following description. Multiple answer are possible, and answer can be repeated. If multiple answers are possible, please indicate them all.

    | | Description | Method(s) |
    |---|---|---|
    | 1 | Estimates the power spectral density by modeling the random signal as a linear random signal model. | |
    | 2 | Divides the signal into segments, allowing overlap between the segments. | |
    | 3 | Is a consistent estimator of the power spectral density. | |
    | 4 | Estimates the power spectrum as the Fourier transform of the autocorrelation function. | |
    | 5 | The bias of the power spectral density estimate is proportional to the square of the true spectrum. | |
    | 6 | Averages multiple periodogram estimates. | |

!!! sheet "In the cheat sheet: box 3I — and the last two rows need a second look"
    <div class="stepper" markdown>

    **1 · "linear random signal model"** → box 3I's row: **AR / MA / ARMA (parametric)**.

    ***

    **2 · "allowing overlap"** → **Welch**. (Non-overlapping would be Bartlett.)

    ***

    **3 · "consistent"** → box 3I tags this word on **Blackman–Tukey**. Bartlett and Welch also become consistent as $K\to\infty$, so list those too if the space allows: **Blackman–Tukey (+ Bartlett, Welch with $K\to\infty$)**.

    ***

    **4 · "Fourier transform of the autocorrelation function"** → **correlogram** and **Blackman–Tukey** (both are an FT of $\hat r$; BT just windows it first).

    ***

    **5 · "bias proportional to the square of the true spectrum"** → **none, as written.** The periodogram's and correlogram's *variance* is $\propto P^2$, not their bias. Say so rather than guessing.

    ***

    **6 · "averages multiple periodogram estimates"** → box 3I's last row: **Bartlett and Welch**.

    </div>

!!! answer "Answer"
    1 AR/MA/ARMA · 2 Welch · 3 Blackman–Tukey (+ Bartlett, Welch with $K\to\infty$) · 4 correlogram, Blackman–Tukey · 5 none as written (the $\propto P^2$ is the *variance*) · 6 Bartlett, Welch

## 6 · November 2019 · 1c — the big table, 1.5 points

!!! exam "Written exam, November 2019 · 1c · 1.5 p"
    Complete Table 2, which provides an overview of non-parametric spectral estimation methods. Answers can be descriptive. In other words, formulas are not necessary. Please use the template table in the answer sheet and limit your answers to the assigned space in each entry of the table.

    | | Description (basic idea) | Bias | Variance |
    |---|---|---|---|
    | Periodogram | | | |
    | Correlogram | | | |
    | Bartlett's periodogram | | | |
    | WOSA | | | |
    | Blackman-Tukey | | | |

!!! sheet "In the cheat sheet: box 3I gives the idea column; box 3J gives the other two"
    <div class="stepper" markdown>

    **Sheet step 1 · the "basic idea" column = box 3I's left column, written in words.**
    Periodogram: $\frac1N|\text{FT of the data}|^2$ · Correlogram: FT of $\hat r[k]$ · Bartlett: average $K$ periodograms of non-overlapping segments · WOSA (Welch): average periodograms of **overlapping, windowed** segments · Blackman–Tukey: window $\hat r[l]$ with a short lag window, then FT.

    ***

    **Sheet step 2 · the bias column.**
    Periodogram and correlogram are the **same** estimator (box 3J: "Periodogram better bias than correlogram → F"), both smoothed by a triangular window, asymptotically unbiased.
    Bartlett: **larger** bias (segments of length $M=N/K$ → resolution $\approx\frac{2\pi}M$).
    WOSA: larger than raw, but **less** than Bartlett (its segments are longer).
    Blackman–Tukey: larger for a shorter lag window $M$.

    ***

    **Sheet step 3 · the variance column.**
    Periodogram and correlogram: $\propto P^2$ and **not consistent** (box 3J's first row).
    Bartlett: $\approx P^2/K$ — the $\frac1K$ row.
    WOSA: reduced, but **not** $\frac1K$ (overlapping segments are correlated).
    Blackman–Tukey: $\approx\frac{P^2}{N}\sum w^2[l]\to0$ → **consistent**.

    </div>

!!! answer "Answer"

    | | Description (basic idea) | Bias | Variance |
    |---|---|---|---|
    | Periodogram | $\frac1N\lvert\text{FT of the data}\rvert^2$ | smoothed by a triangular window; asymptotically unbiased | $\propto P^2$; does not decrease with $N$ (not consistent) |
    | Correlogram | FT of the estimated autocorrelation (lags up to $N-1$) | same as the periodogram | $\propto P^2$, not consistent |
    | Bartlett | average $K$ periodograms of non-overlapping segments of length $M=N/K$ | larger (resolution $\approx2\pi/M$) | $\approx P^2/K$ |
    | WOSA (Welch) | average periodograms of overlapping, windowed segments | larger than raw, but less than Bartlett | reduced, but not as $1/K$ (correlated segments) |
    | Blackman–Tukey | window $\hat r[l]$ with a short lag window ($M\ll N$), then FT | larger for shorter $M$ | $\approx\frac{P^2}{N}\sum w^2[l]\to0$: consistent |

## 7 · June 2026 · 3a — true/false, read the row

!!! exam "Resit, June 2026 · 3a · 0.25 p"
    Which of the following statements regarding the standard periodogram as an estimator of the Power Spectral Density (PSD) is TRUE?

    - a) Increasing the length of the data window on which the periodogram is calculated decreases spectral leakage
    - b) The periodogram is not a consistent estimator because its variance does not tend to zero as the data record length $N \rightarrow \infty$.
    - c) Applying a data window (e.g., a Hamming window) improves the frequency resolution (main lobe width) of the periodogram.
    - d) Bartlett's method decreases the variance of the periodogram by zero-padding the original sequence.

!!! sheet "In the cheat sheet: box 3J, four rows"
    <div class="stepper" markdown>

    **Sheet step 1 · (b) is the sheet's very first row** — *"Periodogram NOT consistent: variance does not go to 0 as $N\to\infty$"* → **T (Jun26 b)**. The sheet tags this exam.

    ***

    **Sheet step 2 · (a) vs "Longer data or window reduces leakage" → F.**

    ***

    **Sheet step 3 · (c) vs "A window (Hamming…) improves resolution" → F** (it lowers **leakage**; rectangular has the best resolution).

    ***

    **Sheet step 4 · (d) vs "Bartlett reduces variance by zero-padding" → F** (it splits the data into segments).

    </div>

!!! answer "Answer"
    **(b)**

## 8 · April 2025 · 3b and November 2022 · 3a — the bias/variance trade

!!! exam "Final exam, 13 April 2025 · 3b · 0.25 p"
    Which of the following statements on spectral estimation is TRUE?

    - a) The problem of bias in the spectral estimate affects both deterministic and stochastic signals.
    - b) Zero-padding prior to applying the discrete Fourier transform can improve the spectral resolution of the spectral estimate, i.e. the ability to distinguish spectral peaks.
    - c) The "raw" periodogram achieves better performance in terms of bias, but worse in terms of variance compared to the "raw" correlogram.
    - d) The type of window used to window the signal affects both the bias and the variance of the spectral estimate obtained using the "raw" periodogram.

!!! exam "Final exam, November 2022 · 3a · 0.25 p"
    In the context of non-parametric spectral estimation, which of the following statements is TRUE?

    - a) Compared to the periodogram, the Bartlett method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. However, the bias increases.
    - b) Compared to the periodogram, the WOSA method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. However, the bias increases.
    - c) Compared to the periodogram, the Bartlett method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. The bias also decreases, but not proportionally to 1/K.
    - d) Compared to the periodogram, the WOSA method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. The bias also decreases, but not proportionally to 1/K.

!!! sheet "In the cheat sheet: box 3J, two rows each"
    <div class="stepper" markdown>

    **April 2025 · (a) is the row *"Bias affects deterministic and stochastic signals"* → T (Apr25 a).**
    (b) is *"Zero-padding improves resolution"* → F. (c) is *"Periodogram better bias than correlogram"* → F (they are the same). (d) is *"Window type changes the periodogram's variance"* → F.

    ***

    **November 2022 · (a) is the row *"Bartlett: variance drops like $\frac1K$, but bias increases"* → T (Nov22 a).**
    (b) and (d) are the *"Welch/WOSA: variance drops exactly $\frac1K$"* → F row: overlapping segments are **correlated**, so the drop is not $\frac1K$. (c) says the bias *decreases* — it increases.

    ***

    **Sheet check.**
    Both papers ask the same trade: averaging kills variance and costs bias. $\frac1K$ is a Bartlett statement only.

    </div>

!!! answer "Answer"
    April 2025 → **(a)** · November 2022 → **(a)**

## 9 · January 2019 · 1c — "which ones are true", so read all four

!!! exam "Retake, January 2019 · 1c · 0.5 p"
    In the context of non-parametric spectral estimation methods, which ones of the following statements are true?

    - A. In Bartlett's method, the bias of the estimated power spectrum increases as the length of the window $M$ of each raw periodogram decreases.
    - B. In Welch's periodogram with overlap of 50%, the variance of the power spectrum estimate decreases as $1/K$, with $K$ equal to the number of raw periodogram estimates.
    - C. The Blackman-Tukey correlogram is a consistent estimator of the power spectrum.
    - D. In general, zero-padding increases spectral resolution.

!!! sheet "In the cheat sheet: box 3J, plus the Blackman–Tukey line of box 3I"
    <div class="stepper" markdown>

    **A · T.** Shorter segments → coarser resolution → more bias. (Same idea as the Bartlett row: splitting the data buys variance at the price of bias.)

    ***

    **B · F.** The sheet's row: *"Welch/WOSA: variance drops exactly $\frac1K$"* → **F**, because overlapping segments are correlated.

    ***

    **C · T.** Box 3I puts the word "consistent" on the Blackman–Tukey row, and the 3J table says its variance $\to0$.

    ***

    **D · F.** *"Zero-padding improves resolution"* → **F**: it only gives you more dots (step $\frac{2\pi}L$) on the same curve.

    ***

    **Sheet check · "which ones" (plural).**
    Answer key: **A and C**. When the question says "which ones", keep checking after you find one true statement.

    </div>

!!! answer "Answer"
    **A and C**

## 10 · January 2020 · 1b — Welch, four near-identical sentences

!!! exam "Retake, January 2020 · 1b · 0.25 p"
    Select the correct answer regarding the Welch's method for non-parametric spectral estimation, also known as WOSA:

    - A. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, not allowing overlap between the segments. The variance is lower than the periodogram, proportionally to $1/K$.
    - B. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, allowing overlap between the segments. The variance is lower than Bartlett's method, but not proportionally to $1/K$.
    - C. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, not allowing overlap between the segments. The variance is larger than Bartlett's method, but lower than the periodogram.
    - D. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, allowing overlap between the segments. The variance is larger than Bartlett's method, but lower than the periodogram.

!!! sheet "In the cheat sheet: box 3I's two rows"
    <div class="stepper" markdown>

    **Sheet step 1 · Welch = "OVERLAPPING segments, average the periodograms".**
    That kills **A** and **C** immediately (they say "not allowing overlap" — that is Bartlett).

    ***

    **Sheet step 2 · where does its variance sit?**
    Box 3J: *"Welch/WOSA: variance drops exactly $\frac1K$ → F (overlapping segments are correlated)"*. So Welch is **worse than Bartlett** (which does get $\frac1K$) but still **better than a single periodogram** (which is the worst).

    $$\mathrm{Var}_{Bartlett} \;\lt\; \mathrm{Var}_{Welch} \;\lt\; \mathrm{Var}_{periodogram}$$

    ***

    **Sheet step 3 · match.**
    **B** says "lower than Bartlett" (wrong direction). **D** says "larger than Bartlett's method, but lower than the periodogram" ✓.

    </div>

!!! answer "Answer"
    **D**

## 11 · November 2022 · 3b and January 2020 · 1c — the window words

!!! exam "Final exam, November 2022 · 3b · 0.25 p"
    In the context of windowing and zero-padding, which of the following statements is TRUE?

    - a) Given the same window length, a triangular window provides higher spectral resolution compared to a rectangular window.
    - b) When calculating the spectrum of a windowed signal, the main-lobe width of the window function determines spectral resolution, while the height of the side lobes determines spectral leakage.
    - c) When estimating the spectrum using a rectangular window, spectral leakage can be reduced by increasing the window length.
    - d) When calculating the Fourier transform of a N-sample discrete signal, extending the signal to a length L by zero padding is equivalent to sampling the L-sample Fourier Transform for Continuous time signal (FTD) at a step given by theta = k * 2pi / N

!!! exam "Retake, January 2020 · 1c · 0.25 p"
    In the context of windowing, which one of the following statements is true:

    - A. The higher the side lobes of the window function, the worse the resolution of the spectral estimate.
    - B. The higher the side lobes of the window function, the smaller the effects of spectral leakage.
    - C. The wider the main lobe of the window function, the worse the resolution of the spectral estimate.
    - D. The wider the main lobe of the window function, the larger the effects of spectral leakage.

!!! sheet "In the cheat sheet: box 3J's two window rows"
    <div class="stepper" markdown>

    **The two words to keep apart** (box 3J: *"Main-lobe width → resolution; side-lobe height → leakage"* → T):
    **main lobe** = resolution (wide lobe = you cannot separate two close peaks). **side lobes** = leakage (tall lobes = energy spills into other frequencies).

    ***

    **November 2022 · (b) is that row word for word** → **T**.
    (a) is *"Triangular window: better resolution than rectangular"* → F. (c) is *"Longer data or window reduces leakage"* → F. (d) mixes the two: with padding to length $L$ the step is $\frac{2\pi}{L}$, not $\frac{2\pi}{N}$ → F.

    ***

    **January 2020 · (C) is "wider main lobe → worse resolution"** → **T**, the second half of the same row.
    (A) and (B) put the side lobes on resolution/leakage backwards. (D) puts leakage on the main lobe.

    </div>

!!! answer "Answer"
    November 2022 → **(b)** · January 2020 → **(C)**

## 12 · January 2022 · 3a — pick the plot

!!! exam "Resit, January 2022 · 3a · 0.3 p"
    The infinitely-long discrete-time signal $x[n] = 20 \cos(2\pi \frac{f}{f_s} n)$, with $f = 25 \text{ Hz}$ and $f_s = 50 \text{ Hz}$, is windowed with a rectangular window of length $N$ to obtain the window signal $\tilde{x}[n]$. In the plots below, the following Fourier transforms are shown:

    1. The Fourier Transform for Discrete time signals (FTD) of $x[n]$
    2. The FTD of $\tilde{x}[n]$.
    3. The Discrete Fourier Transform (DFT) of $\tilde{x}[n]$ calculated for $N = 24$ and zero padding of $M = 12$ samples.
    4. The Discrete Fourier Transform (DFT) of $\tilde{x}[n]$ calculated for $N = 24$ with no zero padding.

    Which of the following is the correct association?

    - (a) 1B, 2D, 3A, 3C
    - (b) 1B, 2D, 3C, 4A
    - (c) 1C, 2A, 3D, 4B
    - (d) 1D, 2B, 3C, 4A

!!! sheet "In the cheat sheet: box 3F + the window rows of box 3J"
    <div class="stepper" markdown>

    **Sheet step 0 · find the frequency first.**
    $\frac{f}{f_s}=\frac{25}{50}=\frac12$, so $x[n]=20\cos(\pi n)$ — one cosine at $\theta=\pi$. That is why everything sits in one place.

    ***

    **Sheet step 1 · item 1: the FTD of an infinite cosine = two spikes.**
    Two sharp lines at $\pm\pi$. That is plot **B**.

    ***

    **Sheet step 2 · item 2: windowed → a smooth main lobe with side lobes.**
    Cutting the signal to length $N$ smears each spike into a sinc-like lobe. That is plot **D**.

    ***

    **Sheet step 3 · items 3 and 4: DFT = samples of that same smooth curve.**
    Same curve as item 2, just **sampled**. Zero padding to $N+M=36$ → **more dots** on the same curve → plot **C**. No padding → 24 dots → **fewer**, coarser → plot **A**.

    ***

    **Sheet step 4 · match.** 1B, 2D, 3C, 4A → **(b)**.
    *(Option (a) as printed lists "3A, 3C" — two entries for item 3 — which cannot be right either.)*

    ***

    **Sheet check · the box 3J row behind it.**
    *"Zero-padding improves resolution → F (only more points)"*. Dots, not resolution: plots C and A show the same shape at different densities.

    </div>

!!! answer "Answer"
    **(b)** 1B, 2D, 3C, 4A

## 13 · June 2026 · 3e — model order

!!! exam "Resit, June 2026 · 3e · 0.75 p"
    You are given a finite data record of length $N$ and you decide to estimate its power spectral density by fitting an Autoregressive (AR) model of order $p$.

    1. Suppose you evaluate the quality of your fitted model by strictly looking at the variance of the residual error (the difference between the data and the prediction). As you increase the model order $p$, what will happen to this residual error, and what is the primary risk of choosing an excessively high order $p$? [0.25]
    2. Name at least one specific model selection criteria discussed in the course that are designed to prevent the issue identified in question 1. Briefly explain the mathematical mechanism it uses to do so. [0.25]
    3. It is a known property that any arbitrary power spectrum (even one originating from an MA process containing deep spectral nulls) can be approximated using strictly an AR model. What is required to achieve this? [0.25]

!!! sheet "In the cheat sheet: the AR-order paragraph at the bottom of box 3J"
    <div class="stepper" markdown>

    **Sheet step 1 · "Bigger $p$ → residual error always goes down → risk: overfitting (fake peaks)."**
    With more parameters you can always fit the data a little better, including its noise. So the residual variance **decreases monotonically** — which is exactly why you cannot use it to pick $p$.

    ***

    **Sheet step 2 · "Fix: AIC $=N\ln\hat\sigma^2+2p$ (also FPE, MDL)."**
    Mechanism: the first term $N\ln\hat\sigma^2$ falls as $p$ grows (better fit), the penalty $2p$ grows with the number of parameters. Their sum has a minimum — **choose the $p$ with the smallest AIC**. (FPE $=\frac{N+p}{N-p}\hat\sigma^2$ does the same job.)

    ***

    **Sheet step 3 · "Any PSD can be approximated by an AR model of high enough order."**
    Deep spectral nulls are an MA thing, but an AR model of a **high enough order** (in theory AR($\infty$)) reproduces any spectrum to any accuracy.

    </div>

!!! answer "Answer"
    1. The residual error **decreases monotonically**; the risk is **overfitting** (fitting noise, spurious peaks). 2. **AIC** $=N\ln\hat\sigma^2+2p$ (or FPE / AICc / MDL): a fit term plus a complexity penalty $2p$, choose the minimum. 3. A **high enough** AR order.

## Traps

!!! trap "Where points are lost (each one is a line of the sheet you skipped)"
    - Welch overlap: $D=L(1-\text{overlap})$, not $L$. With 50 % overlap the segments are $L=200$ long but only advance 100.
    - $K=\frac{N-L}{D}+1$ — forgetting the $+1$ gives 8 instead of 9.
    - Claiming Welch's variance drops as $\frac1K$. It is **Bartlett** that gets $\frac1K$; overlapping segments are correlated.
    - "A window improves **resolution**" → false, it improves **leakage**. Main lobe = resolution, side lobes = leakage. Keep the two words attached to the right thing.
    - "Longer data reduces leakage" and "zero-padding improves resolution" → both false, and both are in the sheet's 3J table.
    - $\cos(t)u(t)$ is a **power** signal: the step function starts it, it never dies.
    - $A\sin\omega t$ power $=\frac{A^2}{2}$, not $A^2$ (the average of $\sin^2$ is $\frac12$).
    - $\sum_{n\ge0}e^{-2n}=\frac1{1-e^{-2}}=1.1565$ — write the geometric-sum line before the number.
    - "Name the method": **non**-overlapping = Bartlett, overlapping = Welch. That single word is worth the whole row.
    - Multiple-answer tables (April 2024): after you find one, keep reading. "Consistent" and "FT of the autocorrelation" both have two answers.
