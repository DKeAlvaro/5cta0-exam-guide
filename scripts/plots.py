"""Generate every solution figure of the guide into docs/img/gen/*.svg.

Run: python scripts/plots.py
"""
import math
import os

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
from scipy import stats

OUT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'img', 'gen')
os.makedirs(OUT, exist_ok=True)

INK = '#1d1b19'
RED = '#b3261e'
BLUE = '#1f5fae'
GREEN = '#2e7d32'
ORANGE = '#d9822b'
PURPLE = '#6a3d9a'
GREY = '#8a8580'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10.5,
    'axes.edgecolor': INK,
    'axes.labelcolor': INK,
    'xtick.color': INK,
    'ytick.color': INK,
    'axes.grid': True,
    'grid.color': '#e6e1d8',
    'grid.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'svg.fonttype': 'path',
    'mathtext.fontset': 'cm',
    'lines.linewidth': 2,
})

PI_TICKS = ([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
TH = np.linspace(-np.pi, np.pi, 1001)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + '.svg'), bbox_inches='tight')
    if os.environ.get('PREVIEW'):
        fig.savefig(os.path.join(os.environ['PREVIEW'], name + '.png'), bbox_inches='tight', dpi=80)
    plt.close(fig)
    print('wrote', name)


def pi_axis(ax):
    ax.set_xticks(*PI_TICKS)
    ax.set_xlim(-np.pi, np.pi)
    ax.set_xlabel(r'$\theta$ (rad/sample)')


def corr_psd(r, t=TH):
    return r[0] + 2 * sum(r[k] * np.cos(k * t) for k in range(1, len(r)))


def ar_psd(a, s2, t=TH):
    return s2 / np.abs(1 + sum(a[k] * np.exp(-1j * (k + 1) * t) for k in range(len(a)))) ** 2


def ma_psd(b, s2, t=TH):
    return s2 * np.abs(1 + sum(b[k] * np.exp(-1j * (k + 1) * t) for k in range(len(b)))) ** 2


def yw(r, p):
    Rm = np.array([[r[abs(i - j)] for j in range(p)] for i in range(p)])
    a = np.linalg.solve(Rm, -np.array(r[1:p + 1]))
    return a, r[0] + sum(a[k] * r[k + 1] for k in range(p))


# ------------------------------------------------------------------ Part 1
def bayes_tree():
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    root = (0.6, 3)
    machines = [('$M_1$', 0.40, 0.02, 5.0), ('$M_2$', 0.35, 0.04, 3.0), ('$M_3$', 0.25, 0.05, 1.0)]
    ax.text(*root, 'chip', ha='center', va='center', fontsize=11,
            bbox=dict(boxstyle='round,pad=0.35', fc='#f3eee4', ec=INK))
    for name, pm, pd, yy in machines:
        ax.plot([1.1, 3.4], [3, yy], color=INK, lw=1.4)
        ax.text(2.0, (3 + yy) / 2 + (0.3 if yy >= 3 else -0.45), f'{pm:.2f}', color=BLUE, fontsize=10, ha='center')
        ax.text(3.75, yy, name, ha='center', va='center', fontsize=12,
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=INK))
        ax.plot([4.1, 6.2], [yy, yy + 0.45], color=RED, lw=1.4)
        ax.plot([4.1, 6.2], [yy, yy - 0.45], color=GREY, lw=1.0)
        ax.text(5.0, yy + 0.5, f'{pd:.2f}', color=RED, fontsize=10, ha='center')
        ax.text(6.35, yy + 0.45, 'defective', color=RED, fontsize=10, va='center')
        ax.text(6.35, yy - 0.45, 'ok', color=GREY, fontsize=10, va='center')
        ax.text(8.0, yy + 0.45, f'{pm:.2f}×{pd:.2f} = {pm * pd:.4f}', fontsize=10, va='center', color=INK)
    ax.text(8.0, 5.85, 'path probability', fontsize=9.5, color=GREY)
    save(fig, 'p1_bayes_tree')


def supports():
    fig, axs = plt.subplots(1, 3, figsize=(10, 3.4))
    # Apr24 1c: 0<=y<=x<=1
    ax = axs[0]
    ax.fill([0, 1, 1], [0, 0, 1], color=BLUE, alpha=.18)
    ax.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE)
    yy = 0.35
    ax.plot([yy, 1], [yy, yy], color=RED, lw=3)
    ax.annotate('fix $y$: $x$ runs from $y$ to 1', xy=(0.66, yy), xytext=(0.05, 0.8), color=RED,
                arrowprops=dict(arrowstyle='->', color=RED), fontsize=9.5)
    ax.set_title(r'Apr 2024 1c: $0\leq y\leq x\leq 1$', fontsize=10.5)
    # Apr25 1c: x,y>=0, x+y<1
    ax = axs[1]
    ax.fill([0, 1, 0], [0, 0, 1], color=GREEN, alpha=.18)
    ax.plot([0, 1, 0, 0], [0, 0, 1, 0], color=GREEN)
    yy = 0.3
    ax.plot([0, 1 - yy], [yy, yy], color=RED, lw=3)
    ax.annotate('fix $y$: $x$ from 0 to $1-y$', xy=(0.35, yy), xytext=(0.3, 0.75), color=RED,
                arrowprops=dict(arrowstyle='->', color=RED), fontsize=9.5)
    ax.set_title(r'Apr 2025 1c: $x,y\geq0,\ x+y<1$', fontsize=10.5)
    # Jun26 1c: unit square
    ax = axs[2]
    ax.fill([0, 1, 1, 0], [0, 0, 1, 1], color=ORANGE, alpha=.18)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=ORANGE)
    ax.text(0.5, 0.5, 'rectangle:\nlimits do not\ndepend on each other', ha='center', va='center', fontsize=9.5)
    ax.set_title(r'June 2026 1c: $0\leq x,y\leq1$', fontsize=10.5)
    for ax in axs:
        ax.set_xlim(-0.1, 1.15)
        ax.set_ylim(-0.1, 1.15)
        ax.set_aspect('equal')
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
    save(fig, 'p1_supports')


def gauss_contours():
    fig, axs = plt.subplots(1, 3, figsize=(10, 3.4))
    g = np.linspace(-2.5, 2.5, 300)
    X, Y = np.meshgrid(g, g)
    cases = [(np.array([[0.4, 0], [0, 1.5]]), r'$\sigma_x^2<\sigma_y^2,\ \mathrm{cov}=0$', BLUE),
             (np.array([[1, 0], [0, 1]]), r'$\sigma_x^2=\sigma_y^2,\ \mathrm{cov}=0$', GREEN),
             (np.array([[1, 0.8], [0.8, 1]]), r'$\mathrm{cov}(X,Y)=0.8\neq0$', RED)]
    for ax, (C, title, col) in zip(axs, cases):
        Ci = np.linalg.inv(C)
        Z = np.exp(-0.5 * (Ci[0, 0] * X ** 2 + 2 * Ci[0, 1] * X * Y + Ci[1, 1] * Y ** 2))
        ax.contour(X, Y, Z, levels=[0.1, 0.3, 0.5, 0.7, 0.9], colors=col, linewidths=1.4)
        ax.axhline(0, color=GREY, lw=0.8)
        ax.axvline(0, color=GREY, lw=0.8)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=10.5)
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
    axs[2].text(0, -2.2, 'tilted = correlated', ha='center', color=RED, fontsize=10)
    axs[0].text(0, -2.2, 'axis-aligned', ha='center', color=BLUE, fontsize=10)
    save(fig, 'p1_gauss_contours')


def processes():
    rng = np.random.default_rng(3)
    fig, axs = plt.subplots(2, 2, figsize=(10, 5.6))
    t = np.linspace(0, 12, 400)
    ax = axs[0, 0]
    for k in range(4):
        u = rng.uniform(0, 2 * np.pi)
        ax.plot(t, np.cos(t + u), lw=1.4)
    ax.axhline(0, color=INK, lw=1.2, ls='--')
    ax.set_title(r'$X(t)=\cos(t+U)$: every realisation averages to 0', fontsize=10)
    ax.set_xlabel('$t$')
    ax = axs[0, 1]
    for k in range(4):
        a = rng.normal(1, math.sqrt(2))
        ax.plot(t, a * np.cos(t), lw=1.4)
    ax.plot(t, np.cos(t), color=INK, lw=2.2, ls='--', label=r'ensemble mean $\cos t$')
    ax.legend(loc='lower left', fontsize=9)
    ax.set_title(r'$X(t)=A\cos t$: mean changes with $t$ (not WSS)', fontsize=10)
    ax.set_xlabel('$t$')
    ax = axs[1, 0]
    n = np.arange(40)
    for k in range(3):
        ax.plot(n, rng.integers(1, 7, 40) + 0.08 * k, 'o', ms=3.5)
    ax.axhline(3.5, color=INK, ls='--', lw=1.4)
    ax.set_title('dice process: each row is one die; time average → 3.5', fontsize=10)
    ax.set_xlabel('$n$')
    ax = axs[1, 1]
    for a in [0.4, 1.4, 3.0]:
        ax.plot(n, rng.uniform(-a, a, 40), 'o-', ms=3, lw=0.8, label=f'$A={a}$')
    ax.axhline(0, color=INK, ls='--', lw=1.4)
    ax.legend(loc='lower left', fontsize=9, ncol=3)
    ax.set_title(r'Nov 2022 1c: $X[n]\sim U(-A,A)$, $A$ fixed per realisation', fontsize=10)
    ax.set_xlabel('$n$')
    save(fig, 'p1_processes')


def rB_psd():
    fig, ax = plt.subplots(figsize=(7, 3.2))
    p = 2 - 3 * np.cos(TH) + np.cos(2 * TH)
    ax.plot(TH, p, color=BLUE, label=r'$\sum_l r_B[l]e^{-jl\theta}=2-3\cos\theta+\cos2\theta$')
    ax.fill_between(TH, p, 0, where=p < 0, color=RED, alpha=.35, label='negative: impossible for a real PSD')
    ax.axhline(0, color=INK, lw=1)
    pi_axis(ax)
    ax.legend(fontsize=9, loc='upper center')
    ax.set_ylim(-0.6, 6.5)
    save(fig, 'p1_rB_psd')


def unit_circle():
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.8))
    for ax, a, ok in [(axs[0], 0.75, True), (axs[1], 4 / 3, False)]:
        circ = np.linspace(0, 2 * np.pi, 300)
        ax.plot(np.cos(circ), np.sin(circ), color=GREY, lw=1.2)
        ax.plot([a], [0], 'x', ms=13, mew=3, color=GREEN if ok else RED)
        ax.axhline(0, color=GREY, lw=0.6)
        ax.axvline(0, color=GREY, lw=0.6)
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.4, 1.4)
        ax.set_aspect('equal')
        ax.set_title(('pole at $3/4$: inside → keep' if ok else 'pole at $4/3$: outside → reject'), fontsize=10.5,
                     color=GREEN if ok else RED)
        ax.set_xlabel('Re $z$')
        ax.set_ylabel('Im $z$')
    save(fig, 'p1_unit_circle')


# ------------------------------------------------------------------ Part 2
def mle_idea():
    rng = np.random.default_rng(7)
    k = 3
    data = rng.gamma(k, 2.0, 12)
    thetas = np.linspace(0.6, 5, 400)
    ll = np.array([np.sum(stats.gamma.logpdf(data, k, scale=t)) for t in thetas])
    th_hat = data.mean() / k
    fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.3))
    axs[0].plot(thetas, np.exp(ll - ll.max()), color=BLUE)
    axs[0].set_title(r'likelihood $L(\theta)$ (rescaled)', fontsize=10.5)
    axs[1].plot(thetas, ll, color=RED)
    axs[1].set_title(r'log-likelihood $\ln L(\theta)$', fontsize=10.5)
    for ax in axs:
        ax.axvline(th_hat, color=INK, ls='--', lw=1.3)
        ax.set_xlabel(r'$\theta$')
        ax.text(th_hat + 0.08, ax.get_ylim()[0] + 0.1 * (ax.get_ylim()[1] - ax.get_ylim()[0]),
                r'$\hat\theta=\bar x/k$', fontsize=10)
    save(fig, 'p2_mle_idea')


def beta_post():
    t = np.linspace(0, 1, 500)
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    prior = stats.beta.pdf(t, 2, 3)
    lik = t ** 10 * (1 - t) ** 12
    lik = lik / np.trapezoid(lik, t)
    post = stats.beta.pdf(t, 12, 15)
    ax.plot(t, prior, color=GREY, ls='--', label='prior Beta(2,3)')
    ax.plot(t, lik, color=BLUE, label=r'likelihood $\propto\theta^{10}(1-\theta)^{12}$')
    ax.plot(t, post, color=RED, label='posterior Beta(12,15)')
    ax.axvline(11 / 25, color=RED, lw=1.2)
    ax.axvline(10 / 22, color=BLUE, lw=1.2, ls=':')
    ax.text(11 / 25 - 0.02, 4.6, 'MAP 0.44', color=RED, ha='right')
    ax.text(10 / 22 + 0.02, 4.6, 'MLE 0.455', color=BLUE)
    ax.set_xlabel(r'$\theta$')
    ax.legend(fontsize=9, loc='upper right')
    save(fig, 'p2_beta_post')


def gamma_post():
    l = np.linspace(0, 7, 600)
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    prior = stats.gamma.pdf(l, 3, scale=1 / 2)
    lik = l ** 20 * np.exp(-6 * l)
    lik = lik / np.trapezoid(lik, l)
    post = stats.gamma.pdf(l, 23, scale=1 / 8)
    ax.plot(l, prior, color=GREY, ls='--', label=r'prior Gamma($\alpha$=3, $\beta$=2)')
    ax.plot(l, lik, color=BLUE, label=r'likelihood $\propto\lambda^{20}e^{-6\lambda}$')
    ax.plot(l, post, color=RED, label=r'posterior Gamma(23, 8)')
    ax.axvline(2.75, color=RED, lw=1.2)
    ax.axvline(10 / 3, color=BLUE, lw=1.2, ls=':')
    ax.text(2.7, 1.08, 'MAP 2.75', color=RED, ha='right')
    ax.text(3.4, 1.08, 'MLE 3.33', color=BLUE)
    ax.set_xlabel(r'$\lambda$ (spikes/day)')
    ax.legend(fontsize=9, loc='upper right')
    save(fig, 'p2_gamma_post')


def mixture():
    x = 3.0
    t = np.linspace(-6, 6, 800)
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.3), sharey=True)
    for ax, cval in zip(axs, [0.5, 0.75]):
        p = cval * stats.norm.pdf(t, x, 1) + (1 - cval) * stats.norm.pdf(t, -x, 1)
        ax.plot(t, p, color=BLUE)
        mmse = x * (2 * cval - 1)
        ax.axvline(mmse, color=RED, lw=1.5, label=f'MMSE = {mmse:g}')
        if cval == 0.5:
            ax.plot([-x, x], [p.max()] * 2, 'v', color=GREEN, ms=9, label=r'MAP = $\pm x$')
        else:
            ax.plot([x], [p.max()], 'v', color=GREEN, ms=9, label=r'MAP $\approx x$')
        ax.set_title(f'$c={cval:g}$, observed $x=3$', fontsize=10.5)
        ax.set_xlabel(r'$\theta$')
        ax.legend(fontsize=9, loc='upper left')
    save(fig, 'p2_mixture')


def nov22_post():
    s = 2.0
    t = np.linspace(0, 3.5, 500)
    p = s ** 2 * t * np.exp(-s * t)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(t, p, color=BLUE, label=r'$p(\theta|x)=(x+a)^2\theta e^{-(x+a)\theta}$ with $x+a=2$')
    ax.axvline(1 / s, color=GREEN, lw=1.5, label=r'MAP $=1/(x+a)$ (peak)')
    ax.axvline(2 / s, color=RED, lw=1.5, label=r'MMSE $=2/(x+a)$ (mean)')
    ax.set_xlabel(r'$\theta$')
    ax.legend(fontsize=9)
    save(fig, 'p2_nov22_post')


def lsfit():
    xs = np.array([0, 2, 3])
    ys = np.array([3, 4, 3])
    a, b = 1 / 14, 45 / 14
    g = np.linspace(-0.5, 3.5, 10)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.plot(g, a * g + b, color=RED, label=r'$\hat y=\frac{1}{14}x+\frac{45}{14}$')
    for xi, yi in zip(xs, ys):
        ax.plot([xi, xi], [yi, a * xi + b], color=GREY, lw=1.2, ls='--')
    ax.plot(xs, ys, 'o', color=BLUE, ms=8, label='data')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_ylim(2.5, 4.5)
    ax.legend(fontsize=9.5)
    ax.text(1.1, 2.7, 'dashed = residuals; LS minimises the sum of their squares', fontsize=9, color=GREY)
    save(fig, 'p2_lsfit')


def sigmoid_ll():
    t = np.linspace(-4, 4, 500)
    lam = 1 / (1 + np.exp(-t))
    fig, ax = plt.subplots(figsize=(7, 3.2))
    for x, col in [(3.0, BLUE), (1.5, ORANGE)]:
        ll = np.log(3 * lam) - 4 / 7 * lam * x
        ax.plot(t, ll, color=col, label=f'$x={x}$')
    th = -math.log(4 * 3 / 7 - 1)
    ax.axvline(th, color=BLUE, ls='--', lw=1.2)
    ax.text(th + 0.1, -1.6, r'$\hat\theta=-\ln(\frac{4x}{7}-1)$', color=BLUE)
    ax.text(1.0, 0.2, 'x < 7/4: keeps rising, no finite max', color=ORANGE, fontsize=9)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'$\ln p(x|\theta)$')
    ax.legend(fontsize=9, loc='lower right')
    save(fig, 'p2_sigmoid')


# ------------------------------------------------------------------ Part 3
def windows():
    N = 25
    w_r = np.ones(N)
    w_h = np.hanning(N + 2)[1:-1]
    f = np.linspace(-np.pi, np.pi, 4001)
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.3))
    for w, col, lab in [(w_r, BLUE, 'rectangular'), (w_h, RED, 'Hann')]:
        W = np.abs(np.array([np.sum(w * np.exp(-1j * f_ * np.arange(N))) for f_ in f]))
        axs[0].plot(f, 20 * np.log10(W / W.max() + 1e-9), color=col, label=lab, lw=1.5)
    axs[0].set_ylim(-80, 3)
    axs[0].set_xlim(-np.pi, np.pi)
    axs[0].set_xticks(*PI_TICKS)
    axs[0].set_ylabel('dB')
    axs[0].set_title('window spectra, $N=25$', fontsize=10.5)
    axs[0].annotate('main lobe\n(width → resolution)', xy=(0, -3), xytext=(0.9, -20), fontsize=9,
                    arrowprops=dict(arrowstyle='->'))
    axs[0].annotate('side lobes\n(height → leakage)', xy=(-0.62, -13), xytext=(-3.0, -8), fontsize=9,
                    arrowprops=dict(arrowstyle='->'))
    axs[0].legend(fontsize=9, loc='upper right')
    # two close sinusoids
    n = np.arange(N)
    x = np.cos(1.0 * n) + 0.02 * np.cos(2.3 * n)
    for w, col, lab in [(w_r, BLUE, 'rectangular'), (w_h, RED, 'Hann')]:
        X = np.abs(np.array([np.sum(w * x * np.exp(-1j * f_ * n)) for f_ in f]))
        axs[1].plot(f, 20 * np.log10(X / X.max() + 1e-9), color=col, lw=1.4, label=lab)
    axs[1].axvline(2.3, color=GREEN, ls='--', lw=1.2)
    axs[1].text(2.36, -6, 'weak tone (−34 dB):\nlost in rectangular\nleakage, visible\nwith Hann', color=GREEN, fontsize=8.3,
                va='top')
    axs[1].set_xlim(0, np.pi)
    axs[1].set_ylim(-80, 3)
    axs[1].set_title('strong tone at 1.0 + weak tone at 2.3', fontsize=10.5)
    axs[1].set_xlabel(r'$\theta$')
    axs[1].legend(fontsize=9, loc='lower left')
    save(fig, 'p3_windows')


def zeropad():
    N = 16
    n = np.arange(N)
    th0 = 2 * np.pi * 3.4 / N
    x = np.cos(th0 * n)
    f = np.linspace(0, np.pi, 2000)
    X = np.abs(np.array([np.sum(x * np.exp(-1j * f_ * n)) for f_ in f]))
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.plot(f, X, color=GREY, lw=1.4, label=r'$N$-sample FTD (continuous in $\theta$)')
    k = np.arange(N // 2 + 1)
    ax.plot(2 * np.pi * k / N, np.abs(np.fft.fft(x))[:N // 2 + 1], 's', color=BLUE, ms=7, label='N-point DFT (N=16)')
    L = 64
    k = np.arange(L // 2 + 1)
    ax.plot(2 * np.pi * k / L, np.abs(np.fft.fft(x, L))[:L // 2 + 1], 'o', color=RED, ms=3.5,
            label='zero-padded to L=64')
    ax.set_xlim(0, np.pi)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel('magnitude')
    ax.legend(fontsize=9)
    ax.set_title('zero padding samples the same curve more densely; it does not sharpen it', fontsize=10)
    save(fig, 'p3_zeropad')


def welch():
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.axis('off')
    ax.set_xlim(-30, 1030)
    ax.set_ylim(-1.8, 10.5)
    ax.plot([0, 1000], [-0.8, -0.8], color=INK, lw=3)
    ax.text(500, -1.6, 'data record, N = 1000 samples', ha='center', fontsize=10)
    for k in range(9):
        s = 100 * k
        col = [BLUE, RED][k % 2]
        ax.add_patch(FancyBboxPatch((s, k + 0.1), 200, 0.7, boxstyle='round,pad=0.01', fc=col, alpha=.35, ec=col))
        ax.text(s + 100, k + 0.42, f'segment {k + 1}: [{s}, {s + 199}]', ha='center', va='center', fontsize=8.2)
    ax.text(910, 4, 'L = 200\nhop D = 100\n(50% overlap)\n\nK = (N−L)/D + 1\n   = 9', fontsize=9.5, va='center')
    save(fig, 'p3_welch')


def psd_compare(name, curves, title=None, ylim=None, legend_loc='upper center'):
    fig, ax = plt.subplots(figsize=(7.4, 3.5))
    for y, lab, col, ls in curves:
        ax.plot(TH, y, color=col, ls=ls, label=lab)
    ax.axhline(0, color=INK, lw=0.8)
    pi_axis(ax)
    if ylim:
        ax.set_ylim(*ylim)
    if title:
        ax.set_title(title, fontsize=10.5)
    ax.legend(fontsize=9, loc=legend_loc)
    save(fig, name)


def spectral_cases():
    # June 2026
    r = [3, 2, 1]
    a, s2 = yw(r, 2)
    psd_compare('p3_jun26', [(corr_psd(r), r'$\hat P_{corr}=(2\cos\theta+1)^2$', BLUE, '-'),
                             (ar_psd(a, s2), r'$\hat P_{AR(2)}=10/(5\cos^2\theta-12\cos\theta+8)$', RED, '--')],
                'June 2026: correlogram vs AR(2)')
    # April 2025
    r = [2, -1 / 4, -3 / 16]
    a, s2 = yw(r, 1)
    b1 = -4 + math.sqrt(15)
    psd_compare('p3_apr25', [(corr_psd(r), r'$P_{corr}$', BLUE, '-'),
                             (ar_psd(a, s2), r'$P_{AR(1)}=126/(65+16\cos\theta)$', RED, '--'),
                             (ma_psd([b1], -0.25 / b1), r'$P_{MA(1)}\approx2-0.5\cos\theta$', GREEN, ':')],
                'April 2025: this is plot D', ylim=(0, 3.2), legend_loc='lower center')
    # April 2024
    bco = np.array([1, -.5, .25, -.5])
    rr = [sum(bco[k] * bco[k - l] for k in range(l, 4)) for l in range(4)]
    a, s2 = yw(rr, 2)
    psd_compare('p3_apr24', [(corr_psd(rr), r'$P_{corr}$ (= true MA(3) PSD)', BLUE, '-'),
                             (ar_psd(a, s2), r'$P_{AR(2)}$', RED, '--')],
                'April 2024: this is plot B', ylim=(0, 6.2))
    # Nov 2022
    true = 7 / 8 * np.abs(1 - np.exp(-1j * TH)) ** 2 / np.abs(1 - .75 * np.exp(-1j * TH)) ** 2
    b1 = -4 + math.sqrt(15)
    psd_compare('p3_nov22', [(true, 'true ARMA(1,1)', INK, '-'),
                             (corr_psd([1, -1 / 8, -3 / 32]), 'correlogram, 3 lags', BLUE, '-'),
                             (ar_psd([1 / 8], 63 / 64), 'AR(1)', RED, '--'),
                             (ma_psd([b1], -0.125 / b1), r'MA(1) $=1-0.25\cos\theta$', GREEN, ':')],
                'November 2022: no low-order model captures the zero at θ = 0', ylim=(0, 1.5),
                legend_loc='lower right')
    # Jan 2022
    psd_compare('p3_jan22', [(corr_psd([13 / 8, -15 / 16, 1 / 4]), r'correlogram $=$ true MA(2) PSD', BLUE, '-'),
                             (ar_psd([15 / 26], 451 / 416), 'AR(1) fit', RED, '--')],
                'January 2022 resit', ylim=(0, 4.5), legend_loc='upper center')
    # Practice 2021
    true = np.abs(1 - 2 / 3 * np.exp(-1j * TH)) ** 2 / np.abs(1 - .5 * np.exp(-1j * TH)) ** 2
    psd_compare('p3_pe21', [(true, 'true ARMA(1,1)', INK, '-'),
                            (ar_psd([1 / 7], 64 / 63), 'AR(1)', RED, '--'),
                            (corr_psd([28 / 27, -4 / 27]), 'correlogram, MA(1) lags', BLUE, ':')],
                'Practice exam 2021', ylim=(0, 1.6), legend_loc='lower center')
    # Jan 2020
    psd_compare('p3_jan20', [(corr_psd([1 / 21, 2 / 105]), r'$P_{corr}=P_{MA(1)}=\frac{1}{21}+\frac{4}{105}\cos\theta$', BLUE, '-')],
                'January 2020: both methods give the same curve', ylim=(0, 0.1), legend_loc='lower center')
    # Nov 2019
    r = [1, .7, .5, .3]
    a, s2 = yw(r, 2)
    psd_compare('p3_nov19', [(corr_psd(r), r'$P_{corr}$', BLUE, '-'), (ar_psd(a, s2), r'$P_{AR(2)}$', RED, '--')],
                'November 2019', ylim=(-0.5, 6.5))


def ar_ma_shapes():
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.1))
    axs[0].plot(TH, ar_psd([-0.8], 1), color=RED, label='$a_1=-0.8$')
    axs[0].plot(TH, ar_psd([0.8], 1), color=BLUE, ls='--', label='$a_1=+0.8$')
    axs[0].set_title('AR(1): peaks (poles)', fontsize=10.5)
    axs[1].plot(TH, ma_psd([1.0], 1), color=GREEN, label='$b_1=1$')
    axs[1].plot(TH, ma_psd([-1.0], 1), color=ORANGE, ls='--', label='$b_1=-1$')
    axs[1].set_title('MA(1): smooth, can touch 0 (zeros)', fontsize=10.5)
    axs[2].plot(TH, corr_psd([1, 0.6, 0.4, 0.3]), color=BLUE)
    axs[2].axhline(0, color=INK, lw=0.8)
    axs[2].set_title('correlogram: wiggly, may go < 0', fontsize=10.5)
    for ax in axs:
        pi_axis(ax)
        if ax is not axs[2]:
            ax.legend(fontsize=9)
    save(fig, 'p3_shapes')


def model_order():
    rng = np.random.default_rng(5)
    N = 200
    i_ = rng.normal(0, 1, N + 100)
    x = np.zeros_like(i_)
    for n in range(2, len(i_)):
        x[n] = i_[n] + 1.2 * x[n - 1] - 0.6 * x[n - 2]
    x = x[100:]
    r = [np.sum(x[l:] * x[:N - l]) / N for l in range(13)]
    ps = np.arange(1, 13)
    s2 = np.array([yw(r, p)[1] for p in ps])
    aic = N * np.log(s2) + 2 * (ps + 1)
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.2))
    axs[0].plot(ps, s2, 'o-', color=BLUE)
    axs[0].set_title(r'residual variance $\hat\sigma_p^2$ only goes down', fontsize=10.5)
    axs[1].plot(ps, aic, 'o-', color=RED)
    axs[1].plot(ps[np.argmin(aic)], aic.min(), '*', ms=16, color=GREEN)
    axs[1].set_title(r'AIC $=N\ln\hat\sigma_p^2+2P$ has a minimum', fontsize=10.5)
    for ax in axs:
        ax.set_xlabel('model order $p$')
    save(fig, 'p3_order')


# ------------------------------------------------------------------ Part 4
def regions_generic():
    x = np.linspace(-4, 6, 800)
    p0 = stats.norm.pdf(x, 0, 1)
    p1 = stats.norm.pdf(x, 2, 1)
    g = 1.3
    fig, axs = plt.subplots(1, 3, figsize=(11, 3.1), sharey=True)
    for ax in axs:
        ax.plot(x, p0, color=BLUE, label=r'$p(x|\mathcal{H}_0)$')
        ax.plot(x, p1, color=RED, ls='--', label=r'$p(x|\mathcal{H}_1)$')
        ax.axvline(g, color=INK, lw=1.2)
        ax.set_xlabel('$x$')
        ax.text(g + 0.1, 0.42, r'decide $\mathcal{H}_1$ →', fontsize=9)
        ax.text(g - 0.1, 0.42, r'← decide $\mathcal{H}_0$', fontsize=9, ha='right')
        ax.set_ylim(0, 0.47)
    axs[0].fill_between(x, p0, where=x > g, color=BLUE, alpha=.35)
    axs[0].set_title(r'$P_{FA}$: $\mathcal{H}_0$ true, said $\mathcal{H}_1$', fontsize=10.5)
    axs[1].fill_between(x, p1, where=x > g, color=RED, alpha=.3)
    axs[1].set_title(r'$P_D$: $\mathcal{H}_1$ true, said $\mathcal{H}_1$', fontsize=10.5)
    axs[2].fill_between(x, p1, where=x < g, color=ORANGE, alpha=.4)
    axs[2].set_title(r'$P_M=1-P_D$: $\mathcal{H}_1$ true, said $\mathcal{H}_0$', fontsize=10.5)
    axs[0].legend(fontsize=9, loc='upper left')
    save(fig, 'p4_regions')


def nov22_y():
    y = np.linspace(0, 5, 600)
    p0 = np.exp(-y)
    p1 = 2 * np.exp(-2 * y)
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.3), sharey=True)
    for ax in axs:
        ax.plot(y, p0, color=INK, label=r'$p(y;\mathcal{H}_0)=e^{-y}$')
        ax.plot(y, p1, color=INK, ls='--', label=r'$p(y;\mathcal{H}_1)=2e^{-2y}$')
        ax.axvline(1, color=GREY, ls=':', lw=1.5)
        ax.set_xlabel('$y$')
        ax.text(0.5, 1.75, r'decide $\mathcal{H}_1$', ha='center', color=RED, fontsize=9)
        ax.text(2.5, 1.75, r'decide $\mathcal{H}_0$', ha='center', color=GREEN, fontsize=9)
    axs[0].fill_between(y, p0, where=y < 1, color=BLUE, alpha=.35)
    axs[0].set_title(r'$P_{FA}=\int_0^1 e^{-y}dy=1-e^{-1}\approx0.63$', fontsize=10.5)
    axs[1].fill_between(y, p1, where=y > 1, color=ORANGE, alpha=.5)
    axs[1].set_title(r'$P_M=\int_1^\infty 2e^{-2y}dy=e^{-2}\approx0.14$', fontsize=10.5)
    axs[0].legend(fontsize=9, loc='center right')
    save(fig, 'p4_nov22_y')


def nov22_bayes():
    y = np.linspace(0, 4, 600)
    w0 = 0.4 * np.exp(-y)
    w1 = 0.6 * 2 * np.exp(-2 * y)
    g = math.log(3)
    fig, ax = plt.subplots(figsize=(7, 3.3))
    ax.plot(y, w0, color=INK, label=r'$P_0\,p(y;\mathcal{H}_0)=0.4e^{-y}$')
    ax.plot(y, w1, color=INK, ls='--', label=r'$P_1\,p(y;\mathcal{H}_1)=1.2e^{-2y}$')
    ax.axvline(g, color=RED, lw=1.4)
    ax.fill_between(y, w0, where=y < g, color=BLUE, alpha=.3, label=r'$P_0P_{FA}=4/15$')
    ax.fill_between(y, w1, where=y > g, color=ORANGE, alpha=.45, label=r'$P_1P_M=1/15$')
    ax.text(g + 0.05, 0.9, r'$\gamma\'\'=\ln3\approx1.10$', color=RED)
    ax.set_xlabel('$y=|x|$')
    ax.legend(fontsize=9)
    save(fig, 'p4_nov22_bayes')


def gauss_laplace():
    y = np.linspace(-6, 6, 1200)
    p0 = stats.norm.pdf(y)
    p1 = 0.25 * np.exp(-np.abs(y) / 2)
    yt = 1.5884
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.plot(y, p0, color=BLUE, label=r'$\mathcal{H}_0$: $\frac{1}{\sqrt{2\pi}}e^{-y^2/2}$')
    ax.plot(y, p1, color=RED, ls='--', label=r'$\mathcal{H}_1$: $\frac{1}{4} e^{-|y|/2}$')
    ax.fill_between(y, p0, where=np.abs(y) > yt, color=BLUE, alpha=.45, label=r'$P_{FA}$')
    ax.fill_between(y, p1, where=np.abs(y) < yt, color=ORANGE, alpha=.35, label=r'$P_M$')
    for s in [-1, 1]:
        ax.axvline(s * yt, color=INK, lw=1.1, ls=':')
    ax.text(0, 0.43, r'decide $\mathcal{H}_0$', ha='center', fontsize=9)
    ax.text(3.6, 0.2, r'decide $\mathcal{H}_1$', ha='center', fontsize=9)
    ax.text(-3.6, 0.2, r'decide $\mathcal{H}_1$', ha='center', fontsize=9)
    ax.text(yt + 0.1, 0.33, r'$|y|=1.588$', fontsize=9)
    ax.set_xlabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    save(fig, 'p4_gauss_laplace')


def rayleigh_q123():
    x = np.linspace(0, 6, 600)
    p0 = x * np.exp(-x ** 2 / 2)
    p1 = x / 4 * np.exp(-x ** 2 / 8)
    xt = math.sqrt(8 / 3 * math.log(4))
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.plot(x, p0, color=INK, label=r'$p(x;\mathcal{H}_0)$')
    ax.plot(x, p1, color=INK, ls='--', label=r'$p(x;\mathcal{H}_1)$')
    ax.fill_between(x, p0, where=x > xt, color=BLUE, alpha=.4, label=r'$P_{FA}$')
    ax.fill_between(x, p1, where=x < xt, color=ORANGE, alpha=.4, label=r'$P_M$')
    ax.axvline(xt, color=RED, lw=1.2)
    ax.text(xt + 0.08, 0.55, r'$x=\lambda\'\approx1.92$ (curves cross)', color=RED, fontsize=9.5)
    ax.set_xlabel('$x$')
    ax.legend(fontsize=9, loc='center right')
    save(fig, 'p4_rayleigh_q123')


def nov19():
    s0, s1 = 1.0, 3.0
    x = np.linspace(-8, 8, 1000)
    p0 = stats.norm.pdf(x, 0, s0)
    p1 = stats.norm.pdf(x, 0, s1)
    xt = math.sqrt(2 * s0 ** 2 * s1 ** 2 / (s1 ** 2 - s0 ** 2) * math.log(s1 / s0))
    fig, ax = plt.subplots(figsize=(7.4, 3.3))
    ax.plot(x, p0, color=BLUE, label=r'$\mathcal{H}_0$: $\sigma_0=1$')
    ax.plot(x, p1, color=RED, ls='--', label=r'$\mathcal{H}_1$: $\sigma_1=3$')
    ax.fill_between(x, p1, where=np.abs(x) > xt, color=RED, alpha=.2, label=r'$P_D$')
    ax.fill_between(x, p0, where=np.abs(x) > xt, color=BLUE, alpha=.5, label=r'$P_{FA}$')
    for s in [-1, 1]:
        ax.axvline(s * xt, color=INK, ls=':', lw=1.1)
    ax.text(0, 0.36, r'$\mathcal{H}_0$', ha='center')
    ax.text(5, 0.12, r'decide $\mathcal{H}_1$', ha='center', fontsize=9)
    ax.text(-5, 0.12, r'decide $\mathcal{H}_1$', ha='center', fontsize=9)
    ax.text(xt + 0.15, 0.25, rf'$|x|={xt:.2f}$', fontsize=9)
    ax.set_xlabel('$x$')
    ax.legend(fontsize=9, loc='upper left')
    save(fig, 'p4_nov19')


def jan20():
    x = np.linspace(0, 4, 600)
    l0, l1 = 0.1, 2.0
    xt = math.log(20) / 1.9
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.3))
    ax = axs[0]
    ax.plot(x, l0 * np.exp(-l0 * x), color=BLUE, label=r'$\mathcal{H}_0$: $0.1e^{-0.1x}$')
    ax.plot(x, l1 * np.exp(-l1 * x), color=RED, ls='--', label=r'$\mathcal{H}_1$: $2e^{-2x}$')
    ax.axvline(xt, color=INK, ls=':', lw=1.2)
    ax.fill_between(x, l0 * np.exp(-l0 * x), where=x < xt, color=BLUE, alpha=.35, label=r'$P_{FA}$')
    ax.text(xt + 0.05, 1.5, r'$x_{th}=\frac{\ln20}{1.9}\approx1.58$', fontsize=9.5)
    ax.text(0.4, 1.0, r'decide $\mathcal{H}_1$', color=RED, fontsize=9)
    ax.text(2.6, 1.0, r'decide $\mathcal{H}_0$', color=BLUE, fontsize=9)
    ax.set_xlabel('$x$')
    ax.legend(fontsize=9, loc='upper right')
    ax = axs[1]
    pf = np.linspace(0, 1, 400)
    for ratio, col, lab in [(21.85, INK, r'$\lambda_1=2.19$ (from 5b)'), (60, GREEN, r'$\lambda_1$ larger'),
                            (5, ORANGE, r'$\lambda_1$ smaller')]:
        ax.plot(pf, 1 - (1 - pf) ** ratio, color=col, label=lab)
    ax.plot([0, 1], [0, 1], color=GREY, ls=':', lw=1.2)
    ax.plot([0.1], [0.9], 'o', color=RED)
    ax.text(0.13, 0.86, '(0.1, 0.9)', color=RED, fontsize=9)
    ax.set_xlabel('$P_{FA}$')
    ax.set_ylabel('$P_D$')
    ax.set_title(r'ROC: $P_D=1-(1-P_{FA})^{\lambda_1/\lambda_0}$', fontsize=10.5)
    ax.legend(fontsize=9, loc='lower right')
    save(fig, 'p4_jan20')


def roc_pe21():
    pf = np.linspace(1e-6, 1 - 1e-6, 500)
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    th_ = [-1, 0, 1, 2, 3]
    for mu, col in [(1, BLUE), (2, RED)]:
        ax.plot(pf, stats.norm.sf(stats.norm.isf(pf) - mu), color=col, lw=1.4, alpha=.6)
        P = [(stats.norm.sf(t), stats.norm.sf(t - mu)) for t in th_]
        ax.plot([p[0] for p in P], [p[1] for p in P], 'o', color=col, ms=7, label=rf'$\mu={mu}$ (table points)')
        for t, p in zip(th_, P):
            if mu == 2:
                ax.annotate(f'$y_{{th}}={t}$', p, xytext=(6, -12), textcoords='offset points', fontsize=8.5, color=GREY)
    ax.plot([0, 1], [0, 1], color=GREY, ls=':', lw=1.2, label='chance line')
    ax.set_xlabel('$P_{fa}$')
    ax.set_ylabel('$P_d$')
    ax.set_aspect('equal')
    ax.legend(fontsize=9, loc='lower right')
    save(fig, 'p4_roc_pe21')


def roc_explain():
    pf = np.linspace(1e-6, 1 - 1e-6, 400)
    good = stats.norm.sf(stats.norm.isf(pf) - 1.5)
    fig, ax = plt.subplots(figsize=(5.4, 4.6))
    ax.plot(pf, good, color=GREEN, label='a sensible test')
    ax.plot(good, pf, color=RED, ls='--', label='same test with $P_d$, $P_{fa}$ or $\\mathcal{H}$s swapped')
    ax.plot([0, 1], [0, 1], color=GREY, ls=':', label='coin flip')
    ax.plot([0], [1], '*', ms=14, color=INK)
    ax.text(0.03, 0.93, 'perfect', fontsize=9)
    ax.set_xlabel('$P_{fa}$')
    ax.set_ylabel('$P_d$')
    ax.set_aspect('equal')
    ax.legend(fontsize=8.5, loc='lower right')
    save(fig, 'p4_roc_explain')


def rayleigh_jun26():
    x = np.linspace(0, 8, 600)
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.4))
    ax = axs[0]
    for s, col, ls in [(1, BLUE, '-'), (1.5, ORANGE, '--'), (3, RED, '--')]:
        ax.plot(x, x / s ** 2 * np.exp(-x ** 2 / (2 * s ** 2)), color=col, ls=ls, label=rf'$\sigma={s}$')
    ax.set_xlabel('$x$ (mV)')
    ax.set_title(r'Rayleigh pdfs: $\sigma_0=1$ vs two choices of $\sigma_1$', fontsize=10.5)
    ax.legend(fontsize=9)
    ax = axs[1]
    pf = np.linspace(0, 1, 400)
    for s1, col in [(1.2, ORANGE), (1.5, GREEN), (3, RED)]:
        ax.plot(pf, pf ** (1 / s1 ** 2), color=col, label=rf'$\sigma_1/\sigma_0={s1}$')
    ax.plot([0, 1], [0, 1], color=GREY, ls=':', label='$\\sigma_1=\\sigma_0$ (useless)')
    ax.set_xlabel('$P_{FA}$')
    ax.set_ylabel('$P_D$')
    ax.set_title(r'ROC: $P_D=P_{FA}^{\,\sigma_0^2/\sigma_1^2}$', fontsize=10.5)
    ax.legend(fontsize=9, loc='lower right')
    save(fig, 'p4_rayleigh_jun26')


def apr24_4b():
    y = np.linspace(0, 6, 600)
    p0 = np.exp(-y ** 2 / 2) / math.sqrt(2 * math.pi)
    p1 = 0.25 * np.exp(-y / 2)
    yt = 1.5884
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.plot(y, p0, color=BLUE, label=r'$\mathcal{H}_0$: $\frac{1}{\sqrt{2\pi}}e^{-y^2/2}$')
    ax.plot(y, p1, color=RED, ls='--', label=r'$\mathcal{H}_1$: $\frac{1}{4}e^{-y/2}$')
    ax.fill_between(y, p0, where=y > yt, color=BLUE, alpha=.45, label=r'$P_{FA}$')
    ax.fill_between(y, p1, where=y < yt, color=ORANGE, alpha=.35, label=r'$P_M$ ($P_D$ = rest of the red curve)')
    ax.axvline(yt, color=INK, ls=':', lw=1.2)
    ax.text(yt + 0.08, 0.3, r'$y_{th}\approx1.588$', fontsize=9.5)
    ax.set_xlabel('$y$')
    ax.legend(fontsize=9)
    save(fig, 'p4_apr24')


if __name__ == '__main__':
    for fn in [bayes_tree, supports, gauss_contours, processes, rB_psd, unit_circle,
               mle_idea, beta_post, gamma_post, mixture, nov22_post, lsfit, sigmoid_ll,
               windows, zeropad, welch, spectral_cases, ar_ma_shapes, model_order,
               regions_generic, nov22_y, nov22_bayes, gauss_laplace, rayleigh_q123, nov19, jan20,
               roc_pe21, roc_explain, rayleigh_jun26, apr24_4b]:
        fn()
