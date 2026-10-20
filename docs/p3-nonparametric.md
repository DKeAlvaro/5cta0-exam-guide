# 3.2 Non-parametric estimators: periodogram, correlogram, Bartlett, Welch, Blackman–Tukey

<p class="lead">Every exam has at least one theory question here, usually a multiple choice or a "match the statement to the method" table. It is pure memorisation of one table: <b>what each method does to bias and to variance</b>.</p>

## The idea, from zero

For a random signal the PSD $P(e^{j\theta})$ is defined through the autocorrelation (Wiener–Khinchin): $P(e^{j\theta})=\sum_l r[l]e^{-jl\theta}$. With only $N$ samples you have to *estimate* it. Two "raw" ways:

- **Periodogram** (direct): $\hat P(e^{j\theta})=\frac1N\Big|\sum_{n=0}^{N-1}x[n]e^{-jn\theta}\Big|^2$, the squared magnitude of the DFT divided by $N$.
- **Correlogram** (indirect): first estimate $\hat r[l]$ from the data, then take its Fourier transform, $\hat P(e^{j\theta})=\sum_{l=-(N-1)}^{N-1}\hat r[l]e^{-jl\theta}$.

With the usual (biased, $\frac1N$) autocorrelation estimate the two are **the same estimator**.

**How good are they?**

- **Bias.** $E[\hat P]=P*W_B$: the true PSD smeared by a triangular (Bartlett) window spectrum. So: loss of resolution + leakage, which vanish as $N\to\infty$. The raw estimators are **asymptotically unbiased**.
- **Variance.** $\operatorname{Var}[\hat P]\approx P^2(e^{j\theta})$: proportional to the **square of the true spectrum** and it does **not** shrink with $N$. So the raw estimators are **not consistent**. The estimate stays noisy however long the record.

## The three improvements

| Method | What it does | Bias | Variance |
|---|---|---|---|
| **Periodogram / correlogram** (raw) | $\frac1N\lvert\text{DFT}\rvert^2$ / FT of $\hat r[l]$ | asymptotically unbiased; resolution ≈ $2\pi/N$ | $\approx P^2$, not consistent |
| **Bartlett** (averaged periodogram) | split into $K$ **non-overlapping** segments of length $M=N/K$, average the $K$ periodograms | **increases** (segments are shorter: resolution ≈ $2\pi/M$) | $\approx P^2/K$ (segments independent) |
| **Welch / WOSA** | **overlapping** (50–75 %), **windowed** segments, average | increases **less** than Bartlett (longer segments) | decreases, but **not** as $1/K$ (overlapping segments are correlated) |
| **Blackman–Tukey** | multiply $\hat r[l]$ by a lag window of length $2M-1\ll N$, then FT | increases as $M$ gets smaller | $\approx\frac{P^2}{N}\sum w^2$ → 0: **consistent** |
| **Parametric (AR/MA/ARMA)** | fit a signal model, use its formula | small if the model fits | low; see [3.4](p3-chain.md) |

Number of Welch segments for record length $N$, segment length $L$ and hop $D$ (= $L$ × (1 − overlap)):

$$K=\frac{N-L}{D}+1.$$

!!! idea "The trade-off in one line"
    Averaging **more, shorter** pieces lowers the variance but raises the bias (worse resolution). Bartlett, Welch and Blackman–Tukey are three ways of making that trade.

<figure markdown>
![Welch segments for N=1000, L=200, 50% overlap](img/gen/p3_welch.svg)
<figcaption>June 2026 3b: segments of 200 samples that start every 100 samples. The last one starts at 800 and ends at 999, so there are 9.</figcaption>
</figure>

---

## Exam questions

### June 2026 resit · 3a {#jun26-3a}

!!! exam "Resit Q4, June 2026 · 3a · 0.25 p"
    Which of the following statements regarding the standard periodogram as an estimator of the Power Spectral Density (PSD) is TRUE?

    - a) Increasing the length of the data window on which the periodogram is calculated decreases spectral leakage
    - b) The periodogram is not a consistent estimator because its variance does not tend to zero as the data record length $N \rightarrow \infty$.
    - c) Applying a data window (e.g., a Hamming window) improves the frequency resolution (main lobe width) of the periodogram.
    - d) Bartlett's method decreases the variance of the periodogram by zero-padding the original sequence.

???+ solution "Solution"
    - (a) Longer data improves **resolution**; the side-lobe level (leakage) of the rectangular window does not change. Treated as false in Nov 2022 3b as well.
    - (b) $\operatorname{Var}\approx P^2$ regardless of $N$. ✓
    - (c) Hamming **widens** the main lobe (worse resolution) and lowers the side lobes (less leakage).
    - (d) Bartlett **averages segments**; zero padding has nothing to do with it.

    !!! answer "Answer"
        **(b)**

### June 2026 resit · 3b {#jun26-3b}

!!! exam "Resit Q4, June 2026 · 3b · 0.5 p"
    You are given a data record of $N = 1000$ samples. You want to estimate the power spectral density using Welch's method to reduce the variance of your estimate. You choose a segment length of $L = 200$ samples and an overlap of 50%.

    **Please provide only the final answer. The workout will not be checked.**

    1. How many segments $K$ will be averaged? [0.25]
    2. With the simplifying assumption that the segments are statistically independent, what is the ratio of the variance of your Welch estimate to the variance of a single standard periodogram of length $L$? [0.25]

???+ solution "Solution"
    1. 50 % overlap → each segment starts $D=100$ samples after the previous one: $K=\frac{1000-200}{100}+1=9$ (see the figure above).
    2. Averaging $K$ independent estimates divides the variance by $K$: ratio $=1/9$.

    !!! answer "Answer"
        1. $K=9$  2. $\operatorname{Var}_{Welch}/\operatorname{Var}_{single}=1/9\approx0.11$

!!! trap "Not 5 segments"
    $N/L=5$ is the Bartlett count (no overlap). With 50 % overlap you get $2\cdot5-1=9$.

### April 2025 exam · 3b {#apr25-3b}

!!! exam "Final exam Q3, 13 April 2025 · 3b · 0.25 p"
    Which of the following statements on spectral estimation is TRUE?

    - a) The problem of bias in the spectral estimate affects both deterministic and stochastic signals.
    - b) Zero-padding prior to applying the discrete Fourier transform can improve the spectral resolution of the spectral estimate, i.e. the ability to distinguish spectral peaks.
    - c) The "raw" periodogram achieves better performance in terms of bias, but worse in terms of variance compared to the "raw" correlogram.
    - d) The type of window used to window the signal affects both the bias and the variance of the spectral estimate obtained using the "raw" periodogram.

???+ solution "Solution"
    - (a) Bias comes from **windowing** (finite $N$), which happens to every signal, deterministic or random. Random signals add the **variance** problem on top. ✓
    - (b) Zero padding only interpolates ([3.1](p3-windows.md#dft-ftd-and-zero-padding)).
    - (c) Raw periodogram and raw correlogram are equivalent: same bias, same variance.
    - (d) The window shape changes resolution and leakage (bias). The variance of the raw periodogram stays $\approx P^2$.

    !!! answer "Answer"
        **(a)**

### April 2025 exam · 3c {#apr25-3c}

!!! exam "Final exam Q3, 13 April 2025 · 3c · 0.5 p"
    In the table below, fill in to which power spectral density (PSD) estimator each statement is referring. **Note: only one answer is correct for each statement.**

    | Statement | PSD-estimator |
    |---|---|
    | 1. PSD is estimated by dividing the total signal length in different non-overlapping segments, and averaging the periodograms obtained on each segement. | |
    | 2. PSD is estimated by calculating the modulus squared of the N-point DFT of the random signal, and dividing by the signal length N. | |
    | 3. PSD is estimated by using a model of the form $P(e^{j\theta}) = \sigma_i^2 \left\lvert \frac{1 + \sum_q b_q e^{-jq\theta}}{1 + \sum_p a_p e^{-jp\theta}} \right\rvert^2$ | |
    | 4. PSD is estimated by calculating the L-point DFT of the estimated autocorrelation function of the signal (L=number of lags), after applying a window of length M<L to the autocorrelation function. | |
    | 5. PSD is estimated by dividing the total signal length in different overlapping segments, and averaging the periodograms obtained on each segment. | |

???+ solution "Solution"
    Key words: *non-overlapping* → Bartlett; *modulus squared of the DFT* → periodogram; *a rational model* → ARMA (parametric); *window on the autocorrelation* → Blackman–Tukey; *overlapping* → Welch.

    !!! answer "Answer"
        1 Bartlett · 2 Periodogram · 3 ARMA (parametric) model · 4 Blackman–Tukey · 5 Welch (WOSA)

### April 2024 exam · 3a {#apr24-3a}

!!! exam "Final exam Q3, April 2024 · 3a · 0.9 p"
    Indicate which spectral estimation method(s) fit each of the following description. Multiple answer are possible, and answer can be repeated. If multiple answers are possible, please indicate them all.

    | | Description | Method(s) |
    |---|---|---|
    | 1 | Estimates the power spectral density by modeling the random signal as a linear random signal model. | |
    | 2 | Divides the signal into segments, allowing overlap between the segments. | |
    | 3 | Is a consistent estimator of the power spectral density. | |
    | 4 | Estimates the power spectrum as the Fourier transform of the autocorrelation function. | |
    | 5 | The bias of the power spectral density estimate is proportional to the square of the true spectrum. | |
    | 6 | Averages multiple periodogram estimates. | |

???+ solution "Solution"
    No official key is available for this paper. Reasoning per row:

    1. "Linear random signal model" = AR, MA, ARMA (parametric methods).
    2. Overlap → **Welch (WOSA)** only. Bartlett's segments do not overlap.
    3. The reader calls **Blackman–Tukey** consistent (its variance ∝ $1/N$). Bartlett and Welch also have variance → 0 if the number of segments grows with $N$, so listing them is defensible. The raw periodogram/correlogram are **not** consistent.
    4. FT of the (estimated) autocorrelation → **correlogram** and **Blackman–Tukey** (a windowed correlogram).
    5. Careful: what is proportional to $P^2$ is the **variance** of the raw periodogram/correlogram, not the bias. As printed, no method fits. If it was meant as variance: periodogram and correlogram.
    6. **Bartlett** and **Welch**.

    !!! answer "Answer"
        1 AR/MA/ARMA · 2 Welch · 3 Blackman–Tukey (+ Bartlett, Welch with $K\to\infty$) · 4 correlogram, Blackman–Tukey · 5 none as written (variance ∝ $P^2$ for periodogram/correlogram) · 6 Bartlett, Welch

### November 2022 exam · 3a {#nov22-3a}

!!! exam "Final exam Q1, 7 November 2022 · 3a · 0.25 p"
    In the context of non-parametric spectral estimation, which of the following statements is TRUE?

    - a) Compared to the periodogram, the Bartlett method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. However, the bias increases.
    - b) Compared to the periodogram, the WOSA method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. However, the bias increases.
    - c) Compared to the periodogram, the Bartlett method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. The bias also decreases, but not proportionally to 1/K.
    - d) Compared to the periodogram, the WOSA method with K segments allows a reduction of the variance of the estimated spectrum proportional to 1/K. The bias also decreases, but not proportionally to 1/K.

???+ solution "Solution"
    "Proportional to $1/K$" is only true for **Bartlett** (independent segments), which rules out (b) and (d). Shorter segments → bias **increases**, which rules out (c).

    !!! answer "Answer"
        **(a)**

### January 2020 retake · 1b {#jan20-1b}

!!! exam "Retake exam, 20 January 2020 · Exercise 1(b) · 0.25 p"
    Select the correct answer regarding the Welch's method for non-parametric spectral estimation, also known as WOSA:

    - A. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, not allowing overlap between the segments. The variance is lower than the periodogram, proportionally to $1/K$.
    - B. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, allowing overlap between the segments. The variance is lower than Bartlett's method, but not proportionally to $1/K$.
    - C. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, not allowing overlap between the segments. The variance is larger than Bartlett's method, but lower than the periodogram.
    - D. It consists of averaging $K$ different periodograms, obtained from $K$ segments of the observed random signal, allowing overlap between the segments. The variance is larger than Bartlett's method, but lower than the periodogram.

???+ solution "Solution"
    Welch **allows overlap** (rules out A and C). With the same $K$, overlapping segments are correlated, so the variance drops less than Bartlett's $1/K$: larger than Bartlett, still lower than the raw periodogram (reader §12.2.2).

    !!! answer "Answer"
        **D**

### November 2019 exam · 1c {#nov19-1c}

!!! exam "Written exam, 4 November 2019 · Exercise 1(c) · 1.5 p"
    Complete Table 2, which provides an overview of non-parametric spectral estimation methods. Answers can be descriptive. In other words, formulas are not necessary. Please use the template table in the answer sheet and limit your answers to the assigned space in each entry of the table.

    | | Description (basic idea) | Bias | Variance |
    |---|---|---|---|
    | Periodogram | | | |
    | Correlogram | | | |
    | Bartlett's periodogram | | | |
    | WOSA | | | |
    | Blackman-Tukey | | | |

???+ solution "Solution"
    The official key only filled the periodogram row. Full table:

    | | Description | Bias | Variance |
    |---|---|---|---|
    | Periodogram | $\frac1N\lvert\text{FT of the data}\rvert^2$ | FT of the biased $\hat r$: smoothed by a triangular window; asymptotically unbiased | ∝ $P^2$; does not decrease with $N$ (not consistent) |
    | Correlogram | FT of the estimated autocorrelation (lags up to $N-1$) | same as periodogram (equivalent with biased $\hat r$; the unbiased $\hat r$ can give negative PSD) | ∝ $P^2$, not consistent |
    | Bartlett | average $K$ periodograms of non-overlapping segments of length $M=N/K$ | larger (resolution $\approx2\pi/M$) | ≈ $P^2/K$ |
    | WOSA (Welch) | average periodograms of overlapping, windowed segments | larger than raw, but less than Bartlett (longer segments) | reduced, but not as $1/K$ (correlated segments) |
    | Blackman–Tukey | window $\hat r[l]$ with a short lag window ($M\ll N$), then FT | larger for shorter $M$ (convolution with the window spectrum) | ≈ $\frac{P^2}{N}\sum w^2[l]$ → 0: consistent |

### January 2019 retake · 1c {#jan19-1c}

!!! exam "Written exam, 21 January 2019 · Exercise 1(c) · 0.5 p (1 or 2 answers correct)"
    In the context of non-parametric spectral estimation methods, which ones of the following statements are true?

    - A. In Bartlett's method, the bias of the estimated power spectrum increases as the length of the window $M$ of each raw periodogram decreases.
    - B. In Welch's periodogram with overlap of 50%, the variance of the power spectrum estimate decreases as $1/K$, with $K$ equal to the number of raw periodogram estimates.
    - C. The Blackman-Tukey correlogram is a consistent estimator of the power spectrum.
    - D. In general, zero-padding increases spectral resolution.

???+ solution "Solution"
    A ✓ (shorter segments → wider main lobe). B ✗ (overlap → correlated → not $1/K$). C ✓. D ✗.

    !!! answer "Answer"
        **A and C**
