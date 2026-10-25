---
hide:
  - navigation
  - toc
---

<h1 class="noprint">A4 cheat sheet</h1>

<p class="noprint">You may bring <b>one A4, both sides, own notes</b>. This sheet fills both sides: Ctrl/Cmd + P → A4, margins minimal, untick "headers and footers", scale 100 %. Better still: copy it by hand — writing it is half the studying.</p>
<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## 1.1 · Bayes word problems (counts)
Use this when the question splits items into groups (machines, scanners, students, patients), gives a share or count per group and a rate inside each group, and asks for a probability. Counts or a table → this sheet. A pdf or density is given → not this (use 1.2 / 2.1). A survival formula $\Pr[T\ge t]$ → Ex 5.

Symbols: $k$ = group number (1, 2, 3…). share$_k$ = fraction of all items made by group $k$. items$_k$ = number of items group $k$ makes. bad$_k$ = number of bad items group $k$ makes. "Bad" = the event we count. $P(\cdot)$ = probability of the event inside.

**Recipe** (the bracket says why the step is legal)
1. **Total.** Counts given → total = sum of the counts. Only percentages → pretend total = 1000 (1 000 000 if a rate is tiny, like 0.0005). [The answer is a ratio, so any total gives the same answer.]
2. **items$_k$ = share$_k$ × total.** [share$_k$ is a fraction of all items, so it scales the total.]
3. **Pick "bad".** Bad = the event asked, or the event after "given / if / found to be / has passed / positive". Asked NOT pass with a pass rate given → bad rate = 1 − pass rate [not-pass is the complement of pass]. Asked pass → bad rate = pass rate, no subtraction.
4. **bad$_k$ = bad rate$_k$ × items$_k$.** [A group's bad items are its bad fraction of its own items.]
5. **Event with no "given":** $P(\text{bad})$ = (bad$_1$ + bad$_2$ + …) / total. [Items are mixed at random, so a random item is bad with probability (all bad) ÷ (all items). This is the law of total probability.]
6. **Event with a "given" condition:** $P(k\mid\text{bad})$ = bad$_k$ / (sum of all bad). [Given the condition, only that pile is left, so the denominator is the pile, not the total.]

**Exam phrase → step**
- "found to be defective", "given", "if … has passed", "tests positive", "that chose psychology" → step 6.
- "a randomly selected chip will be defective", "a car will pass", "probability of choosing Engineering" → step 5.
- "NOT pass", "fail" → step 3, bad rate = 1 − pass rate.
- "round to the nearest percent" → multiply by 100, round.
- "Pr[TB]" = $P(\text{ill}\mid+)$.

**Wording** (same meaning)
- defective, fail, NOT pass, positive, infected, ill, has TB, actually present = bad. pass, sufficient quality, good, healthy = good.
- ill = infected = has TB = actually present. healthy = not infected. "+" = positive.
- "false positive 3 %" = 3 % of healthy people test positive. "detects 95 % when present" = 95 % of ill people test positive. "99 % accurate" = 99 % of ill test positive and 99 % of healthy test negative, so 1 % of healthy test positive.
- "scans / paints N patients or cars", one image each = count N.

**Ex 1 · machines (jun26-1b, Q1 and Q2).** M1 makes 40 % of chips (2 % defective), M2 makes 35 % (4 %), M3 makes 25 % (5 %). Step 1: total = 1000 chips. Step 2: M1 makes $0.40 \times 1000 = 400$ chips, M2 makes $0.35 \times 1000 = 350$, M3 makes $0.25 \times 1000 = 250$; check $400+350+250 = 1000$. Step 3: "defective" is bad, and the bad rates 2 %, 4 %, 5 % are given directly. Step 4: defective from M1 = $0.02 \times 400 = 8$; from M2 = $0.04 \times 350 = 14$; from M3 = $0.05 \times 250 = 12.5$. Pile = $8+14+12.5 = 34.5$.
- Q1 "a randomly selected chip will be defective": no "given" → step 5: $P(D) = 34.5 / 1000 = 0.0345$ (answer 0.0345).
- Q2 "found to be defective, produced by M2": given → step 6: $P(M_2\mid D) = 14 / 34.5 = 0.406 \approx 0.41$. The denominator is the defective pile, since the chip is already known to be defective; 14 is the M2 part of that pile.

**Ex 2 · CT scanners (apr25-1a, NOT pass).** CT1, CT2, CT3 scan 18, 22, 15 patients; one image per patient, so images = 18, 22, 15 and total = $18+22+15 = 55$. Pass rates 85 %, 90 %, 66 %. Asked NOT pass → step 3: bad rates $1-0.85 = 0.15$, $1-0.90 = 0.10$, $1-0.66 = 0.34$.
Step 4: bad images from CT1 = $18 \times 0.15 = 2.7$; CT2 = $22 \times 0.10 = 2.2$; CT3 = $15 \times 0.34 = 5.1$. Pile = $2.7+2.2+5.1 = 10.0$.
- Q1 "one image will NOT pass", no "given" → step 5: $10.0 / 55 = 0.18$.
- Q2 "bad quality image comes from CT2", given bad → step 6: $2.2 / 10.0 = 0.22$.

**Ex 3 · screening (apr24-1b TB; pe21-1a virus).** Items = people. "Has TB if one tests positive": ill is wanted, positive is the given → step 6.
TB: rate 0.0005 is tiny, so total = 1 000 000 people. Ill = $0.0005 \times 10^6 = 500$; healthy = $999\,500$. Ill and positive = $0.99 \times 500 = 495$; healthy and positive (the 1 % wrong) = $0.01 \times 999\,500 = 9\,995$. Positive pile = $495 + 9\,995 = 10\,490$. $P(TB\mid+) = 495 / 10\,490 = 0.047$. The numerator is ill-and-positive; the denominator is all positives, because positive is given.
Virus (pe21): 1.8 % infected, detects 95 %, false positive 3 %, total 1000. Infected = $0.018 \times 1000 = 18$; not infected = 982. Infected and positive = $0.95 \times 18 = 17.1$. Not infected and positive = $0.03 \times 982 = 29.46$. Positive pile = $17.1+29.46 = 46.56$. $P(\text{infected}\mid+) = 17.1 / 46.56 = 0.367$, so 37 % → option (b).

**Ex 4 · table (jan25-1a).** Items = students; total = all 8 cells = $45+27+8+10+22+42+20+26 = 200$.
- Q1 "given psychology, the student is female": given pile = psychology column = $10+26 = 36$ (male 10 + female 26). Wanted cell = female psychology = 26. $P = 26/36 = 0.722 \approx 0.72$.
- Q2 "probability of Engineering", no "given" → step 5: Engineering column = $45+22 = 67$; $67/200 = 0.335$.

**Ex 5 · lifetime (apr24-1a).** $T$ = lifetime in years, $t$ = time in years, $\Pr[T\ge t] = e^{-t/5}$ = probability still working at $t$. "Breaks in year 3, given working after 2" = $T$ between 2 and 3, given $T\ge 2$. Given $T\ge2$, the product either still works at 3 or breaks in year 3, and these add to 1, so $P(\text{breaks}) = 1 - P(T\ge3\mid T\ge2)$.
$P(T\ge3\mid T\ge2) = \Pr[T\ge3]/\Pr[T\ge2]$ [conditional probability; $T\ge3$ lies inside $T\ge2$, so the overlap is $T\ge3$] $= e^{-3/5}/e^{-2/5} = e^{-3/5+2/5} = e^{-1/5} = 0.8187$ [dividing powers of $e$ subtracts exponents; use a calculator]. Breaks in year 3 = $1 - 0.8187 = 0.18$ → (d).

**Ex 6 · experience (jan22-1a).** S = satisfactory 75 %; $S^c$ = not satisfactory 25 %. Experience E given S = 80 %. "No experience given $S^c$" = 15 %, so experience given $S^c$ = $1-0.15 = 0.85$ [complement]. Total 1000: S = 750, $S^c$ = 250. Experienced in S = $0.80 \times 750 = 600$; experienced in $S^c$ = $0.85 \times 250 = 212.5$. Experienced pile = $600+212.5 = 812.5$.
- "Hired with experience, unsatisfactory": given E → step 6: $P(S^c\mid E) = 212.5 / 812.5 = 0.26$ → (c).

**Ex 7 · total probability (nov22-1a; jan20-2).** Nov22: 65 % followed the course, so followed = $0.65 \times 1000 = 650$, not followed = 350. Pass rate followed 0.75 → $650 \times 0.75 = 487.5$ pass; not followed 0.40 → $350 \times 0.40 = 140$ pass. No "given" → step 5 with bad = pass: $P(\text{pass}) = (487.5+140)/1000 = 0.6275$ → (c) 0.63. Passing can happen through either group, so both piles are added.
Jan20-2 is the same with counts 30, 45, 25 cars (total 100): passing = $25.5+41.4+15 = 81.9$, so (a) $0.819$; (b) "passed, painted by M3" is given pass → $15/81.9 = 0.18$.

**Yes/no and "always true" statements**
- Independent ⇔ $P(A\mid B) = P(A)$ ⇔ $P(A\cap B) = P(A)P(B)$. So "$P(A\mid B)=P(A)$" is always true for independent events (jun26-1a: d). "$P(A\mid B)=P(B)$" is not.
- $P(A\cap B)=0$ means disjoint, not independent: if B happened, A cannot have, so they depend on each other.
- $P(A\cup B)=P(A)+P(B)$ only for disjoint events. "50 % here, 25 % on Mars, so 75 % here or Mars" is F: the events may overlap, and the sum then counts the overlap twice.
- Bayes theorem is F for "obtained from the total law and conditional probability": it follows from the definition of conditional probability alone; the total law only fills the denominator.
- Relative frequency → pmf $P(X=x)$ for discrete variables: T.
- CDF $F(x)=\Pr[X\le x]$ is 0 at $-\infty$ (nothing is ≤ −∞) and 1 at $\infty$ (everything is ≤ ∞): T.
- Wiener FIR one-step prediction gives an all-pole (AR) estimate, not a moving-average (MA) one: F.
- nov19-1b answer: A F, B F, C T, D T, E F.

## 1.2 · Joint PDF: $c$, marginal, conditional, independent

**Use this** when two variables $X,Y$ come with a joint function $p(x,y)$: a formula (continuous, integrate) or a table (discrete, add). A single variable's PDF belongs to 2.1. Plain counts per group are not this recipe.

Here $p(x,y)$ is the joint PDF (or PMF for a table), and "0 otherwise" means it is zero outside the given region. **First, draw the region where $p\ne0$** in the $(x,y)$ plane and read every limit from it.

**Recipe**

1. **Find $c$ (normalisation).** The total probability must be 1, because $X,Y$ take some value for sure. Integrate $p$ over the region: inner $\int dx$ from one edge of the region to the other (for fixed $y$), then outer $\int dy$ over the rest. Set the result $=1$ and solve for $c$.

2. **Marginal.** $p_X(x)=\int p(x,y)\,dy$: fix $x$ and integrate $y$ over all its values, because $Y$ may be anything and we only ask about $X$. Likewise $p_Y(y)=\int p\,dx$. Write the domain where it is non-zero, and "0 otherwise". For a PMF table, $p_X(x)$ is the **sum of the row** $X=x$ over all $Y$ columns, same reason with sums.

3. **Conditional.** $p_{X\mid Y}(x\mid y)=\dfrac{p(x,y)}{p_Y(y)}$, where $p_Y(y)$ is the marginal of $Y$. Fixing $Y=y$ keeps one slice of the joint; dividing by the slice's total mass $p_Y(y)$ rescales it so it integrates to 1 in $x$. Domain: the $x$-values of the slice, and the $y$ with $p_Y(y)>0$.

4. **Independent** iff (a) the region is a **rectangle** (the $x$-limits do not depend on $y$) and (b) $p(x,y)=p_X(x)\,p_Y(y)$ at every point. Multiply the two marginals and compare with $p$. Fail either → dependent. Rectangle matters because if the limits depend on $y$, knowing $Y$ restricts $X$.

Integrals: $\int_a^b x^n dx=\frac{b^{n+1}-a^{n+1}}{n+1}$, $\int_a^\infty e^{-kx}dx=\frac{e^{-ka}}{k}$.

**Worked examples, one per type**

Exam says "find the constant $c$" → step 1. *apr25-1c:* $p=cx+1$ on $x,y\ge0$, $x+y<1$. The region is a triangle. For fixed $y\in[0,1)$, $x$ runs from 0 to $1-y$, because $x<1-y$. Inner integral: $\int_0^{1-y}(cx+1)\,dx=c\frac{(1-y)^2}{2}+(1-y)$. Outer: $\int_0^1\frac{(1-y)^2}{2}dy=\frac16$ and $\int_0^1(1-y)dy=\frac12$, so the total is $\frac c6+\frac12$. Set it to 1: $\frac c6=\frac12$, so $c=3$. This is the answer to "find c".

Exam says "normalization constant" → step 1. *jun24-1c:* $ce^{-x}e^{-y}$ for $0\le y\le x<\infty$. Here $x$ runs from $y$ to $\infty$ (inner), $y$ from 0 to $\infty$. Inner: $\int_y^\infty e^{-x}dx=e^{-y}$ ($k=1$, $a=y$). Times the $e^{-y}$ still in $p$: $e^{-2y}$. Outer: $\int_0^\infty e^{-2y}dy=\frac12$ ($k=2$, $a=0$). So $c\cdot\frac12=1$, $c=2$ → answer (d).

Exam says "marginal PDF, indicate its domain" → step 2; "justify independence" → step 4. *jun26-1c:* $p=6x^2y$ on $0\le x\le1$, $0\le y\le1$. For fixed $x$, $y$ runs over $[0,1]$: $p_X(x)=\int_0^1 6x^2y\,dy=6x^2\cdot\frac{1}{2}=3x^2$, domain $0\le x\le1$. Independence: the region is the square $[0,1]^2$, a rectangle. Also $p_Y(y)=\int_0^1 6x^2y\,dx=6y\cdot\frac13=2y$. Then $p_X p_Y=3x^2\cdot2y=6x^2y=p$ everywhere → **independent**. Write this product line as the justification.

Exam says "marginal PMF of X" from a table → step 2. *nov22-1b:* row $X=0$ holds $\frac16,\frac14,\frac18$. Add them, in 24ths: $\frac{4}{24}+\frac{6}{24}+\frac{3}{24}=\frac{13}{24}$. Row $X=1$: $\frac{3}{24}+\frac{4}{24}+\frac{4}{24}=\frac{11}{24}$. Check: $\frac{13}{24}+\frac{11}{24}=1$. Answer (b). The others have wrong values or an extra $p_X(2)$, which a 2-row table cannot have.

Exam says "conditional PDF, domain" → steps 2 then 3. *apr24-1c:* $p=2$ on $0\le y\le x\le1$. For fixed $y$, $x$ runs from $y$ to 1, so $p_Y(y)=\int_y^1 2\,dx=2(1-y)$ for $0\le y\le1$. Check: $\int_0^1 2(1-y)dy=1$. Then $p_{X\mid Y}(x\mid y)=\frac{2}{2(1-y)}=\frac{1}{1-y}$ for $y\le x\le1$. Check: $\int_y^1\frac{dx}{1-y}=1$. Domain also needs $y<1$, since $p_Y(1)=0$ cannot divide.

Exam says "discrete or continuous?" → concept. **Counted** (integers: applicants, number of 4s, days without accidents, a phone number as a label) → discrete. **Measured** (time, distance, weight, an average amount of money) → continuous. *jun24-1b:* applicants = discrete; distance driven = continuous.

Exam says "expected value" → concept. $E[X]=\sum_x x\,p(x)$: each value $x$ is weighted by its probability $p(x)$ and summed. That is the **weighted average**, i.e. the mean over infinitely many observations. Not the highest-probability value, not the most common, not the largest, not the simple or geometric average. Answers: apr25-1b (d) weighted average; jan20-1d (B) mean over infinitely many observations.

Exam says "exactly 6 of 8" → binomial. *pe21-1b:* $n=8$ throws, $k=6$ hits, each hit with $p=0.8$. Patterns with 6 hits: $\binom{8}{6}=28$ (choose which 6 throws hit). One pattern has probability $0.8^6\cdot0.2^2=0.262144\cdot0.04=0.01048576$. Total: $28\times0.01048576=0.29360128\approx0.2936$ → (d).

Exam says "which contour plot is NOT possible" → Gaussian. *jan25-1b:* diagonal covariance means $\operatorname{Cov}(X,Y)=0$, so contours are circles or ellipses with axes along $x$ and $y$. A **tilted** ellipse (axes not along $x,y$) needs $\operatorname{Cov}\ne0$ → it is the one NOT possible → C.

Exam says "random process / random signal" → concept. *jan22-1b:* colours are integers 0–255, so a pixel is discrete. One picture is one realization (one outcome) of the process, so a random signal. The whole family of pictures is the random process. (a) is wrong (discrete), (d) puts the process on a pixel instead of the pictures → answer (b).

## 1.3 · WSS and ergodic
Words: $X(t)$ = random process, a family of signals. One fixed signal (one draw of the randomness) is a realization. $E[\cdot]$ = average over the random part ($U$, $A$, or the die roll), with $t$ kept fixed. $r[\tau]$ = autocorrelation at lag $\tau$ (correlation of the signal with a copy of itself shifted by $\tau$ steps). "auto-correlation" and "autocorr" mean the same.

**Exam phrase → step**: "wide-sense stationary" / "WSS" → A. "ergodic in the mean", "ergodic (mean)" or plain "ergodic" → B. "ergodic in both mean and variance" → pick that option (key answer in the exam set). "legitimate auto-correlation" → D. "cross-correlation $r_{xy}[\tau]$" → E. A pdf given and asked for mean or variance → 1.2 / 2.1, not here.

**A. WSS.** Do steps 1 and 2 for each process. Both must pass.
1. Compute the mean $E[X(t)]$. If $t$ is still in the answer → not WSS and not ergodic. Otherwise the mean is a constant. (Why: WSS needs a constant mean.)
2. Compute $E[X(t)X(t+\tau)]$, the correlation between times $t$ and $t+\tau$. If $t$ is still there → not WSS. If only $\tau$ is left → WSS yes. (Why: the correlation must depend only on the shift, not on the starting time.)
Not the WSS test: "PDF constant over time" (that is strict stationarity) and "PSD constant" are distractors.

**B. Ergodic in the mean.** Only if A.1 gave a constant mean. If not, answer "not ergodic" at once.
1. Fix ONE draw ($U$, $A$, or one die). Average that single signal over time $t$.
2. If this time average equals $E[X]$ for every draw → ergodic yes. If it differs from draw to draw → not ergodic. (Why: one long signal then reveals the ensemble mean.)
Options that give a mean value plus "ergodic / not ergodic": check the mean value first, then the word.

**C. Worked examples, one per type.**

*Type 1, "WSS and ergodic in the mean", $X(t)=\cos(t+U)$, $U\sim$ Uniform$(0,2\pi)$ (apr24, process 1).* $U$ is a random phase, any angle between 0 and $2\pi$ equally likely.
- Step A.1: over one full cosine cycle the positive halves cancel the negative halves, so $E[X(t)]=0$. No $t$ left → constant mean 0.
- Step A.2: the question gives $\cos\alpha\cos\beta=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2$. Put $\alpha=t+U$ and $\beta=t+\tau+U$. Then $\alpha-\beta=-\tau$ and $\alpha+\beta=2t+\tau+2U$. So $r[\tau]=\frac12\cos\tau+\frac12\cos(2t+\tau+2U)$. The first term has no random part. The second averages to 0 over $U$ (one full cycle). So $r[\tau]=\frac12\cos\tau$, no $t$ → WSS **yes**.
- Step B: one fixed $U$ gives $\cos(t+U)$, whose time average is 0 for every $U$, equal to the mean 0 → ergodic **yes**.
- Table row 1: WSS Yes, Ergodic Yes.

*Type 2, $X(t)=A\cos t$, $A\sim\mathcal N(1,2)$ (apr24, process 2; first number = mean).* For a fixed $t$, $\cos t$ is just a number, so $E[A\cos t]=E[A]\cos t=1\cdot\cos t=\cos t$. It still has $t$ → WSS **no**. Mean not constant → ergodic **no**. Table row 2: No, No.

*Type 3, "samples randomly with equal probability between $-A$ and $A$", $A\sim\mathcal N(1,2)$ (nov22).* For every $A$, the midpoint of $[-A,A]$ is $(-A+A)/2=0$, so the mean is the constant 0. Each realization's time average is that midpoint, 0, for every $A$ → ergodic yes, mean 0. The mean 1 of $A$ is a trap: it does not move the midpoint. Key answer: option (d).

*Type 4, fair dice (apr25, jan22).* Mean of one die: $(1+2+3+4+5+6)/6=21/6=3.5$, not 0. So any option saying "$E=0$" is false. Each die's long-run average over its rolls is also 3.5, the same as the mean → ergodic in the mean. Key answer: option "ergodic in both mean and variance" (apr25 (b), jan22 (b)).

*Type 5, definition check (jun26).* WSS = constant mean and autocorrelation depending only on the lag. Key answer (b). Option (a) describes ergodicity, not WSS; (c) is a PDF condition; (d) is a PSD condition.

**D. Legitimate autocorrelation (plot of $r$).** Keep a plot $r$ only if both hold:
1. Symmetric: $r[l]=r[-l]$ for every lag $l$. (Why: correlating $x$ with its shift forward or backward gives the same value.)
2. $r[0]\ge|r[l]|$ for every lag. (Why: $r[0]$ is the average of $x^2$, the largest possible correlation.)
Pick the option that lists exactly the kept plots. jan20 key: option A (only $r_B$). The figure values are not in this sheet; check the mirror image and the peak at lag 0 by eye.

**E. Cross-correlation** (nov19):

$$r_{xy}[\tau]=\frac1N\sum_n x[n]\,y[n+\tau]$$

Here $N$ = number of samples in the window, $n$ = sample index, $\tau$ = lag.
1. Shift $\tau$: pair $x[n]$ with $y[n+\tau]$. Keep only pairs where both samples exist. (Why: $y$ is only known inside the window.)
2. Multiply each pair, keeping signs, and add the products.
3. Divide by $N$, even if fewer pairs were kept. (Why: the formula divides by $N$.)

Worked example: $x=[1,1,1,0]$, $y=[1,3,3,5]$, $N=4$.
- $\tau=0$: pairs (1,1), (1,3), (1,3), (0,5). Products 1, 3, 3, 0. Sum 7. Divide by 4 → $r_{xy}[0]=7/4$.
- $\tau=1$: $x[0]$ with $y[1]=3$, $x[1]$ with $y[2]=3$, $x[2]$ with $y[3]=5$; $x[3]$ has no $y[4]$, so it is dropped. Products 3, 3, 5. Sum 11. Divide by 4 → $r_{xy}[1]=11/4$.

Rule: compute $\tau=0$ first and drop options whose value differs. If no option matches exactly, take the nearest and say so. nov19 key: option B (its values match the computed ones only up to a shift of 3 lags, so no option is exact).

## 1.4 · Spectral factorisation

**Use this recipe** when the power spectrum $P(e^{j\theta})$ is a ratio of cosine expressions (no time-domain pdf is given; a pdf given means 1.2 / 2.1 instead). Goal: the innovation filter $L(z)$ and the input noise variance $\sigma_i^2$, so that $x[n]$ is what you get when white noise of variance $\sigma_i^2$ goes through $L$.

**Names:** $\theta$ = frequency angle in radians; $z=e^{j\theta}$ = point on the unit circle; $z^{-1}$ = one-sample delay; $N,M$ = constants of the top, $A,B$ = constants of the bottom; $p,q$ = generic constants of one cosine factor; $r$ = a root; $a,b$ = filter coefficients; $C,D$ = scaling constants; $\sigma_i^2$ = noise variance; $L$ = causal filter.

**Tool and why it works:** $p+q\cos\theta=\frac{q}{2r}(1+rz^{-1})(1+rz)$, because $(1+rz^{-1})(1+rz)=r\,(r+\frac1r+2\cos\theta)$ and $r+\frac1r=\frac{2p}{q}$. Roots: $r=\frac{p\pm\sqrt{p^2-q^2}}{q}$ (two of them, $r$ and $1/r$). **Keep $|r|<1$**: then $(1+rz^{-1})$ has its zero inside the unit circle, which makes $L$ causal and minimum phase.

**Recipe**
1. Bottom $A+B\cos\theta$: take $p=A$, $q=B$, keep the root with $|a|<1$ as $a$. Then $C=\frac{q}{2a}$. Why: by the tool, the bottom equals $C(1+az^{-1})(1+az)$.
2. Top $N+M\cos\theta$: same with $p=N$, $q=M$, giving $b$ and $D$. If $M=0$ there is no cosine to factor: no $b$, and $D=N$.
3. So $P=\frac DC\cdot\frac{(1+bz^{-1})(1+bz)}{(1+az^{-1})(1+az)}$. Keep only the $z^{-1}$ parts for $L$, because $L$ must be causal (the $z$ parts are the mirror image, not causal). Why $\sigma_i^2=\frac DC$: white noise of variance $\sigma_i^2$ filtered by $L$ gives $\sigma_i^2|L|^2$, so the constant in front is the variance.
4. Answer: $\sigma_i^2=\frac DC$ and $L(z)=\frac{1+bz^{-1}}{1+az^{-1}}$ (if $M=0$: $L=\frac{1}{1+az^{-1}}$).

**Self-check:** put $z=1$ ($\theta=0$). Then $P(0)=\sigma_i^2L(1)^2$. Use it to kill wrong options.

**Exam phrasing -> step**
- "find the spectral factorisation, $L(z)$ and $\sigma_i^2$" -> steps 1-4.
- "which of the following is the spectral factorisation?" -> run steps 1-4 once, match the option; reject any option with the outside-circle root in $L$.
- "which statement is true?" with a factorisation printed -> example C (test it).
- "which condition must the innovation filter satisfy?" -> minimum phase: all poles and zeros inside the unit circle (not maximum phase, not all-pass).

**Example A** ("find the spectral factorisation", April 2024, $P=\frac{7}{25-24\cos\theta}$, no cosine on top)
Bottom: $A=25$, $B=-24$, so $p=25$, $q=-24$. The square root is $\sqrt{625-576}=\sqrt{49}=7$. The two roots are $\frac{25+7}{-24}=-\frac43$ and $\frac{25-7}{-24}=-\frac34$. Only $-\frac34$ has $|r|<1$, so $a=-\frac34$ and $C=\frac{-24}{2(-3/4)}=\frac{-24}{-3/2}=16$.
Top: no cosine, so $D=N=7$ and no $b$.
Answer: $\sigma_i^2=\frac{7}{16}$ and $L(z)=\frac{1}{1-\frac34z^{-1}}$ (since $1+az^{-1}$ with $a=-\frac34$ is $1-\frac34z^{-1}$). Check: $P(0)=7$, and $\frac{7}{16}\cdot\frac{1}{(1/4)^2}=7$. ✓ The two requested items are the two lines above.

**Example B** (January 2024, MC, $P=\frac{10+6\cos\theta}{17-8\cos\theta}$, options (a)-(d))
Bottom: $p=17$, $q=-8$, $\sqrt{289-64}=15$, roots $\frac{17+15}{-8}=-4$ and $\frac{17-15}{-8}=-\frac14$. Keep $a=-\frac14$; $C=\frac{-8}{2(-1/4)}=16$.
Top: $p=10$, $q=6$, $\sqrt{100-36}=8$, roots $\frac{18}{6}=3$ and $\frac{2}{6}=\frac13$. Keep $b=\frac13$; $D=\frac{6}{2\cdot\frac13}=9$.
Answer: $\sigma_i^2=\frac{9}{16}$, $L=\frac{1+\frac13z^{-1}}{1-\frac14z^{-1}}$ = option **(c)**. Options (a), (b), (d) put the outside-circle root $3$ or $-4$ into $L$, so they are not minimum phase. Check: $P(0)=\frac{16}{9}$; $\frac{9}{16}\cdot\left(\frac{4/3}{3/4}\right)^2=\frac{9}{16}\cdot\frac{256}{81}=\frac{16}{9}$. ✓

**Example C** (January 2022, MC, $P=\frac{17/8-\cos\theta}{25/16-\frac32\cos\theta}$; printed claim $2\frac{(1-\frac14z^{-1})(1-\frac14z)}{(1+\frac34z^{-1})(1+\frac34z)}$; which statement is true?)
Do not trust the printed factorisation: test it at $z=1$. True value: numerator $\frac98$, denominator $\frac{25}{16}-\frac{24}{16}=\frac1{16}$, so $P(0)=18$. Printed claim at $z=1$: $2\cdot\frac{(3/4)^2}{(7/4)^2}=\frac{18}{49}\approx0.37\neq18$. So the printed factorisation is not $P$: statement **(a)** is true. Running the recipe on the real $P$ gives $L=\frac{1-\frac14z^{-1}}{1-\frac34z^{-1}}$ and $\sigma_i^2=2$. The official key marks (c), which needs $+\frac34$ in the denominator, i.e. a bottom with $+\frac32\cos\theta$; the question has $-\frac32\cos\theta$, so (c) is not derivable from the question as printed.

## 2.1 · Maximum likelihood (MLE)

**Use this recipe** when a pdf $p(x\mid\theta)$ of the data is given and the question asks for the estimate $\hat\theta$. Exam phrasings: "derive the MLE", "determine the maximum likelihood estimate", "find an estimator for $\theta$", "find the maximum likelihood estimator for $\lambda$". **Not this one**: if a prior or a posterior $p(\theta\mid x)$ appears, that is MAP (see MC below); if the question asks for a least-squares fit, that is not MLE.

**Symbols.** $\theta$ = the unknown parameter we estimate. $\hat\theta$ ("theta hat") = our estimate. $x_n$ = the $n$-th observed sample, $n=1,\dots,N$. $N$ = number of samples. $\ln$ = natural log. $L$ = likelihood = joint pdf of all samples, read as a function of $\theta$. $\sum$ = add over all samples. $\bar x=\frac1N\sum x_n$ = sample mean. $\arg\max_\theta f$ = the $\theta$ where $f$ peaks (not the peak height).

**Recipe**

1. Likelihood and log-likelihood. $L=\prod_{n=1}^N p(x_n\mid\theta)$: samples are independent, so the joint density is the product of single densities. $\ln L=\sum_n\ln p(x_n\mid\theta)$: ln is increasing, so the $\theta$ that maximises $L$ also maximises $\ln L$, and sums are easier to differentiate. Log rules: $\ln(ab)=\ln a+\ln b$, $\ln\frac ab=\ln a-\ln b$, $\ln x^k=k\ln x$, $\ln e^u=u$.
2. Differentiate $\ln L$ with respect to $\theta$. Only $\theta$ varies, so a term without $\theta$ (e.g. $\ln x$) is a constant with derivative 0. Rules: $\ln\theta\to\frac1\theta$; $\frac c\theta\to-\frac c{\theta^2}$; $\frac c{\theta^2}\to-\frac{2c}{\theta^3}$; $c\theta\to c$. A term without $n$ appears in all $N$ terms of the sum, so it counts $N$ times.
3. Set the derivative to 0: a maximum of a smooth curve is where its slope is zero. Multiply by $\theta^2$ (or $\theta^3$) to clear fractions; legal because $\theta>0$. Solve for $\hat\theta$. If you get $\theta^2=s$, take $\hat\theta=\sqrt s$ (positive root, since $\theta>0$).

**Unknown squared (e.g. $\rho$).** Exponent $-a\rho^2+b\rho$ → derivative $-2a\rho+b=0$ → $\rho=\frac b{2a}$. A common factor multiplies every term, so it does not move the zero: drop it.

**Worked examples** (each line says what the number is)

**A. Gamma with known $k$ (jun26-2b).** "Write the likelihood and log-likelihood" → step 1 only. "Derive the MLE for $\theta$" → steps 1–3. "Explain what the MLE tells us" → last paragraph. Here $x_i$ = recovery days of patient $i$, $n$ patients, $k$ = known number of stages, $\theta$ = unknown average time per stage.

1. Each patient's factor has $\theta^{-k}$; $n$ patients give $\theta^{-nk}$. $\ln L=\sum_i(k-1)\ln x_i-nk\ln\theta-\frac{\sum_i x_i}{\theta}-n\ln\Gamma(k)$. The first and last terms have no $\theta$.
2. $\frac{d\ln L}{d\theta}=-\frac{nk}\theta+\frac{\sum_i x_i}{\theta^2}$ ($-nk\ln\theta$ gives $-\frac{nk}\theta$; $-\frac{\sum x_i}\theta$ gives $+\frac{\sum x_i}{\theta^2}$).
3. Times $\theta^2$: $-nk\theta+\sum x_i=0$, so $\hat\theta=\frac{\sum x_i}{nk}=\frac{\bar x}k$.

Meaning: $\hat\theta=\bar x/k$ is the estimated average time per stage. The Gamma mean is $k\theta$, so $k\hat\theta=\bar x$: the fitted mean recovery equals the observed mean. Made-up check: $n=3$ patients take 4, 6, 8 days, $k=2$: $\sum x=18$, $nk=6$, $\hat\theta=18/6=3$ days per stage; $k\hat\theta=6=\bar x=18/3$ ✓.

**B. Exponential, find $\lambda$ from $N$ observations (jan19-2a).** $p=\lambda e^{-\lambda x}$, $\lambda$ = rate.

1. $\prod_n\lambda e^{-\lambda x_n}=\lambda^N e^{-\lambda\sum x_n}$ ($\lambda$ appears once per sample, so $N$ times). $\ln L=N\ln\lambda-\lambda\sum x_n$.
2. $\frac{d\ln L}{d\lambda}=\frac N\lambda-\sum x_n$.
3. $\frac N\lambda=\sum x_n$, so $\hat\lambda=\frac N{\sum x_n}=\frac1{\bar x}$ — the answer to "find the MLE for $\lambda$".

**C. Scale in prefactor and exponent (apr24-2c; pe21-2b has $\frac x\theta$ prefactor, same answer).** "Derive the MLE for $\theta$" → 1–3. Here $p(x_n\mid\theta)=\frac{x_n}{2\theta}e^{-x_n^2/(2\theta)}$.

1. $\ln p=\ln x_n-\ln2-\ln\theta-\frac{x_n^2}{2\theta}$; $\ln x_n$ and $\ln 2$ are constants. Summing $-\ln\theta$ over $N$ samples gives $-N\ln\theta$.
2. $\frac{d\ln L}{d\theta}=-\frac N\theta+\frac{\sum x_n^2}{2\theta^2}$.
3. Times $\theta^2$: $-N\theta+\frac{\sum x_n^2}2=0$, so $\hat\theta=\frac{\sum x_n^2}{2N}$.

Variant q1-23-2b, exponent $-x^2/\theta$ (no 2): $-\frac N\theta+\frac{\sum x^2}{\theta^2}=0$ → $\hat\theta=\frac{\sum x^2}N$.

**D. Square root (nov19-3a).** $p=\frac x{\theta^2}e^{-x^2/(2\theta^2)}$; "find the MLE for $\theta$" → 1–3.

1. $\ln p=\ln x-2\ln\theta-\frac{x^2}{2\theta^2}$; summed over $N$: $-2N\ln\theta$.
2. $\frac{d\ln L}{d\theta}=-\frac{2N}\theta+\frac{\sum x_n^2}{\theta^3}$ (since $-\frac{x^2}2\theta^{-2}$ has derivative $+\frac{x^2}{\theta^3}$).
3. Times $\theta^3$: $-2N\theta^2+\sum x_n^2=0$, so $\hat\theta^2=\frac{\sum x_n^2}{2N}$, $\hat\theta=\sqrt{\frac{\sum x_n^2}{2N}}$.

**E. Unknown $\rho$, single observation (jan25-2b).** Here the $\theta$ inside the pdf is a *given* correlation number, not the parameter. $\mu,\sigma,\theta$ = observed data; $N=1$, so no sum.

1. The prefactor $\frac1{2\pi\sqrt{1-\theta^2}}$ does not contain $\rho$, so it is constant. Exponent: $\mu^2\rho^2+\sigma^2\rho^2=(\mu^2+\sigma^2)\rho^2$, so $\ln p=\text{const}-\frac{(\mu^2+\sigma^2)\rho^2-2\mu\sigma\theta\rho}{2(1-\theta^2)}$.
2. $\frac{d\ln p}{d\rho}=-\frac{2(\mu^2+\sigma^2)\rho-2\mu\sigma\theta}{2(1-\theta^2)}$.
3. The factor $-\frac1{2(1-\theta^2)}$ is nonzero (since $|\theta|<1$), so set the bracket to 0: $(\mu^2+\sigma^2)\rho=\mu\sigma\theta$, so $\hat\rho=\frac{\mu\sigma\theta}{\mu^2+\sigma^2}$.

**F. Angle (nov22-2d).** $\mathbf x=A(\cos\theta,\sin\theta)+\mathbf w$; $\theta$ = unknown angle, $A>0$ and $\sigma$ are known.

1. The pdf is $\exp(-S/2\sigma^2)$ with $S=(x_1-A\cos\theta)^2+(x_2-A\sin\theta)^2$. Maximising $\exp(-S/2\sigma^2)$ is the same as minimising $S$ (exp is increasing, and $-S$ flips min to max).
2. Expand: $S=x_1^2+x_2^2+A^2(\cos^2\theta+\sin^2\theta)-2A(x_1\cos\theta+x_2\sin\theta)$. $\cos^2+\sin^2=1$, so $A^2$ is constant. Minimising $S$ = maximising $x_1\cos\theta+x_2\sin\theta$.
3. Derivative: $-x_1\sin\theta+x_2\cos\theta=0$, so $\tan\theta=\frac{x_2}{x_1}$ and $\hat\theta=\tan^{-1}\frac{x_2}{x_1}$. Made-up check: $x_1=x_2=1$ → $\pi/4$. Caveat: $\tan^{-1}$ only gives angles in $(-\pi/2,\pi/2)$; if $x_1<0$, shift by $\pi$ so $(\cos\hat\theta,\sin\hat\theta)$ points the way $(x_1,x_2)$ does.

**G. Sigmoid (apr25-2c).** $\lambda(\theta)=\frac1{1+e^{-\theta}}$ is a number in $(0,1)$. Do NOT expand $\lambda(\theta)$: find $\hat\lambda$ first, then convert. $p=3\lambda e^{-4\lambda x/7}$, $x>1$.

1. $\ln p=\ln3+\ln\lambda-\frac{4x}7\lambda$.
2. $\frac{d\ln p}{d\lambda}=\frac1\lambda-\frac{4x}7$.
3. $\frac1{\hat\lambda}=\frac{4x}7$, so $\hat\lambda=\frac7{4x}$.
4. Sigmoid is one-to-one, so invert it: $1+e^{-\theta}=\frac1\lambda$ → $e^{-\theta}=\frac{1-\lambda}\lambda$ → $\hat\theta=\ln\frac{\hat\lambda}{1-\hat\lambda}$. With $\hat\lambda=\frac7{4x}$: $\frac{7/(4x)}{(4x-7)/(4x)}=\frac7{4x-7}$, so $\hat\theta=\ln\frac7{4x-7}=-\ln\left(\frac{4x}7-1\right)$.

Valid only for $x>\frac74$: otherwise $\hat\lambda\ge1$, and a sigmoid never reaches 1. Hint route (same answer): $\frac{d\ln p}{d\theta}=\left(\frac1\lambda-\frac{4x}7\right)\lambda(1-\lambda)$; $\lambda(1-\lambda)\neq0$, so drop it.

**MC (no algebra, pick the TRUE one)**

- jan22-2b, answer **(c)**: transform the parameter, solve for $\hat\alpha$, map back with $\psi^{-1}$. (a) is false: ML maximises over $\theta$, so the answer is a $\theta$ value, not $x$. (b) is false: for large $N$ the estimate is approximately Gaussian with mean $\theta$, not uniform.
- nov22-2b, answer **(c)**: ML is asymptotically unbiased (bias fades as $N$ grows). (a) is false: ML reaches the Cramér-Rao bound only for large $N$, not always. (b) is false: ML works for general non-linear problems too (often numerically).
- jan19-1b, answer **D**: $\arg\max_\theta p(x\mid\theta)$. A is least squares, B is minimum mean-squared error, C is MAP (uses a prior $p(\theta)$). ML uses no prior.

## 2.2 · MAP with a prior

Symbols: $\theta$ (or $\lambda$) is the unknown parameter. $x$ is the observed data. $L(\theta)$ is the likelihood, the probability of the data as a function of $\theta$. $p(\theta|x)$ is the posterior, the density of $\theta$ after seeing the data. Bayes' rule gives posterior $\propto$ likelihood $\times$ prior. The sign $\propto$ means "equal up to a constant that does not contain $\theta$". Such constants cannot move a peak, so MAP never needs them.

**Which estimator (match the exam words):**
- "MAP", "maximum a posteriori", "most probable": the peak of the posterior, $\hat\theta_{MAP}=\arg\max_\theta p(\theta|x)$. Needs a prior.
- "MMSE", "minimum mean square error", "posterior mean": the average of $\theta$ under the posterior, $\hat\theta_{MMSE}=\int\theta\,p(\theta|x)\,d\theta$.
- "MLE": the peak of $L$ alone, no prior.
- Bayes risk is the average cost. Squared-error cost gives MMSE. 0/1 or uniform cost gives MAP.

**Pick the recipe by what the question gives:**
- Beta or Gamma prior plus a standard PMF/pdf likelihood: recipe A.
- Posterior already written as $\theta^A(1-\theta)^B$ or $\lambda^Ae^{-B\lambda}$: skip to A-step 4 (MAP) or A-step 5 (MMSE).
- Posterior contains a function of $\theta$ (sigmoid, $e^{\theta}$) or a non-conjugate prior: recipe B.
- Binary $X=\pm1$ plus Gaussian noise: recipe C.
- Posterior is a sum of two bumps (mixture): recipe D.
- Flat prior on a bounded interval: recipe E.

**Recipe A: conjugate prior (Beta or Gamma)**

A Beta($\alpha,\beta$) prior has pdf $\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$. A Gamma($\alpha,\beta$) prior has pdf $\propto\lambda^{\alpha-1}e^{-\beta\lambda}$, where $\beta$ is a rate. Use the numbers the question gives.

1. Likelihood $L=\prod_i P(x_i|\theta)$. Multiply the probabilities of the $n$ observations because they are independent. Drop factors without $\theta$, such as $\binom{x-1}{k-1}$ or $1/x_i!$, because they do not move the peak. Add exponents of equal bases: $\theta^a\theta^b=\theta^{a+b}$.
2. Multiply by the prior, by Bayes' rule. Add the exponents again.
3. Name the posterior. $\theta^A(1-\theta)^B$ is Beta($A+1,B+1$). $\lambda^Ae^{-B\lambda}$ is Gamma(shape $A+1$, rate $B$). The $+1$ is there because a Beta($a,b$) pdf has exponents $a-1$ and $b-1$.
4. MAP. Beta type: $\hat\theta=\frac{A}{A+B}$, from setting the derivative of $A\ln\theta+B\ln(1-\theta)$ to zero. Gamma type: $\hat\lambda=\frac AB$, from $A/\lambda-B=0$.
5. MMSE = mean of the posterior. Beta type: $\frac{A+1}{A+B+2}$. Gamma type: $\frac{A+1}{B}$.
6. MLE: step 1 only, then the same peak formula with no prior exponents.

*Example, exam says "write the likelihood, derive the posterior, compute MAP" (jun26-2c).* Each patient's screening count has PMF $\theta^2(1-\theta)^{x-2}$, because the $k=2$ successes give $\theta^2$ and the $x-2$ failures give $(1-\theta)^{x-2}$. There are $n=5$ rounds with $x=3,5,4,6,4$, so $\sum x=3+5+4+6+4=22$.
- Step 1: the $\theta$ exponent is $2$ per round, so $2\times5=10$. The $(1-\theta)$ exponent is $\sum(x-2)=22-2\times5=12$. So $L\propto\theta^{10}(1-\theta)^{12}$. This answers "write the likelihood".
- Step 2: the prior Beta(2,3) is $\propto\theta^1(1-\theta)^2$. Multiplying gives $\theta^{10+1}(1-\theta)^{12+2}=\theta^{11}(1-\theta)^{14}$, so $A=11$, $B=14$.
- Step 3: posterior Beta($A+1,B+1$) = Beta(12,15). This answers "derive the posterior".
- Step 4: $\hat\theta_{MAP}=\frac{11}{11+14}=\frac{11}{25}=0.44$. This answers "compute MAP".

*Example, Poisson with Gamma prior (jun26-2d).* The Poisson PMF is $\lambda^xe^{-\lambda}/x!$, and $x!$ is dropped. There are $n=6$ days with $\sum x=2+4+3+5+2+4=20$. Each day contributes $\lambda^{x}$ and $e^{-\lambda}$, so six days give $e^{-6\lambda}$.
- Step 1: $L\propto\lambda^{20}e^{-6\lambda}$.
- Step 2: the Gamma($\alpha=3,\beta=2$) prior is $\propto\lambda^{2}e^{-2\lambda}$. The product is $\lambda^{22}e^{-8\lambda}$, so $A=22$, $B=8$.
- Step 3: posterior Gamma(shape 23, rate 8).
- Step 4: $\hat\lambda_{MAP}=\frac{22}{8}=2.75$.
- MLE (step 6): $\frac{20}{6}=3.33$. The prior mean is $\alpha/\beta=\frac32=1.5$.
- Exam says "compare with MLE and explain the effect of the prior": 2.75 lies between the prior mean 1.5 and the MLE 3.33. The prior pulls the estimate down. The prior adds only 2 to the $\lambda$ exponent and 2 to the rate, while the data add $\sum x=20$ and $n=6$. So with more data the prior fades and MAP approaches MLE.

**Recipe B: posterior with a function of $\theta$ (no conjugate form)**

*Example, exam says "derive the MAP for $\theta$" (apr24-2d).* The posterior is $\frac{\lambda}{2}e^{-\lambda x/2}$, where $\lambda=\frac1{1+e^{-\theta}}$ is the logistic sigmoid of $\theta$.
1. Take the log of the posterior, since $\ln$ is increasing and turns the product into a sum: $\ln p=\ln\lambda-\frac{\lambda x}{2}+\text{const}$.
2. Differentiate with the chain rule, using $\lambda'=\lambda(1-\lambda)$ from the hint: $\lambda'\left(\frac1\lambda-\frac x2\right)=0$.
3. $\lambda'>0$ always, because the sigmoid is strictly increasing, so it cannot be zero. Therefore $\frac1\lambda=\frac x2$, i.e. $\lambda=\frac2x$.
4. Invert the sigmoid. $\frac1{1+e^{-\theta}}=\frac2x$ gives $e^{-\theta}=\frac x2-1$, so $\hat\theta=-\ln\left(\frac x2-1\right)=\ln\frac{2}{x-2}$. This needs $x>2$, so that $\lambda=2/x$ lies in $(0,1)$.

*Example, exponential prior (nov22-2f; the same logic gives the MMSE in q3-23-2h).* The prior is $ae^{-a\theta}$ and the likelihood is $\theta e^{-\theta x}$ for one observation $x$.
- Steps 1–2: the product is $\theta e^{-(x+a)\theta}$, so $A=1$ and $B=x+a$.
- Step 3: with $A=1$ this is Gamma(shape 2, rate $B$). Normalised, the posterior is $(x+a)^2\theta e^{-(x+a)\theta}$.
- Step 4: MAP $=\frac AB=\frac1{x+a}$.
- Step 5: MMSE $=\frac{A+1}{B}=\frac2{x+a}$. This is the mean of Gamma(2, rate $B$). The integral hint in the exam is for this.
- Variant: if the likelihood is $\frac1xe^{-\theta x}$, then $A=0$, the posterior is $(x+a)e^{-(x+a)\theta}$, and MMSE $=\frac1{x+a}$.

*Example, MAP leads to an equation with no closed form (nov19-3c).* The likelihood of each observation is $\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}$, and the prior is $\lambda e^{-\lambda\theta}$. Let $S=\sum_n x_n^2$, which is a constant in $\theta$.
1. The product over $N$ observations gives $\theta^{-2N}e^{-S/(2\theta^2)}$. Multiplying by the prior gives $\theta^{-2N}e^{-S/(2\theta^2)-\lambda\theta}$.
2. The log is $-2N\ln\theta-\frac{S}{2\theta^2}-\lambda\theta$. Its derivative is $-\frac{2N}{\theta}+\frac{S}{\theta^3}-\lambda=0$.
3. Multiply by $\theta^3$: $\lambda\theta^3+2N\theta^2-S=0$. The MAP is the positive root of this cubic. The question accepts an implicit answer like this.

**Recipe C: $Y=X+N$ with $X=\pm1$ (jan22-2f)**

$X$ is $+1$ or $-1$ with probability $\frac12$ each. $N$ is zero-mean Gaussian noise with variance $\sigma^2$. We observe $y$.
1. For each value $s\in\{1,-1\}$, compute $w_s=e^{-(y-s)^2/(2\sigma^2)}$. This is large when $y$ is close to $s$. The Gaussian normalising constant is the same for both and cancels.
2. Posterior: $P[X=s|y]=\frac{w_s}{w_1+w_{-1}}$. Dividing by the sum makes the two probabilities add to 1, by the law of total probability over the two values of $X$.
3. Ratio: $(y-1)^2-(y+1)^2=-4y$, so $\frac{w_1}{w_{-1}}=e^{2y/\sigma^2}$. Hence $P[X=1|y]=\frac1{1+e^{-2y/\sigma^2}}$ and $P[X=-1|y]=\frac1{1+e^{2y/\sigma^2}}$.
4. MMSE ("find the MMSE estimate"): $\hat X=P[1|y]\cdot(+1)+P[-1|y]\cdot(-1)=P_1-P_{-1}$. With $u=y/\sigma^2$, the identity $\frac{e^{2u}-1}{e^{2u}+1}=\tanh u$ gives $\hat X_{MMSE}=\tanh(y/\sigma^2)$.
5. MAP ("find the MAP estimate", "threshold"): pick the larger posterior. $\frac{P_1}{P_{-1}}=e^{2y/\sigma^2}>1$ exactly when $y>0$. So $\hat X_{MAP}=+1$ if $y>0$, $-1$ if $y<0$, and $y_{th}=0$. The MAP is a hard decision, while the MMSE is a soft value in $(-1,1)$.

**Recipe D: mixture of two bumps (q3-23-2f, 2g)**

The posterior has bump 1 centred at $+x$ with weight $c$, and bump 2 centred at $-x$ with weight $1-c$.
- MMSE: each bump's mean is its centre, so the weighted mean is $cx-(1-c)x=(2c-1)x$. For $c=\frac12$ this is $0$. For $c=\frac34$ it is $\frac12x$.
- MAP: the tallest peak. For $c=\frac12$ both bumps are equally tall, so there are two maxima at $\pm x$. For $c=\frac34$ the bump at $+x$ is taller, so MAP $=x$.
- Sketch: the MMSE sits in the valley or between the bumps, where the posterior is small. The mean and the peak differ because the posterior is not one symmetric bump.

**Recipe E: flat prior on a bounded interval (jan19-2b)**

The prior is $\frac12$ on $[0,2]$ and $0$ outside. The likelihood is $\lambda e^{-\lambda x}$ for one observation $x$.
- MMSE: the posterior is the likelihood restricted to $[0,2]$ and normalised. The $\frac12$ cancels, so $\hat\lambda=N/D$ with $N=\int_0^2\lambda^2e^{-\lambda x}d\lambda$ and $D=\int_0^2\lambda e^{-\lambda x}d\lambda$. Integration by parts gives $N=\frac{2-e^{-2x}(2+4x+4x^2)}{x^3}$ and $D=\frac{1-e^{-2x}(1+2x)}{x^2}$. The result is $\hat\lambda_{MMSE}=\frac2x\left(1-\frac{2x^2e^{-2x}}{1-e^{-2x}(1+2x)}\right)$.
- MAP: the peak of $\lambda e^{-\lambda x}$ is where $\frac1\lambda-x=0$, so $\lambda=\frac1x$. The flat prior clips this to the allowed interval, giving $\hat\lambda_{MAP}=\min(\frac1x,2)$. For $n$ observations, the peak is $\frac{n}{\sum x_i}$, clipped at 2.

**MC bullets (the reason is given where it is not obvious)**
- "MMSE is the mean of the posterior": TRUE. "MMSE is the maximum of the posterior": FALSE. The maximum is MAP.
- "MAP always equals the posterior mean" (jun26-2a-type): FALSE. They are equal only for one symmetric bump, e.g. a Gaussian posterior.
- "MMSE and MAP always give different estimates" (apr25-2a, apr24-2b, jan22-2d): FALSE, for the same reason. They can be equal, and they are equal for one symmetric bump.
- "MAP converges to MLE regardless of the prior" (jun26-2a): FALSE. More data does shrink the prior's effect. But a prior that rules out the MLE value keeps MAP away from it, however much data arrives.
- "MAP depends on the likelihood and the prior and cannot be computed without a prior": TRUE.
- "The MLE is the argmax of the likelihood": TRUE.
- "Bayesian estimators do not use prior knowledge": FALSE. That is the point of Bayesian estimation.
- "Minimising Bayes risk with uniform cost gives MMSE": FALSE. Uniform cost gives MAP.
- "The Bayes estimate minimises Bayes risk, the average cost": TRUE.

Answer letters: jun26-2a = c, apr25-2a = c, apr24-2b = a, jan22-2d = b, nov22-2c = b.

## 2.3 · Least squares
Symbols: $x[n]$ = observed data sample number $n$; $s[n]$ = what the model predicts for sample $n$; $w[n]$ = noise; $\theta$ (theta) = unknown parameter(s) to estimate; $\hat\theta$ = the estimate; $J$ = cost, the total squared gap between data and model. Least squares (LS) = choose the unknowns that make $J$ smallest. Every sum $\sum$ runs over all data samples.

**Recipe A · straight line $y=ax+b$.** Exam says "find the linear function having least squares error" -> use A.
1. Compute $\bar x$ = mean of the x-values and $\bar y$ = mean of the y-values. The best line passes through $(\bar x,\bar y)$, which is why step 4 works.
2. Deviations $dx=x_n-\bar x$, $dy=y_n-\bar y$ for each point. Centering removes $b$ from the slope equation.
3. $a=\dfrac{\sum dx\,dy}{\sum dx^2}$ (minimising $J$ over $a$ gives this).
4. $b=\bar y-a\bar x$ (the line passes through $(\bar x,\bar y)$).

Worked (apr25-2b, points $(0,3),(2,4),(3,3)$):
- Three points. x-values 0, 2, 3: $\bar x=(0+2+3)/3=5/3$. y-values 3, 4, 3: $\bar y=10/3$.
- $dx$: $0-\tfrac53=-\tfrac53$; $2-\tfrac53=\tfrac13$; $3-\tfrac53=\tfrac43$.
- $dy$: $3-\tfrac{10}3=-\tfrac13$; $4-\tfrac{10}3=\tfrac23$; $3-\tfrac{10}3=-\tfrac13$.
- $\sum dx\,dy=\tfrac59+\tfrac29-\tfrac49=\tfrac39=\tfrac13$.
- $\sum dx^2=\tfrac{25}9+\tfrac19+\tfrac{16}9=\tfrac{42}9=\tfrac{14}3$.
- $a=\tfrac{1/3}{14/3}=\tfrac1{14}\approx0.071$.
- $b=\tfrac{10}3-\tfrac1{14}\cdot\tfrac53=\tfrac{140}{42}-\tfrac5{42}=\tfrac{135}{42}=\tfrac{45}{14}\approx3.21$.
- Final answer, the line the question asks for: $y=\tfrac1{14}x+\tfrac{45}{14}$.

**Recipe B · closed form, avoid nonlinear optimisation.** Exam says "closed-form", "avoid the nonlinear optimization" -> use B. Works when $s=g(\theta)$ and $g$ is invertible (e.g. $\ln$, $e^{\cdot}$).
1. Write $\alpha=g(\theta)$. The cost in $\alpha$ is an ordinary sum of squares, so it is solvable directly (step 2). Why: a one-to-one relabelling keeps the best fit the same.
2. Solve LS for $\alpha$ with recipe C. For $x[n]=\alpha+w[n]$ the answer is $\hat\alpha=\bar x$.
3. Map back: $\hat\theta=g^{-1}(\hat\alpha)$ (the inverse undoes step 1).

Worked (q3-23-2d, $x[n]=\ln\theta+w[n]$, $n=0,\dots,N-1$): put $\alpha=\ln\theta$, so $x[n]=\alpha+w[n]$. LS gives $\hat\alpha=\bar x=\tfrac1N\sum_{n=0}^{N-1}x[n]$, the mean of all $N$ samples. Map back: $\hat\theta=e^{\hat\alpha}=\exp\big(\tfrac1N\sum x[n]\big)$. Answer: yes, closed form, the exp of the sample mean.

**Recipe C · signal linear in one amplitude $A$.** Use when $s[n]=A\,h[n]$ with $h[n]$ known (e.g. $h=e^{\phi n}$, or $h=1$ for a constant). Not for $\phi$ and $A$ both unknown -> D.
1. $J=\sum(x[n]-A\,h[n])^2$, the cost.
2. Set $dJ/dA=0$: $\sum h[n](x[n]-A\,h[n])=0$ (the best fit makes the gap orthogonal to $h$).
3. $\hat A=\dfrac{\sum x[n]h[n]}{\sum h[n]^2}$. Constant $h=1$ gives $\hat A=\bar x$.

Worked (jan20-4b, $s[n]=Ae^{\phi n}$, $\phi$ known): here $h[n]=e^{\phi n}$. Step 2: $\sum e^{\phi n}(x[n]-Ae^{\phi n})=0$. Step 3, using $e^{\phi n}e^{\phi n}=e^{2\phi n}$: $\hat A=\sum x[n]e^{\phi n}\big/\sum e^{2\phi n}$. This is the closed form in $\phi$ and the data that the question asks for.

**Recipe D · nonlinear model, $\phi$ and $A$ both unknown.** Exam says "write the cost function" -> D1. "Gauss-Newton... iterative" -> D2–D4.
1. Cost with $\theta=[\phi\ A]^T$ (a column of unknowns; $^T$ = transpose, just makes it a column): $J=\sum(x[n]-Ae^{\phi n})^2$.
2. Matrix $G$ holds the partial derivatives of $s$ per sample $n$: column 1 $\partial s/\partial\phi = nAe^{\phi n}$, column 2 $\partial s/\partial A=e^{\phi n}$. Why: Gauss-Newton replaces the curve by its straight-line approximation at the current guess.
3. Start from a guess $\theta_0$.
4. Iterate: $\theta_{k+1}=\theta_k+(G^TG)^{-1}G^T\big(x-s(\theta_k)\big)$, with $G$ and $s(\theta_k)$ evaluated at the current guess $\theta_k$ (index $k$ = iteration number). Why: solving the linear LS for the correction moves the guess toward the minimum; repeat until it stops changing.

**Facts and MC traps**
- Linear model $x=H\theta+w$: $\hat\theta=(H^TH)^{-1}H^Tx$. Needs at least as many data as unknowns, not exactly as many (fewer data: $H^TH$ cannot be inverted).
- The error $x-H\hat\theta$ is perpendicular to every column of $H$. FALSE: "error lies in the column space of $H$". $\hat\theta$ itself is not perpendicular to them.
- WLS with $W=C_x^{-1}$ is the best linear unbiased estimator (BLUE): TRUE.
- Nonlinear: separating into linear + nonlinear LS, or transforming to a linear problem, can give a closed form: TRUE.
- Nonlinear: "only Gauss-Newton works, not Newton-Raphson" is FALSE; both work.
- "What kind of estimator?" for jan20-4a: least squares (LS), cost $J$ as in D1 or C1.

## 2.4 · CRLB

**Words.** $\theta$ = the unknown number we want to estimate. $p(x;\theta)$ = probability density of the data $x$ when the true value is $\theta$ (the ";" means $\theta$ is fixed, not random). $N$ = number of samples. $\hat\theta$ = estimator, a formula on the data that gives a guess. $E$ = average over the random data. $\operatorname{Var}$ = spread of $\hat\theta$ over repeated experiments. $\ln$ = natural log. Unbiased = $E[\hat\theta]=\theta$ on average. MVUE = unbiased estimator with the smallest variance. MLE = maximum-likelihood estimator. CRLB = Cramér-Rao lower bound, the smallest variance an unbiased estimator can have. $\mathcal I(\theta)$ = Fisher information for all $N$ samples; $i(\theta)$ = for one sample.

**Facts and T/F traps.**
- $i(\theta)=-E[\frac{d^2}{d\theta^2}\ln p]\ge0$. It is non-negative because $\ln p$ peaks at the best $\theta$, so its average curvature is negative and its negative is positive. "Strictly negative" is FALSE.
- N i.i.d. samples: $\mathcal I=N\,i(\theta)$ is TRUE. Why: $\ln$ of a product of independent densities is a sum, and sums of second derivatives and averages add.
- Bound: $\operatorname{Var}(\hat\theta)\ge 1/\mathcal I$, never $\ge\mathcal I$ (swapped-formula trap). Why: more information means sharper data, so less variance: the bound is the reciprocal.
- The bound is $\propto 1/N$, so it shrinks as $N$ grows. The Jan 2022 option calls this "decreases linearly"; the key marks it TRUE.
- "Always derivable" is FALSE: it needs Recipe D. The bound applies to unbiased estimators only.
- "Variance lower than CRLB means efficient" is FALSE. Unbiased estimators cannot go below the bound; efficient means exactly equal to it.

**Recipe A: pdf $p(x;\theta)$ is written out.** Use for "derive Fisher information" or "CRLB for the MLE" when a density is given. For "$x$ = signal + noise" use B.
1. Take $\ln p$. Why: the formula is written with the log-density.
2. Differentiate twice w.r.t. $\theta$. Why: the formula needs the curvature of $\ln p$.
3. Negate, then take $E$ over $x$. Why: averaging removes the random $x$, leaving a function of $\theta$.
4. $\mathcal I=N\,i$. Why: N independent samples.
5. Bound $=1/\mathcal I$. Why: Cramér-Rao inequality for unbiased estimators.

**Example (Nov 2019 3b).** One sample has $p=\frac{x}{\theta^2}e^{-x^2/2\theta^2}$, $x\ge0$. Question: "Find the CRLB for the MLE."
Step 1: $\ln p=\ln x-2\ln\theta-\frac{x^2}{2\theta^2}$. The log of a product is a sum, and $\ln e^{y}=y$.
Step 2: first derivative $-\frac{2}{\theta}+\frac{x^2}{\theta^3}$; second derivative $\frac{2}{\theta^2}-\frac{3x^2}{\theta^4}$ (since $\theta^{-3}$ differentiates to $-3\theta^{-4}$).
Step 3: negate: $-\frac{2}{\theta^2}+\frac{3x^2}{\theta^4}$. Take $E$: $E[x^2]=\int_0^\infty x^2\frac{x}{\theta^2}e^{-x^2/2\theta^2}dx=2\theta^2$ (substitute $u=x^2$). The $\theta$ terms are constants, so they stay: $-\frac{2}{\theta^2}+\frac{3\cdot2\theta^2}{\theta^4}=-\frac{2}{\theta^2}+\frac{6}{\theta^2}=\frac{4}{\theta^2}$. So $i=4/\theta^2$.
Step 4: N samples: $\mathcal I=N\cdot\frac{4}{\theta^2}=\frac{4N}{\theta^2}$.
Step 5: bound $=\frac{1}{\mathcal I}=\frac{\theta^2}{4N}$. This is the answer to "CRLB for the MLE". The key writes $\hat\theta^2/4N$: the same formula with the estimate plugged in for $\theta$.

**Recipe B: $x$ = signal($\theta$) + white Gaussian noise $w$ with variance $\sigma^2$.** Use when the model is written as a mean plus noise (Nov 2022 2e), not as a density.
1. Write each sample's mean $\mu_n(\theta)$ and its derivative $\mu_n'$. Why: the signal carries $\theta$.
2. $\mathcal I=\sum_n(\mu_n')^2/\sigma^2$. Why: for Gaussian noise, the expectation in A reduces to $\mu'^2/\sigma^2$, because the noise averages to zero ($E[x-\mu]=0$).
3. Simplify the sum with $\sin^2+\cos^2=1$.

**Example (Nov 2022 2e).** $\mathbf x=A[\cos\theta,\sin\theta]^T+\mathbf w$, so sample 1 has mean $\mu_1=A\cos\theta$ and sample 2 has $\mu_2=A\sin\theta$ (the exam hint).
Step 1: $\mu_1'=-A\sin\theta$ (derivative of $\cos$ is $-\sin$) and $\mu_2'=A\cos\theta$.
Step 2: $\mathcal I=\frac{(-A\sin\theta)^2+(A\cos\theta)^2}{\sigma^2}$. Squaring removes the minus sign.
Step 3: $=\frac{A^2(\sin^2\theta+\cos^2\theta)}{\sigma^2}=\frac{A^2}{\sigma^2}$. This answers "derive $\mathcal I(\theta)$".

**Recipe C: MVUE given, find the pdf.** Use for "given the MVUE ... find $p(\mathbf x;\theta)$, use the MVUE condition". The data $x[n]$ are i.i.d. with noise variance $\sigma^2$.
1. Find $\sigma^2$ from the given variance. Why: the mean of N samples has variance $\sigma^2/N$. Example: $\operatorname{Var}(\hat\theta)=\frac{1}{N^2}\cdot N\sigma^2=\frac{\sigma^2}{N}$; matching $A^2/N$ gives $\sigma^2=A^2$.
2. $\mathcal I=1/\operatorname{Var}(\hat\theta)=N/A^2$. Why: an MVUE hits the bound.
3. MVUE condition: $\frac{\partial\ln p}{\partial\theta}=\mathcal I(\hat\theta-\theta)$. Why: this equality holds exactly when the estimator reaches the bound.
4. Substitute $N\hat\theta=\sum_n x[n]$: $\frac{N}{A^2}(\hat\theta-\theta)=\frac{1}{A^2}\sum_n(x[n]-\theta)$. Why: $N\theta=\sum_n\theta$, so $\theta$ moves inside the sum.
5. Integrate over $\theta$. The hint $\int(x+a)dx=\frac12(x+a)^2$ with $a=-x$ gives $\int(x-\theta)d\theta=-\frac12(x-\theta)^2$ (check: differentiating the right side w.r.t. $\theta$ gives $x-\theta$). So $\ln p=-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2+g(\mathbf x)$, where $g$ depends on the data only, not on $\theta$.
6. Exponentiate and fix the constant: $p=(2\pi A^2)^{-N/2}\exp\!\big(-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2\big)$. Why: $p$ must integrate to 1 over the data; each sample's Gaussian term integrates to $\sqrt{2\pi A^2}$, and the N independent samples give $(2\pi A^2)^{N/2}$.

**Recipe D: "check whether the CRLB can be derived".** Use when the density is nonzero only on a range that depends on $\theta$.
1. Find the support: the set of $x$ where $p>0$.
2. If the edges of the support move with $\theta$, the CRLB is NOT possible. Why: the proof differentiates an integral over a fixed range of $x$; moving edges break this (regularity violated).
3. Otherwise derive with A.

**Example (Jan 2022 2e).** $p=\frac{2}{\theta}x$ for $0\le x\le\theta$. If $\theta=2$, data lie in $[0,2]$; if $\theta=3$, in $[0,3]$. The range changes with $\theta$, so the answer is "not possible: the support depends on $\theta$."

**Which recipe:** "derive $\mathcal I$" with a density → A; with signal + noise → B; "given MVUE, find pdf" → C; "can the CRLB be derived / justify" → D; "which statement is TRUE/FALSE" → facts list.

**Example (Q1 2023 2a, "exactly one FALSE").** (a) $N$ i.i.d. gives $N\,i$: TRUE (sums add). (b) "Var $\ge\mathcal I$": FALSE, the bound is $1/\mathcal I$. (c) "strictly positive": doubtful, since $\mathcal I=0$ when $p$ does not depend on $\theta$. The key marks (b).

**Answers.** Nov 2022 2a: (a); the other two are a swapped bound and a negative information. Apr 2024 2a: (c); (a) is the swapped bound, (b) is negative. Jan 2022 2a: (b); (a) fails regularity, (c) is impossible for unbiased estimators.

## 2.5 · MC words

Symbols: $\theta$ (theta) = the unknown parameter we want; $\hat\theta$ = its estimate computed from data $x$; $N$ = number of observations; $p(x;\theta)$ = probability density of the data for a given $\theta$; $\mathcal I(\theta)$ = Fisher information of all $N$ observations, $i(\theta)$ = for one observation; $E[\cdot]$ = average; Var = variance; CRLB = Cramér–Rao lower bound.

**Facts to check statements against**
- Unbiased: $E[\hat\theta]=\theta$ (the average estimate is right). Consistent: $\hat\theta\to\theta$ as $N\to\infty$.
- Efficient: unbiased AND Var $=$ CRLB. Going below the bound is impossible, so "below the bound = efficient" is false.
- CRLB $=1/\mathcal I(\theta)$, NOT $\mathcal I$. $\mathcal I\ge 0$ (an average of a second derivative, so never negative). $N$ iid observations: $\mathcal I=N\,i(\theta)$, so CRLB $=1/(N i)$ falls as $1/N$.
- MLE = $\arg\max_\theta p(x;\theta)$, the value that makes the data most likely. Asymptotically unbiased: true. Always reaching the CRLB: false (only for large $N$). Asymptotically normal, not uniform. Computable in general models by maximising. Invariance: if $\alpha=\psi(\theta)$ is one-to-one, then $\hat\theta=\psi^{-1}(\hat\alpha)$ (the inverse map applied to the MLE of $\alpha$).
- Bayes: $\theta$ has a prior $p(\theta)$, so Bayes estimators use the prior ("do not use prior" is false). Squared error cost gives MMSE = posterior mean $E[\theta|x]$. Uniform cost gives MAP = posterior maximum. "MMSE is the posterior max" is false. "MMSE and MAP always differ" is false: they coincide for a symmetric bell posterior. MAP needs a prior. Only for large $N$ does the data dominate the prior, so MAP approaches MLE. "Regardless of the prior" is false.

**Which recipe**: a statement with options (a)(b)(c) → recipe A. A formula or number asked from a likelihood $p(x|\lambda)$ and prior $p(\lambda)$ → recipe B.

**Recipe A: true/false statements**
1. Find the topic word (MLE, CRLB/Fisher, MMSE/MAP). Why: each option tests one fact of one topic.
2. Compare each option with the facts above and mark T/F. Why: distractors swap one word ($\ge\mathcal I$ vs $\ge 1/\mathcal I$, mean vs max, "always").
3. Read the phrasing: "Which is TRUE?" → pick the one true option. "Which is FALSE? (exactly one)" → pick the one false option, the others are true. "always / regardless / any" → look for a counterexample, usually false.

Example A1 (apr24-2a, CRLB): $N=10$ iid observations, each with $i(\theta)=2$. Then $\mathcal I=10\cdot 2=20$ (N iid observations add information), and the bound is $1/20=0.05$. Option "Var $\ge\mathcal I$" says Var $\ge 20$: false, since the bound is $0.05$. Same for q1-23 (b).

Example A2 (apr25-2a, MMSE vs MAP): posterior is a bell centred at 1. Its mean is 1 (balance point) and its max is 1 (peak). They are equal, so "always different" is false (apr25 (c), apr24-2b (c)).

Example A3 (jan22-2b, invariance): MLE of $\theta$ is $\hat\theta=3$, and $\alpha=2\theta$. Then $\hat\alpha=2\cdot 3=6$, and $\psi^{-1}(\alpha)=\alpha/2$ gives $\hat\theta=6/2=3$. Option (c) is true.

**Recipe B: MMSE and MAP from a likelihood and prior (jan19-2b)**
Given: $p(x|\lambda)=\lambda e^{-\lambda x}$ for $x\ge0$ (exponential model, $\lambda$ = rate, $x$ = observed value) and prior $p(\lambda)=\tfrac12$ on $[0,2]$.
1. Bayes' rule: $p(\lambda|x)=\dfrac{p(x|\lambda)\,p(\lambda)}{\int p(x|u)p(u)\,du}$. Why: posterior = likelihood times prior, divided by the total so it integrates to 1 ($u$ is a dummy integration variable).
2. MMSE $=E[\lambda|x]=\int_0^2\lambda\,p(\lambda|x)\,d\lambda$. Why: squared cost gives the posterior mean. Exam "provide the formula, specifying each distribution" → write steps 1–2 with $p(x|\lambda)$ and $p(\lambda)$ explicit.
3. The $\tfrac12$ is the same top and bottom, so it cancels: posterior $\propto\lambda e^{-\lambda x}$ on $[0,2]$.
4. Numerator $\int_0^2\lambda^2e^{-\lambda x}d\lambda$, denominator $\int_0^2\lambda e^{-\lambda x}d\lambda$. Use the given integrals with $a=-x$, evaluate at 2 and subtract the value at 0 (a definite integral is $F(2)-F(0)$). Exam "solve the formula from b1" → this step.
5. Result: $\hat\lambda_{MMSE}=\dfrac{2}{x}\cdot\dfrac{1-(1+2x+2x^2)e^{-2x}}{1-(1+2x)e^{-2x}}$. Check $x=1$: numerator $2(1-5e^{-2})=2(1-0.677)=0.647$, denominator $1-3e^{-2}=1-0.406=0.594$, ratio $\approx1.09$, inside $[0,2]$.
6. MAP = $\arg\max_\lambda p(\lambda|x)$. Exam "find the MAP" → this step. The denominator of step 1 does not depend on $\lambda$, so drop it (a constant cannot move the peak). Take the log: $\ln\lambda-\lambda x$, derivative $1/\lambda-x=0$, so $\lambda=1/x$. The prior is zero above 2, so cap at 2: $\hat\lambda_{MAP}=\min(1/x,\,2)$ (key: $N/\sum x_i$ for $N$ observations, same cap). Example $x=0.25$: $1/0.25=4$ lies outside $[0,2]$, the posterior still rises at 2, so the answer is $\min(4,2)=2$.

**Related**: CRLB "decreases linearly with N" (jan22-2a b): key says true, but the real shape is $1/N$. It is the only option about $N$ that holds.

## Checks & sign rules
- Probabilities lie in $[0,1]$; $\iint p=1$; a PSD never goes negative (a *correlogram estimate* may); $P_{FA}$ uses the $H_0$ curve.
- Dividing an inequality by a negative **flips** it.
- Roots of the AR/factorisation quadratics come in pairs $a$ and $1/a$: always keep $|a|\lt1$, $|b|\lt1$ (that is what "minimum phase" wants).
- $x[n]=i[n]-a_1x[n-1]-\dots$ with $r[1]>0$ gives a **negative** $a_1$; a minus sign in front of $\cos\theta$ gives a negative $a$.
- Round only at the very end.

</div>
</div>

<div class="pagebreak"></div>

<div class="cheat" markdown>
<div class="cheat-cols" markdown>

## 3.1 · Correlogram + pick the plot

**Symbols.** $r[k]$ = autocorrelation at lag $k$: how much the signal resembles itself $k$ steps later; $r[0]$ = its variance (no shift). $r[-k]=r[k]$ (symmetry). $\theta$ = frequency in radians, from $0$ (slowest) to $\pi$ (fastest alternation). $\hat P(\theta)$ = estimated power spectral density (power per frequency). $c=\cos\theta$ (shorthand). $i[n]$ = white noise input (zero mean, uncorrelated in time); its variance is $\sigma^2$ (written $\sigma_i^2$ in exams). $a_k$ = AR weights on past outputs, $b$ = MA weight, $p$ = AR order, $q$ = MA order, $N$ = data length.

**Which recipe?** "correlogram", "non-parametric", "using only the given lags", "function of $\cos\theta$" → recipe 1. "AR(1)" → 2. "AR(2)", "Yule-Walker" → 3. "MA(1)", "approximate as MA", "MA(q)" → 4. "which plot/figure/option" → 5. "order $p$", "residual", "criterion" → 6. "Wiener", "FIR coefficients", "$J_{min}$" → 7.

**1. Correlogram (uses only the given lags)**

1. Write the given lags. Lags not given, or "$r=0$ for $|k|>q$", are zero, so drop them. Why: the correlogram sums only the known lags.
2. Write $\hat P(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$ and stop at the last nonzero lag. Why: the PSD is the Fourier transform of $r$; $r[k]$ and $r[-k]$ pair up into $2r[k]\cos k\theta$, while lag 0 has no partner, so it is not doubled.
3. For a function of $c$: $\cos2\theta=2c^2-1$, $\cos3\theta=4c^3-3c$ (multiple-angle identities), then collect powers of $c$.

Worked story (jun26-3c, "as function of $\cos\theta$"): $r[0]=3$, $r[1]=2$, $r[2]=1$, zero beyond lag 2. So we stop at lag 2: $\hat P=3+2\cdot2\cos\theta+2\cdot1\cos2\theta=3+4\cos\theta+2\cos2\theta$. Step 3: $2\cos2\theta=2(2c^2-1)=4c^2-2$, so $\hat P=3+4c+4c^2-2=4c^2+4c+1=(2c+1)^2$. Check: at $\theta=0$ ($c=1$) this is $9=3+4+2$.

**2. AR(1)** (use when a model is named; not for a plain correlogram)

Model: $x[n]+a_1x[n-1]=i[n]$: today = $-a_1\times$ yesterday + new noise. Yule-Walker equations come from multiplying by $x[n-k]$ and taking expectations; $i[n]$ is uncorrelated with the past, so its term vanishes.

1. $a_1=-r[1]/r[0]$. Why: the lag-1 equation is $r[1]=-a_1r[0]$.
2. $\sigma^2=r[0]+a_1r[1]$. Why: the variance the past cannot predict is the noise variance.
3. $\hat P=\sigma^2/(1+2a_1\cos\theta+a_1^2)$. Why: this is $\sigma^2/|1+a_1e^{-j\theta}|^2$ expanded.

Worked story (apr25-3e, $r[0]=2$, $r[1]=-\tfrac14$): $a_1=-(-\tfrac14)/2=\tfrac18$. $\sigma^2=2+\tfrac18\cdot(-\tfrac14)=2-\tfrac1{32}=\tfrac{63}{32}$. Denominator: $1+\tfrac{2}{8}c+\tfrac1{64}=\tfrac{65+16c}{64}$, so $\hat P=\tfrac{63}{32}\cdot\tfrac{64}{65+16c}=\tfrac{126}{65+16c}$. Check: $P(0)=126/81\approx1.56$. Other AR(1) keys: nov22-3f $a_1=\tfrac18$, $\sigma^2=\tfrac{63}{64}$, $\hat P=\tfrac{63}{65+16c}$; jan22-3d $a_1=\tfrac{15}{26}$, $\hat P=\tfrac{5863}{7208+6240c}$.

**3. AR(2)**

1. Yule-Walker in matrix form: $\begin{pmatrix}r[0]&r[1]\\r[1]&r[0]\end{pmatrix}\begin{pmatrix}a_1\\a_2\end{pmatrix}=-\begin{pmatrix}r[1]\\r[2]\end{pmatrix}$. Why: the lag-1 and lag-2 equations, with $r[-1]=r[1]$.
2. Solve it: $D=r[0]^2-r[1]^2$, $a_1=-r[1](r[0]-r[2])/D$, $a_2=(r[1]^2-r[0]r[2])/D$.
3. $\sigma^2=r[0]+a_1r[1]+a_2r[2]$ (same reason as AR(1)).
4. $\hat P=\sigma^2/(1+a_1^2+a_2^2+2a_1(1+a_2)\cos\theta+2a_2\cos2\theta)$. Why: expanding $|1+a_1e^{-j\theta}+a_2e^{-2j\theta}|^2$. Quick checks: $P(0)=\sigma^2/(1+a_1+a_2)^2$, $P(\pi)=\sigma^2/(1-a_1+a_2)^2$.

Worked story (jun26-3d, $r=3,2,1$): the equations are $3a_1+2a_2=-2$ and $2a_1+3a_2=-1$. $D=9-4=5$, $a_1=-2(3-1)/5=-\tfrac45$, $a_2=(4-3)/5=\tfrac15$. Check the first: $3(-\tfrac45)+2(\tfrac15)=-2$ ✓. $\sigma^2=3+(-\tfrac45)(2)+\tfrac15(1)=\tfrac85$. Denominator in $c$: $1+\tfrac{16}{25}+\tfrac1{25}-\tfrac{48}{25}c+\tfrac25(2c^2-1)=\tfrac{4(5c^2-12c+8)}{25}$, so $\hat P=\tfrac{10}{5c^2-12c+8}$. Check: $P(0)=10=(\tfrac85)/(\tfrac25)^2$.

**4. MA(1)** (key fact: MA($q$) autocorrelation is zero beyond lag $q$, so the correlogram over lags $0..q$ is already the exact MA PSD)

Model: $x[n]=i[n]+b\,i[n-1]$. Let $\rho=r[1]/r[0]$.

1. Only if parameters are asked: $\rho=b/(1+b^2)$, solve the quadratic in $b$, keep the root with $|b|<1$ (the usual invertible choice).
2. $\sigma^2=r[0]/(1+b^2)$. Why: $r[0]=\sigma^2(1+b^2)$.
3. $\hat P=r[0]+2r[1]\cos\theta$. Why: step 1 of recipe 1 with lags $0..q$ only.

Worked story (jan20-3b, $r[0]=\tfrac1{21}$, $r[1]=\tfrac2{105}$): $\rho=\tfrac{2/105}{1/21}=\tfrac25$. Then $b/(1+b^2)=\tfrac25$ gives $2b^2-5b+2=0$, $b=\tfrac{5\pm3}{4}\in\{2,\tfrac12\}$. Keep $b=\tfrac12$ ($|b|<1$). $\sigma^2=\tfrac{1/21}{5/4}=\tfrac4{105}$. PSD $=\tfrac1{21}+\tfrac4{105}\cos\theta$, identical to the correlogram in 3(a): that answers "how does this relate?" (the given $r$ is exactly an MA(1) autocorrelation). Pe21-3c: "no need for MA parameters" → steps 3 only.

**5. Pick the plot** (curves: correlogram, AR, MA)

1. Compute each PSD at $\theta=0$ ($c=1$, all cosines $=1$) and at $\theta=\pi$ ($c=-1$, $\cos2\theta=1$, $\cos3\theta=-1$). Why: two endpoints separate the curves quickly; you do not need the whole shape.
2. Match these heights to the plot. The plot with the matching heights is the answer.

Apr25-3g: correlogram $1.125$ at $0$, $2.125$ at $\pi$; MA(1) $1.5$ and $2.5$; AR(1) $1.56$ and $2.57$. All three start at $1.1$–$1.6$ and end at $2.1$–$2.6$: key plot D. Apr24-3f: correlogram $\tfrac1{16}\approx0.06$ at $0$ and $\tfrac{81}{16}\approx5.06$ at $\pi$; AR(2) $\approx0.69$ at $0$ and $\approx5.62$ at $\pi$: key plot B.

Trap: the correlogram may dip below 0 (nov19-2a is exactly $0$ at $\pi$); a true PSD never does.

**6. AR order and model selection** (jun26-3e, theory)

- Residual variance $\sigma^2$ never rises as $p$ grows; it falls. The risk is overfitting: the model fits noise and shows spurious peaks.
- Criteria against this: $\text{AIC}=N\ln\hat\sigma^2+2p$ (or FPE/AICc). Why: the first term falls with a better fit, the $2p$ penalty grows with the number of parameters; pick the order that minimises the sum.
- Any spectrum, even one with deep nulls from an MA, is approximated by an AR model of high enough order (AR($\infty$) in theory).

**7. Wiener filter** (jan19-4; not a PSD, but in this pack)

1. Normal equations $R\,w=d$: $R$ = matrix of input autocorrelations, $d$ = cross-correlations of reference $e$ with the input, $w$ = filter weights. Why: setting the error's derivative to zero.
2. $J_{min}=\sigma_e^2-w^Td$. Why: the error left is the reference variance minus what the filter explains.

Story (a, $H=1$, $x[k]=i[k]+\tfrac12x[k-1]$, $\sigma_i^2=\tfrac14$): $r_x[0]=\tfrac{1/4}{1-1/4}=\tfrac13$, $r_x[1]=\tfrac12\cdot\tfrac13=\tfrac16$. $d=(\tfrac23,\tfrac56)$. Rows: $2w_0+w_1=4$, $w_0+2w_1=5$, so $w=(1,2)$. $J_{min}=\tfrac73-(\tfrac23+\tfrac53)=0$.

Story (b, $H=1-2z^{-1}$): $g[k]=x[k]-2x[k-1]$. $r_g[0]=5\cdot\tfrac13-4\cdot\tfrac16=1$, $r_g[1]=5\cdot\tfrac16-2\cdot\tfrac13-2\cdot\tfrac1{12}=0$, so $R=I$. $d=(\rho_{ex}[0]-2\rho_{ex}[1],\ \rho_{ex}[1]-2\rho_{ex}[2])=(\tfrac23-\tfrac53,\ \tfrac56-\tfrac56)=(-1,0)$, so $w=(-1,0)$, $J_{min}=\tfrac73-1=\tfrac43$.

**Exam traps.** Jan22-3c fallback $a=\tfrac14$, $b=\tfrac54$ does not reproduce the given $r$ ($r[1]$ would be $\tfrac9{16}$, not $-\tfrac{15}{16}$): use the stated $r$ values (key: $\tfrac{13}8-\tfrac{15}8c+\tfrac12\cos2\theta$). Jun26-3e "order too high": the residual variance decreases, the risk is overfitting.

## 3.2 · AR / MA from $r[k]$

**Symbols.** $x[n]$: the random signal at time $n$. $i[n]$: the innovation, a fresh, unpredictable white-noise input (zero mean, variance $\sigma_i^2$) that drives the signal. $r[k]$: autocorrelation at lag $k$ (how many steps apart the two samples are), $r[k]=E\{x[n]x[n-k]\}$, with $r[-k]=r[k]$. $\theta$: frequency angle ($\theta=0$ is the slowest, $\theta=\pi$ the fastest). $c=\cos\theta$. $P$: power spectral density (PSD), the power per frequency. $p$: AR order, $q$: MA order. $a_1,a_2$: AR coefficients. $b$: MA coefficient. $\alpha,\beta$: ARMA coefficients. $N$: data length.

**Which recipe?** Right side has only $i$ terms with delays up to $q$ → MA($q$). Left side has past $x$ terms → AR($p$). Both → ARMA. Given a PSD or r directly, use A. Given a model, use B–E. Given a plot, use F. Wiener filter, use G. True/false or "what happens as $p$ grows", use H.

**Exam wording → step**
- "correlogram", "non-parametric", "using only the given lags" → A.
- "model as AR(1)" → B. "AR(2)", "Yule–Walker matrix" → C.
- "model as MA(1)/MA(2)", "find $a,b$" → D.
- "which kind of model", "autocorrelation of $x$" from a difference equation → E.
- "express as a function of cosines" → replace $\cos2\theta=2c^2-1$, $\cos3\theta=4c^3-3c$.
- "hint: MA autocorrelation is finite" → lags beyond $q$ are zero, stop at lag $q$.

**A. Correlogram (PSD from $r[k]$).**
1. Keep the lags up to the last one given, drop the rest. Why: the question says they are zero (or "use only these").
2. $P=r[0]+2r[1]\cos\theta+2r[2]\cos2\theta+\dots$. Why: $e^{jk\theta}+e^{-jk\theta}=2\cos k\theta$, and the lag $-k$ term equals the lag $+k$ term.
3. Write in $c$ with the formulas above.

Example jun26-3c: $r[0]=3$, $r[1]=2$, $r[2]=1$, zero beyond. Step 2: the lag-1 term is $2\cdot2\cos\theta=4\cos\theta$, the lag-2 term is $2\cdot1\cos2\theta=2\cos2\theta$, so $P=3+4\cos\theta+2\cos2\theta$. Step 3: $2\cos2\theta=2(2c^2-1)=4c^2-2$, so $P=3+4c+4c^2-2=4c^2+4c+1=(2c+1)^2$. This is the answer to 3c.

Example nov19-2a: $r=1,0.7,0.5,0.3$ and $r[4]=0$. Keep lags 0 to 3 (lag 4 is zero): $P=1+1.4c+\cos2\theta+0.6\cos3\theta$.

**B. AR(1).** Use for one coefficient.
1. $a_1=-\dfrac{r[1]}{r[0]}$. Why: multiply $x[n]+a_1x[n-1]=i[n]$ by $x[n-1]$ and take expectations; the right side is zero because $i[n]$ is new, so it is uncorrelated with the past.
2. $\sigma_i^2=r[0]+a_1r[1]$. Why: same equation times $x[n]$; the right side gives $\sigma_i^2$ because $i[n]$ is the new part of $x[n]$.
3. $P=\dfrac{\sigma_i^2}{1+a_1^2+2a_1c}$. Why: $|1+a_1e^{-j\theta}|^2=1+a_1^2+2a_1\cos\theta$.

Example apr25-3e: $r[0]=2$, $r[1]=-\frac14$. Step 1: $a_1=-\frac{-1/4}{2}=\frac18$. Step 2: $\sigma_i^2=2+\frac18\cdot(-\frac14)=2-\frac1{32}=\frac{63}{32}$. Step 3: $1+a_1^2=\frac{65}{64}$ and $2a_1=\frac14$, so $P=\dfrac{63/32}{65/64+c/4}$. Multiply top and bottom by 64: $P=\dfrac{126}{65+16c}$. This is the answer to 3e.

Example pe21-3b: $\rho[0]=\frac{28}{27}$, $\rho[1]=-\frac4{27}$. $a_1=\frac{4/27}{28/27}=\frac17$, $\sigma_i^2=\frac{28}{27}-\frac17\cdot\frac4{27}=\frac{64}{63}$, $P=\dfrac{224}{225+63c}$. Sketch: heights $\approx0.78$ at $\theta=0$ and $\approx1.38$ at $\theta=\pi$ (positive $a_1$ puts the peak at $\pi$).

**C. AR(2).** Use for two coefficients, given $r[0],r[1],r[2]$.
1. Yule–Walker in matrix form: $\begin{bmatrix}r[0]&r[1]\\r[1]&r[0]\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}=-\begin{bmatrix}r[1]\\r[2]\end{bmatrix}$. Why: multiply $x[n]+a_1x[n-1]+a_2x[n-2]=i[n]$ by $x[n-1]$ and by $x[n-2]$, take expectations; the right side is zero (new noise vs. past).
2. $D=r[0]^2-r[1]^2$ (determinant), $a_1=\dfrac{-r[1](r[0]-r[2])}{D}$, $a_2=\dfrac{r[1]^2-r[0]r[2]}{D}$. Why: Cramer's rule solves two equations in two unknowns.
3. $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$. Why: the same equation times $x[n]$, the right side gives $\sigma_i^2$.
4. $P=\dfrac{\sigma_i^2}{1+a_1^2+a_2^2+2(a_1+a_1a_2)c+2a_2(2c^2-1)}$. Why: $|1+a_1e^{-j\theta}+a_2e^{-2j\theta}|^2$ expanded, then $\cos2\theta=2c^2-1$.

Example jun26-3d: $r[0]=3$, $r[1]=2$, $r[2]=1$. Step 1: $D=9-4=5$. Step 2: $a_1=\dfrac{-2(3-1)}{5}=-\frac45$, $a_2=\dfrac{4-3}{5}=\frac15$. Check: $3(-\frac45)+2(\frac15)=-2=-r[1]$. Step 3: $\sigma_i^2=3+(-\frac45)(2)+\frac15(1)=3-\frac85+\frac15=\frac85$. Step 4: $a_1+a_1a_2=-\frac{24}{25}$, so the denominator is $\frac{42}{25}-\frac{48}{25}c+\frac25(2c^2-1)=\frac{20c^2-48c+32}{25}=\frac{4(5c^2-12c+8)}{25}$, and $P=\frac85\cdot\frac{25}{4(5c^2-12c+8)}=\dfrac{10}{5c^2-12c+8}$. This is the answer to 3d.

nov19-2b uses the same steps: $D=0.51$, $a_1=-0.686$, $a_2=-0.0196$, $\sigma_i^2\approx0.510$.

**D. MA(1) and MA(2) from $r$.** Use when asked to find $b$ (or $a,b$). Unknown: $b$, and $\sigma_i^2$ when not given.

MA(1): $x[n]=i[n]+b\,i[n-1]$. Why the formulas: $r[0]$ pairs each coefficient with itself, $r[1]$ pairs neighbours, so $r[0]=\sigma_i^2(1+b^2)$, $r[1]=\sigma_i^2b$.
1. $u=\dfrac{r[0]}{r[1]}$ (a helper, not the order). Why: dividing kills $\sigma_i^2$, leaving $u=\dfrac{1+b^2}{b}$.
2. $b^2-ub+1=0$, so $b=\dfrac{u\pm\sqrt{u^2-4}}{2}$.
3. Keep the root with $|b|<1$. Why: the two roots multiply to 1, so exactly one qualifies; that is the invertible model.
4. $\sigma_i^2=\dfrac{r[1]}{b}$.
5. $P=r[0]+2r[1]c$. Why: $\sigma_i^2(1+b^2+2bc)$ is the same thing. Use only lags 0 and 1 even if more are given, because the MA(1) model says the rest are zero.

Example apr25-3f: $r[0]=2$, $r[1]=-\frac14$ (ignore $r[2]=-\frac3{16}$). Step 1: $u=\dfrac{2}{-1/4}=-8$. Step 2: $b=\dfrac{-8\pm\sqrt{64-4}}{2}=-4\pm\sqrt{15}$, about $-0.127$ or $-7.87$. Step 3: keep $b\approx-0.13$. Step 4: $\sigma_i^2=\dfrac{-1/4}{-0.127}\approx1.97$. Step 5: $P=2-\frac12c$. Check: $1.97(1+0.016-0.254c)\approx2-0.5c$. This is the answer to 3f.

jan20-3b: $r[0]=\frac1{21}$, $r[1]=\frac2{105}$, so $u=\frac52$, $b=\frac{5/2\pm3/2}{2}$, keep $b=\frac12$, $\sigma_i^2=\frac{2/105}{1/2}=\frac4{105}$. Its PSD equals the correlogram in (a), because the given $r$ is exactly the MA(1) autocorrelation (zero beyond lag 1).

MA(2): $x[n]=i[n]+a\,i[n-1]+b\,i[n-2]$. Why: lag 2 has one pair ($1\cdot b$), lag 1 has two pairs ($1\cdot a$ and $a\cdot b$), so $r[2]=\sigma_i^2b$, $r[1]=\sigma_i^2a(1+b)$.
1. $b=\dfrac{r[2]}{\sigma_i^2}$.
2. $a=\dfrac{r[1]}{\sigma_i^2(1+b)}$.
3. $r[0]=\sigma_i^2(1+a^2+b^2)$ if $r[0]$ is not given.

Example jan22-3b: $r[1]=-\frac{15}{16}$, $r[2]=\frac14$, $\sigma_i^2=1$. $b=\frac14$. $a=\dfrac{-15/16}{1+1/4}=-\frac{15}{16}\cdot\frac45=-\frac34$. Check: $a+ab=-\frac34-\frac3{16}=-\frac{15}{16}$ ✓. Then jan22-3c: $r[0]=1+\frac9{16}+\frac1{16}=\frac{13}8$, and the correlogram is $\frac{13}8-\frac{15}8c+\frac12\cos2\theta$. Note: the fallback $a=\frac14$, $b=\frac54$ in the exam does not reproduce the given $r$ (it gives $r[1]=\frac9{16}$); trust your derived $a=-\frac34$, $b=\frac14$.

**E. Model type and $r[\tau]$ from a difference equation (ARMA).**
Model type: count which terms appear. Only $i$ with delays → MA(largest delay). $x$ on the right too → ARMA($p$,$q$) with $p$ the largest $x$-delay and $q$ the largest $i$-delay.

MA($q$) autocorrelation: $r[l]=\sigma_i^2\times$(sum of products of coefficients $l$ places apart), zero beyond $q$.

Example apr24-3c: $x[n]=i[n]-\frac12i[n-1]+\frac14i[n-2]-\frac12i[n-3]$ is MA(3) (largest delay 3). Coefficients $1,-\frac12,\frac14,-\frac12$; $\sigma_i^2$ not given, take 1 as the key does. $r[0]=1+\frac14+\frac1{16}+\frac14=\frac{25}{16}$. $r[1]=1(-\frac12)+(-\frac12)(\frac14)+(\frac14)(-\frac12)=-\frac34$. $r[2]=1\cdot\frac14+(-\frac12)(-\frac12)=\frac12$. $r[3]=1(-\frac12)=-\frac12$, and $r=0$ for $|l|\ge4$.

ARMA(1,1): write $x[n]=i[n]+\beta\,i[n-1]-\alpha\,x[n-1]$ and read $\beta$ and $\alpha$ (the sign of $\alpha$ flips). Also $H(z)=\dfrac{1+\beta z^{-1}}{1+\alpha z^{-1}}$ reads off the same way. Then:
1. $P=\sigma_i^2\dfrac{1+\beta^2+2\beta c}{1+\alpha^2+2\alpha c}$. Why: $|1+\beta e^{-j\theta}|^2$ over $|1+\alpha e^{-j\theta}|^2$.
2. $d=\beta-\alpha$, $r[0]=\sigma_i^2\left(1+\dfrac{d^2}{1-\alpha^2}\right)$, $r[l]=\sigma_i^2(-\alpha)^{l-1}\left(d-\dfrac{\alpha d^2}{1-\alpha^2}\right)$ for $l\ge1$. Why: the MA weights of $x$ are $1$ then $(-\alpha)^{j-1}d$, and lag products are geometric sums.

Example nov22-3c–3e: $x[k]=i[k]-i[k-1]+\frac34x[k-1]$ has both $x$ and $i$, so ARMA(1,1). Read $\beta=-1$, and $-\alpha=\frac34$ gives $\alpha=-\frac34$, $\sigma_i^2=\frac78$. PSD: numerator $1+1-2c=2-2c$, denominator $1+\frac9{16}-\frac32c=\frac{25-24c}{16}$, so $P=\frac78\cdot\frac{16(2-2c)}{25-24c}=\dfrac{28(1-c)}{25-24c}$ (answer 3d). For $r$: $d=-1+\frac34=-\frac14$, $\frac{d^2}{1-\alpha^2}=\frac{1/16}{7/16}=\frac17$, so $r[0]=\frac78\cdot\frac87=1$. Bracket: $-\frac14-(-\frac34)\cdot\frac17=-\frac17$, so $r[l]=\frac78(\frac34)^{l-1}(-\frac17)=-\frac18(\frac34)^{|l|-1}$ (answer 3e).

**F. Plot matching.** Do not judge shapes. Compute the height at $\theta=0$ ($c=1$) and at $\theta=\pi$ ($c=-1$), then match.
- apr25: correlogram $1.125$ at 0, $2.125$ at $\pi$ (from $2-\frac12c-\frac38\cos2\theta$); AR(1) $\frac{126}{81}\approx1.56$ and $\frac{126}{49}\approx2.57$; MA(1) $1.5$ and $2.5$. Key: option (a) = Plot D.
- apr24: correlogram $\frac{25}{16}-\frac32+1-1=\frac1{16}$ at 0, and $\frac{25}{16}+\frac32+1+1=\frac{81}{16}$ at $\pi$; AR(2) $\approx0.69$ at 0 and $\approx5.6$ at $\pi$. Key: (c) = Plot B.

**G. Wiener filter (jan19-4).** Notation: $r_x$ is the autocorrelation of the filter input, $\rho_{ex}[\tau]=E\{e[k]x[k-\tau]\}$ the cross-correlation with the reference $e$, $\mathbf w=[w_0,w_1]$ the filter weights.
1. Solve $\begin{bmatrix}r_x[0]&r_x[1]\\r_x[1]&r_x[0]\end{bmatrix}\mathbf w=\begin{bmatrix}\rho_{ex}[0]\\\rho_{ex}[1]\end{bmatrix}$. Why: the best error is uncorrelated with the input (orthogonality).
2. $J_{min}=\sigma_e^2-\mathbf p^T\mathbf w$, with $\mathbf p$ the right-hand vector. Why: the filter removes exactly $\mathbf p^T\mathbf w$ of the reference power.
3. If $H(z)\neq1$, the filter input is $g=h*x$: for $H=1-2z^{-1}$, $g[k]=x[k]-2x[k-1]$, so $r_g[0]=5r_x[0]-4r_x[1]$, $r_g[1]=5r_x[1]-2r_x[0]-2r_x[2]$, $\rho_{eg}[\tau]=\rho_{ex}[\tau]-2\rho_{ex}[\tau+1]$. Why: substitute the definition and shift the index.

For $x[k]=i[k]+\frac12x[k-1]$ (AR(1)): $r_x[0]=\frac{\sigma_i^2}{1-1/4}=\frac13$, $r_x[l]=\frac13(\frac12)^{|l|}$, so $r_x[1]=\frac16$, $r_x[2]=\frac1{12}$. Given $\rho_{ex}=(\frac23,\frac56,\frac5{12})$, $\sigma_e^2=\frac73$.

Example (a), $H=1$: $\frac13w_0+\frac16w_1=\frac23$ and $\frac16w_0+\frac13w_1=\frac56$. Multiply by 6: $2w_0+w_1=4$, $w_0+2w_1=5$, so $w_0=1$, $w_1=2$. $J=\frac73-(\frac23\cdot1+\frac56\cdot2)=\frac73-\frac73=0$.

Example (b), $H=1-2z^{-1}$: $\rho_{eg}[0]=\frac23-\frac53=-1$, $\rho_{eg}[1]=\frac56-\frac56=0$, $r_g[0]=\frac53-\frac23=1$, $r_g[1]=\frac56-\frac16-\frac23=0$. The matrix is the identity, so $\mathbf w=(-1,0)$ and $J=\frac73-(-1)(-1)=\frac43$.

**H. Theory and true/false.**
- Residual error variance never rises as $p$ grows (more parameters fit at least as well). Risk: overfitting, the model fits the noise and creates spurious peaks.
- Fix: AIC $=N\ln\hat\sigma^2+2p$ (MDL, FPE similar). First term = fit quality, $2p$ = penalty per parameter. Choose the order with the minimum: the error keeps falling slowly, the penalty grows linearly.
- Any spectrum, even one with deep MA nulls, is approximated by an AR model of high enough order (AR($\infty$) in theory).
- Linear models compress data: a few coefficients replace $N$ samples. True.
- MA($q$) $r$ has values at lags $0..q$, that is $q+1$ values, nonzero only there. "Length $q$" is false.
- ARMA autocorrelation matrix is not diagonal, since $r[1]\neq0$ in general. False.
- MA Yule–Walker equations are non-linear in $b$; AR ones are linear. True.
- jan19-1d answer: C and D.

## 3.3 · Periodogram, Bartlett, Welch, windows

Symbols: $N$ = number of samples in the data record. $P$ = true PSD value. $r[k]$ = autocorrelation at lag $k$ (similarity of the signal with itself $k$ samples later). $\hat r$ = estimate of $r$. $\theta$ = normalised angle frequency. $K$ = number of segments averaged. $M$ = window or segment length. $L$ = DFT length.

**Estimators: idea, bias, variance** (use this list to fill any table)
- **Periodogram**: $\frac1N|\text{DFT of data}|^2$, one segment of all $N$ samples. Variance $\approx P^2$, does not shrink with $N$, so not consistent. Asymptotically unbiased.
- **Correlogram**: DFT of $\hat r[k]$, lags up to $N-1$. Same bias and variance as the periodogram.
- **Bartlett**: $K$ **non-overlapping** segments of length $M=N/K$, periodograms averaged. Variance $\approx P^2/K$. Bias larger for shorter $M$ (resolution $\approx2\pi/M$).
- **Welch (WOSA)**: $K$ **overlapping, windowed** segments, averaged. Variance below the periodogram but above Bartlett: neighbouring segments share samples, so they are correlated and the $1/K$ gain is lost. Bias above the periodogram, below Bartlett (segments are longer).
- **Blackman–Tukey (BT)**: window $\hat r[k]$ with a short lag window $M<L$, then DFT. Consistent: variance $\to0$. Bias grows for shorter $M$.
- **Parametric (AR/MA/ARMA)**: $P(e^{j\theta})=\sigma^2|B|^2/|A|^2$. $\sigma^2$ = noise variance, $A$ and $B$ = model polynomials.

Consistent: BT, Bartlett, Welch (only as $K\to\infty$). Average periodograms: Bartlett, Welch. FT of $r$: correlogram, BT. "Bias $\propto P^2$": none.

**Recipe A: Welch count and variance ratio** (jun26-3b: $N=1000$, $L=200$, 50% overlap). Use when the question gives $N$, $L$ and overlap and asks for $K$ or a variance ratio.
1. Overlap in samples = overlap% $\times L$, the samples two neighbours share. Story: 50% of 200 is 100 shared samples.
2. Step $D=L-\text{overlap}$, the distance between segment starts. $D=200-100=100$.
3. $K=\frac{N-L}{D}+1$. Segments start at 0, 100, 200, ... and the last must end by sample $N$. Story: after the first start, 800 samples remain, each step moves 100, so $800/100=8$ more starts. Total $K=8+1=9$. This answers "how many segments".
4. Variance ratio: $K$ independent periodograms, each with variance $P^2$, averaged give variance $P^2/K$ (an average of $K$ independent items has $1/K$ of the variance). Ratio $=1/K=1/9\approx0.11$. This answers the variance line.

**Recipe B: energy or power** (apr25-3a, q2-24-3a). Use when a signal $x(t)$ or $x[n]$ is given. Not for PSD estimators.
1. Does the signal die out (go to 0) or have finite length? Yes: **energy**, because the energy $E$ (total of $|x|^2$ over all time) is finite only if the signal fades. No (constant, sine, cos, $\cos t\,u(t)$ keep oscillating): **power**, because $E$ would be infinite, so use the average power $\bar P$ instead.
2. Energy $E=\sum|x[n]|^2$ (integral for $t$). Power $\bar P$ = average of $|x|^2$ over time.

Story (energy): $x[n]=e^{-n}$ for $n\ge0$ decays, so energy. $E=\sum_{n=0}^{\infty}e^{-2n}$. Each term is $q^n$ with $q=e^{-2}\approx0.135$, a geometric series worth $\frac1{1-q}=\frac1{0.865}\approx1.16$. Since $E$ is finite, $\bar P=0$ (finite energy spread over infinite time). Answers item 2 of apr25-3a.

Story (power): $x(t)=A\sin\omega t$ never dies, so $E=\infty$. Over one period $\sin^2=(1-\cos2\omega t)/2$, and the cosine averages to 0, so $\bar P=A^2/2$. Answers item 1.

Table: $e^{-t}u(t)$, $5$ on $-2\le t\le2$, $5e^{-2|t|}$ are energy. $\cos(t)u(t)$ is power.

**Recipe C: match a description to a method** (apr25-3c, apr24-3a, nov19-1c). Use when a description is given and you name the method(s). Several can fit; repeats allowed. Match the key phrase:
- "non-overlapping segments, average periodograms" = Bartlett. "overlapping segments" = Welch.
- "DFT of estimated autocorrelation, window of length $M<L$ applied to it" = BT (the window makes it not a plain correlogram).
- "modulus squared of DFT, divided by $N$" = periodogram. "DFT of $\hat r$" with no window = correlogram.
- "model with $|B|^2/|A|^2$" = AR/MA/ARMA.

Story (apr25-3c): row 1 says non-overlapping and averaging periodograms, so Bartlett. Row 5 has the same words but "overlapping", so Welch. The single word decides.

**Recipe D: which statement is TRUE** (apr25-3b, nov22-3a, jan20-1b, jan19-1c). Use for options a–d about bias, variance, Bartlett, Welch.
1. Pick the claim in each option and check it against the list above.
2. Reject an option if any part is false, even if the first part is true.
3. Some questions have several true options (jan19-1c: A and C).

Story (nov22-3a): (a) Bartlett, variance $\propto1/K$ (true), bias increases (true): TRUE. (b) WOSA with $1/K$: false, overlap correlates segments. (c) bias decreases: false, shorter segments raise bias. Answer (a).

**Recipe E: windows and zero-padding** (nov22-3b, jan20-1c). Use for lobes, leakage, padding.
- Main-lobe width sets **resolution** (wide = worse). Side-lobe height sets **leakage** (high = worse). Rectangular window: narrowest main lobe, highest side lobes. Longer window: narrower lobe.
- Zero-padding $N$ samples to length $L$: the DFT samples the same curve at $L$ points, step $2\pi/L$. Denser dots, no better resolution.

Story (jan20-1c, option C): a wide main lobe means worse resolution: true. A is wrong (side lobes drive leakage, not resolution). B is wrong (high side lobes mean more leakage). D is wrong (main lobe drives resolution, not leakage). Answer C.

Story (nov22-3b, option d): padding to $L$ samples samples at step $2\pi/L$, not $2\pi/N$, so false. Answer (b).

**Recipe F: AR order $p$** (jun26-3e). Use for AR model order and criteria.
1. The residual error (variance $\sigma^2$) always falls as $p$ grows, so it cannot choose $p$. Too high $p$ = **overfitting**: the model fits noise and creates spurious peaks.
2. Use AIC $=N\ln\hat\sigma^2+2p$ or FPE $=\frac{N+p}{N-p}\hat\sigma^2$. The first term is the error (falls with $p$), the $2p$ is a penalty (rises with $p$). Compute for each $p$ and take the minimum: beyond it the penalty grows faster than the error falls.
3. Any PSD is approximated by an AR model of **high enough order**.

**Recipe G: plot matching** (jan22-3a). Use for transforms shown as plots A–D.
Story: $f/f_s=25/50=\tfrac12$, so the angle is $2\pi\cdot\tfrac12=\pi$. An infinite cosine gives two spikes at $\pm\pi$: plot B (item 1).
A rectangular window multiplies the cosine by a box. The FTD of a box is a smooth main lobe with side lobes: plot D (item 2).
Padded DFT: $N+M=24+12=36$ points on the same smooth curve, so dense dots: C (item 3). Unpadded: $N=24$ points, few dots: A (item 4). Answer (b).

**Traps (true/false)**
- False: longer data cuts leakage (it narrows lobes; leakage is set by side lobes). False: a window improves resolution (rectangular is best there). False: Bartlett zero-pads (it splits the record). False: periodogram beats correlogram (same). False: a window changes the periodogram's variance (it changes bias). False: zero-padding increases resolution.
- True: bias affects both deterministic and stochastic signals.

## 4.1 · Likelihood-ratio test

**Use this recipe when** the question gives the full pdf (a formula in $x$) of the observation under both hypotheses and asks for a decision rule, a cut, or $P_{FA}$, $P_D$. One sample or $N$ samples both work. Do not use it when the question only gives means, standard deviations and a table of areas: go to Type 7.

**Symbols in plain words**
- $x$: the number you measure. $x_n$: sample number $n$ (the $n$-th measurement), $n=0,\dots,N-1$. $N$: how many samples you have.
- $\mathcal H_0$: "nothing there" (null hypothesis). $\mathcal H_1$: "signal there" (alternative).
- $p(x\mid\mathcal H_i)$: the pdf (height of the curve) of $x$ if hypothesis $i$ is true.
- $L$: likelihood ratio = height of the $\mathcal H_1$ curve ÷ height of the $\mathcal H_0$ curve at your $x$.
- $\lambda$, $\eta$ or $\gamma$ (letters vary): the **bar**, a number given in the question. If an $L$-test says "threshold $\gamma=1$", that is the bar on $L$, not a cut in $x$.
- **cut** ($x_{th}$, $\gamma'$, $y_{th}$): the value of $x$ where $L$ equals the bar. Your decision flips at the cut.
- $P_{FA}$: probability of false alarm = $P(\text{decide }\mathcal H_1\mid \mathcal H_0\text{ true})$ = $\mathcal H_0$ area in the "decide $\mathcal H_1$" region.
- $P_D$: probability of detection = $\mathcal H_1$ area in the same region. $P_M=1-P_D$ (missed detection) = the rest of the $\mathcal H_1$ curve.
- $Q(t)$: area under the standard Gaussian (mean 0, std 1) to the right of $t$.

**Reading the exam arrows.** $\overset{\mathcal H_1}{\underset{\mathcal H_0}{\gtrless}}$: decide $\mathcal H_1$ when the quantity is bigger. $\underset{\mathcal H_1}{\overset{\mathcal H_0}{\gtrless}}$ (nov22 uses this): decide $\mathcal H_1$ when it is smaller. The side of the sign tells you the hypothesis.

**Recipe**
1. Write $L=\frac{(\mathcal H_1\text{ formula})}{(\mathcal H_0\text{ formula})}$ with the numbers in. For $N$ independent samples the joint pdf is the product of single-sample pdfs, so $L$ is the product of the $N$ single-sample ratios.
2. Simplify with legal algebra: $x^a/x^b=x^{a-b}$; $e^a/e^b=e^{a-b}$; $\prod_n e^{-|x_n|}=e^{-\sum_n|x_n|}$ (exponents add); $c\cdot c\cdots c=c^N$; equal factors top and bottom cancel.
3. Compare with the bar: $L\gt\lambda$. Take $\ln$ of both sides: legal because $\ln$ is increasing, so the direction ">" survives. Use $\ln e^a=a$, $\ln c^N=N\ln c$, $\ln\frac1a=-\ln a$.
4. Isolate $x$ (or $x^2$, or $\sum x_n^2$) by moving constants across. Multiplying or dividing by a **negative** number flips ">" to "<" (because the order of numbers reverses when you flip their sign).
5. Check the direction: put one $x$ on each side into the original $L$. If $L\gt$ bar there, that side is $\mathcal H_1$. This catches sign mistakes.
6. Probabilities: $P_{FA}$ = integral of the $\mathcal H_0$ pdf over the decide-$\mathcal H_1$ region; $P_D$ = same integral for $\mathcal H_1$. If the region is $|x|\gt\gamma$ it has two tails: multiply by 2 when the curves are symmetric, because each tail has the same area.

Integrals: $\int_t^\infty ke^{-ay}dy=\frac ka e^{-at}$; $\int_0^g ke^{-ay}dy=\frac ka(1-e^{-ag})$.

**Type 1 · two power-law pdfs, one sample, bar given (apr25 4a).** Exam: "what value of $x$ for which $\mathcal H_1$ should be accepted?" → steps 1, 2, 3, 4.
- Here $p(x\mid\theta)=k_1\theta x^{k_2\theta-1}$, with $k_1=1$, $k_2=2$. $\theta$ is the unknown parameter; $\theta_0=3$ under $\mathcal H_0$ and $\theta_1=6$ under $\mathcal H_1$.
- Step 1: under $\mathcal H_0$, $1\cdot3\cdot x^{2\cdot3-1}=3x^5$. Under $\mathcal H_1$, $1\cdot6\cdot x^{2\cdot6-1}=6x^{11}$. So $L=\frac{6x^{11}}{3x^5}=2x^6$ ($x^{11}/x^5=x^6$).
- Step 3: bar $\lambda=0.2$, so $2x^6\gt0.2$.
- Step 4: divide by 2 (positive, no flip): $x^6\gt0.1$, so $x\gt0.1^{1/6}$. Since $\ln0.1=-2.303$, $\ln x\gt-2.303/6=-0.384$, $x\gt e^{-0.384}=0.68$.
- Answer: $\mathcal H_1$ is accepted for $0.68\lt x\lt1$ (the data range of the question).

**Type 2 · two one-sided pdfs (Gaussian vs exponential), bar $\gamma=1$ (apr24 4b, jan22 4b/4c).** Exam: "for threshold $\gamma=1$ calculate $P_D$ and $P_{FA}$" → steps 1–6. Here $y$ is the observation, $\mathcal H_0$: $\frac1{\sqrt{2\pi}}e^{-y^2/2}$, $\mathcal H_1$: $\frac14e^{-y/2}$, $y\gt0$.
- Step 1: $L=\frac{\frac14e^{-y/2}}{\frac1{\sqrt{2\pi}}e^{-y^2/2}}=\frac{\sqrt{2\pi}}4e^{y^2/2-y/2}$. The constant is $2.507/4=0.627$.
- Step 3: $L\gt1$. Take $\ln$: $\ln0.627=-0.467$, so $-0.467+\frac{y^2}2-\frac y2\gt0$.
- Step 4: multiply by 2 (positive): $y^2-y-0.934\gt0$. The cut solves $y^2-y-0.934=0$: $y=\frac{1\pm\sqrt{1+3.738}}2=\frac{1\pm2.177}2$. The positive root is $y_{th}=1.59$.
- Step 5: at $y=0$, $L=0.627\lt1$ → $\mathcal H_0$. At $y=3$, $L=0.627e^{4.5-1.5}=0.627\cdot20.1=12.6\gt1$ → $\mathcal H_1$. So decide $\mathcal H_1$ for $y\gt1.59$.
- Step 6: $P_{FA}=\int_{1.59}^\infty\frac1{\sqrt{2\pi}}e^{-y^2/2}dy=Q(1.59)=0.0559\approx0.056$ (read from the table). $P_D=\int_{1.59}^\infty\frac14e^{-y/2}dy=\frac14\cdot2e^{-0.795}=\frac12\cdot0.452=0.226\approx0.23$. $P_M=1-0.23=0.77$.
- Sketch: $\mathcal H_0$ is a bell peaking at 0.40 at $y=0$; $\mathcal H_1$ starts at $0.25$ at $y=0$ and decays. Mark $y=1.59$, shade the $\mathcal H_0$ tail right of it ($P_{FA}$); $P_M$ is the $\mathcal H_1$ area left of it.
- Variant jan22 (pdf with $|y|$, two-sided): same algebra with $|y|$ gives the cut $|y|\gt1.588$. Both tails count: $P_{FA}=2\cdot0.056=0.11$, $P_D=2\cdot0.226=0.45$.

**Type 3 · Rayleigh pdfs with two scales (jun26 4b, q1-23 4c/4d).** Pdf $\frac{x}{\sigma^2}e^{-x^2/2\sigma^2}$, where $\sigma$ is the scale. Read $\sigma^2$ from the exponent: $e^{-x^2/8}$ means $2\sigma^2=8$, so $\sigma^2=4$.
- Worked numbers (q1-23): $\mathcal H_0$: $xe^{-x^2/2}$, so $\sigma_0^2=1$. $\mathcal H_1$: $\frac x4e^{-x^2/8}$, so $\sigma_1^2=4$. Bar $\lambda=1$.
- Step 1: $L=\frac{\frac x4e^{-x^2/8}}{xe^{-x^2/2}}$. The $x$ top and bottom cancel (equal factors). The exponents subtract: $-\frac{x^2}8+\frac{x^2}2=\frac{3x^2}8$. So $L=\frac14e^{3x^2/8}$.
- Step 3: $L\gt1$; $\ln$: $\ln\frac14+\frac{3x^2}8\gt0$, so $\frac{3x^2}8\gt\ln4=1.386$.
- Step 4: $x^2\gt\frac83\cdot1.386=3.70$, so $x\gt\lambda'=1.92$. Check: $x=3$ gives $L=\frac14e^{3.375}=7.3\gt1$ → $\mathcal H_1$ ✓.
- Step 6: $P_{FA}=P(x\gt1.92\mid\mathcal H_0)=e^{-1.92^2/2}=e^{-1.84}\approx0.16$ (Rayleigh: area right of $t$ is $e^{-t^2/2\sigma^2}$). $P_M=P(x\lt1.92\mid\mathcal H_1)=1-e^{-1.92^2/8}=1-e^{-0.46}\approx0.37$.
- Jun26 general form (bar $\eta$, $\sigma_1\gt\sigma_0$): steps 1–4 give $\frac{x^2}2\big(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\big)\gt\ln\frac{\eta\sigma_1^2}{\sigma_0^2}$. Since $\frac1{\sigma_0^2}-\frac1{\sigma_1^2}=\frac{\sigma_1^2-\sigma_0^2}{\sigma_0^2\sigma_1^2}$, the cut is $\gamma=\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{\eta\sigma_1^2}{\sigma_0^2}}$. Decide $\mathcal H_1$ for $x\gt\gamma$.
- Separation (exam: "discuss how separation affects $P_D$"): $P_{FA}=e^{-\gamma^2/2\sigma_0^2}$, $P_D=e^{-\gamma^2/2\sigma_1^2}=P_{FA}^{\sigma_0^2/\sigma_1^2}$. Larger $\sigma_1$ relative to $\sigma_0$ makes the power $\sigma_0^2/\sigma_1^2$ smaller, so $P_D$ is higher at the same $P_{FA}$: less overlap.

**Type 4 · Laplace pdfs, $N$ samples (nov22 4c/4d/4e).** Pdfs $\frac12e^{-|x|}$ and $e^{-2|x|}$. Exam: "show the test takes the form $\sum|x_n|\lessgtr\gamma'$ and find $\gamma'$" → steps 1–4.
- Step 1: per sample, $\frac{e^{-2|x_n|}}{\frac12e^{-|x_n|}}=2e^{-|x_n|}$. Multiplying $N$ such factors gives $2^N e^{-\sum_n|x_n|}$.
- Step 3: $2^Ne^{-\sum|x_n|}\gt\lambda$; $\ln$: $N\ln2-\sum|x_n|\gt\ln\lambda$.
- Step 4: multiply by $-1$ → flip: $\sum_n|x_n|\lt N\ln2-\ln\lambda=\gamma'$. Decide $\mathcal H_1$ when the sum is smaller than $\gamma'$.
- $N=1$, $P_{FA}=0.1$ (4e). Let $y=|x|$: $\mathcal H_0$ is $e^{-y}$, $\mathcal H_1$ is $2e^{-2y}$, and we decide $\mathcal H_1$ for $y\lt\gamma'$. Step 6 backwards: $P_{FA}=\int_0^{\gamma'}e^{-y}dy=1-e^{-\gamma'}=0.1$, so $e^{-\gamma'}=0.9$ and $\gamma'=-\ln0.9=0.105$.
- Then $P_D=\int_0^{\gamma'}2e^{-2y}dy=1-e^{-2\gamma'}=1-0.9^2=1-0.81=0.19$. $(e^{-\gamma'})^2=e^{-2\gamma'}$ is the reason for $0.9^2$.

**Type 5 · exponential pdfs (jan20 5a/5b/5c).** $\mathcal H_0$: $\lambda_0e^{-\lambda_0x}$; $\mathcal H_1$: $\lambda_1e^{-\lambda_1x}$, with $\lambda_1\gt\lambda_0$ ($\lambda$ is a rate, larger means shorter tail). Exam: "for $\lambda_1=2$, $\lambda_0=0.1$, mark $x_{th}$ for $L=1$" → steps 1–4.
- Step 1: $L=\frac{2e^{-2x}}{0.1e^{-0.1x}}=20e^{-1.9x}$ (exponents subtract: $-2x+0.1x$).
- Step 3: $20e^{-1.9x}\gt1$; $\ln$: $\ln20-1.9x\gt0$.
- Step 4: $1.9x\lt\ln20$, dividing by positive 1.9 keeps the direction: $x\lt x_{th}=\frac{2.996}{1.9}=1.58$. Decide $\mathcal H_1$ for small $x$.
- Step 5 check: $x=0.5$ gives $L=20e^{-0.95}=7.7\gt1$ → $\mathcal H_1$ ✓.
- Step 6 (exam hint: $P(x\lt t)=1-e^{-\lambda t}$): $P_D=1-e^{-2\cdot1.58}=1-0.043=0.957$; $P_{FA}=1-e^{-0.1\cdot1.58}=1-0.854=0.146$.
- Exam "find $\lambda_1$ for $P_D=0.9$ when $P_{FA}=0.1$, $\lambda_0=0.1$" → invert. First the cut from $P_{FA}$: $1-e^{-0.1x_{th}}=0.1$, so $x_{th}=-\ln0.9/0.1=1.054$. Then $P_D$: $1-e^{-\lambda_1x_{th}}=0.9$, so $e^{-\lambda_1x_{th}}=0.1$ and $\lambda_1=\frac{\ln10}{1.054}=2.19$.
- ROC (exam: plot $P_D$ vs $P_{FA}$ for $\lambda_1=2.19$): for each chosen $P_{FA}$ compute $x_{th}=-\ln(1-P_{FA})/\lambda_0$, then $P_D=1-e^{-\lambda_1x_{th}}$. $P_{FA}=0.5$: $x_{th}=6.93$, $P_D\approx1$. $P_{FA}=0.9$: $x_{th}=23.0$, $P_D\approx1$. A bigger $\lambda_1$ bends the curve further to the top-left; a smaller one lies lower. All curves lie above the diagonal $P_D=P_{FA}$.

**Type 6 · two zero-mean Gaussians, different variances (pe21 4b, nov19 4a/4b/4c).** Decide $\mathcal H_1$ for $|x|\gt\gamma$ (large $|x|$ favours the wider $\sigma_1$).
- Single sample, nov19 (b): $\sigma_1=3\sigma_0$, cut $x_{th}=\sigma_1$. Table: $\Pr(0\le x\le\sigma)=0.341$, so $\Pr(|x|\le\sigma)=0.682$.
- $P_{FA}$: the cut $\sigma_1=3\sigma_0$ is 3 standard deviations of $\mathcal H_0$: $P_{FA}=1-2(0.341+0.136+0.021)=1-0.996=0.004$.
- $P_D$: the same number is 1 standard deviation of $\mathcal H_1$: $P_D=1-2(0.341)=0.318$.
- Trap: convert the cut to each hypothesis' own $\sigma$. Equivalently $P_{FA}=2Q(\gamma/\sigma_0)$, $P_D=2Q(\gamma/\sigma_1)$.
- Written form (nov19 a): $P_D=\int_{|x|\gt\gamma}p(x\mid\mathcal H_1)dx$, $P_{FA}=\int_{|x|\gt\gamma}p(x\mid\mathcal H_0)dx$.
- $N$ samples (pe21, nov19 c): each ratio is $\frac{\sigma_0}{\sigma_1}e^{\frac12(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})x_n^2}$. Product and $\ln$: $N\ln\frac{\sigma_0}{\sigma_1}+\frac12\big(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\big)\sum_n x_n^2\gt\ln\eta$. Decide $\mathcal H_1$ when $\sum_n x_n^2\gt\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\big(\ln\eta-N\ln\frac{\sigma_0}{\sigma_1}\big)$. Use $x_n^2$, not $x_n$.

**Type 7 · Gaussian with a mean and std (jan19 3b).** Exam gives a table of $\operatorname{erf}$ values. Assume decide $\mathcal H_1$ for $x\gt X$ (the exam's threshold).
- $\mathcal H_0$ is $N(0,1)$: $P_{FA}=P(x\gt X\mid\mathcal H_0)=Q(X)$.
- $\mathcal H_1$ is $N(\mu_1,\sigma_1)$: standardise by subtracting the mean and dividing by the std: $P_D=Q\big(\frac{X-\mu_1}{\sigma_1}\big)$. Use $Q(-t)=1-Q(t)$.
- $(X,\mu_1,\sigma_1)=(1,3,1)$: $P_{FA}=Q(1)=0.159$; $P_D=Q(-2)=1-Q(2)=1-0.023=0.977$.
- $(1,3,2)$: $P_D=Q(-1)=1-0.159=0.841$. $(1,1,1)$: $P_D=Q(0)=0.5$. $(2,3,1)$: $P_{FA}=Q(2)=0.023$, $P_D=Q(-1)=0.841$.

**Other exam phrasings → which step**
- "derive the log-likelihood ratio test" → steps 1–4 with $\ln$; state the final sum and the inequality.
- "roughly plot the pdfs and mark the threshold" → draw both curves; the cut is where they cross ($L=1$).
- "indicate $P_{FA}$ and $P_M$ in the plot" → shade the $\mathcal H_0$ area and the $\mathcal H_1$ area on the wrong side of the cut.
- "for $P_{FA}=0.1$ calculate the threshold" → invert step 6: get the cut from $P_{FA}$ first.
- "show the LR can be written as $x\lessgtr\lambda'$" → steps 1–4 only; $\lambda'$ is the cut.

**Traps**
- $\ln$ never flips the direction; only multiplying or dividing by a negative does.
- $P_D\gt P_{FA}$ for any useful test; if you get $P_D\lt P_{FA}$, you have the decision direction backwards (step 5).
- $P_M=1-P_D$, not $1-P_{FA}$.
- Symmetric $|x|\gt\gamma$: two tails, so double each area.

## 4.2 · Bayesian detection

**Symbols.** $H_0$ = null hypothesis (nothing sent), $H_1$ = alternative (signal sent). $P_0,P_1$ = priors: the chance of $H_0$ and of $H_1$ before looking at the data. $C_{ij}$ = cost of deciding $i$ when $j$ is true: $C_{10}$ = false alarm cost, $C_{01}$ = miss cost, $C_{00},C_{11}$ = cost of a correct decision (usually 0). $p_0(x),p_1(x)$ = probability density of the data $x$ under $H_0$ and under $H_1$. $\lambda$ (lambda) = threshold on the likelihood ratio $p_1/p_0$ (same role as $\eta$ in 4.1). $y$ = scalar test statistic, $\gamma''$ = its threshold value. $P_D$ = probability of detection (decide $H_1$ when $H_1$ is true), $P_{FA}$ = probability of false alarm (decide $H_1$ when $H_0$ is true), $P_M$ = probability of miss $=1-P_D$. $P_e$ = total error probability.

**Recipe A · priors and costs given, densities given (Bayes likelihood-ratio test).**
Use this when the question gives $P_0,P_1$, costs, and the densities $p_0,p_1$. Use recipe B if it gives posteriors instead.

1. Compute $\lambda=\frac{(C_{10}-C_{00})P_0}{(C_{01}-C_{11})P_1}$. Why: deciding $H_1$ has average cost $C_{10}P_0p_0+C_{11}P_1p_1$, deciding $H_0$ has $C_{00}P_0p_0+C_{01}P_1p_1$; picking the smaller one minimises the Bayes risk (average cost), and this is the threshold it gives.
2. If correct costs are 0 and both errors cost the same, $\lambda=P_0/P_1$. If the priors are also equal, $\lambda=1$, which is the maximum-likelihood rule.
3. Decide $H_1$ when $p_1(x)/p_0(x)>\lambda$. Why: step 1 already contains the priors and costs, so compare only the likelihood ratio.
4. Put $\lambda$ as $\eta$ into the threshold formula of the matching test (e.g. the Rayleigh threshold of 4.1). Why: that formula was derived for a likelihood-ratio threshold $\eta$.

*Example (jun26-4c).* Priors $P_0=0.9$, $P_1=0.1$; errors cost the same, correct costs 0. Step 2: $\lambda=P_0/P_1=0.9/0.1=9$. Step 4: with $\eta=9$ the Rayleigh threshold is $x>\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{9\sigma_1^2}{\sigma_0^2}}$. This expression is the answer to "when should the sensor accept $H_1$" (x = the measured value).

**Recipe B · posteriors given.**
Use this when the question gives $P(H_0|x)$, $P(H_1|x)$ or a ratio of them ("posterior is 5 times smaller").

1. Form $P(H_1|x)/P(H_0|x)$. Why: the posterior already contains priors and likelihoods, so no $p_1/p_0$ is needed.
2. Decide $H_1$ if this ratio $>\frac{C_{10}-C_{00}}{C_{01}-C_{11}}$. Why: same cost rule as recipe A, with the priors already absorbed.

*Example (apr25-4c).* $C_{01}=100C_{10}$, $C_{11}=C_{00}=0$, so the right side is $\frac{C_{10}}{100C_{10}}=0.01$. The $H_0$ posterior is 5 times smaller than the $H_1$ posterior, so $P(H_1|x)/P(H_0|x)=5$. Since $5>0.01$, decide $H_1$. The question asks "should the student fail": the student fails when $H_1$ is accepted, so **yes**.

**Recipe C · threshold where weighted densities meet ($\gamma''$).**
Use this when asked for the value $y$ where $p_1P_1=p_0P_0$.

*Example (nov22-4f):* $p_0=e^{-y}$, $p_1=2e^{-2y}$, $P_0=0.4$, $P_1=0.6$.

1. Write equality: $2e^{-2y}\cdot0.6=e^{-y}\cdot0.4$. Why: the question defines the threshold as this equality.
2. Divide both sides by $e^{-y}$ (allowed, it is positive). Since $e^{-2y}/e^{-y}=e^{-y}$, we get $1.2e^{-y}=0.4$.
3. So $e^{-y}=0.4/1.2=\frac13$.
4. Take logs: $y=\ln3\approx1.10$. General rule: $e^{-y}=1/k$ gives $y=\ln k$.
5. Direction: for small $y$, $e^{-y}>\frac13$, so $p_1P_1>p_0P_0$, which means $H_1$. Decide $H_1$ when $y<\ln3$.

**Recipe D · miss and false alarm from tails (exponential densities).**
Use this when the question asks $P_M$ and $P_{FA}$ for the test of recipe C. $P_{FA}$ integrates $H_0$'s density over the region where you decide $H_1$; $P_M$ integrates $H_1$'s density over the region where you decide $H_0$.

For a density $ce^{-cy}$ ($y\ge0$), integrating gives $P(y>a)=e^{-ca}$ and $P(y<a)=1-e^{-ca}$.

*Example (nov22-4g), continuing recipe C.*

1. $P_{FA}=P(y<\ln3;H_0)$, $H_0$ has $c=1$: $1-e^{-\ln3}=1-\frac13=\frac23$.
2. $P_M=P(y>\ln3;H_1)$, $H_1$ has $c=2$: $e^{-2\ln3}=(\frac13)^2=\frac19$.
3. If the question asks the total error with priors: $P_{FA}P_0=\frac23\cdot0.4=\frac4{15}$, $P_MP_1=\frac19\cdot0.6=\frac1{15}$, $P_e=\frac5{15}=\frac13$.

**Recipe E · Gaussian $P_D$, $P_{FA}$ from an erf table (pe21-4a).**
Use this when the densities are Gaussian with given $\sigma$ and a table of $\text{erf}$ is supplied. $\mu$ = mean under $H_1$ (mean under $H_0$ is 0). $y_{th}$ = threshold.

1. The CDF is $P(y<y_{th};\mu)=0.5\left(1+\text{erf}\frac{y_{th}-\mu}{\sigma\sqrt2}\right)$. With $\sigma=1$, set $x=y_{th}-\mu$ and look up $\text{erf}(x/\sqrt2)$ in the table.
2. The exceedance probability is the complement: $P=1-0.5(1+\text{erf}(x/\sqrt2))$. Why: "decide $H_1$" means $y>y_{th}$, and the complement of $y<y_{th}$ is $y>y_{th}$.
3. $P_D$: use $x=y_{th}-\mu$. $P_{FA}$: use $\mu=0$, so $x=y_{th}$.

*Example* $(y_{th},\mu)=(1,1)$. $P_D$: $x=0$, erf $=0$, so $1-0.5(1+0)=0.5$. $P_{FA}$: $x=1$, erf$(1/\sqrt2)=0.683$, so $1-0.5(1.683)=0.1585$.
Exam's full table, as $(y_{th},\mu)$: $P_D$, $P_{FA}$: $(-1,1)$: .977, .8415; $(-1,2)$: .9985, .8415; $(0,1)$: .8415, .5; $(0,2)$: .977, .5; $(1,1)$: .5, .1585; $(1,2)$: .8415, .1585; $(2,1)$: .1585, .023; $(2,2)$: .5, .023; $(3,1)$: .023, .0015; $(3,2)$: .1585, .0015.

**Recipe F · decoding the 2×2 table (rows = decision, columns = truth).**
- Decide $H_0$, truth $H_0$: true negative (correct).
- Decide $H_0$, truth $H_1$: miss, false negative, type II error.
- Decide $H_1$, truth $H_0$: false alarm, false positive, type I error.
- Decide $H_1$, truth $H_1$: detection, true positive.

**Multiple-choice rules (4.2).**
- Bayes **minimises** the Bayesian risk (average cost). "Maximised" is false.
- Equal costs for the two errors (1, 10, any equal non-zero value) with correct costs 0 minimise $P_e$. Why: then the cost ratio is 1 and $\lambda=P_0/P_1$ only depends on priors.
- Neyman–Pearson: fix $P_{FA}$, then **maximise** $P_D$ (priors not needed). "Minimise $P_D$" is false.
- Priors: higher $P_0$ raises $\lambda$, harder to decide $H_1$. Higher $P_1$ lowers $\lambda=P_0/P_1$, easier to decide $H_1$. "Higher $P_1$ raises the threshold" is false.
- If every option reads correct (apr25-4b key: no option false), answer "none is false". Check each verb: risk **min**, $P_D$ **max**.
- Matched filter: maximises output SNR; impulse response $h[n]=s[N-1-n]$ (the signal reversed in time, $N$ = signal length). "$h[n]=s[n]$" is false. "Only for uncorrelated noise" is false: it is optimal for white noise, and coloured noise is whitened first, not forbidden.

**ROC curves.** Vertical $P_D$, horizontal $P_{FA}$. Correct curves lie **above** the diagonal ($P_D>P_{FA}$). Curves below mean: $H_0/H_1$ swapped in $L$; CDF used instead of its complement ($P_D=P(y<\gamma)$ instead of $P(y>\gamma)$); or $P_D$ and $P_{FA}$ swapped. A wrong $\sigma$ changes how high the curve is, never which side of the diagonal, so "variance of $H_0$ too high" cannot cause a lower-triangle curve. Bigger $\mu$ (more separation) gives a higher curve.

**t-statistic** $t=\frac{\hat\mu-\mu_0}{\hat\sigma/\sqrt N}$: $\hat\mu$ = estimated mean, $\mu_0$ = mean under $H_0$, $\hat\sigma$ = estimated standard deviation, $N$ = number of samples. Big $|t|$ = evidence against $H_0$. Larger $N$ gives bigger $|t|$; larger $\hat\sigma$ gives smaller $|t|$. $t$ is itself random (it depends on the samples). "Smaller $t$ means $H_0$ less likely" is false: small $t$ means the data look like $H_0$.

**Exam phrasing → step.**
- "when should the sensor accept $H_1$" (priors + densities) → recipe A, steps 1–4.
- "should the student fail" (posteriors, costs) → recipe B.
- "value of $y$ where $p_1P_1=p_0P_0$", "find $\gamma''$" → recipe C.
- "probability of miss and false alarm" for exponentials → recipe D.
- "calculate $P_d$ and $P_{fa}$ for the table" (Gaussian) → recipe E.
- "which statement is TRUE/FALSE" → multiple-choice rules.
- "which expression is not correct" for $t$ → t-statistic bullets.

</div>
</div>
