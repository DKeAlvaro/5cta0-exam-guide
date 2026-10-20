# 4.3 Bayesian detection & matched filter

<p class="lead">When you know how often each hypothesis happens (priors) and how bad each mistake is (costs), the threshold of the likelihood ratio test is no longer free: it follows from one formula. Recent exams wrap this in a story (a sensor, a genAI detector) and ask "should we decide $\mathcal H_1$?".</p>

## The idea, from zero

- **Priors** $P_0=P(\mathcal H_0)$, $P_1=P(\mathcal H_1)$: how often each situation occurs.
- **Costs** $C_{i,j}$ = cost of **deciding $\mathcal H_i$ when $\mathcal H_j$ is true**. Usually correct decisions cost 0 ($C_{00}=C_{11}=0$). $C_{10}$ is the cost of a false alarm, $C_{01}$ the cost of a miss.
- **Bayes risk** = expected cost. Minimising it gives a likelihood ratio test with threshold

$$\boxed{\frac{p(\mathbf x\mid\mathcal H_1)}{p(\mathbf x\mid\mathcal H_0)}\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda=\frac{(C_{10}-C_{00})\,P_0}{(C_{01}-C_{11})\,P_1}}$$

How the threshold moves (and how the MC questions are built):

| Change | Effect on $\lambda$ | Meaning |
|---|---|---|
| $P_0$ larger ($\mathcal H_1$ rarer) | **up** | need stronger evidence to say $\mathcal H_1$ |
| $P_1$ larger | **down** | easier to say $\mathcal H_1$ |
| false alarms more costly ($C_{10}$ up) | up | say $\mathcal H_1$ less often |
| misses more costly ($C_{01}$ up) | down | say $\mathcal H_1$ more often |
| all costs × the same factor | unchanged | |

Special cases:

- **0/1 costs** ($C_{01}=C_{10}=1$, $C_{00}=C_{11}=0$): the risk is $P_0P_{FA}+P_1P_M$, the **total probability of error**. Threshold $\lambda=P_0/P_1$. Equivalent to "pick the hypothesis with the larger posterior" (MAP rule): decide $\mathcal H_1$ if $P_1\,p(\mathbf x\mid\mathcal H_1)>P_0\,p(\mathbf x\mid\mathcal H_0)$.
- **Equal priors + 0/1 costs**: $\lambda=1$, the **maximum likelihood** rule.

**With posteriors instead of likelihoods.** Since $p(\mathbf x\mid\mathcal H_i)P_i\propto P(\mathcal H_i\mid\mathbf x)$, the same rule reads

$$\text{decide }\mathcal H_1\iff(C_{01}-C_{11})\,P(\mathcal H_1\mid\mathbf x)>(C_{10}-C_{00})\,P(\mathcal H_0\mid\mathbf x).$$

## The matched filter

Detecting a **known** signal $s_n$ in white Gaussian noise ($\mathcal H_0$: $x_n=w_n$, $\mathcal H_1$: $x_n=s_n+w_n$). The LRT reduces to a **correlator**:

$$\sum_{n=0}^{N-1}x_n\,s_n\ \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\ \lambda'=\sigma^2\ln\lambda+\frac12\sum_ns_n^2 .$$

- As an FIR filter: impulse response = the **time-reversed** signal, $h[n]=s[N-1-n]$, output sampled at $n=N-1$.
- Among all linear filters it **maximises the output SNR** (Cauchy–Schwarz).
- With **correlated** noise, whiten the data first (generalised matched filter). It is not limited to uncorrelated noise.

---

## Exam questions

### June 2026 resit · 4c {#jun26-4c}

!!! exam "Resit Q4, June 2026 · 4c · 1 p"
    *(Same Rayleigh sensor as [4b](p4-lrt.md#jun26-4b).)* Now assume prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$, reflecting the fact that a transmitting device is present only 10% of the time. Assume equal costs for false alarms and miss-detections. When should the sensor accept $H_1$?

???+ solution "Solution"
    Equal costs (0 for correct, the same cost for both errors) → $\eta=\frac{P_0}{P_1}=\frac{0.9}{0.1}=9$. Plug into the test from 4b:

    $$\frac{\sigma_0^2}{\sigma_1^2}\exp\!\left[\frac{x^2}{2}\cdot\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}\right]>9\quad\Longleftrightarrow\quad x>\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\,\ln\!\left(\frac{9\,\sigma_1^2}{\sigma_0^2}\right)}.$$

    Because the device is rare, the threshold is higher than with equal priors ($\ln(9\sigma_1^2/\sigma_0^2)$ instead of $\ln(\sigma_1^2/\sigma_0^2)$): the sensor needs a clearly stronger envelope before it declares a device.

    !!! answer "Answer"
        Accept $H_1$ when $x>\sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\!\dfrac{9\sigma_1^2}{\sigma_0^2}}$ (LRT threshold $\eta=9$)

### June 2026 resit · 4a {#jun26-4a}

!!! exam "Resit Q4, June 2026 · 4a · 0.5 p"
    Which of the following statements about prior probabilities in Bayesian hypothesis testing is FALSE?

    - a When prior probabilities are equal, $P(H_0) = P(H_1)$, and equal costs are assigned, the Bayesian decision rule reduces to the maximum likelihood decision rule.
    - b A higher prior probability $P(H_0)$ raises the Bayesian threshold $\eta$, requiring stronger evidence before $H_1$ is selected.
    - c Increasing the prior probability $P(H_1)$ raises the Bayesian decision threshold $\eta$, making it harder to decide in favour of $H_1$.

???+ solution "Solution"
    $\eta\propto P_0/P_1$. More $P_1$ → **lower** threshold → easier to pick $H_1$. (a) and (b) are true.

    !!! answer "Answer"
        **(c)**

### April 2025 exam · 4c {#apr25-4c}

!!! exam "Final exam Q3, 13 April 2025 · 4c · 1 p"
    The teaching team in a MSc course uses an AI agent to detect whether assignments have been generated using genAI which is considered fraudulent. There are two hypotheses to choose from $\mathcal{H}_0$: the assignment has been generated by a student; $\mathcal{H}_1$: the assignment has been generated by genAI. The system uses Bayesian hypothesis testing and the student fails the course if the agent accepts $\mathcal{H}_1$. Assume that $C_{0,1} = 100C_{1,0}$, $C_{1,1} = C_{0,0} = 0$. In addition, assume that the posterior of $\mathcal{H}_0$ is 5 times smaller than the posterior of $\mathcal{H}_1$. Should the student fail the course?

???+ solution "Solution"
    **Decode the costs.** $C_{0,1}$ = decide $\mathcal H_0$ (student) when $\mathcal H_1$ (AI) is true = **missing** an AI assignment. It is 100 times worse than $C_{1,0}$, failing an honest student.

    **Posterior form of the rule:** decide $\mathcal H_1$ iff $C_{01}P(\mathcal H_1\mid x)>C_{10}P(\mathcal H_0\mid x)$, i.e.

    $$\frac{P(\mathcal H_1\mid x)}{P(\mathcal H_0\mid x)}>\frac{C_{10}}{C_{01}}=\frac{1}{100}=0.01.$$

    The posterior ratio is $5$ (the posterior of $\mathcal H_0$ is 5 times smaller). $5>0.01$ → accept $\mathcal H_1$. With these costs the system would flag the assignment even if AI were 100 times *less* likely than a human author. (Even with equal costs, 5 > 1 would still mean fail.)

    !!! answer "Answer"
        **Yes**, the student fails: $5\ge\lambda=0.01$.

### November 2022 exam · 4f, 4g {#nov22-4f}

!!! exam "Final exam Q1, 7 November 2022 · 4f, 4g · 0.5 p each"
    *(Same $y=|x|$ problem as [4c–4e](p4-lrt.md#nov22-4c): $p(y;\mathcal H_0)=e^{-y}$, $p(y;\mathcal H_1)=2e^{-2y}$.)*

    Consider the prior probabilities $P_0 = 0.4$ and $P_1 = 0.6$ for the hypotheses $\mathcal{H}_0$ and $\mathcal{H}_1$, respectively. The Bayesian hypothesis test for the cost $C_{1,1} = C_{0,0} = 0$ and $C_{0,1} = C_{1,0} = 1$ is

    $$L(\mathbf{x}) = \frac{p(\mathbf{x}|\mathcal{H}_1)}{p(\mathbf{x}|\mathcal{H}_0)} \underset{\mathcal{H}_0}{\overset{\mathcal{H}_1}{\gtrless}} \frac{P_0}{P_1},$$

    or, equivalently, $p(\mathbf{x}|\mathcal{H}_1)P_1 \underset{\mathcal{H}_0}{\overset{\mathcal{H}_1}{\gtrless}} p(\mathbf{x}|\mathcal{H}_0)P_0,$ that is, we decide for $\mathcal{H}_1$ if the probability of observing $y$ under $\mathcal{H}_1$ is greater than under $\mathcal{H}_0$. At the threshold, the observation $y$ admits the same probabilities under both hypotheses. A sketch of the two distributions is provided below.

    ![weighted pdfs](img/exam/nov22-4f.jpg)

    **4f** Find the threshold $\gamma''$, i.e., the value of $y$ for which $p(\mathbf{x}|\mathcal{H}_1)P_1 = p(\mathbf{x}|\mathcal{H}_0)P_0$.

    **4g** Determine the probability of miss $P_M$ and the probability of false alarm $P_{FA}$ for the Bayesian hypothesis test.

???+ solution "Solution"
    **Reading the plot:** each PDF is multiplied by its prior. Solid $0.4e^{-y}$ starts at 0.4; dashed $0.6\cdot2e^{-2y}=1.2e^{-2y}$ starts at 1.2. Where dashed is on top, decide $\mathcal H_1$.

    **4f.** Set them equal:

    $$0.4e^{-y}=1.2e^{-2y}\iff e^{y}=3\iff\gamma''=\ln3\approx1.10.$$

    Decide $\mathcal H_1$ for $y<\ln3$.

    **4g.** Conditional probabilities (the official clarification says so):

    $$P_{FA}=\int_0^{\ln3}e^{-y}dy=1-\tfrac13=\tfrac23,\qquad P_M=\int_{\ln3}^\infty2e^{-2y}dy=e^{-2\ln3}=\tfrac19.$$

    ![Bayesian threshold](img/gen/p4_nov22_bayes.svg)

    Weighted by the priors these are $0.4\cdot\frac23=\frac4{15}$ and $0.6\cdot\frac19=\frac1{15}$, total error $\frac13$, the minimum possible (the review deck shows only these weighted values; the key gives the conditional ones).

    !!! answer "Answer"
        4f: $\gamma''=\ln3\approx1.10$. 4g: $P_{FA}=\frac23$, $P_M=\frac19$ (prior-weighted: $\frac4{15}$ and $\frac1{15}$, $P_e=\frac13$).

### January 2022 resit · 4a {#jan22-4a}

!!! exam "Resit, 24 January 2022 · 4a · 0.3 p"
    Which of the following statements about the matched filter is true?

    - (a) The signal-to-noise ratio at the output of the matched filter is maximized.
    - (b) The matched filter can be implemented as a FIR filter with impulse response $h[n] = s[n]$.
    - (c) The matched filter can only be applied for uncorrelated noise samples.

???+ solution "Solution"
    (b) needs the **time-reversed** signal, $h[n]=s[N-1-n]$. (c) with correlated noise you prewhiten first.

    !!! answer "Answer"
        **(a)**
