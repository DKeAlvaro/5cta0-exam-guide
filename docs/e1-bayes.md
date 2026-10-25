# 1.1 Bayes word problems

<div class="meta"><span class="hot">In 7 of the last 7 exams</span><span>0.25–0.3 points</span><span>15 min</span></div>

<figure class="pod"><video src="video/pod_ep5_probability.mp4" poster="video/pod_ep5_probability.jpg" controls playsinline preload="none"></video><figcaption><b>Watch first: podcast episode 5, Block 1: Bayes, joint PDFs, ergodic, factorisation</b> (with sound). Answer every purple YOUR TURN out loud before the countdown ends; pause if you need more time. <a href="podcast.html">All 5 episodes</a>.</figcaption></figure>

## The idea in one minute

Percentages of percentages are confusing. **Counts** are not. Pretend you have exactly 1000 items and follow them:

<div class="widget" data-w="bayes"></div>

That is all there is. The two formulas below are the same steps written with symbols ($P(A\mid B)$ reads "probability of $A$ **given** $B$"):

<div class="key" markdown>

$$P(D)=\sum_k P(D\mid M_k)\,P(M_k)\qquad\qquad P(M_k\mid D)=\frac{P(D\mid M_k)\,P(M_k)}{P(D)}$$

</div>

## How to fight this section with the sheet

Here is the honest bad news: **your A4 sheet has no box for this question type.** Box 1A is the joint PDF, 1B is WSS, 1C is spectral factorisation — the word problems are not on the sheet, and that is deliberate (they need no formulas).

It is also the question that appears in **7 of the last 7 exams**, so you do not want to improvise it. Two things:

1. **Write the recipe below in the margin of your sheet.** You are allowed your own notes on that A4, and this is the single most valuable thing to put there.
2. The **Numbers** and **Calculations** strips at the bottom of the sheet do the arithmetic for you (fractions, $\ln$, $e$).

!!! sheet "Write this in the margin of your sheet — the recipe the sheet does not carry"
    **IF YOU SEE** groups (machines, scanners, students, patients) with counts or shares, a rate inside each group, and a probability is asked.

    1. **Total.** Counts given → items = those counts, total = their sum. Only percentages → pretend total $=1000$ (1 000 000 if a rate is tiny, like 0.0005).
    2. **Items$_k$** $=$ share$_k\times$ total.
    3. **Pick "bad".** Bad $=$ the event asked, or the event after "given / if / found to be / has had / has passed / positive". Asked **NOT** pass when a **pass** rate is given → bad rate $=1-$pass rate.
    4. **Bad$_k$** $=$ bad rate$_k\times$ items$_k$.
    5. **$P(\text{bad})$** $=$ (sum of all bad$_k$) $/$ total.
    6. **$P(k\mid\text{bad})$** $=$ bad$_k$ $/$ (sum of all bad). **Divide by the pile, not by the total.**

    **Wording** (exam word → same step): defective, fail, NOT pass, positive, infected, has TB, actually present → **bad**. pass, sufficient quality, good → the good event. "false positive 3 %" $=$ 3 % **of the healthy** test positive. "detects 95 % when present" $=$ 95 % of the ill test positive. "99 % accurate" $=$ 99 % of the ill **and** 99 % of the healthy classified right. "scans / paints $N$ patients" $=$ that is your count. "mixed at random" $=$ step 5.

Two more sheet places you will need: the **Calculations** strip when the answer is a fraction of a fraction, and the **Numbers** strip for $e^{-1/5}=0.82$-style values. For the yes/no and true/false questions there is no recipe at all — those are one-line definitions, given in exercises 10 and 11 below.

## 1 · June 2026 · 1b — three machines. Read this one with the sheet margin next to you

!!! exam "Resit, June 2026 · 1b · 0.3 p"
    A manufacturing plant has three machines, $M_1$, $M_2$, and $M_3$, that produce microchips. Machine $M_1$ produces 40% of the chips, $M_2$ produces 35%, and $M_3$ produces 25%. The probability that a chip is defective is 2% for $M_1$, 4% for $M_2$, and 5% for $M_3$. The chips from all machines are mixed together randomly before quality control.

    **Please provide only the final answer. The workout will not be checked.**

    1. What is the probability that a randomly selected chip will be defective? [0.15]
    2. If a randomly selected chip is found to be defective, what is the probability that it was produced by machine $M_2$? [0.15]

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    *(The [0.15] marks are the points of each sub-question, not answers.)*

    **Margin step 1 · "Total. Only percentages → pretend total $=1000$."**
    1000 chips. No counts are given, so any total works — 1000 is the easy one.

    ***

    **Margin step 2 · "Items$_k$ $=$ share$_k\times$ total."**
    $M_1$: $0.40\times1000=400$. $M_2$: $0.35\times1000=350$. $M_3$: $0.25\times1000=250$. (Check: $400+350+250=1000$ ✓.)

    ***

    **Margin step 3 · "Pick bad."**
    The question asks "defective", and then "found to be **defective**" — so bad $=$ defective. The rates 2 %, 4 %, 5 % are already defective rates: **no** $1-$ step here.

    ***

    **Margin step 4 · "Bad$_k$ $=$ bad rate$_k\times$ items$_k$."**
    $0.02\times400=8$ · $0.04\times350=14$ · $0.05\times250=12.5$.

    ***

    **Margin step 5 · "$P(\text{bad})=$ sum $/$ total."**
    $8+14+12.5=34.5$ bad chips out of 1000:

    $$P(D)=\frac{34.5}{1000}=\mathbf{0.0345}$$

    ***

    **Margin step 6 · "$P(k\mid\text{bad})=$ bad$_k$ $/$ sum of bad."**
    "Found to be defective" means we are standing **inside the pile of 34.5**, not in the 1000. $M_2$ contributed 14 of them:

    $$P(M_2\mid D)=\frac{14}{34.5}=\mathbf{0.41}$$

    </div>

!!! answer "Answer"
    1. $P(D)=0.0345$ · 2. $P(M_2\mid D)\approx 0.41$

## 2 · April 2025 · 1a — the rate is given for the **good** ones, and the counts are given

!!! exam "Final exam, 13 April 2025 · 1a · 0.3 p"
    An hospital has three CT scanners CT1, CT2, and CT3. It has been observed that 85% of the images produced by CT1 have sufficient quality, while CT2 and CT3 the percentages of images with sufficient quality are 90% and 66%, respectively. Each day, CT1 scans 18 patients, CT2 scans 22 patients, and CT3 scans 15 patients. The images from all CT scanners are mixed at random before image quality control. Assuming that the same number of images are produced for each patients:

    ***Provide only the final answer. The workout will not be checked.***

    1. What is the probability the one image will NOT pass the quality test?
    2. What is the probability that a bad quality image comes from CT2?

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    **Margin step 1 · "Counts given → items = those counts, total = their sum."**
    They say how many patients each scanner does: 18, 22, 15. Total $=55$. **Do not** invent 1000.

    ***

    **Margin step 2 · items.** CT1: 18 · CT2: 22 · CT3: 15.

    ***

    **Margin step 3 · "Asked NOT pass when a pass rate is given → bad rate $=1-$pass rate."**
    This is the trap of this question. They give **sufficient quality** rates but ask for **NOT pass**:
    $1-0.85=0.15$ · $1-0.90=0.10$ · $1-0.66=0.34$.

    ***

    **Margin step 4 · "Bad$_k$ $=$ bad rate $\times$ items."**
    $18\times0.15=2.7$ · $22\times0.10=2.2$ · $15\times0.34=5.1$.

    ***

    **Margin step 5 · "$P(\text{bad})=$ sum $/$ total."**
    $2.7+2.2+5.1=10.0$ out of 55:

    $$P(\text{NOT pass})=\frac{10.0}{55}=\mathbf{0.18}$$

    ***

    **Margin step 6 · "$P(k\mid\text{bad})=$ bad$_k$ $/$ sum of bad."**
    "A **bad** quality image" — inside the pile of 10.0. CT2 gave 2.2 of them:

    $$P(\text{CT2}\mid\text{bad})=\frac{2.2}{10.0}=\mathbf{0.22}$$

    </div>

!!! answer "Answer"
    1. $10/55=0.18$ · 2. $2.2/10=0.22$

## 3 · April 2024 · 1b — a rare disease: take 1 000 000 people

!!! exam "Final exam, April 2024 · 1b · 0.25 p"
    Assume the probability of having tuberculosis (TB) is 0.0005, and a test for TB is 99% accurate. What is the probability one has TB if one tests positive for the disease?

    **Note: provide only the final answer. No passages will be checked.**

    Provide the value of $\Pr[TB]$

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    **Margin step 1 · "Only percentages → pretend total $=1000$ (1 000 000 if a rate is tiny, like 0.0005)."**
    0.0005 is tiny, so take **1 000 000 people**.

    ***

    **Margin step 2 · items.**
    $0.0005\times1\,000\,000=500$ have TB. The other $999\,500$ do not.

    ***

    **Margin step 3 · "'99 % accurate' $=$ 99 % of the ill **and** 99 % of the healthy classified right."**
    So: ill people test **positive** 99 % of the time, and **1 % of the healthy also test positive**. That 1 % of a huge group is the whole question.

    ***

    **Margin step 4 · "Bad$_k$ $=$ bad rate $\times$ items."** (bad $=$ tests positive)
    Sick: $0.99\times500=495$. Healthy: $0.01\times999\,500=9\,995$.

    ***

    **Margin step 5 · the pile.**
    $495+9\,995=10\,490$ positive tests.

    ***

    **Margin step 6 · "Divide by the pile, not by the total."**
    "One has TB **if** one tests positive" → stand inside the 10 490:

    $$\Pr[TB\mid +]=\frac{495}{10\,490}=\mathbf{0.047}$$

    *(The exam's "$\Pr[TB]$" at the end means the conditional — they want $\Pr[TB\mid+]$.)*

    </div>

!!! answer "Answer"
    $P(TB\mid +)=\dfrac{495}{10\,490}\approx 0.047$ — only about 5 %: most positives are healthy people, because there are so many more of them.

## 4 · Practice exam 2021 · 1a — "false positive 3 %" is about the **healthy**

!!! exam "Practice exam, October 2021 · 1a · 0.5 p"
    A virus has infected 1.8% of a population. A test detects this virus 95% of the time when it is actually present, but it returns a false positive 3% of the time when the virus is not present. If a person selected at random from this population tests positive for the virus, what is the probability that this person is actually infected? Please round to the nearest percent.

    a) 26%  b) 37%  c) 95%  d) 92%

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    **Margin step 1 · total.**
    1.8 % is small but not tiny — 1000 people works fine.

    ***

    **Margin step 2 · items.** Infected: $0.018\times1000=18$. Not infected: $982$.

    ***

    **Margin step 3 · read the two rates off the margin's wording table.**
    "detects 95 % **when it is actually present**" → $P(+\mid\text{inf})=0.95$.
    "false positive 3 % **when the virus is not present**" → $P(+\mid\text{not})=0.03$.
    (The 95 % is **not** the answer. That is option (c), and it is the trap.)

    ***

    **Margin step 4 · "Bad$_k$ $=$ bad rate $\times$ items."**
    $0.95\times18=17.1$ · $0.03\times982=29.46$.

    ***

    **Margin step 5 · the pile.** $17.1+29.46=46.56$ positives.

    ***

    **Margin step 6 · divide by the pile.**
    $\dfrac{17.1}{46.56}=0.367$. "Round to the nearest percent" → $\mathbf{37\%}$.

    </div>

!!! answer "Answer"
    **(b) 37 %**

## 5 · January 2020 · 2 — asked about **pass**, so there is no $1-$ step

!!! exam "Retake, January 2020 · Exercise 2 · 2 p"
    A car production company has three machines $M_1$, $M_2$, and $M_3$ for painting cars. It has been observed that 85% of the cars painted by $M_1$ pass the quality test, while for machines $M_2$ and $M_3$ the percentages of a car passing the quality test are 92% and 60%, respectively. Each day, machine $M_1$ paints 30 cars, $M_2$ paints 45 cars, and $M_3$ paints 25 cars. All the cars are mixed at random before quality control.

    - (a) What is the probability that a car will pass the quality test? [1 pt]
    - (b) What is the probability that a car that has passed the test was painted by machine $M_3$? [1 pt]

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    **Margin step 1 · "Counts given → items = those counts."**
    $30+45+25=100$ cars per day.

    ***

    **Margin step 2 · items.** $M_1$: 30 · $M_2$: 45 · $M_3$: 25.

    ***

    **Margin step 3 · "Pick bad."**
    Here bad $=$ **passes** (that is what they ask). The rates 85 %, 92 %, 60 % are already pass rates → **do not** subtract from 1. (Compare with exercise 2, where they asked "NOT pass".)

    ***

    **Margin step 4 · passers per machine.**
    $30\times0.85=25.5$ · $45\times0.92=41.4$ · $25\times0.60=15$.

    ***

    **Margin step 5 · "$P=$ sum $/$ total."**
    $25.5+41.4+15=81.9$ out of 100: $P(\text{pass})=\mathbf{0.819}$.

    ***

    **Margin step 6 · "$P(k\mid\text{bad})=$ bad$_k$ $/$ sum of bad."**
    "A car that **has passed**" → inside the 81.9. $M_3$ gave 15 of them:

    $$P(M_3\mid\text{pass})=\frac{15}{81.9}=\mathbf{0.18}$$

    </div>

!!! answer "Answer"
    (a) $0.819$ · (b) $0.18$

## 6 · January 2022 · 1a — the rate is given for the **complement**

!!! exam "Resit, January 2022 · 1a · 0.3 p"
    A small manufacturing company has rated 75% of its employees as satisfactory (S) and 25% as unsatisfactory ($S^c$). Personnel records show that 80% of the satisfactory workers had previous work experience (E) in the job they are now doing, while 15% of the unsatisfactory workers had no work experience ($E^c$) in the job they are now doing. If a person who has had previous work experience is hired, what is the approximate empirical probability that this person will be an unsatisfactory employee?

    a) 0.24  b) 0.25  c) 0.26  d) 0.28

!!! sheet "In the margin you wrote: steps 1 to 6"
    <div class="stepper" markdown>

    **Margin step 1 · total.** 1000 employees.

    ***

    **Margin step 2 · items.** S: $750$ · $S^c$: $250$.

    ***

    **Margin step 3 · "Pick bad."**
    The pile we are asked about is **"has had previous work experience"** (the person "is hired" with experience). So bad $=$ has experience.
    Two different wordings on purpose: "80 % **had** experience" given S → $P(E\mid S)=0.80$. "15 % had **no** experience" given $S^c$ → so $P(E\mid S^c)=1-0.15=0.85$. The $1-$ lives **inside** the group here, not on the final answer.

    ***

    **Margin step 4 · experienced per group.**
    $750\times0.80=600$ · $250\times0.85=212.5$.

    ***

    **Margin step 5 · the pile.** $600+212.5=812.5$ experienced workers.

    ***

    **Margin step 6 · divide by the pile.**
    "A person who **has had** previous work experience … unsatisfactory" → $S^c$ inside the pile:

    $$P(S^c\mid E)=\frac{212.5}{812.5}=0.2615\approx\mathbf{0.26}$$

    </div>

!!! answer "Answer"
    **(c) 0.26**

## 7 · January 2025 · 1a — a table instead of words

!!! exam "Resit, January 2025 · 1a"
    Two-hundred high school students were asked which university studies they would like to do. Their answers are shown in the table below. Please calculate the following probabilities:

    |        | Engineering | Life Sciences | Literature | Psychology |
    |--------|-------------|---------------|------------|------------|
    | Male   | 45          | 27            | 8          | 10         |
    | Female | 22          | 42            | 20         | 26         |

    Please only provide the final answer. The workout will not be checked.

    1. Given a student at random that chose psychology, the probability that the students was a female.
    2. The probability of choosing Engineering

!!! sheet "In the margin you wrote: steps 1 to 6, with the table as the total"
    <div class="stepper" markdown>

    **Margin step 1 · "Total."**
    Here the total is given: 200. Check the cells: $45+27+8+10+22+42+20+26=200$ ✓.

    ***

    **Margin step 2 · nothing to compute** — the cells *are* the items. Add the column or row you need.

    ***

    **Margin step 3 · "Pick bad."**
    Question 1 says "**Given** a student … that chose psychology" → the pile is the **Psychology column**.
    Question 2 has **no** "given" → the pile is everybody.

    ***

    **Margin step 4 · count the piles.**
    Psychology column: $10+26=36$. Engineering column: $45+22=67$.

    ***

    **Margin step 5 · question 2 first (it is the easy one).**
    $P(\text{Engineering})=\dfrac{67}{200}=\mathbf{0.335}$.

    ***

    **Margin step 6 · question 1, "divide by the pile".**
    Inside the 36 psychology students, 26 are female:

    $$P(\text{female}\mid\text{psychology})=\frac{26}{36}=\mathbf{0.72}$$

    </div>

!!! answer "Answer"
    1. $26/36=0.72$ · 2. $67/200=0.335$

## 8 · November 2022 · 1a — no counts anywhere, so use the formula

!!! exam "Final exam, November 2022 · 1a · 0.25 p"
    About 65% of students who enroll for the exam of the course statistical signal processing have followed the course. Suppose we know that the probability of passing the exam for students who have followed the course is 0.75, while it is 0.4 for students who have not followed it. What is the probability of passing the exam?

    (a) 0.53  (b) 0.52  (c) 0.63  (d) 0.65

!!! sheet "In the margin you wrote: steps 1 to 6 (counts still work; the formula is the same)"
    <div class="stepper" markdown>

    **Margin step 1 · total.** 1000 students.

    ***

    **Margin step 2 · items.** Followed: $650$ · Not followed: $350$.

    ***

    **Margin step 3 · "Pick bad."** Bad $=$ **passes**.

    ***

    **Margin step 4 · passers per group.** $650\times0.75=487.5$ · $350\times0.40=140$.

    ***

    **Margin step 5 · "$P=$ sum $/$ total."**
    $487.5+140=627.5$ out of 1000 → $0.6275\approx\mathbf{0.63}$.

    ***

    **Margin step 6 · same thing in symbols** (the formula at the top of the page), if you prefer:

    $$P(\text{pass})=0.65\cdot0.75+0.35\cdot0.40=0.4875+0.14=0.6275$$

    *Sanity check:* the answer must sit **between** 0.40 and 0.75, and closer to 0.75 because 65 % followed the course. 0.63 does; (a) 0.53 and (b) 0.52 do not.

    </div>

!!! answer "Answer"
    **(c) 0.63**

## 9 · April 2024 · 1a — "given that it survived": divide the two tails

!!! exam "Final exam, April 2024 · 1a · 0.25 p"
    The manual of an ultrasound transducer states that the lifetime $T$ of the product, defined as the amount of time (in years) the product works properly until it breaks down, follows the following probability distribution:

    $$\Pr[T \geq t] = e^{-t/5},$$

    with $t \leq 0$ measured in years.

    Suppose that in an ultrasound lab, they have been using the transducer for two years without any problems. What is the probability that it breaks down in the third year, given that it was still working after 2 years?

    **Hint:** the third year is the year between the $t = 2$ and $t = 3$.

    (a) 0.24  (b) 0.12  (c) 0.30  (d) 0.18

!!! sheet "In the margin you wrote: conditional $=$ part $/$ whole, and the Calculations strip"
    <div class="stepper" markdown>

    **Margin step 0 · read the given function.**
    $\Pr[T\ge t]=e^{-t/5}$ is the probability of **still working at year $t$**. (The printed "$t\le0$" is a typo for $t\ge0$.)

    ***

    **Margin step 1 · "Pick bad."**
    Bad $=$ "breaks down in the third year" $=$ $2\le T\lt3$. But it is **conditional**: "given that it was still working after 2 years" → the pile is $T\ge2$.

    ***

    **Margin step 2 · conditional $=$ part $/$ whole** (the formula at the top of the page):

    $$P(2\le T\lt3\mid T\ge2)=\frac{P(T\ge2)-P(T\ge3)}{P(T\ge2)}=1-\frac{P(T\ge3)}{P(T\ge2)}$$

    ***

    **Margin step 3 · plug in, and use the Calculations strip** ($\frac{e^a}{e^b}=e^{a-b}$):

    $$1-\frac{e^{-3/5}}{e^{-2/5}}=1-e^{-3/5+2/5}=1-e^{-1/5}$$

    ***

    **Margin step 4 · the Numbers strip** has $e^{-1}=0.368$, so get $e^{-0.2}$ from a calculator: $0.8187$.
    $1-0.8187=\mathbf{0.1813}\approx 0.18$.

    ***

    **Margin check.**
    The four options are 0.12 / 0.18 / 0.24 / 0.30. Only 0.18 is close. (Quick feel: in one year a device with a 5-year "half-life-ish" scale breaks about 18 % of the time.)

    </div>

!!! answer "Answer"
    **(d) 0.18**

## 10 · June 2026 · 1a — independence is a one-line definition

!!! exam "Resit, June 2026 · 1a · 0.2 p"
    Which of the following statements about two events $A$ and $B$ (assuming both have non-zero probabilities) is ALWAYS TRUE if they are statistically independent?

    - (a) $P(A \cup B) = P(A) + P(B)$
    - (b) $P(A | B) = P(B)$
    - (c) $P(A \cap B) = 0$
    - (d) $P(A | B) = P(A)$

!!! sheet "Not on the sheet — one line to know by heart"
    <div class="stepper" markdown>

    **Step 1 · the definition.** Independent means knowing $B$ tells you **nothing** about $A$:

    $$P(A\mid B)=P(A)\qquad\Longleftrightarrow\qquad P(A\cap B)=P(A)P(B)$$

    That is option **(d)**.

    ***

    **Step 2 · kill the others.**
    (a) $P(A\cup B)=P(A)+P(B)$ only for **disjoint** events (no overlap) — independent events usually do overlap.
    (b) $P(A\mid B)=P(B)$ swaps the roles; nothing says that.
    (c) $P(A\cap B)=0$ means they **cannot happen together** — that is disjoint, the *opposite* of independent (unless one probability is 0, which they excluded).

    </div>

!!! answer "Answer"
    **(d)** $P(A\mid B)=P(A)$

## 11 · November 2019 · 1b — a true/false list

!!! exam "Written exam, November 2019 · 1b · 0.5 p"
    Please indicate if the following statements are true or false.

    - A. Bayes theorem is obtained from the total law of probability and the conditional probability (T/F)
    - B. There is a 50% chance of rain here and a 25% chance of rain on Mars. Therefore, there is a 75% chance that it will rain here or on Mars. (T/F)
    - C. For discrete random variables, the relative frequency tends to the probability mass function as the number of trials tends to infinity (T/F)
    - D. For any random variable, the cumulative distribution function in $-\infty$ and $\infty$ are 0 and 1, respectively. (T/F)
    - E. The Wiener FIR filter for 1-step linear prediction can be used for moving-average parametric spectral estimation (T/F).

!!! sheet "Not on the sheet — five one-liners, and this is what a T/F list looks like"
    <div class="stepper" markdown>

    **A · F.** Bayes comes from the **definition of conditional probability** plus the product rule; the total law of probability only supplies the denominator $P(B)$. (This is the answer the key gives — the sentence is built to look right.)

    ***

    **B · F.** $P(A\cup B)=P(A)+P(B)$ needs the events to be **disjoint**. Rain here and rain on Mars can happen together, so the union is at most 75 % and at least 50 % — not 75 %.

    ***

    **C · T.** That is what "relative frequency" means: count the value, divide by the number of trials. As trials $\to\infty$ that ratio $\to$ the PMF. (Wording: **PMF** $=P(X=x)$ for each value.)

    ***

    **D · T.** $F(x)=P(X\le x)$. Nothing is $\le-\infty$ → 0. Everything is $\le\infty$ → 1.

    ***

    **E · F.** A 1-step linear predictor gives an all-**pole** (AR) model, not an MA model. This one is from an old topic — if it comes back, say "AR, not MA" and move on.

    ***

    **Sheet check.**
    Answer key: **F F T T F**. Notice the shape of the exercise: a T/F list mixes topics, so it is really 5 separate recall questions. Do not spend 2 minutes on one line.

    </div>

!!! answer "Answer"
    **F F T T F**

## Traps

!!! trap "Where points are lost (each one is a line of the margin recipe you skipped)"
    - The rate is given for the **good** items ("sufficient quality", "accurate", "pass"): convert with $1-$rate **only** when the question asks for the bad one (exercises 2 and 5 are the same question with the sign flipped).
    - Step 6 divides by the **pile of bad ones**, not by the total. That is the single most common mistake in this block.
    - "99 % accurate" applies to **both** groups: 1 % of the healthy test positive, and they outnumber the sick.
    - Reading "95 % detects" as the answer. It is $P(+\mid\text{ill})$, and they want $P(\text{ill}\mid +)$ — the two are different and the exam offers both as options.
    - "had **no** experience" inside a group → flip it **inside** the group (exercise 6), not at the end.
    - "Given that it survived" → the answer is a ratio of two tails, $1-\frac{P(T\ge3)}{P(T\ge2)}$.
    - Round only at the very end. "Provide only the final answer" means no partial credit for a wrong number.
