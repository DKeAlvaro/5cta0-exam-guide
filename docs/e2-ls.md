# 2.3 Least-squares line

<div class="meta"><span class="hot">1 point in April 2025, 2.5 in Jan 2020</span><span>+ 3 multiple choice</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep3_estimation.mp4" poster="video/pod_ep3_estimation.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 3, Estimation: MLE and MAP</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

We want the line $y=a\,x+b$ that passes "as close as possible" to the points. For each point, the **miss** is the vertical distance between the point and the line. Least squares squares each miss and adds them up, then picks $a$ and $b$ that make this total as small as possible. In the picture, each squared miss is a real square: make the orange area as small as you can, then press the button.

<div class="widget" data-w="ls"></div>

Nothing probabilistic is happening: **least squares needs no model at all**, just points. (If the noise *is* Gaussian, this same answer is also the MLE — that is a bonus, not a step.)

## How to fight this section with the sheet

The exam says **"least squares", "LSE", "fit a line", "linear function"** with a list of points → you open **box 2C** on your A4 sheet and do its 3 steps. That is the whole method for the "fit a line" question, and it is worth a full point for about four minutes of arithmetic.

Each step below names **the sheet's term it uses**. Press **Next step** to go one at a time — cover the step, do it yourself, then reveal it.

!!! sheet "Box 2C, exactly as it is printed on the sheet"
    **IF YOU SEE** points $(x,y)$ + "least squares"/"least-squares"/"LSE", "linear function", "fit a line"

    1. Means $\bar x$ and $\bar y$.
    2. Slope $a=\dfrac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}$.
    3. $b=\bar y-a\bar x$. Answer: $y=ax+b$. Check: $x=\bar x$ must give $y=\bar y$.

    *Apr25* $(0,3),(2,4),(3,3)$: $\bar x=\frac53$, $\bar y=\frac{10}3$, $a=\frac{1/3}{14/3}=\frac1{14}$, $b=\frac{45}{14}$ → $y=\frac1{14}x+\frac{45}{14}$.

    Also: $x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$. $x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$.

    **Beyond a straight line.** $J(\theta)=\sum_n(x[n]-s[n;\theta])^2$, $\hat\theta=\arg\min J$ — write this when they ask "what kind of estimator". One amplitude $s[n]=Ah[n]$: $\hat A=\dfrac{\sum x[n]h[n]}{\sum h[n]^2}$. Linear model $x=\mathbf H\theta+w$: $\hat\theta=(\mathbf H^T\mathbf H)^{-1}\mathbf H^Tx$; the **error** $x-\mathbf H\hat\theta$ is orthogonal to the columns of $\mathbf H$ (it is the error, **not** $\hat\theta$); WLS with $\mathbf W=\mathbf C_x^{-1}$ = **BLUE**. Nonlinear: transform it (the $e^{\bar x}$ line), or iterate **Gauss–Newton** $\theta_{k+1}=\theta_k+(\mathbf G^T\mathbf G)^{-1}\mathbf G^T(x-s(\theta_k))$, $\mathbf G[:,i]=\frac{\partial s}{\partial\theta_i}$ — Newton–Raphson works too, "only Gauss–Newton" is **false**.

What each line of the box means:

| the sheet says | what you actually do |
|---|---|
| "Means $\bar x$ and $\bar y$" | do this **first**, before any table: $\bar x=\frac1N\sum x_n$, $\bar y=\frac1N\sum y_n$ |
| $\sum(x-\bar x)(y-\bar y)$ | build a 5-column table ($x$, $y$, $x-\bar x$, $y-\bar y$, product) and add the product column |
| $\sum(x-\bar x)^2$ | the last column of the same table |
| "$b=\bar y-a\bar x$" | the line always passes through the centre point $(\bar x,\bar y)$ |
| "Check: $x=\bar x$ must give $y=\bar y$" | a 5-second check that catches every arithmetic slip |
| "$x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$" | box 2C already did the LS for you: this is the case $h[n]=1$ |
| "$x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$" | the "transform the problem into a linear one" trick, already solved — write this line down |

**This is now printed on your A4**, at the bottom of box 2C under "**Beyond a straight line**". The three numbered steps of the box stop at the straight line; the exams do not.

- **Cost and estimator.** $J(\theta)=\displaystyle\sum_n\big(x[n]-s[n;\theta]\big)^2$, and $\hat\theta=\arg\min_\theta J$. That is the definition of "least squares"; write it when they ask "what kind of estimator".
- **Linear in one amplitude.** If $s[n]=A\,h[n]$ (any shape $h$, one unknown $A$): $\hat A=\dfrac{\sum_n x[n]h[n]}{\sum_n h[n]^2}$.
- **Linear model** $x=\mathbf H\theta+w$: $\hat\theta=(\mathbf H^T\mathbf H)^{-1}\mathbf H^Tx$. The **error** $x-\mathbf H\hat\theta$ is orthogonal to the columns of $\mathbf H$ (it is the *error* that is orthogonal, **not** $\hat\theta$). You need at least as many data as unknowns. Weighted LS with $\mathbf W=\mathbf C_x^{-1}$ is the **BLUE**.
- **Nonlinear**, two ways out: split into a linear and a nonlinear part, **or** transform the problem until it is linear (the $e^{\bar x}$ line). **Gauss–Newton and Newton–Raphson both work** — "only Gauss–Newton" is false.
- **Gauss–Newton.** Linearise $s(\theta)$ at $\theta_k$, then solve the linear LS: $\theta_{k+1}=\theta_k+(\mathbf G^T\mathbf G)^{-1}\mathbf G^T\big(x-s(\theta_k)\big)$, where $\mathbf G$ has one column per parameter, $\mathbf G[:,i]=\dfrac{\partial s}{\partial\theta_i}$.

## 1 · April 2025 · 2b — the classic. Read this one with the sheet next to you

!!! exam "Final exam, 13 April 2025 · 2b · 1 p"
    Find the linear function having least squares error for the data $\{(0, 3), (2, 4), (3, 3)\}$.

!!! sheet "In the cheat sheet: box 2C, every line used (the *Apr25* line runs the three steps on these numbers)"
    <div class="stepper" markdown>

    **Sheet step 1 · "Means $\bar x$ and $\bar y$."**
    Three points, so divide by 3 (Calculations: $\sum_n x_n=N\bar x$):

    $$\bar x=\frac{0+2+3}{3}=\frac53,\qquad \bar y=\frac{3+4+3}{3}=\frac{10}{3}$$

    ***

    **Sheet step 2 · the table for $\sum(x-\bar x)(y-\bar y)$ and $\sum(x-\bar x)^2$.**
    Fill the middle two columns first, then multiply across and square down:

    | $x$ | $y$ | $x-\bar x$ | $y-\bar y$ | product | $(x-\bar x)^2$ |
    |---|---|---|---|---|---|
    | 0 | 3 | $-\frac53$ | $-\frac13$ | $\frac59$ | $\frac{25}9$ |
    | 2 | 4 | $\frac13$ | $\frac23$ | $\frac29$ | $\frac19$ |
    | 3 | 3 | $\frac43$ | $-\frac13$ | $-\frac49$ | $\frac{16}9$ |
    | | | | **sum** | $\frac{5+2-4}{9}=\frac39$ | $\frac{25+1+16}{9}=\frac{42}9$ |

    ***

    **Sheet step 3 · "Slope $a$".**
    $$a=\frac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}=\frac{3/9}{42/9}=\frac{3}{42}=\frac{1}{14}$$
    (The $/9$ cancels top and bottom — Calculations: $\frac ab\div\frac cd=\frac{ad}{bc}$.)

    ***

    **Sheet step 4 · "$b=\bar y-a\bar x$".**
    $$b=\frac{10}{3}-\frac{1}{14}\cdot\frac{5}{3}=\frac{10}{3}-\frac{5}{42}=\frac{140-5}{42}=\frac{135}{42}=\frac{45}{14}$$

    ***

    **Sheet step 5 · the sheet's check.** "$x=\bar x$ must give $y=\bar y$":
    $\frac1{14}\cdot\frac53+\frac{45}{14}=\frac{5}{42}+\frac{135}{42}=\frac{140}{42}=\frac{10}{3}=\bar y$ ✓

    ***

    **Sheet check · the box's own check.**
    Step 3: *"Check: $x=\bar x$ must give $y=\bar y$."* $\frac1{14}\cdot\frac53+\frac{45}{14}=\frac{5+135}{42}=\frac{10}3=\bar y$ ✓ — the line goes through the centre point, whatever the data are.

    </div>

!!! answer "Answer"
    $\displaystyle y=\frac{1}{14}x+\frac{45}{14}\approx 0.071\,x+3.21$

## 2 · Q3 2022-23 · 2d — transform, solve the line, transform back

!!! exam "Q3 2022-23 exam · 2d"
    Suppose we observe data from the following signal model:

    $$x[n] = \ln(\theta) + w[n],$$

    with $n = 0, 1, \dots, N - 1$.

    **2d** Can you find a way to avoid the non linear optimization? In other words, can you find a closed-form solution for $\hat{\theta}_{LSE}$?

!!! sheet "In the cheat sheet: box 2C, the last line"
    <div class="stepper" markdown>

    **Sheet step 0 · look at the bottom of box 2C first.**
    The pattern rule: *"$x[n]=\ln\theta+\text{noise}$ → $\hat\theta=e^{\bar x}$"*. That line is the **output** of the three moves below — run them yourself and any variant (a scale factor, $\theta^2$, a different link) falls the same way.

    ***

    **Sheet step 1 · why that line is allowed.**
    The model is $x[n]=\ln\theta+w[n]$. Call $\alpha=\ln\theta$ — then the model is $x[n]=\alpha+w[n]$, which is *linear* in $\alpha$ (a constant plus noise). That is the sheet's margin rule: *"transform the problem into a linear problem"*.

    ***

    **Sheet step 2 · least squares in $\alpha$.**
    $J(\alpha)=\sum_n (x[n]-\alpha)^2$ is minimised by the average of the data (box 2C's other line, "$x[n]=\theta+\text{noise}$ → $\hat\theta=\bar x$", with $\theta$ renamed $\alpha$):

    $$\hat\alpha=\bar x=\frac1N\sum_{n=0}^{N-1}x[n]$$

    ***

    **Sheet step 3 · transform back.**
    $\alpha=\ln\theta$ is one-to-one, so invert it (Calculations strip: "$y=k\ln x$ → $x=e^{y/k}$" with $k=1$):

    $$\hat\theta_{LSE}=e^{\hat\alpha}=e^{\bar x}$$

    ***

    **Sheet check · same idea as the MLE invariance.**
    Box 2D's row *"MLE of $\alpha=\psi(\theta)$: $\hat\theta=\psi^{-1}(\hat\alpha)$"* is the same move. The question says "avoid the non linear optimization" — this is exactly how you avoid it.

    </div>

!!! answer "Answer"
    $\displaystyle\hat\theta_{LSE}=e^{\bar x}=e^{\frac1N\sum_n x[n]}$

## 3 · Q3 2023 resit · 2c — the BLUE sentence

!!! exam "Q3 2023 resit · 2c"
    Which statement about the least square estimator is TRUE?

    - a) For linear system models $x = \mathbf{H}\theta + w$, the estimation error is in the column space of the observation matrix $\mathbf{H}$.
    - b) To find the least square estimate, we need exactly as many observations as parameters to be estimated.
    - c) For a linear model $x = \mathbf{H}\theta + w$ with mean $\mathrm{E}[x] = \mathbf{H}\theta$ and covariance matrix $\mathbf{C}_{\mathbf{x}}$, the weighted least square estimator with weighting matrix $\mathbf{W} = \mathbf{C}_{\mathbf{x}}^{-1}$ is the best linear unbiased estimator.

!!! sheet "In the cheat sheet: not a box — the margin line you wrote"
    <div class="stepper" markdown>

    **Sheet step 1 · (c) is the margin line word for word.**
    *"Weighted LS with $\mathbf W=\mathbf C_x^{-1}$ is the BLUE."* → **TRUE**.

    ***

    **Sheet step 2 · (a) is the trap.**
    The **error** $x-\mathbf H\hat\theta$ is **orthogonal** to the columns of $\mathbf H$ — orthogonal means *outside* the column space, not in it. (It is the error that is orthogonal; $\hat\theta$ itself lives entirely inside the column space.)

    ***

    **Sheet step 3 · (b) is the other trap.**
    "Exactly as many" — no: you need **at least** as many observations as parameters. More observations is the normal case (that is what $N\gg1$ means).

    </div>

!!! answer "Answer"
    **(c)**

## 4 · January 2022 · 2c — how you get out of a nonlinear problem

!!! exam "Resit, January 2022 · 2c · 0.3 p"
    Which of the following statements about the least-squares estimator is true?

    - (a) Some nonlinear least-squares estimation problems can be solved analytically by either separating the problem into nonlinear and linear least-squares problems or by transforming the nonlinear problem into a linear problem.
    - (b) For linear signal models, the solution vector $\hat{\theta}$ is orthogonal to the span of the columns of the observation matrix $\mathbf{H}$.
    - (c) Only the Gauss-Newton method can be applied for nonlinear least-squares problems but not the Newton-Raphson method.

!!! sheet "In the cheat sheet: the margin lines again"
    <div class="stepper" markdown>

    **Sheet step 1 · (a) is the margin line, literally.**
    *"Nonlinear, two ways out: split into a linear and a nonlinear part, **or** transform the problem until it is linear."* → **TRUE**. Exercise 2 above is the transform version.

    ***

    **Sheet step 2 · (b) is the same trap as the previous question.**
    The **error** is orthogonal to the columns of $\mathbf H$, not the solution vector $\hat\theta$.

    ***

    **Sheet step 3 · (c) is the "only" trap.**
    *"Gauss–Newton **and** Newton–Raphson both work"* — "only Gauss–Newton" is false.

    </div>

!!! answer "Answer"
    **(a)**

## 5 · January 2020 · 4 — the 2.5-point one: amplitude and a power

!!! exam "Retake, January 2020 · Exercise 4 · 2.5 p"
    Consider the observed data $x[0], x[1], \dots, x[n]$, which consists of independent identically distributed samples. The data comes from an experiment, which generates a signal according to model

    $$s[n] = Ae^{\phi n}$$

    where the amplitude $A$ and the power term $\phi \lt 0$ are to be estimated based on the observed data.

    - (a) What kind of estimators can be used to solve this problem? Explain your reasoning and write down the formulations for the estimators that can be used. [0.5 pt.]
    - (b) For the case where $\phi$ is known but $A$ is unknown, find an estimator for $A$. The estimator you find must have a closed form that depends on $\phi$ and observed data $x[0], x[1], \dots, x[n]$. [0.5 pt.]
    - (c) For the case where both $\phi$ and $A$ are unknown, write the cost function for an estimator for $\theta = [\phi \ A]^T$, where $[\cdot]^T$ indicates the transpose of a vector or matrix. **Hint:** The expression you find will be non-linear, which is why the solution in (d) is asked. [0.5 pt.]
    - (d) Formulate the Gauss-Newton solution for the estimator cost function derived in (c). Clearly show the iterative formulation. [1 pt.]

!!! sheet "In the cheat sheet: box 2C starts it, the margin lines finish it"
    <div class="stepper" markdown>

    **Sheet step (a) · write the definition of least squares.**
    No pdf for the noise is given, so there is no likelihood → the ML route (box 2A) is closed. Least squares needs **no model of the noise**, only a model of the signal, so it is always available:

    $$J(\theta)=\sum_{n=0}^{N-1}\big(x[n]-s[n;\theta]\big)^2,\qquad \hat\theta=\arg\min_\theta J(\theta)$$

    (If you want a second one: when the noise is Gaussian, this same $\hat\theta$ is also the MLE. Say it as a remark.)

    ***

    **Sheet step (b) · $\phi$ known → the problem is linear in $A$.**
    The margin line: *"If $s[n]=A\,h[n]$ … $\hat A=\frac{\sum x[n]h[n]}{\sum h[n]^2}$"*. Here $h[n]=e^{\phi n}$, so

    $$J(A)=\sum_n\big(x[n]-A e^{\phi n}\big)^2,\qquad \frac{dJ}{dA}=-2\sum_n e^{\phi n}\big(x[n]-Ae^{\phi n}\big)=0$$

    $$A\sum_n e^{2\phi n}=\sum_n x[n]e^{\phi n}\qquad\Longrightarrow\qquad \hat A=\frac{\sum_n x[n]e^{\phi n}}{\sum_n e^{2\phi n}}$$

    (Closed form, as required. Sanity: if $\phi=0$ then $e^{\phi n}=1$ and $\hat A=\bar x$ — box 2C's first extra line.)

    ***

    **Sheet step (c) · both unknown → write the cost and stop.**
    $\theta=[\phi\ A]^T$, so plug both into $J$:

    $$J(\phi,A)=\sum_{n=0}^{N-1}\big(x[n]-A e^{\phi n}\big)^2$$

    The hint is telling you this is **nonlinear** in $\theta$ (the $Ae^{\phi n}$ has the unknowns multiplied and in an exponent) — that is the whole reason for (d). 0.5 points for writing it down.

    ***

    **Sheet step (d) · Gauss–Newton** (the last margin line).
    Linearise $s(\theta)$ at the current guess $\theta_k$:

    $$s(\theta)\approx s(\theta_k)+\mathbf G_k\,(\theta-\theta_k)$$

    Build $\mathbf G_k$ one column per parameter, $\mathbf G[:,i]=\frac{\partial s}{\partial\theta_i}$, evaluated at $\theta_k=[\phi_k\ A_k]^T$:

    $$\frac{\partial s}{\partial A}=e^{\phi n},\qquad \frac{\partial s}{\partial \phi}=A\,n\,e^{\phi n} \qquad\Longrightarrow\qquad \mathbf G_k[n]=\Big[\;A_k\,n\,e^{\phi_k n}\ \ \ e^{\phi_k n}\;\Big]$$

    Then the update:

    $$\boxed{\ \theta_{k+1}=\theta_k+(\mathbf G_k^T\mathbf G_k)^{-1}\mathbf G_k^T\big(x-s(\theta_k)\big)\ }$$

    Iterate until $\theta_{k+1}$ stops changing. ($x$ is the column vector of the data, $s(\theta_k)$ the column vector of the model at $\theta_k$.)

    ***

    **Sheet check · what each piece costs.**
    (a) 0.5 for the definition + "why": no noise model needed. (b) 0.5 for the closed form. (c) 0.5 for the cost. (d) 1 for $\mathbf G$ **and** the iteration — write both, the update alone loses half.

    </div>

!!! answer "Answer"
    **(a)** LS: $J=\sum_n(x[n]-s[n;\theta])^2$, $\hat\theta=\arg\min J$ (no noise model needed; = MLE for Gaussian noise) · **(b)** $\hat A=\dfrac{\sum_n x[n]e^{\phi n}}{\sum_n e^{2\phi n}}$ · **(c)** $J(\phi,A)=\sum_n (x[n]-Ae^{\phi n})^2$ · **(d)** $\mathbf G_k[n]=\big[A_k n e^{\phi_k n},\ e^{\phi_k n}\big]$, $\ \theta_{k+1}=\theta_k+(\mathbf G_k^T\mathbf G_k)^{-1}\mathbf G_k^T(x-s(\theta_k))$

## Traps

!!! trap "Where points are lost (each one is a line of the sheet you skipped)"
    - Doing $\bar x$ and $\bar y$ **after** the table. Box 2C lists them as step 1 because every column depends on them.
    - Slope formula upside down: $a=\dfrac{\text{product sum}}{\text{square sum}}$, not the other way round.
    - Forgetting to write the **domain** or to answer with the full line "$y=ax+b$". The exam wants the function, not just $a$.
    - Skipping the check "$x=\bar x$ gives $y=\bar y$". It is free, and it catches every arithmetic slip.
    - $x[n]=\ln\theta+\text{noise}$ → answer $e^{\bar x}$, **not** $\ln\bar x$. The sheet's last line is the whole question.
    - Saying the **estimate** $\hat\theta$ is orthogonal to the columns of $\mathbf H$. It is the **error** that is orthogonal.
    - "Exactly as many observations as parameters" → false, it is **at least**.
    - "Only Gauss–Newton works for nonlinear LS" → false, Newton–Raphson does too.
    - Gauss–Newton: writing the update but not $\mathbf G$. Half the points are for the columns $\frac{\partial s}{\partial\theta_i}$.
