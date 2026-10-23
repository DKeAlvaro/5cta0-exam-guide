"""Render the episodes in order and mail each one to Alvaro (Windows send-mail, Gmail SMTP) as soon as it is done.

python scripts/podcast/run_all.py [Ep1Detection ...]      # default: all, in study-priority order
"""
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '..', 'docs', 'video')
SENDMAIL = r'C:\Users\Alvaro\bin\send-mail.py'
SITE = 'https://dkealvaro.github.io/5cta0-exam-guide/'
LIMIT = 24e6  # Gmail attachment cap is 25 MB

EPS = [
    ('Ep1Detection', 'Detection: the likelihood ratio test', 'e4-lrt.html',
     'Las dos hipótesis, P_FA / P_M / P_D, la receta de 5 pasos, April 2025 4a, el "flip" de Nov 2022, priors y costes (June 2026, el detector de IA), y las 3 frases del test.'),
    ('Ep2Spectral', 'Spectral estimation: correlogram, AR, MA', 'e3-corr.html',
     'Qué es r[k] y qué es una PSD, el correlograma término a término (June 2026), elegir el plot con theta=0 y pi, AR(1) (April 2025), AR(2) con Yule-Walker (June 2026) y MA(1).'),
    ('Ep3Estimation', 'Estimation: MLE and MAP', 'e2-mle.html',
     'La idea de likelihood, la receta de 4 pasos, April 2024 2c, el truco de la sigmoide, MAP con prior conjugado (Poisson+Gamma de June 2026, Beta) y las frases del test (MMSE, Fisher, CRLB).'),
    ('Ep4Quiz', 'Rapid-fire true or false (all blocks)', 'e2-facts.html',
     '34 frases de las que reciclan en los test, de los 4 bloques. Lee, 3 segundos para decir TRUE/FALSE en voz alta, respuesta y por qué. Repítelo el lunes por la mañana.'),
    ('Ep5Probability', 'Block 1: Bayes, joint PDFs, ergodic, factorisation', 'e1-bayes.html',
     'Bayes contando 1000 chips (June 2026), PDF conjunta dibujando la región (April 2024), WSS vs ergódico con los dados, y factorización espectral (April 2025).'),
]


def snake(name):
    import re
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '_', name).lower()


def dur(p):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                         capture_output=True, text=True).stdout
    return float(out or 0)


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def main():
    want = sys.argv[1:] or [e[0] for e in EPS]
    for i, (name, title, lesson, blurb) in enumerate(EPS, 1):
        if name not in want:
            continue
        t0 = time.time()
        log('render', name)
        r = subprocess.run([sys.executable, os.path.join(HERE, 'render.py'), name])
        if r.returncode:
            log('FAILED', name)
            continue
        mp4 = os.path.join(OUT, 'pod_' + snake(name) + '.mp4')
        att = mp4
        if os.path.getsize(mp4) > LIMIT:
            att = os.path.join(tempfile.gettempdir(), 'pod_' + snake(name) + '_mail.mp4')
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp4, '-vf', 'scale=-2:540', '-c:v', 'libx264', '-crf', '32',
                            '-preset', 'medium', '-c:a', 'aac', '-b:a', '64k', '-ac', '1', '-movflags', '+faststart', att], check=True)
        mins = dur(mp4) / 60
        body = (f'Episodio {i} de {len(EPS)} del podcast de 5CTA0 (en inglés, {mins:.0f} min): {title}.\n\n'
                f'{blurb}\n\n'
                'Cómo usarlo: cuando salga YOUR TURN en morado, contesta en voz alta (o en papel) antes de que acabe '
                'la cuenta atrás. Si necesitas más tiempo, pausa el vídeo. Escucharlo sin contestar sirve mucho menos.\n\n'
                f'Después, haz el "Your turn" de la lección en papel: {SITE}{lesson}\n\n'
                'Vídeo adjunto.\n')
        bf = os.path.join(tempfile.gettempdir(), 'pod_mail_body.txt')
        with open(bf, 'w', encoding='utf-8') as f:
            f.write(body)
        m = subprocess.run([sys.executable, SENDMAIL, f'5CTA0 podcast {i}/{len(EPS)} · {title}', bf, '-a', att])
        log('mailed' if m.returncode == 0 else 'MAIL FAILED', name, f'{os.path.getsize(att) / 1e6:.1f} MB',
            f'{mins:.1f} min video', f'{(time.time() - t0) / 60:.1f} min wall')
    log('ALLDONE')


if __name__ == '__main__':
    main()
