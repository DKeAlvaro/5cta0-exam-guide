# 1.3 Stationary and ergodic

<div class="meta"><span class="hot">In 5 of the last 5 exams</span><span>0.25–0.3 points</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

A **random process** is a whole stack of signals. Example: infinitely many dice, each rolled forever. Die $i$ gives one signal $x_i[n]$, called a **realisation**. Stack them as rows. Now there are two ways to average:

- **Down a column**: all realisations at the same time $n$. That is the **ensemble mean** $E[X[n]]$ (what probability theory computes).
- **Along a row**: one realisation over all time. That is the **time average** (what you can measure from one recording).

<div class="key" markdown>

- **WSS** (wide-sense stationary): the column average is the **same at every $n$**, **and** the correlation between times $n$ and $n+k$ depends **only on the gap $k$**.
- **Ergodic in the mean**: the time average of a single row **equals** the ensemble mean.

</div>

Try the four tabs. In each, compare the red line (time average of row 1) with the blue dashed line (ensemble mean):

<div class="widget" data-w="ensemble"></div>

## How to fight this section with the sheet

The exam says **"WSS"**, **"ergodic"**, **"dice"**, **"random phase"** → you open **box 1B** on your A4 sheet. It gives the definition, a two-line test, and a table of processes whose answer is already printed. Every question below is one of those two things: either read a row of the table, or run the two-line test.

!!! sheet "Box 1B, exactly as it is printed on the sheet"
    **IF YOU SEE** "WSS"/"wide-sense stationary"/"stationary", "ergodic", dice, random phase, random amplitude

    - **WSS** = the mean is constant AND the autocorrelation depends only on the lag $\tau$ (not on $t$). Jun26: pick the option saying exactly this.
    - **Ergodic** = averaging ONE signal over time gives the same as averaging over all signals.
    - **Test it:** is $\mathrm E[x(t)]$ constant in $t$? Does $r(t_1,t_2)$ only depend on $t_1-t_2$? Both yes → WSS. Ergodic: does one long realisation visit every value? Random **phase** → yes, random **amplitude** → no.
    - *$\cos(t+U)$ worked out:* $E[\cos(t+U)]=0$ in every $t$ — a uniform phase averages a whole turn to 0 → constant. $r=E[\cos(t_1{+}U)\cos(t_2{+}U)]=\frac12\cos(t_1-t_2)$ — use $\cos\alpha\cos\beta$; the term carrying $2U$ averages to 0 → only the lag. Time average of one long realisation $=0$ = the mean → **ergodic in the mean**.
    - **Words (Jan22-1b):** a *random process* = the whole infinite **set** of possible signals (the ensemble) · one recording (one picture) = a **realisation** = a random signal · one number / one pixel = a random **variable**. A set of pictures is WSS only if the question says the statistics do not shift.

    | The process | WSS? | Ergodic? |
    |---|---|---|
    | $\cos(t+U)$, $U$ uniform $0..2\pi$ (random phase) | yes | yes |
    | $A\cos t$, $A$ random (random amplitude) | no | no |
    | Many fair dice, each rolled forever | yes | yes, in mean AND variance |
    | Numbers uniform in $[-A,A]$, $A$ random (Nov22) | yes, mean 0 | key: ergodic, mean 0 → (d) |

Two more sheet places: **box 1E** ("Rules": $E[c\cdot z]=c\,E[z]$, uniform $[a,b]$ → mean $\frac{a+b}2$) when the mean has to be computed, and the **Calculations** strip for $\cos\alpha\cos\beta$ (bottom of the Part 3 band).

## 1 · April 2024 · 1d — the two processes, straight from the table

!!! exam "Final exam, April 2024 · 1d · 0.3 p"
    For the following random processes, indicate if they are WSS and ergodic in the mean:

    1. $X(t) = \cos(t + U)$, where $U \sim Uniform(0, 2\pi)$
    2. $X(t) = A \cos(t)$, where $A \sim N(1, 2)$

    The following formula might be useful:

    $$\cos(\alpha) \cos(\beta) = \frac{\cos(\alpha + \beta) + \cos(\alpha - \beta)}{2}$$

!!! sheet "In the cheat sheet: box 1B — the table's first two rows are this question"
    <div class="stepper" markdown>

    **Sheet step 1 · match the words.**
    Process 1 is "$\cos(t+U)$, $U$ uniform $0..2\pi$" = the sheet's **random phase** row. Process 2 is "$A\cos t$, $A$ random" = the **random amplitude** row. Read the two rows: (yes, yes) and (no, no).

    ***

    **Sheet step 2 · prove it with the "Test it" line, process 1.**
    Is $E[x(t)]$ constant? The sheet's worked line: *"$E[\cos(t+U)]=0$ in every $t$ — a uniform phase averages a whole turn to 0"* → constant ✓. Does $r$ depend only on $\tau$? The same line: $r=\frac12\cos(t_1-t_2)$ ✓ → **WSS**.

    ***

    **Sheet step 3 · ergodic, process 1.**
    Sheet: *"Time average of one long realisation $=0$ = the mean → ergodic in the mean."* One row is $\cos(t+u_1)$ with a frozen $u_1$, and a cosine's long-time average is 0 whatever the phase ✓.

    ***

    **Sheet step 4 · process 2, the mean decides it.**
    Box 1E: a constant factor comes out of the average → $E[A\cos t]=E[A]\cos t=1\cdot\cos t$, which **moves with $t$**. The sheet's test: "is $E[x(t)]$ constant in $t$?" → **no** → not WSS, and therefore not ergodic. (The table row says the same: random amplitude → no / no.)

    ***

    **Sheet check · the example line.**
    The sheet's worked line *is* process 1, and the table's first two rows *are* the answer sheet you have to fill. If your table looks like the sheet's table, you have the points.

    </div>

!!! answer "Answer"
    1. WSS **yes**, ergodic in the mean **yes**. 2. WSS **no**, ergodic **no**.

## 2 · January 2022 · 1c and April 2025 · 1d — the dice question (asked twice)

!!! exam "Resit, 24 January 2022 · 1c · 0.3 p"
    Suppose we have infinitely many fair dice and we define a random process as the ensemble of the random signals obtained by rolling each die infinitely many times and recording the number on the upward face. Which of the following statements is true?

    - a) This random process is not ergodic, but it is stationary.
    - b) This random process is ergodic in the mean and variance.
    - c) This random process is ergodic in the mean, but not in the variance.
    - d) None of the above.

!!! sheet "In the cheat sheet: box 1B, table row 3"
    <div class="stepper" markdown>

    **Sheet step 1 · the row.**
    The table has exactly this process: *"Many fair dice, each rolled forever → WSS: yes · Ergodic: **yes, in mean AND variance**"*. That is option **(b)**. (April 2025 1d is the same question with options shuffled — same row, "ergodic in both mean and variance", also (b).)

    ***

    **Sheet step 2 · why, if they ask.**
    The sheet's ergodic line: *"averaging ONE signal over time gives the same as averaging over all signals."* One die rolled forever shows each face in $\frac16$ of its rolls → time average $=\frac{1+2+3+4+5+6}{6}=3.5$, and the spread $\frac{35}{12}$. All dice at one time (the ensemble) give the same two numbers. Same → ergodic in both.

    ***

    **Sheet step 3 · kill the neighbours.**
    "(c) only in the mean" understates the row. "$E[X]=0$" (Apr25 option c) confuses dice with zero-mean noise — the sheet's row never says the mean is 0, and $\frac{1+\dots+6}{6}=3.5$.

    </div>

!!! answer "Answer"
    **(b)** — ergodic in the mean and the variance (both papers).

## 3 · June 2026 · 1d — the definition MC

!!! exam "Resit Q4, June 2026 · 1d · 0.25 p"
    Which of the following conditions is required for a random process to be considered Wide-Sense Stationary (WSS)?

    - (a) Time averages of all its individual realizations are strictly equal to its ensemble averages.
    - (b) Its mean is constant and its autocorrelation function depends only on the time difference (lag).
    - (c) Its probability density function remains strictly constant over all time indices.
    - (d) Its power spectral density is a constant value across all frequencies.

!!! sheet "In the cheat sheet: box 1B, first line — and it names this exam"
    <div class="stepper" markdown>

    **Sheet step 1 · read the sheet's definition.**
    *"$\mathbf{WSS} =$ the mean is constant AND the autocorrelation depends only on the lag $\tau$ (not on $t$). Jun26: pick the option saying exactly this."* The sheet literally tags this exam. That is option **(b)** word for word.

    ***

    **Sheet step 2 · what the others are (the sheet defines them too).**
    (a) is the sheet's **ergodic** line. (c) is strict-sense stationarity — more than WSS. (d) is white noise ("PSD constant"), which the sheet mentions in box 1C as the flat input, not as a WSS condition.

    </div>

!!! answer "Answer"
    **(b)**

## 4 · November 2022 · 1c — uniform numbers with a random $A$

!!! exam "Final exam Q1, 7 November 2022 · 1c · 0.25 p"
    A random process $X(t)$ is represented by a random number generator. For each realization of the random process, the random number generator samples randomly (with equal probability) infinitely many numbers between $-A$ and $A$. Random variable $A$ follows a normal distribution with mean $\mu_A = 1$ and $\sigma_A = 2$. Which of the following statements is TRUE?

    - a) The random process is NOT ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 1$
    - b) The random process is ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 1$
    - c) The random process is NOT ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 0$
    - d) The random process is ergodic. The mean of the process is constant and equal to $\mu_{X(t)} = 0$

!!! sheet "In the cheat sheet: box 1B, table row 4 — the answer is printed"
    <div class="stepper" markdown>

    **Sheet step 1 · the row.**
    *"Numbers uniform in $[-A,A]$, $A$ random (Nov22) → WSS: yes, **mean 0** · key: **ergodic, mean 0 → (d)**."* The sheet prints this exam's answer: mean 0 and ergodic → **(d)**.

    ***

    **Sheet step 2 · why the mean is 0 (box 1E).**
    The numbers are uniform on $[-A,A]$, and box 1E says *"Uniform $[a,b]$ → mean $\frac{a+b}2$"* with $a=-A$, $b=A$: $\frac{-A+A}{2}=0$. The random size of $A$ does not matter — the centre is 0 whatever $A$ is. That kills (a) and (b) on the mean alone.

    ***

    **Sheet step 3 · why ergodic.**
    Each realisation freezes one $A$ and then samples numbers evenly on $[-A,A]$, so its time average is 0 = the ensemble mean. The sheet's ergodic line: *"averaging ONE signal over time gives the same as averaging over all signals"* ✓ → (d).

    </div>

!!! answer "Answer"
    **(d)** — ergodic, mean 0.

## 5 · January 2022 · 1b — the vocabulary question

!!! exam "Resit, 24 January 2022 · 1b · 0.3 p"
    Suppose we are analyzing a infinite set of pictures. For each pixel in each picture we record its color as an integer between 0 and 255. Which of the following statements is true?

    - a) The color of each pixel is a continuous random variable.
    - b) Each picture is a realization of a random process, hence a random signal.
    - c) The infinite set of pictures represents a wide sense stationary random process.
    - d) Each picture represents a random process, and the color of each pixel is a realization of the random process, hence a random signal.

!!! sheet "In the cheat sheet: box 1B, the Words line — and box 1E for 'discrete or continuous'"
    <div class="stepper" markdown>

    **Sheet step 1 · the Words line.**
    *"a random process = the whole infinite set of possible signals · one recording (one picture) = a realisation = a random signal · one number / one pixel = a random variable."* That maps: the **set of pictures** = the process, **one picture** = a realisation = a random signal, **one pixel colour** = a random variable.

    ***

    **Sheet step 2 · read the options against it.**
    (b) says "each picture is a realization of a random process, hence a random signal" — the sheet's sentence, word for word → **(b)**. (d) swaps the roles (it calls one picture a whole process). (c) the Words line warns: *"A set of pictures is WSS only if the question says the statistics do not shift"* — the text says nothing about shifts, so you may not claim WSS.

    ***

    **Sheet step 3 · the colour question (box 1E).**
    *"Discrete = the values can be listed: counts, dice, digits 0–255."* 0–255 is a list → discrete, so (a) is false.

    </div>

!!! answer "Answer"
    **(b)**

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - Mixing up the two sheet rows: random **phase** → yes/yes, random **amplitude** → no/no. The words "random amplitude" in the enunciado are the whole answer.
    - Saying "not ergodic" because the process has a random $A$. The sheet's dice row and Nov22 row show frozen randomness can still be ergodic — what matters is whether one long realisation averages to the ensemble mean.
    - Calling the dice "mean 0" (Apr25's trap). Fair dice average 3.5; the sheet's row never says 0.
    - Answering (c) "the PDF stays constant" to "what does WSS require" — that is strict stationarity; the sheet's WSS line has only mean + autocorrelation.
    - Forgetting that "is it WSS?" is two checks, not one: constant mean **and** lag-only correlation ("Test it" line). $A\cos t$ fails the first one.
    - Using $E[A\cos t]=E[A]\cos t$ without noticing the $t$ is still there — box 1E: "a constant factor comes out", but $\cos t$ is not constant in $t$.
