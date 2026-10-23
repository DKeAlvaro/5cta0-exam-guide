"""Episode 4 · Rapid-fire true/false: the multiple-choice sentences the exams recycle, all four blocks."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manim import DOWN, LEFT, UP, FadeIn, Rectangle, VGroup  # noqa: E402
from podkit import Pod, card, chip  # noqa: E402
from vidkit import BLUE, GREEN, GREY, INK, MT, ORANGE, PURPLE, RED  # noqa: E402

# (block, shown statement, spoken statement, True?, shown reason, spoken reason)
Q = [
    ('Block 4 · Detection', r'Neyman–Pearson fixes $P_{FA}$ and then MINIMISES $P_D$.',
     'Neyman Pearson fixes the false alarm probability and then minimises the detection probability.', False,
     r'It MAXIMISES $P_D$. Nobody wants fewer detections.', 'It maximises the detection probability. Nobody wants fewer detections.'),
    ('Block 4 · Detection', 'Bayesian detection chooses the decision regions that MAXIMISE the Bayes risk.',
     'Bayesian detection chooses the decision regions that maximise the Bayes risk.', False,
     'Risk = expected cost. You MINIMISE it.', 'Risk is expected cost. You minimise it.'),
    ('Block 4 · Detection', r'With costs $C_{01}=C_{10}=1$, $C_{00}=C_{11}=0$, the Bayes test minimises the probability of error.',
     'With cost one for each mistake and zero for being right, the Bayes test minimises the total probability of error.', True,
     'With 0/1 costs, the risk IS the error probability.', 'With zero one costs, the risk is exactly the error probability.'),
    ('Block 4 · Detection', r'Increasing $P(H_1)$ RAISES the threshold, making it harder to decide $H_1$.',
     'Increasing the prior of H one raises the threshold, making it harder to decide H one.', False,
     r'It LOWERS the threshold: $\lambda=P_0/P_1$ gets smaller. $H_1$ gets easier.', 'It lowers the threshold. Lambda is P zero over P one, which gets smaller. H one gets easier.'),
    ('Block 4 · Detection', 'Equal priors and equal costs reduce the Bayes rule to the maximum likelihood rule.',
     'Equal priors and equal costs reduce the Bayes rule to the maximum likelihood rule.', True,
     r'$\lambda=1$: just pick the taller curve.', 'Lambda becomes one: just pick the taller curve.'),
    ('Block 4 · Detection', 'A type I error is a false alarm.', 'A type one error is a false alarm.', True,
     r'Decide $H_1$ while $H_0$ is true. A miss is type II.', 'You decide H one while H zero is true. A miss is a type two error.'),
    ('Block 4 · Detection', r'$P_D$ is the area under the $H_0$ curve in the decide-$H_1$ zone.',
     'P D is the area under the H zero curve in the decide H one zone.', False,
     r'That is $P_{FA}$. $P_D$ uses the $H_1$ curve.', 'That is the false alarm probability. P D uses the H one curve.'),
    ('Block 2 · Estimation', 'The MMSE estimate is the MAXIMUM of the posterior.', 'The MMSE estimate is the maximum of the posterior.', False,
     'MMSE = the MEAN of the posterior. The maximum is the MAP.', 'MMSE is the mean of the posterior. The maximum is the MAP.'),
    ('Block 2 · Estimation', 'The MMSE and the MAP estimators ALWAYS give different estimates.',
     'The MMSE and the MAP estimators always give different estimates.', False,
     'Same for a symmetric posterior, like a Gaussian.', 'They are the same for a symmetric posterior, like a Gaussian.'),
    ('Block 2 · Estimation', r'The Fisher information of $N$ i.i.d. samples is $N\,i(\theta)$.',
     'The Fisher information of N independent identical samples is N times i of theta.', True,
     'Each independent sample adds the same information.', 'Each independent sample adds the same amount of information.'),
    ('Block 2 · Estimation', r'Any unbiased estimator has Var$(\hat\theta)\geq\mathcal{I}(\theta)$.',
     'Any unbiased estimator has variance at least the Fisher information.', False,
     r'At least ONE OVER it: Var $\geq 1/\mathcal{I}(\theta)$.', 'At least one over the Fisher information.'),
    ('Block 2 · Estimation', 'The Fisher information is strictly negative.', 'The Fisher information is strictly negative.', False,
     r'It is always $\geq 0$.', 'It is never negative.'),
    ('Block 2 · Estimation', 'The Cramér–Rao lower bound can always be derived.', 'The Cramer Rao lower bound can always be derived.', False,
     r'Not when the range of $x$ depends on $\theta$, e.g. $0\leq x\leq\theta$.', 'Not when the range of x depends on theta, for example x between zero and theta.'),
    ('Block 2 · Estimation', 'The MLE always achieves the CRLB.', 'The MLE always achieves the Cramer Rao bound.', False,
     r'Only asymptotically, when $N\to\infty$.', 'Only asymptotically, when N goes to infinity.'),
    ('Block 2 · Estimation', 'The MLE is asymptotically unbiased.', 'The MLE is asymptotically unbiased.', True,
     'Right on average when N is large.', 'It is right on average when N is large.'),
    ('Block 2 · Estimation', r'If $\alpha=\psi(\theta)$ is one-to-one, then $\hat\theta_{ML}=\psi^{-1}(\hat\alpha_{ML})$.',
     'If alpha is a one to one function of theta, the MLE of theta is the inverse function of the MLE of alpha.', True,
     'Invariance of the MLE: the sigmoid trick.', 'That is the invariance of the MLE. You used it in the sigmoid trick.'),
    ('Block 2 · Estimation', 'As N grows, the MAP converges to the MLE REGARDLESS of the prior.',
     'As N grows, the MAP converges to the MLE regardless of the prior.', False,
     '"Regardless" kills it: a prior that is zero at the truth can never be overruled.', 'The word regardless kills it. A prior that is zero at the true value can never be overruled.'),
    ('Block 2 · Estimation', 'An estimator with variance LOWER than the CRLB is called efficient.',
     'An estimator with variance lower than the Cramer Rao bound is called efficient.', False,
     'Efficient = EQUAL to the bound. Lower is impossible.', 'Efficient means equal to the bound. Lower is impossible for an unbiased estimator.'),
    ('Block 3 · Spectral', r'The periodogram is a consistent estimator of the PSD.', 'The periodogram is a consistent estimator of the PSD.', False,
     r'Its variance does NOT go to 0 as $N\to\infty$.', 'Its variance does not go to zero as N grows. More data gives more points, not calmer points.'),
    ('Block 3 · Spectral', 'Zero padding improves the frequency resolution.', 'Zero padding improves the frequency resolution.', False,
     'Only more dots on the same curve. Resolution needs more REAL data.', 'It only gives more dots on the same curve. Resolution needs more real data.'),
    ('Block 3 · Spectral', 'A Hamming window gives BETTER resolution than a rectangular one.',
     'A Hamming window gives better resolution than a rectangular window.', False,
     'Lower side lobes (less leakage), but a WIDER main lobe (worse resolution).', 'It has lower side lobes, so less leakage, but a wider main lobe, so worse resolution.'),
    ('Block 3 · Spectral', 'Main lobe width sets the resolution; side lobe height sets the leakage.',
     'The main lobe width sets the resolution, and the side lobe height sets the leakage.', True,
     'Narrow main lobe = close peaks separate. Low side lobes = little leakage.', 'Narrow main lobe means close peaks can be separated. Low side lobes mean little leakage.'),
    ('Block 3 · Spectral', r'Bartlett with $K$ segments: variance $\div K$, but the bias increases.',
     'Bartlett with K segments divides the variance by K, but the bias increases.', True,
     'Shorter segments = more smearing.', 'Shorter segments mean more smearing, so more bias.'),
    ('Block 3 · Spectral', 'Welch averages periodograms of NON-overlapping segments.', 'Welch averages periodograms of non overlapping segments.', False,
     'Welch OVERLAPS (and windows). Non-overlapping is Bartlett.', 'Welch uses overlapping, windowed segments. Non overlapping is Bartlett.'),
    ('Block 3 · Spectral', 'Blackman–Tukey = DFT of the windowed autocorrelation estimate.',
     'Blackman Tukey is the DFT of the windowed autocorrelation estimate.', True,
     'Window the lags, then transform.', 'You window the lags, then transform.'),
    ('Block 3 · Spectral', r'$N=1000$, $L=200$, 50 % overlap  $\Rightarrow$  $K=9$ Welch segments.',
     'N equals one thousand, segment length two hundred, fifty percent overlap. That gives nine Welch segments.', True,
     r'$K=\frac{N-L}{D}+1=\frac{800}{100}+1=9$, variance ratio $\frac{1}{9}$.', 'K equals N minus L over the hop, plus one: eight hundred over one hundred, plus one. Nine. The variance ratio is one ninth.'),
    ('Block 3 · Spectral', 'Raising the AR order keeps lowering the residual error, so the highest order is best.',
     'Raising the AR order keeps lowering the residual error, so the highest order is best.', False,
     'Overfitting. Use AIC or FPE, which penalise the order.', 'That is overfitting. Use A I C or F P E, which penalise the order.'),
    ('Block 1 · Probability', 'WSS means the time averages equal the ensemble averages.', 'Wide sense stationary means the time averages equal the ensemble averages.', False,
     'That is ERGODICITY.', 'That is ergodicity, a different property.'),
    ('Block 1 · Probability', 'WSS = constant mean, and autocorrelation that depends only on the lag.',
     'Wide sense stationary means a constant mean, and an autocorrelation that depends only on the lag.', True,
     'The definition.', 'That is the definition.'),
    ('Block 1 · Probability', 'Infinitely many fair dice, each rolled forever: ergodic ONLY in the mean.',
     'Infinitely many fair dice, each rolled forever. The process is ergodic only in the mean.', False,
     'Ergodic in the mean AND the variance. Asked twice, same answer.', 'It is ergodic in both the mean and the variance. This was asked twice, with the same answer.'),
    ('Block 1 · Probability', r'$X[n]=A$, a random constant, is ergodic in the mean.', 'X of n equals A, a random constant. It is ergodic in the mean.', False,
     r'One row always averages to its own $A$, not to $E[A]$.', 'One realisation always averages to its own A, not to the expected value of A.'),
    ('Block 1 · Probability', r'$A$ and $B$ independent  $\Rightarrow$  $P(A\,|\,B)=P(A)$.', 'If A and B are independent, the probability of A given B equals the probability of A.', True,
     'Knowing B tells you nothing about A.', 'Knowing B tells you nothing about A.'),
    ('Block 1 · Probability', 'The innovation filter of a spectral factorisation must be minimum phase.',
     'The innovation filter of a spectral factorisation must be minimum phase.', True,
     'Poles and zeros inside the unit circle: keep the root with $|a|<1$.', 'Poles and zeros inside the unit circle. That is why you keep the root smaller than one.'),
    ('Block 1 · Probability', 'Zero covariance implies independence.', 'Zero covariance implies independence.', False,
     'Only the other way round: independent implies zero covariance.', 'Only the other way round. Independent implies zero covariance.'),
]


class Ep4Quiz(Pod):
    episode = 'Episode 4 · Rapid-fire true or false'
    sections = ['intro', 'quiz', 'outro']

    def intro(self):
        self.header('intro')
        self.say('T', "Episode four: rapid fire. The multiple choice questions in this exam recycle the same sentences, year after year, often with one word swapped. Maximise becomes minimise, mean becomes maximum.",
                 self.title_card('Rapid-fire true or false', f'{len(Q)} sentences the multiple-choice questions keep recycling',
                                 [chip('all four blocks', RED), chip('about 2 to 3 points', BLUE), chip('say your answer out loud', GREEN)]))
        self.say('T', "I read a sentence. You get three seconds. Say true or false out loud, then I give you the answer and the reason. Ben plays along.")
        self.say('S', "Three seconds. No pressure.")

    def quiz(self):
        last = None
        for i, (blk, shown, spoken, ok, why_s, why_t) in enumerate(Q):
            if blk != last:
                self.header(blk)
                last = blk
            num = MT(f'{i + 1} / {len(Q)}', 22, GREY).to_edge(UP, buff=0.75)
            st = MT(shown, 32)
            if st.width > 12.6:
                st.width = 12.6
            st.next_to(num, DOWN, buff=0.6)
            q = MT('True or false?', 26, PURPLE).next_to(st, DOWN, buff=0.45)
            self.say('T', spoken, self.wipe(0.3), [self.put(num, rt=0.4), self.put(st, rt=0.5)], self.put(q, rt=0.3), pause=0.1)
            bar = Rectangle(width=6, height=0.16, fill_color=ORANGE, fill_opacity=1, stroke_width=0).next_to(q, DOWN, buff=0.3)
            self.board.add(bar)
            self.add(bar)
            self.play(bar.animate(run_time=3, rate_func=lambda t: t).stretch(0.01, 0, about_edge=LEFT))
            v = chip('TRUE' if ok else 'FALSE', GREEN if ok else RED, 30)
            why = MT(why_s, 27, INK)
            if why.width > 12.6:
                why.width = 12.6
            VGroup(v, why).arrange(DOWN, buff=0.3).next_to(q, DOWN, buff=0.35)
            self.board.remove(bar)
            self.remove(bar)
            self.say('T', ('True. ' if ok else 'False. ') + why_t, [self.put(v, rt=0.3), self.put(why, rt=0.5)], pause=0.6)

    def outro(self):
        self.header('outro')
        r = card(['Count how many you got right.', 'Every one you missed: write the correct sentence on your A4 sheet.',
                  'Then do the True/False cards on the site (lessons 1.2, 1.3, 2.4, 3.3, 4.2).'], 28).move_to(UP * 0.5)
        self.say('S', "I got most of them. The window ones are evil.", self.wipe())
        self.say('T', "Count how many you got right. Every one you missed, write the correct sentence on your A4 sheet. Then do the true or false cards on the site, in lessons 1.2, 1.3, 2.4, 3.3 and 4.2. Replay this episode on Monday morning.",
                 self.put(r, rt=1.0))
