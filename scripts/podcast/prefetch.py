"""Synthesise every line of every episode in parallel into the TTS cache, so rendering does not wait on the network.

python scripts/podcast/prefetch.py
"""
import ast
import asyncio
import glob
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge_tts  # noqa: E402
from podkit import AUD, VOICE  # noqa: E402


def lines_of(path):
    """(who, text) for every self.say('X', "literal") / self.think("literal") call in an episode file."""
    out = []
    for node in ast.walk(ast.parse(open(path, encoding='utf-8').read())):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ('say', 'think'):
            a = node.args
            if node.func.attr == 'say' and len(a) >= 2 and isinstance(a[0], ast.Constant) and isinstance(a[1], ast.Constant):
                out.append((a[0].value, a[1].value))
            if node.func.attr == 'think' and a and isinstance(a[0], ast.Constant):
                out.append(('T', a[0].value))
    return out


def quiz_lines():
    from ep4_quiz import Q
    out = []
    for _, _, spoken, ok, _, why in Q:
        out += [('T', spoken), ('T', ('True. ' if ok else 'False. ') + why)]
    return out


async def one(sem, who, text):
    voice, rate = VOICE[who][:2]
    key = hashlib.md5(f'{voice}|{rate}|{text}'.encode()).hexdigest()[:16]
    p = os.path.join(AUD, key + '.mp3')
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return 'cached'
    async with sem:
        for attempt in range(6):
            try:
                await edge_tts.Communicate(text, voice, rate=rate).save(p + '.part')
                if os.path.getsize(p + '.part') > 0:
                    os.replace(p + '.part', p)
                    return 'new'
            except Exception:
                pass
            await asyncio.sleep(1.5 * (attempt + 1))
    return 'FAILED: ' + text[:50]


async def main():
    jobs = []
    for f in sorted(glob.glob(os.path.join(HERE, 'ep*.py'))):
        jobs += lines_of(f)
    jobs += quiz_lines()
    jobs = list(dict.fromkeys(jobs))
    sem = asyncio.Semaphore(6)
    res = await asyncio.gather(*[one(sem, w, t) for w, t in jobs])
    print(len(jobs), 'lines:', res.count('cached'), 'cached,', res.count('new'), 'new')
    for r in res:
        if r.startswith('FAILED'):
            print(r)


if __name__ == '__main__':
    asyncio.run(main())
