"""Video podcasts: two voices (edge-tts neural TTS) talking over Manim visuals, one Scene per episode.

A line of dialogue = self.say(who, text, *animations): the audio is synthesised (cached), placed at the current
scene time, the subtitle is swapped, the animations play, and the scene waits until the voice is done.
Render with scripts/podcast/render.py.
"""
import asyncio
import hashlib
import html
import os
import subprocess
import sys
import tempfile
import textwrap
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import edge_tts  # noqa: E402
from manim import (DOWN, LEFT, RIGHT, UL, UP, WHITE, FadeIn, FadeOut, MarkupText, Rectangle,  # noqa: E402
                   RoundedRectangle, Scene, VGroup, Wait, Write)
from vidkit import FONT, GREY, INK, MT, PAPER, Txt  # noqa: E402
from manim.animation.animation import prepare_animation  # noqa: E402

# who -> (voice, rate, display name, subtitle colour)
VOICE = {
    'T': ('en-US-AvaMultilingualNeural', '-5%', 'Ava', '#1f5fae'),
    'S': ('en-US-BrianMultilingualNeural', '+0%', 'Ben', '#c26a12'),
}
AUD = os.path.join(tempfile.gettempdir(), 'ssp_pod_audio')
os.makedirs(AUD, exist_ok=True)
ONLY = [s for s in os.environ.get('POD_SECTIONS', '').split(',') if s]


def tts(who, text):
    voice, rate = VOICE[who][:2]
    key = hashlib.md5(f'{voice}|{rate}|{text}'.encode()).hexdigest()[:16]
    p = os.path.join(AUD, key + '.mp3')
    for attempt in range(5):
        if os.path.exists(p) and os.path.getsize(p) > 0:
            break
        try:
            asyncio.run(edge_tts.Communicate(text, voice, rate=rate).save(p + '.w'))
            if os.path.getsize(p + '.w') > 0:
                os.replace(p + '.w', p)
        except Exception as e:  # the service drops a request now and then
            print('tts retry', attempt, e, file=sys.stderr)
            time.sleep(2 + attempt * 2)
    if not (os.path.exists(p) and os.path.getsize(p) > 0):
        raise RuntimeError('TTS failed for: ' + text[:60])
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                         capture_output=True, text=True).stdout
    return p, float(out)


def card(lines, fs=26, color=INK, fill=PAPER, buff=0.3, width=None):
    """A rounded box with lines of text/math stacked inside."""
    body = VGroup(*[MT(s, fs, color) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    w = max(body.width + 2 * buff, width or 0)
    box = RoundedRectangle(corner_radius=0.15, width=w, height=body.height + 2 * buff,
                           fill_color=fill, fill_opacity=1, stroke_color=GREY, stroke_width=1.5)
    body.move_to(box)
    if width:
        body.align_to(box, LEFT).shift(RIGHT * buff)
    return VGroup(box, body)


def chip(s, color, fs=22):
    t = MT(s, fs, '#ffffff')
    box = RoundedRectangle(corner_radius=0.18, width=t.width + 0.4, height=t.height + 0.26,
                           fill_color=color, fill_opacity=1, stroke_width=0)
    t.move_to(box)
    return VGroup(box, t)


def stack(lines, fs=30, buff=0.28, color=INK):
    return VGroup(*[MT(s, fs, color) if isinstance(s, str) else s for s in lines]).arrange(DOWN, buff=buff)


class Pod(Scene):
    episode = ''
    sections = []

    def setup(self):
        self.camera.background_color = WHITE
        self.add(Rectangle(width=14.4, height=1.5, fill_color=PAPER, fill_opacity=1, stroke_width=0)
                 .to_edge(DOWN, buff=0))
        self.sub = None
        self.head = None
        self.board = VGroup()

    def construct(self):
        for name in self.sections:
            if not ONLY or name in ONLY:
                getattr(self, name)()

    # ----- the frame around the board -----
    def header(self, s):
        new = Txt(f'{self.episode}  ·  {s}', 20, GREY).to_corner(UL, buff=0.28)
        if self.head is not None:
            self.remove(self.head)
        self.add(new)
        self.head = new

    def subtitle(self, who, text):
        name, col = VOICE[who][2], VOICE[who][3]
        body = '\n'.join(textwrap.wrap(text, 92))
        m = MarkupText(f'<span foreground="{col}" weight="bold">{name}</span>   {html.escape(body, quote=False)}',
                       font=FONT, font_size=17, color=INK, line_spacing=0.6)
        if m.width > 13.6:
            m.width = 13.6
        if m.height > 1.22:
            m.height = 1.22
        m.move_to([0, -3.25, 0])
        if self.sub is not None:
            self.remove(self.sub)
        self.add(m)
        self.sub = m

    # ----- dialogue -----
    def say(self, who, text, *steps, pause=0.35):
        path, dur = tts(who, text)
        self.subtitle(who, text)
        self.add_sound(path)
        used = 0.0
        for st in steps:
            if isinstance(st, (int, float)):
                self.wait(st)
                used += st
                continue
            group = [prepare_animation(a) for a in (st if isinstance(st, (list, tuple)) else [st])]
            if not group:
                continue
            self.play(*group)
            used += max(a.run_time for a in group)
        rest = dur + pause - used
        if rest > 0.03:
            self.wait(rest, frozen_frame=True)

    def think(self, text, shown, secs=5.0):
        """Ava asks the listener; a 'your turn' strip and a countdown give time to answer before the reveal."""
        from manim import Rectangle as _R
        path, dur = tts('T', text)
        self.subtitle('T', text)
        self.add_sound(path)
        q = MT('YOUR TURN  ·  ' + shown, 25, '#6a3d9a')
        if q.width > 12.6:
            q.width = 12.6
        bg = RoundedRectangle(corner_radius=0.14, width=q.width + 0.6, height=q.height + 0.42, fill_color=WHITE,
                              fill_opacity=0.96, stroke_color='#6a3d9a', stroke_width=2.5)
        strip = VGroup(bg, q).move_to([0, -1.95, 0])
        q.move_to(bg)
        bar = _R(width=bg.width - 0.3, height=0.08, fill_color='#6a3d9a', fill_opacity=1, stroke_width=0)
        bar.next_to(bg, DOWN, buff=0.0).shift(UP * 0.1)
        self.play(FadeIn(strip, run_time=0.3))
        self.wait(max(0.05, dur - 0.3), frozen_frame=True)
        self.add(bar)
        self.play(bar.animate(run_time=secs, rate_func=lambda t: t).stretch(0.01, 0, about_edge=LEFT))
        self.play(FadeOut(strip, run_time=0.3), FadeOut(bar, run_time=0.3))

    # ----- board: everything above the subtitle band -----
    def put(self, m, anim=FadeIn, rt=0.7, **kw):
        if m.width > 13.6:
            m.width = 13.6
        self.board.add(m)
        return anim(m, run_time=rt, **kw)

    def write(self, m, rt=1.0):
        return self.put(m, Write, rt)

    def wipe(self, rt=0.5):
        if len(self.board) == 0:
            return Wait(0.05)
        old = self.board
        self.board = VGroup()
        return FadeOut(old, run_time=rt)

    def title_card(self, title, sub, chips):
        t = MT(title, 44).move_to(UP * 1.1)
        s = MT(sub, 28, GREY).next_to(t, DOWN, buff=0.35)
        c = VGroup(*chips).arrange(RIGHT, buff=0.3).next_to(s, DOWN, buff=0.5)
        return [self.put(t, rt=0.8), self.put(s, rt=0.8), self.put(c, rt=0.8)]


def np_grid(a, b, n=400):
    return np.linspace(a, b, n)


def matrix(rows, fs=30, hb=0.55, vb=0.28, color=INK):
    """A bracketed matrix/vector of math entries (mathtext has no matrix environment)."""
    from manim import VMobject
    ents = VGroup(*[Txt(c, fs, color) for r in rows for c in r])
    ents.arrange_in_grid(rows=len(rows), cols=len(rows[0]), buff=(hb, vb))
    top, bot = ents.get_top()[1] + 0.12, ents.get_bottom()[1] - 0.12
    x0, x1 = ents.get_left()[0] - 0.14, ents.get_right()[0] + 0.14

    def br(x, d):
        m = VMobject(stroke_color=color, stroke_width=2.5)
        m.set_points_as_corners([[x + d, top, 0], [x, top, 0], [x, bot, 0], [x + d, bot, 0]])
        return m
    return VGroup(br(x0, 0.12), ents, br(x1, -0.12))
