"""Topic 0 song: the Relax video (vertical, 720x1280) rebuilt 16:9 for the projector.

The original video sits in the middle with its own captions. The left panel holds the title and Lee & Tee.
The right panel is a phase rail: the six parts of Morning Meeting, each lighting up while the song names it.

python3 music/00-our-morning-meeting/projector.py --src <relax.mp4> [--out out/00-our-morning-meeting/our-morning-meeting-song.mp4]
"""
import argparse, os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
IMG = os.path.join(ROOT, 'assets', 'img')
FONTS = os.path.join(ROOT, 'assets', 'fonts')

W, H = 1920, 1080
VW = 608                      # 720x1280 scaled to 1080 tall
VX = (W - VW) // 2
PAPER, CHAR, RED = '#FFF8EA', '#232323', '#E21C24'
COLORS = ['#1F8A4C', '#2F80ED', '#F28C28', '#F2B705', '#E21C24', '#2F80ED']

PARTS = [  # (art, EN move, ES, KR, phase name)
    ('class_breathe', 'Breathe', 'Respiro', 'Respire', 'Regulate'),
    ('mm_circle', 'Look', 'Miro', 'Gade', 'Orient'),
    ('talk', 'Listen', 'Escucho', 'Koute', 'Connect'),
    ('mm_try', 'Try', 'Lo intento', 'Eseye', 'Practice'),
    ('promise', 'Whisper my goal', 'Susurro mi meta', 'Di l tou ba', 'Commit'),
    ('leave', 'Move slow', 'Despacio', 'Dousman', 'Transition'),
]

# When each rail state shows (seconds). State 0 = no part lit, 1-6 = that part lit, 7 = all lit (outro).
# Times come from the on-screen captions of the source video (see lyrics.md).
WINDOWS = [
    (1, 16.0, 27.2), (2, 27.2, 38.4), (3, 61.4, 67.4), (4, 67.4, 77.0),
    (5, 94.6, 108.4), (6, 108.4, 115.5), (7, 115.5, 999),
]


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def rounded(im, r):
    m = Image.new('L', im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], r, fill=255)
    im.putalpha(m)
    return im


def cover(path, w, h, fy=0.4):
    im = Image.open(path).convert('RGB')
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def kente(d, y0, h):
    pat = [('#1F8A4C', 26), ('#F2B705', 14), ('#E21C24', 26), (CHAR, 6), ('#F2B705', 14), ('#F28C28', 26), (CHAR, 6)]
    x = 0
    while x < W:
        for c, w in pat:
            d.rectangle([x, y0, x + w, y0 + h], fill=c)
            x += w


def outlined(d, xy, text, f, fill, stroke=4, shadow=5):
    x, y = xy
    d.text((x + shadow, y + shadow), text, font=f, fill=CHAR, stroke_width=stroke, stroke_fill=CHAR)
    d.text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=CHAR)


def background():
    bg = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(bg)
    for gx in range(0, W, 48):
        d.line([gx, 0, gx, H], fill='#EAE6F2')
    for gy in range(0, H, 48):
        d.line([0, gy, W, gy], fill='#EAE6F2')
    kente(d, 0, 18)
    kente(d, H - 18, 18)
    # left panel: title, Lee & Tee, the instruction
    big = font('lilita.ttf', 96)
    outlined(d, (60, 70), 'OUR', big, RED)
    outlined(d, (60, 170), 'MORNING', big, RED)
    outlined(d, (60, 270), 'MEETING', big, RED)
    lt = Image.open(os.path.join(IMG, 'welcome.jpg')).convert('RGB')
    s = 560 / lt.width
    lt = lt.resize((560, round(lt.height * s)), Image.LANCZOS)
    lt = lt.crop((0, 0, 560, min(lt.height, 430)))
    card = Image.new('RGB', (580, lt.height + 20), CHAR)
    card.paste(lt, (10, 10))
    bg.paste(rounded(card, 26), (40, 400), rounded(card, 26))
    f = font('fred7.ttf', 40)
    d.rounded_rectangle([40, 870, 620, 1030], 28, fill='#1F8A4C', outline=CHAR, width=5)
    d.text((330, 950), 'Do the move\nwhen your part\nlights up!', font=f, fill='white', anchor='mm', align='center', spacing=4)
    # video frame shadow
    d.rectangle([VX - 6, 0, VX + VW + 6, H], fill=CHAR)
    return bg


def rail(state):
    """Transparent overlay with the six-part rail. state: 0 none lit, 1-6 one lit, 7 all lit."""
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    x0, x1 = VX + VW + 34, W - 34
    top, gap = 40, 12
    rh = (H - 2 * top - 5 * gap) // 6
    fen, fsm, fnum, fph = font('lilita.ttf', 46), font('fred7.ttf', 22), font('lilita.ttf', 54), font('fred7.ttf', 18)
    for i, (art, en, es, kr, ph) in enumerate(PARTS):
        lit = state == 7 or state == i + 1
        dim = state in range(1, 7) and not lit
        y = top + i * (rh + gap)
        col = COLORS[i]
        box = Image.new('RGBA', (x1 - x0, rh), (0, 0, 0, 0))
        b = ImageDraw.Draw(box)
        b.rounded_rectangle([0, 0, box.width - 1, rh - 1], 24, fill=col if lit else '#FFFFFF',
                            outline=CHAR, width=7 if lit else 4)
        # number badge
        b.ellipse([16, rh // 2 - 44, 104, rh // 2 + 44], fill=col if not lit else '#FFFFFF', outline=CHAR, width=4)
        b.text((60, rh // 2 + 2), str(i + 1), font=fnum, fill='#FFFFFF' if not lit else CHAR, anchor='mm')
        # picture
        ph_w, ph_h = 170, rh - 26
        pic = cover(os.path.join(IMG, art + '.jpg'), ph_w, ph_h, 0.35 if art != 'promise' else 0.15)
        frame = Image.new('RGB', (ph_w + 8, ph_h + 8), CHAR)
        frame.paste(pic, (4, 4))
        frame = rounded(frame, 16)
        box.alpha_composite(frame, (122, 9))
        tx = 122 + ph_w + 26
        txt = '#FFFFFF' if lit and col not in ('#F2B705',) else CHAR
        room = box.width - tx - 16
        fe = fen
        while b.textlength(en, font=fe) > room and fe.size > 30:
            fe = font('lilita.ttf', fe.size - 2)
        b.text((tx, 10), ph.upper(), font=fph, fill=txt)
        b.text((tx, 32), en, font=fe, fill=txt)
        b.text((tx, 92), f'ES  {es}', font=fsm, fill=txt)
        b.text((tx, 118), f'KR  {kr}', font=fsm, fill=txt)
        if dim:
            a = box.getchannel('A').point(lambda v: int(v * 0.38))
            box.putalpha(a)
        if lit and state != 7:
            glow = Image.new('RGBA', (box.width + 40, rh + 40), (0, 0, 0, 0))
            ImageDraw.Draw(glow).rounded_rectangle([20, 20, box.width + 19, rh + 19], 30, fill=col)
            glow = glow.filter(ImageFilter.GaussianBlur(12))
            ov.alpha_composite(glow, (x0 - 20, y - 20))
        ov.alpha_composite(box, (x0, y))
    return ov


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--out', default=os.path.join(ROOT, 'out', '00-our-morning-meeting', 'our-morning-meeting-song.mp4'))
    ap.add_argument('--preview', action='store_true', help='write rail state PNGs only')
    a = ap.parse_args()
    tmp = tempfile.mkdtemp()
    bg = background()
    bgp = os.path.join(tmp, 'bg.png'); bg.save(bgp)
    states = []
    for st in range(8):
        p = os.path.join(tmp, f'rail{st}.png'); rail(st).save(p); states.append(p)
        if a.preview:
            frame = bg.copy().convert('RGBA'); frame.alpha_composite(Image.open(p))
            frame.convert('RGB').save(os.path.join(os.path.dirname(a.out), f'rail-preview-{st}.jpg'), quality=85)
    if a.preview:
        return
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    inputs = ['-loop', '1', '-i', bgp, '-i', a.src]
    for p in states:
        inputs += ['-loop', '1', '-i', p]
    fc = [f'[1:v]scale={VW}:{H},setsar=1[v]', f'[0:v][v]overlay={VX}:0:shortest=1[b0]']
    last = 'b0'
    # state 0 (nothing lit) shows whenever no other window is active
    lit = '+'.join(f'between(t,{s},{e})' for _, s, e in WINDOWS)
    fc.append(f'[{last}][2:v]overlay=0:0:enable=\'not({lit})\'[b1]'); last = 'b1'
    for n, (st, s, e) in enumerate(WINDOWS, 2):
        fc.append(f'[{last}][{st + 2}:v]overlay=0:0:enable=\'between(t,{s},{e})\'[b{n}]'); last = f'b{n}'
    fc.append(f'[{last}]format=yuv420p[out]')
    cmd = ['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-map', '1:a',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-r', '30', '-c:a', 'aac', '-b:a', '160k',
           '-movflags', '+faststart', '-shortest', a.out]
    subprocess.run(cmd, check=True)
    print(a.out)


if __name__ == '__main__':
    main()
