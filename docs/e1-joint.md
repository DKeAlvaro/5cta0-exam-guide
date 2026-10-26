# 1.2 Joint PDFs: find $c$, marginal, conditional, independent

<div class="meta"><span class="hot">In 4 of the last 4 exams</span><span>0.3–0.5 points</span><span>25 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

You get a formula $p_{X,Y}(x,y)$ that is non-zero only on some **region** of the $(x,y)$ plane. Think of it as a **height** above that region. Three facts:

- The total volume under it is 1 (that is how you find $c$).
- The **marginal** $p_Y(y)$: stand at height $y$, walk across the region horizontally, and add up the heights you pass: $p_Y(y)=\int p(x,y)\,dx$ **along that slice**.
- The only hard part is **where the slice starts and ends**. Read it off a drawing. Always draw the region.

Move the slice and watch the marginal being traced:

<div class="widget" data-w="region" data-preset="0"></div>

## How to fight this section with the sheet

The exam gives a $p(x,y)$ on a region and says **"find $c$"**, **"marginal"**, **"conditional"**, **"independent"**, **"domain"** → you open **box 1A** on your A4 sheet. Four bullets = the four questions, and each bullet ends with a worked line showing the moves on past numbers. There is also a "Doing the double integral" strip: the general calculation for the $c$ question.

!!! sheet "Box 1A, exactly as it is printed on the sheet"
    **IF YOU SEE** a joint PDF/PMF $p(x,y)$ on a region + "find $c$" / "marginal" / "conditional" / "independent" / "domain"

    First draw the region on $x$–$y$ axes: **every integral below takes its limits from that picture**, never from the formula.

    - **"Find $c$"** → integrate $p$ over the whole region, set the result $=1$, solve for $c$.<br>
      **Limits in 4 moves.** (1) Choose the order $dx\,dy$ = inner $x$, outer $y$ (the other order works too). (2) Freeze the outer letter at one value. (3) Inner limits: "from where to where can the inner letter move now?" — they may contain the outer letter ($x$ from $0$ to $1-y$). (4) Outer limits: the full range of the frozen letter, always plain numbers ($y$ from $0$ to $1$). Rectangle → both limits are numbers, order free. Triangle/wedge → one limit is an expression in the other letter. Limits can be $\infty$ (Jun24): $e^{-\infty}=0$.<br>
      *Apr25:* $cx+1$ on the triangle $x,y\ge0$, $x+y\lt1$ — the whole integral is worked out below.
    - **"Marginal $p_X(x)$"** → integrate the OTHER letter away: $p_X(x)=\int p(x,y)\,dy$, inner limits as in move 3. Range of $x$ = the region's shadow on the $x$ axis; write it and "0 otherwise".<br>
      *Jun26:* $6x^2y$ on the square $0\le x,y\le1$: $p_X=\int_0^1 6x^2y\,dy=3x^2$ for $0\le x\le1$. Same way $p_Y=2y$.
    - **"Conditional $p(x\mid y)$"** → $p(x,y)$ divided by $p_Y(y)$; state the ranges ($y$ over its shadow, $x$ over the slice at that $y$).<br>
      *Apr24:* $p=2$ on $0\le y\le x\le1$: $p_Y=\int_y^1 2\,dx=2(1-y)$ → $p(x\mid y)=\frac1{1-y}$ for $y\le x\le1$.
    - **"Independent?"** → YES only if the region is a rectangle AND $p(x,y)=p_X(x)\cdot p_Y(y)$.<br>
      *Jun26:* square, and $3x^2\cdot2y=6x^2y$ → independent. A triangle region → never independent.

    **Doing the double integral** (the *Apr25* one above, step by step). $\int_0^1\!\int_0^{1-y}(cx+1)\,dx\,dy$:<br>
    **(a)** inner $dx$ first — treat $y$ as a plain number: $\int_0^{1-y}(cx+1)dx=\big[\frac{cx^2}{2}+x\big]_0^{1-y}=\frac{c(1-y)^2}{2}+(1-y)$. Top limit minus bottom; at the bottom every $x$ is 0. **The answer still holding $y$ is normal.**<br>
    **(b)** now in $y$ — expand first, $(1-y)^2=1-2y+y^2$: $\int_0^1(1-y)dy=\big[y-\frac{y^2}{2}\big]_0^1=\frac12$ · $\int_0^1\frac{(1-y)^2}{2}dy=\big[-\frac{(1-y)^3}{6}\big]_0^1=\frac16$ → total $\frac c6+\frac12=1$ → $c=3$.<br>
    Rules: $\int x^n dx=\frac{x^{n+1}}{n+1}$ · $\int k\,dx=kx$ · $\int(a-y)^n dy=-\frac{(a-y)^{n+1}}{n+1}$ · always top minus bottom · expand powers first.

One more sheet place: **box 1E** ("$E[x]$ = the weighted average of the outcomes", "Discrete = the values can be listed") for the multiple-choice words at the bottom of this page.

## 1 · April 2025 · 1c — find $c$ (the sheet works this one out for you)

!!! exam "Final exam Q3, 13 April 2025 · 1c · 0.3 p"
    Let $X$ and $Y$ be jointly continuous random variables with joint PDF given by:

    $$p_{X,Y}(x,y) = \begin{cases} cx + 1 & x, y \geq 0, x + y < 1 \\ 0 & \text{otherwise} \end{cases}$$

    **Note:** For the conditions $x, y \geq 0, x + y < 1$ to be satisfied, $x < 1 - y$ and $y < 1$, or equivalently $y < 1 - x$ and $x < 1$.

    ***Provide only the final answer. The workout will not be checked.***

    Find the constant $c$.

!!! sheet "In the cheat sheet: box 1A, bullet 1 + the 'Doing the double integral' strip"
    <div class="stepper" markdown>

    **Sheet step 1 · draw, then read the limits off the picture.**
    The sheet's first line: *"First draw the region … every integral below takes its limits from that picture."* $x,y\ge0$ and $x+y<1$ = the triangle under the diagonal. The exam's own note gives the sheet's move 3: inner $x$ from $0$ to $1-y$.

    ***

    **Sheet step 2 · the four moves.**
    *"(1) Choose the order $dx\,dy$ = inner $x$, outer $y$. (2) Freeze the outer letter. (3) Inner limits … may contain the outer letter ($x$ from $0$ to $1-y$). (4) Outer limits … plain numbers ($y$ from $0$ to $1$)."* Triangle → *"one limit is an expression in the other letter"* — exactly what we have.

    ***

    **Sheet step 3 · inner integral (the strip's line (a)).**
    $\int_0^{1-y}(cx+1)dx=\big[\frac{cx^2}{2}+x\big]_0^{1-y}=\frac{c(1-y)^2}{2}+(1-y)$. The sheet warns: *"The answer still holding $y$ is normal."*

    ***

    **Sheet step 4 · outer integral (the strip's line (b)).**
    *"expand first, $(1-y)^2=1-2y+y^2$"* → $\int_0^1(1-y)dy=\frac12$ and $\int_0^1\frac{(1-y)^2}{2}dy=\frac16$ → total $\frac c6+\frac12=1$ → $c=3$.

    ***

    **Sheet check · the box's own check.**
    The strip's rule is that the whole integral has to come out $=1$ — that equation is what gives $c$. If you cannot write "$\frac c6+\frac12=1$", you stopped mid-strip.

    </div>

!!! answer "Answer"
    $c=3$

## 2 · April 2024 · 1c — marginal + conditional, domains included

!!! exam "Final exam Q3, April 2024 · 1c · 0.3 p"
    Random variables $X$ and $Y$ have joint PDF

    $$p_{X,Y}(x,y) = \begin{cases} 2, & 0 \leq y \leq x \leq 1 \\ 0, & \text{otherwise} \end{cases}$$

    Find the marginal PDF of $Y$ ($p_Y(y)$), and the conditional PDF $p_{X|Y}(x|y)$. For both PDFs make sure to correctly indicate their domain.

    **Note: provide only the final answer. No passages will be checked.**

!!! sheet "In the cheat sheet: box 1A, bullets 3 and 4 (the *Apr24* lines run the same bullets on other numbers)"
    <div class="stepper" markdown>

    **Sheet step 1 · draw.**
    $0\le y\le x\le1$ = the triangle under the diagonal $y=x$ (first tab of the widget). Freeze $y$: walking right, the slice runs from the diagonal $x=y$ to $x=1$.

    ***

    **Sheet step 2 · marginal (bullet 3's example).**
    *"Apr24: $p=2$ on $0\le y\le x\le1$: $p_Y=\int_y^1 2\,dx=2(1-y)$."* The sheet hands you the answer. Domain: bullet 2 — *"write it and '0 otherwise'"* → $0\le y\le1$.

    ***

    **Sheet step 3 · conditional (bullet 4's rule + same example).**
    *"$p(x,y)$ divided by $p_Y(y)$; state the ranges ($y$ over its shadow, $x$ over the slice at that $y$)."* → $\frac{2}{2(1-y)}=\frac1{1-y}$ for $y\le x\le1$ (the slice), 0 otherwise.

    ***

    **Sheet check · the shape of the answer.**
    Bullet 3 says *"state the ranges ($y$ over its shadow, $x$ over the slice at that $y$)"* — your pair must carry **both** ranges whatever the numbers are, and that is where points get lost.

    </div>

!!! answer "Answer"
    $p_Y(y)=2(1-y)$ for $0\le y\le1$ (0 otherwise); $\;p_{X\mid Y}(x\mid y)=\dfrac{1}{1-y}$ for $y\le x\le1$ (0 otherwise).

## 3 · June 2026 · 1c — marginal + independence on a square

!!! exam "Resit Q4, June 2026 · 1c · 0.5 p"
    Let $X$ and $Y$ be jointly continuous random variables with a joint Probability Density Function (PDF) given by:

    $$p_{X,Y}(x, y) = \begin{cases} 6x^2y, & 0 \leq x \leq 1 \text{ and } 0 \leq y \leq 1 \\ 0, & \text{otherwise} \end{cases}$$

    **Please provide only the final answer. The workout will not be checked.**

    1. Find the marginal PDF $p_X(x)$ and indicate its domain. [0.25]
    2. Determine whether $X$ and $Y$ are independent, and briefly justify why. [0.25]

!!! sheet "In the cheat sheet: box 1A, bullets 3 and 5 (the *Jun26* lines run the same bullets)"
    <div class="stepper" markdown>

    **Sheet step 1 · the region.**
    $0\le x,y\le1$ = the unit square (third tab of the widget). The sheet's move 4: *"Rectangle → both limits are numbers, order free"* → every slice is 0 to 1.

    ***

    **Sheet step 2 · marginal (bullet 3's example).**
    *"Jun26: $6x^2y$ on the square: $p_X=\int_0^1 6x^2y\,dy=3x^2$ for $0\le x\le1$."* The sheet hands you $3x^2$. (If they ask $p_Y$: *"Same way $p_Y=2y$."*) Domain from bullet 2: the shadow, $0\le x\le1$, "0 otherwise".

    ***

    **Sheet step 3 · independence (bullet 5's example).**
    *"YES only if the region is a rectangle AND $p(x,y)=p_X(x)\cdot p_Y(y)$ … Jun26: square, and $3x^2\cdot2y=6x^2y$ → independent."* Both conditions printed → **independent**, and the justification is the multiplication $3x^2\cdot 2y=6x^2y$ on a rectangle.

    ***

    **Sheet check · the box's two conditions.**
    Bullet 5: *"YES only if the region is a rectangle AND $p(x,y)=p_X(x)\cdot p_Y(y)$"* — test both, in that order. The rectangle test alone already kills every triangle region.

    </div>

!!! answer "Answer"
    1. $p_X(x)=3x^2$ for $0\le x\le1$, 0 otherwise. 2. **Independent**: the support is a rectangle and $p_{X,Y}=p_X\,p_Y=3x^2\cdot2y$.

## 4 · June 2024 · 1c — $c$ with limits at infinity (MC)

!!! exam "Resit June 2024 · 1c · 0.25 p"
    Random variables have joint PDF given by:

    $$p_{X,Y}(x, y) = ce^{-x}e^{-y},$$

    for $0 \leq y \leq x < \infty$.

    What is the correct values for the normalization constant $c$?

    a) 1  b) 4  c) 1/2  d) 2

!!! sheet "In the cheat sheet: box 1A, bullet 1 — the $\infty$ line and the same four moves"
    <div class="stepper" markdown>

    **Sheet step 1 · draw, freeze $x$.**
    $0\le y\le x<\infty$: the wedge below the diagonal, open to the right. Move 3: inner $y$ from $0$ to $x$ (an expression in the outer letter — *"Triangle/wedge → one limit is an expression in the other letter"*). Move 4: outer $x$ from $0$ to $\infty$.

    ***

    **Sheet step 2 · inner.**
    $\int_0^x e^{-y}dy=1-e^{-x}$ (top minus bottom; the sheet's rule *"always top minus bottom"*).

    ***

    **Sheet step 3 · outer, with the sheet's infinity line.**
    *"Limits can be $\infty$ (Jun24): $e^{-\infty}=0$."* $\int_0^\infty e^{-x}(1-e^{-x})dx=\int_0^\infty e^{-x}dx-\int_0^\infty e^{-2x}dx=1-\frac12=\frac12$. (The $e^{-\infty}=0$ is what makes both terms plain numbers.)

    ***

    **Sheet step 4 · solve.**
    $c\cdot\frac12=1$ → $c=2$ → **(d)**.

    </div>

!!! answer "Answer"
    **(d) $c=2$**

## 5 · November 2022 · 1b — marginal from a table (sum, don't integrate)

!!! exam "Final exam Q1, 7 November 2022 · 1b · 0.25 p"
    Consider two random variables $X$ and $Y$ with joint PMF $p_{X,Y}(x,y)$ given by the following table. What is the marginal PMF of $X$?

    |         | $Y = 0$ | $Y = 1$ | $Y = 2$ |
    |---------|---------|---------|---------|
    | $X = 0$ | 1/6     | 1/4     | 1/8     |
    | $X = 1$ | 1/8     | 1/6     | 1/6     |

    - (a) $p_X(0)=7/24$, $p_X(1)=5/24$, 0 otherwise
    - (b) $p_X(0)=13/24$, $p_X(1)=11/24$, 0 otherwise
    - (c) $p_X(0)=13/24$, $p_X(1)=5/24$, $p_X(2)=11/24$, 0 otherwise
    - (d) $p_X(0)=7/24$, $p_X(1)=5/12$, $p_X(2)=7/24$, 0 otherwise

!!! sheet "In the cheat sheet: box 1A, bullet 3 — same rule, table version"
    <div class="stepper" markdown>

    **Sheet step 1 · the rule.**
    *"Marginal $p_X(x)$ → integrate the OTHER letter away."* With a table there is nothing to integrate: **sum** the other letter away = add each **row** across. (Box 1E: *"Discrete = the values can be listed"* — a table is the discrete twin of a joint PDF.)

    ***

    **Sheet step 2 · common denominator, then row sums.**
    $\frac16=\frac4{24}$, $\frac14=\frac6{24}$, $\frac18=\frac3{24}$. Row $X=0$: $\frac{4+6+3}{24}=\frac{13}{24}$. Row $X=1$: $\frac{3+4+4}{24}=\frac{11}{24}$. Check: $13+11=24$ ✓ (box 1A's normalisation: the whole thing adds to 1).

    ***

    **Sheet step 3 · kill the impossible options.**
    The table has only $X=0$ and $X=1$ — the marginal's domain is those two values ("0 otherwise"). (c) and (d) invent $X=2$ → out. (a)'s fractions don't sum to 1 ($\frac{7+5}{24}=\frac12$) → out.

    </div>

!!! answer "Answer"
    **(b)** $p_X(0)=13/24$, $p_X(1)=11/24$, 0 otherwise.

## 6 · The MC words (April 2025 · 1b and friends) — box 1E

!!! exam "Final exam, 13 April 2025 · 1b · 0.25 p (type)"
    Which statement about the expected value is true? (The expected value is … the weighted average of the values weighted by the PMF / the simple average of the PMF values / …)

!!! sheet "In the cheat sheet: box 1E, first bullet"
    <div class="stepper" markdown>

    **Sheet step 1 · the printed sentence.**
    *"$E[x]$ … = the **weighted average of the outcomes** (the probabilities are the weights) = the long-run mean."* → the option saying "weighted average of its values, weighted by the PMF" is true (Apr25-1b answer **(d)**).

    ***

    **Sheet step 2 · the printed traps.**
    *""Integral/sum of the pmf itself" $=1$, **not** $E$. "highest probability / most common" = the **mode**."* → "the simple average of the PMF values" is false; "most likely value" questions ask for the **mode**, not $E$.

    </div>

!!! answer "Answer"
    The weighted-average statement is true; "simple average of the PMF" is false. Variance: $\text{Var}(X)=E[X^2]-(E[X])^2$; independent $\Rightarrow$ zero covariance, but zero covariance $\not\Rightarrow$ independent.

## Traps

!!! trap key "Where points are lost (each one is a line of the sheet you skipped)"
    - **No drawing** → wrong limits. The sheet's first sentence: the limits come *"from that picture, never from the formula"*.
    - **Forgetting the domain.** Bullet 2: *"write it and '0 otherwise'"*. "Indicate its domain" is half the points (Apr24, Jun26).
    - Swapping the roles in the conditional: it is **joint / marginal of the GIVEN letter**, and the $x$-range is *"the slice at that $y$"* ($y\le x\le1$), not $0\le y\le1$.
    - Calling a triangle independent. Bullet 5: *"A triangle region → never independent"* — on a triangle, knowing $y$ changes the range of $x$.
    - Writing $\frac{c(1-y)^2}{2}+(1-y)$ and panicking because $y$ is still in it. The sheet: *"The answer still holding $y$ is normal."*
    - Forgetting to expand $(1-y)^2$ before integrating — the sheet's rule: *"expand powers first"*.
    - Treating a PMF table like a PDF (or vice versa): table = sum the row, formula on a region = integrate the slice. Same bullet, discrete twin.
    - Letting $\infty$ into an answer: the sheet's line *"Limits can be $\infty$ (Jun24): $e^{-\infty}=0$"* — the boundary term always kills the $e^{-\infty}$ piece.
