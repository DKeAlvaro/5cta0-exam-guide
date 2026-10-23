"""Episode 2 · Spectral estimation: correlogram, AR, MA, pick the plot (lessons 3.1 and 3.2)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
from manim import (DOWN, LEFT, RIGHT, UP, Create, Dot, FadeIn, SurroundingRectangle, Transform,  # noqa: E402
                   VGroup)
from podkit import Pod, card, chip, matrix, np_grid, stack  # noqa: E402
from vidkit import Txt  # noqa: E402
from vidkit import BLUE, GREEN, GREY, INK, MT, ORANGE, PURPLE, RED, curve, mk_axes, stems  # noqa: E402

TH = np_grid(0, math.pi, 200)


def theta_axes(yr, w=7.2, h=3.4, center=RIGHT * 2.6 + UP * 0.3):
    ax = mk_axes([0, math.pi, 1], yr, w, h).move_to(center)
    labs = VGroup(MT('$0$', 22).next_to(ax.c2p(0, yr[0]), DOWN, buff=0.12),
                  MT(r'$\pi/2$', 22).next_to(ax.c2p(math.pi / 2, yr[0]), DOWN, buff=0.12),
                  MT(r'$\pi$', 22).next_to(ax.c2p(math.pi, yr[0]), DOWN, buff=0.12),
                  MT(r'$\theta$', 24).next_to(ax.c2p(math.pi, yr[0]), RIGHT, buff=0.2))
    return VGroup(ax, labs), ax


class Ep2Spectral(Pod):
    episode = 'Episode 2 · Spectral estimation'
    sections = ['intro', 'rk', 'psd', 'corr', 'plot', 'ar1', 'ar2', 'ma1', 'recap']

    def intro(self):
        self.header('intro')
        self.say('T', "Episode two: spectral estimation. This is the chain question. They give you a few autocorrelation values, and you compute a correlogram, an AR model, sometimes an MA model, and you pick the right plot.",
                 self.title_card('The Part 3 chain: correlogram, AR, MA', 'Lessons 3.1 and 3.2 of the guide',
                                 [chip('in 7 of 9 exams', RED), chip('about 2 points', BLUE), chip('pure arithmetic', GREEN)]))
        self.say('T', "It is worth about two points, it is in almost every exam, and once you know four formulas it is pure arithmetic.")
        self.say('S', "I don't even know what an autocorrelation is.")
        self.say('T', "Then that is exactly where we start.")

    def rk(self):
        self.header('what r[k] means')
        rng = np.random.default_rng(3)
        n = np.arange(24)
        slow = np.zeros(24)
        for i in range(1, 24):
            slow[i] = 0.85 * slow[i - 1] + rng.normal(0, 0.5)
        ax1 = mk_axes([0, 25, 5], [-2, 2, 1], 6.2, 2.0).move_to(LEFT * 3.4 + UP * 1.4)
        s1 = stems(ax1, n, slow, BLUE, r=0.05)
        s1b = stems(ax1, n + 1, slow, ORANGE, r=0.05)
        t1 = MT('$x[n]$ (blue) and the copy shifted by 1 (orange)', 18).next_to(ax1, UP, buff=0.15)
        self.say('T', "Take a signal: just a list of numbers, x of n, one per time step. Now make a copy and shift it by one step. The autocorrelation r of one asks: how similar is the signal to its own shifted copy?",
                 self.wipe(), self.put(VGroup(ax1, t1)), self.put(s1, rt=0.8), self.put(s1b, rt=0.8))
        self.say('T', "You multiply the two, sample by sample, and average. This one changes slowly, so neighbours look alike. Big products, so r of one is big and positive.")
        self.think('Quick check. A signal that flips sign at every step: is r of one positive or negative?', 'flips sign every step: is $r[1]$ positive or negative?', 4)
        alt = np.array([(-1) ** i * (1 + 0.4 * rng.normal()) for i in range(24)])
        ax2 = mk_axes([0, 25, 5], [-2, 2, 1], 6.2, 2.0).move_to(RIGHT * 3.4 + UP * 1.4)
        t2 = MT('a signal that flips sign every step', 18).next_to(ax2, UP, buff=0.15)
        s2 = stems(ax2, n, alt, BLUE, r=0.05)
        s2b = stems(ax2, n + 1, alt, ORANGE, r=0.05)
        self.say('T', "This one flips sign every step. Its shifted copy is the opposite of itself, so the products are negative, and r of one is negative.",
                 self.put(VGroup(ax2, t2)), self.put(s2, rt=0.6), self.put(s2b, rt=0.6))
        facts = card([r'$r[k]$ = how much $x$ looks like itself shifted by $k$',
                      r'$r[0]$ = the power of the signal (no shift)',
                      r'$r[-k]=r[k]$  (left or right shift: same comparison)'], 26).move_to(DOWN * 1.3)
        self.say('T', "Three facts. r of k measures how much the signal looks like itself shifted by k. r of zero, no shift, is just the power of the signal. And r of minus k always equals r of k.",
                 self.put(facts))

    def psd(self):
        self.header('what a PSD is')
        g, ax = theta_axes([0, 1, 1], w=9, h=1.2, center=DOWN * 0.2)
        self.say('S', "OK. And the PSD?", self.wipe())
        slow = VGroup(*[Dot(radius=0.06, color=BLUE).move_to([-5.4 + 0.3 * i, 1.6 + 0.6 * math.cos(0.25 * i), 0]) for i in range(10)])
        fast = VGroup(*[Dot(radius=0.06, color=RED).move_to([2.6 + 0.3 * i, 1.6 + 0.6 * (-1) ** i, 0]) for i in range(10)])
        ls = MT(r'$\theta$ near 0: slow', 24, BLUE).next_to(slow, UP, buff=0.2)
        lf = MT(r'$\theta=\pi$: $+,-,+,-$ (fastest)', 24, RED).next_to(fast, UP, buff=0.2)
        self.say('T', "The power spectral density, P of theta, says how the power of the signal is spread over frequency. Theta goes from zero to pi.",
                 self.put(g))
        self.say('T', "Theta near zero means slow: the signal barely changes. Theta equal to pi is the fastest a sampled signal can wiggle: plus, minus, plus, minus.",
                 self.put(VGroup(slow, ls)), self.put(VGroup(fast, lf)))
        self.say('T', "So a slowly changing signal has its power near zero, on the left. A wiggly one has its power near pi, on the right. Keep that picture: it is how you pick the right plot.")

    def corr(self):
        self.header('the correlogram (June 2026, 3c)')
        f = MT(r'$\hat P_{corr}(\theta)=r[0]+2r[1]\cos\theta+2r[2]\cos 2\theta+\dots$', 32).to_edge(UP, buff=0.65)
        self.say('T', "The correlogram turns the autocorrelation values into a PSD. Every lag k becomes a cosine wave, cos k theta, weighted by r of k. The formula: r of zero, plus two r of one cos theta, plus two r of two cos two theta, and so on.",
                 self.wipe(), self.write(f, 1.4))
        self.say('S', "Why the two?")
        self.say('T', "Because lag plus k and lag minus k have the same value. Together they make two times a cosine. That is the only reason. And r of zero has no partner, so it is not doubled.",
                 self.put(SurroundingRectangle(f, color=ORANGE, buff=0.1), Create, 0.6))
        g, ax = theta_axes([-1.5, 9.5, 1], w=6.2, h=3.2, center=RIGHT * 3.1 + DOWN * 0.75)
        zero = curve(ax, TH, 0 * TH, GREY, 1.5)
        data = MT(r'June 2026:  $r[0]=3$,  $r[1]=2$,  $r[2]=1$', 26).move_to(UP * 1.75)
        s0 = curve(ax, TH, 3 + 0 * TH, RED, 5)
        self.say('T', "June 2026, question 3c. r of zero is three, r of one is two, r of two is one. Start with r of zero: a flat line at three.",
                 self.put(data), self.put(VGroup(g, zero)), self.put(s0))
        e1 = MT(r'$3$', 28).move_to(LEFT * 3.9 + DOWN * 0.5)
        e2 = MT(r'$3+4\cos\theta$', 28).move_to(e1)
        e3 = MT(r'$3+4\cos\theta+2\cos 2\theta$', 28, RED).move_to(e1)
        t1 = curve(ax, TH, 4 * np.cos(TH), ORANGE, 3)
        self.board.add(e1)
        self.add(e1)
        self.think('Your turn. With r of one equal to two, what is the new term, two r of one cos theta?', '$2\\,r[1]\\cos\\theta$ with $r[1]=2$ = ?', 4)
        self.say('T', "Add two times r of one, times cos theta. Two times two is four: four cos theta. The curve tilts: high at zero, low at pi.",
                 self.put(t1, rt=0.6), [Transform(s0, curve(ax, TH, 3 + 4 * np.cos(TH), RED, 5), run_time=1.5), Transform(e1, e2, run_time=1.5)])
        t2 = curve(ax, TH, 2 * np.cos(2 * TH), ORANGE, 3)
        self.say('T', "Add two times r of two, cos two theta. That is two cos two theta. And that is the answer: three plus four cos theta plus two cos two theta.",
                 [Transform(t1, t2, run_time=0.8)], [Transform(s0, curve(ax, TH, 3 + 4 * np.cos(TH) + 2 * np.cos(2 * TH), RED, 5), run_time=1.5), Transform(e1, e3, run_time=1.5)])
        self.c = (ax, s0, t1)

    def plot(self):
        self.header('pick the plot: evaluate the two ends')
        ax, s0, t1 = self.c
        d0 = Dot(ax.c2p(0, 9), color=RED, radius=0.1)
        d1 = Dot(ax.c2p(math.pi, 1), color=RED, radius=0.1)
        l0 = MT(r'$\theta=0$: $3+4+2=9$', 24).next_to(d0, UP + RIGHT, buff=0.1)
        l1 = MT(r'$\theta=\pi$: $3-4+2=1$', 24).next_to(d1, UP, buff=0.35).shift(LEFT * 1.7)
        self.say('T', "Now the plot question. You do not need to draw anything. Just evaluate the two ends.",
                 self.wipe_one(t1))
        self.think('Do it yourself first. What is P at theta equals zero? And at theta equals pi?', '$3+4\\cos\\theta+2\\cos2\\theta$:   $P(0)$ = ?   $P(\\pi)$ = ?', 8)
        self.say('T', "At theta equals zero, every cosine is one. Three plus four plus two: nine.", self.put(VGroup(d0, l0)))
        self.say('T', "At theta equals pi, cos pi is minus one and cos two pi is plus one. Three minus four plus two: one. So the right plot starts at nine on the left and ends at one on the right.",
                 self.put(VGroup(d1, l1)))
        self.say('S', "That's it? Two numbers?")
        self.say('T', "Two numbers. In April 2025 that was a quarter of a point, almost for free. And remember the picture: high on the left means a slow signal.")

    def wipe_one(self, m):
        from manim import FadeOut
        self.board.remove(m)
        return FadeOut(m, run_time=0.4)

    def ar1(self):
        self.header('the AR(1) model (April 2025, 3e)')
        m = MT(r'AR(1):   $x[n]=-a_1\,x[n-1]+i[n]$', 34).to_edge(UP, buff=0.65)
        sub = MT(r'today = a bit of yesterday + new white noise $i[n]$ (power $\sigma_i^2$)', 24, GREY).next_to(m, DOWN, buff=0.2)
        self.say('T', "Next: the AR model. AR means autoregressive. Today's value is a bit of yesterday's value plus fresh random noise. In the course's notation: x of n equals minus a one times x of n minus one, plus i of n. i of n is white noise with power sigma squared.",
                 self.wipe(), self.write(m), self.put(sub))
        self.say('S', "Why the minus sign?")
        self.say('T', "It is just the course's convention. Keep the minus, or every sign in your answer flips.")
        rec = card([r'$a_1=-\dfrac{r[1]}{r[0]}$',
                    r'$\sigma_i^2=r[0]+a_1\,r[1]$',
                    r'$P_{AR}(\theta)=\dfrac{\sigma_i^2}{1+a_1^2+2a_1\cos\theta}$'], 30).move_to(LEFT * 3.6 + DOWN * 0.6)
        self.say('T', "Fitting the model means choosing a one and sigma squared so that the model has the r values you were given. Three formulas. a one equals minus r one over r zero. Sigma squared equals r zero plus a one r one. And the PSD is sigma squared over one plus a one squared plus two a one cos theta.",
                 self.put(rec, rt=1.0))
        nums = stack([r'$r[0]=2$,  $r[1]=-\frac{1}{4}$',
                      r'$a_1=-\dfrac{-1/4}{2}=\dfrac{1}{8}$',
                      r'$\sigma_i^2=2+\frac{1}{8}\cdot(-\frac{1}{4})=\dfrac{63}{32}$',
                      r'$P_{AR}=\dfrac{63/32}{\frac{65}{64}+\frac{1}{4}\cos\theta}=\dfrac{126}{65+16\cos\theta}$'], 28, buff=0.3).move_to(RIGHT * 3.2 + DOWN * 0.6)
        self.think('Try it. With r zero equal to two and r one equal to minus a quarter, what is a one?', '$a_1=-r[1]/r[0]$ with $r[0]=2$, $r[1]=-1/4$ = ?', 6)
        self.say('T', "April 2025: r zero is two, r one is minus a quarter. a one is minus, minus a quarter, over two: plus one eighth.",
                 self.put(nums[0]), self.write(nums[1]))
        self.say('T', "Sigma squared is two plus one eighth times minus a quarter. Two minus one over thirty two: sixty three over thirty two.", self.write(nums[2]))
        self.say('T', "The denominator: one plus one sixty fourth plus a quarter cos theta. Multiply top and bottom by sixty four, and you get one hundred twenty six over sixty five plus sixteen cos theta.",
                 self.write(nums[3], 1.4))

    def ar2(self):
        self.header('AR(2): Yule–Walker (June 2026, 3d, 1 point)')
        yw = VGroup(matrix([['r[0]', 'r[1]'], ['r[1]', 'r[0]']]), matrix([['a₁'], ['a₂']]), Txt('=  −', 34),
                    matrix([['r[1]'], ['r[2]']])).arrange(RIGHT, buff=0.25).to_edge(UP, buff=0.75)
        self.say('T', "AR two has two coefficients, and you get them from the Yule Walker equations. A matrix with r zero on the diagonal and r one off the diagonal, times the vector a one, a two, equals minus the vector r one, r two.",
                 self.wipe(), self.put(yw, rt=1.2))
        self.say('S', "I hate matrices.")
        rows = stack([r'$3a_1+2a_2=-2$', r'$2a_1+3a_2=-1$'], 32).next_to(yw, DOWN, buff=0.45).shift(LEFT * 3.3)
        self.say('T', "It is just two equations. Row one: r zero a one plus r one a two equals minus r one. Row two: r one a one plus r zero a two equals minus r two. June 2026, with three, two and one: three a one plus two a two equals minus two, and two a one plus three a two equals minus one.",
                 self.write(rows, 1.4))
        sol = stack([r'$a_1=-\frac{4}{5}$,   $a_2=\frac{1}{5}$', r'check: $3(-\frac{4}{5})+2(\frac{1}{5})=-2$'], 28).next_to(rows, RIGHT, buff=1.0)
        self.think('Pause the video if you need to, and solve these two equations yourself.', 'solve  $3a_1+2a_2=-2$,  $2a_1+3a_2=-1$', 10)
        self.say('T', "Solve them any way you like. The answer is a one equals minus four fifths, a two equals one fifth. Always check row one: three times minus four fifths is minus twelve fifths, plus two fifths, gives minus two. Correct.",
                 self.write(sol, 1.2))
        s2 = MT(r'$\sigma_i^2=r[0]+a_1r[1]+a_2r[2]=3-\frac{8}{5}+\frac{1}{5}=\frac{8}{5}$', 30).next_to(VGroup(rows, sol), DOWN, buff=0.4)
        self.say('T', "Noise power: r zero plus a one r one plus a two r two. Three, minus eight fifths, plus one fifth: eight fifths.", self.write(s2))
        a = MT(r'$|A|^2=1+a_1^2+a_2^2+2(a_1+a_1a_2)\cos\theta+2a_2\cos 2\theta$', 30, PURPLE).next_to(s2, DOWN, buff=0.35)
        p = MT(r'$P_{AR}=\dfrac{\sigma_i^2}{|A|^2}=\dfrac{40}{42-48\cos\theta+10\cos 2\theta}$', 30, RED).next_to(a, DOWN, buff=0.3)
        self.say('T', "And the PSD is sigma squared over the magnitude squared of A. For AR two, that magnitude is one plus a one squared plus a two squared, plus two times a one plus a one a two, times cos theta, plus two a two cos two theta. Copy that formula onto your A4 sheet.",
                 self.write(a, 1.4))
        self.say('T', "Plug in the numbers and you get forty over forty two minus forty eight cos theta plus ten cos two theta.", self.write(p, 1.2))

    def ma1(self):
        self.header('the MA(1) model (April 2025, 3f)')
        m = MT(r'MA(1):   $x[n]=i[n]+b_1\,i[n-1]$', 34).to_edge(UP, buff=0.65)
        self.say('T', "Last model: MA one, a moving average. Today's value is today's noise plus a bit of yesterday's noise: x of n equals i of n plus b one times i of n minus one.",
                 self.wipe(), self.write(m))
        p = card([r'$P_{MA}(\theta)=r[0]+2r[1]\cos\theta$', r'April 2025:  $2-0.5\cos\theta$'], 32, color=RED).next_to(m, DOWN, buff=0.45)
        self.think('Guess. The MA one PSD is the correlogram, stopped after which lag?', 'MA(1) PSD = the correlogram stopped after lag ... ?', 4)
        self.say('T', "The good news: its PSD is simply r zero plus two r one cos theta. The correlogram, stopped after lag one. For April 2025: two minus zero point five cos theta.",
                 self.put(p))
        self.say('S', "And b one? They ask for the parameters too.")
        b = stack([r'$\dfrac{r[0]}{r[1]}=\dfrac{1+b_1^2}{b_1}$:    $\dfrac{2}{-1/4}=-8$   $\Rightarrow$   $b_1^2+8b_1+1=0$',
                   r'$b_1=-4\pm\sqrt{15}$:   $-0.127$  or  $-7.87$   $\Rightarrow$  keep $|b_1|<1$:  $b_1\approx-0.127$',
                   r'$\sigma_i^2=r[1]/b_1\approx1.97$'], 27).next_to(p, DOWN, buff=0.4)
        self.say('T', "Use r zero over r one equals one plus b squared, over b. In April 2025 that is minus eight, so b squared plus eight b plus one equals zero.", self.write(b[0], 1.2))
        self.say('T', "A quadratic always gives two roots, b and one over b. Keep the one smaller than one in size: minus four plus root fifteen, about minus zero point one two seven.", self.write(b[1], 1.2))
        self.say('T', "And sigma squared is r one over b one: about one point nine seven.", self.write(b[2]))

    def recap(self):
        self.header('recap')
        r = card([r'correlogram:  $r[0]+2r[1]\cos\theta+2r[2]\cos2\theta$   (do not double $r[0]$)',
                  r'pick the plot:  evaluate at $\theta=0$ (all $\cos=1$) and $\theta=\pi$ ($\cos\pi=-1$)',
                  r'AR(1):  $a_1=-r[1]/r[0]$,   $\sigma_i^2=r[0]+a_1r[1]$,   $P=\sigma_i^2/(1+a_1^2+2a_1\cos\theta)$',
                  r'AR(2):  Yule–Walker, two equations, $\sigma_i^2=r[0]+a_1r[1]+a_2r[2]$',
                  r'MA(1):  $P=r[0]+2r[1]\cos\theta$,   $b_1$ from the quadratic, keep $|b_1|<1$'], 24).move_to(UP * 0.5)
        self.say('S', "Give me the summary.", self.wipe())
        self.think('Before I summarise: say the AR one formulas out loud.', 'AR(1):  $a_1$ = ?    $\\sigma_i^2$ = ?', 7)
        self.say('T', "Correlogram: r zero plus two r k cos k theta. Pick the plot: evaluate at zero and at pi. AR one: a equals minus r one over r zero, and sigma squared equals r zero plus a r one. AR two: Yule Walker, two equations. MA one: the PSD is r zero plus two r one cos theta.",
                 self.put(r, rt=1.0))
        nxt = MT('Now: lesson 3.2 on the site, do November 2022 yourself.', 28, PURPLE).next_to(r, DOWN, buff=0.45)
        self.say('T', "Now go to lesson 3.2 on the site and do the November 2022 question on paper. Same formulas, different numbers.", self.put(nxt))
        self.say('S', "On it. Thanks, Ava.")
