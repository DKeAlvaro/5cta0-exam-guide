# 1.3 Random processes: stationarity, ergodicity, autocorrelation

<p class="lead">One multiple-choice question per exam, usually 0.25–0.3 p. They test two words: <b>stationary</b> (WSS) and <b>ergodic</b>. Once you can picture a process as a stack of signals, both are easy.</p>

## The idea, from zero

A **random process** $X(t)$ (or $X[n]$ in discrete time) is a **collection of signals**. Each time you run the experiment you get one whole signal, called a **realisation**. The collection of all possible realisations is the **ensemble**.

Two ways to average:

- **Ensemble average** (vertical): fix a time $t$, average over *all realisations*. This is $E[X(t)]$.
- **Time average** (horizontal): take *one* realisation and average it over time, $\frac1N\sum_n x[n]$.

<figure markdown>
![Four example processes](img/gen/p1_processes.svg)
<figcaption>Top left: $\cos(t+U)$. Every realisation wiggles around 0, so the time average of any one of them equals the ensemble mean 0. Top right: $A\cos t$. The ensemble mean is $\cos t$, which changes with time. Bottom left: dice. Every row is i.i.d. rolls, so time averages are the same for every row. Bottom right: the Nov 2022 process. $A$ is drawn once per realisation, so the spread differs from row to row.</figcaption>
</figure>

**Wide-sense stationary (WSS)**: the statistics up to second order do not depend on *when* you look.

1. The mean is constant: $E[X(t)]=\mu$ for all $t$.
2. The autocorrelation $r(t_1,t_2)=E[X(t_1)X(t_2)]$ depends only on the lag $\tau=t_2-t_1$.

**Ergodic**: you can learn the ensemble statistics from **one** (infinitely long) realisation, because time averages equal ensemble averages. The course requires a process to be stationary before it can be ergodic.

- **Ergodic in the mean**: $\frac1N\sum x[n]\to E[X]$ for every realisation.
- **Ergodic in the variance / autocorrelation**: the same for $x^2$ or $x[n]x[n+l]$.

!!! recipe "Recipe: is it WSS? is it ergodic?"
    1. Compute $E[X(t)]$. If it depends on $t$ → **not WSS** → not ergodic. Stop.
    2. Compute $E[X(t_1)X(t_2)]$. Use $\cos\alpha\cos\beta=\tfrac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$ when there are cosines. If only $t_1-t_2$ survives → WSS.
    3. For ergodicity, look for a random quantity that is **drawn once per realisation and then frozen** (an amplitude $A$, the size of the range). Any statistic that depends on it differs from realisation to realisation → not ergodic in that statistic. A random **phase** $U$ that is uniform over $[0,2\pi)$ does not hurt the mean: every realisation still averages to 0.
    4. If everything is drawn fresh at every time step (i.i.d. samples: dice, white noise), the process is ergodic in everything.

### Autocorrelation: what a valid one looks like

For a real WSS signal, $r[l]=E\{x[n]\,x[n-l]\}$ must satisfy:

1. **Symmetric**: $r[-l]=r[l]$.
2. **Peak at zero lag**: $r[0]\ge|r[l]|$ ($r[0]=E[x^2]$ is the power).
3. **Non-negative spectrum**: the PSD $P(e^{j\theta})=\sum_l r[l]e^{-jl\theta}$ (Wiener–Khinchin) must be $\ge0$ for every $\theta$.

White noise has $r[l]=\sigma^2\delta[l]$ (correlated only with itself) and a flat PSD $P=\sigma^2$.

The **cross-correlation** between two signals is $r_{xy}[l]=E\{x[n]\,y[n-l]\}$. For ergodic signals you estimate it from data as $\hat r_{xy}[l]=\frac1N\sum_n x[n]\,y[n-l]$ (reader, Table 3.2).

---

## Exam questions

### June 2026 resit · 1d {#jun26-1d}

!!! exam "Resit Q4, June 2026 · 1d · 0.25 p"
    Which of the following conditions is required for a random process to be considered Wide-Sense Stationary (WSS)?

    - (a) Time averages of all its individual realizations are strictly equal to its ensemble averages.
    - (b) Its mean is constant and its autocorrelation function depends only on the time difference (lag).
    - (c) Its probability density function remains strictly constant over all time indices.
    - (d) Its power spectral density is a constant value across all frequencies.

???+ solution "Solution"
    (a) is the definition of **ergodic**. (c) is (first-order) **strict-sense** stationarity, more than WSS asks for. (d) describes **white** noise.

    !!! answer "Answer"
        **(b)**

### April 2025 exam · 1d {#apr25-1d}

!!! exam "Final exam Q3, 13 April 2025 · 1d · 0.25 p"
    *(The question text was missing from the printed exam. The official clarification gives it:)* Suppose we have infinitely many fair dice and we define a random process $X[n]$ as the ensemble of the random signals $x_i[n]$ obtained by rolling each die infinitely many times and recording the number on the upward face of the die. Which of the following statements is true?

    - (a) The process is ergodic, but only in the mean.
    - (b) The process is ergodic in both mean and variance.
    - (c) $E[X[n]] = E[x_i[n]] = 0, \forall i$
    - (d) The process is stationary but not ergodic.

???+ solution "Solution"
    Every die is fair and every roll is independent, so every realisation is an i.i.d. sequence with the **same** distribution. The time average of any single realisation converges to the ensemble mean $3.5$, and its time-averaged spread converges to the ensemble variance $35/12$. (c) is wrong because the mean is 3.5, not 0.

    !!! answer "Answer"
        **(b)** ergodic in both mean and variance

### January 2022 resit · 1c {#jan22-1c}

!!! exam "Resit, 24 January 2022 · 1c · 0.3 p"
    Suppose we have infinitely many fair dice and we define a random process as the ensemble of the random signals obtained by rolling each die infinitely many times and recording the number on the upward face. Which of the following statements is true?

    - a) This random process is not ergodic, but it is stationary.
    - b) This random process is ergodic in the mean and variance.
    - c) This random process is ergodic in the mean, but not in the variance.
    - d) None of the above.

???+ solution "Solution"
    Same question as April 2025, same reasoning: i.i.d. rolls from identical dice, so one realisation tells you everything.

    !!! answer "Answer"
        **(b)**

### April 2024 exam · 1d {#apr24-1d}

!!! exam "Final exam Q3, April 2024 · 1d · 0.3 p"
    For the following random processes, indicate if they are WSS and ergodic in the mean:

    1. $X(t) = \cos(t + U)$, where $U \sim Uniform(0, 2\pi)$
    2. $X(t) = A \cos(t)$, where $A \sim N(1, 2)$

    The following formula might be useful:

    $$\cos(\alpha) \cos(\beta) = \frac{\cos(\alpha + \beta) + \cos(\alpha - \beta)}{2}$$

    | Random process | WSS (Yes/No) | Ergodic in the mean (Yes/No) |
    |---|---|---|
    | 1 | | |
    | 2 | | |

???+ solution "Solution"
    **Process 1, random phase.** Mean: averaging $\cos(t+U)$ over a uniform phase covers a full period, so $E[X(t)]=\frac1{2\pi}\int_0^{2\pi}\cos(t+u)\,du=0$ for every $t$. Constant.

    Autocorrelation, with the hint:

    $$E[\cos(t_1+U)\cos(t_2+U)]=\tfrac12E[\cos(t_1+t_2+2U)]+\tfrac12\cos(t_1-t_2)=\tfrac12\cos(t_1-t_2).$$

    The first term averages to 0 (again a full period). Only the lag $t_1-t_2$ survives → **WSS**. Every realisation is a cosine that averages to 0 over time, equal to the ensemble mean → **ergodic in the mean**.

    **Process 2, random amplitude.** $E[X(t)]=E[A]\cos t=\cos t$: depends on $t$ → **not WSS** → not ergodic. Look at the figure at the top: one realisation $a\cos t$ averages to 0 over time, while the ensemble mean is $\cos t$.

    !!! answer "Answer"
        | | WSS | Ergodic in the mean |
        |---|---|---|
        | 1 | Yes | Yes |
        | 2 | No | No |

### November 2022 exam · 1c {#nov22-1c}

!!! exam "Final exam Q1, 7 November 2022 · 1c · 0.25 p"
    A random process $X(t)$ is represented by a random number generator. For each realization of the random process, the random number generator samples randomly (with equal probability) infinitely many numbers between $-A$ and $A$. Random variable $A$ follows a normal distribution with mean $\mu_A = 1$ and $\sigma_A = 2$. Which of the following statements is TRUE?

    - a) The random process is NOT ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 1$
    - b) The random process is ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 1$
    - c) The random process is NOT ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 0$
    - d) The random process is ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 0$

???+ solution "Solution"
    **Mean.** Given $A=a$, each sample is uniform on $[-a,a]$, which has mean 0. So $E[X]=0$: this kills options (a) and (b).

    **Ergodic in the mean?** One realisation has a fixed $a$ and i.i.d. samples with mean 0, so its time average → 0 = ensemble mean. **Yes.**

    **Ergodic in the variance?** One realisation has time-averaged power $a^2/3$, which depends on the $a$ drawn for that realisation. The ensemble power is $E[A^2]/3=(1+4)/3=5/3$. **No.** (The process is still WSS: $E[X[n]X[n+k]]=\tfrac53\delta[k]$.)

    So it comes down to what "ergodic" means here. The **official 2026 key** says: *"ergodic" is meant as ergodic in the mean* → (d). The 2026-27 review slides marked (c) instead ("not ergodic"). If this exact question shows up again, (d) follows the latest key. If they say "ergodic in the variance/autocorrelation", the answer is "not ergodic".

    !!! answer "Answer"
        **(d)** per the official key (ergodic in the mean, mean = 0)

### January 2020 retake · 1a {#jan20-1a}

!!! exam "Retake exam, 20 January 2020 · Exercise 1(a) · 0.25 p"
    Looking at Figure 1, which sequences are legitimate auto-correlation functions

    ![Figure 1: r_A, r_B, r_C, r_D](img/exam/jan20-1a-autocorr.jpg)

    - A. Only $r_B[l]$.
    - B. Only $r_D[l]$.
    - C. $r_A[l]$ and $r_B[l]$.
    - D. $r_B[l]$ and $r_D[l]$.
    - E. $r_C[l]$ and $r_D[l]$.
    - F. All.

???+ solution "Solution"
    **Reading the plots:** each stem is one lag $l$, its height is $r[l]$. Check the rules one by one:

    - $r_A$: $r_A[0]=1$ but $r_A[\pm1]=-1.5$, so $|r[1]|>r[0]$ ✗.
    - $r_C$: not symmetric ($r_C[-3]=0.8$, $r_C[3]=0.5$; $r_C[-2]=1$, $r_C[2]=1.5$) ✗.
    - $r_D$: negative on the left, positive on the right: not symmetric ✗.
    - $r_B$: symmetric, peak $r_B[0]=2$ at zero lag ✓.

    Expected answer: only $r_B$.

    !!! trap "Strictly speaking"
        The third rule (PSD ≥ 0) fails for $r_B$ too: $P(e^{j\theta})=2-3\cos\theta+\cos2\theta=(2\cos\theta-1)(\cos\theta-1)$ is negative for $|\theta|<\pi/3$. The question only meant the two quick checks, so answer A, but know that symmetry and a peak at 0 are necessary, not sufficient.

        ![PSD of r_B](img/gen/p1_rB_psd.svg)

    !!! answer "Answer"
        **A** (only $r_B$), per the key

### November 2019 exam · 1a {#nov19-1a}

!!! exam "Written exam, 4 November 2019 · Exercise 1(a) · 1 p"
    Let $x[n]$ and $y[n]$ be two random signals. Suppose we observe $x[n]$ and $y[n]$ in a limited time window as shown in Fig. 1 below. Assuming $x[n]$ and $y[n]$ to be ergodic, what is the cross-correlation $r_{xy}[\tau]$?

    ![Figure 1: x[n] and y[n]](img/exam/nov19-1a-xy.jpg)

    - A. $r_{xy}[0] = 5/4$, $r_{xy}[1] = -8/4$, $r_{xy}[2] = 11/4$, $r_{xy}[3] = -7/4$, $r_{xy}[4] = 1$, $r_{xy}[5] = 1/4$ and zero elsewhere
    - B. $r_{xy}[0] = 5/4$, $r_{xy}[1] = 8/4$, $r_{xy}[2] = 11/4$, $r_{xy}[3] = 7/4$, $r_{xy}[4] = 1$, $r_{xy}[5] = 1/4$ and zero elsewhere
    - C. $r_{xy}[0] = 5/4$, $r_{xy}[1] = -8/4$, $r_{xy}[2] = 13/4$, $r_{xy}[3] = 7/4$ and zero elsewhere
    - D. $r_{xy}[0] = 5/4$, $r_{xy}[1] = 8/4$, $r_{xy}[2] = 13/4$, $r_{xy}[3] = 7/4$ and zero elsewhere

???+ solution "Solution"
    Read the stems: $x=[1,1,1,0]$ and $y=[1,3,3,5]$ for $n=0,1,2,3$. "Ergodic" lets us replace $E\{\cdot\}$ by a time average over the $N=4$ samples:

    $$\hat r_{xy}[l]=\frac14\sum_n x[n]\,y[n-l].$$

    Slide $y$ along $x$ and add the products where both exist:

    | $l$ | products | $\hat r_{xy}[l]$ |
    |---|---|---|
    | $-3$ | $x_0y_3=5$ | $5/4$ |
    | $-2$ | $x_0y_2+x_1y_3=3+5$ | $8/4$ |
    | $-1$ | $x_0y_1+x_1y_2+x_2y_3=3+3+5$ | $11/4$ |
    | $0$ | $1+3+3+0$ | $7/4$ |
    | $1$ | $x_1y_0+x_2y_1+x_3y_2=1+3+0$ | $4/4$ |
    | $2$ | $x_2y_0+x_3y_1=1+0$ | $1/4$ |

    These are exactly the numbers of option B, but B puts them at lags $0\dots5$ instead of $-3\dots2$. The official key: *"Due to mistake, there is no correct answer. The closest is B, but the correct answer should be shifted by 3."* All values are positive (everything is $\ge0$), which rules out A and C immediately.

    !!! answer "Answer"
        **B** (the right values, shifted by 3 lags; strictly no option is correct)
