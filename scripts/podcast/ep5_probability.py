"""Episode 5 · Block 1 in one go: Bayes with counts, joint PDFs, stationary/ergodic, spectral factorisation."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
from manim import (DOWN, LEFT, RIGHT, UP, Circle, Create, Cross, DashedLine, Dot, Line, Polygon, Rectangle,  # noqa: E402
                   RoundedRectangle, Square, Transform, ValueTracker, VGroup, always_redraw)
from podkit import Pod, card, chip, stack  # noqa: E402
from vidkit import BLUE, GREEN, GREY, INK, MT, ORANGE, PURPLE, RED, mk_axes  # noqa: E402


class Ep5Probability(Pod):
    episode = 'Episode 5 · Probability (block 1)'
    sections = ['intro', 'bayes', 'joint', 'wss', 'factor', 'recap']

    def intro(self):
        self.header('intro')
        self.say('T', "Episode five: block one, probability. It is worth one and a half points, split into four small questions that come back every year: a Bayes word problem, a joint PDF, a stationary or ergodic question, and a spectral factorisation.",
                 self.title_card('Block 1 in one go', 'Lessons 1.1 to 1.4 of the guide',
                                 [chip('4 small questions', RED), chip('1.5 points', BLUE), chip('often final answer only', GREEN)]))
        self.say('S', "Final answer only? So one arithmetic mistake and it's zero?")
        self.say('T', "Yes. So we go slowly, and we use tricks that make mistakes hard.")

    def bayes(self):
        self.header('Bayes word problems with counts (June 2026, 1b)')
        ex = card([r'June 2026 · 1b:  machines $M_1,M_2,M_3$ make 40 %, 35 %, 25 % of the chips.',
                   r'Defect rates: 2 %, 4 %, 5 %.   $P$(defective)?   $P(M_2\,|$ defective$)$?'], 25).to_edge(UP, buff=0.6)
        self.say('T', "Question one, Bayes. Three machines make chips: forty, thirty five and twenty five percent of them. Their defect rates are two, four and five percent. What is the probability that a random chip is defective? And given that it is defective, what is the probability it came from machine two?",
                 self.wipe(), self.put(ex))
        self.say('S', "Percentages of percentages. My brain is melting.")
        L, R, y, h = -6.2, 6.2, 0.35, 1.5
        whole = Rectangle(width=R - L, height=h, fill_color=GREY, fill_opacity=0.25, stroke_width=0).move_to([0, y, 0])
        wl = MT('1000 chips', 32).move_to(whole)
        self.say('T', "So do not use percentages. Use counts. Imagine exactly one thousand chips.", self.put(VGroup(whole, wl)))
        shares, rates, cols = [0.40, 0.35, 0.25], [0.02, 0.04, 0.05], [BLUE, PURPLE, GREEN]
        gap = 0.2
        span = R - L - 2 * gap
        segs, labs, x = VGroup(), VGroup(), L
        for s, c, nm in zip(shares, cols, ['M_1', 'M_2', 'M_3']):
            w = span * s
            segs.add(Rectangle(width=w, height=h, fill_color=c, fill_opacity=0.2, stroke_width=0).move_to([x + w / 2, y, 0]))
            labs.add(MT(f'${nm}$: {int(1000 * s)}', 26).move_to([x + w / 2, y + h / 2 + 0.3, 0]))
            x += w + gap
        self.board.remove(whole, wl)
        self.say('T', "Split them by machine: four hundred, three hundred fifty, two hundred fifty.",
                 [Transform(whole, segs, run_time=1.2), wl.animate(run_time=0.5).set_opacity(0)], self.put(labs))
        self.board.add(whole)
        reds, rl = VGroup(), VGroup()
        for seg, r, s in zip(segs, rates, shares):
            hh = h * r * 8
            reds.add(Rectangle(width=seg.width, height=hh, fill_color=RED, fill_opacity=0.85, stroke_width=0)
                     .align_to(seg, DOWN).align_to(seg, LEFT))
            rl.add(MT(f'{int(r * 100)} %  →  {1000 * s * r:g}', 22, RED).next_to(reds[-1], UP, buff=0.08))
        self.say('T', "Defective ones in each group. Two percent of four hundred is eight. Four percent of three hundred fifty is fourteen. Five percent of two hundred fifty is twelve and a half. Half a chip is fine, it is an average.",
                 self.put(reds), self.put(rl))
        pile = VGroup()
        bad = [8, 14, 12.5]
        x = L
        for b in bad:
            w = (R - L) * b / 34.5
            pile.add(Rectangle(width=w - 0.05, height=0.55, fill_color=RED, fill_opacity=0.85, stroke_width=0).move_to([x + w / 2, -1.15, 0]))
            x += w
        pl = VGroup(*[MT(f'{b:g}', 24, '#ffffff').move_to(p) for b, p in zip(bad, pile)])
        p1 = MT(r'$P(D)=\dfrac{8+14+12.5}{1000}=\dfrac{34.5}{1000}=0.0345$', 26).next_to(pile, DOWN, buff=0.2).align_to(pile, LEFT)
        self.board.remove(reds)
        self.think('Your turn. Add up the defective chips. How many out of the thousand?', '8 + 14 + 12.5 = ?   out of 1000', 5)
        self.say('T', "Throw all the defective chips on one pile: thirty four and a half out of a thousand. So the probability of a defective chip is zero point zero three four five.",
                 Transform(reds, pile, run_time=1.4), self.put(pl, rt=0.4), self.write(p1))
        self.board.add(reds)
        p2 = MT(r'$P(M_2\,|\,D)=\dfrac{14}{34.5}\approx0.41$', 26, RED).next_to(p1, RIGHT, buff=0.6)
        self.think('And given that a chip is defective, what is the probability it came from machine two?', '$P(M_2\\,|\\,D)$ = ?', 6)
        self.say('T', "Now, given that it is defective: look only at the pile. Fourteen of the thirty four and a half came from machine two. Fourteen divided by thirty four point five: zero point four one.",
                 self.write(p2))
        self.say('S', "So you divide by the pile, not by a thousand.")
        self.say('T', "Exactly. That is Bayes' rule. One trap: if they give you a quality rate, like eighty five percent good images, then the bad rate is fifteen percent. Convert first.")

    def joint(self):
        self.header('joint PDFs: draw the region, slice it (April 2024, 1c)')
        sq = Square(side_length=3.4, stroke_color=GREY, stroke_width=2).move_to(LEFT * 3.6 + UP * 0.2)
        o = sq.get_corner(DOWN + LEFT)
        P = lambda x, y: o + np.array([3.4 * x, 3.4 * y, 0])  # noqa: E731
        tri = Polygon(P(0, 0), P(1, 0), P(1, 1), fill_color=BLUE, fill_opacity=0.25, stroke_color=BLUE)
        ax = VGroup(MT('$x$', 24).next_to(P(1, 0), RIGHT, buff=0.15), MT('$y$', 24).next_to(P(0, 1), UP, buff=0.1),
                    MT('$0$', 20).next_to(P(0, 0), DOWN + LEFT, buff=0.08), MT('$1$', 20).next_to(P(1, 0), DOWN, buff=0.1),
                    MT('$1$', 20).next_to(P(0, 1), LEFT, buff=0.1), MT('$y=x$', 22, BLUE).next_to(P(0.55, 0.62), UP + LEFT, buff=0.05))
        ex = MT(r'April 2024 · 1c:   $p(x,y)=2$  on  $0\leq y\leq x\leq 1$.   Find $p_Y(y)$ and $p_{X|Y}(x\,|\,y)$.', 26).to_edge(UP, buff=0.6)
        self.say('T', "Question two, joint PDFs. You get a formula p of x and y that is non zero only on some region. They ask for a constant, a marginal, a conditional, or whether x and y are independent.",
                 self.wipe(), self.put(ex))
        self.say('T', "Rule number one: always draw the region. April 2024: p equals two, where y is between zero and x, and x is at most one. y below x: that is the triangle under the diagonal.",
                 self.put(VGroup(sq, ax)), self.put(tri))
        yv = ValueTracker(0.3)
        sl = always_redraw(lambda: Line(P(yv.get_value(), yv.get_value()), P(1, yv.get_value()), color=RED, stroke_width=6))
        sd = always_redraw(lambda: VGroup(Dot(P(yv.get_value(), yv.get_value()), color=RED), Dot(P(1, yv.get_value()), color=RED)))
        e = [MT(r'slice at height $y$:  $x$ goes from $y$ to $1$', 28),
             MT(r'$p_Y(y)=\int_y^{1}2\,dx=2(1-y)$,   $0\leq y\leq1$', 30, RED),
             MT(r'$p_{X|Y}(x\,|\,y)=\dfrac{2}{2(1-y)}=\dfrac{1}{1-y}$,   $y\leq x\leq 1$', 30)]
        VGroup(*e).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(RIGHT * 2.9 + UP * 0.2)
        self.say('T', "The marginal of y: stand at height y and walk across the region. You enter at the diagonal, where x equals y, and you leave at x equals one.",
                 self.put(VGroup(sl, sd), rt=0.6), yv.animate(run_time=2.5).set_value(0.75), yv.animate(run_time=1.5).set_value(0.3), self.write(e[0]))
        self.think('Your turn. Integrate two, from x equals y to x equals one.', '$\\int_y^{1}2\\,dx$ = ?', 5)
        self.say('T', "So integrate two from y to one. That is two times one minus y. And write the domain: y between zero and one.", self.write(e[1], 1.2))
        self.say('T', "The conditional is the joint divided by the marginal: two over two times one minus y, which is one over one minus y, for x between y and one.", self.write(e[2], 1.2))
        ind = card([r'Independent  $\Leftrightarrow$  region is a RECTANGLE  and  $p=f(x)\,g(y)$',
                    r'June 2026: $6x^2y$ on the unit square  $\Rightarrow$  independent ($3x^2\cdot 2y$).   Triangle: never.'], 24).to_edge(DOWN, buff=1.7)
        self.say('T', "Independence has a quick test. The region must be a rectangle, and the formula must split into a function of x times a function of y. June 2026 had six x squared y on the unit square: independent. A triangle is never independent.",
                 self.put(ind))

    def wss(self):
        self.header('stationary and ergodic (the dice)')
        rng = np.random.default_rng(5)
        rows = VGroup()
        for r in range(4):
            vals = rng.integers(1, 7, 28)
            rows.add(VGroup(*[Dot([-5.6 + 0.4 * i, 2.6 - 0.75 * r + 0.08 * (v - 3.5), 0], radius=0.06, color=INK if r == 0 else GREY) for i, v in enumerate(vals)]))
        names = VGroup(*[MT(f'die {r + 1}', 20, GREY).next_to(rows[r], LEFT, buff=0.25) for r in range(4)])
        col = RoundedRectangle(corner_radius=0.12, width=0.32, height=2.9, fill_color=BLUE, fill_opacity=0.15, stroke_width=0).move_to([-5.6 + 0.4 * 9, 1.475, 0])
        row = RoundedRectangle(corner_radius=0.12, width=11.6, height=0.6, fill_color=RED, fill_opacity=0.12, stroke_width=0).move_to(rows[0])
        cl = MT('down a column: ensemble mean', 22, BLUE).next_to(col, DOWN, buff=0.1).shift(RIGHT * 1.6)
        rl = MT('along a row: time average', 22, RED).next_to(row, UP, buff=0.02).align_to(row, RIGHT)
        self.say('T', "Question three, stationary and ergodic. A random process is a whole stack of signals. Picture infinitely many dice, each rolled forever. Each die gives one row of numbers.",
                 self.wipe(), self.put(VGroup(rows, names), rt=1.0))
        self.say('T', "There are two ways to average. Down a column: all the dice at the same moment. That is the ensemble mean. Along a row: one die over all time. That is the time average.",
                 self.put(VGroup(col, cl)), self.put(VGroup(row, rl)))
        defs = card([r'WSS: the column average is the same at every time, and the correlation depends only on the gap.',
                     r'Ergodic: the row average EQUALS the column average.'], 23).to_edge(DOWN, buff=1.65)
        self.say('T', "Wide sense stationary, WSS, means the column average is the same at every time, and the correlation between two times depends only on the gap between them. Ergodic means the row average equals the column average.",
                 self.put(defs))
        self.say('S', "So the dice?")
        ans = card([r'dice: row $3.5$ = column $3.5$  $\Rightarrow$  ergodic in mean AND variance',
                    r'$X=A$ random constant: row $=A\neq E[A]$  $\Rightarrow$  WSS but NOT ergodic',
                    r'$A\cos t$: mean $=E[A]\cos t$ changes with $t$  $\Rightarrow$  NOT WSS'], 23, color=INK).to_edge(DOWN, buff=1.65)
        self.board.remove(defs)
        self.think('Think. Is the dice process ergodic? Imagine one single die, rolled forever.', 'dice: ergodic? in the mean? in the variance?', 5)
        self.say('T', "Every die is the same fair die, so one die rolled forever averages three point five, exactly like the column. Ergodic in the mean and in the variance. If instead each row is a flat line at its own random height A, the row average is A, not the expected value of A: WSS, but not ergodic. And A times cos t has a mean that changes with time: not even WSS.",
                 Transform(defs, ans, run_time=1.0))
        self.board.add(defs)

    def factor(self):
        self.header('spectral factorisation (April 2025, 1e)')
        ex = MT(r'April 2025 · 1e:   $P_x(\theta)=\dfrac{1}{61+60\cos\theta}$.   Find $L(z)$ and $\sigma_i^2$.', 28).to_edge(UP, buff=0.6)
        self.say('T', "Question four, spectral factorisation. They give a PSD like one over sixty one plus sixty cos theta, and you have to find a filter L of z and a noise power sigma squared that produce it.",
                 self.wipe(), self.put(ex))
        idea = MT(r'$L(z)=\dfrac{1}{1+a\,z^{-1}}$   $\Rightarrow$   $P=\dfrac{\sigma_i^2}{1+a^2+2a\cos\theta}$', 27, PURPLE).next_to(ex, DOWN, buff=0.25)
        self.say('T', "The filter is always one over one plus a z to the minus one. Its PSD is sigma squared over one plus a squared plus two a cos theta. So we must write sixty one plus sixty cos theta in that shape, times some constant C.",
                 self.write(idea, 1.2))
        e = [MT(r'match:  $C(1+a^2)=61$,   $2Ca=60$', 25),
             MT(r'divide:  $\dfrac{1+a^2}{2a}=\dfrac{61}{60}$   $\Rightarrow$   $30a^2-61a+30=0$   $\Rightarrow$   $a=\dfrac{5}{6}$ or $\dfrac{6}{5}$', 25),
             MT(r'keep $|a|<1$ (inside the unit circle, minimum phase):   $a=\dfrac{5}{6}$', 25, RED),
             MT(r'$C=\dfrac{60}{2\cdot 5/6}=36$   $\Rightarrow$   $\sigma_i^2=\dfrac{1}{36}$,    $L(z)=\dfrac{1}{1+\frac{5}{6}z^{-1}}$', 25)]
        VGroup(*e).arrange(DOWN, buff=0.2).next_to(idea, DOWN, buff=0.25)
        self.say('T', "Match the pieces. The constant: C times one plus a squared equals sixty one. The cosine: two C a equals sixty.", self.write(e[0]))
        self.say('T', "Divide one by the other and C disappears. You get a quadratic, thirty a squared minus sixty one a plus thirty equals zero, with two roots: five sixths and six fifths.", self.write(e[1], 1.3))
        self.think('Which root do you keep, five sixths or six fifths? And why?', 'keep $a=5/6$ or $a=6/5$? why?', 5)
        self.say('T', "They always come as a pair, a and one over a. Keep the one inside the unit circle, five sixths. That is called minimum phase, and it was a multiple choice answer in June 2026.", self.write(e[2], 1.2))
        self.say('T', "Then C is sixty over two times five sixths, which is thirty six. So sigma squared is one over thirty six, and L of z is one over one plus five sixths z to the minus one.", self.write(e[3], 1.3))
        self.say('S', "And if it's a minus cosine?")
        self.say('T', "Then a comes out negative. April 2024 had twenty five minus twenty four cos theta: a is minus three quarters, so L is one over one minus three quarters z to the minus one, and sigma squared is seven sixteenths.")

    def recap(self):
        self.header('recap')
        r = card([r'Bayes: 1000 items, split, take the bad ones, divide by the PILE',
                  r'joint PDF: DRAW the region, slice it, limits from the drawing, always give the domain',
                  r'WSS: constant mean + correlation by gap only.   Ergodic: row average = column average.   Dice: both.',
                  r'factorisation: $C(1+a^2)=A$, $2Ca=B$, keep $|a|<1$, $\sigma_i^2=N/C$'], 24).move_to(UP * 0.5)
        self.say('S', "The thirty second version?", self.wipe())
        self.think('Before the summary: say the four tricks of block one out loud.', 'say the four block-1 tricks out loud', 8)
        self.say('T', "Bayes: count a thousand items and divide by the pile. Joint PDFs: draw the region and slice it. WSS: constant mean and correlation by gap. Ergodic: the row average equals the column average. Factorisation: match, divide, keep a inside the circle.",
                 self.put(r, rt=1.0))
        nxt = MT('Now: lessons 1.1 to 1.4, the "Your turn" questions, on paper.', 28, PURPLE).next_to(r, DOWN, buff=0.45)
        self.say('T', "Now do the your turn questions in lessons one point one to one point four, on paper. And then, a full mock exam: April 2025, three hours, timed.", self.put(nxt))
        self.say('S', "Deal. Thanks, Ava.")
