"""Render a podcast episode (Manim + voices) into docs/video/<snake_name>.mp4 with a .jpg poster.

python scripts/podcast/render.py Ep1Detection             # full episode, 720p30
POD_SECTIONS=intro,story python scripts/podcast/render.py --test Ep1Detection   # 480p, only those sections
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '..', 'docs', 'video')
MEDIA = os.path.join(tempfile.gettempdir(), 'ssp_pod_manim')


def snake(name):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '_', name).lower()


def source_of(name):
    for f in glob.glob(os.path.join(HERE, 'ep*.py')):
        if re.search(rf'^class {name}\(', open(f, encoding='utf-8').read(), re.M):
            return f
    raise SystemExit('no scene ' + name)


def main():
    args = sys.argv[1:]
    test = '--test' in args
    name = [a for a in args if not a.startswith('--')][0]
    src = source_of(name)
    q = '-ql' if test else '-qm'
    dry = ['--dry_run'] if '--dry' in args else []
    subprocess.run([sys.executable, '-m', 'manim', 'render', q, *dry, '--disable_caching', '--progress_bar', 'none',
                    '-v', 'WARNING', '--media_dir', MEDIA, src, name], check=True)
    if dry:
        print('dry run ok:', name)
        return
    res = '480p15' if test else '720p30'
    mp4 = os.path.join(MEDIA, 'videos', os.path.splitext(os.path.basename(src))[0], res, name + '.mp4')
    if test:
        print('test render:', mp4)
        return
    dst = os.path.join(OUT, 'pod_' + snake(name))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp4, '-c:v', 'libx264', '-crf', '28', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k', '-ac', '1', '-movflags', '+faststart',
                    dst + '.mp4'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '4', '-i', mp4, '-frames:v', '1', '-q:v', '4',
                    dst + '.jpg'], check=True)
    print('wrote', dst + '.mp4', f'{os.path.getsize(dst + ".mp4") / 1e6:.1f} MB', flush=True)


if __name__ == '__main__':
    main()
