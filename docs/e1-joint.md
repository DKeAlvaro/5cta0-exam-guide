# 1.2 Joint PDFs: find $c$, marginal, conditional, independent

<div class="meta"><span class="hot">In 4 of the last 4 exams</span><span>0.3–0.5 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## What the exam asks

You get a formula $p_{X,Y}(x,y)$ that is non-zero only on some **region** of the $(x,y)$ plane. They ask some of: **(a)** find the constant $c$, **(b)** the marginal $p_X(x)$ or $p_Y(y)$ **with its domain**, **(c)** the conditional $p_{X\mid Y}(x\mid y)$, **(d)** are $X$ and $Y$ independent? Usually "final answer only".

## The idea in one minute

Think of $p(x,y)$ as a **height** above the region. Three facts:

- The total volume under it is 1 (that is how you find $c$).
- The **marginal** $p_Y(y)$: stand at height $y$, walk across the region horizontally, and add up the heights you pass: $p_Y(y)=\int p(x,y)\,dx$ **along that slice**.
- The only hard part is **where the slice starts and ends**. Read it off a drawing. Always draw the region.

Move the slice and watch the marginal being traced:

<div class="widget" data-w="region" data-preset="0"></div>

## The recipe

!!! recipe key "Joint PDF questions"
    1. **Draw the region.** Mark its corners and boundary lines.
    2. **Find $c$**: $\iint p=1$. Inner integral along a slice (limits from the drawing), outer integral over all slice positions.
    3. **Marginal** $p_Y(y)=\int p(x,y)\,dx$, with $x$ running across the slice at height $y$. Write the domain of $y$ ("for $0\le y\le1$, 0 otherwise").
    4. **Conditional** $p_{X\mid Y}(x\mid y)=\dfrac{p(x,y)}{p_Y(y)}$; its domain is the slice.
    5. **Independent** $\iff p(x,y)=p_X(x)\,p_Y(y)$ everywhere. Quick test: the region is a **rectangle** and the formula splits as (only $x$)·(only $y$). A triangle is never independent.

!!! idea "The only integral rule you need"
    $\int_a^b x^n\,dx=\Big[\frac{x^{n+1}}{n+1}\Big]_a^b$, and anything that does not contain the integration variable comes out as a constant: $\int_0^1 6x^2y\,dy=6x^2\int_0^1y\,dy=6x^2\cdot\frac12$.

## Watch it once: April 2024 · 1c (marginal + conditional)

!!! exam "Final exam, April 2024 · 1c · 0.3 p"
    $p_{X,Y}(x,y) = 2$ for $0 \leq y \leq x \leq 1$, 0 otherwise. Find $p_Y(y)$ and $p_{X|Y}(x|y)$, with their domains. **Final answer only.**

<div class="stepper" markdown>

**Step 1 · Draw.** $0\le y\le x\le1$: $y$ is below $x$, so the region is the triangle **under the diagonal** $y=x$, with corners $(0,0)$, $(1,0)$, $(1,1)$. (First tab of the widget.)

***

**Step 2 · The slice at height $y$.** Walking right at height $y$, you enter the triangle at the diagonal, $x=y$, and leave at $x=1$.

***

**Step 3 · Marginal.** $p_Y(y)=\displaystyle\int_y^1 2\,dx=2(1-y)$ for $0\le y\le1$, 0 otherwise.
Check: $\int_0^12(1-y)\,dy=2\cdot\frac12=1$ ✓.

***

**Step 4 · Conditional.** $p_{X\mid Y}(x\mid y)=\dfrac{2}{2(1-y)}=\dfrac1{1-y}$ for $y\le x\le1$ (the slice), 0 otherwise. It is flat along the slice: uniform.

</div>

## Watch it once more: April 2025 · 1c (find $c$)

!!! exam "Final exam, 13 April 2025 · 1c · 0.3 p"
    $p_{X,Y}(x,y) = cx + 1$ for $x, y \geq 0,\ x + y < 1$, 0 otherwise. Find the constant $c$. **Final answer only.**

<div class="stepper" markdown>

**Step 1 · Draw.** $x,y\ge0$ and $x+y<1$: the triangle with corners $(0,0)$, $(1,0)$, $(0,1)$, below the line $y=1-x$. (Second tab.)

***

**Step 2 · Inner integral (vertical slice at $x$).** $y$ goes from 0 to $1-x$. The height $cx+1$ has no $y$, so it is height × length: $\int_0^{1-x}(cx+1)\,dy=(cx+1)(1-x)$.

***

**Step 3 · Outer integral.** $\int_0^1(cx+1)(1-x)\,dx=\int_0^1(cx-cx^2+1-x)\,dx=\frac c2-\frac c3+1-\frac12=\frac c6+\frac12$.

***

**Step 4 · Set to 1.** $\frac c6+\frac12=1$ → $c=\mathbf 3$.

</div>

## Your turn

!!! exam "Resit, June 2026 · 1c · 0.5 p"
    $p_{X,Y}(x, y) = 6x^2y$ for $0 \leq x \leq 1$ and $0 \leq y \leq 1$, 0 otherwise. **Final answer only.**

    1. Find the marginal PDF $p_X(x)$ and indicate its domain. [0.25]
    2. Determine whether $X$ and $Y$ are independent, and briefly justify why. [0.25]

??? solution "Check your answer"
    The region is the unit square (third tab), so every slice runs from 0 to 1.
    $p_X(x)=\int_0^16x^2y\,dy=6x^2\cdot\frac12=3x^2$. Likewise $p_Y(y)=\int_0^16x^2y\,dx=6y\cdot\frac13=2y$. Product: $3x^2\cdot2y=6x^2y$ = the joint. ✓

    !!! answer "Answer"
        1. $p_X(x)=3x^2$ for $0\le x\le1$, 0 otherwise. 2. **Independent**: the support is a rectangle and $p_{X,Y}=p_X\,p_Y=3x^2\cdot2y$.

## Quick facts for the MC

<div class="tf" markdown>

| Statement | | Why |
|---|---|---|
| The expected value of a discrete random variable is the weighted average of its values, weighted by the PMF. | T | $E[X]=\sum_x x\,p(x)$. April 2025 1b, answer (d). |
| The expected value is the simple average of the PMF values. | F | Each value must be weighted by its probability. |
| $\text{Var}(X)=E[X^2]-(E[X])^2$. | T | The handy way to compute a variance. |
| Independent variables have zero covariance. | T | $\text{Cov}=E[XY]-E[X]E[Y]=0$ when $E[XY]=E[X]E[Y]$. |
| Zero covariance implies independence. | F | Only the other way round (except for jointly Gaussian variables). |
| A joint PDF on a triangle can be independent if the formula splits into $f(x)g(y)$. | F | The support also has to be a rectangle. On a triangle, knowing $y$ changes the range of $x$. |

</div>

## Traps

!!! trap key "Where points are lost"
    - **No drawing** → wrong limits. The limits of the inner integral can contain the other variable ($x$ from $y$ to 1).
    - **Forgetting the domain** of the marginal or conditional. "Indicate its domain" is half the points.
    - Calling a triangle independent.
