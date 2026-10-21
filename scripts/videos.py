"""Manim animations for the guide (one idea each, 15-30 s, no audio: captions at the bottom).

Render one scene:  python scripts/render_videos.py EnergyPower
Render all:        python scripts/render_videos.py
Output: docs/video/<snake_name>.mp4 + .jpg poster (last frame).
"""
import math
import os
import sys

import numpy as np
from manim import (DOWN, LEFT, ORIGIN, RIGHT, UL, UP, UR, Arrow, Circle, Create, DashedLine, Dot, FadeIn, FadeOut,
                   Line, Rectangle, ReplacementTransform, Square, Transform, ValueTracker, VGroup, VMobject, Write,
                   always_redraw, linear, smooth)
from scipy import stats
from scipy.signal import lfilter

sys.path.insert(0, os.path.dirname(__file__))
from vidkit import (BLUE, GREEN, GREY, INK, LIGHT, ORANGE, PAPER, PURPLE, RED, Base, MT, P, Txt, area, curve,
                    mk_axes, stems, xlabel, ylabel)


# ------------------------------------------------------------------ Chapter 0
class SamplingAlias(Base):
    def construct(self):
        self.title('Sampling a tone: one value every $T_s=0.1$ s ($f_s=10$ Hz)')
        fs = 10
        ax = mk_axes([0, 1, 0.1], [-1.3, 1.3, 1], 12, 4).shift(UP * 0.2)
        lab = VGroup(xlabel(ax, 1, '$t$ (s)'), xlabel(ax, 0, '0'))
        f = ValueTracker(1.0)
        t = np.linspace(0, 1, 600)
        n = np.arange(11)

        def tone():
            return curve(ax, t, np.cos(2 * np.pi * f.get_value() * t), BLUE, 4)

        def samples():
            return stems(ax, n / fs, np.cos(2 * np.pi * f.get_value() * n / fs), RED, r=0.08, w=3)

        def alias():
            fv = f.get_value()
            if fv <= 5.02:
                return VMobject()
            return curve(ax, t, np.cos(2 * np.pi * (fs - fv) * t), ORANGE, 5, opacity=0.9)

        def info():
            fv = f.get_value()
            s = f'f = {fv:.1f} Hz    θ = 2π·f/fs = {2 * fv / fs:.2f}π'
            if fv > 5.02:
                s += f'    looks like {fs - fv:.1f} Hz'
            return Txt(s, 26, INK).next_to(ax, UP, buff=0.15)

        self.play(Create(ax), FadeIn(lab))
        self.add(always_redraw(tone), always_redraw(alias), always_redraw(samples), always_redraw(info))
        self.say('blue: the real tone, red dots: what the sampler keeps', 1.2)
        self.play(f.animate.set_value(4.5), run_time=4, rate_func=linear)
        self.play(f.animate.set_value(5), run_time=1.2)
        self.say('f = fs/2 = 5 Hz: samples +1, −1, +1, …  the fastest possible wiggle (θ = π)', 2.2)
        self.play(f.animate.set_value(9), run_time=5, rate_func=linear)
        self.say('above fs/2 the same dots fit a SLOWER tone (orange): 9 Hz is indistinguishable from 1 Hz', 3)


class Phasor(Base):
    def construct(self):
        self.title(r'$e^{j\theta}$ is an arrow going round; two mirrored arrows add up to $2\cos\theta$')
        R = 1.5
        c0 = LEFT * 4.3 + DOWN * 0.3
        circ = Circle(radius=R, color=GREY, stroke_width=2).move_to(c0)
        axes_l = VGroup(Line(c0 + LEFT * 3.3, c0 + RIGHT * 3.3, color=GREY, stroke_width=1.5),
                        Line(c0 + DOWN * 2.2, c0 + UP * 2.2, color=GREY, stroke_width=1.5))
        re_l = MT('real', 20, GREY).next_to(c0 + RIGHT * 3.3, DOWN, buff=0.1)
        ax = mk_axes([0, 4 * np.pi, np.pi], [-2.2, 2.2, 1], 6.4, 4.2).move_to(RIGHT * 3.4 + DOWN * 0.3)
        xl = VGroup(*[xlabel(ax, k * np.pi, s, 20) for k, s in [(1, r'$\pi$'), (2, r'$2\pi$'), (3, r'$3\pi$'),
                                                                 (4, r'$4\pi$')]])
        ax_t = MT(r'$\theta$', 22).next_to(ax.c2p(4 * np.pi, -2.2), RIGHT, buff=0.1)
        th = ValueTracker(0.0)
        mirror = ValueTracker(0.0)

        def tip(sign=1):
            a = th.get_value()
            return c0 + R * np.array([math.cos(a), sign * math.sin(a), 0])

        def arrows():
            g = VGroup(Arrow(c0, tip(), buff=0, color=BLUE, stroke_width=6, max_tip_length_to_length_ratio=0.15))
            a = th.get_value()
            g.add(Line(c0, c0 + RIGHT * R * math.cos(a), color=GREEN, stroke_width=9))
            g.add(DashedLine(tip(), c0 + RIGHT * R * math.cos(a), color=GREY, stroke_width=2))
            m = mirror.get_value()
            if m > 0:
                g.add(Arrow(c0, tip(-1), buff=0, color=GREY, stroke_width=5, max_tip_length_to_length_ratio=0.15)
                      .set_opacity(m))
                s = c0 + RIGHT * 2 * R * math.cos(a)
                if abs(math.cos(a)) > 0.03:
                    g.add(Arrow(c0, s, buff=0, color=RED, stroke_width=7, max_tip_length_to_length_ratio=0.12)
                          .set_opacity(m))
                g.add(DashedLine(tip(), s, color=RED, stroke_width=1.5).set_opacity(0.6 * m))
                g.add(DashedLine(tip(-1), s, color=RED, stroke_width=1.5).set_opacity(0.6 * m))
            return g

        def traces():
            a = th.get_value()
            xs = np.linspace(0, max(a, 1e-3), 300)
            g = VGroup()
            if mirror.get_value() < 1:
                g.add(curve(ax, xs, np.cos(xs), GREEN, 4))
                g.add(Dot(ax.c2p(a, math.cos(a)), radius=0.07, color=GREEN))
            else:
                g.add(curve(ax, xs, 2 * np.cos(xs), RED, 4))
                g.add(Dot(ax.c2p(a, 2 * math.cos(a)), radius=0.07, color=RED))
            return g

        def readout():
            a = th.get_value()
            if mirror.get_value() < 1:
                s = f'cos θ = {math.cos(a):+.2f}'
                col = GREEN
            else:
                s = f'2 cos θ = {2 * math.cos(a):+.2f}'
                col = RED
            return Txt(s, 26, col).next_to(ax, UP, buff=0.1)

        self.play(Create(circ), FadeIn(axes_l), FadeIn(re_l), Create(ax), FadeIn(xl), FadeIn(ax_t))
        self.add(always_redraw(arrows), always_redraw(traces), always_redraw(readout))
        self.say(r'blue arrow $e^{j\theta}$: length 1, angle $\theta$. Its shadow on the real axis (green) is $\cos\theta$',
                 0.6)
        self.play(th.animate.set_value(4 * np.pi), run_time=8, rate_func=linear)
        self.say(r'add the mirror image $e^{-j\theta}$ (grey): the up/down parts cancel', 0.4)
        self.play(th.animate.set_value(0), run_time=0.8)
        self.play(mirror.animate.set_value(1), run_time=0.8)
        self.say(r'the sum (red) always lies on the real axis: $e^{j\theta}+e^{-j\theta}=2\cos\theta$', 0.4)
        self.play(th.animate.set_value(4 * np.pi), run_time=8, rate_func=linear)
        self.wait(1.5)


# ------------------------------------------------------------------ Part 3.1
class EnergyPower(Base):
    def construct(self):
        self.title('Energy vs power: let the window $[-T/2,\\ T/2]$ grow')
        axE = mk_axes([-10, 10, 5], [0, 1.15, 0.5], 6.6, 1.9).move_to(LEFT * 3.25 + UP * 1.55)
        axP = mk_axes([-10, 10, 5], [0, 1.15, 0.5], 6.6, 1.9).move_to(LEFT * 3.25 + DOWN * 1.15)
        aE = mk_axes([0, 20, 5], [0, 10.5, 5], 4.6, 1.9).move_to(RIGHT * 4.1 + UP * 1.55)
        aP = mk_axes([0, 20, 5], [0, 1.1, 0.5], 4.6, 1.9).move_to(RIGHT * 4.1 + DOWN * 1.15)
        labels = VGroup(
            MT(r'energy signal: $x^2=e^{-2t}u(t)$', 22, BLUE).next_to(axE, UP, buff=0.08),
            MT(r'power signal: $x^2=\sin^2(\pi t)$, $A=1$', 22, RED).next_to(axP, UP, buff=0.08),
            MT(r'$E(T)$ = area inside the window', 22).next_to(aE, UP, buff=0.08),
            MT(r'$P(T)=E(T)/T$', 22).next_to(aP, UP, buff=0.08),
            xlabel(aP, 20, '$T$', 20), xlabel(aE, 20, '$T$', 20), xlabel(axP, 10, '$t$', 20),
            ylabel(aE, 10, '10', 18), ylabel(aE, 0.5, r'$\frac{1}{2}$', 18, BLUE), ylabel(aP, 0.5, r'$\frac{1}{2}$', 18),
            ylabel(aP, 1, '1', 18))
        T = ValueTracker(0.2)
        t = np.linspace(-10, 10, 1200)
        xe = np.where(t >= 0, np.exp(-2 * t), 0)
        xp = np.sin(np.pi * t) ** 2

        def EeT(T_):
            return (1 - np.exp(-T_)) / 2

        def EpT(T_):
            return T_ / 2 - np.sin(np.pi * T_) / (2 * np.pi)

        def window():
            h = T.get_value() / 2
            g = VGroup()
            for ax in (axE, axP):
                lo, hi = P(ax, [-h, h], [0, 1.15])
                g.add(Rectangle(width=hi[0] - lo[0] + 1e-4, height=hi[1] - lo[1], stroke_width=0, fill_color=PAPER,
                                fill_opacity=1).move_to((lo + hi) / 2).set_z_index(-1))
                g.add(DashedLine(ax.c2p(-h, 0), ax.c2p(-h, 1.15), color=INK, stroke_width=2))
                g.add(DashedLine(ax.c2p(h, 0), ax.c2p(h, 1.15), color=INK, stroke_width=2))
            return g

        def fills():
            h = T.get_value() / 2
            m = np.abs(t) <= h
            return VGroup(area(axE, t[m], xe[m], BLUE, 0.4), area(axP, t[m], xp[m], RED, 0.35))

        def traces():
            Tv = T.get_value()
            Ts = np.linspace(0.2, max(Tv, 0.21), 400)
            g = VGroup(curve(aE, Ts, EeT(Ts), BLUE, 4), curve(aE, Ts, EpT(Ts), RED, 4),
                       curve(aP, Ts, EeT(Ts) / Ts, BLUE, 4), curve(aP, Ts, EpT(Ts) / Ts, RED, 4))
            for ax, v, c in [(aE, EeT(Tv), BLUE), (aE, EpT(Tv), RED), (aP, EeT(Tv) / Tv, BLUE),
                             (aP, EpT(Tv) / Tv, RED)]:
                g.add(Dot(ax.c2p(Tv, v), radius=0.06, color=c))
            return g

        def readout():
            Tv = T.get_value()
            return VGroup(
                Txt(f'energy signal:  T = {Tv:4.1f}   E = {EeT(Tv):.2f}   P = {EeT(Tv) / Tv:.3f}', 20, BLUE),
                Txt(f'power signal:   T = {Tv:4.1f}   E = {EpT(Tv):.2f}   P = {EpT(Tv) / Tv:.3f}', 20, RED),
            ).arrange(RIGHT, buff=0.6).move_to(DOWN * 2.75)

        curves = VGroup(curve(axE, t, xe, BLUE, 3), curve(axP, t, xp, RED, 3))
        self.play(*[Create(a) for a in (axE, axP, aE, aP)], FadeIn(labels))
        self.add(always_redraw(window), always_redraw(fills))
        self.play(Create(curves))
        self.add(always_redraw(traces), always_redraw(readout))
        self.say('energy = the area of $x^2$ inside the window. Now let the window grow…', 0.3)
        self.play(T.animate.set_value(6), run_time=6, rate_func=linear)
        self.say('blue area stops growing at $\\frac{1}{2}$ (finite energy); red area grows forever ($E=\\infty$)', 0.3)
        self.play(T.animate.set_value(20), run_time=7, rate_func=linear)
        self.say('average power $P=E/T$: blue $\\to 0$ (finite ÷ huge), red $\\to A^2/2=\\frac{1}{2}$', 3.5)


class Windowing(Base):
    def construct(self):
        self.title('Recording $N$ samples = multiplying by a window; the spectrum gets smeared')
        top = mk_axes([-20, 100, 10], [-1.3, 1.3, 1], 12.4, 1.8).move_to(UP * 1.8)
        bot = mk_axes([0, np.pi, 1], [-80, 5, 20], 12.4, 2.9).move_to(DOWN * 1.15)
        th0, th1, weak = 1.0, 2.3, 0.01
        n = np.arange(-20, 101)
        x = np.cos(th0 * n) + weak * np.cos(th1 * n)
        N = ValueTracker(12.0)
        hann = ValueTracker(0.0)
        nfft = 4096
        thg = 2 * np.pi * np.arange(nfft // 2 + 1) / nfft

        def win():
            Nv = int(round(N.get_value()))
            k = np.arange(Nv)
            w = (1 - hann.get_value()) * np.ones(Nv) + hann.get_value() * (np.hanning(Nv + 2)[1:-1])
            return Nv, w

        def time_part():
            Nv, w = win()
            full = np.zeros_like(n, dtype=float)
            full[(n >= 0) & (n < Nv)] = w
            g = VGroup(stems(top, n, x, LIGHT, r=0.025, w=2))
            g.add(stems(top, n[(n >= 0) & (n < Nv)], (x * full)[(n >= 0) & (n < Nv)], BLUE, r=0.03, w=2.5))
            g.add(curve(top, n, full, RED, 3))
            return g

        def spec():
            Nv, w = win()
            k = np.arange(Nv)
            X = np.abs(np.fft.rfft(w * (np.cos(th0 * k) + weak * np.cos(th1 * k)), nfft))
            X = 20 * np.log10(X / X.max() + 1e-9)
            return curve(bot, thg, np.clip(X, -80, 5), BLUE, 3)

        def info():
            Nv, _ = win()
            kind = 'rectangular' if hann.get_value() < 0.5 else 'Hann'
            return Txt(f'N = {Nv}   window: {kind}', 22, RED).next_to(top, UP, buff=0.05).align_to(top, RIGHT)

        marks = VGroup(
            DashedLine(bot.c2p(th0, -80), bot.c2p(th0, 5), color=GREY, stroke_width=2),
            DashedLine(bot.c2p(th1, -80), bot.c2p(th1, 5), color=GREEN, stroke_width=2),
            MT('strong tone', 18, GREY).next_to(bot.c2p(th0, 5), UP, buff=0.05),
            MT('weak tone (−40 dB)', 18, GREEN).next_to(bot.c2p(th1, 5), UP, buff=0.05),
            DashedLine(bot.c2p(0, -13.3), bot.c2p(np.pi, -13.3), color=ORANGE, stroke_width=2),
            MT('−13 dB', 18, ORANGE).next_to(bot.c2p(2.75, -13.3), UP, buff=0.05),
            ylabel(bot, 0, '0 dB', 18), ylabel(bot, -40, '−40', 18), ylabel(bot, -80, '−80', 18),
            xlabel(bot, np.pi, r'$\theta=\pi$', 18), xlabel(bot, 0, '0', 18),
            MT('grey: true signal · red: window · blue: recorded', 18).next_to(top, UP, buff=0.05)
            .align_to(top, LEFT))
        self.play(Create(top), Create(bot), FadeIn(marks))
        self.add(always_redraw(time_part), always_redraw(spec), always_redraw(info))
        self.say('each tone becomes a copy of the window spectrum: main lobe + side lobes', 1.0)
        self.play(N.animate.set_value(60), run_time=6, rate_func=linear)
        self.say('longer $N$: narrower main lobe (better resolution) … but side lobes stay at −13 dB', 1.0)
        self.say('the weak tone at 2.3 is still buried under the side lobes (leakage)', 1.2)
        self.play(hann.animate.set_value(1), run_time=3)
        self.say('Hann window: side lobes far lower → the weak tone appears. Price: a wider main lobe', 3.2)


class ZeroPad(Base):
    def construct(self):
        self.title('Zero padding: more points on the SAME curve, not a sharper curve')
        top = mk_axes([0, 64, 8], [-1.2, 1.2, 1], 12.4, 1.4).move_to(UP * 2.0)
        ax = mk_axes([0, np.pi, 1], [0, 1.12, 0.5], 12.4, 3.2).move_to(DOWN * 0.95)
        N = 16
        n = np.arange(N)
        th0 = 2 * np.pi * 3.4 / N
        x = np.cos(th0 * n)
        th = np.linspace(0, np.pi, 1500)
        F = np.abs(np.exp(-1j * np.outer(th, n)) @ x)
        m = F.max()
        grey = curve(ax, th, F / m, GREY, 3)
        labs = VGroup(xlabel(ax, np.pi, r'$\theta=\pi$', 18), xlabel(ax, 0, '0', 18),
                      MT('16 real samples (blue) + zeros (grey)', 18).next_to(top, UP, buff=0.05)
                      .align_to(top, LEFT))

        def dots(L):
            k = np.arange(L // 2 + 1)
            v = np.abs(np.fft.fft(x, L))[:L // 2 + 1] / m
            return VGroup(*[Dot(p, radius=0.07 if L <= 32 else 0.045, color=RED) for p in P(ax, 2 * np.pi * k / L, v)])

        def samples(L):
            g = stems(top, n, x, BLUE, r=0.05, w=3)
            z = np.arange(N, min(L, 64))
            g.add(VGroup(*[Dot(p, radius=0.035, color=GREY) for p in P(top, z, np.zeros(len(z)))]))
            if L > 64:
                g.add(MT(f'… and more zeros, up to $n={L - 1}$', 18, GREY).next_to(top, UP, buff=0.05)
                      .align_to(top, RIGHT))
            return g

        self.play(Create(top), Create(ax), FadeIn(labs))
        self.play(Create(grey))
        self.say('grey: the FTD of the 16 samples (the curve the DFT samples)', 0.5)
        d = dots(16)
        s = samples(16)
        info = Txt('L = 16 point DFT', 24, RED).next_to(ax, UP, buff=0.05).align_to(ax, RIGHT)
        self.play(FadeIn(d), FadeIn(s), FadeIn(info))
        self.wait(1)
        for L in (32, 64, 256):
            self.play(ReplacementTransform(d, d := dots(L)), ReplacementTransform(s, s := samples(L)),
                      Transform(info, Txt(f'L = {L} point DFT', 24, RED).move_to(info)), run_time=1.3)
            self.wait(1.2)
        self.say('the red dots only trace the grey curve more densely: the peak is NOT narrower', 1.5)
        n64 = np.arange(64)
        F64 = np.abs(np.exp(-1j * np.outer(th, n64)) @ np.cos(th0 * n64))
        g64 = curve(ax, th, F64 / F64.max(), GREEN, 4)
        self.play(Create(g64), run_time=1.5)
        self.say('green: 64 REAL samples. Only more real data makes the peak narrower (resolution)', 3)


# ------------------------------------------------------------------ Part 3.2
class PeriodogramAverage(Base):
    def construct(self):
        self.title('The periodogram is noisy, and more data does not calm it. Averaging does.')
        rng = np.random.default_rng(11)
        ax = mk_axes([0, np.pi, 1], [0, 7, 1], 12.4, 4.4).shift(DOWN * 0.35)
        lab = VGroup(xlabel(ax, np.pi, r'$\theta=\pi$', 18), xlabel(ax, 0, '0', 18), ylabel(ax, 1, '1', 18),
                     ylabel(ax, 6, '6', 18))
        true = DashedLine(ax.c2p(0, 1), ax.c2p(np.pi, 1), color=RED, stroke_width=4)
        tl = MT('true PSD = 1 (white noise)', 20, RED).next_to(ax.c2p(np.pi, 1), UP, buff=0.08).shift(LEFT * 1.9)

        def pg(N):
            x = rng.standard_normal(N)
            p = np.abs(np.fft.rfft(x)) ** 2 / N
            return curve(ax, 2 * np.pi * np.arange(len(p)) / N, np.minimum(p, 7), BLUE, 2.2 if N < 500 else 1.4)

        self.play(Create(ax), FadeIn(lab), Create(true), FadeIn(tl))
        c = pg(64)
        info = Txt('N = 64', 26, BLUE).next_to(ax, UP, buff=0.05).align_to(ax, RIGHT)
        self.play(Create(c), FadeIn(info))
        self.say('periodogram of 64 samples: it jumps from 0 to 5 around the true value 1', 0.8)
        for N in (256, 1024, 4096):
            self.play(ReplacementTransform(c, c := pg(N)), Transform(info, Txt(f'N = {N}', 26, BLUE).move_to(info)),
                      run_time=1)
            self.wait(1)
        self.say('more samples only give MORE bins, each one just as noisy (variance ≈ $P^2$)', 1.5)
        x = rng.standard_normal(4096)
        for K in (4, 16, 64):
            M = 4096 // K
            p = np.mean([np.abs(np.fft.rfft(x[k * M:(k + 1) * M])) ** 2 / M for k in range(K)], axis=0)
            nc = curve(ax, 2 * np.pi * np.arange(len(p)) / M, np.minimum(p, 7), GREEN, 3)
            self.play(ReplacementTransform(c, nc),
                      Transform(info, Txt(f'Bartlett: average of K = {K} pieces', 26, GREEN).move_to(info, aligned_edge=RIGHT)),
                      run_time=1.2)
            c = nc
            self.wait(1)
        self.say('cut the record into K pieces and average their periodograms: variance ≈ $P^2/K$', 1.2)
        self.say('price: each piece has only $M=N/K$ samples, so resolution is only $2\\pi/M$: peaks get blurred',
                 2.5)


class SlideBase(Base):
    seq = [1, 2, 3]
    norm = '3'
    title_s = ''
    lags = [0, 1, 2]
    names = 'x'

    def construct(self):
        self.title(self.title_s)
        s = self.seq
        L = len(s)
        box = 0.95
        x0 = LEFT * 4.9 + UP * 1.6
        ax = mk_axes([-max(self.lags) - 0.6, max(self.lags) + 0.6, 1], [-0.6, 1.6, 0.5], 4.6, 3.4).move_to(
            RIGHT * 4.3 + DOWN * 0.1)
        axl = VGroup(*[xlabel(ax, l, f'{l}', 18) for l in range(-max(self.lags), max(self.lags) + 1)],
                     MT(r'lag $l$', 20).next_to(ax, DOWN, buff=0.45),
                     MT(self.result_name, 22).next_to(ax, UP, buff=0.1))
        self.play(Create(ax), FadeIn(axl))
        scale = 1 / max(abs(v) for v in self.values())

        def row(vals, y_shift, color, offset=0):
            g = VGroup()
            for k, v in enumerate(vals):
                sq = Square(box, color=color, stroke_width=3, fill_color=color, fill_opacity=0.08)
                sq.move_to(x0 + RIGHT * (k + offset) * box + DOWN * y_shift)
                g.add(VGroup(sq, Txt(f'{v:g}', 26, color).move_to(sq)))
            return g

        top = row(s, 0, BLUE)
        tl = MT(self.top_name, 22, BLUE).next_to(top, LEFT, buff=0.2)
        self.play(FadeIn(top), FadeIn(tl))
        bottom = row(s, 1.15, ORANGE)
        bl = MT(self.bottom_name(0), 22, ORANGE).next_to(bottom, LEFT, buff=0.2)
        self.play(FadeIn(bottom), FadeIn(bl))
        dots = VGroup()
        prev = VGroup()
        for l in self.lags:
            target = row(s, 1.15, ORANGE, offset=l)
            self.play(Transform(bottom, target), Transform(bl, MT(self.bottom_name(l), 22, ORANGE)
                                                         .next_to(target, LEFT, buff=0.2).set_x(bl.get_x())),
                      FadeOut(prev), run_time=0.9)
            prods = VGroup()
            terms = []
            for k in range(l, L):
                v = s[k] * s[k - l]
                terms.append(v)
                prods.add(Txt(f'{v:g}', 24, PURPLE).move_to(x0 + RIGHT * k * box + DOWN * 2.3))
            total = sum(terms)
            res = self.result(total)
            if terms:
                expr = ' + '.join(f'{v:g}' for v in terms)
                line = MT(f'$l={l}$:  {expr} $= {total:g}$   →   {self.formula(total)}', 24)
            else:
                line = MT(f'$l={l}$: the boxes no longer overlap → 0', 24)
            line.move_to(LEFT * 3.2 + DOWN * 3.05)
            mul = MT('×  (multiply the boxes that overlap)', 18, PURPLE).next_to(prods, DOWN, buff=0.1) if terms else VGroup()
            self.play(FadeIn(prods), FadeIn(mul), FadeIn(line), run_time=0.8)
            st = stems(ax, [l, -l] if l else [0], [res * scale] * (2 if l else 1), GREEN, r=0.07, w=4)
            vl = MT(f'{res:.3g}', 18, GREEN).next_to(ax.c2p(l, res * scale), UP if res >= 0 else DOWN, buff=0.08)
            self.play(FadeIn(st), FadeIn(vl), run_time=0.6)
            dots.add(st, vl)
            self.wait(1.4)
            prev = VGroup(prods, line, mul)
        self.play(FadeOut(prev), run_time=0.4)
        self.say(self.final, 3)


class SlideCorr(SlideBase):
    seq = [1, 2, 3]
    lags = [0, 1, 2]
    title_s = r'Estimating $\hat r[l]$ from $x=[1,2,3]$: slide, multiply, add, divide by $N=3$'
    top_name = '$x[n]$'
    result_name = r'$\hat r[l]$ (symmetric: $\hat r[-l]=\hat r[l]$)'
    final = r'the stems are the autocorrelation estimate; long lags use few products (only 1 at $l=2$)'

    def bottom_name(self, l):
        return f'$x[n-{l}]$' if l else '$x[n]$'

    def values(self):
        return [14 / 3, 8 / 3, 1]

    def result(self, total):
        return total / 3

    def formula(self, total):
        return f'$\\hat r = {total:g}/3 = {total / 3:.3g}$'


class SlideMA(SlideBase):
    seq = [1, 0.5, -0.4]
    lags = [0, 1, 2, 3]
    title_s = r'MA(2) autocorrelation: slide the coefficients $b=[1,\ 0.5,\ -0.4]$ over themselves'
    top_name = '$b_m$'
    result_name = r'$r[l]$ with $\sigma_i^2=1$'
    final = r'MA($q$) memory is exactly $q$ steps: $r[l]=0$ for $|l|>q$ (here $q=2$)'

    def bottom_name(self, l):
        return f'$b_{{m-{l}}}$' if l else '$b_m$'

    def values(self):
        return [1.41, 0.3, -0.4]

    def result(self, total):
        return total

    def formula(self, total):
        return f'$r[l]=\\sigma_i^2\\times{total:.3g}$'


# ------------------------------------------------------------------ Part 3.3
class ARRecursion(Base):
    def construct(self):
        self.title(r'AR(1): $x[n]=0.8\,x[n-1]+i[n]$, keep 80 % of the last value, add a fresh kick')
        rng = np.random.default_rng(5)
        i = rng.normal(0, 1, 40)
        x = lfilter([1], [1, -0.8], i)
        ax = mk_axes([-0.5, 40, 5], [-4, 4, 2], 12.4, 2.8).move_to(UP * 1.1)
        ai = mk_axes([-0.5, 40, 5], [-3, 3, 1], 12.4, 1.6).move_to(DOWN * 1.75)
        labs = VGroup(MT('signal $x[n]$', 22, BLUE).next_to(ax, UP, buff=0.05).align_to(ax, LEFT),
                      MT('noise kicks $i[n]$', 22, GREY).next_to(ai, UP, buff=0.05).align_to(ai, LEFT))
        self.play(Create(ax), Create(ai), FadeIn(labs))
        shown = VGroup()
        for k in range(5):
            kick = stems(ai, [k], [i[k]], GREY, r=0.06, w=5)
            self.play(FadeIn(kick), run_time=0.35)
            parts = VGroup()
            if k:
                carry = 0.8 * x[k - 1]
                ghost = Line(ax.c2p(k, 0), ax.c2p(k, carry), color=BLUE, stroke_width=10, stroke_opacity=0.3)
                arr = Arrow(ax.c2p(k - 1, x[k - 1]), ax.c2p(k, carry), buff=0.05, color=BLUE, stroke_width=3,
                            max_tip_length_to_length_ratio=0.2)
                parts.add(ghost, arr, MT('×0.8', 18, BLUE).next_to(arr, UP, buff=0.02))
            else:
                carry = 0
            top = Line(ax.c2p(k, carry), ax.c2p(k, x[k]), color=GREY, stroke_width=10, stroke_opacity=0.6)
            parts.add(top)
            self.play(FadeIn(parts), run_time=0.6)
            st = stems(ax, [k], [x[k]], BLUE, r=0.07, w=4)
            self.play(FadeIn(st), FadeOut(parts), run_time=0.5)
            shown.add(kick, st)
            if k == 0:
                self.say('blue = 0.8 × previous value (faded bar) + today\'s kick (grey bar)', 0.3)
        self.say('repeat forever: the signal remembers its past, so it changes smoothly', 0.2)
        for k in range(5, 40):
            g = VGroup(stems(ai, [k], [i[k]], GREY, r=0.05, w=4), stems(ax, [k], [x[k]], BLUE, r=0.06, w=4))
            self.play(FadeIn(g), run_time=0.11)
            shown.add(g)
        self.wait(1)
        self.play(FadeOut(shown))
        self.say('one single kick $i[0]=1$ and nothing after: it fades as $0.8^n$ but never fully dies', 0.2)
        n = np.arange(40)
        imp = VGroup(stems(ai, [0], [1], GREY, r=0.06, w=5))
        self.play(FadeIn(imp), run_time=0.4)
        resp = VGroup(*[stems(ax, [k], [3 * 0.8 ** k], BLUE, r=0.06, w=4) for k in n])
        self.play(LaggedStart_(resp), run_time=3)
        self.say(r'that fading memory is the autocorrelation: $r[l]\propto0.8^{|l|}$ (an AR model never forgets fully)',
                 3)


def LaggedStart_(group):
    from manim import LaggedStart
    return LaggedStart(*[FadeIn(m) for m in group], lag_ratio=0.15)


# ------------------------------------------------------------------ Part 1
class BayesZoom(Base):
    def construct(self):
        self.title('Bayes = zoom into the part of the world you know happened')
        W, H = 8.0, 4.4
        o = LEFT * 6.4 + DOWN * 2.3
        widths, defects = [.40, .35, .25], [.02, .04, .05]
        names, cols = ['M1', 'M2', 'M3'], [BLUE, GREEN, PURPLE]
        strips, reds, texts = VGroup(), VGroup(), VGroup()
        x = 0
        for w, d, nm, c in zip(widths, defects, names, cols):
            r = Rectangle(width=w * W, height=H, stroke_color=INK, stroke_width=2, fill_color=c, fill_opacity=0.15)
            r.move_to(o + RIGHT * (x + w / 2) * W + UP * H / 2)
            rr = Rectangle(width=w * W, height=d * 10 * H, stroke_width=0, fill_color=RED, fill_opacity=0.85)
            rr.move_to(o + RIGHT * (x + w / 2) * W + UP * d * 10 * H / 2)
            strips.add(r)
            reds.add(rr)
            texts.add(Txt(f'{nm}\n{w * 10000:.0f} chips', 22, c).move_to(r.get_top() + DOWN * 0.5))
            texts.add(Txt(f'{d:.0%} bad = {w * d * 10000:.0f}', 20, RED).next_to(rr, UP, buff=0.08))
            x += w
        self.play(FadeIn(strips), FadeIn(texts[0::2]))
        self.say('10 000 chips. Width = share of each machine (40 %, 35 %, 25 %)', 1.0)
        self.play(FadeIn(reds), FadeIn(texts[1::2]))
        self.say('red = defective chips (heights ×10 so you can see them)', 1.0)
        self.say('we are told: "the chip is defective". Throw away everything that is not red', 0.3)
        self.play(FadeOut(strips), FadeOut(texts), run_time=1)
        bar_o = RIGHT * 0.2 + UP * 0.2
        BW = 10.5
        targets = VGroup()
        acc = 0
        for cnt, c in zip([80, 140, 125], cols):
            tr = Rectangle(width=cnt / 345 * BW, height=2.2, stroke_color=WHITE_, stroke_width=3, fill_color=c,
                           fill_opacity=0.8)
            tr.move_to(bar_o + RIGHT * (acc + cnt / 2) / 345 * BW)
            targets.add(tr)
            acc += cnt
        targets.move_to(ORIGIN + UP * 0.4)
        self.play(*[ReplacementTransform(a, b) for a, b in zip(reds, targets)], run_time=1.6)
        fr = VGroup()
        for tr, cnt, nm in zip(targets, [80, 140, 125], names):
            fr.add(Txt(f'{nm}\n{cnt}/345\n= {cnt / 345:.3f}', 26, WHITE_).move_to(tr))
        tot = MT('345 defective chips in total: $P(\\mathrm{defective})=0.0345$', 22).next_to(targets, UP, buff=0.3)
        self.play(FadeIn(fr), FadeIn(tot))
        self.say(r'$P(M_2\mid\mathrm{defective})=\frac{140}{345}=0.406$: the share of $M_2$ inside the red part', 3.5)


WHITE_ = '#ffffff'


class Ensemble(Base):
    def construct(self):
        self.title('A random process is a stack of signals: average DOWN a column or ALONG a row')
        rows = 5
        axs = VGroup(*[mk_axes([0, 4 * np.pi, np.pi], [-1.9, 1.9, 1], 7.6, 0.95) for _ in range(rows)])
        axs.arrange(DOWN, buff=0.18).move_to(LEFT * 0.85 + DOWN * 0.15)
        t = np.linspace(0, 4 * np.pi, 500)
        U = np.arange(rows) * 2 * np.pi / rows + 0.4
        sig = [np.cos(t + u) for u in U]
        lines = VGroup(*[curve(a, t, s, BLUE, 3) for a, s in zip(axs, sig)])
        names = VGroup(*[MT(f'realisation {k + 1}', 16, GREY).next_to(a, LEFT, buff=0.1) for k, a in enumerate(axs)])
        self.play(*[Create(a) for a in axs], FadeIn(names))
        self.play(Create(lines), run_time=1.5)
        self.say(r'$x(t)=\cos(t+U)$, with a random phase $U$ drawn once per realisation', 1.0)
        t0 = ValueTracker(1.0)

        def column():
            tv = t0.get_value()
            g = VGroup(Line(axs[0].c2p(tv, 1.9), axs[-1].c2p(tv, -1.9), color=RED, stroke_width=3))
            vals = [math.cos(tv + u) for u in U]
            for a, v in zip(axs, vals):
                g.add(Dot(a.c2p(tv, v), radius=0.07, color=RED))
            g.add(Txt(f'column at t = {tv:4.1f}\nmean of the dots = {np.mean(vals):+.2f}', 22, RED)
                  .next_to(axs, RIGHT, buff=0.3).shift(UP * 1.0))
            return g

        col = always_redraw(column)
        self.add(col)
        self.say('ensemble average: freeze a time, average over all realisations', 0.2)
        self.play(t0.animate.set_value(11.5), run_time=5, rate_func=linear)
        self.remove(col)
        self.say('the column mean is 0 at every time → the mean does not depend on $t$ (stationary)', 0.6)
        t1 = ValueTracker(0.3)

        def rowavg():
            tv = t1.get_value()
            m = t <= tv
            g = VGroup(area(axs[0], t[m], sig[0][m], ORANGE, 0.3))
            g.add(Txt(f'time average of row 1\nover [0, {tv:4.1f}] = {np.mean(sig[0][m]):+.2f}', 22, ORANGE)
                  .next_to(axs, RIGHT, buff=0.3).shift(DOWN * 0.6))
            return g

        ra = always_redraw(rowavg)
        self.add(ra)
        self.say('time average: follow ONE realisation and average along time', 0.2)
        self.play(t1.animate.set_value(4 * np.pi), run_time=5, rate_func=linear)
        self.say('it also goes to 0 = the ensemble mean → ergodic (in the mean)', 1.2)
        self.remove(ra)
        A = np.array([-1.0, 0.6, 1.4, -0.4, 0.8])
        sig2 = [a + 0.2 * np.sin(3 * t + k) + 0.12 * np.sin(7.3 * t + 2 * k) for k, a in enumerate(A)]
        new = VGroup(*[curve(a, t, s, PURPLE, 3) for a, s in zip(axs, sig2)])
        self.play(ReplacementTransform(lines, new), run_time=1.2)
        lv = VGroup(*[MT(f'$A={a:+.1f}$', 18, PURPLE).next_to(ax_, RIGHT, buff=0.1) for a, ax_ in zip(A, axs)])
        self.play(FadeIn(lv))
        self.say('now $x(t)=A+$ wiggle, with $A$ drawn ONCE per realisation and then frozen', 1.4)
        self.say(f'row 1 averages to its own $A=-1$, but the ensemble mean is {A.mean():.2f} → NOT ergodic', 3.2)


# ------------------------------------------------------------------ Part 2
class LikelihoodSweep(Base):
    def construct(self):
        self.title(r'Likelihood: slide the model, multiply the heights at the data')
        data = np.array([3.1, 4.2, 4.9])
        top = mk_axes([0, 8, 1], [0, 0.45, 0.1], 12, 2.6).move_to(UP * 1.45)
        bot = mk_axes([0, 8, 1], [0, 0.031, 0.01], 12, 2.2).move_to(DOWN * 1.75)
        labs = VGroup(MT(r'model $\mathcal{N}(\mu,1)$', 20, BLUE).next_to(top, UP, buff=0.05)
                      .align_to(top, LEFT),
                      MT(r'$L(\mu)$ = product of the 3 red heights', 20).next_to(bot, UP, buff=0.08)
                      .align_to(bot, LEFT),
                      xlabel(bot, 8, r'$\mu$', 20), xlabel(top, 8, '$x$', 20))
        for k in range(0, 8, 2):
            labs.add(xlabel(bot, k, str(k), 16))
        mu = ValueTracker(0.8)
        xs = np.linspace(0, 8, 500)

        def L(m):
            return np.prod(stats.norm.pdf(data[:, None], np.atleast_1d(m)[None, :], 1), axis=0)

        def model():
            m = mu.get_value()
            g = VGroup(curve(top, xs, stats.norm.pdf(xs, m, 1), BLUE, 4))
            for d in data:
                g.add(Line(top.c2p(d, 0), top.c2p(d, stats.norm.pdf(d, m, 1)), color=RED, stroke_width=7))
            g.add(DashedLine(top.c2p(m, 0), top.c2p(m, 0.42), color=BLUE, stroke_width=2))
            return g

        seen = [0.8]

        def trace():
            m = mu.get_value()
            seen[0] = max(seen[0], m)
            ms = np.linspace(0.8, max(seen[0], 0.81), 300)
            g = VGroup(curve(bot, ms, L(ms), INK, 4), Dot(bot.c2p(m, L(m)[0]), radius=0.08, color=RED))
            h = stats.norm.pdf(data, m, 1)
            g.add(Txt(f'μ = {m:.2f}:  {h[0]:.3f} × {h[1]:.3f} × {h[2]:.3f} = {np.prod(h):.4f}', 20, RED)
                  .next_to(top, UP, buff=0.08).align_to(top, RIGHT))
            return g

        dots = VGroup(*[Dot(top.c2p(d, 0), radius=0.09, color=INK) for d in data])
        self.play(Create(top), Create(bot), FadeIn(labs), FadeIn(dots))
        self.add(always_redraw(model), always_redraw(trace))
        self.say(r'black dots: the data. For each candidate $\mu$ read the bell height at every data point', 0.3)
        self.play(mu.animate.set_value(7.2), run_time=8, rate_func=linear)
        self.say(r'the product is largest when the bell sits on the data: $\hat\mu=\bar x=4.07$', 0.3)
        self.play(mu.animate.set_value(data.mean()), run_time=2.5)
        self.wait(2.5)


class BayesUpdate(Base):
    def construct(self):
        self.title(r'Bayesian update: prior × likelihood → posterior, one coin flip at a time')
        ax = mk_axes([0, 1, 0.1], [0, 7.2, 1], 11.6, 3.9).shift(DOWN * 0.35)
        labs = VGroup(*[xlabel(ax, v, f'{v:g}', 18) for v in (0, 0.2, 0.4, 0.6, 0.8, 1)],
                      MT(r'$\theta$ = probability of heads', 18).next_to(ax.c2p(0.5, 0), DOWN, buff=0.42))
        th = np.linspace(0.001, 0.999, 400)
        prior = curve(ax, th, stats.beta.pdf(th, 2, 3), GREY, 3)
        pl = MT('prior Beta(2, 3): "probably a bit tails-heavy"', 20, GREY).next_to(ax.c2p(0.02, 2.0), UR, buff=0.05)
        truth = DashedLine(ax.c2p(0.7, 0), ax.c2p(0.7, 7.2), color=GREEN, stroke_width=2)
        tl = MT('true coin: 0.7', 18, GREEN).next_to(ax.c2p(0.7, 5.6), RIGHT, buff=0.08)
        self.play(Create(ax), FadeIn(labs), Create(prior), FadeIn(pl))
        rng = np.random.default_rng(2)
        flips = (rng.random(60) < 0.7).astype(int)
        h = t_ = 0
        post = prior.copy().set_color(BLUE)
        self.add(post)
        info = Txt('heads 0, tails 0 → Beta(2, 3)', 24, BLUE).next_to(ax, UP, buff=0.12).align_to(ax, RIGHT)
        row = VGroup()
        self.play(FadeIn(info))
        self.say('each flip multiplies by $\\theta$ (heads) or $1-\\theta$ (tails): just add 1 to an exponent', 0.2)
        for k, fl in enumerate(flips):
            h += fl
            t_ += 1 - fl
            a, b = 2 + h, 3 + t_
            new = curve(ax, th, np.minimum(stats.beta.pdf(th, a, b), 7.2), BLUE, 4)
            mode = (a - 1) / (a + b - 2)
            chip = Txt('H' if fl else 'T', 16, RED if fl else INK)
            if k < 30:
                chip.move_to(LEFT * 6.6 + RIGHT * 0.36 * k + UP * 2.65)
                row.add(chip)
            rt = 0.7 if k < 5 else 0.12
            anims = [Transform(post, new),
                     Transform(info, Txt(f'heads {h}, tails {t_} → Beta({a}, {b})   MAP = {mode:.2f}', 24, BLUE)
                               .move_to(info, aligned_edge=RIGHT))]
            if k < 30:
                anims.append(FadeIn(chip))
            self.play(*anims, run_time=rt)
            if k == 4:
                self.play(Create(truth), FadeIn(tl))
                self.say('few flips: the prior still matters, the posterior is wide', 0.8)
                self.say('many flips: the data take over and the posterior narrows around 0.7', 0.0)
        self.wait(2.5)


class LSLine(Base):
    def construct(self):
        self.title('Least squares: the line with the smallest total area of squares')
        pts = np.array([[0.5, 1.2], [1.5, 1.9], [2.5, 3.4], [3.5, 3.1], [4.5, 4.6], [5.5, 4.9]])
        ax = mk_axes([0, 6.5, 1], [-0.5, 7, 1], 6.5 * 0.86, 7.5 * 0.86).move_to(LEFT * 2.6 + DOWN * 0.35)
        A = np.c_[pts[:, 0], np.ones(6)]
        a_ls, b_ls = np.linalg.lstsq(A, pts[:, 1], rcond=None)[0]
        a = ValueTracker(0.0)
        b = ValueTracker(3.2)

        def scene_part():
            av, bv = a.get_value(), b.get_value()
            g = VGroup(curve(ax, [0, 6.5], [bv, av * 6.5 + bv], ORANGE, 4))
            J = 0
            for x, y in pts:
                yh = av * x + bv
                r = y - yh
                J += r * r
                lo, hi = P(ax, [x, x + abs(r)], [min(y, yh), max(y, yh)])
                g.add(Rectangle(width=hi[0] - lo[0] + 1e-4, height=hi[1] - lo[1] + 1e-4, stroke_color=RED, stroke_width=1.5,
                                fill_color=RED, fill_opacity=0.25).move_to((lo + hi) / 2))
                g.add(Line(ax.c2p(x, yh), ax.c2p(x, y), color=RED, stroke_width=3))
            g.add(Txt(f'slope a = {av:.2f}\nintercept b = {bv:.2f}\n\nJ = total red area\n   = {J:.2f}', 28, INK)
                  .move_to(RIGHT * 4.3 + UP * 0.6))
            return g

        dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.08, color=INK) for x, y in pts])
        self.play(Create(ax), FadeIn(dots))
        self.add(always_redraw(scene_part))
        self.bring_to_front(dots)
        self.say('each error $y_i-(ax_i+b)$ becomes a square; the cost $J$ is their total area', 0.5)
        for av, bv in [(1.2, -0.4), (0.3, 3.8), (0.9, 0.6)]:
            self.play(a.animate.set_value(av), b.animate.set_value(bv), run_time=2)
        self.say('least squares = the one line where the total area is smallest', 0.2)
        self.play(a.animate.set_value(a_ls), b.animate.set_value(b_ls), run_time=2.5)
        self.say(f'here: $a={a_ls:.3f}$, $b={b_ls:.3f}$ (from the two normal equations)', 3)


# ------------------------------------------------------------------ Part 4
class ROCSweep(Base):
    def construct(self):
        self.title(r'The ROC: slide the threshold, record ($P_{FA}$, $P_D$) every time')
        ax = mk_axes([-3.5, 5.5, 1], [0, 0.45, 0.1], 7.6, 3.6).move_to(LEFT * 2.9 + DOWN * 0.2)
        roc = mk_axes([0, 1, 0.2], [0, 1, 0.2], 3.8, 3.8).move_to(RIGHT * 4.6 + DOWN * 0.2)
        labs = VGroup(MT('$P_{FA}$', 20).next_to(roc, DOWN, buff=0.1), MT('$P_D$', 20).next_to(roc, LEFT, buff=0.1),
                      xlabel(roc, 1, '1', 16), ylabel(roc, 1, '1', 16), xlabel(ax, 5.5, '$x$', 20),
                      MT(r'$\mathcal{H}_0$: $\mathcal{N}(0,1)$', 20, BLUE).next_to(ax.c2p(-2.6, 0.38), UP),
                      MT(r'$\mathcal{H}_1$: $\mathcal{N}(2,1)$', 20, RED).next_to(ax.c2p(3.8, 0.38), UP),
                      DashedLine(roc.c2p(0, 0), roc.c2p(1, 1), color=GREY, stroke_width=2))
        x = np.linspace(-3.5, 5.5, 600)
        p0, p1 = stats.norm.pdf(x), stats.norm.pdf(x, 2)
        g = ValueTracker(4.5)

        def shade():
            gv = g.get_value()
            m = x >= gv
            out = VGroup(area(ax, x[m], p1[m], RED, 0.3), area(ax, x[m], p0[m], BLUE, 0.55),
                         DashedLine(ax.c2p(gv, 0), ax.c2p(gv, 0.45), color=INK, stroke_width=3),
                         MT(r'$\gamma$', 22).next_to(ax.c2p(gv, 0.45), UP, buff=0.05))
            gs = np.linspace(4.5, max(gv, -3.4), 300) if gv < 4.5 else np.array([4.5])
            if len(gs) > 1:
                out.add(curve(roc, stats.norm.sf(gs), stats.norm.sf(gs - 2), GREEN, 4))
            out.add(Dot(roc.c2p(stats.norm.sf(gv), stats.norm.sf(gv - 2)), radius=0.09, color=GREEN))
            out.add(Txt(f'γ = {gv:+.2f}\nP_FA = {stats.norm.sf(gv):.3f} (blue)\nP_D  = {stats.norm.sf(gv - 2):.3f} (red)',
                        22).next_to(roc, UP, buff=0.15))
            return out

        self.play(Create(ax), Create(roc), FadeIn(labs))
        self.play(Create(curve(ax, x, p0, BLUE, 4)), Create(curve(ax, x, p1, RED, 4)))
        self.add(always_redraw(shade))
        self.say('threshold far right: almost never say "yes" → both areas ≈ 0 → ROC point (0, 0)', 0.3)
        self.play(g.animate.set_value(1.0), run_time=5, rate_func=linear)
        self.say('γ = 1: $P_{FA}=Q(1)=0.159$, $P_D=Q(-1)=0.841$', 1.2)
        self.play(g.animate.set_value(-3.4), run_time=4, rate_func=linear)
        self.say('every threshold is one point; together they draw the ROC, bending to the top-left', 3)


class BayesThreshold(Base):
    def construct(self):
        self.title(r'Bayes detector: weight each PDF by its prior; decide where the weighted curves cross')
        ax = mk_axes([-3.5, 5.5, 1], [0, 0.48, 0.1], 11.8, 4.2).shift(DOWN * 0.4)
        x = np.linspace(-3.5, 5.5, 600)
        P1 = ValueTracker(0.5)
        labs = VGroup(xlabel(ax, 5.5, '$x$', 20), *[xlabel(ax, k, str(k), 16) for k in range(-3, 6)])

        def part():
            p1 = P1.get_value()
            p0 = 1 - p1
            gth = 1 + math.log(p0 / p1) / 2
            g = VGroup(curve(ax, x, p0 * stats.norm.pdf(x), BLUE, 4), curve(ax, x, p1 * stats.norm.pdf(x, 2), RED, 4))
            lo, hi = P(ax, [gth, 5.5], [0, 0.48])
            if gth < 5.5:
                g.add(Rectangle(width=hi[0] - lo[0], height=hi[1] - lo[1], stroke_width=0, fill_color=RED,
                                fill_opacity=0.07).move_to((lo + hi) / 2))
            g.add(DashedLine(ax.c2p(gth, 0), ax.c2p(gth, 0.48), color=INK, stroke_width=3))
            g.add(Txt(f'P0 = {p0:.2f}   P1 = {p1:.2f}   λ = P0/P1 = {p0 / p1:.2f}   →   decide H1 for x > {gth:.2f}',
                      24).next_to(ax, UP, buff=0.12))
            g.add(MT(r'$P_0\,p(x\mid\mathcal{H}_0)$', 20, BLUE).next_to(ax.c2p(-2.2, p0 * 0.25), UP))
            g.add(MT(r'$P_1\,p(x\mid\mathcal{H}_1)$', 20, RED).next_to(ax.c2p(4.0, p1 * 0.2), UP))
            return g

        self.play(Create(ax), FadeIn(labs))
        self.add(always_redraw(part))
        self.say('equal priors: the curves cross halfway between the means, at $x=1$', 1.5)
        self.say('make $\\mathcal{H}_1$ rarer: its curve shrinks, the crossing moves right', 0.2)
        self.play(P1.animate.set_value(0.1), run_time=4)
        self.say('$P_1=0.1$: $\\lambda=9$, decide $\\mathcal{H}_1$ only for $x>2.10$ (rare events need stronger evidence)', 1.5)
        self.play(P1.animate.set_value(0.8), run_time=4)
        self.say('$\\mathcal{H}_1$ common: the bar drops, you say "yes" more easily', 2.5)


class MatchedFilter(Base):
    def construct(self):
        self.title(r'Matched filter: slide the known pattern along the data, multiply and add')
        rng = np.random.default_rng(2)
        s = np.array([1, 2, 3, 2, 1.])
        Nn, pos = 60, 31
        x = rng.normal(0, 0.8, Nn)
        x[pos:pos + 5] += s
        top = mk_axes([-1, Nn, 5], [-3.5, 5.5, 1], 12.4, 2.6).move_to(UP * 1.3)
        bot = mk_axes([-1, Nn, 5], [-10, 25, 5], 12.4, 2.3).move_to(DOWN * 1.9)
        corr = np.array([np.dot(x[k:k + 5], s) for k in range(Nn - 4)])
        thr = 0.5 * np.dot(s, s)
        labs = VGroup(MT('data $x_n$ (pattern hidden at $n=31$)', 20).next_to(top, UP, buff=0.05).align_to(top, LEFT),
                      MT(r'output $\sum_n x_n s_n$ for each position', 20).next_to(bot, UP, buff=0.05)
                      .align_to(bot, LEFT),
                      DashedLine(bot.c2p(-1, thr), bot.c2p(Nn, thr), color=PURPLE, stroke_width=2),
                      MT(r'threshold $\frac{1}{2}\sum s_n^2=9.5$', 18, PURPLE).next_to(bot.c2p(Nn, thr), UP, buff=0.05)
                      .shift(LEFT * 1.2))
        k = ValueTracker(0)

        def slide():
            kv = int(round(k.get_value()))
            g = VGroup(stems(top, np.arange(kv, kv + 5), s, ORANGE, r=0.06, w=6))
            lo, hi = P(top, [kv - 0.5, kv + 4.5], [-3.5, 5.5])
            g.add(Rectangle(width=hi[0] - lo[0], height=hi[1] - lo[1], stroke_color=ORANGE, stroke_width=2,
                            fill_opacity=0).move_to((lo + hi) / 2))
            g.add(curve(bot, np.arange(kv + 1), corr[:kv + 1], GREEN, 4))
            g.add(Dot(bot.c2p(kv, corr[kv]), radius=0.08, color=GREEN))
            return g

        self.play(Create(top), Create(bot), FadeIn(labs))
        self.play(FadeIn(stems(top, np.arange(Nn), x, GREY, r=0.04, w=2.5)))
        self.say('orange: the known pattern $s=[1,2,3,2,1]$. Can you spot it in the grey noise?', 1.2)
        self.add(always_redraw(slide))
        self.play(k.animate.set_value(Nn - 5), run_time=9, rate_func=linear)
        self.say('where the pattern really is, all products are positive and the sum shoots up', 1.2)
        self.say('that is the matched filter = a correlator: the best linear detector for white noise', 3)


SCENES = [SamplingAlias, Phasor, EnergyPower, Windowing, ZeroPad, PeriodogramAverage, SlideCorr, SlideMA, ARRecursion,
          BayesZoom, Ensemble, LikelihoodSweep, BayesUpdate, LSLine, ROCSweep, BayesThreshold, MatchedFilter]
