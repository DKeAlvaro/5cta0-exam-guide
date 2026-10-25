# 2.3 Least-squares line

<div class="meta"><span>In April 2025 (1 point) and Jan 2020</span><span>15 min</span></div>

## What the exam asks

"Find the linear function with least squares error for the data $\{(0,3),(2,4),(3,3)\}$." A small table and two formulas.

## The idea in one minute

We want the line $y=a\,x+b$ that passes "as close as possible" to the points. For each point, the **miss** is the vertical distance between the point and the line. Least squares squares each miss and adds them up, then picks $a$ and $b$ that make this total as small as possible. In the picture, each squared miss is a real square: make the orange area as small as you can, then press the button.

<div class="widget" data-w="ls"></div>

## The recipe

!!! recipe key "LS line in 3 steps"
    1. Means: $\bar x=\frac1N\sum x_n$, $\ \bar y=\frac1N\sum y_n$.
    2. Slope: $a=\dfrac{\sum_n(x_n-\bar x)(y_n-\bar y)}{\sum_n(x_n-\bar x)^2}$.
    3. Intercept: $b=\bar y-a\,\bar x$ (the line always passes through the "centre" $(\bar x,\bar y)$).

## Watch it once: April 2025 · 2b

!!! exam "Final exam, 13 April 2025 · 2b · 1 p"
    Find the linear function having least squares error for the data $\{(0, 3), (2, 4), (3, 3)\}$.

<div class="stepper" markdown>

**Step 1 · Means.** $\bar x=\frac{0+2+3}{3}=\frac53$, $\ \bar y=\frac{3+4+3}{3}=\frac{10}3$.

***

**Step 2 · Table.**

| $x$ | $y$ | $x-\bar x$ | $y-\bar y$ | product | $(x-\bar x)^2$ |
|---|---|---|---|---|---|
| 0 | 3 | $-\frac53$ | $-\frac13$ | $\frac59$ | $\frac{25}9$ |
| 2 | 4 | $\frac13$ | $\frac23$ | $\frac29$ | $\frac19$ |
| 3 | 3 | $\frac43$ | $-\frac13$ | $-\frac49$ | $\frac{16}9$ |
| | | | **sum** | $\frac39$ | $\frac{42}9$ |

***

**Step 3 · Slope.** $a=\dfrac{3/9}{42/9}=\dfrac3{42}=\dfrac1{14}$.

***

**Step 4 · Intercept.** $b=\frac{10}3-\frac1{14}\cdot\frac53=\frac{10}3-\frac5{42}=\frac{140-5}{42}=\frac{135}{42}=\frac{45}{14}$.

$$y=\frac1{14}x+\frac{45}{14}\approx0.071x+3.21$$

</div>

## Your turn (practice numbers, not from an exam)

!!! exam "Practice"
    Find the least-squares line for $\{(0,1),(1,3),(2,4)\}$.

??? solution "Check your answer"
    **What is being asked?** The line $y=ax+b$ that minimises the sum of squared misses, for the three points $(0,1),(1,3),(2,4)$.

    **Step 1 · Means.** $\bar x=\frac{0+1+2}{3}=1$, $\ \bar y=\frac{1+3+4}{3}=\frac83$.

    **Step 2 · Table** (same as the [recipe](#the-recipe)):

    | $x$ | $y$ | $x-\bar x$ | $y-\bar y$ | product | $(x-\bar x)^2$ |
    |---|---|---|---|---|---|
    | 0 | 1 | $-1$ | $-\frac53$ | $\frac53$ | $1$ |
    | 1 | 3 | $0$ | $\frac13$ | $0$ | $0$ |
    | 2 | 4 | $1$ | $\frac43$ | $\frac43$ | $1$ |
    | | | | **sum** | $3$ | $2$ |

    **Step 3 · Slope.** $a=\dfrac{\text{sum of products}}{\text{sum of squares}}=\dfrac32$.

    **Step 4 · Intercept.** $b=\bar y-a\bar x=\dfrac83-\dfrac32\cdot1=\dfrac{16-9}{6}=\dfrac76$.

    **Step 5 · Check.** The line must pass through $(\bar x,\bar y)$: $1.5\cdot1+\frac76=\frac32+\frac76=\frac{16}{6}=\frac83$ ✓.

    !!! answer "Answer"
        $y=1.5x+\frac76\approx1.5x+1.17$

!!! idea "Facts that appear in multiple choice"
    - LS needs **no probability model**: it only minimises the squared misses.
    - If the noise is Gaussian, the LS estimate equals the MLE.
    - Some nonlinear LS problems can be solved by splitting them into a linear and a nonlinear part, or by transforming them into a linear problem (January 2022 2c, the TRUE one).
