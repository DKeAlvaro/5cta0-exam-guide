"""Theory figures: one picture per idea, for the "from zero" sections of every page.

Writes docs/img/gen/*.svg (same style as plots.py, which holds the exam-solution figures).
Run: python scripts/theory_plots.py            (all)
     python scripts/theory_plots.py p0_sine ... (only these)
"""
import math
import sys

import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle
from scipy.signal import lfilter
from scipy.signal.windows import blackmanharris

from plots import (BLUE, GREEN, GREY, INK, ORANGE, PI_TICKS, PURPLE, RED, ar_psd, ma_psd, plt, save,
                   stats, yw)

PAPER = '#f3eee4'
TEAL = '#0f766e'
HALF_PI_TICKS = ([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi], ['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])


def stems(ax, x, y, color=BLUE, ms=5, lw=1.6, base=0.0, label=None, marker='o', alpha=1.0):
    ax.vlines(x, base, y, color=color, lw=lw, alpha=alpha)
    ax.plot(x, y, marker, color=color, ms=ms, label=label, ls='none', alpha=alpha)


def arrow(ax, x0, y0, x1, y1, color=INK, lw=2, ls='-', style='-|>', ms=14):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=ms,
                                shrinkA=0, shrinkB=0))


def half_pi(ax, label=True):
    ax.set_xticks(*HALF_PI_TICKS)
    ax.set_xlim(0, np.pi)
    if label:
        ax.set_xlabel(r'$\theta$ (rad/sample)')


def full_pi(ax, label=True):
    ax.set_xticks(*PI_TICKS)
    ax.set_xlim(-np.pi, np.pi)
    if label:
        ax.set_xlabel(r'$\theta$ (rad/sample)')


def ar2_coeffs(radius=0.9, angle=1.0):
    return [1, -2 * radius * math.cos(angle), radius ** 2]


def ar2_data(N, seed, radius=0.9, angle=1.0):
    rng = np.random.default_rng(seed)
    return lfilter([1], ar2_coeffs(radius, angle), rng.standard_normal(N + 300))[300:]


def ar2_true(th, radius=0.9, angle=1.0):
    a = ar2_coeffs(radius, angle)
    return 1 / np.abs(a[0] + a[1] * np.exp(-1j * th) + a[2] * np.exp(-2j * th)) ** 2


def pgram(x, nfft=2048):
    return np.abs(np.fft.fft(x, nfft)[:nfft // 2 + 1]) ** 2 / len(x)


def db(p):
    return 10 * np.log10(np.maximum(p, 1e-12))


# ================================================================== Chapter 0
def p0_sampling():
    fs = 8
    def x(t):
        return np.sin(2 * np.pi * 1.2 * t) + 0.45 * np.cos(2 * np.pi * 2.9 * t + 0.6)
    t = np.linspace(0, 1, 1000)
    n = np.arange(9)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.3), sharey=True)
    ax = axs[0]
    ax.plot(t, x(t), color=BLUE)
    ax.set_title('continuous time $x(t)$: a value at every instant', fontsize=10.5)
    ax.set_xlabel('$t$ (seconds)')
    ax = axs[1]
    ax.plot(t, x(t), color=GREY, lw=1, alpha=.45)
    stems(ax, n / fs, x(n / fs), color=RED)
    ax.set_xticks(n / fs, [str(k) for k in n])
    ax.set_xlabel('$n$ (sample number); sample $n$ is taken at time $t=nT_s$')
    ax.set_title(r'discrete time $x[n]=x(nT_s)$: just a list of numbers', fontsize=10.5)
    y0 = -1.62
    arrow(ax, 2 / fs, y0, 3 / fs, y0, style='<->', lw=1.3, ms=10)
    ax.text(2.5 / fs, y0 + 0.08, '$T_s=1/f_s$', ha='center', va='bottom', fontsize=9.5)
    ax.annotate('$x[3]=x(3T_s)$', xy=(3 / fs, x(3 / fs)), xytext=(4.1 / fs, 1.45), fontsize=9.5,
                arrowprops=dict(arrowstyle='->', color=INK, lw=1))
    for a in axs:
        a.axhline(0, color=GREY, lw=.7)
        a.set_ylim(-1.8, 1.8)
    save(fig, 'p0_sampling')


def p0_sine():
    t = np.linspace(0, 2, 1000)
    fig, ax = plt.subplots(figsize=(8, 3.3))
    ax.plot(t, 2 * np.sin(2 * np.pi * t), color=BLUE, label=r'$2\sin(2\pi\cdot1\cdot t)$: $A=2$, $f=1$ Hz')
    ax.plot(t, np.sin(2 * np.pi * 3 * t), color=ORANGE, lw=1.4, label=r'$\sin(2\pi\cdot3\cdot t)$: $A=1$, $f=3$ Hz')
    arrow(ax, 0.25, 0, 0.25, 2, color=BLUE, style='<->', lw=1.4, ms=10)
    ax.text(0.28, 0.95, '$A=2$', color=BLUE, fontsize=10)
    arrow(ax, 1.0, -2.35, 2.0, -2.35, color=BLUE, style='<->', lw=1.4, ms=10)
    ax.text(1.5, -2.28, 'one period $T=1/f=1$ s (one full wiggle)', ha='center', va='bottom', color=BLUE,
            fontsize=9.5)
    ax.axhline(0, color=GREY, lw=.8)
    ax.set_ylim(-2.7, 2.6)
    ax.set_xlabel('$t$ (s)')
    ax.legend(fontsize=9, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
    save(fig, 'p0_sine')


def p0_alias():
    fs = 50
    t = np.linspace(0, 0.2, 2000)
    n = np.arange(11)
    tn = n / fs
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    ax = axs[0]
    ax.plot(t, np.cos(2 * np.pi * 25 * t), color=GREY, lw=1.2)
    stems(ax, tn, np.cos(np.pi * n), color=RED)
    ax.set_title(r'$f=25$ Hz at $f_s=50$ Hz: $\theta=\pi$, samples $+1,-1,+1,\dots$', fontsize=10)
    ax = axs[1]
    ax.plot(t, np.cos(2 * np.pi * 10 * t), color=BLUE, lw=1.8, label=r'10 Hz: $\theta=2\pi\frac{10}{50}=0.4\pi$')
    ax.plot(t, np.cos(2 * np.pi * 40 * t), color=ORANGE, lw=1.0, label=r'40 Hz: $\theta=1.6\pi$, same as $-0.4\pi$')
    stems(ax, tn, np.cos(2 * np.pi * 10 * tn), color=RED, label='the samples (identical)')
    ax.set_title('10 Hz and 40 Hz give exactly the same samples', fontsize=10)
    ax.legend(fontsize=8.5, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2)
    for a in axs:
        a.axhline(0, color=GREY, lw=.7)
        a.set_xlabel('$t$ (s)')
        a.set_ylim(-1.3, 1.3)
    save(fig, 'p0_alias')


def p0_complex():
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.3))
    ax = axs[0]
    a, b = 3, 2
    ax.plot([a, a], [0, b], ':', color=INK, lw=1)
    ax.plot([0, a], [b, b], ':', color=INK, lw=1)
    arrow(ax, 0, 0, a, b, color=BLUE)
    arrow(ax, 0, 0, a, -b, color=GREY, ls='--', lw=1.6)
    ax.text(a + 0.1, b + 0.1, '$z=a+jb=3+2j$', color=BLUE, fontsize=10)
    ax.text(a + 0.1, -b - 0.35, r'$z^*=3-2j$ (mirror image)', color=GREY, fontsize=9.5)
    ax.text(0.55, 1.25, r'$|z|=\sqrt{3^2+2^2}=\sqrt{13}$', rotation=33.7, color=BLUE, fontsize=9.5)
    ax.text(a / 2, -0.38, '$a=3$ (right)', ha='center', fontsize=9.5)
    ax.text(a + 0.12, b / 2, '$b=2$ (up)', va='center', fontsize=9.5)
    ax.set_xlim(-0.6, 5.3)
    ax.set_ylim(-2.7, 2.9)
    ax.set_title('a complex number is an arrow', fontsize=10.5)
    ax = axs[1]
    th = np.deg2rad(50)
    c, s = math.cos(th), math.sin(th)
    circ = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(circ), np.sin(circ), color=GREY, lw=1.2)
    ax.plot([c, 2 * c], [s, 0], ':', color=INK, lw=1)
    ax.plot([c, 2 * c], [-s, 0], ':', color=INK, lw=1)
    arrow(ax, 0, 0, c, s, color=BLUE)
    arrow(ax, 0, 0, c, -s, color=GREY, ls='--', lw=1.6)
    arrow(ax, 0, 0, 2 * c, 0, color=RED, lw=2.4)
    ax.plot([c, c], [0, s], color=ORANGE, lw=2.2)
    ax.plot([0, c], [0, 0], color=GREEN, lw=4, alpha=.8, solid_capstyle='butt')
    arc = np.linspace(0, th, 50)
    ax.plot(0.28 * np.cos(arc), 0.28 * np.sin(arc), color=INK, lw=1)
    ax.text(0.32, 0.1, r'$\theta$', fontsize=11)
    ax.text(c + 0.05, s + 0.07, r'$e^{j\theta}=\cos\theta+j\sin\theta$', color=BLUE, fontsize=10)
    ax.text(c + 0.05, -s - 0.17, r'$e^{-j\theta}$', color=GREY, fontsize=10)
    ax.text(c / 2, -0.17, r'$\cos\theta$', color=GREEN, ha='center', fontsize=10)
    ax.text(c + 0.04, s / 2, r'$\sin\theta$', color=ORANGE, fontsize=10)
    ax.text(2 * c + 0.04, 0.08, r'$e^{j\theta}+e^{-j\theta}=2\cos\theta$', color=RED, fontsize=10)
    ax.set_xlim(-1.25, 2.6)
    ax.set_ylim(-1.25, 1.25)
    ax.set_title('the unit circle: length 1, angle $\\theta$', fontsize=10.5)
    for a_ in axs:
        a_.axhline(0, color=GREY, lw=.7)
        a_.axvline(0, color=GREY, lw=.7)
        a_.set_aspect('equal')
        a_.set_xlabel('real part')
        a_.set_ylabel('imaginary part')
    save(fig, 'p0_complex')


def p0_integral_sum():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.4), sharey=True)
    t = np.linspace(0, 4, 500)
    ax = axs[0]
    ax.plot(t, np.exp(-2 * t), color=BLUE)
    ax.fill_between(t, np.exp(-2 * t), color=BLUE, alpha=.25)
    ax.text(0.9, 0.6, r'shaded area $=\int_0^\infty e^{-2t}\,dt=\frac{1}{2}$', fontsize=10.5)
    ax.set_title(r'round brackets $x(t)$: the total is an area ($\int$)', fontsize=10.5)
    ax.set_xlabel('$t$')
    ax = axs[1]
    n = np.arange(0, 5)
    ax.bar(n, np.exp(-2 * n), width=0.55, color=RED, alpha=.75)
    for k in n:
        ax.text(k, np.exp(-2 * k) + 0.03, f'{np.exp(-2 * k):.3f}', ha='center', fontsize=8.5)
    ax.text(0.9, 0.6, r'total $=1+0.135+0.018+\dots=1.1565$', fontsize=10.5)
    ax.set_title(r'square brackets $x[n]$: the total is a sum ($\sum$)', fontsize=10.5)
    ax.set_xlabel('$n$')
    ax.set_xticks(n)
    axs[0].set_ylim(0, 1.15)
    save(fig, 'p0_integral_sum')


def p0_geometric():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.3), gridspec_kw=dict(width_ratios=[1.25, 1]))
    ax = axs[0]
    x0 = 0
    labels = ['1', r'$\frac{1}{2}$', r'$\frac{1}{4}$', r'$\frac{1}{8}$', '', '', '', '']
    for k in range(9):
        w = 0.5 ** k
        ax.add_patch(Rectangle((x0, 0), w, 1, fc=[BLUE, ORANGE][k % 2], alpha=.35 + .3 * (k % 2), ec='white', lw=1))
        if labels[k:k + 1] and labels[k]:
            ax.text(x0 + w / 2, 0.5, labels[k], ha='center', va='center', fontsize=13)
        x0 += w
    ax.axvline(2, color=RED, ls='--', lw=1.5)
    ax.text(2.03, 1.1, r'$\frac{1}{1-r}=2$', color=RED, fontsize=11)
    ax.set_xlim(0, 2.45)
    ax.set_ylim(0, 1.35)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title(r'$1+\frac{1}{2}+\frac{1}{4}+\dots$: each piece fills half of the gap left', fontsize=10.5)
    ax = axs[1]
    Ns = np.arange(0, 13)
    for r, col in [(0.5, ORANGE), (math.exp(-2), BLUE)]:
        S = np.cumsum(r ** Ns)
        ax.plot(Ns, S, 'o-', color=col, ms=4, lw=1.4, label=rf'$r={r:.3g}$')
        ax.axhline(1 / (1 - r), color=col, ls='--', lw=1)
        ax.text(12.3, 1 / (1 - r), f'{1 / (1 - r):.4g}', color=col, va='center', fontsize=9)
    ax.set_xlabel('number of terms added ($N+1$)')
    ax.set_title(r'partial sums $1+r+\dots+r^N$ level off at $\frac{1}{1-r}$', fontsize=10.5)
    ax.legend(fontsize=9, loc='center right')
    ax.set_ylim(0.9, 2.15)
    save(fig, 'p0_geometric')


def p0_sin2():
    a = np.linspace(0, 4 * np.pi, 1000)
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    ticks = ([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi], ['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
    ax = axs[0]
    ax.plot(a, np.sin(a), color=GREY, lw=1.3, label=r'$\sin\alpha$: averages to 0')
    ax.plot(a, np.sin(a) ** 2, color=BLUE, label=r'$\sin^2\alpha$: never negative')
    ax.axhline(0, color=GREY, lw=.7)
    ax.set_ylim(-1.15, 1.5)
    ax.legend(fontsize=9, loc='upper center', ncol=2)
    ax.set_title('squaring flips the negative half up, and doubles the speed', fontsize=10)
    ax = axs[1]
    s2 = np.sin(a) ** 2
    ax.plot(a, s2, color=BLUE)
    ax.axhline(0.5, color=INK, ls='--', lw=1.2)
    ax.fill_between(a, s2, 0.5, where=s2 >= 0.5, interpolate=True, color=GREEN, alpha=.35, label=r'above $\frac{1}{2}$')
    ax.fill_between(a, s2, 0.5, where=s2 < 0.5, interpolate=True, color=ORANGE, alpha=.35, label=r'below $\frac{1}{2}$')
    ax.text(0.15, 1.13, r'$\sin^2\alpha=\frac{1}{2}-\frac{1}{2}\cos 2\alpha$', fontsize=11)
    ax.set_ylim(-0.05, 1.32)
    ax.legend(fontsize=9, loc='upper right', ncol=2)
    ax.set_title(r'humps above $\frac{1}{2}$ exactly fill the dips: average $=\frac{1}{2}$', fontsize=10)
    for x in axs:
        x.set_xticks(*ticks)
        x.set_xlabel(r'$\alpha$')
    save(fig, 'p0_sin2')


def p0_limit():
    T = np.linspace(0.3, 60, 3000)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.2))
    ax = axs[0]
    ax.plot(T, 0.5 + np.sin(T) / (2 * T), color=BLUE)
    ax.axhline(0.5, color=RED, ls='--', lw=1.3)
    ax.text(40, 0.55, r'settles on $\frac{1}{2}$', color=RED, fontsize=10)
    ax.set_ylim(0.3, 1.05)
    ax.set_xlabel('window length $T$')
    ax.set_title(r'average of $\cos^2 t$ over $[-\frac{T}{2},\frac{T}{2}]$ $=\frac{1}{2}+\frac{\sin T}{2T}$', fontsize=10)
    ax = axs[1]
    for c, col in [(1, BLUE), (3, ORANGE), (10, GREEN)]:
        ax.plot(T, c / T, color=col, label=f'$c={c}$')
    ax.set_ylim(0, 2)
    ax.set_xlabel('$T$')
    ax.legend(fontsize=9)
    ax.set_title(r'a fixed number divided by a growing $T$: $\frac{c}{T}\to0$', fontsize=10)
    save(fig, 'p0_limit')


def p0_spectrum():
    t = np.linspace(0, 1, 2000)
    x1 = np.cos(2 * np.pi * 5 * t)
    x2 = 0.5 * np.cos(2 * np.pi * 12 * t)
    fig, axs = plt.subplots(1, 2, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=[1.3, 1]))
    ax = axs[0]
    ax.plot(t, x1, color=BLUE, lw=1, ls='--', label='5 Hz tone, amplitude 1')
    ax.plot(t, x2, color=ORANGE, lw=1, ls='--', label='12 Hz tone, amplitude 0.5')
    ax.plot(t, x1 + x2, color=INK, lw=1.8, label='the signal = their sum')
    ax.set_xlabel('$t$ (s)')
    ax.set_ylim(-1.7, 2.7)
    ax.legend(fontsize=8, loc='upper center', ncol=3, handlelength=1.4, columnspacing=.8)
    ax.set_title('time: what you record', fontsize=10.5)
    ax = axs[1]
    for f0, h, col in [(5, 0.5, BLUE), (12, 0.25, ORANGE)]:
        stems(ax, [-f0, f0], [h, h], color=col, ms=7, lw=2.2)
        ax.text(f0, h + 0.03, f'{h:g}', ha='center', color=col, fontsize=9.5)
        ax.text(-f0, h + 0.03, f'{h:g}', ha='center', color=col, fontsize=9.5)
    ax.axhline(0, color=GREY, lw=.8)
    ax.set_xlim(-15, 15)
    ax.set_ylim(0, 0.65)
    ax.set_xlabel('frequency $f$ (Hz)')
    ax.set_title('frequency: the recipe (spectrum)', fontsize=10.5)
    save(fig, 'p0_spectrum')


def p0_ftd_dft():
    fs, N = 50, 24
    n = np.arange(N)
    x = np.cos(2 * np.pi * 10 * n / fs)
    f = np.linspace(0, 25, 3000)
    X = np.abs(np.exp(-2j * np.pi * np.outer(f, n) / fs) @ x)
    k = np.arange(N // 2 + 1)
    fk = k * fs / N
    Xk = np.abs(np.fft.fft(x))[:N // 2 + 1]
    fig, ax = plt.subplots(figsize=(8.6, 3.5))
    ax.plot(f, X, color=GREY, lw=1.5, label='FTD of the 24 samples: a continuous curve')
    ax.plot(fk, Xk, 'o', color=BLUE, ms=6, label=r'DFT: the same curve sampled at the bins $k\,f_s/N$')
    ax.vlines(fk, 0, Xk, color=BLUE, lw=.8, alpha=.5)
    arrow(ax, fk[1], 9.5, fk[2], 9.5, style='<->', lw=1.2, ms=9)
    ax.text(fk[1] - 0.2, 10.2, r'bin width $\frac{f_s}{N}=\frac{50}{24}\approx2.08$ Hz', fontsize=9.5)
    ax.set_xlabel('frequency (Hz)')
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 14.5)
    ax.legend(fontsize=9, loc='upper right')
    sec = ax.secondary_xaxis('top', functions=(lambda ff: 2 * np.pi * ff / fs, lambda th: th * fs / (2 * np.pi)))
    sec.set_xticks([np.pi / 2, np.pi], [r'$\theta=\pi/2$', r'$\theta=\pi$ ($f_s/2$)'])
    ax.set_title('10 Hz tone, $f_s=50$ Hz, $N=24$ samples', fontsize=10.5, pad=22)
    save(fig, 'p0_ftd_dft')


def p0_db():
    fs, N, L = 50, 256, 4096
    n = np.arange(N)
    x = np.cos(2 * np.pi * 10 * n / fs) + 0.02 * np.cos(2 * np.pi * 18 * n / fs)
    X = np.abs(np.fft.rfft(x * blackmanharris(N), L))
    X /= X.max()
    f = np.fft.rfftfreq(L, 1 / fs)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.3))
    ax = axs[0]
    ax.plot(f, X, color=BLUE)
    ax.annotate('the 18 Hz tone is here\n(height 0.02: invisible)', xy=(18, 0.03), xytext=(13.5, 0.5), fontsize=9,
                arrowprops=dict(arrowstyle='->', color=GREEN), color=GREEN)
    ax.set_title('linear scale', fontsize=10.5)
    ax.set_ylabel('$|X|$')
    ax = axs[1]
    ax.plot(f, 20 * np.log10(X + 1e-12), color=BLUE)
    ax.set_ylim(-88, 6)
    ax.axhline(-34, color=GREEN, ls=':', lw=1.2)
    ax.annotate(r'$20\log_{10}0.02=-34$ dB', xy=(18, -34), xytext=(19.5, -14), fontsize=9, color=GREEN,
                arrowprops=dict(arrowstyle='->', color=GREEN))
    ax.set_title('dB scale: tiny and huge in one picture', fontsize=10.5)
    ax.set_ylabel('dB')
    for a in axs:
        a.set_xlim(0, 25)
        a.set_xlabel('frequency (Hz)')
    save(fig, 'p0_db')


def p0_pdfs():
    fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.2))
    ax = axs[0]
    x = np.linspace(-0.5, 2.5, 1001)
    p = np.where((x >= 0) & (x <= 2), 0.5, 0)
    ax.plot(x, p, color=BLUE)
    ax.fill_between(x, p, where=(x >= 0.5) & (x <= 1.5), color=BLUE, alpha=.3)
    ax.text(1, 0.22, 'area = $1\\times\\frac{1}{2}$\n$=0.5$', ha='center', fontsize=10)
    ax.set_ylim(0, 0.8)
    ax.set_title(r'uniform on $[0,2]$: $P(0.5<X<1.5)=0.5$', fontsize=10)
    ax = axs[1]
    x = np.linspace(0, 5, 500)
    ax.plot(x, np.exp(-x), color=BLUE)
    ax.fill_between(x, np.exp(-x), where=x >= 1, color=RED, alpha=.3)
    ax.text(1.6, 0.3, r'area $=\int_1^\infty e^{-x}dx=e^{-1}\approx0.368$', fontsize=9.5)
    ax.set_title(r'exponential $e^{-x}$: $P(X>1)=0.368$', fontsize=10)
    ax = axs[2]
    x = np.linspace(-0.05, 0.15, 1001)
    p = np.where((x >= 0) & (x <= 0.1), 10, 0)
    ax.plot(x, p, color=BLUE)
    ax.fill_between(x, p, color=BLUE, alpha=.2)
    ax.text(0.05, 5, 'height 10 (> 1!)\nbut area\n$0.1\\times10=1$', ha='center', fontsize=10)
    ax.set_ylim(0, 12)
    ax.set_title(r'uniform on $[0,0.1]$: heights are not probabilities', fontsize=10)
    for a in axs:
        a.set_xlabel('$x$')
    axs[0].set_ylabel('$p(x)$')
    save(fig, 'p0_pdfs')


def fulcrum(ax, x, y0, w, h):
    ax.add_patch(Polygon([[x, y0], [x - w, y0 - h], [x + w, y0 - h]], closed=True, fc=RED, ec=RED, clip_on=False))


def p0_expectation():
    fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.2))
    ax = axs[0]
    ax.bar(range(1, 7), [1 / 6] * 6, width=.6, color=BLUE, alpha=.7)
    fulcrum(ax, 3.5, 0, 0.25, 0.035)
    ax.text(3.5, 0.215, r'balance point $\mathbb{E}[X]=3.5$', ha='center', color=RED, fontsize=10)
    ax.set_ylim(-0.04, 0.25)
    ax.set_title('a die: each face has probability $\\frac{1}{6}$', fontsize=10)
    ax.set_xlabel('$x$')
    ax = axs[1]
    x = np.linspace(0, 5, 500)
    ax.plot(x, np.exp(-x), color=BLUE)
    ax.fill_between(x, np.exp(-x), color=BLUE, alpha=.2)
    fulcrum(ax, 1, 0, 0.18, 0.13)
    ax.text(1.15, 0.45, r'mean $\mathbb{E}[X]=1$: balance point', color=RED, fontsize=9.5)
    ax.text(0.08, 0.93, 'most likely value is 0', fontsize=9.5, color=INK)
    ax.set_ylim(-0.15, 1.1)
    ax.set_title(r'$p(x)=e^{-x}$: mean $\neq$ most likely value', fontsize=10)
    ax.set_xlabel('$x$')
    ax = axs[2]
    x = np.linspace(-6, 6, 800)
    for s, col in [(0.6, BLUE), (2, ORANGE)]:
        ax.plot(x, stats.norm.pdf(x, 0, s), color=col, label=rf'$\sigma={s}$ ($\sigma^2={s * s:.2g}$)')
        y = stats.norm.pdf(s, 0, s)
        arrow(ax, -s, y, s, y, color=col, style='<->', lw=1.2, ms=9)
    ax.legend(fontsize=9)
    ax.set_title('same mean 0, different variance (spread)', fontsize=10)
    ax.set_xlabel('$x$')
    save(fig, 'p0_expectation')


def p0_gauss():
    x = np.linspace(-4, 4, 1000)
    p = stats.norm.pdf(x)
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.5))
    ax = axs[0]
    ax.plot(x, p, color=INK)
    for k, al in [(3, .12), (2, .2), (1, .35)]:
        ax.fill_between(x, p, where=np.abs(x) <= k, color=BLUE, alpha=al)
    for k, lab in [(1, '68.3 %'), (2, '95.4 %'), (3, '99.7 %')]:
        y = -0.045 * k
        arrow(ax, -k, y, k, y, style='<->', lw=1.1, ms=8)
        ax.text(0, y + 0.006, lab, ha='center', va='bottom', fontsize=9)
    ax.set_ylim(-0.16, 0.45)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3],
                  [r'$\mu-3\sigma$', r'$-2\sigma$', r'$-\sigma$', r'$\mu$', r'$+\sigma$', r'$+2\sigma$', r'$\mu+3\sigma$'])
    ax.set_title(r'$\mathcal{N}(\mu,\sigma^2)$: how much area within $\pm1,2,3\,\sigma$', fontsize=10)
    ax = axs[1]
    ax.plot(x, p, color=INK)
    ax.fill_between(x, p, where=x >= 1, color=RED, alpha=.4)
    ax.fill_between(x, p, where=x <= -1, color=ORANGE, alpha=.3)
    ax.annotate(r'$Q(1)=0.1587$', xy=(1.5, 0.05), xytext=(1.6, 0.25), fontsize=10, color=RED,
                arrowprops=dict(arrowstyle='->', color=RED))
    ax.annotate('same area by symmetry,\nso $Q(-1)=1-Q(1)$', xy=(-1.5, 0.05), xytext=(-4, 0.25), fontsize=9,
                color=ORANGE, arrowprops=dict(arrowstyle='->', color=ORANGE))
    ax.set_title(r'$Q(x)$ = area of the right tail beyond $x$ (here $x=1$)', fontsize=10)
    ax.set_xlabel(r'$z$ (standardised: $z=\frac{x-\mu}{\sigma}$)')
    save(fig, 'p0_gauss')


def p0_likelihood():
    th_vals, cols = [1, 3, 5], [ORANGE, GREEN, PURPLE]
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    ax = axs[0]
    y = np.linspace(-1.5, 8.5, 800)
    for th, c in zip(th_vals, cols):
        ax.plot(y, stats.norm.pdf(y, th), color=c, lw=1.6, label=rf'$\theta={th}$')
        ax.plot([3], [stats.norm.pdf(3, th)], 'o', color=c, ms=8)
    ax.axvline(3, color=INK, ls='--', lw=1.2)
    ax.text(3.1, 0.44, 'measured $y=3$', fontsize=9.5)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel('$y$ (possible data)')
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title(r'PDF: fix $\theta$, read a curve over the data $y$', fontsize=10)
    ax = axs[1]
    th = np.linspace(-1.5, 8.5, 800)
    ax.plot(th, stats.norm.pdf(3, th), color=INK)
    for t_, c in zip(th_vals, cols):
        ax.plot([t_], [stats.norm.pdf(3, t_)], 'o', color=c, ms=8)
    ax.axvline(3, color=RED, ls=':', lw=1.2)
    ax.text(3.15, 0.44, r'best: $\hat\theta=3$', color=RED, fontsize=9.5)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel(r'$\theta$ (possible parameter)')
    ax.set_title(r'likelihood: fix $y=3$, read a curve over $\theta$', fontsize=10)
    save(fig, 'p0_likelihood')


def p0_autocorr():
    rng = np.random.default_rng(3)
    N, a = 4000, 0.9
    x = lfilter([1], [1, -a], rng.standard_normal(N)) * math.sqrt(1 - a * a)
    fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.1), gridspec_kw=dict(width_ratios=[1.7, 1, 1, 1.3]))
    ax = axs[0]
    ax.plot(np.arange(120), x[:120], color=BLUE, lw=1.3)
    ax.set_title('one recording $x[n]$', fontsize=10)
    ax.set_xlabel('$n$')
    for ax, l, col in [(axs[1], 1, GREEN), (axs[2], 20, ORANGE)]:
        ax.plot(x[:-l][:1500], x[l:][:1500], '.', color=col, ms=2, alpha=.5, rasterized=True)
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-3.5, 3.5)
        ax.set_aspect('equal')
        ax.set_xlabel(f'$x[n-{l}]$')
        ax.set_ylabel('$x[n]$')
        ax.set_title(('tilted: related' if l == 1 else 'round: unrelated') + f' ($l={l}$)', fontsize=10)
    ax = axs[3]
    lags = np.arange(0, 31)
    stems(ax, lags, a ** lags, color=GREY, ms=3, lw=1)
    stems(ax, [1], [a], color=GREEN, ms=7)
    stems(ax, [20], [a ** 20], color=ORANGE, ms=7)
    ax.set_xlabel('lag $l$')
    ax.set_title('$r[l]$: how tilted the cloud is', fontsize=10)
    save(fig, 'p0_autocorr')


def p0_r_psd():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.0))
    ax = axs[0]
    lags = np.arange(-3, 4)
    r = np.array([0, 0, 0.5, 1, 0.5, 0, 0])
    stems(ax, lags, r, color=BLUE, ms=7)
    for l_, v in zip(lags, r):
        if v:
            ax.text(l_, v + 0.06, f'{v:g}', ha='center', fontsize=9.5)
    ax.set_ylim(-0.05, 1.25)
    ax.set_xlabel('lag $l$')
    ax.set_title('autocorrelation $r[l]$ (time side)', fontsize=10.5)
    ax = axs[1]
    th = np.linspace(-np.pi, np.pi, 600)
    ax.plot(th, 1 + np.cos(th), color=RED)
    ax.plot([0], [2], 'o', color=RED)
    ax.text(0.1, 2.02, r'$P(0)=2=0.5+1+0.5$', fontsize=9.5)
    ax.set_ylim(0, 2.4)
    full_pi(ax)
    ax.set_title(r'PSD $P(\theta)=1+\cos\theta$ (frequency side)', fontsize=10.5)
    save(fig, 'p0_r_psd')


# ================================================================== Part 3.1
def p3_energy_power():
    fig, axs = plt.subplots(2, 2, figsize=(10.6, 5.2), sharex='col')
    t1 = np.linspace(-1, 5, 1000)
    x1 = np.where(t1 >= 0, np.exp(-t1), 0)
    axs[0, 0].plot(t1, x1, color=BLUE)
    axs[0, 0].set_title(r'energy signal $x(t)=e^{-t}u(t)$: dies out', fontsize=10.5)
    axs[1, 0].plot(t1, x1 ** 2, color=BLUE)
    axs[1, 0].fill_between(t1, x1 ** 2, color=BLUE, alpha=.3)
    axs[1, 0].text(1.0, 0.5, r'total area $=\int_0^\infty e^{-2t}dt=\frac{1}{2}$' + '\n→ finite energy, $P=0$', fontsize=10)
    t2 = np.linspace(0, 10, 2000)
    x2 = np.sin(np.pi * t2)
    axs[0, 1].plot(t2, x2, color=RED)
    axs[0, 1].set_title(r'power signal $x(t)=A\sin(\omega t)$: goes on forever', fontsize=10.5)
    axs[1, 1].plot(t2, x2 ** 2, color=RED)
    axs[1, 1].fill_between(t2, x2 ** 2, color=RED, alpha=.2)
    axs[1, 1].axhline(0.5, color=INK, ls='--', lw=1.3)
    axs[1, 1].text(0.1, 1.08, r'average height $\frac{A^2}{2}$ (dashed) → $P=\frac{A^2}{2}$', fontsize=9.5)
    axs[1, 1].text(5.2, 0.62, 'area keeps growing\n→ $E=\\infty$', fontsize=9.5, ha='center',
                   bbox=dict(fc='white', ec='none', alpha=.85))
    axs[1, 1].text(10.05, 0.25, '…', fontsize=16)
    axs[0, 1].text(10.05, 0, '…', fontsize=16)
    axs[1, 1].set_ylim(0, 1.3)
    axs[1, 0].set_ylim(0, 1.15)
    axs[0, 0].set_ylabel('$x(t)$')
    axs[1, 0].set_ylabel('$x^2(t)$')
    for a in axs[1]:
        a.set_xlabel('$t$')
    for a in axs.flat:
        a.axhline(0, color=GREY, lw=.7)
    save(fig, 'p3_energy_power')


def p3_examples():
    fig, axs = plt.subplots(2, 3, figsize=(11.4, 5.4))
    t = np.linspace(-6, 6, 2000)
    E, P = BLUE, RED
    cases = [
        ('A', r'$A\sin(\omega t)$', np.sin(2 * t), P, r'power: $P=\frac{A^2}{2}$, $E=\infty$'),
        ('C', r'$e^{-t}u(t)$', np.where(t >= 0, np.exp(-t), 0), E, r'energy: $E=\frac{1}{2}$, $P=0$'),
        ('D', r'$\cos(t)\,u(t)$', np.where(t >= 0, np.cos(t), 0), P, r'power: $P=\frac{1}{4}$, $E=\infty$'),
        ('E', r'$5$ on $[-2,2]$', np.where(np.abs(t) <= 2, 5, 0), E, r'energy: $E=100$, $P=0$'),
        ('F', r'$5e^{-2|t|}$', 5 * np.exp(-2 * np.abs(t)), E, r'energy: $E=12.5$, $P=0$'),
    ]
    order = [axs[0, 0], axs[0, 2], axs[1, 0], axs[1, 1], axs[1, 2]]
    for ax, (k, name, y, col, res) in zip(order, cases):
        ax.plot(t, y, color=col)
        ax.set_title(f'{k}: {name}\n{res}', fontsize=10, color=col)
    ax = axs[0, 1]
    n = np.arange(-3, 7)
    stems(ax, n, np.where(n >= 0, np.exp(-n.astype(float)), 0), color=E, ms=5)
    ax.set_title('B: $e^{-n}$ for $n\\geq0$\n' + r'energy: $E=\frac{1}{1-e^{-2}}\approx1.1565$, $P=0$', fontsize=10,
                 color=E)
    for a in axs.flat:
        a.axhline(0, color=GREY, lw=.7)
        a.tick_params(labelsize=8.5)
    save(fig, 'p3_examples')


def p3_cos_u():
    t = np.linspace(-32, 32, 6000)
    x2 = np.where(t >= 0, np.cos(t) ** 2, 0)
    T = 50
    fig, ax = plt.subplots(figsize=(9.6, 3.2))
    ax.axvspan(-T / 2, 0, color=GREY, alpha=.15)
    ax.axvspan(0, T / 2, color=RED, alpha=.07)
    ax.plot(t, x2, color=RED, lw=1.2)
    ax.plot([0, T / 2], [0.5, 0.5], color=INK, ls='--', lw=1.3)
    ax.text(-T / 4, 0.55, 'left half: signal is off\ncontributes 0', ha='center', fontsize=10)
    ax.text(T / 4, 1.08, r'right half: average of $\cos^2$ is $\frac{1}{2}$', ha='center', fontsize=10)
    arrow(ax, -T / 2, -0.2, T / 2, -0.2, style='<->', lw=1.2, ms=10)
    ax.text(0, -0.17, r'window $[-\frac{T}{2},\frac{T}{2}]$ of length $T$', ha='center', va='bottom', fontsize=9.5,
            bbox=dict(fc='white', ec='none'))
    ax.set_ylim(-0.3, 1.3)
    ax.set_xlim(-32, 32)
    ax.set_xlabel('$t$')
    ax.set_ylabel(r'$x^2(t)=\cos^2(t)\,u(t)$')
    ax.set_title(r'$P=\frac{1}{T}\left(\frac{T}{2}\cdot0+\frac{T}{2}\cdot\frac{1}{2}\right)=\frac{1}{4}$: on only half the time',
                 fontsize=10.5)
    save(fig, 'p3_cos_u')


def p3_window_time():
    n = np.arange(-12, 46)
    x = np.cos(0.45 * n)
    N = 32
    inside = (n >= 0) & (n < N)
    hann = np.hanning(N + 2)[1:-1]
    w_r = inside.astype(float)
    w_h = np.where(inside, hann[np.clip(n, 0, N - 1)], 0)
    fig, axs = plt.subplots(2, 3, figsize=(11.6, 4.4), sharex=True, sharey=True)
    for row, (w, col, name) in enumerate([(w_r, BLUE, 'rectangular'), (w_h, RED, 'Hann')]):
        stems(axs[row, 0], n, x, color=GREY, ms=2.5, lw=1)
        axs[row, 1].plot(n, w, color=col, drawstyle='steps-mid' if row == 0 else 'default', lw=2)
        stems(axs[row, 2], n, x * w, color=col, ms=2.5, lw=1)
        axs[row, 0].set_ylabel(name, fontsize=10.5, color=col)
    axs[0, 0].set_title('true signal $x[n]$ (never stops)', fontsize=10)
    axs[0, 1].set_title('× window $w[n]$ (1 = "recorded")', fontsize=10)
    axs[0, 2].set_title(r'= what you get: $x[n]\,w[n]$', fontsize=10)
    for a in axs[1]:
        a.set_xlabel('$n$')
    for a in axs.flat:
        a.axhline(0, color=GREY, lw=.6)
    save(fig, 'p3_window_time')


def rect_spec(N, th):
    th = np.where(np.abs(th) < 1e-9, 1e-9, th)
    return np.abs(np.sin(N * th / 2) / (N * np.sin(th / 2)))


def p3_N_lobes():
    th = np.linspace(0, np.pi, 6000)
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    for N, col in [(8, ORANGE), (16, BLUE), (32, GREEN)]:
        W = rect_spec(N, th)
        axs[0].plot(th, W, color=col, label=f'$N={N}$')
        axs[1].plot(th, 20 * np.log10(W + 1e-9), color=col, label=f'$N={N}$')
        axs[0].plot([2 * np.pi / N], [0], 'v', color=col, ms=8)
    axs[0].text(0.85, 0.75, r'first zero at $\theta=\frac{2\pi}{N}$ (triangles)', fontsize=9.5)
    axs[0].set_title('longer $N$ → narrower main lobe (better resolution)', fontsize=10)
    axs[1].axhline(-13.3, color=RED, ls='--', lw=1.3)
    axs[1].text(1.2, -11, 'highest side lobe: −13 dB for EVERY $N$', color=RED, fontsize=9.5)
    axs[1].set_ylim(-50, 3)
    axs[1].set_ylabel('dB')
    axs[1].set_title('… but the side lobes stay just as high (same leakage)', fontsize=10)
    axs[0].legend(fontsize=9)
    for a in axs:
        half_pi(a)
    save(fig, 'p3_N_lobes')


def p3_resolution():
    t1, t2 = 1.0, 1.2
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.2), sharey=True)
    th = np.linspace(0, np.pi, 4000)

    def ftd(N):
        n = np.arange(N)
        x = np.cos(t1 * n) + np.cos(t2 * n)
        return np.abs(np.exp(-1j * np.outer(th, n)) @ x)

    X16 = ftd(16)
    n = np.arange(16)
    x16 = np.cos(t1 * n) + np.cos(t2 * n)
    k = np.arange(9)
    D16 = np.abs(np.fft.fft(x16))[:9]
    m = X16.max()
    axs[0].plot(2 * np.pi * k / 16, D16 / m, 's-', color=BLUE, ms=6, lw=1)
    axs[0].set_title('$N=16$, plain DFT: one blob', fontsize=10)
    axs[1].plot(th, X16 / m, color=BLUE, lw=1.5)
    L = 128
    kk = np.arange(L // 2 + 1)
    axs[1].plot(2 * np.pi * kk / L, np.abs(np.fft.fft(x16, L))[:L // 2 + 1] / m, 'o', color=RED, ms=2.5)
    axs[1].set_title('same 16 samples zero-padded: smoother,\nstill ONE blob', fontsize=10)
    X64 = ftd(64)
    axs[2].plot(th, X64 / X64.max(), color=GREEN, lw=1.5)
    axs[2].set_title('$N=64$ real samples: two peaks', fontsize=10)
    for a in axs:
        a.axvline(t1, color=GREY, ls=':', lw=1)
        a.axvline(t2, color=GREY, ls=':', lw=1)
        half_pi(a)
        a.set_ylim(0, 1.12)
    axs[0].text(t2 + 0.06, 1.02, 'true tones\n(dotted)', fontsize=8.5, color=GREY, va='top')
    save(fig, 'p3_resolution')


# ================================================================== Part 3.2
def p3_darts():
    rng = np.random.default_rng(7)
    cases = [('no bias, low variance', (0, 0), .13, GREEN), ('no bias, HIGH variance', (0, 0), .45, ORANGE),
             ('BIASED, low variance', (.5, .35), .1, ORANGE), ('biased AND high variance', (.45, .3), .45, RED)]
    fig, axs = plt.subplots(1, 4, figsize=(11.4, 3.2))
    for ax, (title, c, s, col) in zip(axs, cases):
        for r_, fc in [(1, '#f6f1e7'), (0.66, '#ece4d4'), (0.33, '#e0d5bf')]:
            ax.add_patch(Circle((0, 0), r_, fc=fc, ec=GREY, lw=.8))
        ax.plot([0], [0], '+', color=INK, ms=12, mew=2)
        d = rng.normal(c, s, (12, 2))
        ax.plot(d[:, 0], d[:, 1], 'x', color=BLUE, ms=6, mew=1.6)
        mu = d.mean(axis=0)
        ax.plot([mu[0]], [mu[1]], '*', color=RED, ms=13)
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.15, 1.15)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=10, color=col)
    fig.text(0.5, 0.0, 'centre (+) = the true PSD value · blue × = estimates from different recordings · '
                       'red ★ = their average', ha='center', fontsize=9.5)
    save(fig, 'p3_darts')


def p3_periodogram_N():
    rng = np.random.default_rng(11)
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.2), sharey=True)
    for ax, N in zip(axs, [64, 256, 1024]):
        x = rng.standard_normal(N)
        P = np.abs(np.fft.rfft(x)) ** 2 / N
        th = 2 * np.pi * np.arange(len(P)) / N
        ax.plot(th, P, color=BLUE, lw=.8, marker='.' if N == 64 else None, ms=4)
        ax.axhline(1, color=RED, ls='--', lw=1.6)
        ax.set_title(f'$N={N}$: {len(P)} bins, jumps just as big', fontsize=10)
        half_pi(ax)
        ax.set_ylim(0, 7)
    axs[0].set_ylabel(r'$\hat P(e^{j\theta})$')
    axs[0].text(0.1, 6.2, 'true PSD = 1 (red dashed)', color=RED, fontsize=9)
    save(fig, 'p3_periodogram_N')


def p3_rhat_bias():
    N = 20
    l = np.arange(0, N)
    r = 0.9 ** l
    tri = 1 - l / N
    fig, ax = plt.subplots(figsize=(8.4, 3.3))
    stems(ax, l - 0.15, r, color=GREY, ms=4, label=r'true $r[l]=0.9^{l}$')
    stems(ax, l + 0.15, tri * r, color=BLUE, ms=4, label=r'average of $\hat r[l]$ $=(1-\frac{l}{N})\,r[l]$')
    ax.plot(l, tri, ls='--', color=ORANGE, lw=1.5, label=r'the triangle $1-\frac{l}{N}$ (Bartlett window)')
    ax.annotate('lag 10: only half\nof the true value', xy=(10.15, 0.5 * 0.9 ** 10), xytext=(12.5, 0.4), fontsize=9,
                arrowprops=dict(arrowstyle='->', color=INK))
    ax.set_xlabel('lag $l$')
    ax.set_title(r'$N=20$: the $\frac{1}{N}$ estimate shrinks the long lags', fontsize=10.5)
    ax.legend(fontsize=9, loc='upper right')
    save(fig, 'p3_rhat_bias')


def bartlett_est(x, K, nfft=2048):
    M = len(x) // K
    return np.mean([pgram(x[k * M:(k + 1) * M], nfft) for k in range(K)], axis=0)


def welch_est(x, L, D, nfft=2048):
    w = np.hanning(L)
    U = np.sum(w ** 2) / L
    segs = [x[s:s + L] for s in range(0, len(x) - L + 1, D)]
    return np.mean([np.abs(np.fft.fft(w * s, nfft)[:nfft // 2 + 1]) ** 2 / (L * U) for s in segs], axis=0), len(segs)


def bt_est(x, M, nfft=2048):
    N = len(x)
    r = np.array([np.dot(x[l:], x[:N - l]) / N for l in range(M)])
    w = 0.5 * (1 + np.cos(np.pi * np.arange(M) / M))
    th = 2 * np.pi * np.arange(nfft // 2 + 1) / nfft
    return r[0] * w[0] + 2 * sum(r[l] * w[l] * np.cos(l * th) for l in range(1, M))


def p3_bartlett():
    x = ar2_data(1024, 5)
    th = 2 * np.pi * np.arange(1025) / 2048
    K = 8
    M = 1024 // K
    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    for k in range(K):
        ax.plot(th, db(pgram(x[k * M:(k + 1) * M])), color=GREY, lw=.6, alpha=.6,
                label='periodogram of one segment ($M=128$)' if k == 0 else None)
    ax.plot(th, db(bartlett_est(x, K)), color=BLUE, lw=2.2, label='average of the 8 (Bartlett)')
    ax.plot(th, db(ar2_true(th)), color=RED, ls='--', lw=1.6, label='true PSD')
    half_pi(ax)
    ax.set_ylim(-25, 30)
    ax.set_ylabel('dB')
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title('cut 1024 samples into 8 pieces, average the 8 noisy periodograms', fontsize=10.5)
    save(fig, 'p3_bartlett')


def p3_methods():
    x = ar2_data(512, 21)
    th = 2 * np.pi * np.arange(1025) / 2048
    true = db(ar2_true(th))
    wel, K = welch_est(x, 128, 64)
    est = [('raw periodogram ($N=512$): right shape, huge jumps', pgram(x), GREY),
           ('Bartlett ($K=8$, $M=64$): calm, peak lower and wider', bartlett_est(x, 8), BLUE),
           (f'Welch ($L=128$, 50 %, Hann, $K={K}$): calm, sharper', wel, GREEN),
           ('Blackman–Tukey (lags $<16$): calmest, most smeared', bt_est(x, 16), PURPLE)]
    fig, axs = plt.subplots(2, 2, figsize=(11, 5.6), sharex=True, sharey=True)
    for ax, (title, P, col) in zip(axs.flat, est):
        ax.plot(th, db(P), color=col, lw=1.1 if col == GREY else 2)
        ax.plot(th, true, color=RED, ls='--', lw=1.4)
        ax.set_title(title, fontsize=10)
        ax.set_ylim(-25, 30)
    for a in axs[1]:
        half_pi(a)
    for a in axs[:, 0]:
        a.set_ylabel('dB')
    axs[0, 0].text(2.1, 22, 'red dashed = true PSD', color=RED, fontsize=9)
    save(fig, 'p3_methods')


def p3_bt():
    N = 256
    x = ar2_data(N, 9)
    r = np.array([np.dot(x[l:], x[:N - l]) / N for l in range(N)])
    M = 20
    w = np.where(np.arange(N) < M, 0.5 * (1 + np.cos(np.pi * np.arange(N) / M)), 0)
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.4))
    ax = axs[0]
    L = 90
    stems(ax, np.arange(L), r[:L], color=GREY, ms=2.5, lw=1, label=r'$\hat r[l]$: all lags (long ones are noise)')
    ax.plot(np.arange(L), w[:L] * r[0], color=ORANGE, lw=1.6, ls='--', label='lag window $w[l]$ (scaled)')
    stems(ax, np.arange(M), (w * r)[:M], color=BLUE, ms=3, lw=1.4, label=r'kept: $w[l]\,\hat r[l]$')
    ax.set_xlabel('lag $l$')
    ax.legend(fontsize=8.5)
    ax.set_title('keep the short lags, throw away the noisy long ones', fontsize=10)
    ax = axs[1]
    th = 2 * np.pi * np.arange(1025) / 2048
    ax.plot(th, db(pgram(x)), color=GREY, lw=.9, label='all lags = periodogram')
    ax.plot(th, db(bt_est(x, M)), color=BLUE, lw=2, label=f'Blackman–Tukey ($M={M}$)')
    ax.plot(th, db(ar2_true(th)), color=RED, ls='--', lw=1.4, label='true PSD')
    half_pi(ax)
    ax.set_ylim(-25, 30)
    ax.set_ylabel('dB')
    ax.legend(fontsize=8.5, loc='upper right')
    ax.set_title('fewer lags: much calmer, but blurrier', fontsize=10)
    save(fig, 'p3_bt')


# ================================================================== Part 3.3
def p3_memory():
    rng = np.random.default_rng(4)
    i = rng.standard_normal(400)
    th = np.linspace(0, np.pi, 600)
    models = [
        ('white noise\n$x[n]=i[n]$', [1], [1], GREY),
        ('MA(1)\n$x[n]=i[n]+0.9\\,i[n-1]$', [1, 0.9], [1], GREEN),
        ('AR(1)\n$x[n]=i[n]+0.9\\,x[n-1]$', [1], [1, -0.9], BLUE),
        ('AR(1)\n$x[n]=i[n]-0.9\\,x[n-1]$', [1], [1, 0.9], RED),
    ]
    fig, axs = plt.subplots(4, 3, figsize=(11.6, 8.2), gridspec_kw=dict(width_ratios=[1.7, 1, 1]))
    for row, (name, b, a, col) in enumerate(models):
        x = lfilter(b, a, i)[300:380]
        axs[row, 0].plot(np.arange(80), x, color=col, lw=1.2)
        axs[row, 0].set_ylabel(name, fontsize=9.5, color=col)
        h = lfilter(b, a, np.r_[1, np.zeros(200)])
        lags = np.arange(11)
        r = np.array([np.dot(h[l:], h[:len(h) - l]) for l in lags])
        stems(axs[row, 1], lags, r / r[0], color=col, ms=4)
        axs[row, 1].set_ylim(-1.1, 1.15)
        H = np.polyval(b[::-1], np.exp(-1j * th)) / np.polyval(a[::-1], np.exp(-1j * th))
        axs[row, 2].semilogy(th, np.abs(H) ** 2, color=col)
        axs[row, 2].set_ylim(0.004, 300)
        half_pi(axs[row, 2], label=row == 3)
        if row < 3:
            axs[row, 2].set_xticklabels([])
    axs[0, 0].set_title('one realisation (the SAME noise $i[n]$ in every row)', fontsize=10)
    axs[0, 1].set_title('autocorrelation $r[l]/r[0]$', fontsize=10)
    axs[0, 2].set_title(r'PSD $P(e^{j\theta})$ (log scale)', fontsize=10)
    axs[3, 0].set_xlabel('$n$')
    axs[3, 1].set_xlabel('lag $l$')
    save(fig, 'p3_memory')


def p3_impulse():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.1), sharey=True)
    n = np.arange(13)
    h_ma = np.zeros(13)
    h_ma[:3] = [1, 0.5, -0.4]
    stems(axs[0], n, h_ma, color=GREEN)
    axs[0].set_title(r'MA(2), $b=[1,\ 0.5,\ -0.4]$: the kick is gone after 2 steps', fontsize=10)
    stems(axs[1], n, 0.8 ** n, color=BLUE)
    axs[1].set_title(r'AR(1), $x[n]=i[n]+0.8\,x[n-1]$: fades as $0.8^n$, never exactly 0', fontsize=10)
    for a in axs:
        a.set_xlabel('$n$ (steps after a single kick $i[0]=1$)')
        a.axhline(0, color=GREY, lw=.7)
    axs[0].set_ylabel('response $h[n]$')
    save(fig, 'p3_impulse')


def p3_shaping():
    th = np.linspace(0, np.pi, 600)
    s2 = 2
    rows = [('AR(1), $a_1=-0.8$', 1 / np.abs(1 - 0.8 * np.exp(-1j * th)) ** 2, BLUE, r'$\frac{1}{|1-0.8e^{-j\theta}|^2}$'),
            ('MA(1), $b_1=-0.9$', np.abs(1 - 0.9 * np.exp(-1j * th)) ** 2, GREEN, r'$|1-0.9e^{-j\theta}|^2$')]
    fig, axs = plt.subplots(2, 3, figsize=(11, 5))
    for r, (name, H2, col, lab) in enumerate(rows):
        axs[r, 0].plot(th, np.full_like(th, s2), color=GREY, lw=2)
        axs[r, 0].set_ylim(0, 3)
        axs[r, 1].plot(th, H2, color=col, lw=2)
        axs[r, 2].plot(th, s2 * H2, color=col, lw=2)
        axs[r, 1].set_title(f'× {name}: ' + r'$|H|^2=$' + lab, fontsize=10)
        axs[r, 2].set_title(r'= output PSD $\sigma_i^2|H|^2$', fontsize=10)
        axs[r, 0].set_title(r'white noise in: flat $\sigma_i^2=2$', fontsize=10)
        for c in range(3):
            half_pi(axs[r, c], label=r == 1)
    save(fig, 'p3_shaping')


def p3_poles_zeros():
    th = np.linspace(0, np.pi, 800)
    fig, axs = plt.subplots(2, 2, figsize=(10.4, 6.6), gridspec_kw=dict(width_ratios=[1, 1.6]))
    circ = np.linspace(0, 2 * np.pi, 300)
    cases = [(0, 'pole', 0.9, 1.2, BLUE), (1, 'zero', 0.95, 2.2, GREEN)]
    for r, kind, rad, ang, col in cases:
        ax = axs[r, 0]
        ax.plot(np.cos(circ), np.sin(circ), color=GREY, lw=1.2)
        ax.axhline(0, color=GREY, lw=.6)
        ax.axvline(0, color=GREY, lw=.6)
        p = rad * np.exp(1j * ang)
        mk = 'x' if kind == 'pole' else 'o'
        for q in (p, np.conj(p)):
            ax.plot([q.real], [q.imag], mk, color=col, ms=11, mew=2.5, mfc='none' if kind == 'zero' else col)
        e = np.exp(1j * ang)
        ax.plot([e.real], [e.imag], 'o', color=RED, ms=6)
        ax.plot([e.real, p.real], [e.imag, p.imag], color=RED, lw=1.5)
        ax.text(e.real * 1.12, e.imag * 1.12 + 0.05, r'$e^{j\theta}$ at $\theta=%.1f$' % ang, color=RED, fontsize=9,
                ha='center')
        ax.set_aspect('equal')
        ax.set_xlim(-1.35, 1.35)
        ax.set_ylim(-1.35, 1.45)
        ax.set_title(f'{kind}s at radius {rad}, angle $\\pm{ang}$', fontsize=10)
        ax.set_xlabel('Re $z$')
        ax.set_ylabel('Im $z$')
        a = [1, -2 * rad * math.cos(ang), rad ** 2]
        A2 = np.abs(a[0] + a[1] * np.exp(-1j * th) + a[2] * np.exp(-2j * th)) ** 2
        ax = axs[r, 1]
        ax.semilogy(th, 1 / A2 if kind == 'pole' else A2, color=col, lw=2)
        ax.axvline(ang, color=RED, ls=':', lw=1.2)
        half_pi(ax)
        ax.set_title('AR: peak where the circle passes close to a pole' if kind == 'pole'
                     else 'MA: dip where the circle passes close to a zero', fontsize=10)
        ax.set_ylabel('PSD (log scale)')
    save(fig, 'p3_poles_zeros')


def p3_ar1_tail():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.2), sharey=True)
    l = np.arange(11)
    r0 = 1 / (1 - 0.64)
    for ax, s, col, title in [(axs[0], 1, BLUE, r'$x[n]=i[n]+0.8\,x[n-1]$ ($a=-0.8$): smooth signal'),
                              (axs[1], -1, RED, r'$x[n]=i[n]-0.8\,x[n-1]$ ($a=+0.8$): zig-zag signal')]:
        r = r0 * (s * 0.8) ** l
        stems(ax, l, r, color=col)
        for k in range(3):
            ax.text(l[k] + 0.25, r[k], f'{r[k]:.2f}', fontsize=9, va='center')
        ax.axhline(0, color=GREY, lw=.7)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel('lag $l$')
    axs[0].set_ylabel(r'$r[l]=\frac{\sigma_i^2}{1-a^2}(-a)^{|l|}$')
    save(fig, 'p3_ar1_tail')


# ================================================================== Part 3.4
def p3_chain_three():
    r = [1, 0.4, 0.1]
    th = np.linspace(-np.pi, np.pi, 1001)
    a1, s1 = yw(r, 1)
    a2, s2 = yw(r, 2)
    fig, ax = plt.subplots(figsize=(8.8, 3.8))
    curves = [('correlogram: $1+0.8\\cos\\theta+0.2\\cos2\\theta$', r[0] + 2 * r[1] * np.cos(th) + 2 * r[2] * np.cos(2 * th), GREY, '-'),
              ('MA(1), $b=0.5$, $\\sigma_i^2=0.8$: $1+0.8\\cos\\theta$', 1 + 0.8 * np.cos(th), GREEN, '-'),
              (f'AR(1), $a_1={a1[0]:.2f}$, $\\sigma_i^2={s1:.2f}$', ar_psd(a1, s1, th), BLUE, '--'),
              (f'AR(2), $a=[{a2[0]:.3f},\\ {a2[1]:.3f}]$, $\\sigma_i^2={s2:.3f}$', ar_psd(a2, s2, th), RED, ':')]
    for lab, P, col, ls in curves:
        ax.plot(th, P, color=col, ls=ls, lw=2, label=lab)
    full_pi(ax)
    ax.set_ylim(0, 2.6)
    ax.legend(fontsize=8.8, loc='upper left', bbox_to_anchor=(1.01, 1))
    ax.set_title(r'given $r[0]=1,\ r[1]=0.4,\ r[2]=0.1$: four guesses at the same PSD', fontsize=10.5)
    save(fig, 'p3_chain_three')


def p3_corr_negative():
    th = np.linspace(-np.pi, np.pi, 1001)
    r = [1, 0.7, 0.49]
    P = r[0] + 2 * r[1] * np.cos(th) + 2 * r[2] * np.cos(2 * th)
    a2, s2 = yw(r, 2)
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    ax.plot(th, P, color=GREY, lw=2, label=r'correlogram $1+1.4\cos\theta+0.98\cos2\theta$')
    ax.fill_between(th, P, 0, where=P < 0, color=RED, alpha=.5, interpolate=True)
    ax.plot(th, ar_psd(a2, s2, th), color=BLUE, lw=2, ls='--',
            label=r'AR(2) fit of the same $r$ (here the true PSD, always $>0$)')
    ax.axhline(0, color=INK, lw=1)
    ax.annotate(r'dips to $-0.23$: impossible for a real PSD', xy=(1.94, -0.2), xytext=(0.3, -1.1), fontsize=9.5,
                color=RED, arrowprops=dict(arrowstyle='->', color=RED))
    full_pi(ax)
    ax.set_ylim(-1.4, 7.9)
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title('chopping $r[l]$ after lag 2 can make the correlogram dip below zero', fontsize=10.5)
    save(fig, 'p3_corr_negative')


def p3_ar_notch():
    th = np.linspace(0, np.pi, 1000)
    r = [1.81, -0.9] + [0] * 40
    true = ma_psd([-0.9], 1, th)
    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    ax.plot(th, db(true), color=INK, lw=2.4, label=r'true: MA(1), $b=-0.9$ (deep notch at $\theta=0$)')
    for p, col in [(1, ORANGE), (4, BLUE), (16, GREEN)]:
        a, s = yw(r, p)
        ax.plot(th, db(ar_psd(a, s, th)), color=col, lw=1.5, label=f'AR({p}) fitted by Yule–Walker')
    half_pi(ax)
    ax.set_ylabel('dB')
    ax.set_ylim(-22, 8)
    ax.legend(fontsize=9, loc='lower right')
    ax.set_title('an AR model can only make a notch with many coefficients', fontsize=10.5)
    save(fig, 'p3_ar_notch')


# ================================================================== Part 1
def p1_bayes_area():
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.9), gridspec_kw=dict(width_ratios=[1.45, 1]))
    ax = axs[0]
    widths, defects = [.40, .35, .25], [.02, .04, .05]
    names, cols = ['$M_1$', '$M_2$', '$M_3$'], [BLUE, GREEN, PURPLE]
    x0 = 0
    for w, d, nm, c in zip(widths, defects, names, cols):
        ax.add_patch(Rectangle((x0, 0), w, 1, fc=c, alpha=.16, ec=INK, lw=1))
        ax.add_patch(Rectangle((x0, 0), w, d * 10, fc=RED, alpha=.8, ec='none'))
        ax.text(x0 + w / 2, 0.88, f'{nm}\n{w * 10000:.0f} chips', ha='center', va='center', fontsize=10)
        ax.text(x0 + w / 2, d * 10 + 0.05, f'{d:.0%} defective\n= {w * d * 10000:.0f} chips', ha='center',
                fontsize=9, color=RED)
        x0 += w
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, .4, .75, 1])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title('all 10 000 chips (width = share of each machine; red heights ×10 so you can see them)',
                 fontsize=9.5)
    ax = axs[1]
    x0 = 0
    for k, (cnt, nm, c) in enumerate(zip([80, 140, 125], names, cols)):
        ax.add_patch(Rectangle((x0, 0), cnt, 1, fc=c, alpha=.55, ec='white', lw=2))
        ax.text(x0 + cnt / 2, 0.5, f'{nm}\n{cnt}/345\n$={cnt / 345:.3f}$', ha='center', va='center', fontsize=10)
        x0 += cnt
    ax.set_xlim(0, 345)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_xticks([0, 80, 220, 345])
    ax.set_title('zoom into the 345 defective chips only:\n$P(M_k\\mid$defective$)$ = share of this bar', fontsize=10)
    save(fig, 'p1_bayes_area')


def p1_indep_disjoint():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4))
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 1, 1, fc=PAPER, ec=INK))
    ax.add_patch(Rectangle((0.08, 0.15), 0.35, 0.6, fc=BLUE, alpha=.45))
    ax.add_patch(Rectangle((0.55, 0.3), 0.37, 0.5, fc=ORANGE, alpha=.45))
    ax.text(0.255, 0.45, '$A$', fontsize=16, ha='center')
    ax.text(0.735, 0.55, '$B$', fontsize=16, ha='center')
    ax.set_title('disjoint: they never happen together\n$P(A\\cap B)=0$ (knowing $B$ rules $A$ out)', fontsize=10)
    ax = axs[1]
    ax.add_patch(Rectangle((0, 0), 1, 1, fc=PAPER, ec=INK))
    ax.add_patch(Rectangle((0, 0), 0.4, 1, fc=BLUE, alpha=.35))
    ax.add_patch(Rectangle((0, 0), 1, 0.3, fc=ORANGE, alpha=.35))
    ax.text(0.2, 0.65, '$A$\n$P(A)=0.4$', fontsize=12, ha='center')
    ax.text(0.7, 0.13, '$B$: $P(B)=0.3$', fontsize=12, ha='center')
    ax.text(0.2, 0.13, '$A\\cap B$\n$0.4\\times0.3$', fontsize=10, ha='center', va='center')
    ax.set_title('independent: inside $B$, $A$ still takes 40 %\n$P(A\\cap B)=P(A)P(B)=0.12$', fontsize=10)
    for a in axs:
        a.set_xlim(-0.02, 1.02)
        a.set_ylim(-0.02, 1.02)
        a.set_aspect('equal')
        a.axis('off')
    save(fig, 'p1_indep_disjoint')


def p1_pmf_cdf():
    fig, axs = plt.subplots(1, 4, figsize=(12, 2.9))
    k = np.arange(1, 7)
    stems(axs[0], k, np.full(6, 1 / 6), color=BLUE, ms=6)
    axs[0].set_ylim(0, 0.3)
    axs[0].set_title('die: PMF $P(X=x)$ (dots that sum to 1)', fontsize=9.5)
    xs = np.r_[0, k, 7]
    axs[1].step(xs, np.r_[0, k / 6, 1], where='post', color=BLUE)
    axs[1].set_title('die: CDF $P(X\\leq x)$ jumps at each face', fontsize=9.5)
    x = np.linspace(0, 5, 400)
    axs[2].plot(x, np.exp(-x), color=RED)
    axs[2].fill_between(x, np.exp(-x), color=RED, alpha=.2)
    axs[2].set_title('exponential: PDF (area = 1)', fontsize=9.5)
    axs[3].plot(x, 1 - np.exp(-x), color=RED)
    axs[3].set_title('exponential: CDF $1-e^{-x}$ (smooth, 0 → 1)', fontsize=9.5)
    for a in axs:
        a.set_xlabel('$x$')
    for a in axs[[1, 3]]:
        a.set_ylim(-0.03, 1.08)
    save(fig, 'p1_pmf_cdf')


def p1_joint_ops():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.5))
    ax = axs[0]
    ax.add_patch(Polygon([[0, 0], [1, 0], [1, 1]], fc=BLUE, alpha=.25, ec=BLUE))
    ax.text(0.68, 0.22, '$p=2$ here', fontsize=10)
    ax.plot([0.3, 1], [0.3, 0.3], color=ORANGE, lw=4)
    ax.text(0.02, 0.36, '$y=0.3$: $x$ runs\nfrom 0.3 to 1', fontsize=9.5, color=ORANGE)
    ax.plot([0, 1], [0, 1], color=GREY, ls=':', lw=1)
    ax.text(0.45, 0.62, '$y=x$', color=GREY, rotation=45, fontsize=9)
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1.05)
    ax.set_aspect('equal')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('region $0\\leq y\\leq x\\leq1$', fontsize=10)
    ax = axs[1]
    y = np.linspace(0, 1, 200)
    ax.plot(y, 2 * (1 - y), color=BLUE)
    ax.plot([0.3], [1.4], 'o', color=ORANGE, ms=8)
    ax.text(0.34, 1.45, r'$p_Y(0.3)=\int_{0.3}^{1}2\,dx=1.4$', fontsize=9.5)
    ax.set_xlabel('$y$')
    ax.set_title('marginal $p_Y(y)=2(1-y)$: add up each strip', fontsize=10)
    ax.set_ylim(0, 2.3)
    ax = axs[2]
    x = np.linspace(0, 1.1, 500)
    ax.plot(x, np.where((x >= 0.3) & (x <= 1), 1 / 0.7, 0), color=ORANGE)
    ax.fill_between(x, np.where((x >= 0.3) & (x <= 1), 1 / 0.7, 0), color=ORANGE, alpha=.25)
    ax.text(0.65, 0.7, 'area $0.7\\times\\frac{1}{0.7}=1$', ha='center', fontsize=9.5)
    ax.set_xlabel('$x$')
    ax.set_ylim(0, 2.3)
    ax.set_title('conditional $p(x\\mid y=0.3)=\\frac{2}{1.4}$: the strip,\nrescaled to area 1', fontsize=10)
    save(fig, 'p1_joint_ops')


def p1_cov():
    rng = np.random.default_rng(2)
    fig, axs = plt.subplots(1, 4, figsize=(12, 3.2))
    for ax, rho in zip(axs[:3], [-0.8, 0, 0.8]):
        d = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], 400)
        ax.plot(d[:, 0], d[:, 1], '.', color=BLUE if rho else GREY, ms=3, alpha=.6, rasterized=True)
        ax.set_title(rf'$\rho={rho:g}$: ' + {-0.8: 'big $X$ ↔ small $Y$', 0: 'no linear relation',
                                              0.8: 'big $X$ ↔ big $Y$'}[rho], fontsize=10)
    x = rng.uniform(-2, 2, 400)
    yv = x ** 2 + rng.normal(0, 0.25, 400) - 1.3
    axs[3].plot(x, yv, '.', color=RED, ms=3, alpha=.6, rasterized=True)
    axs[3].set_title(rf'$\rho\approx{np.corrcoef(x, yv)[0, 1]:.2f}$, but $Y$ depends on $X$!', fontsize=10, color=RED)
    for a in axs:
        a.set_xlim(-3, 3)
        a.set_ylim(-3, 3)
        a.set_aspect('equal')
        a.set_xlabel('$X$')
    axs[0].set_ylabel('$Y$')
    save(fig, 'p1_cov')


def p1_valid_r():
    fig, axs = plt.subplots(2, 4, figsize=(12, 4.8), gridspec_kw=dict(height_ratios=[1, 0.9]))
    lags = np.arange(-4, 5)
    th = np.linspace(-np.pi, np.pi, 600)
    cases = [
        ('valid', 0.7 ** np.abs(lags), GREEN),
        ('not symmetric ✗', np.array([0, 0, 0.1, 0.2, 1, 0.6, 0.3, 0.1, 0]), RED),
        ('$r[1]>r[0]$ ✗', np.array([0, 0, 0, 1.2, 1, 1.2, 0, 0, 0]), RED),
        ('looks fine, but PSD < 0 ✗', np.array([0, 0, 0, 0.9, 1, 0.9, 0, 0, 0]), RED),
    ]
    for c, (title, r, col) in enumerate(cases):
        stems(axs[0, c], lags, r, color=col, ms=5)
        axs[0, c].set_ylim(-0.1, 1.35)
        axs[0, c].set_title(title, fontsize=10, color=col)
        axs[0, c].set_xlabel('lag $l$')
        ax = axs[1, c]
        if c in (0, 3):
            P = sum(r[i] * np.cos(l_ * th) for i, l_ in enumerate(lags))
            ax.plot(th, P, color=col)
            ax.axhline(0, color=INK, lw=.8)
            ax.fill_between(th, P, 0, where=P < 0, color=RED, alpha=.4, interpolate=True)
            full_pi(ax)
            ax.set_title('PSD ≥ 0 everywhere ✓' if c == 0 else r'PSD $1+1.8\cos\theta$ goes negative', fontsize=9.5)
        else:
            ax.axis('off')
            ax.text(0.5, 0.5, 'rejected before even\ncomputing the PSD', ha='center', va='center', fontsize=10,
                    transform=ax.transAxes, color=RED)
    save(fig, 'p1_valid_r')


def p1_innovation():
    rng = np.random.default_rng(8)
    i = rng.standard_normal(260)
    x = lfilter([1], [1, -0.75], i)[60:]
    i = i[60:]
    th = np.linspace(0, np.pi, 300)
    fig = plt.figure(figsize=(11.2, 3.8))
    bg = fig.add_axes([0, 0, 1, 1])
    bg.axis('off')
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    a1 = fig.add_axes([0.04, 0.56, 0.27, 0.33])
    a1.plot(i[:80], color=GREY, lw=1)
    a1.set_title('white noise $i[n]$: no memory', fontsize=10)
    a2 = fig.add_axes([0.04, 0.12, 0.27, 0.28])
    a2.plot(th, np.ones_like(th), color=GREY, lw=2)
    a2.set_ylim(0, 2)
    half_pi(a2)
    a2.set_title(r'flat PSD $\sigma_i^2$', fontsize=10)
    a3 = fig.add_axes([0.69, 0.56, 0.28, 0.33])
    a3.plot(x[:80], color=BLUE, lw=1.2)
    a3.set_title('coloured signal $x[n]$: has memory', fontsize=10)
    a4 = fig.add_axes([0.69, 0.12, 0.28, 0.28])
    a4.plot(th, 1 / np.abs(1 - 0.75 * np.exp(-1j * th)) ** 2, color=BLUE, lw=2)
    half_pi(a4)
    a4.set_title(r'PSD $\sigma_i^2|L(e^{j\theta})|^2$', fontsize=10)
    bg.text(0.5, 0.66, '$L(z)$', fontsize=20, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.6', fc=PAPER, ec=INK))
    arrow(bg, 0.34, 0.66, 0.44, 0.66, lw=2)
    arrow(bg, 0.56, 0.66, 0.66, 0.66, lw=2)
    arrow(bg, 0.66, 0.36, 0.34, 0.36, color=GREEN, lw=1.8, ls='--')
    bg.text(0.5, 0.41, 'whitening filter $1/L(z)$', ha='center', fontsize=10, color=GREEN)
    bg.text(0.5, 0.25, 'stable only if $L$ is minimum phase\n(all poles and zeros inside the unit circle)',
            ha='center', va='top', fontsize=9, color=GREEN)
    save(fig, 'p1_innovation')


def p1_twins():
    th = np.linspace(-np.pi, np.pi, 600)
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    ax = axs[0]
    m1 = np.abs(1 - 0.75 * np.exp(-1j * th)) ** 2
    m2 = np.abs(1 - (4 / 3) * np.exp(-1j * th)) ** 2
    ax.plot(th, m2, color=RED, lw=1.2, alpha=.6, label=r'$|1-\frac{4}{3}e^{-j\theta}|^2$')
    ax.plot(th, m1, color=BLUE, lw=3, label=r'$|1-\frac{3}{4}e^{-j\theta}|^2$')
    ax.plot(th, (0.75 ** 2) * m2, color=RED, ls='--', lw=1.8, label=r'$(\frac{3}{4})^2\,|1-\frac{4}{3}e^{-j\theta}|^2$')
    full_pi(ax)
    ax.legend(fontsize=9, loc='upper center')
    ax.set_ylim(0, 6.2)
    ax.set_title('same shape: the twin is just a constant factor taller', fontsize=10)
    ax = axs[1]
    n = np.arange(13)
    stems(ax, n, 0.75 ** n, color=BLUE, label=r'$a=\frac{3}{4}$: $(\frac{3}{4})^n$ fades')
    stems(ax, n + 0.15, (4 / 3) ** n, color=RED, label=r'$a=\frac{4}{3}$: $(\frac{4}{3})^n$ explodes')
    ax.set_ylim(0, 33)
    ax.legend(fontsize=9, loc='upper left')
    ax.set_xlabel('$n$')
    ax.set_title(r'$x[n]=a\,x[n-1]+i[n]$ after one kick', fontsize=10)
    save(fig, 'p1_twins')


# ================================================================== Part 2
def p2_sampling_dist():
    rng = np.random.default_rng(1)
    mu, sig = 5, 2
    x = np.linspace(2, 8, 600)
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    for N, col in [(4, ORANGE), (25, BLUE), (100, GREEN)]:
        means = rng.normal(mu, sig, (4000, N)).mean(axis=1)
        ax.hist(means, bins=60, density=True, histtype='stepfilled', alpha=.25, color=col)
        ax.plot(x, stats.norm.pdf(x, mu, sig / math.sqrt(N)), color=col,
                label=rf'$N={N}$: spread $\sigma/\sqrt{{N}}={sig / math.sqrt(N):.2g}$')
    ax.axvline(mu, color=RED, ls='--', lw=1.4)
    ax.text(mu + 0.08, 1.85, r'true $\mu=5$', color=RED, fontsize=9.5)
    ax.set_xlabel(r'value of the estimate $\bar x$ (one per dataset)')
    ax.legend(fontsize=9)
    ax.set_title(r'4000 datasets → 4000 estimates $\bar x$: centred on $\mu$, narrower with more data', fontsize=10)
    save(fig, 'p2_sampling_dist')


def p2_sharp_flat():
    rng = np.random.default_rng(6)
    mu = np.linspace(0, 4, 600)
    fig, axs = plt.subplots(1, 2, figsize=(10.8, 3.5))
    ax = axs[0]
    for N, col in [(5, ORANGE), (50, BLUE)]:
        x = rng.normal(2, 1, N)
        ll = -0.5 * ((x[:, None] - mu[None, :]) ** 2).sum(axis=0)
        ll -= ll.max()
        ax.plot(mu, ll, color=col, label=rf'$N={N}$: curvature $-N/\sigma^2=-{N}$')
        m = x.mean()
        w = 1 / math.sqrt(N)
        arrow(ax, m - w, -0.5, m + w, -0.5, color=col, style='<->', lw=1.4, ms=9)
    ax.axhline(-0.5, color=GREY, ls=':', lw=1)
    ax.text(0.05, -0.42, r'drop of $\frac{1}{2}$', color=GREY, fontsize=9)
    ax.set_ylim(-4, 0.3)
    ax.set_xlabel(r'$\mu$')
    ax.set_ylabel('log-likelihood (top set to 0)')
    ax.legend(fontsize=9, loc='lower center')
    ax.set_title(r'sharp peak (big $N$) pins $\mu$ down; flat hill does not', fontsize=10)
    ax = axs[1]
    for N, col in [(5, ORANGE), (50, BLUE)]:
        est = rng.normal(2, 1, (5000, N)).mean(axis=1)
        ax.hist(est, bins=60, density=True, histtype='stepfilled', alpha=.3, color=col)
        g = np.linspace(0, 4, 400)
        ax.plot(g, stats.norm.pdf(g, 2, 1 / math.sqrt(N)), color=col,
                label=rf'$N={N}$: variance $=\frac{{1}}{{\mathcal{{I}}}}=\frac{{1}}{{{N}}}$')
    ax.set_xlabel(r'MLE $\hat\mu$ over 5000 datasets')
    ax.legend(fontsize=9)
    ax.set_title(r'and indeed: the estimates spread exactly $1/\mathcal{I}$', fontsize=10)
    save(fig, 'p2_sharp_flat')


def p2_regularity():
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.3))
    ax = axs[0]
    x = np.linspace(-0.2, 2.3, 800)
    for th, col in [(1, BLUE), (1.5, GREEN), (2, ORANGE)]:
        ax.plot(x, np.where((x >= 0) & (x <= th), 1 / th, 0), color=col, label=rf'$\theta={th}$')
    ax.legend(fontsize=9)
    ax.set_xlabel('$x$')
    ax.set_title(r'uniform on $[0,\theta]$: the EDGE moves with $\theta$', fontsize=10)
    ax = axs[1]
    th = np.linspace(0.3, 2.5, 800)
    L = np.where(th >= 0.8, th ** -5.0, 0)
    ax.plot(th, L, color=RED)
    ax.plot([0.8], [0.8 ** -5], 'o', color=RED)
    ax.text(0.95, 2.2, r'max at $\theta=\max x_n=0.8$: a cliff,' + '\nthe slope is NOT 0 there', fontsize=9.5,
            va='center')
    ax.set_xlabel(r'$\theta$')
    ax.set_title(r'likelihood $\theta^{-N}$ for $\theta\geq\max x_n$ ($N=5$)', fontsize=10)
    save(fig, 'p2_regularity')


def p2_coin():
    th = np.linspace(0, 1, 600)
    prior = stats.beta.pdf(th, 2, 3)
    lik = stats.beta.pdf(th, 4, 2)
    post = stats.beta.pdf(th, 5, 4)
    fig, ax = plt.subplots(figsize=(8.8, 3.6))
    ax.plot(th, prior, color=GREY, lw=1.8, label=r'prior Beta(2,3): $\theta(1-\theta)^2$')
    ax.plot(th, lik, color=ORANGE, lw=1.8, ls='--', label=r'likelihood (3 heads, 1 tail): $\theta^3(1-\theta)$')
    ax.plot(th, post, color=BLUE, lw=2.6, label=r'posterior Beta(5,4): $\theta^4(1-\theta)^3$')
    for v, lab, col, y, ha in [(0.75, 'MLE 0.75', ORANGE, 2.35, 'left'), (4 / 7, 'MAP 0.571', BLUE, 2.62, 'left'),
                               (5 / 9, 'MMSE 0.556', PURPLE, 2.62, 'right')]:
        ax.axvline(v, color=col, ls=':', lw=1.4)
        ax.text(v + (0.008 if ha == 'left' else -0.008), y, lab, color=col, fontsize=9.5, ha=ha)
    ax.set_xlabel(r'$\theta$ (probability of heads)')
    ax.set_ylim(0, 2.9)
    ax.legend(fontsize=8.8, loc='upper left')
    ax.set_title('the prior pulls the answer from 0.75 towards its own belief (0.4)', fontsize=10.5)
    save(fig, 'p2_coin')


def p2_costs():
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.4))
    e = np.linspace(-2, 2, 600)
    ax = axs[0]
    ax.plot(e, e ** 2, color=PURPLE, label='quadratic $e^2$ → posterior mean (MMSE)')
    ax.plot(e, np.abs(e), color=GREEN, label=r'absolute $|e|$ → median')
    ax.plot(e, np.where(np.abs(e) < 0.15, 0, 1), color=BLUE, label='hit-or-miss → mode (MAP)')
    ax.set_ylim(-0.1, 2.3)
    ax.set_xlabel(r'error $e=\theta-\hat\theta$')
    ax.legend(fontsize=8.8, loc='upper center')
    ax.set_title('how much each mistake costs', fontsize=10)
    ax = axs[1]
    th = np.linspace(0, 10, 800)
    p = stats.gamma.pdf(th, 3)
    ax.plot(th, p, color=INK)
    ax.fill_between(th, p, color=GREY, alpha=.15)
    for v, lab, col, y in [(2, 'mode 2 (MAP)', BLUE, 0.335), (stats.gamma.median(3), 'median 2.67', GREEN, 0.305),
                           (3, 'mean 3 (MMSE)', PURPLE, 0.275)]:
        ax.axvline(v, color=col, ls='--', lw=1.4)
        ax.text(v + 0.1, y, lab, color=col, fontsize=9.5)
    ax.set_ylim(0, 0.36)
    ax.set_xlabel(r'$\theta$')
    ax.set_title('a skewed posterior: three different "best" numbers', fontsize=10)
    save(fig, 'p2_costs')


def p2_ls_squares():
    xs = np.array([2, 4, 6.])
    n = np.array([0, 1.6, 3.2])
    fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.7), gridspec_kw=dict(width_ratios=[1, 1, 1.1]))
    for ax, A, col in [(axs[0], 3, ORANGE), (axs[1], 4, GREEN)]:
        ax.axhline(A, color=col, lw=2)
        for xi, v in zip(n, xs):
            r = v - A
            if r:
                ax.add_patch(Rectangle((xi, A), abs(r), r, fc=RED, alpha=.25, ec=RED))
            ax.plot([xi, xi], [A, v], color=RED, lw=1.5)
        ax.plot(n, xs, 'o', color=INK, ms=7, zorder=5)
        J = ((xs - A) ** 2).sum()
        ax.set_title(f'$A={A}$: squares $' + '+'.join(f'{int((v - A) ** 2)}' for v in xs) + f'={J:g}$', fontsize=10,
                     color=col)
        ax.set_xlim(-0.6, 5.8)
        ax.set_ylim(0, 7.6)
        ax.set_aspect('equal')
        ax.set_xticks(n, ['$x[0]$', '$x[1]$', '$x[2]$'])
    axs[0].set_ylabel('value')
    ax = axs[2]
    A = np.linspace(1, 7, 400)
    ax.plot(A, ((xs[:, None] - A[None, :]) ** 2).sum(axis=0), color=INK)
    ax.plot([3], [11], 'o', color=ORANGE, ms=8)
    ax.plot([4], [8], 'o', color=GREEN, ms=8)
    ax.text(4, 9.5, 'minimum: $\\hat A=4$, $J=8$', ha='center', color=GREEN, fontsize=9.5)
    ax.set_xlabel('$A$')
    ax.set_title('cost $J(A)$ = total red area', fontsize=10)
    save(fig, 'p2_ls_squares')


def p2_projection():
    H = np.array([[1, 0], [0, 1], [0.3, 0.5]])
    x = np.array([1.4, 1.1, 2.4])
    th = np.linalg.solve(H.T @ H, H.T @ x)
    p = H @ th
    fig = plt.figure(figsize=(6.6, 5))
    ax = fig.add_subplot(projection='3d')
    s, t = np.meshgrid(np.linspace(-0.3, 2, 2), np.linspace(-0.3, 2, 2))
    P = s[..., None] * H[:, 0] + t[..., None] * H[:, 1]
    ax.plot_surface(P[..., 0], P[..., 1], P[..., 2], color=BLUE, alpha=.15)

    def vec(v, col, lab, ls='-', o=(0, 0, 0)):
        ax.quiver(*o, *(np.array(v) - np.array(o)), color=col, lw=2.2, arrow_length_ratio=0.08, linestyle=ls)
        ax.text(*(np.array(v) + 0.06), lab, color=col, fontsize=11)
    vec(H[:, 0], GREY, 'column 1 of $\\mathbf{H}$')
    vec(H[:, 1], GREY, 'column 2')
    vec(x, INK, 'data $\\mathbf{x}$')
    vec(p, GREEN, 'fit $\\mathbf{H}\\hat{\\theta}$')
    ax.plot(*zip(p, x), color=RED, ls='--', lw=2)
    mid = (p + x) / 2
    ax.text(*(mid + np.array([0.05, 0.05, 0])), 'error: at right angles\nto the plane', color=RED, fontsize=10)
    ax.view_init(elev=18, azim=-58)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_title('LS = drop the data perpendicularly onto the plane of the columns', fontsize=10)
    save(fig, 'p2_projection')


def p2_gauss_newton():
    n = np.arange(6)
    rng = np.random.default_rng(4)
    xd = np.exp(-0.7 * n) + rng.normal(0, 0.03, 6)

    def J(t):
        return ((xd[:, None] - np.exp(-np.outer(n, t))) ** 2).sum(axis=0)
    t = np.linspace(0, 1.6, 600)
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    ax.plot(t, J(t), color=INK, lw=2.2, label=r'true cost $J(\theta)$ (model $e^{-\theta n}$)')
    tk = 0.15
    cols = [ORANGE, BLUE, GREEN]
    for k in range(3):
        s = np.exp(-tk * n)
        h = -n * s
        step = np.dot(h, xd - s) / np.dot(h, h)
        q = ((xd[:, None] - s[:, None] - np.outer(h, t - tk)) ** 2).sum(axis=0)
        ax.plot(t, q, color=cols[k], ls='--', lw=1.4, label=f'straight-line model around $\\theta_{k}={tk:.3f}$')
        ax.plot([tk], J(np.array([tk])), 'o', color=cols[k], ms=7)
        arrow(ax, tk, J(np.array([tk]))[0], tk + step, J(np.array([tk + step]))[0], color=cols[k], lw=1.4, ms=10)
        tk += step
    ax.set_ylim(0, 2.6)
    ax.set_xlabel(r'$\theta$')
    ax.legend(fontsize=8.8, loc='upper right')
    ax.set_title('Gauss–Newton: replace the curve by an easy parabola, jump to its bottom, repeat', fontsize=10)
    save(fig, 'p2_gauss_newton')


# ================================================================== Part 4
def p4_snr_roc():
    x = np.linspace(-4, 7, 700)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.7), gridspec_kw=dict(width_ratios=[1.3, 1]))
    ax = axs[0]
    ax.plot(x, stats.norm.pdf(x), color=INK, lw=2.2, label=r'$\mathcal{H}_0$: $\mathcal{N}(0,1)$')
    pf = np.linspace(1e-5, 1 - 1e-5, 500)
    for d, col in [(0.5, ORANGE), (1, GREEN), (2, BLUE), (3, PURPLE)]:
        ax.plot(x, stats.norm.pdf(x, d), color=col, ls='--', lw=1.4, label=rf'$\mathcal{{H}}_1$: mean {d:g}')
        axs[1].plot(pf, stats.norm.sf(stats.norm.isf(pf) - d), color=col, label=f'separation {d:g}')
    ax.legend(fontsize=8.8, loc='upper right')
    ax.set_title('the further apart the two stories…', fontsize=10)
    ax.set_xlabel('$x$')
    ax = axs[1]
    ax.plot([0, 1], [0, 1], color=GREY, ls=':')
    ax.set_aspect('equal')
    ax.set_xlabel('$P_{FA}$')
    ax.set_ylabel('$P_D$')
    ax.legend(fontsize=8.5, loc='lower right')
    ax.set_title('…the closer the ROC hugs the corner', fontsize=10)
    save(fig, 'p4_snr_roc')


def p4_lr():
    x = np.linspace(-3, 5, 800)
    p0, p1 = stats.norm.pdf(x), stats.norm.pdf(x, 2)
    fig, axs = plt.subplots(2, 1, figsize=(8.6, 5.4), sharex=True, gridspec_kw=dict(height_ratios=[1, 1]))
    ax = axs[0]
    ax.plot(x, p0, color=BLUE, label=r'$p(x\mid\mathcal{H}_0)$: $\mathcal{N}(0,1)$')
    ax.plot(x, p1, color=RED, label=r'$p(x\mid\mathcal{H}_1)$: $\mathcal{N}(2,1)$')
    ax.vlines(1.5, 0, stats.norm.pdf(1.5), color=BLUE, lw=4, alpha=.7)
    ax.vlines(1.52, 0, stats.norm.pdf(1.5, 2), color=RED, lw=2.5, alpha=.6)
    ax.text(1.62, 0.36, 'at $x=1.5$: 0.3521', color=RED, fontsize=9.5)
    ax.text(1.62, 0.1, '0.1295', color=BLUE, fontsize=9.5)
    ax.plot([1], [stats.norm.pdf(1)], 'o', color=INK)
    ax.annotate('equal heights at $x=1$\n($L=1$)', xy=(1, stats.norm.pdf(1)), xytext=(-2.9, 0.2), fontsize=9,
                arrowprops=dict(arrowstyle='->', color=INK))
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title(r'$L(1.5)=\frac{0.3521}{0.1295}=2.72$: $\mathcal{H}_1$ explains $x=1.5$ 2.7× better', fontsize=10)
    ax = axs[1]
    ax.semilogy(x, np.exp(2 * x - 2), color=INK, lw=2, label=r'$L(x)=e^{2x-2}$')
    for lam, xt, col in [(1, 1, GREEN), (9, 1 + math.log(9) / 2, PURPLE)]:
        ax.axhline(lam, color=col, ls='--', lw=1.2)
        ax.axvline(xt, color=col, ls=':', lw=1.2)
        ax.text(-2.9, lam * 1.4, rf'$\lambda={lam}$ → decide $\mathcal{{H}}_1$ for $x>{xt:.2f}$', color=col,
                fontsize=9.5)
    ax.set_xlabel('$x$')
    ax.set_ylabel('likelihood ratio (log scale)')
    ax.legend(fontsize=9, loc='lower right')
    save(fig, 'p4_lr')


def p4_tails():
    fig, axs = plt.subplots(1, 2, figsize=(10.8, 3.5))
    x = np.linspace(-5, 5, 1000)
    ax = axs[0]
    p0, p1 = stats.norm.pdf(x), stats.norm.pdf(x, 0, 2)
    g = math.sqrt(8 * math.log(2) / 3)
    ax.plot(x, p0, color=BLUE, label=r'$\mathcal{H}_0$: $\mathcal{N}(0,1)$')
    ax.plot(x, p1, color=RED, label=r'$\mathcal{H}_1$: $\mathcal{N}(0,4)$ (wider)')
    ax.axvspan(-5, -g, color=RED, alpha=.1)
    ax.axvspan(g, 5, color=RED, alpha=.1)
    ax.text(3.3, 0.3, 'decide\n$\\mathcal{H}_1$', color=RED, ha='center', fontsize=9.5)
    ax.text(-3.3, 0.3, 'decide\n$\\mathcal{H}_1$', color=RED, ha='center', fontsize=9.5)
    ax.text(0, 0.03, f'$\\mathcal{{H}}_0$ for $|x|<{g:.2f}$', color=BLUE, ha='center', fontsize=9.5)
    ax.legend(fontsize=8.8, loc='upper left')
    ax.set_ylim(0, 0.45)
    ax.set_title('variance test: the wider PDF wins in BOTH tails', fontsize=10)
    ax = axs[1]
    p0, p1 = 0.5 * np.exp(-np.abs(x)), np.exp(-2 * np.abs(x))
    g = math.log(2)
    ax.plot(x, p0, color=BLUE, label=r'$\mathcal{H}_0$: $\frac{1}{2}e^{-|x|}$')
    ax.plot(x, p1, color=RED, label=r'$\mathcal{H}_1$: $e^{-2|x|}$ (narrower)')
    ax.axvspan(-g, g, color=RED, alpha=.1)
    ax.text(0, 1.03, f'decide $\\mathcal{{H}}_1$ for $|x|<\\ln 2={g:.2f}$', color=RED, ha='center', fontsize=9.5)
    ax.legend(fontsize=8.8, loc='center right')
    ax.set_ylim(0, 1.15)
    ax.set_title('Laplacian test: the narrower PDF wins near the centre', fontsize=10)
    for a in axs:
        a.set_xlabel('$x$')
    save(fig, 'p4_tails')


def p4_more_samples():
    x = np.linspace(-2, 3, 800)
    fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.2), sharey=True)
    for ax, N in zip(axs, [1, 4, 16]):
        s = 1 / math.sqrt(N)
        p0, p1 = stats.norm.pdf(x, 0, s), stats.norm.pdf(x, 1, s)
        ax.plot(x, p0, color=BLUE)
        ax.plot(x, p1, color=RED)
        ax.fill_between(x, p0, where=x > 0.5, color=BLUE, alpha=.35)
        ax.fill_between(x, p1, where=x < 0.5, color=RED, alpha=.25)
        ax.axvline(0.5, color=INK, ls=':', lw=1.2)
        ax.set_title(rf'$N={N}$: $P_{{FA}}=P_M=Q({math.sqrt(N) / 2:g})={stats.norm.sf(math.sqrt(N) / 2):.3f}$',
                     fontsize=10)
        ax.set_xlabel(r'$\bar x$')
    axs[0].text(-1.9, 1.4, r'blue: $\bar x$ under $\mathcal{H}_0$ (mean 0)' + '\n' + r'red: under $\mathcal{H}_1$ (mean 1)',
                fontsize=9)
    axs[0].set_ylim(0, 1.75)
    save(fig, 'p4_more_samples')


def p4_prior_threshold():
    x = np.linspace(-3, 5, 800)
    p0, p1 = stats.norm.pdf(x), stats.norm.pdf(x, 2)
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.5))
    for ax, P1 in zip(axs[:2], [0.5, 0.1]):
        P0 = 1 - P1
        g = 1 + math.log(P0 / P1) / 2
        ax.plot(x, P0 * p0, color=BLUE, label=rf'$P_0\,p(x|\mathcal{{H}}_0)$, $P_0={P0:g}$')
        ax.plot(x, P1 * p1, color=RED, label=rf'$P_1\,p(x|\mathcal{{H}}_1)$, $P_1={P1:g}$')
        ax.axvline(g, color=INK, ls='--', lw=1.3)
        ax.axvspan(g, 5, color=RED, alpha=.07)
        ax.text(g + 0.1, 0.33, f'decide $\\mathcal{{H}}_1$\nfor $x>{g:.2f}$', fontsize=9.5)
        ax.set_ylim(0, 0.42)
        ax.legend(fontsize=8.5, loc='upper left')
        ax.set_xlabel('$x$')
        ax.set_title('equal priors: cross at $x=1$' if P1 == 0.5 else r'$\mathcal{H}_1$ rare: crossing moves right',
                     fontsize=10)
    ax = axs[2]
    g = np.linspace(-1, 4.5, 500)
    for P1, col in [(0.5, GREEN), (0.1, PURPLE)]:
        Pe = (1 - P1) * stats.norm.sf(g) + P1 * stats.norm.cdf(g - 2)
        ax.plot(g, Pe, color=col, label=f'$P_1={P1:g}$')
        gs = 1 + math.log((1 - P1) / P1) / 2
        ax.plot([gs], [(1 - P1) * stats.norm.sf(gs) + P1 * stats.norm.cdf(gs - 2)], 'o', color=col, ms=7)
    ax.set_xlabel(r'threshold $\gamma$')
    ax.set_title(r'total error $P_0P_{FA}+P_1P_M$: lowest at the crossing', fontsize=10)
    ax.legend(fontsize=9)
    save(fig, 'p4_prior_threshold')


def p4_matched_products():
    s = np.array([1, 2, 1.])
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.4), sharey=True)
    for ax, x, col in [(axs[0], np.array([0.8, 2.5, 0.3]), GREEN), (axs[1], np.array([0.1, -0.4, 0.5]), RED)]:
        n = np.arange(3)
        ax.bar(n - 0.25, s, width=0.22, color=GREY, alpha=.6, label='template $s_n$')
        ax.bar(n, x, width=0.22, color=BLUE, alpha=.7, label='data $x_n$')
        ax.bar(n + 0.25, x * s, width=0.22, color=col, alpha=.85, label=r'product $x_n s_n$')
        tot = (x * s).sum()
        ax.axhline(0, color=INK, lw=.8)
        ax.set_xticks(n, ['$n=0$', '$n=1$', '$n=2$'])
        verdict = r'$>3$ → $\mathcal{H}_1$' if tot > 3 else r'$<3$ → $\mathcal{H}_0$'
        ax.set_title(f'sum of products = {tot:.1f} ' + verdict, fontsize=10.5, color=col)
        ax.legend(fontsize=8.8, loc='upper right')
    axs[0].set_ylim(-1.2, 5.6)
    save(fig, 'p4_matched_products')


PAGES_B = [p1_bayes_area, p1_indep_disjoint, p1_pmf_cdf, p1_joint_ops, p1_cov, p1_valid_r, p1_innovation, p1_twins,
           p2_sampling_dist, p2_sharp_flat, p2_regularity, p2_coin, p2_costs, p2_ls_squares, p2_projection,
           p2_gauss_newton,
           p4_snr_roc, p4_lr, p4_tails, p4_more_samples, p4_prior_threshold, p4_matched_products]

PAGES_A = [p0_sampling, p0_sine, p0_alias, p0_complex, p0_integral_sum, p0_geometric, p0_sin2, p0_limit, p0_spectrum,
           p0_ftd_dft, p0_db, p0_pdfs, p0_expectation, p0_gauss, p0_likelihood, p0_autocorr, p0_r_psd,
           p3_energy_power, p3_examples, p3_cos_u, p3_window_time, p3_N_lobes, p3_resolution,
           p3_darts, p3_periodogram_N, p3_rhat_bias, p3_bartlett, p3_methods, p3_bt,
           p3_memory, p3_impulse, p3_shaping, p3_poles_zeros, p3_ar1_tail,
           p3_chain_three, p3_corr_negative, p3_ar_notch]


if __name__ == '__main__':
    todo = {f.__name__: f for f in PAGES_A + PAGES_B}
    for name in (sys.argv[1:] or list(todo)):
        todo[name]()
