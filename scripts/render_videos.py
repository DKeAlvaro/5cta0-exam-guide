"""Render the Manim scenes of videos.py into docs/video/<snake_name>.mp4 (+ .jpg poster = last frame).

python scripts/render_videos.py                       # every scene, 720p30
python scripts/render_videos.py EnergyPower ZeroPad   # only these
python scripts/render_videos.py --last EnergyPower    # only the last frame, as PNG into $PREVIEW (quick check)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'docs', 'video')
MEDIA = os.path.join(tempfile.gettempdir(), 'ssp_guide_manim')


def snake(name):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', '_', name).lower()


def all_scenes():
    with open(os.path.join(HERE, 'videos.py'), encoding='utf-8') as f:
        block = re.search(r'SCENES = \[(.*?)\]', f.read(), re.S).group(1)
    return re.findall(r'\w+', block)


def manim(name, *flags):
    subprocess.run([sys.executable, '-m', 'manim', 'render', *flags, '--disable_caching', '--progress_bar', 'none',
                    '-v', 'WARNING', '--media_dir', MEDIA,
                    os.path.join(HERE, 'videos.py'), name], check=True, stdout=subprocess.DEVNULL)


def render(name):
    manim(name, '-qm')
    src = os.path.join(MEDIA, 'videos', 'videos', '720p30', name + '.mp4')
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, snake(name))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-c:v', 'libx264', '-crf', '30', '-preset', 'slow',
                    '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', dst + '.mp4'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-sseof', '-0.3', '-i', src, '-frames:v', '1', '-q:v', '4',
                    dst + '.jpg'], check=True)
    print('wrote', snake(name), f'{os.path.getsize(dst + ".mp4") / 1e6:.2f} MB', flush=True)


def last_frame(name):
    manim(name, '-ql', '-s')
    src = os.path.join(MEDIA, 'images', 'videos', name + '_ManimCE_v0.22.0.png')
    shutil.copy(src, os.path.join(os.environ.get('PREVIEW', tempfile.gettempdir()), 'v_' + snake(name) + '.png'))
    print('frame', name, flush=True)


if __name__ == '__main__':
    args = sys.argv[1:]
    quick = '--last' in args
    names = [a for a in args if not a.startswith('--')] or all_scenes()
    for n in names:
        (last_frame if quick else render)(n)
