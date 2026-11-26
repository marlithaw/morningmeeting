# Spark Week 8 scenes: Back and Ready (routines after the break, a calm testing day, new rooms, finishing strong). Winter touches.
from art2 import kid, text, bubble, flame, points, wall, svg, INK, RED, YEL, BLUE, GREEN, PURP, ORNG, PINK, TEAL
from art3 import banner, table, huddle

NAVY = '#0E2244'; ICE = '#D7ECFA'; CRAN = '#B3203B'


def flakes(pts, col='#FFFFFF', s=1.0):
    out = []
    for x, y in pts:
        out.append(f'<g transform="translate({x},{y}) scale({s})" stroke="{col}" stroke-width="3" stroke-linecap="round">'
                   '<path d="M0 -12 V12 M-10.4 -6 L10.4 6 M-10.4 6 L10.4 -6"/></g>')
    return ''.join(out)


def window(x=640, y=130, w=200, h=150):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#9FC6E8" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M{x + w / 2} {y} V{y + h} M{x} {y + h / 2} H{x + w}" stroke="{INK}" stroke-width="4"/>'
            f'<path d="M{x + 4} {y + h - 18} Q{x + w / 2} {y + h - 34} {x + w - 4} {y + h - 18} V{y + h - 4} H{x + 4} Z" fill="#fff"/>'
            + flakes([(x + 30, y + 30), (x + 80, y + 52), (x + 150, y + 28), (x + 120, y + 90), (x + 40, y + 100)], s=.6))


def huddle_br():
    s = huddle().replace(text(480, 36 + 40 + 34 * .36, 'STRONGER TOGETHER · MÁS FUERTES JUNTOS', 34, YEL),
                         text(480, 36 + 40 + 30 * .36, 'BACK AND READY · DE REGRESO Y LISTOS', 30, YEL))
    return s.replace('Every voice!', 'Welcome back!').replace('¡Cada voz!', '¡Bienvenidos!') + flakes([(60, 300), (870, 320), (40, 420), (880, 200)], col='#9FC6E8', s=.8)


# ---------------- Tuesday · Picture of the Day ----------------
def quiet_hall():
    b = [wall('#E8EEF5', '#C9B48E'), banner('HALLWAY · PASILLO', NAVY, '#fff', fs=36)]
    b.append(f'<rect x="620" y="140" width="170" height="290" fill="#7FB3E6" stroke="{INK}" stroke-width="6"/>'
             f'<rect x="636" y="170" width="138" height="96" rx="6" fill="#fff" stroke="{INK}" stroke-width="4"/>'
             + text(705, 205, 'TESTING', 26, CRAN) + text(705, 240, 'QUIET PLEASE', 18, NAVY))
    for i, (x, sk, c, h) in enumerate([(160, 0, PINK, 'puffs'), (300, 3, GREEN, 'fade'), (440, 1, ORNG, 'braids')]):
        b.append(kid(x, 480, .9, skin=sk, top=c, hair=h, pose='stand', face='smile'))
        b.append(f'<path d="M{x - 2} {480 - 186 * .9 + 4} v14" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    b.append(bubble(110, 150, 220, 60, 'Shhh… whisper walk', 22))
    return ''.join(b)


def test_desk():
    b = [wall('#EAF2FA', '#C9B48E'), window(660, 120, 200, 150)]
    b.append(table(80, 360, 500))
    b.append(f'<rect x="230" y="300" width="200" height="62" rx="6" fill="#CBD5E1" stroke="{INK}" stroke-width="4"/><rect x="246" y="310" width="168" height="44" fill="#BEE3F8"/>')
    b.append(kid(330, 480, 1.0, skin=2, top=BLUE, hair='curly', pose='tray', face='flat'))
    b.append(''.join(f'<circle cx="{330 + dx}" cy="{250 - dy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" opacity=".7"/>' for dx, dy, r in ((-60, 0, 12), (-84, 26, 18), (-112, 56, 24))))
    b.append(f'<rect x="40" y="110" width="300" height="76" rx="30" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(190, 156, 'Breathe. Reread. I can try.', 22, fam='Andika,sans-serif'))
    b.append(kid(760, 480, .85, skin=4, top=GREEN, hair='braids', pose='tray', face='smile', flip=True))
    return ''.join(b)


def plan_card():
    b = [wall('#EAF2FA', '#C9B48E'), window(680, 90, 180, 130)]
    b.append(table(60, 400, 560))
    b.append(f'<g transform="translate(330,230) rotate(-2)"><rect x="-250" y="-170" width="500" height="330" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             + text(0, -126, 'MY TEST-DAY PLAN', 30, CRAN)
             + text(-226, -78, 'BEFORE: 3 slow breaths', 22, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(-226, -34, 'DURING: reread, cross out,', 22, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(-140, 0, 'skip and come back', 22, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(-226, 44, 'AFTER: check my work,', 22, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(-140, 78, 'then stay silent', 22, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(120, 128, 'by Sofia', 22, BLUE, anchor='start', fam='Andika,sans-serif') + '</g>')
    b.append(kid(790, 500, .8, skin=1, top=PURP, hair='hijab', pose='point', flip=True))
    return ''.join(b)


def silent_finish():
    b = [wall('#E3ECF6', '#C9B48E'), banner('TESTING · DO NOT DISTURB', NAVY, YEL, fs=32)]
    b.append(table(60, 360, 340) + table(500, 360, 340))
    b.append(kid(230, 480, .95, skin=3, top=TEAL, hair='fade', pose='tray', face='smile'))
    b.append(f'<rect x="290" y="338" width="70" height="22" fill="#F6E3A8" stroke="{INK}" stroke-width="3"/><path d="M325 338 V360" stroke="{INK}" stroke-width="2"/>')
    b.append(kid(670, 480, .95, skin=0, top=CRAN, hair='puffs', pose='tray', face='flat', flip=True))
    b.append(f'<rect x="540" y="318" width="96" height="42" rx="5" fill="#CBD5E1" stroke="{INK}" stroke-width="4"/><rect x="550" y="326" width="76" height="28" fill="#BEE3F8"/>')
    b.append(bubble(70, 150, 300, 60, 'Done. Checked. Silent.', 22))
    b.append(f'<g transform="translate(450,250)">{flakes([(0, 0)], col="#9FC6E8", s=1.4)}</g>')
    return ''.join(b)


# ---------------- Wednesday · Zoom In ----------------
def routines_door():
    b = [wall('#E8EEF5', '#C9B48E'), banner('ROOM 63 · SALÓN 63', NAVY, '#fff', fs=36)]
    b.append(f'<rect x="80" y="150" width="170" height="280" fill="#7FB3E6" stroke="{INK}" stroke-width="6"/><circle cx="230" cy="300" r="9" fill="{YEL}" stroke="{INK}" stroke-width="3"/>')
    b.append(f'<rect x="520" y="140" width="330" height="250" rx="10" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             + text(685, 182, 'OUR ROUTINES', 28, CRAN)
             + text(540, 224, 'Enter: greet · seat · start', 20, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(540, 262, 'Supplies: bin by the window', 20, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(540, 300, 'Hand up to speak', 20, NAVY, anchor='start', fam='Andika,sans-serif')
             + text(685, 356, 'SAFE · RESPECTFUL · RESPONSIBLE', 17, BLUE))
    b.append(kid(330, 480, .9, skin=2, top=GREEN, hair='curly', pose='wave', face='smile'))
    b.append(kid(430, 490, 1.08, skin=4, top=PURP, hair='locs', pose='wave', face='smile', flip=True))
    b.append(bubble(250, 150, 230, 60, 'Good morning!', 24, 'right'))
    b.append(flakes([(870, 110), (500, 110), (40, 120)], col='#9FC6E8', s=.8))
    return ''.join(b)


# ---------------- Thursday · Would You Rather ----------------
def wyr_br(kind):
    b = [f'<rect width="900" height="560" fill="#EAF2FA"/>' + flakes([(450, 40), (450, 520), (20, 280), (880, 280)], col='#9FC6E8', s=.9)]

    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{CRAN}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="#CFE7F8" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 24, NAVY)}</g>')
    if kind == 'k1':
        a = kid(205, 390, .95, skin=0, top=PINK, hair='puffs', pose='stand', face='smile') + f'<path d="M203 222 v14" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>' + text(205, 110, 'WHISPER WALK', 26, BLUE)
        bb = kid(205, 400, .95, skin=3, top=GREEN, hair='fade', pose='both', face='smile') + text(205, 110, 'TIPTOE WALK', 26, GREEN)
        b.append(panel(30, 'WHISPER WALK', a, 'A') + panel(460, 'TIPTOE WALK', bb, 'B'))
    elif kind == '23':
        a = f'<rect x="80" y="120" width="250" height="230" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(205, 170, '#1 HARDEST', 28, CRAN) + ''.join(f'<path d="M100 {210 + i * 34} H310" stroke="#A0AEC0" stroke-width="4"/>' for i in range(4))
        bb = f'<rect x="80" y="120" width="250" height="230" fill="#fff" stroke="{INK}" stroke-width="4"/>' + ''.join(f'<path d="M100 {150 + i * 34} H310" stroke="#A0AEC0" stroke-width="4"/>' for i in range(4)) + text(205, 330, 'HARDEST LAST', 28, BLUE)
        b.append(panel(30, 'HARDEST FIRST', a, 'A') + panel(460, 'HARDEST LAST', bb, 'B'))
    elif kind == '45':
        a = kid(205, 400, 1.0, skin=1, top=ORNG, hair='ponytail', pose='both', face='smile') + text(205, 110, 'QUICK STRETCH', 26, GREEN)
        bb = table(60, 300, 290) + kid(205, 390, .9, skin=5, top=PURP, hair='hijab', pose='tray', face='flat') + text(205, 110, 'PUSH THROUGH', 26, CRAN)
        b.append(panel(30, 'STRETCH BREAK', a, 'A') + panel(460, 'PUSH STRAIGHT THROUGH', bb, 'B'))
    else:
        a = ''.join(kid(90 + i * 115, 390, .7, skin=i, top=[TEAL, CRAN, BLUE][i], hair=['fade', 'puffs', 'locs'][i], pose='stand', face='smile') for i in range(3)) + text(205, 110, 'STUDY GROUP', 28, BLUE)
        bb = kid(205, 390, .95, skin=4, top='#4A5568', hair='cap', pose='tray', face='flat') + f'<rect x="160" y="282" width="90" height="56" fill="#F6E3A8" stroke="{INK}" stroke-width="3"/>' + text(205, 110, 'SOLO', 28, CRAN)
        b.append(panel(30, 'STUDY WITH A GROUP', a, 'A') + panel(460, 'STUDY ALONE', bb, 'B'))
    return ''.join(b)


HUDDLE = huddle_br
WYR = wyr_br
TUE = {'k1': quiet_hall, '23': test_desk, '45': plan_card, '68': silent_finish}
WED = {'k1': routines_door, '23': routines_door, '45': routines_door, '68': routines_door}
