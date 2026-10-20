"""Recompute every numeric exam answer used in the guide.

Run: python scripts/verify.py  (prints a report; any FAIL means the guide text needs fixing)
"""
import math
import numpy as np
import sympy as sp
from scipy import stats, integrate, optimize

R = sp.Rational
th = sp.symbols('theta', real=True)
c = sp.cos(th)
results = []


def check(name, got, expected, tol=1e-3):
    ok = abs(float(got) - float(expected)) <= tol * max(1, abs(float(expected)))
    results.append((ok, name, got, expected))


def Q(x):
    return stats.norm.sf(x)


# ---------- Part 1: probability ----------
# Jun26 1b
pD = 0.4 * .02 + .35 * .04 + .25 * .05
check('Jun26 1b P(def)', pD, 0.0345)
check('Jun26 1b P(M2|def)', .35 * .04 / pD, 0.4058)
# Apr25 1a
pq = (18 * .85 + 22 * .9 + 15 * .66) / 55
check('Apr25 1a P(fail)', 1 - pq, 0.1818)
check('Apr25 1a P(CT2|fail)', (22 / 55 * .1) / (1 - pq), 0.22)
# Apr24 1a
check('Apr24 1a', 1 - math.exp(-1 / 5), 0.1813)
# Apr24 1b
check('Apr24 1b', .99 * .0005 / (.99 * .0005 + .01 * .9995), 0.0472)
# Nov22 1a
check('Nov22 1a', .75 * .65 + .4 * .35, 0.6275)
# Jan22 1a
check('Jan22 1a', .85 * .25 / (.8 * .75 + .85 * .25), 0.2615)
# PE21 1a, 1d
check('PE21 1a', .95 * .018 / (.95 * .018 + .03 * .982), 0.367)
check('PE21 1d', math.comb(8, 6) * .8 ** 6 * .2 ** 2, 0.2936)
# Jan20 2
pp = (30 * .85 + 45 * .92 + 25 * .6) / 100
check('Jan20 2a', pp, 0.819)
check('Jan20 2b', .25 * .6 / pp, 0.1832)
# Jan25 1a
check('Jan25 1a-1', 26 / 36, 0.7222)
check('Jan25 1a-2', 67 / 200, 0.335)

# joint pdfs
x, y, cc = sp.symbols('x y c', positive=True)
sol = sp.solve(sp.integrate(sp.integrate(cc * x + 1, (x, 0, 1 - y)), (y, 0, 1)) - 1, cc)
check('Apr25 1c c', sol[0], 3)
check('Jun24 1c c', 1 / sp.integrate(sp.integrate(sp.exp(-x) * sp.exp(-y), (y, 0, x)), (x, 0, sp.oo)), 2)
print('Jun26 1c pX =', sp.integrate(6 * x ** 2 * y, (y, 0, 1)), ' pY =', sp.integrate(6 * x ** 2 * y, (x, 0, 1)))
print('Apr24 1c pY =', sp.integrate(2, (x, y, 1)))


# spectral factorisation helper: P = num/den in cos; check sigma^2|L|^2 equals P
def same_psd(P, Lnum, Lden, s2):
    z = sp.exp(sp.I * th)
    H = Lnum(z) / Lden(z)
    lhs = s2 * sp.simplify(H * sp.conjugate(H))
    vals = [abs(complex(sp.N((lhs - P).subs(th, t)))) for t in np.linspace(0.1, 3, 7)]
    return max(vals)


check('Nov22 1d', same_psd(1 / (R(5, 3) - c), lambda z: 1, lambda z: 1 - R(1, 3) / z, R(2, 3)), 0, 1e-9)
check('Apr24 1e', same_psd(7 / (25 - 24 * c), lambda z: 1, lambda z: 1 - R(3, 4) / z, R(7, 16)), 0, 1e-9)
check('Apr25 1e', same_psd(1 / (61 + 60 * c), lambda z: 1, lambda z: 1 + R(5, 6) / z, R(1, 36)), 0, 1e-9)
check('Jan24 1f', same_psd((10 + 6 * c) / (17 - 8 * c), lambda z: 1 + R(1, 3) / z, lambda z: 1 - R(1, 4) / z, R(9, 16)), 0, 1e-9)
check('Jan22 1d', same_psd((R(17, 8) - c) / (R(25, 16) + R(3, 2) * c), lambda z: 1 - R(1, 4) / z, lambda z: 1 + R(3, 4) / z, 2), 0, 1e-9)

# Jan20 1a: PSD of r_B
pB = lambda t: 2 - 3 * np.cos(t) + np.cos(2 * t)
print('Jan20 1a r_B PSD min =', min(pB(t) for t in np.linspace(0, np.pi, 1001)), '(negative => strictly not valid)')
# Nov19 1a cross-correlation
xs = np.array([1, 1, 1, 0]); ys = np.array([1, 3, 3, 5])
cc_full = {l: sum(xs[n] * ys[n - l] for n in range(4) if 0 <= n - l < 4) / 4 for l in range(-3, 4)}
print('Nov19 1a r_xy[l]=E{x[n]y[n-l]}:', cc_full)

# ---------- Part 2: estimation ----------
# Jun26 2c NegBin + Beta
xsn = [3, 5, 4, 6, 4]; a_post = 2 + 2 * len(xsn); b_post = 3 + sum(xsn) - 2 * len(xsn)
check('Jun26 2c MAP', (a_post - 1) / (a_post + b_post - 2), 0.44)
print('Jun26 2c posterior Beta(', a_post, ',', b_post, ')')
# Jun26 2d Poisson + Gamma
xp = [2, 4, 3, 5, 2, 4]
check('Jun26 2d MAP', (3 + sum(xp) - 1) / (2 + len(xp)), 2.75)
check('Jun26 2d MLE', sum(xp) / len(xp), 10 / 3)
# Apr25 2b line fit
A = np.array([[0, 1], [2, 1], [3, 1]]); b = np.array([3, 4, 3])
sl = np.linalg.lstsq(A, b, rcond=None)[0]
check('Apr25 2b slope', sl[0], 1 / 14); check('Apr25 2b icpt', sl[1], 45 / 14)
# Apr25 2c numeric check of MLE at x = 3
xo = 3.0
f = lambda t: -(math.log(1 / (1 + math.exp(-t))) - 4 / 7 / (1 + math.exp(-t)) * xo)
tnum = optimize.minimize_scalar(f, bounds=(-10, 10), method='bounded').x
check('Apr25 2c theta(x=3)', tnum, -math.log(4 * xo / 7 - 1), 1e-3)
# Apr24 2d numeric (x=3)
f = lambda t: -(math.log(1 / (1 + math.exp(-t))) - 0.5 / (1 + math.exp(-t)) * xo)
tnum = optimize.minimize_scalar(f, bounds=(-10, 10), method='bounded').x
check('Apr24 2d theta(x=3)', tnum, -math.log(xo / 2 - 1), 1e-3)
# Nov19 3b CRLB: Fisher info for Rayleigh(theta) per sample = 4/theta^2
t0 = 1.7
d2 = lambda xv: 2 / t0 ** 2 - 3 * xv ** 2 / t0 ** 4
EI = -integrate.quad(lambda xv: d2(xv) * xv / t0 ** 2 * math.exp(-xv ** 2 / (2 * t0 ** 2)), 0, 50)[0]
check('Nov19 3b i(theta)', EI, 4 / t0 ** 2)
# Jan19 2b MMSE with uniform prior on [0,2], single x
lam, xx = sp.symbols('lambda x', positive=True)
num = sp.integrate(lam ** 2 * sp.exp(-lam * xx), (lam, 0, 2)); den = sp.integrate(lam * sp.exp(-lam * xx), (lam, 0, 2))
mm = sp.simplify(num / den)
mine = 2 / xx * (1 - 2 * xx ** 2 * sp.exp(-2 * xx) / (1 - sp.exp(-2 * xx) * (2 * xx + 1)))
key = 2 / xx * (1 - xx ** 2 * sp.exp(-2 * xx) / (1 - sp.exp(-2 * xx) * (2 * xx + 1)))
check('Jan19 2b mine (x=0.7)', mm.subs(xx, 0.7), mine.subs(xx, 0.7), 1e-9)
print('Jan19 2b official key at x=0.7:', float(key.subs(xx, 0.7)), ' true:', float(mm.subs(xx, 0.7)))
# Nov22 2f MMSE
a_, x_ = 0.8, 1.3
post = lambda t: (x_ + a_) ** 2 * t * math.exp(-(x_ + a_) * t)
check('Nov22 2f', integrate.quad(lambda t: t * post(t), 0, 60)[0], 2 / (x_ + a_))
check('Nov22 2g', optimize.minimize_scalar(lambda t: -post(t), bounds=(0, 10), method='bounded').x, 1 / (x_ + a_))
# Jan22 2g: tanh
s2, yv = 0.7, 0.4
p1 = math.exp(-(yv - 1) ** 2 / (2 * s2)); pm = math.exp(-(yv + 1) ** 2 / (2 * s2))
check('Jan22 2g', (p1 - pm) / (p1 + pm), math.tanh(yv / s2))

# ---------- Part 3: spectra ----------
def corr_psd(r):
    return lambda t: r[0] + 2 * sum(r[k] * np.cos(k * t) for k in range(1, len(r)))


def yule_walker(r, p):
    Rm = np.array([[r[abs(i - j)] for j in range(p)] for i in range(p)])
    a = np.linalg.solve(Rm, -np.array(r[1:p + 1]))
    s2 = r[0] + sum(a[k] * r[k + 1] for k in range(p))
    return a, s2


def ar_psd(a, s2):
    return lambda t: s2 / abs(1 + sum(a[k] * np.exp(-1j * (k + 1) * t) for k in range(len(a)))) ** 2


def ma1(r0, r1):
    # sigma^2 (1+b^2) = r0, sigma^2 b = r1  -> r1 b^2 - r0 b + r1 = 0
    roots = np.roots([r1, -r0, r1]); b = roots[np.argmin(abs(roots))].real
    return b, r1 / b


# Jun26 3c/3d
r = [3, 2, 1]
a, s2 = yule_walker(r, 2)
check('Jun26 a1', a[0], -0.8); check('Jun26 a2', a[1], 0.2); check('Jun26 s2', s2, 1.6)
P = ar_psd(a, s2)
check('Jun26 PAR(0)', P(0), 10); check('Jun26 PAR(pi)', P(np.pi), 0.4)
check('Jun26 PAR closed form', P(1.0), 10 / (5 * np.cos(1) ** 2 - 12 * np.cos(1) + 8))
check('Jun26 Pcorr (2c+1)^2', corr_psd(r)(1.0), (2 * np.cos(1) + 1) ** 2)
check('Jun26 3b K', (1000 - 200) / 100 + 1, 9)
# Apr25 3d-3g
r = [2, -1 / 4, -3 / 16]
a, s2 = yule_walker(r, 1)
check('Apr25 a1', a[0], 1 / 8); check('Apr25 s2', s2, 63 / 32)
check('Apr25 PAR', ar_psd(a, s2)(0.7), 126 / (65 + 16 * np.cos(0.7)))
b1, s2m = ma1(2, -1 / 4)
check('Apr25 b1', b1, -4 + math.sqrt(15)); check('Apr25 s2 MA', s2m, 1.968)
for t in [0, np.pi]:
    print('Apr25 3g at', round(t, 2), 'corr', corr_psd(r)(t), 'AR', ar_psd(a, s2)(t), 'MA', s2m * abs(1 + b1 * np.exp(-1j * t)) ** 2)
# Apr24 MA(3)
bco = np.array([1, -.5, .25, -.5])
rr = [sum(bco[k] * bco[k - l] for k in range(l, 4)) for l in range(4)]
print('Apr24 r =', rr)
a, s2 = yule_walker(rr, 2)
check('Apr24 a1', a[0], 204 / 481); check('Apr24 a2', a[1], -56 / 481); check('Apr24 s2', s2, 9129 / 7696)
for t in [0, np.pi / 2, np.pi]:
    print('Apr24 3f at', round(t, 2), 'corr', corr_psd(rr)(t), 'AR', ar_psd(a, s2)(t))
# Nov22 ARMA(1,1)
s2i = 7 / 8
r0 = sp.symbols('r0'); r1s = sp.symbols('r1')
solr = sp.solve([sp.Eq(r0, s2i * (1 + R(1, 4)) + R(3, 4) * r1s), sp.Eq(r1s, -s2i + R(3, 4) * r0)], [r0, r1s])
check('Nov22 r0', solr[r0], 1); check('Nov22 r1', solr[r1s], -1 / 8)
# simulate ARMA(1,1) to cross-check r
rng = np.random.default_rng(1)
i_ = rng.normal(0, math.sqrt(7 / 8), 400000); xx_ = np.zeros_like(i_)
for n in range(1, len(i_)):
    xx_[n] = i_[n] - i_[n - 1] + .75 * xx_[n - 1]
print('Nov22 simulated r0,r1,r2:', np.mean(xx_ ** 2), np.mean(xx_[1:] * xx_[:-1]), np.mean(xx_[2:] * xx_[:-2]), ' theory r2 =', -3 / 32)
a, s2 = yule_walker([1, -1 / 8], 1)
check('Nov22 3f a1', a[0], 1 / 8); check('Nov22 3f s2', s2, 63 / 64)
b1, s2m = ma1(1, -1 / 8)
check('Nov22 3g b1', b1, -0.127); check('Nov22 3g s2', s2m, 0.984)
# Jan22 3b-3d
a, s2 = yule_walker([13 / 8, -15 / 16], 1)
check('Jan22 3d a1', a[0], 15 / 26); check('Jan22 3d s2', s2, 451 / 416)
check('Jan22 3d PSD', ar_psd(a, s2)(1.1), 5863 / (7208 + 6240 * np.cos(1.1)))
# PE21
i_ = rng.normal(0, 1, 400000); xx_ = np.zeros_like(i_)
for n in range(1, len(i_)):
    xx_[n] = i_[n] - 2 / 3 * i_[n - 1] + .5 * xx_[n - 1]
print('PE21 simulated r0,r1:', np.mean(xx_ ** 2), np.mean(xx_[1:] * xx_[:-1]), ' theory', 28 / 27, -4 / 27)
a, s2 = yule_walker([28 / 27, -4 / 27], 1)
check('PE21 a1', a[0], 1 / 7); check('PE21 s2', s2, 64 / 63)
check('PE21 PAR', ar_psd(a, s2)(0.9), (32 / 9) / (25 / 7 + np.cos(0.9)))
# Jan20 3b
b1, s2m = ma1(1 / 21, 2 / 105)
check('Jan20 b1', b1, .5); check('Jan20 s2', s2m, 4 / 105)
# Nov19 2b
a, s2 = yule_walker([1, .7, .5], 2)
print('Nov19 AR(2):', a, s2)
# Jan19 Wiener
Rx = np.array([[1 / 3, 1 / 6], [1 / 6, 1 / 3]]); rex = np.array([2 / 3, 5 / 6])
w = np.linalg.solve(Rx, rex); check('Jan19 4a w0', w[0], 1); check('Jan19 4a w1', w[1], 2)
check('Jan19 4a J', 7 / 3 - w @ rex, 0, 1e-9)

# ---------- Part 4: detection ----------
# Jan22 4c / Apr24 4b
yth = optimize.brentq(lambda v: .25 * math.exp(-v / 2) / (math.exp(-v * v / 2) / math.sqrt(2 * math.pi)) - 1, 0.5, 5)
check('Jan22 yth', yth, 1.5884)
check('Jan22 PD', math.exp(-yth / 2), 0.4521)
check('Jan22 PFA', 2 * Q(yth), 0.1122)
# Nov22
check('Nov22 4e PD', 1 - .9 ** 2, 0.19)
check('Nov22 4g PFA', 1 - 1 / 3, 2 / 3); check('Nov22 4g PM', 1 / 9, 1 / 9)
# Apr25 4a
check('Apr25 4a', 0.1 ** (1 / 6), 0.6813)
# Jan20 5
xth = math.log(20) / 1.9; check('Jan20 5a xth', xth, 1.5767)
x1 = -math.log(.9) / .1; l1 = math.log(10) / x1
check('Jan20 5b lam1', l1, 2.1854)
# Nov19 4b
check('Nov19 PD', 2 * Q(1), 0.3173, 5e-3); check('Nov19 PFA', 2 * Q(3), 0.0027, 0.5)
# Jan19 3b
for X, mu, sg in [(1, 1, 1), (1, 3, 1), (1, 3, 2), (2, 3, 1)]:
    print('Jan19 3b', X, mu, sg, 'Pd', stats.norm.sf(X, mu, sg), 'Pfa', Q(X))
# Q1-2023 4d
check('Q1-23 4d', math.sqrt(8 / 3 * math.log(4)), 1.9228)

bad = [r_ for r_ in results if not r_[0]]
for ok, name, got, exp in results:
    print(('ok  ' if ok else 'FAIL'), name, float(got), float(exp))
print(len(results), 'checks,', len(bad), 'failed')
