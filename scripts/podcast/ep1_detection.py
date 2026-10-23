"""Episode 1 · Detection: the likelihood ratio test (lessons 4.1 and 4.2)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from manim import (DOWN, LEFT, RIGHT, UP, Create, DashedLine, Dot, FadeIn, FadeOut, Indicate, MarkupText, Rectangle,
                   SurroundingRectangle, ValueTracker, VGroup, always_redraw)
from podkit import Pod, card, chip, np_grid, stack
from vidkit import BLUE, FONT, GREEN, GREY, INK, MT, ORANGE, PURPLE, RED, area, curve, mk_axes


def npdf(x, m=0.0):
    return np.exp(-(np.asarray(x) - m) ** 2 / 2) / math.sqrt(2 * math.pi)


def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


class Det(VGroup):
    """Two PDFs, a threshold gamma, the decide bands, P_FA (blue) and P_M (red) areas, live numbers."""

    def __init__(self, f0, f1, F0, F1, xr, yr, side='>', g=1.0, prior=None, ticks=(), w=9.6, h=3.2,
                 center=UP * 0.45, names=('H_0', 'H_1'), show_areas=True):
        super().__init__()
        ax = mk_axes(xr, yr, w, h).move_to(center)
        xs = np_grid(xr[0], xr[1], 320)
        self.g = ValueTracker(g)
        self.prior = prior
        w0 = lambda: 1 - prior.get_value() if prior else 1.0  # noqa: E731
        w1 = lambda: prior.get_value() if prior else 1.0  # noqa: E731

        def zone(h1):
            gv = self.g.get_value()
            right = (side == '>') == h1
            sel = xs[xs >= gv] if right else xs[xs <= gv]
            return np.r_[gv, sel] if right else np.r_[sel, gv]

        c0 = always_redraw(lambda: curve(ax, xs, w0() * f0(xs), BLUE, 4))
        c1 = always_redraw(lambda: curve(ax, xs, w1() * f1(xs), RED, 4))
        top = ax.c2p(xr[0], yr[1])[1] + 0.28

        def bands():
            gx = ax.c2p(self.g.get_value(), 0)[0]
            x0, x1 = ax.c2p(xr[0], 0)[0], ax.c2p(xr[1], 0)[0]
            lcol, rcol = (BLUE, RED) if side == '>' else (RED, BLUE)
            lt, rt = ('decide H<sub>0</sub>', 'decide H<sub>1</sub>') if side == '>' else ('decide H<sub>1</sub>', 'decide H<sub>0</sub>')
            grp = VGroup()
            for a, b, col, t in ((x0, gx, lcol, lt), (gx, x1, rcol, rt)):
                if b - a > 0.05:
                    grp.add(Rectangle(width=b - a, height=0.36, fill_color=col, fill_opacity=0.15, stroke_width=0)
                            .move_to([(a + b) / 2, top, 0]))
                if b - a > 1.6:
                    grp.add(MarkupText(t, font=FONT, font_size=16, color=INK).move_to([(a + b) / 2, top, 0]))
            return grp

        line = always_redraw(lambda: DashedLine(ax.c2p(self.g.get_value(), 0), [ax.c2p(self.g.get_value(), 0)[0], top + 0.18, 0],
                                                color=INK, stroke_width=3))
        glab = always_redraw(lambda: MT(r'$\gamma=%.2f$' % self.g.get_value(), 20).next_to(ax.c2p(self.g.get_value(), 0), DOWN, buff=0.12))
        tk = VGroup(*[MT(f'${v}$', 18, GREY).next_to(ax.c2p(v, 0), DOWN, buff=0.45) for v in ticks])
        self.ax, self.c0, self.c1, self.line, self.glab, self.ticks = ax, c0, c1, line, glab, tk
        self.bands = always_redraw(bands)
        self.fa = always_redraw(lambda: area(ax, zone(True), w0() * f0(zone(True)), BLUE, 0.38))
        self.pm = always_redraw(lambda: area(ax, zone(False), w1() * f1(zone(False)), RED, 0.38))

        def errs():
            gv = self.g.get_value()
            pfa = 1 - F0(gv) if side == '>' else F0(gv)
            pm = F1(gv) if side == '>' else 1 - F1(gv)
            return pfa, pm

        self.errs = errs
        self.nums = always_redraw(lambda: VGroup(
            MarkupText(f'P<sub>FA</sub> = {errs()[0]:.3f}', font=FONT, font_size=20, color=BLUE),
            MarkupText(f'P<sub>M</sub> = {errs()[1]:.3f}', font=FONT, font_size=20, color=RED),
            MarkupText(f'P<sub>D</sub> = {1 - errs()[1]:.3f}', font=FONT, font_size=20, color=INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(ax, RIGHT, buff=0.35).shift(UP * 0.4))
        pk0 = xs[np.argmax(f0(xs))]
        pk1 = xs[np.argmax(f1(xs))]
        self.n0 = MT(f'${names[0]}$', 26, BLUE).next_to(ax.c2p(pk0, f0(np.array([pk0]))[0]), UP + LEFT * 0.6, buff=0.1)
        self.n1 = MT(f'${names[1]}$', 26, RED).next_to(ax.c2p(pk1, f1(np.array([pk1]))[0]), UP + RIGHT * 0.6, buff=0.1)
        ax.get_y_axis().set_stroke(opacity=0)
        self.add(ax, tk, c0, c1, self.n0, self.n1)


GAUSS = dict(center=DOWN * 0.3, f0=lambda x: npdf(x), f1=lambda x: npdf(x, 2), F0=Phi, F1=lambda x: Phi(x - 2),
             xr=[-3.5, 5.5, 1], yr=[0, 0.45, 0.1], ticks=(-2, 0, 2, 4))
EXPO = dict(f0=lambda y: np.exp(-np.asarray(y)), f1=lambda y: 2 * np.exp(-2 * np.asarray(y)),
            F0=lambda y: 1 - math.exp(-y), F1=lambda y: 1 - math.exp(-2 * y), xr=[0, 4, 1], yr=[0, 2.1, 0.5],
            ticks=(0, 1, 2, 3, 4), side='<', names=('e^{-y}', '2e^{-2y}'), center=DOWN * 0.3)


class Ep1Detection(Pod):
    episode = 'Episode 1 · Detection'
    sections = ['intro', 'story', 'errors', 'recipe', 'apr25', 'flip', 'priors', 'theory', 'recap']

    def intro(self):
        self.header('intro')
        self.say('T', "Welcome to Pass 5CTA0. I'm Ava, and with me is Ben, who knows nothing about this course.",
                 self.title_card('Detection: the likelihood ratio test', 'Lessons 4.1 and 4.2 of the guide',
                                 [chip('in 9 of 9 exams', RED), chip('2 to 2.5 points', BLUE), chip('very mechanical', GREEN)]))
        self.say('S', "Literally nothing. And the exam is on Monday.")
        self.say('T', "Perfect. Today is detection. It is in every single exam, worth about two points, and it is the most mechanical part of the paper. Learn one recipe and those points are yours.")

    def story(self):
        self.header('what the question looks like')
        self.say('S', "OK. What does a detection question even look like?", self.wipe())
        h0 = card(['$H_0$: nothing is there', '(just noise, no device, a real student)'], 24, width=6.0)
        h1 = card(['$H_1$: something is there', '(a signal, a device, an AI cheater)'], 24, width=6.0)
        VGroup(h0, h1).arrange(RIGHT, buff=0.6).move_to(UP * 0.6)
        self.say('T', "You measure one number, called x. And there are two possible stories that could explain it. Story H zero: nothing is there, it is just noise. Story H one: something is there.",
                 self.put(h0), self.put(h1))
        self.d = d = Det(**GAUSS)
        self.say('T', "Each story comes with a curve, called a PDF, a probability density. It says which values of x are likely under that story. Where the curve is high, the value is likely.",
                 self.wipe(), self.put(d, rt=1.2))
        self.say('S', "So the blue one is the nothing-there story, and the red one is the something-there story.")
        x = 1.5
        ax = d.ax
        v0, v1 = float(npdf(x)), float(npdf(x, 2))
        sticks = VGroup(DashedLine(ax.c2p(x, 0), ax.c2p(x, 0.43), color=GREY),
                        MT('$x=1.5$', 22).next_to(ax.c2p(x, 0.43), UP, buff=0.08),
                        Dot(ax.c2p(x, v0), color=BLUE, radius=0.08),
                        Dot(ax.c2p(x, v1), color=RED, radius=0.08),
                        MT(f'${v0:.2f}$', 20, BLUE).next_to(ax.c2p(x, v0), LEFT, buff=0.15),
                        MT(f'${v1:.2f}$', 20, RED).next_to(ax.c2p(x, v1), RIGHT, buff=0.15))
        self.say('T', "Now suppose you measure x equals one point five. Look at both curves at one point five. Which one is higher?",
                 self.put(sticks, rt=1.0))
        self.think('Pause and answer before Ben does: which curve is higher at one point five, the blue or the red?', 'which curve is higher at $x=1.5$?', 4)
        self.say('S', "The red one. A bit higher.")
        eq = MT(r'$L(x)=\dfrac{p(x\,|\,H_1)}{p(x\,|\,H_0)}=\dfrac{%.2f}{%.2f}=%.2f$' % (v1, v0, v1 / v0), 28).move_to([-3.4, 2.75, 0])
        self.say('T', "So this measurement fits story H one better. The likelihood ratio test just makes that precise. Divide the height of the red curve by the height of the blue curve.",
                 self.write(eq, 1.2))
        rule = card([r'ratio $>\lambda$  $\Rightarrow$  decide $H_1$', r'ratio $<\lambda$  $\Rightarrow$  decide $H_0$'], 22).move_to([3.6, 2.75, 0])
        self.say('T', "If the ratio is bigger than some number lambda, you decide H one. If it is smaller, you decide H zero. Lambda is just how convinced you need to be before you shout H one.",
                 self.put(rule))
        self.say('T', "Notice the order: always the H one curve on top, the H zero curve at the bottom.",
                 Indicate(eq, color=RED, run_time=1.2))
        self.leftovers = VGroup(sticks, eq, rule)

    def errors(self):
        self.header('the threshold and the two mistakes')
        d = self.d
        self.board.remove(*self.leftovers)
        self.say('S', "And where do the points come from?", FadeOut(self.leftovers, run_time=0.5))
        self.say('T', "After a bit of algebra, the ratio test always turns into a simple cut on the x axis. Decide H one when x is bigger than a threshold, called gamma. Everything to the right of the line: H one. To the left: H zero.",
                 [Create(d.line, run_time=0.8), FadeIn(d.glab, run_time=0.8)], self.put(d.bands, rt=0.8))
        self.board.add(d.line, d.glab)
        self.think('Think first. A false alarm means nothing was there, but you said H one. Which curve is that, and which side of the line?', 'false alarm = which curve, which side?', 5)
        self.say('T', "Because the curves overlap, you will make mistakes. Two kinds. The first is a false alarm: nothing was there, but you said H one. That is the part of the blue curve on the right of the line. Its area is P F A, the probability of false alarm.",
                 self.put(d.fa, rt=1.0))
        self.say('T', "The second is a miss: something was there, but you said H zero. That is the part of the red curve on the left of the line. Its area is P M, the probability of a miss.",
                 self.put(d.pm, rt=1.0))
        self.say('S', "And detection?", self.put(d.nums, rt=0.6))
        self.say('T', "P D, the probability of detection, is the rest of the red curve, the part in the decide H one zone. So P D is one minus P M.")
        self.think('Predict it. If I push the line to the right, what happens to P F A, and what happens to P M?', 'line moves right:  $P_{FA}$ ?  $P_M$ ?', 5)
        self.say('T', "Now watch what happens when I push the threshold to the right.",
                 d.g.animate(run_time=3).set_value(2.6))
        self.say('S', "The blue area shrinks, the red area grows. Fewer false alarms, but more misses.")
        self.say('T', "Always. Moving the line can never shrink both. And now to the left.",
                 d.g.animate(run_time=3).set_value(-0.3), d.g.animate(run_time=1.5).set_value(1.0))
        self.say('T', "Remember the colours, because the exam asks you to shade these areas. P F A lives under the H zero curve. P M and P D live under the H one curve. People lose points by shading the wrong curve.")

    def recipe(self):
        self.header('the recipe')
        steps = [r'1. Ratio:  $\dfrac{p(x\,|\,H_1)}{p(x\,|\,H_0)}>\lambda$',
                 r'2. Take $\ln$ of both sides  ($\ln e^{u}=u$, $\ln(ab)=\ln a+\ln b$)',
                 r'3. Isolate $x$.  Multiply or divide by a NEGATIVE number $\Rightarrow$ FLIP $>$ into $<$',
                 r'4. Write the rule:  decide $H_1$ if $x>\gamma$  (or $x<\gamma$ after a flip)',
                 r'5. $P_{FA}=\int p(x\,|\,H_0)$ over the decide-$H_1$ zone,   $P_D=\int p(x\,|\,H_1)$ over the same zone']
        rows = [MT(s, 26) for s in steps]
        VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.38).move_to(UP * 0.5)
        self.say('T', "Here is the recipe. Five steps, every single time.", self.wipe(), self.put(MT('The LRT recipe', 34).to_edge(UP, buff=0.65)))
        self.say('T', "One. Write the ratio: the H one PDF divided by the H zero PDF, bigger than lambda.", self.put(rows[0]))
        self.say('T', "Two. Take the natural log of both sides. The log is an increasing function, so the inequality keeps its direction. And the log kills exponentials: log of e to the u is just u.", self.put(rows[1]))
        self.say('T', "Three. Isolate x. And here is the big trap. If you multiply or divide by a negative number, you must flip the inequality. Bigger than becomes smaller than.", self.put(rows[2]))
        box = SurroundingRectangle(rows[2], color=RED, buff=0.1)
        self.say('S', "Flip when negative. Got it.", self.put(box, Create, 0.6))
        self.say('T', "Four. Write the final rule. Decide H one if x is bigger than gamma, or smaller than gamma if you flipped.", self.put(rows[3]))
        self.say('T', "Five. The error probabilities. P F A is the area of the H zero curve over the zone where you decide H one. P D is the area of the H one curve over that same zone.", self.put(rows[4]))

    def apr25(self):
        self.header('worked example: April 2025, 4a (0.5 p)')
        ex = card([r'April 2025 · 4a · 0.5 p',
                   r'One data point $x$, $0<x<1$, with $p(x)=k_1\theta\, x^{k_2\theta-1}$.',
                   r'$H_0:\ \theta=3$,    $H_1:\ \theta=6$.    $\lambda=0.2$,  $k_1=1$,  $k_2=2$.',
                   r'For which $x$ should $H_1$ be accepted?'], 24).to_edge(UP, buff=0.6)
        self.say('S', "Can we do a real exam question?", self.wipe())
        self.say('T', "April 2025, question 4a, half a point. One data point x between zero and one. The PDF is theta times x to the power two theta minus one. H zero says theta is three. H one says theta is six. And lambda is zero point two.",
                 self.put(ex, rt=1.0))
        e = [MT(r'$H_0:\ 3x^{5}$        $H_1:\ 6x^{11}$', 32),
             MT(r'$\dfrac{6x^{11}}{3x^{5}}=2x^{6}>0.2$', 34),
             MT(r'$x^{6}>0.1$   $\Rightarrow$   $x>0.1^{1/6}\approx0.681$', 34)]
        VGroup(*e).arrange(DOWN, buff=0.4).next_to(ex, DOWN, buff=0.45)
        self.say('T', "Step one, write both PDFs. Under H zero, theta is three, so two theta minus one is five: three x to the fifth. Under H one, theta is six: six x to the eleventh.", self.write(e[0]))
        self.think('Your turn. Write the ratio of the two PDFs and simplify it.', 'simplify $6x^{11}\\,/\\,(3x^{5})$', 6)
        self.say('T', "Step two, the ratio. Six x to the eleventh over three x to the fifth. Six over three is two. And x to the eleven over x to the five is x to the six: you subtract the powers.", self.write(e[1]))
        self.say('S', "So two x to the six has to be bigger than zero point two.")
        self.think('Now isolate x. Do you need to flip the inequality or not?', 'isolate $x$ in $2x^6>0.2$: flip or not?', 6)
        self.say('T', "Divide by two. Two is positive, so no flip: x to the six bigger than zero point one. Take the sixth root of both sides: x bigger than zero point one to the power one sixth. On the calculator that is zero point six eight one.", self.write(e[2]))
        ans = card([r'Accept $H_1$ for $0.681<x<1$'], 30, color=GREEN).next_to(e[2], DOWN, buff=0.4)
        self.say('T', "So you accept H one when x is between zero point six eight one and one. Half a point, in four lines.", self.put(ans))

    def flip(self):
        self.header('the flip: November 2022, 4c to 4e')
        ex = card([r'November 2022 · 4c–4e',
                   r'$H_0:\ p(x)=\frac{1}{2}e^{-|x|}$      $H_1:\ p(x)=e^{-2|x|}$,    $N$ independent samples $x_n$'], 24).to_edge(UP, buff=0.6)
        self.say('S', "You said the flip is the big trap. Show me one.", self.wipe())
        self.say('T', "November 2022. Under H zero, the PDF is one half e to the minus absolute value of x. Under H one, e to the minus two absolute x. And now you have N independent samples.", self.put(ex))
        e = [MT(r'one sample:  $\dfrac{e^{-2|x|}}{\frac{1}{2}e^{-|x|}}=2e^{-|x|}$', 30),
             MT(r'$N$ samples:  $2^{N}e^{-\sum_n|x_n|}>\gamma$', 30),
             MT(r'$\ln$:  $N\ln 2-\sum_n|x_n|>\ln\gamma$', 30),
             MT(r"$\times(-1)$, FLIP:   $\sum_n|x_n|<N\ln 2-\ln\gamma=\gamma'$", 30, RED)]
        VGroup(*e).arrange(DOWN, buff=0.32).next_to(ex, DOWN, buff=0.4)
        self.say('T', "The ratio for one sample: e to the minus two absolute x, over one half e to the minus absolute x. That is two times e to the minus absolute x.", self.write(e[0]))
        self.say('T', "With N independent samples you multiply N of those. Two to the N, times e to the minus the sum of the absolute values.", self.write(e[1]))
        self.say('T', "Take the log. N log two, minus the sum, bigger than log gamma.", self.write(e[2]))
        self.think('What happens to the bigger than sign when you multiply both sides by minus one?', 'multiply by $-1$: what happens to $>$ ?', 4)
        self.say('T', "Now isolate the sum. It has a minus sign in front. To get rid of it, multiply everything by minus one, and bigger than becomes smaller than.", self.write(e[3]))
        self.say('S', "So we decide H one when the sum is small? That feels backwards.")
        d = Det(**EXPO, g=1.0)
        self.say('T', "Look at the curves and it makes sense. With one sample, call y the absolute value. Under H zero, y has PDF e to the minus y. Under H one, two e to the minus two y. The red curve is the tall one near zero.",
                 self.wipe(), self.put(d, rt=1.0))
        self.say('T', "So small values point to H one. Decide H one to the left of the threshold. The false alarm area is now on the left, under the blue curve, and the miss is on the right, under the red curve.",
                 [Create(d.line, run_time=0.6), FadeIn(d.glab, run_time=0.6)], self.put(d.bands, rt=0.6), [FadeIn(d.fa), FadeIn(d.pm)], self.put(d.nums, rt=0.5))
        self.board.add(d.line, d.glab, d.fa, d.pm)
        calc = stack([r'$P_{FA}=\int_0^{\gamma}e^{-y}dy=1-e^{-\gamma}=0.1$  $\Rightarrow$  $\gamma=-\ln 0.9\approx0.105$',
                      r'$P_D=\int_0^{\gamma}2e^{-2y}dy=1-e^{-2\gamma}=1-0.9^{2}=0.19$'], 26).to_edge(UP, buff=0.55)
        self.say('T', "Part e asks for the threshold that gives a false alarm probability of zero point one. P F A is the integral of e to the minus y from zero to gamma: one minus e to the minus gamma. Set that to zero point one. Then e to the minus gamma is zero point nine, so gamma is minus log zero point nine, about zero point one zero five.",
                 d.g.animate(run_time=2).set_value(0.105), self.put(calc[0]))
        self.say('T', "And P D is one minus e to the minus two gamma, which is one minus zero point nine squared. Zero point one nine.", self.put(calc[1]))

    def priors(self):
        self.header('priors and costs (lesson 4.2)')
        self.say('S', "What if one story is much more common than the other?", self.wipe())
        pr = ValueTracker(0.5)
        d = Det(**GAUSS, prior=pr)
        d.g.add_updater(lambda m: m.set_value(1 + math.log((1 - pr.get_value()) / pr.get_value()) / 2))
        self.add(d.g)
        lab = always_redraw(lambda: MarkupText(f'P(H<sub>1</sub>) = {pr.get_value():.2f}', font=FONT, font_size=22, color=RED)
                            .next_to(d.ax, RIGHT, buff=0.35).shift(UP * 0.9))
        self.say('T', "Then you use priors. P zero is how often H zero happens, P one how often H one happens. Bayes says: multiply each curve by its prior, and decide H one wherever the red hill is the taller one.",
                 self.put(d, rt=1.0), [Create(d.line, run_time=0.6), FadeIn(d.glab, run_time=0.6), FadeIn(lab, run_time=0.6)], self.put(d.bands, rt=0.5))
        self.board.add(d.line, d.glab, lab)
        self.think('Predict it. If H one becomes rare, does the threshold move left or right?', '$P(H_1)$ drops: does the line move left or right?', 5)
        self.say('T', "Watch. If devices become rare, so P one drops to zero point one, the red hill shrinks and the crossing point moves right. You need stronger evidence before you say H one.",
                 pr.animate(run_time=3.5).set_value(0.1))
        self.say('S', "And if H one becomes common, the line moves left. H one gets easier.",
                 pr.animate(run_time=3).set_value(0.8), pr.animate(run_time=1.5).set_value(0.5))
        d.g.clear_updaters()
        f = card([r'$\dfrac{p(x\,|\,H_1)}{p(x\,|\,H_0)}>\lambda=\dfrac{C_{10}\,P_0}{C_{01}\,P_1}$',
                  r'$C_{10}$ = cost of a false alarm,   $C_{01}$ = cost of a miss',
                  r'equal costs:  $\lambda=P_0/P_1$'], 26).move_to(UP * 0.6)
        self.say('T', "In formulas, it is the same ratio test. Only lambda changes. Lambda equals C one zero times P zero, over C zero one times P one. C one zero is the cost of a false alarm, C zero one the cost of a miss. With equal costs, lambda is just P zero over P one.",
                 self.wipe(), self.put(f))
        e1 = MT(r'June 2026:  $P_0=0.9$, $P_1=0.1$, equal costs  $\Rightarrow$  $\lambda=0.9/0.1=9$', 28).next_to(f, DOWN, buff=0.4)
        self.say('T', "June 2026, question 4c: P zero is zero point nine, P one is zero point one, equal costs. Lambda is zero point nine over zero point one: nine. Then you run the same five-step recipe with lambda equal to nine.", self.write(e1))
        self.say('S', "And the AI cheating question?")
        e2 = stack([r'April 2025:  miss costs $100\times$ a false alarm;  posterior of $H_1$ is $5\times$ that of $H_0$',
                    r'decide $H_1$ if  $\dfrac{P(H_1\,|\,x)}{P(H_0\,|\,x)}>\dfrac{C_{10}}{C_{01}}$:    $5>\dfrac{1}{100}$  $\Rightarrow$  accept $H_1$, the student fails'], 25).next_to(e1, DOWN, buff=0.35)
        self.say('T', "April 2025. An AI detector. A miss costs a hundred times more than a false alarm, and the posterior of H zero is five times smaller than the posterior of H one. When they give you posteriors, the priors are already inside. Compare the posterior ratio, five, with the cost ratio, one over a hundred. Five is bigger, so you accept H one. The student fails.",
                 self.put(e2, rt=1.0))

    def theory(self):
        self.header('the multiple-choice sentences')
        cards = [card([r'Neyman–Pearson: fix $P_{FA}$, then MAXIMISE $P_D$.'], 28, width=11.5),
                 card([r'Bayes detection MINIMISES the Bayes risk (expected cost).', r'Costs 0 for right, 1 for wrong  $\Rightarrow$  minimises the probability of error.'], 28, width=11.5),
                 card([r'Raising $P(H_1)$ LOWERS the threshold: $H_1$ gets easier, not harder.'], 28, width=11.5)]
        VGroup(*cards).arrange(DOWN, buff=0.35).move_to(UP * 0.5)
        self.say('T', "Last, the multiple choice. Three sentences come back almost every year, sometimes with one word swapped.", self.wipe())
        self.think('True or false: Neyman Pearson fixes the false alarm probability, and then minimises the detection probability.', 'NP fixes $P_{FA}$ and MINIMISES $P_D$. True or false?', 4)
        self.say('T', "One. Neyman Pearson: you fix the false alarm probability, and then you maximise the detection probability. Maximise. If an option says minimise, it is false.", self.put(cards[0]))
        self.think('True or false: Bayesian detection maximises the Bayes risk.', 'Bayes detection MAXIMISES the Bayes risk. True or false?', 4)
        self.say('T', "Two. Bayesian detection minimises the Bayes risk, which is the expected cost. And with cost zero for being right and one for being wrong, that is the same as minimising the probability of error.", self.put(cards[1]))
        self.think('True or false: raising the prior of H one makes it harder to decide H one.', 'raising $P(H_1)$ makes $H_1$ HARDER. True or false?', 4)
        self.say('T', "Three. Raising the prior of H one lowers the threshold. It makes H one easier, not harder. That was the false statement in June 2026.", self.put(cards[2]))

    def recap(self):
        self.header('recap')
        r = card([r'1. $\dfrac{p(x\,|\,H_1)}{p(x\,|\,H_0)}>\lambda$     2. $\ln$     3. isolate $x$, FLIP if you divide by a negative',
                  r'4. rule: $x>\gamma$ or $x<\gamma$     5. $P_{FA}$ under the $H_0$ curve, $P_D$ under the $H_1$ curve, same zone',
                  r'priors and costs:  $\lambda=\dfrac{C_{10}P_0}{C_{01}P_1}$'], 25).move_to(UP * 0.6)
        self.say('S', "Can you give me the whole thing in thirty seconds?", self.wipe())
        self.think('Before I say it: try to say the five steps out loud, from memory.', 'say the five LRT steps out loud, from memory', 9)
        self.say('T', "Ratio of the two PDFs, H one over H zero, bigger than lambda. Take the log. Isolate x, and flip if you divide by a negative number. P F A is the H zero curve in the decide H one zone, P D is the H one curve in the same zone. With priors, lambda is P zero over P one.",
                 self.put(r, rt=1.0))
        nxt = MT('Now: lesson 4.1 on the site, do the June 2026 question yourself.', 28, PURPLE).next_to(r, DOWN, buff=0.5)
        self.say('T', "Now open lesson 4.1 on the site and do the June 2026 Rayleigh question on paper, by yourself. That is the real practice.", self.put(nxt))
        self.say('S', "Thanks, Ava. See you in the next episode.")
