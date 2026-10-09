#!/usr/bin/env python3
"""Captioned music video for one topic, from music/<slug>/mv.py (timing, lyrics, title) and its clips.

    python3 music/build_mv.py 07-gentle-hands                   # encode out/<slug>/<deck>-song.mp4
    python3 music/build_mv.py 07-gentle-hands --clips /path/to/clips
    python3 music/build_mv.py 07-gentle-hands --dry-run         # captions + ffmpeg command only, no encode

The video lands where build.py looks for the song (out/<slug>/<deck_slug>-song.mp4), so the next
`python3 build.py topics/<slug>.py` adds the deck's Play the song button, the page's Watch section, and the ZIP copy.
"""
import argparse, os, re, shlex, subprocess, sys, importlib.util
from PIL import Image, ImageDraw, ImageFont

MUSIC = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(MUSIC)
FONTS = os.path.join(KIT, 'assets', 'fonts')
FLAME = os.path.join(KIT, 'assets', 'matchbook-flame.png')
W, H = 1280, 720


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def wrap(txt, font, maxw):
    words = txt.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if font.getlength(t) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur); return lines


def captions(mv, cap):
    """Caption, logo bug, and title-card PNGs (transparent 1280x720 overlays)."""
    os.makedirs(cap, exist_ok=True)
    fb = ImageFont.truetype(os.path.join(FONTS, 'fred7.ttf'), 44)
    ft = ImageFont.truetype(os.path.join(FONTS, 'lilita.ttf'), 118)
    fl = ImageFont.truetype(os.path.join(FONTS, 'fred7.ttf'), 24)
    for i, (t, txt) in enumerate(mv.LYR):
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        lines = wrap(txt, fb, 1080); lh = 56; total = lh * len(lines)
        y0 = H - 40 - total
        pad = 18
        bw = max(fb.getlength(l) for l in lines) + 60
        d.rounded_rectangle(((W - bw) / 2, y0 - pad, (W + bw) / 2, y0 + total + pad - 6), radius=26, fill=(35, 35, 35, 200))
        for k, l in enumerate(lines):
            x = (W - fb.getlength(l)) / 2; y = y0 + k * lh
            for p in re.split(r'(\([^)]*\)?|[^(]*\))', l):     # echo parts (in parentheses) in yellow
                if not p:
                    continue
                col = (249, 220, 124) if p.startswith('(') or p.endswith(')') else (255, 255, 255)
                d.text((x, y), p, font=fb, fill=col, stroke_width=3, stroke_fill=(20, 20, 20))
                x += fb.getlength(p)
        im.save(os.path.join(cap, f'c{i:02d}.png'))
    logo = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(logo)
    fl_img = Image.open(FLAME).convert('RGBA'); fl_img.thumbnail((40, 44))
    d.rounded_rectangle((18, 16, 30 + fl_img.width + 10 + fl.getlength('MATCHBOOK LEARNING') + 22, 16 + 52), radius=26, fill=(255, 255, 255, 215))
    logo.alpha_composite(fl_img, (30, 20)); d.text((30 + fl_img.width + 10, 28), 'MATCHBOOK LEARNING', font=fl, fill=(35, 35, 35))
    logo.save(os.path.join(cap, 'logo.png'))
    title = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(title)
    tt = mv.TITLE; tw = ft.getlength(tt); x = (W - tw) / 2; y = 70
    d.text((x + 8, y + 8), tt, font=ft, fill=(35, 35, 35))
    d.text((x, y), tt, font=ft, fill=(226, 28, 36), stroke_width=5, stroke_fill=(35, 35, 35))
    sub = mv.SUBTITLE; sw = fl.getlength(sub)
    d.rounded_rectangle(((W - sw) / 2 - 16, y + 140, (W + sw) / 2 + 16, y + 178), radius=18, fill=(31, 138, 76))
    d.text(((W - sw) / 2, y + 145), sub, font=fl, fill=(255, 255, 255))
    title.save(os.path.join(cap, 'title.png'))
    if getattr(mv, 'TITLE_LAYOUT', 'overlay') == 'frame':
        opening(mv, cap)


FRAME = (248, 156, 784, 441)        # x, y, w, h of the framed video during the opening title


def opening(mv, cap):
    """Opening card for TITLE_LAYOUT='frame': the title sits on a paper band above a framed, smaller video,
    so the title never covers a face. Captions stay at the bottom as usual."""
    ft = ImageFont.truetype(os.path.join(FONTS, 'lilita.ttf'), 80)
    fl = ImageFont.truetype(os.path.join(FONTS, 'fred7.ttf'), 24)
    bg = Image.new('RGBA', (W, H), (255, 248, 236, 255)); d = ImageDraw.Draw(bg)
    for gx in range(0, W, 32):
        d.line((gx, 0, gx, H), fill=(240, 228, 208, 255))
    for gy in range(0, H, 32):
        d.line((0, gy, W, gy), fill=(240, 228, 208, 255))
    kente = [(226, 28, 36), (242, 183, 5), (31, 138, 76), (35, 35, 35), (242, 183, 5), (31, 138, 76)]
    for k, gx in enumerate(range(0, W, 40)):
        d.rectangle((gx, 0, gx + 40, 10), fill=kente[k % len(kente)])
        d.rectangle((gx, H - 10, gx + 40, H), fill=kente[(k + 3) % len(kente)])
    tt = mv.TITLE; tw = ft.getlength(tt); x = (W - tw) / 2; y = 12
    d.text((x + 6, y + 6), tt, font=ft, fill=(35, 35, 35))
    d.text((x, y), tt, font=ft, fill=(226, 28, 36), stroke_width=4, stroke_fill=(35, 35, 35))
    sub = mv.SUBTITLE; sw = fl.getlength(sub)
    d.rounded_rectangle(((W - sw) / 2 - 16, y + 90, (W + sw) / 2 + 16, y + 122), radius=16, fill=(31, 138, 76))
    d.text(((W - sw) / 2, y + 93), sub, font=fl, fill=(255, 255, 255))
    fx, fy, fw, fh = FRAME
    d.rounded_rectangle((fx - 12 + 10, fy - 12 + 10, fx + fw + 12 + 10, fy + fh + 12 + 10), radius=22, fill=(35, 35, 35, 255))
    d.rounded_rectangle((fx - 12, fy - 12, fx + fw + 12, fy + fh + 12), radius=22, fill=(255, 255, 255, 255), outline=(35, 35, 35, 255), width=4)
    bg.convert('RGB').save(os.path.join(cap, 'opening.png'))


def command(mv, clips, song, cap, out):
    beat = 60 / mv.BPM

    def snap(t):
        if t <= 0.05 or t >= mv.SNAP_UNTIL:
            return t
        k = round((t - mv.BEAT0) / beat); return round(mv.BEAT0 + k * beat, 3)

    END = mv.END
    inputs = []; fc = []; start = 0.0
    for n, (end, clip, src) in enumerate(mv.SEG):
        e = snap(end) if n < len(mv.SEG) - 1 else END
        dur = round(e - start, 3)
        assert src + dur <= mv.CLIP_LEN, f'segment {n} (clip {clip}) needs {src}+{dur}s, clips are {mv.CLIP_LEN}s'
        inputs += ['-i', os.path.join(clips, f'{clip}.mp4')]
        fc.append(f'[{n}:v]trim=start={src}:duration={dur},setpts=PTS-STARTPTS,scale={W}:{H},fps=24,format=yuv420p[v{n}]')
        start = e
    nseg = len(mv.SEG)
    fc.append(''.join(f'[v{n}]' for n in range(nseg)) + f'concat=n={nseg}:v=1:a=0[base]')
    idx = nseg
    inputs += ['-i', song]; aidx = idx; idx += 1
    inputs += ['-i', os.path.join(cap, 'logo.png')]; logo_i = idx; idx += 1
    inputs += ['-i', os.path.join(cap, 'title.png')]; title_i = idx; idx += 1
    cur = 'base'
    if getattr(mv, 'TITLE_LAYOUT', 'overlay') == 'frame':
        # opening: paper card with the title on top and the video framed underneath, then full frame
        fx, fy, fw, fh = FRAME
        inputs += ['-loop', '1', '-t', str(mv.TITLE_UNTIL + 0.5), '-i', os.path.join(cap, 'opening.png')]; open_i = idx; idx += 1
        fc.append(f'[base]split[bfull][bsm]')
        cx, cy, cw, ch = getattr(mv, 'OPENING_CROP', (0, 0, W, H))   # zoom into the opening clip (source px)
        fc.append(f'[bsm]trim=duration={mv.TITLE_UNTIL + 0.5},crop={cw}:{ch}:{cx}:{cy},scale={fw}:{fh}[small]')
        fc.append(f'[{open_i}:v]fps=24,format=yuv420p[obg]')
        fc.append(f'[obg][small]overlay={fx}:{fy}:shortest=1[open]')
        fc.append(f'[bfull][open]overlay=0:0:eof_action=pass:enable=\'lt(t,{mv.TITLE_UNTIL})\'[o_open]'); cur = 'o_open'
        fc.append(f'[{cur}][{logo_i}:v]overlay=0:0:enable=\'gte(t,{mv.TITLE_UNTIL})\'[o_t]'); cur = 'o_t'
    else:
        fc.append(f'[{cur}][{logo_i}:v]overlay=0:0[o_logo]'); cur = 'o_logo'
        fc.append(f'[{cur}][{title_i}:v]overlay=0:0:enable=\'between(t,0,{mv.TITLE_UNTIL})\'[o_t]'); cur = 'o_t'
    for i, (t, txt) in enumerate(mv.LYR):
        t2 = mv.LYR[i + 1][0] if i + 1 < len(mv.LYR) else END
        inputs += ['-i', os.path.join(cap, f'c{i:02d}.png')]
        fc.append(f'[{cur}][{idx}:v]overlay=0:0:enable=\'between(t,{t},{t2-0.04})\'[o{i}]'); cur = f'o{i}'; idx += 1
    fc.append(f'[{cur}]fade=t=in:st=0:d=0.4,fade=t=out:st={END-1.2}:d=1.2[vout]')
    fc.append(f'[{aidx}:a]atrim=0:{END},afade=t=out:st={END-1.5}:d=1.5[aout]')
    return (['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', '[aout]',
            '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
            '-movflags', '+faststart', out])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug', help='topic folder under music/, e.g. 07-gentle-hands')
    ap.add_argument('--clips', help='folder of NN.mp4 clips (default music/<slug>/<CLIPS from mv.py>)')
    ap.add_argument('--out', help='output mp4 (default out/<slug>/<deck_slug>-song.mp4)')
    ap.add_argument('--dry-run', action='store_true', help='write captions and print the ffmpeg command; do not encode')
    a = ap.parse_args()
    here = os.path.join(MUSIC, a.slug)
    mv = load(os.path.join(here, 'mv.py'), 'mv')
    clips = os.path.abspath(a.clips) if a.clips else os.path.join(here, getattr(mv, 'CLIPS', 'clips'))
    song = os.path.join(here, mv.SONG)
    work = os.path.join(KIT, 'out', a.slug, '_work', 'mv')
    cap = os.path.join(work, 'cap')
    if a.out:
        out = os.path.abspath(a.out)
    else:
        sys.path.insert(0, os.path.join(KIT, 'builder'))
        from common import load_topic, names
        out = os.path.join(KIT, 'out', a.slug, names(load_topic(os.path.join(KIT, 'topics', a.slug + '.py')))['song'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    captions(mv, cap)
    cmd = command(mv, clips, song, cap, out)
    print(f'captions: {cap} ({len(mv.LYR)} lines + logo + title)')
    if a.dry_run:
        print(' '.join(shlex.quote(c) for c in cmd))
        return
    missing = sorted({c for _, c, _ in mv.SEG if not os.path.exists(os.path.join(clips, f'{c}.mp4'))})
    if missing:
        sys.exit(f'missing clips in {clips}: {", ".join(m + ".mp4" for m in missing)}')
    subprocess.run(cmd, check=True)
    print(out)


if __name__ == '__main__':
    main()
