# Spark Week 7 scenes: Thankful Together (gratitude in places students know).
from art2 import kid, text, bubble, flame, points, wall, svg, INK, RED, YEL, BLUE, GREEN, PURP, ORNG, PINK, TEAL
from art3 import banner, table, huddle


def huddle_tt():
    s = huddle().replace(text(480, 36 + 40 + 34 * .36, 'STRONGER TOGETHER · MÁS FUERTES JUNTOS', 34, YEL), text(480, 36 + 40 + 28 * .36, 'THANKFUL TOGETHER · AGRADECIDOS JUNTOS', 28, YEL))
    return s.replace('Every voice!', 'Thank you!').replace('¡Cada voz!', '¡Gracias!')


def door(x=640, y=110, w=170, h=320):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#7FB3E6" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x+24}" y="{y+30}" width="{w-48}" height="90" fill="#DCEBFA" stroke="{INK}" stroke-width="4"/>'
            f'<circle cx="{x+24}" cy="{y+h/2+20}" r="9" fill="{YEL}" stroke="{INK}" stroke-width="3"/>')


# ---------------- Tuesday · Picture of the Day ----------------
def hold_door():
    b = [wall('#F3E3C3', '#C9A979'), banner('ROOM 63 · SALÓN 63', BLUE, '#fff', fs=36)]
    b.append(door(560, 140, 150, 290))
    b.append(kid(500, 480, 1.0, skin=2, top=GREEN, hair='curly', pose='point', face='smile'))
    b.append(kid(760, 480, 1.0, skin=0, top=PINK, hair='puffs', pose='tray', face='open', flip=True))
    b.append(f'<rect x="724" y="360" width="70" height="44" rx="4" fill="{ORNG}" stroke="{INK}" stroke-width="3"/><rect x="730" y="340" width="58" height="22" rx="3" fill="{BLUE}" stroke="{INK}" stroke-width="3"/>')
    b.append(bubble(600, 150, 260, 64, 'Thank you!', 28, 'right'))
    b.append(kid(170, 480, .9, skin=4, top=YEL, hair='fade', pose='stand'))
    return ''.join(b)


def lunch_line():
    b = [wall('#EFE2C8', '#C9A979'), banner('CAFETERIA · CAFETERÍA', GREEN, '#fff', fs=38)]
    b.append(kid(660, 400, .8, skin=1, top='#fff', hair='cap', pose='hold', flip=True))
    b.append(f'<rect x="420" y="250" width="440" height="110" rx="8" fill="#CBD5E1" stroke="{INK}" stroke-width="5"/>'
             + ''.join(f'<rect x="{440+i*104}" y="270" width="88" height="44" rx="6" fill="{c}" stroke="{INK}" stroke-width="3"/>' for i, c in enumerate(['#F6E05E', '#9AE6B4', '#FBD38D', '#FEB2B2'])))
    b.append(kid(300, 480, 1.05, skin=3, top=RED, hair='braids', pose='tray', face='open'))
    b.append(f'<rect x="250" y="370" width="100" height="16" rx="4" fill="#A0AEC0" stroke="{INK}" stroke-width="3"/>')
    b.append(kid(120, 480, .9, skin=0, top=BLUE, hair='fade', pose='stand'))
    b.append(bubble(150, 150, 300, 64, 'Thank you for lunch!', 24))
    return ''.join(b)


def note_desk():
    b = [wall('#EFE2C8', '#C9A979')]
    b.append(table(60, 380, 520))
    b.append(f'<g transform="translate(320,220) rotate(-3)"><rect x="-210" y="-170" width="420" height="300" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             + text(-180, -122, 'Dear math buddy,', 26, BLUE, anchor='start', fam='Andika,sans-serif')
             + text(-180, -76, 'Thank you for explaining', 24, anchor='start', fam='Andika,sans-serif')
             + text(-180, -40, 'fractions with the pizza model.', 24, anchor='start', fam='Andika,sans-serif')
             + text(-180, -4, 'It helped me finish number 4', 24, anchor='start', fam='Andika,sans-serif')
             + text(-180, 32, 'on my own!', 24, anchor='start', fam='Andika,sans-serif')
             + text(-180, 90, 'From, Lucia', 24, RED, anchor='start', fam='Andika,sans-serif') + '</g>')
    b.append(f'<rect x="640" y="70" width="220" height="200" rx="10" fill="{YEL}" stroke="{INK}" stroke-width="4"/>' + text(750, 112, 'A STRONG', 24, RED) + text(750, 142, 'THANK-YOU', 24, RED)
             + text(660, 186, '1. What you did', 20, anchor='start') + text(660, 220, '2. How it helped', 20, anchor='start'))
    b.append(kid(760, 480, .9, skin=2, top=TEAL, hair='ponytail', pose='point', flip=True))
    return ''.join(b)


def unseen_work():
    b = [wall('#E8DCC6', '#C7AE86'), banner('HALLWAY · 6:00 P.M.', INK, YEL, fs=36)]
    b.append(f'<rect x="60" y="150" width="120" height="280" fill="#9FB3C8" stroke="{INK}" stroke-width="5"/>' + ''.join(f'<rect x="{70+i*36}" y="{170}" width="28" height="250" fill="#CBD5E1" stroke="{INK}" stroke-width="2"/>' for i in range(3)))
    b.append(kid(400, 480, 1.0, skin=4, top=BLUE, hair='fade', pose='hold', face='smile'))
    b.append(f'<path d="M488 352 L540 470" stroke="#8B5A2B" stroke-width="8"/><path d="M520 470 h50 l-6 12 h-40 z" fill="#E2E8F0" stroke="{INK}" stroke-width="3"/>')
    b.append(f'<path d="M640 470 L675 360 L710 470 Z" fill="{YEL}" stroke="{INK}" stroke-width="4"/>' + text(675, 440, '!', 40, RED))
    b.append(f'<ellipse cx="560" cy="500" rx="120" ry="18" fill="#BEE3F8" opacity=".8"/>')
    b.append(kid(800, 480, .9, skin=0, top=RED, hair='locs', pose='wave', face='open', flip=True))
    b.append(bubble(600, 150, 270, 64, 'Appreciate you!', 26, 'right'))
    return ''.join(b)


# ---------------- Wednesday · Zoom In ----------------
NOTES = [
    (70, 150, '#FEF08A', 'Thank you, bus', 'drivers, for safe', 'rides!'),
    (270, 150, '#BBF7D0', 'Thank you for', 'breakfast every', 'morning!'),
    (470, 150, '#BFDBFE', 'Thank you,', 'custodians, for', 'a clean room.'),
    (670, 150, '#FBCFE8', 'Thanks to my', 'reading buddy', 'for helping me.'),
    (170, 310, '#FED7AA', 'Thank you, nurse,', 'for helping me', 'feel better.'),
    (370, 310, '#DDD6FE', 'Thank you,', 'front office, for', 'calling home.'),
    (570, 310, '#FEF08A', 'Thank you, coach,', 'for believing', 'in me.'),
]


def gratitude_wall():
    b = [wall('#F3E3C3', '#C9A979'), banner('OUR GRATITUDE WALL · NUESTRO MURO DE GRATITUD', RED, '#fff', fs=24)]
    for x, y, c, l1, l2, l3 in NOTES:
        b.append(f'<g transform="rotate({(x % 7) - 3} {x+80} {y+65})"><rect x="{x}" y="{y}" width="160" height="130" fill="{c}" stroke="{INK}" stroke-width="3"/>'
                 f'<path d="M{x+70} {y-6} h20 v14 h-20z" fill="#E2E8F0" opacity=".9"/>'
                 + text(x + 80, y + 40, l1, 17, fam='Andika,sans-serif') + text(x + 80, y + 68, l2, 17, fam='Andika,sans-serif') + text(x + 80, y + 96, l3, 17, fam='Andika,sans-serif')
                 + f'<path d="M{x+132} {y+112} c-6 -10 -18 -4 -12 6 l12 10 l12 -10 c6 -10 -6 -16 -12 -6z" fill="{RED}"/></g>')
    b.append(kid(820, 500, .55, skin=1, top=GREEN, hair='braids', pose='point', flip=True))
    return ''.join(b)


# ---------------- Thursday · Would You Rather ----------------
def wyr_tt(kind):
    b = [f'<rect width="900" height="560" fill="#F2E7CC"/>']

    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{RED}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="{YEL}" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 24)}</g>')
    card = lambda x, y, t: f'<rect x="{x}" y="{y}" width="130" height="100" rx="8" fill="#FBCFE8" stroke="{INK}" stroke-width="4"/><path d="M{x+65} {y+70} c-14 -22 -40 -8 -26 12 l26 20 l26 -20 c14 -20 -12 -34 -26 -12z" fill="{RED}"/>' + text(x + 65, y + 32, t, 18)
    if kind == 'k1':
        a = kid(160, 390, .95, skin=0, top=PINK, hair='puffs', pose='stand', face='open') + f'<rect x="230" y="110" width="150" height="70" rx="16" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(305, 154, 'THANK YOU!', 22)
        bb = kid(140, 390, .95, skin=3, top=GREEN, hair='fade', pose='hold') + card(240, 180, 'FOR YOU')
        b.append(panel(30, 'SAY IT WITH WORDS', a, 'A') + panel(460, 'MAKE A PICTURE', bb, 'B'))
    elif kind == '23':
        a = f'<rect x="90" y="110" width="230" height="250" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(205, 150, 'Dear friend,', 22, BLUE, fam='Andika,sans-serif') + ''.join(f'<path d="M110 {190+i*36} H300" stroke="#A0AEC0" stroke-width="4"/>' for i in range(4))
        bb = kid(140, 390, .9, skin=4, top=BLUE, hair='curly', pose='tray') + f'<rect x="108" y="282" width="64" height="40" fill="{ORNG}" stroke="{INK}" stroke-width="3"/>' + kid(300, 390, .9, skin=2, top=RED, hair='braids', pose='stand', face='open', flip=True)
        b.append(panel(30, 'WRITE A NOTE', a, 'A') + panel(460, 'DO A KIND ACT', bb, 'B'))
    elif kind == '45':
        a = kid(130, 390, .9, skin=1, top=ORNG, hair='ponytail', pose='stand') + kid(290, 390, .9, skin=5, top=PURP, hair='hijab', pose='stand', face='open', flip=True) + text(205, 120, 'ONE, IN DETAIL', 24, GREEN)
        bb = ''.join(kid(70 + i * 68, 390, .55, skin=i, top=[RED, BLUE, GREEN, ORNG, PINK][i], hair=['fade', 'puffs', 'curly', 'braids', 'locs'][i], pose='wave') for i in range(5)) + text(205, 120, 'FIVE, QUICKLY', 24, BLUE)
        b.append(panel(30, 'THANK ONE PERSON', a, 'A') + panel(460, 'THANK FIVE PEOPLE', bb, 'B'))
    else:
        a = kid(205, 390, .95, skin=0, top=TEAL, hair='fade', pose='both', face='open') + f'<path d="M70 150 l30 10 M60 200 l34 0 M330 160 l-30 10 M346 206 l-34 0" stroke="{RED}" stroke-width="6" stroke-linecap="round"/>' + text(205, 110, 'SHOUT-OUT', 28, RED)
        bb = kid(130, 390, .9, skin=3, top=RED, hair='puffs', pose='hold') + kid(300, 390, .9, skin=2, top='#4A5568', hair='cap', pose='stand', flip=True) + f'<rect x="196" y="250" width="44" height="32" fill="#fff" stroke="{INK}" stroke-width="3"/>' + text(205, 110, 'QUIET + PRIVATE', 26, BLUE)
        b.append(panel(30, 'IN FRONT OF EVERYONE', a, 'A') + panel(460, 'ONE ON ONE', bb, 'B'))
    return ''.join(b)


TUE = {'k1': hold_door, '23': lunch_line, '45': note_desk, '68': unseen_work}
WED = {'k1': gratitude_wall, '23': gratitude_wall, '45': gratitude_wall, '68': gratitude_wall}
