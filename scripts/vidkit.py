"""Shared helpers for the Manim animations in videos.py (style = the static figures)."""
import hashlib
import os
import re
import tempfile

import matplotlib

matplotlib.use('Agg')
import manimpango
import matplotlib.pyplot as plt
import numpy as np
from manim import (DOWN, UP, WHITE, Dot, FadeIn, FadeOut, Line, Scene, SVGMobject, Text, VGroup, VMobject, Axes,
                   config)

manimpango.register_font(os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf'))
FONT = 'DejaVu Sans'

INK = '#1d1b19'
RED = '#b3261e'
BLUE = '#1f5fae'
GREEN = '#2e7d32'
ORANGE = '#d9822b'
PURPLE = '#6a3d9a'
GREY = '#8a8580'
PAPER = '#f3eee4'
LIGHT = '#e6e1d8'

config.background_color = WHITE
plt.rcParams.update({'mathtext.fontset': 'cm', 'svg.fonttype': 'path', 'font.family': 'DejaVu Sans'})
CACHE = os.path.join(tempfile.gettempdir(), 'ssp_guide_mathtext')
os.makedirs(CACHE, exist_ok=True)
EMPTY_PATH = re.compile(r'(<path(?![^>]*\sd=)[^>]*?)(/>)')
SCALE = 0.0152  # manim units per (pt of a 40-pt matplotlib render) per font-size unit / 40


def MT(s, fs=26, color=INK):
    """Text with $math$ rendered by matplotlib mathtext (no LaTeX needed), as a vector mobject."""
    key = hashlib.md5(f'{s}|{color}'.encode()).hexdigest()[:16]
    p = os.path.join(CACHE, key + '.svg')
    if not os.path.exists(p):
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.patch.set_visible(False)
        fig.text(0, 0, s, fontsize=40, color=color)
        fig.savefig(p, transparent=True, bbox_inches='tight', pad_inches=0.01)
        plt.close(fig)
        with open(p, encoding='utf-8') as f:
            svg = f.read()
        with open(p, 'w', encoding='utf-8') as f:
            f.write(EMPTY_PATH.sub(r'\1 d="M 0 0"\2', svg))
    with open(p, encoding='utf-8') as f:
        h = float(re.search(r'height="([\d.]+)pt"', f.read()).group(1))
    m = SVGMobject(p)
    m.height = h * fs / 40 * SCALE
    return m


def Txt(s, fs=26, color=INK, **kw):
    return Text(s, font=FONT, font_size=fs, color=color, **kw)


def mk_axes(xr, yr, w, h, color=INK):
    return Axes(x_range=xr, y_range=yr, x_length=w, y_length=h, tips=False,
                axis_config=dict(color=color, stroke_width=2, include_ticks=False))


def P(ax, xs, ys):
    """Vectorised coords_to_point (axes are linear)."""
    o = np.array(ax.c2p(0, 0))
    ux = np.array(ax.c2p(1, 0)) - o
    uy = np.array(ax.c2p(0, 1)) - o
    xs = np.atleast_1d(np.asarray(xs, float))
    ys = np.atleast_1d(np.asarray(ys, float))
    return o + np.outer(xs, ux) + np.outer(ys, uy)


def curve(ax, xs, ys, color=BLUE, w=4, opacity=1.0):
    m = VMobject(stroke_color=color, stroke_width=w, stroke_opacity=opacity)
    m.set_points_as_corners(P(ax, xs, ys))
    return m


def area(ax, xs, ys, color=BLUE, op=0.3, base=0.0):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    if len(xs) < 2:
        return VMobject()
    pts = P(ax, np.r_[xs, xs[::-1], xs[:1]], np.r_[ys, np.full(len(xs), base), ys[:1]])
    m = VMobject(stroke_width=0, fill_color=color, fill_opacity=op)
    m.set_points_as_corners(pts)
    return m


def stems(ax, xs, ys, color=BLUE, r=0.05, w=3, base=0.0):
    g = VGroup()
    for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)):
        if abs(y - base) > 1e-9:
            g.add(Line(ax.c2p(x, base), ax.c2p(x, y), color=color, stroke_width=w))
        if r:
            g.add(Dot(ax.c2p(x, y), radius=r, color=color))
    return g


def xlabel(ax, x, s, fs=22, color=INK, buff=0.12):
    return MT(s, fs, color).next_to(ax.c2p(x, ax.y_range[0]), DOWN, buff=buff)


def ylabel(ax, y, s, fs=22, color=INK, buff=0.12):
    from manim import LEFT
    return MT(s, fs, color).next_to(ax.c2p(ax.x_range[0], y), LEFT, buff=buff)


class Base(Scene):
    """White background, a title, and one caption line at the bottom that the scene rewrites."""

    def setup(self):
        self.camera.background_color = WHITE
        self._cap = None

    def title(self, s, fs=32):
        t = MT(s, fs)
        if t.width > 13.4:
            t.width = 13.4
        t.to_edge(UP, buff=0.3)
        self.play(FadeIn(t, run_time=0.6))
        return t

    def say(self, s, wait=1.6, fs=25, color=INK):
        new = MT(s, fs, color).to_edge(DOWN, buff=0.32)
        if new.width > 13.4:
            new.width = 13.4
        if self._cap is not None:
            self.play(FadeOut(self._cap, run_time=0.3), FadeIn(new, run_time=0.45))
        else:
            self.play(FadeIn(new, run_time=0.45))
        self._cap = new
        if wait:
            self.wait(wait)
