#!/usr/bin/env python3
"""Vertical shorts (1080x1920) built from a topic's song, clips, and level art. No Matchbook logo or intro.

    python3 music/build_short.py 11-right-size-voice hook --clips /home/claude/mv_rv/clips
    python3 music/build_short.py 11-right-size-voice all  --clips ... --out DIR

Each short is a dict in music/<slug>/shorts.py (SHORTS). Layout, top to bottom:
    title band (y 120-390), the 16:9 clip in a white frame (40,420 1000x562, never cropped),
    the credit line, a 0-4 voice meter or a badge, then big captions (y 1210-1470).
Everything sits inside x 40-930 below the frame so the Shorts buttons (right edge) and the channel text
(bottom 420 px) never cover it.

Spec keys
    title, sub              title band text
    audio   [('song', a, b) | ('beat', bars)]  played back to back; 'beat' is a lyric-free drum bed at the song tempo
    clips   [(dur, clip, src_in)]              back to back inside the frame; total must match the audio
    captions [(t0, t1, text)]                  (parentheses) drawn yellow, like the music videos
    badges  [(t0, t1, text, color)]            pill in the meter slot
    meter   [(t0, t1, level|None)]             0-4 voice meter; None shows it with nothing lit
    counts  [(t0, t1, n)]                      countdown bubble on the clip's top right
    reveals [(t0, t1, level, label)]           answer card over the clip: level art, big number, label
    sfx     [('tick'|'chime', t)]
"""
import argparse, os, re, subprocess, sys, importlib.util
import numpy as np
from PIL import Image, ImageDraw, ImageFont

MUSIC = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(MUSIC)
FONTS = os.path.join(KIT, 'assets', 'fonts')
IMG = os.path.join(KIT, 'assets', 'img')
W, H = 1080, 1920
FX, FY, FW, FH = 40, 420, 1000, 562          # clip frame
SR = 48000
INK = (29, 29, 31); PAPER = (255, 248, 234); RED = (226, 28, 36); YEL = (249, 220, 124); GRN = (31, 138, 76)
LEVEL_COL = [(47, 128, 237), (31, 138, 76), (242, 183, 5), (242, 140, 40), (226, 28, 36)]
LEVEL_NAME = ['Lips closed', 'Whisper', 'Table talk', 'Whole room', 'Outside']
CREDIT = 'Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.'


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def wrap(txt, f, maxw):
    words = txt.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if f.getlength(t) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur); return lines


def layer():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); return im, ImageDraw.Draw(im)


def centered(d, cx, y, txt, f, fill, stroke=0, sfill=INK, shadow=0):
    x = cx - f.getlength(txt) / 2
    if shadow:
        d.text((x + shadow, y + shadow), txt, font=f, fill=INK)
    d.text((x, y), txt, font=f, fill=fill, stroke_width=stroke, stroke_fill=sfill)


# ---------- layers ----------
def background(s, path):
    im = Image.new('RGBA', (W, H), PAPER + (255,)); d = ImageDraw.Draw(im)
    for g in range(0, W, 36):
        d.line((g, 0, g, H), fill=(240, 228, 208, 255))
    for g in range(0, H, 36):
        d.line((0, g, W, g), fill=(240, 228, 208, 255))
    kente = [RED, (242, 183, 5), GRN, INK, (242, 183, 5), GRN]
    for k, gx in enumerate(range(0, W, 45)):
        d.rectangle((gx, 0, gx + 45, 16), fill=kente[k % 6])
        d.rectangle((gx, H - 16, gx + 45, H), fill=kente[(k + 3) % 6])
    ft = font('lilita.ttf', 132)
    while ft.getlength(s['title']) > 980:
        ft = font('lilita.ttf', ft.size - 6)
    centered(d, W / 2, 150, s['title'], ft, RED, stroke=6, shadow=9)
    fs = font('fred7.ttf', 40); sw = fs.getlength(s['sub'])
    d.rounded_rectangle((W / 2 - sw / 2 - 26, 312, W / 2 + sw / 2 + 26, 372), radius=30, fill=GRN)
    centered(d, W / 2, 318, s['sub'], fs, (255, 255, 255))
    d.rounded_rectangle((FX - 14 + 12, FY - 14 + 12, FX + FW + 14 + 12, FY + FH + 14 + 12), radius=28, fill=INK)
    d.rounded_rectangle((FX - 14, FY - 14, FX + FW + 14, FY + FH + 14), radius=28, fill=(255, 255, 255), outline=INK, width=5)
    fc = font('fred7.ttf', 21)
    centered(d, W / 2, FY + FH + 26, CREDIT, fc, (110, 100, 90))
    im.convert('RGB').save(path)


def caption(txt, path):
    im, d = layer(); f = font('fred7.ttf', 62)
    lines = wrap(txt, f, 880); lh = 78; total = lh * len(lines)
    y0 = 1340 - total / 2; bw = max(f.getlength(l) for l in lines) + 70; cx = 485
    d.rounded_rectangle((cx - bw / 2, y0 - 22, cx + bw / 2, y0 + total + 14), radius=34, fill=INK + (225,))
    for k, l in enumerate(lines):
        x = cx - f.getlength(l) / 2; y = y0 + k * lh
        for p in re.split(r'(\([^)]*\)?|[^(]*\))', l):
            if not p:
                continue
            col = YEL if p.startswith('(') or p.endswith(')') else (255, 255, 255)
            d.text((x, y), p, font=f, fill=col, stroke_width=3, stroke_fill=(20, 20, 20)); x += f.getlength(p)
    im.save(path)


def badge(txt, color, path):
    im, d = layer(); f = font('lilita.ttf', 60); bw = f.getlength(txt) + 80; cx = 485; y = 1062
    d.rounded_rectangle((cx - bw / 2 + 8, y + 8, cx + bw / 2 + 8, y + 98), radius=45, fill=INK)
    d.rounded_rectangle((cx - bw / 2, y, cx + bw / 2, y + 90), radius=45, fill=color, outline=INK, width=5)
    tc = INK if color == YEL else (255, 255, 255)
    centered(d, cx, y + 10, txt, f, tc)
    im.save(path)


def meter(level, path):
    im, d = layer(); f = font('lilita.ttf', 58); fl = font('fred7.ttf', 24)
    x0, y, pw, gap = 55, 1052, 160, 18
    for n in range(5):
        x = x0 + n * (pw + gap); on = level == n
        col = LEVEL_COL[n]
        if on:
            d.rounded_rectangle((x - 8, y - 8, x + pw + 8, y + 118), radius=26, fill=INK)
        fill = col if on else (255, 255, 255)
        d.rounded_rectangle((x, y, x + pw, y + 110), radius=22, fill=fill, outline=col if not on else INK, width=5)
        tc = (255, 255, 255) if on else col
        centered(d, x + pw / 2, y + 4, str(n), f, tc, stroke=3 if on else 0)
        centered(d, x + pw / 2, y + 76, LEVEL_NAME[n], fl, tc if on else INK)
    im.save(path)


def count(n, path):
    im, d = layer(); r = 112; cx, cy = FX + FW - r - 26, FY + r + 26
    d.ellipse((cx - r + 8, cy - r + 8, cx + r + 8, cy + r + 8), fill=INK)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED, outline=(255, 255, 255), width=10)
    f = font('lilita.ttf', 160); centered(d, cx, cy - 98, str(n), f, (255, 255, 255))
    im.save(path)


def reveal(level, label, path):
    im, d = layer()
    d.rounded_rectangle((FX, FY, FX + FW, FY + FH), radius=14, fill=(255, 255, 255))
    art = Image.open(os.path.join(IMG, f'vl_{level}.jpg')).convert('RGBA')
    art = art.resize((int(art.width * (FH - 20) / art.height), FH - 20), Image.LANCZOS)
    im.alpha_composite(art, (FX + 40, FY + 10))
    cx = FX + 40 + art.width + (FW - 40 - art.width) / 2; r = 140; cy = FY + 200
    d.ellipse((cx - r + 10, cy - r + 10, cx + r + 10, cy + r + 10), fill=INK)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=LEVEL_COL[level], outline=INK, width=6)
    centered(d, cx, cy - 128, str(level), font('lilita.ttf', 230), (255, 255, 255), stroke=5)
    fl = font('lilita.ttf', 70)
    for k, l in enumerate(wrap(label, fl, 470)):
        centered(d, cx, cy + 165 + k * 80, l, fl, INK)
    im.save(path)


# ---------- audio ----------
def song_pcm(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def beat_bed(bars, bpm):
    """Lyric-free kids hip hop drum bed: kick, claps on 2 and 4, eighth-note hats."""
    beat = 60 / bpm; n = int(round(bars * 4 * beat * SR)); out = np.zeros(n, np.float32)
    rng = np.random.default_rng(7)

    def put(snd, t):
        i = int(t * SR); j = min(n, i + len(snd)); out[i:j] += snd[:j - i]
    t = np.arange(int(0.35 * SR)) / SR
    kick = np.sin(2 * np.pi * (45 * t + (110 / 18) * (1 - np.exp(-18 * t)))) * np.exp(-9 * t) * 0.9
    tc = np.arange(int(0.22 * SR)) / SR
    noise = rng.standard_normal(len(tc)).astype(np.float32)
    noise = np.convolve(noise, np.ones(3) / 3, 'same') - np.convolve(noise, np.ones(40) / 40, 'same')
    env = np.zeros(len(tc))
    for off in (0, 0.012, 0.024):
        env += np.where(tc >= off, np.exp(-28 * np.clip(tc - off, 0, None)), 0)
    clap = noise * env * 0.32
    th = np.arange(int(0.05 * SR)) / SR
    hn = rng.standard_normal(len(th)); hn = hn - np.convolve(hn, np.ones(6) / 6, 'same')
    hat = hn * np.exp(-70 * th) * 0.12
    for b in range(bars):
        s0 = b * 4 * beat
        for k in (0, 1.5, 2, 3.5 if b % 2 else 2.75):
            put(kick, s0 + k * beat)
        for k in (1, 3):
            put(clap, s0 + k * beat)
        for k in range(8):
            put(hat * (1.0 if k % 2 else 0.6), s0 + k * beat / 2)
    return np.stack([out, out], 1) * 0.8


def sfx(kind):
    if kind == 'tick':
        t = np.arange(int(0.12 * SR)) / SR
        s = (np.sin(2 * np.pi * 1250 * t) + 0.5 * np.sin(2 * np.pi * 2500 * t)) * np.exp(-40 * t) * 0.35
    else:
        t = np.arange(int(1.2 * SR)) / SR
        s = sum(np.sin(2 * np.pi * f * t) * np.exp(-3.5 * t) * a for f, a in ((1046.5, .3), (1318.5, .25), (1568, .22), (2093, .12)))
        s[: int(0.09 * SR)] *= 0.6
    return np.stack([s, s], 1).astype(np.float32)


def build_audio(s, song, bpm, out):
    parts = []; fade = int(0.02 * SR)
    for p in s['audio']:
        if p[0] == 'song':
            seg = song[int(p[1] * SR):int(p[2] * SR)].copy()
        else:
            seg = beat_bed(p[1], bpm)
        seg[:fade] *= np.linspace(0, 1, fade)[:, None]; seg[-fade:] *= np.linspace(1, 0, fade)[:, None]
        parts.append(seg)
    a = np.concatenate(parts)
    for kind, t in s.get('sfx', []):
        x = sfx(kind); i = int(t * SR); j = min(len(a), i + len(x)); a[i:j] += x[:j - i]
    fo = int(0.6 * SR); a[-fo:] *= np.linspace(1, 0, fo)[:, None]
    a = np.clip(a, -1, 1)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-i', '-', out],
                   input=a.astype(np.float32).tobytes(), check=True)
    return len(a) / SR


# ---------- video ----------
def build(slug, name, s, clips, outdir, bpm):
    work = os.path.join(KIT, 'out', slug, '_work', 'shorts', name); os.makedirs(work, exist_ok=True)
    here = os.path.join(MUSIC, slug)
    song = song_pcm(os.path.join(here, 'song-source.mp4'))
    wav = os.path.join(work, 'audio.wav'); dur = build_audio(s, song, bpm, wav)
    vdur = sum(c[0] for c in s['clips'])
    assert abs(vdur - dur) < 0.05, f'{name}: clips {vdur:.2f}s vs audio {dur:.2f}s'
    background(s, os.path.join(work, 'bg.png'))
    layers = []                                   # (png, t0, t1)
    for i, (t0, t1, txt) in enumerate(s.get('captions', [])):
        p = os.path.join(work, f'cap{i:02d}.png'); caption(txt, p); layers.append((p, t0, t1))
    for i, (t0, t1, lv) in enumerate(s.get('meter', [])):
        p = os.path.join(work, f'met{i:02d}.png'); meter(lv, p); layers.append((p, t0, t1))
    for i, (t0, t1, txt, col) in enumerate(s.get('badges', [])):
        p = os.path.join(work, f'bad{i:02d}.png'); badge(txt, col, p); layers.append((p, t0, t1))
    for i, (t0, t1, n) in enumerate(s.get('counts', [])):
        p = os.path.join(work, f'cnt{i:02d}.png'); count(n, p); layers.append((p, t0, t1))
    for i, (t0, t1, lv, lab) in enumerate(s.get('reveals', [])):
        p = os.path.join(work, f'rev{i:02d}.png'); reveal(lv, lab, p); layers.append((p, t0, t1))
    inputs = ['-loop', '1', '-framerate', '30', '-t', f'{dur:.3f}', '-i', os.path.join(work, 'bg.png')]
    fc = []
    for n, (d, clip, src) in enumerate(s['clips']):
        assert src + d <= 8.05, f'{name}: clip {clip} needs {src}+{d}s'
        inputs += ['-i', os.path.join(clips, f'{clip}.mp4')]
        fc.append(f'[{n + 1}:v]trim=start={src}:duration={d},setpts=PTS-STARTPTS,fps=30,'
                  f'scale={FW}:{FH}:flags=lanczos,format=yuv420p[c{n}]')
    nc = len(s['clips'])
    fc.append(''.join(f'[c{n}]' for n in range(nc)) + f'concat=n={nc}:v=1:a=0[clip]')
    fc.append(f'[0:v]format=yuv420p[bg];[bg][clip]overlay={FX}:{FY}:shortest=1[v0]')
    cur = 'v0'; idx = nc + 1
    for k, (p, t0, t1) in enumerate(layers):
        inputs += ['-i', p]
        fc.append(f"[{cur}][{idx}:v]overlay=0:0:enable='between(t,{t0},{t1 - 0.02})'[l{k}]"); cur = f'l{k}'; idx += 1
    inputs += ['-i', wav]
    fc.append(f'[{cur}]fade=t=in:st=0:d=0.15,fade=t=out:st={dur - 0.5}:d=0.5[vout]')
    out = os.path.join(outdir, f'{slug}-short-{name}.mp4')
    cmd = (['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', f'{idx}:a',
           '-t', f'{dur:.3f}', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', '30',
           '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
    subprocess.run(cmd, check=True)
    print(f'{out}  ({dur:.1f} s)')
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug'); ap.add_argument('name', help="a key in SHORTS, or 'all'")
    ap.add_argument('--clips', required=True); ap.add_argument('--out')
    a = ap.parse_args()
    here = os.path.join(MUSIC, a.slug)
    spec = load(os.path.join(here, 'shorts.py'), 'shorts'); mv = load(os.path.join(here, 'mv.py'), 'mv')
    outdir = os.path.abspath(a.out or os.path.join(KIT, 'out', a.slug, 'shorts')); os.makedirs(outdir, exist_ok=True)
    names = list(spec.SHORTS) if a.name == 'all' else [a.name]
    for n in names:
        build(a.slug, n, spec.SHORTS[n], os.path.abspath(a.clips), outdir, mv.BPM)


if __name__ == '__main__':
    main()
