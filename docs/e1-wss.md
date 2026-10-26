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

The exam says **"WSS"**, **"ergodic"**, **"dice"**, **"random phase"** → you open **box 1B** on your A4 sheet. It gives the definition and a **3-test procedure** you run on whatever process the exam hands you: **mean → correlation → ergodicity**. The sheet never prints the verdict for a process — you produce it with the three tests, and the sheet's worked lines show you the speed and the shape of each step.

!!! sheet "Box 1B, exactly as it is printed on the sheet"
    **IF YOU SEE** "WSS"/"wide-sense stationary"/"stationary", "ergodic", dice, random phase, random amplitude

    **WSS** = the mean is constant AND the autocorrelation depends only on the lag $\tau$ (not on $t$) · **Ergodic** = averaging ONE signal over time gives the same as averaging over all signals. The exam hands you **a process to test** — no list to look it up: run the 3 tests:

    1. **Mean.** $E[x(t)]$, box 1E rules (constants come out; uniform $[a,b]$ → $\frac{a+b}2$). The $t$ has to cancel → constant. Still moves with $t$ → **not WSS**, stop.
    2. **Correlation.** $r(t_1,t_2)=E[x(t_1)x(t_2)]$ — expand the product ($\cos\alpha\cos\beta$), average the random letters away. Only $(t_1-t_2)$ survives → **WSS**; a lone $t$ or $t_1+t_2$ survives → **not WSS**.
    3. **Ergodic in the mean.** Freeze ONE realisation, take its long-time average, compare with test 1's mean. Fresh randomness at **every** time (random phase, dice, a stream of numbers) → the realisation sees every value → **yes**. One random letter frozen for **all** time (random amplitude $A$) → time averaging cannot remove it → **no**. "in the variance" too → same rule on $x^2$.

    *Worked, random phase $\cos(t+U)$:* $E[\cos(t+U)]=0$ — a uniform phase averages a whole turn to 0 → constant ✓. $r=E[\cos(t_1{+}U)\cos(t_2{+}U)]=\frac12\cos(t_1-t_2)$ ✓ (the $2U$ term averages to 0) → **WSS**, and one realisation $\cos(t+u)$ has long-time average $0=$ the mean → **ergodic in the mean**.
    *Worked, random amplitude $A\cos t$:* $E[A\cos t]=E[A]\cos t$ moves with $t$ → **not WSS**, stop. *Dice rolled forever:* fresh roll every time → **ergodic in mean AND variance**. *Numbers uniform in $[-A,A]$ streamed:* mean $\frac{-A+A}2=0$ whatever $A$ is (test 1), each realisation sweeps the whole range → **ergodic, mean 0**.

    **Words (Jan22-1b):** a *random process* = the whole infinite **set** of possible signals (the ensemble) · one recording (one picture) = a **realisation** = a random signal · one number / one pixel = a random **variable**. A set of pictures is WSS only if the question says the statistics do not shift. Definition MC: pick the option saying the WSS line above **word for word** (the wrong ones name ergodic, strict stationarity or white noise).

Two more sheet places: **box 1E** ("Rules": $E[c\cdot z]=c\,E[z]$, uniform $[a,b]$ → mean $\frac{a+b}2$) when the mean has to be computed, and the **Calculations** strip for $\cos\alpha\cos\beta$ (bottom of the Part 3 band).

## 1 · April 2024 · 1d — the two processes, run the tests on each

!!! exam "Final exam, April 2024 · 1d · 0.3 p"
    For the following random processes, indicate if they are WSS and ergodic in the mean:

    1. $X(t) = \cos(t + U)$, where $U \sim Uniform(0, 2\pi)$
    2. $X(t) = A \cos(t)$, where $A \sim N(1, 2)$

    The following formula might be useful:

    $$\cos(\alpha) \cos(\beta) = \frac{\cos(\alpha + \beta) + \cos(\alpha - \beta)}{2}$$

!!! sheet "In the cheat sheet: box 1B — run the 3 tests on each process"
    <div class="stepper" markdown>

    **Sheet step 1 · test 1 (mean) on process 1.**
    *"$E[\cos(t+U)]=0$ — a uniform phase averages a whole turn to 0"* → constant in every $t$ ✓. Passes, keep going.

    ***

    **Sheet step 2 · test 2 (correlation) on process 1.**
    The worked line: $r=E[\cos(t_1{+}U)\cos(t_2{+}U)]=\frac12\cos(t_1-t_2)$ — expand with $\cos\alpha\cos\beta$, the $2U$ term averages to 0. Only $(t_1-t_2)$ survives ✓ → **WSS**.

    ***

    **Sheet step 3 · test 3 (ergodic) on process 1.**
    Sheet: *"one realisation $\cos(t+u)$ has long-time average $0=$ the mean → **ergodic in the mean**"*. One realisation freezes one $u$, and a cosine's long-time average is 0 whatever the phase ✓.

    ***

    **Sheet step 4 · the same three tests on process 2 stop at test 1.**
    Box 1E: a constant factor comes out → $E[A\cos t]=E[A]\cos t=1\cdot\cos t$, which **moves with $t$**. Test 1: *"Still moves with $t$ → **not WSS**, stop."* No need to compute $r$; not WSS implies not ergodic.

    ***

    **Sheet check · the example line.**
    The sheet's two worked lines *are* these two processes — first one ends **"WSS, ergodic in the mean"**, second one ends **"not WSS, stop"**. Your verdicts must come out the same, whatever processes a new exam invents.

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

!!! sheet "In the cheat sheet: box 1B, test 3 + the dice worked line"
    <div class="stepper" markdown>

    **Sheet step 1 · test 3, the "fresh or frozen" question.**
    The process is *"Dice rolled forever"* — and the sheet's worked line for it: *"fresh roll every time → **ergodic in mean AND variance**"*. The rule behind it: *"Fresh randomness at **every** time (random phase, dice, a stream of numbers) → the realisation sees every value → **yes**."* That is option **(b)**. (April 2025 1d is the same question with options shuffled — "ergodic in both mean and variance", also (b).)

    ***

    **Sheet step 2 · the numbers, if they ask why.**
    The sheet's ergodic line: *"averaging ONE signal over time gives the same as averaging over all signals."* One die rolled forever shows each face in $\frac16$ of its rolls → time average $=\frac{1+2+3+4+5+6}{6}=3.5$, and the same on $x^2$ gives the spread $\frac{35}{12}$. All dice at one time (the ensemble) give the same two numbers. Same → ergodic in both.

    ***

    **Sheet step 3 · kill the neighbours.**
    "(c) only in the mean" understates the verdict. "$E[X]=0$" (Apr25 option c) confuses dice with zero-mean noise — the dice average $3.5$, never 0.

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

!!! sheet "In the cheat sheet: box 1B, the WSS definition + the definition-MC rule"
    <div class="stepper" markdown>

    **Sheet step 1 · read the sheet's definition.**
    *"$\mathbf{WSS} =$ the mean is constant AND the autocorrelation depends only on the lag $\tau$ (not on $t$)"*, and the box's rule for this question type: *"Definition MC: pick the option saying the WSS line above **word for word** (the wrong ones name ergodic, strict stationarity or white noise)."* Option **(b)** is that line word for word.

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

!!! sheet "In the cheat sheet: box 1B, tests 1 and 3 + the uniform-stream worked line"
    <div class="stepper" markdown>

    **Sheet step 1 · test 1 (mean), with box 1E.**
    The sheet's worked line: *"Numbers uniform in $[-A,A]$ streamed: mean $\frac{-A+A}2=0$ whatever $A$ is"* — that is box 1E's *"Uniform $[a,b]$ → mean $\frac{a+b}2$"* with $a=-A$, $b=A$. The random size of $A$ does not matter, the centre is 0 → **mean 0, constant**. That kills (a) and (b) on the mean alone.

    ***

    **Sheet step 2 · test 3 (ergodic).**
    The same worked line ends *"each realisation sweeps the whole range → **ergodic, mean 0**"*. Rule: *"Fresh randomness at **every** time (… a stream of numbers) → the realisation sees every value → **yes**."* Each realisation freezes one $A$ but then keeps drawing evenly on $[-A,A]$, so its time average is $0=$ the ensemble mean ✓ → **(d)**.

    ***

    **Sheet check · the worked line.**
    The worked line *is* this process — but you built the answer from test 1 and test 3, so any variant (uniform on $[0,A]$, uniform on $[A,A+1]$, a different law for $A$) falls to the same two tests instead of a row you cannot find.

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
    - Mixing up test 3's two cases: **fresh randomness at every time** (random phase, dice, a stream of numbers) → ergodic · **one random letter frozen for all time** (random amplitude $A$ in $A\cos t$) → not. The words "random amplitude" in the enunciado decide it.
    - Saying "not ergodic" just because a random $A$ is in the formula. Test 3 asks whether fresh randomness keeps arriving: the dice and the uniform stream do, so they are ergodic; $A\cos t$ is one scaled cosine, so it is not.
    - Calling the dice "mean 0" (Apr25's trap). Fair dice average 3.5 — test 1 gives the mean, the formula never says 0.
    - Answering (c) "the PDF stays constant" to "what does WSS require" — that is strict stationarity; the sheet's WSS line has only mean + autocorrelation.
    - Forgetting that "is it WSS?" is two checks, not one: tests 1 **and** 2 (constant mean **and** lag-only correlation). $A\cos t$ fails the first one.
    - Using $E[A\cos t]=E[A]\cos t$ without noticing the $t$ is still there — box 1E: "a constant factor comes out", but $\cos t$ is not constant in $t$.
