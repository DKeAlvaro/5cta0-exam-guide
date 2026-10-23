"""Episode 3 · Estimation: MLE, MAP and the multiple-choice facts (lessons 2.1, 2.2, 2.4)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
from manim import (DOWN, LEFT, RIGHT, UP, Create, DashedLine, Dot, Line, SurroundingRectangle,  # noqa: E402
                   ValueTracker, VGroup, always_redraw)
from podkit import Pod, card, chip, np_grid, stack  # noqa: E402
from vidkit import BLUE, GREEN, GREY, INK, MT, ORANGE, PURPLE, RED, area, curve, mk_axes  # noqa: E402

XS = np.array([1.2, 0.8, 2.1, 1.5, 1.0])
BEST = float(np.sum(XS ** 2) / (2 * len(XS)))


def pdf(x, th):
    x = np.asarray(x, float)
    return x / th * np.exp(-x ** 2 / (2 * th))


def lnL(th):
    return float(np.sum(np.log(pdf(XS, th))))


def beta_shape(a, b, t):
    lv = (a - 1) * np.log(t) + (b - 1) * np.log(1 - t)
    return np.exp(lv - lv.max())


class Ep3Estimation(Pod):
    episode = 'Episode 3 · Estimation'
    sections = ['intro', 'likelihood', 'recipe', 'apr24', 'sigmoid', 'map_idea', 'jun26', 'beta', 'facts', 'recap']

    def intro(self):
        self.header('intro')
        self.say('T', "Episode three: estimation. This is block two of the exam, the biggest one: three to three and a half points. Almost every paper asks you to derive an MLE, derive a MAP, and answer one multiple choice question.",
                 self.title_card('Estimation: MLE and MAP', 'Lessons 2.1, 2.2 and 2.4 of the guide',
                                 [chip('MLE in 7 of 9 exams', RED), chip('MAP in 7 of 9', BLUE), chip('same 4 moves every time', GREEN)]))
        self.say('S', "Derive sounds scary.")
        self.say('T', "It is the same four moves every single time. You will see them three times today, and by the end you will be bored of them. That is the goal.")

    def likelihood(self):
        self.header('the idea: turn the knob until the data look most likely')
        th = ValueTracker(0.45)
        ax = mk_axes([0, 3.6, 1], [0, 1.3, 0.5], 9.0, 2.1).move_to(UP * 1.55)
        gx = np_grid(0.001, 3.6, 200)
        c = always_redraw(lambda: curve(ax, gx, np.minimum(pdf(gx, th.get_value()), 1.3), BLUE, 4))
        st = always_redraw(lambda: VGroup(*[Line(ax.c2p(x, 0), ax.c2p(x, min(1.3, float(pdf(x, th.get_value())))), color=RED, stroke_width=6) for x in XS]))
        dots = VGroup(*[Dot(ax.c2p(x, 0), radius=0.07, color=INK) for x in XS])
        bx = mk_axes([0.2, 3, 0.5], [-16, -3, 1], 9.0, 1.7).move_to(DOWN * 1.15)
        gt = np_grid(0.2, 3, 150)
        lc = curve(bx, gt, np.clip([lnL(t) for t in gt], -16, -3), PURPLE, 4)
        ld = always_redraw(lambda: Dot(bx.c2p(th.get_value(), max(-16, lnL(th.get_value()))), radius=0.1, color=RED))
        lab1 = MT(r'model $p(x\,|\,\theta)$ and 5 data points; red stick = how likely each point is', 20).next_to(ax, UP, buff=0.1)
        lab2 = MT(r'$\ln L(\theta)$ = sum of the log stick heights, for every $\theta$', 20).next_to(bx, UP, buff=0.08)
        thl = always_redraw(lambda: MT(r'$\theta=%.2f$' % th.get_value(), 24, RED).next_to(ax, RIGHT, buff=0.2))
        self.say('T', "Here is the setting. You have some data: numbers x one up to x N. And a model, a PDF, with one unknown number inside it, called theta. Think of theta as a knob on the model.",
                 self.wipe(), self.put(VGroup(ax, lab1, dots)), self.put(c), self.put(thl, rt=0.4))
        self.say('T', "For each position of the knob, the model says how likely your data were. You read the height of the curve at each data point, the red sticks, and you multiply them together. That product is called the likelihood.",
                 self.put(st, rt=0.8))
        self.say('T', "Watch the sticks while I turn the knob. Too small, and the curve is narrow: the point at two point one gets almost nothing. Too big, and every stick is short.",
                 th.animate(run_time=3).set_value(2.6), th.animate(run_time=2).set_value(0.45))
        self.say('T', "The MLE, the maximum likelihood estimate, is the knob position where all the sticks are as tall as possible together. The top of this purple curve.",
                 self.put(VGroup(bx, lab2, lc), rt=0.8), self.put(ld, rt=0.4), th.animate(run_time=2.5).set_value(BEST))
        top = DashedLine(bx.c2p(BEST, -16), bx.c2p(BEST, lnL(BEST)), color=GREEN)
        self.say('S', "And how do you find the top without trying every value?", self.put(top, Create, 0.6))
        flat = Line(bx.c2p(BEST - 0.5, lnL(BEST)), bx.c2p(BEST + 0.5, lnL(BEST)), color=GREEN, stroke_width=5)
        self.think('Think. At the very top of a smooth hill, what is the slope?', 'slope at the very top of a smooth curve = ?', 4)
        self.say('T', "At the top, the curve is flat. Its slope is zero. So you take the derivative and set it equal to zero. That is the whole method.",
                 self.put(flat, Create, 0.8))
        self.say('T', "One more trick. We take the log first. The log turns the product into a sum, which is much easier to differentiate, and it does not move the top.")

    def recipe(self):
        self.header('the recipe')
        rows = [MT(r'1. Likelihood:  $L(\theta)=\prod_n p(x_n\,|\,\theta)$   (independent samples: multiply)', 24),
                MT(r'2. Log:  $\ln L(\theta)=\sum_n \ln p(x_n\,|\,\theta)$   (split into simple pieces)', 24),
                MT(r'3. Differentiate in $\theta$ and set  $\dfrac{d}{d\theta}\ln L=0$', 24),
                MT(r'4. Solve for $\theta$.  That is $\hat\theta_{ML}$.', 24)]
        VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.26).move_to(UP * 1.7)
        tools = card([r'$\ln(ab)=\ln a+\ln b$     $\ln e^{u}=u$     $\ln x^{k}=k\ln x$     $\sum_n c=Nc$',
                      r'$\dfrac{d}{d\theta}\ln\theta=\dfrac{1}{\theta}$     $\dfrac{d}{d\theta}\dfrac{1}{\theta}=-\dfrac{1}{\theta^{2}}$     no $\theta$ in it $\Rightarrow$ derivative $0$'], 22).next_to(VGroup(*rows), DOWN, buff=0.3)
        self.say('T', "The recipe. Step one: the likelihood is the product of the PDF over all samples.", self.wipe(), self.put(rows[0]))
        self.say('T', "Step two: take the log. The product becomes a sum, and you split each term into simple pieces.", self.put(rows[1]))
        self.say('T', "Step three: differentiate with respect to theta and set it to zero. Step four: solve for theta.", self.put(rows[2]), self.put(rows[3]))
        self.say('T', "And these are the only rules you need. Log of a product is a sum of logs. Log of e to the u is u. The derivative of log theta is one over theta. The derivative of one over theta is minus one over theta squared. And anything without theta in it has derivative zero, so it disappears.",
                 self.put(tools, rt=1.0))

    def apr24(self):
        self.header('worked example: April 2024, 2c (1 point)')
        ex = card([r'April 2024 · 2c · 1 p:   independent samples $x_1,\dots,x_N$ with',
                   r'$p(x_n\,|\,\theta)=\dfrac{x_n}{2\theta}\,e^{-x_n^{2}/(2\theta)}$.   Derive the MLE of $\theta$.'], 25).to_edge(UP, buff=0.6)
        self.say('S', "Let's do a real one.", self.wipe())
        self.say('T', "April 2024, one point. The PDF is x over two theta, times e to the minus x squared over two theta. Derive the MLE.", self.put(ex))
        e = [MT(r'one sample:  $\ln p=\ln x_n-\ln 2-\ln\theta-\dfrac{x_n^{2}}{2\theta}$', 28),
             MT(r'sum:  $\ln L=\sum_n\ln x_n-N\ln2-N\ln\theta-\dfrac{1}{2\theta}\sum_n x_n^{2}$', 28),
             MT(r'$\dfrac{d}{d\theta}$:   $0-0-\dfrac{N}{\theta}+\dfrac{1}{2\theta^{2}}\sum_n x_n^{2}=0$', 28),
             MT(r'$\times\theta^{2}$:   $-N\theta+\frac{1}{2}\sum_n x_n^{2}=0$   $\Rightarrow$   $\hat\theta_{ML}=\dfrac{1}{2N}\sum_n x_n^{2}$', 28, RED)]
        VGroup(*e).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(ex, DOWN, buff=0.4)
        self.say('T', "Steps one and two together: the log of one sample. Log of x n, minus log two, minus log theta, minus x n squared over two theta. The log ate the exponential.", self.write(e[0], 1.2))
        self.say('T', "Sum over the N samples. Constants get multiplied by N: minus N log two, minus N log theta, and the last piece becomes minus one over two theta, times the sum of the x squared.", self.write(e[1], 1.2))
        self.think('Your turn. Differentiate minus N log theta, and minus one over two theta times the sum.', 'derivative in $\\theta$ of  $-N\\ln\\theta$  and of  $-\\frac{1}{2\\theta}\\sum x_n^2$ ?', 8)
        self.say('T', "Step three, differentiate. The first two pieces have no theta: zero. Minus N log theta gives minus N over theta. And minus one over two theta gives plus one over two theta squared, because the derivative of one over theta is minus one over theta squared, and minus times minus is plus.", self.write(e[2], 1.2))
        self.say('S', "Then multiply by theta squared?")
        self.say('T', "Exactly. Minus N theta plus one half the sum equals zero. So theta hat is one over two N, times the sum of the x squared. One point.", self.write(e[3], 1.2))
        self.say('T', "The piece people forget is minus N log theta, the one that comes from the theta in front. It is half of the answer.",
                 self.put(SurroundingRectangle(e[1], color=ORANGE, buff=0.08), Create, 0.6))

    def sigmoid(self):
        self.header('the sigmoid trick (April 2025 2c, April 2024 2d)')
        ex = card([r'April 2025 · 2c · 1 p:   $p(x\,|\,\theta)=3\lambda(\theta)\,e^{-4\lambda(\theta)x/7}$,   $\lambda(\theta)=\dfrac{1}{1+e^{-\theta}}$'], 26).to_edge(UP, buff=0.6)
        self.say('T', "Two recent exams had a strange looking one. The parameter theta is hidden inside a sigmoid, called lambda of theta.", self.wipe(), self.put(ex))
        e = [MT(r'$\ln p=\ln 3+\ln\lambda-\dfrac{4x}{7}\lambda$', 30),
             MT(r'$\dfrac{d}{d\lambda}$:   $\dfrac{1}{\lambda}-\dfrac{4x}{7}=0$   $\Rightarrow$   $\hat\lambda=\dfrac{7}{4x}$', 30),
             MT(r'$\dfrac{1}{1+e^{-\theta}}=\dfrac{7}{4x}$  $\Rightarrow$  $e^{-\theta}=\dfrac{4x}{7}-1$  $\Rightarrow$  $\hat\theta=-\ln\!\left(\dfrac{4x}{7}-1\right)$', 30, RED)]
        VGroup(*e).arrange(DOWN, buff=0.35).next_to(ex, DOWN, buff=0.45)
        self.say('T', "The trick: find the best lambda first, then turn lambda back into theta. That is allowed. It is called the invariance of the MLE, and it is also a multiple choice answer.")
        self.think('Try it. Take the log of three lambda e to the minus four x lambda over seven, differentiate in lambda, and set it to zero.', '$\\ln(3\\lambda e^{-4\\lambda x/7})$, then $d/d\\lambda=0$:  $\\hat\\lambda$ = ?', 8)
        self.say('T', "Log: log three plus log lambda minus four x over seven times lambda. Derivative in lambda: one over lambda minus four x over seven equals zero. So lambda hat is seven over four x.",
                 self.write(e[0]), self.write(e[1], 1.2))
        self.say('T', "Now set the sigmoid equal to that. One plus e to the minus theta equals four x over seven. So e to the minus theta is four x over seven minus one, and theta is minus the log of that. It only works when x is bigger than seven quarters, because the log needs a positive number.",
                 self.write(e[2], 1.5))
        self.say('S', "And April 2024 was the same trick, but for a MAP?")
        self.say('T', "Same trick, worth one and a half points. Best lambda is two over x, so theta is minus log of x over two minus one.")

    def map_idea(self):
        self.header('MAP: the data plus what you believed before')
        t = np_grid(0.002, 0.998, 200)
        ax = mk_axes([0, 1, 0.25], [0, 1.15, 0.5], 9.5, 3.2).move_to(UP * 0.55)
        pr = curve(ax, t, beta_shape(2, 3, t), GREY, 4)
        lk = curve(ax, t, beta_shape(11, 13, t), BLUE, 4)
        po = curve(ax, t, beta_shape(12, 15, t), RED, 5)
        poa = area(ax, t, beta_shape(12, 15, t), RED, 0.18)
        leg = VGroup(MT('prior', 22, GREY), MT('likelihood (data)', 22, BLUE), MT('posterior = prior × likelihood', 22, RED)).arrange(RIGHT, buff=0.6).next_to(ax, UP, buff=0.15)
        labs = VGroup(*[MT(f'${v}$', 18, GREY).next_to(ax.c2p(v, 0), DOWN, buff=0.12) for v in (0, 0.5, 1)])
        self.say('T', "Now MAP. The MLE only listens to the data. The MAP also listens to what you believed before you saw the data. That belief is called the prior.",
                 self.wipe(), self.put(VGroup(ax, labs)), self.put(VGroup(pr, leg[0])))
        self.say('T', "The data give the likelihood, the blue curve. Bayes' rule says: posterior is proportional to likelihood times prior. The red curve.",
                 self.put(VGroup(lk, leg[1])), self.put(VGroup(po, poa, leg[2])))
        mp = 11 / 25
        ml = 10 / 22
        lines = VGroup(DashedLine(ax.c2p(mp, 0), ax.c2p(mp, 1.05), color=RED), MT(f'MAP ${mp:.2f}$', 20, RED).next_to(ax.c2p(mp, 1.05), LEFT, buff=0.35),
                       DashedLine(ax.c2p(ml, 0), ax.c2p(ml, 1.05), color=BLUE), MT(f'MLE ${ml:.2f}$', 20, BLUE).next_to(ax.c2p(ml, 1.05), RIGHT, buff=0.35))
        self.say('T', "The MAP is the top of the posterior. It sits between the prior and the data. With more data, the blue curve gets sharper, and the MAP walks onto the MLE.",
                 self.put(lines))
        self.say('S', "Multiplying two curves sounds like a lot of work.")
        rule = MT(r'same base $\Rightarrow$ ADD the exponents:   $\theta^{1}(1-\theta)^{2}\ \times\ \theta^{10}(1-\theta)^{12}=\theta^{11}(1-\theta)^{14}$', 26, PURPLE).move_to(DOWN * 1.75)
        self.say('T', "With the priors the exam uses, Beta and Gamma, it is trivial. Both are powers of the same thing, so you just add the exponents.", self.put(rule))

    def jun26(self):
        self.header('worked example: June 2026, 2d (Poisson + Gamma)')
        ex = card([r'June 2026 · 2d:   daily counts $X_i\sim$ Poisson$(\lambda)$,   data $x=\{2,4,3,5,2,4\}$',
                   r'prior $p(\lambda)\propto\lambda^{\alpha-1}e^{-\beta\lambda}$,  $\alpha=3$, $\beta=2$.   Posterior, MAP, compare with MLE.'], 24).to_edge(UP, buff=0.6)
        self.say('T', "June 2026. Pollution spikes per day follow a Poisson distribution with unknown rate lambda. Six days of data: two, four, three, five, two, four. And a Gamma prior with alpha three and beta two.",
                 self.wipe(), self.put(ex))
        e = [MT(r'likelihood:  $\prod_i\dfrac{\lambda^{x_i}e^{-\lambda}}{x_i!}\ \propto\ \lambda^{\sum x_i}e^{-6\lambda}=\lambda^{20}e^{-6\lambda}$', 28),
             MT(r'$\times$ prior $\lambda^{2}e^{-2\lambda}$:   posterior $\propto\lambda^{22}e^{-8\lambda}$   $=$  Gamma$(23,\,8)$', 28),
             MT(r'MAP $=\dfrac{a-1}{b}=\dfrac{22}{8}=2.75$        MLE $=\dfrac{20}{6}=3.33$', 30, RED)]
        VGroup(*e).arrange(DOWN, buff=0.38).next_to(ex, DOWN, buff=0.45)
        self.say('T', "Likelihood: multiply the Poisson probability, lambda to the x, e to the minus lambda, over x factorial, over the six days. Keep only what has lambda in it. The exponents of lambda add up to twenty, the sum of the data, and e to the minus lambda six times gives e to the minus six lambda.",
                 self.write(e[0], 1.4))
        self.think('Your turn. Multiply lambda to the twenty, e to the minus six lambda, by lambda squared, e to the minus two lambda.', '$\\lambda^{20}e^{-6\\lambda}\\cdot\\lambda^{2}e^{-2\\lambda}$ = ?', 6)
        self.say('T', "Times the prior, lambda squared e to the minus two lambda. Add the exponents: lambda to the twenty two, e to the minus eight lambda. That shape is a Gamma with a equals twenty three, one more than the exponent, and b equals eight.",
                 self.write(e[1], 1.4))
        self.think('And the top of a Gamma with a equal to twenty three and b equal to eight?', 'top of Gamma$(23,8)$ $=(a-1)/b$ = ?', 5)
        self.say('T', "The top of a Gamma is a minus one over b: twenty two over eight, two point seven five. The MLE, data only, is the average: twenty over six, three point three three.",
                 self.write(e[2], 1.2))
        self.say('S', "So the prior pulled it down.")
        self.say('T', "Right. The prior's mean is alpha over beta, one point five, so it pulls the estimate down. And with more days of data, the prior matters less and less. That sentence is the comparison they ask for.")

    def beta(self):
        self.header('the Beta version (June 2026 2c, April 2025 2d)')
        r = card([r'posterior $\propto\theta^{A}(1-\theta)^{B}$   $\Rightarrow$   $\hat\theta_{MAP}=\dfrac{A}{A+B}$',
                  r'(that is Beta$(a,b)$ with $a=A+1$, $b=B+1$:  top $=\dfrac{a-1}{a+b-2}$)'], 28).move_to(UP * 1.4)
        self.say('T', "The other family is the Beta, for probabilities between zero and one. If the posterior is theta to the A times one minus theta to the B, the top is at A over A plus B.",
                 self.wipe(), self.put(r))
        e = MT(r'June 2026 2c:   $\theta^{11}(1-\theta)^{14}$   $\Rightarrow$   Beta$(12,15)$,   $\hat\theta_{MAP}=\dfrac{11}{25}=0.44$', 28, RED).next_to(r, DOWN, buff=0.5)
        self.think('Posterior theta to the eleven, times one minus theta to the fourteen. What is the MAP?', '$\\theta^{11}(1-\\theta)^{14}$:  MAP = ?', 5)
        self.say('T', "In June 2026 the posterior came out as theta to the eleven, times one minus theta to the fourteen. So the MAP is eleven over twenty five: zero point four four. And April 2025 gave the posterior directly, so it was just this formula with letters.",
                 self.write(e, 1.2))
        self.say('S', "Where does A over A plus B come from?")
        d = MT(r'$\ln p=A\ln\theta+B\ln(1-\theta)$   $\Rightarrow$   $\dfrac{A}{\theta}-\dfrac{B}{1-\theta}=0$   $\Rightarrow$   $\theta=\dfrac{A}{A+B}$', 28).next_to(e, DOWN, buff=0.45)
        self.say('T', "The same four moves. Log: A log theta plus B log one minus theta. Derivative: A over theta minus B over one minus theta. Set to zero and solve.", self.write(d, 1.2))

    def facts(self):
        self.header('the multiple-choice facts (lesson 2.4)')
        cs = [card([r'MMSE = the MEAN of the posterior.   MAP = the MAXIMUM (top) of the posterior.', r'Equal for a symmetric posterior (Gaussian), so NOT "always different".'], 25, width=12.2),
              card([r'Fisher information of $N$ i.i.d. samples $=N\,i(\theta)$, and it is $\geq 0$.', r'Bound:  Var$(\hat\theta)\geq 1/\mathcal{I}(\theta)$  (one OVER the information).'], 25, width=12.2),
              card([r'MLE: asymptotically unbiased; invariant ($\hat\alpha=\psi(\hat\theta)$);', r'does NOT always reach the CRLB, works for any model.'], 25, width=12.2)]
        VGroup(*cs).arrange(DOWN, buff=0.3).move_to(UP * 0.45)
        self.say('T', "Last, the multiple choice. The same sentences come back every year, sometimes with one word changed.", self.wipe())
        self.think('True or false: the MMSE estimate is the maximum of the posterior.', 'MMSE = MAXIMUM of the posterior. True or false?', 4)
        self.say('T', "One. The MMSE estimate is the mean of the posterior. The MAP is its maximum, its top. For a symmetric posterior, like a Gaussian, they are the same. So a statement saying they always differ is false.", self.put(cs[0]))
        self.think('True or false: any unbiased estimator has variance at least the Fisher information.', 'Var$(\\hat\\theta)\\geq\\mathcal{I}(\\theta)$. True or false?', 4)
        self.say('T', "Two. The Fisher information of N independent samples is N times the information of one sample, and it is never negative. The variance of an unbiased estimator is at least one over the Fisher information. One over. If it says bigger than the information itself, it is false.", self.put(cs[1]))
        self.think('True or false: the MLE always achieves the Cramer Rao bound.', 'the MLE ALWAYS reaches the CRLB. True or false?', 4)
        self.say('T', "Three. The MLE is asymptotically unbiased, and it is invariant: the MLE of a function is the function of the MLE. But it does not always reach the Cramer Rao bound, and it is not only for linear models.", self.put(cs[2]))

    def recap(self):
        self.header('recap')
        r = card([r'MLE:  likelihood $\to$ $\ln$ $\to$ $d/d\theta=0$ $\to$ solve.   Do not forget $-N\ln\theta$.',
                  r'sigmoid: solve for $\lambda$ first, then $\theta=-\ln(1/\lambda-1)$',
                  r'MAP:  likelihood $\times$ prior, ADD exponents, name it:  Gamma top $=\frac{a-1}{b}$,  Beta top $=\frac{a-1}{a+b-2}$',
                  r'MMSE = posterior mean,  MAP = posterior top,  CRLB $=1/(N\,i(\theta))$'], 24).move_to(UP * 0.5)
        self.say('S', "Summary, please.", self.wipe())
        self.say('T', "MLE: likelihood, log, derivative equals zero, solve. Sigmoid questions: solve for lambda first. MAP: likelihood times prior, add the exponents, recognise the Gamma or the Beta, and take its top. And for the multiple choice: MMSE is the mean, MAP is the top.",
                 self.put(r, rt=1.0))
        nxt = MT('Now: lessons 2.1 and 2.2, do the "Your turn" questions on paper.', 28, PURPLE).next_to(r, DOWN, buff=0.45)
        self.say('T', "Now do the your turn questions in lessons 2.1 and 2.2, on paper, without looking. Then the true or false cards in lesson 2.4.", self.put(nxt))
        self.say('S', "Got it. Thanks, Ava.")
