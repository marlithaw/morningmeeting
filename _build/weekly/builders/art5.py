# Spark Week 8 scenes: Cool Heads, Kind Words (noticing anger, cooling down, talking it out, safe choices).
from art2 import kid, text, bubble, flame, points, wall, svg, INK, RED, YEL, BLUE, GREEN, PURP, ORNG, PINK, TEAL
from art3 import banner, table, huddle


def huddle_ch():
    s = huddle().replace(text(480, 36 + 40 + 34 * .36, 'STRONGER TOGETHER · MÁS FUERTES JUNTOS', 34, YEL),
                         text(480, 36 + 40 + 30 * .36, 'COOL HEADS, KIND WORDS · MENTE TRANQUILA', 30, YEL))
    return s.replace('Every voice!', 'Breathe first!').replace('¡Cada voz!', '¡Respira!')


def thought(x, y, w, h, t, fs=22):
    return (f'<circle cx="{x+30}" cy="{y+h+22}" r="9" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="{x+14}" cy="{y+h+42}" r="6" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="#fff" stroke="{INK}" stroke-width="4" stroke-dasharray="2 0"/>'
            + text(x + w / 2, y + h / 2 + fs * .36, t, fs, INK, fam='Andika,sans-serif'))


def blocks_down():
    b = [wall('#F3E3C3', '#C9A979'), banner('BLOCK CENTER · BLOQUES', BLUE, '#fff', fs=36)]
    cols = [RED, YEL, BLUE, GREEN, ORNG, PURP]
    for i, (x, y, r) in enumerate([(560, 470, 8), (620, 488, -14), (690, 472, 22), (600, 440, -30), (740, 490, 4), (660, 445, 40)]):
        b.append(f'<rect x="{x}" y="{y}" width="56" height="40" rx="4" fill="{cols[i]}" stroke="{INK}" stroke-width="3" transform="rotate({r} {x+28} {y+20})"/>')
    b.append(kid(390, 480, 1.05, skin=3, top=PINK, hair='puffs', pose='tray', face='flat'))
    b.append(''.join(f'<circle cx="{390+dx}" cy="{240-dy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" opacity=".7"/>' for dx, dy, r in ((-60, 0, 12), (-84, 26, 18), (-112, 56, 24))))
    b.append(thought(70, 140, 250, 64, '1, 2, 3, 4…', 26))
    b.append(kid(820, 480, .85, skin=0, top=GREEN, hair='fade', pose='stand', face='worried', flip=True))
    return ''.join(b)


def line_bump():
    b = [wall('#EAD9B8', '#C9A979'), banner('HALLWAY · PASILLO', INK, YEL, fs=36)]
    b.append(f'<path d="M40 470 H860" stroke="{YEL}" stroke-width="10" stroke-dasharray="40 24"/>')
    b.append(kid(170, 480, .95, skin=2, top=BLUE, hair='curly', pose='stand'))
    b.append(kid(330, 480, 1.0, skin=4, top=ORNG, hair='fade', pose='stand', face='worried', flip=True))
    b.append(f'<path d="M262 300 l20 -10 M262 320 l24 0 M262 340 l20 10" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>')
    b.append(kid(560, 480, 1.05, skin=0, top=RED, hair='braids', pose='stand', face='flat'))
    b.append(f'<path d="M640 310 v-54 m-12 8 v-26 m24 26 v-30 m12 34 v-22" stroke="#8D5524" stroke-width="10" stroke-linecap="round"/>')
    b.append(thought(600, 130, 260, 64, 'Stop. Breathe. Count.', 22))
    b.append(kid(780, 480, .9, skin=1, top=GREEN, hair='ponytail', pose='stand', flip=True))
    b.append(bubble(100, 140, 260, 64, 'Sorry! I tripped.', 24))
    return ''.join(b)


def cool_plan():
    b = [wall('#EFE2C8', '#C9A979')]
    b.append(table(60, 400, 440))
    b.append(f'<g transform="translate(300,230) rotate(-2)"><rect x="-230" y="-180" width="460" height="330" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             + text(0, -134, 'MY COOL-DOWN PLAN', 30, RED)
             + text(-206, -84, '1. NOTICE: hot face, tight fists', 22, anchor='start', fam='Andika,sans-serif')
             + text(-206, -40, '2. BREATHE: in 4, out 4', 22, anchor='start', fam='Andika,sans-serif')
             + text(-206, 4, '3. CHOOSE: water, walk,', 22, anchor='start', fam='Andika,sans-serif')
             + text(-160, 38, 'squeeze, or ask for a break', 22, anchor='start', fam='Andika,sans-serif')
             + text(-206, 82, '4. RETURN: ready to talk', 22, anchor='start', fam='Andika,sans-serif')
             + text(130, 128, 'by Andre', 22, BLUE, anchor='start', fam='Andika,sans-serif') + '</g>')
    b.append(f'<rect x="620" y="70" width="70" height="300" rx="35" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             f'<circle cx="655" cy="390" r="48" fill="{RED}" stroke="{INK}" stroke-width="5"/><rect x="638" y="200" width="34" height="180" fill="{RED}"/>'
             + text(760, 120, 'HOT', 26, RED) + text(760, 230, 'WARM', 26, ORNG) + text(760, 340, 'COOL', 26, BLUE))
    b.append(kid(800, 500, .75, skin=2, top=TEAL, hair='fade', pose='point', flip=True))
    return ''.join(b)


def phone_down():
    b = [wall('#E8DCC6', '#C7AE86'), banner('LUNCH · ALMUERZO', GREEN, '#fff', fs=36)]
    b.append(table(80, 360, 740))
    b.append(kid(300, 480, 1.0, skin=4, top='#4A5568', hair='cap', pose='tray', face='flat'))
    b.append(f'<rect x="380" y="344" width="70" height="16" rx="4" fill="{INK}"/>' + text(415, 330, 'phone face down', 16, BLUE, fam='Andika,sans-serif'))
    b.append(f'<g transform="translate(560,130)"><rect width="250" height="150" rx="16" fill="#fff" stroke="{INK}" stroke-width="4"/>'
             + text(125, 40, 'GROUP CHAT', 20, BLUE) + text(125, 82, '“u gonna let him', 20, fam='Andika,sans-serif') + text(125, 112, 'talk to u like that??”', 20, fam='Andika,sans-serif') + '</g>')
    b.append(''.join(f'<circle cx="{300+dx}" cy="{250-dy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" opacity=".7"/>' for dx, dy, r in ((-70, 0, 12), (-94, 26, 18), (-122, 56, 24))))
    b.append(kid(620, 480, .95, skin=1, top=PURP, hair='locs', pose='stand', face='smile', flip=True))
    b.append(bubble(70, 140, 250, 60, 'Not worth it.', 24))
    return ''.join(b)


# ---------------- Wednesday · Zoom In ----------------
def talk_table():
    b = [wall('#F3E3C3', '#C9A979'), banner('TALK IT OUT · RESUÉLVELO HABLANDO', RED, '#fff', fs=32)]
    b.append(f'<rect x="560" y="140" width="300" height="230" rx="10" fill="{YEL}" stroke="{INK}" stroke-width="4"/>'
             + text(710, 182, 'I-STATEMENT', 26, RED)
             + text(580, 226, 'I feel ___', 22, anchor='start', fam='Andika,sans-serif')
             + text(580, 266, 'when ___', 22, anchor='start', fam='Andika,sans-serif')
             + text(580, 306, 'I need ___', 22, anchor='start', fam='Andika,sans-serif')
             + text(710, 352, 'No put-downs. No cursing.', 18, BLUE))
    b.append(f'<rect x="150" y="370" width="380" height="26" rx="10" fill="#B7814A" stroke="{INK}" stroke-width="5"/><path d="M190 396 V440 M490 396 V440" stroke="{INK}" stroke-width="12"/>')
    b.append(kid(200, 480, .95, skin=0, top=BLUE, hair='puffs', pose='hold', face='open'))
    b.append(kid(480, 480, .95, skin=3, top=ORNG, hair='fade', pose='hold', face='smile', flip=True))
    b.append(f'<path d="M282 356 Q340 330 398 356" stroke="{INK}" stroke-width="4" fill="none" stroke-dasharray="8 6"/>')
    b.append(bubble(40, 140, 300, 64, 'I feel upset when…', 24))
    b.append(bubble(330, 220, 220, 60, 'I hear you.', 24, 'right'))
    return ''.join(b)


# ---------------- Thursday · Would You Rather ----------------
def wyr_ch(kind):
    b = [f'<rect width="900" height="560" fill="#F2E7CC"/>']

    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{RED}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="{YEL}" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 24)}</g>')
    rings = lambda cx, cy: ''.join(f'<circle cx="{cx+dx}" cy="{cy-dy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" opacity=".75"/>' for dx, dy, r in ((40, 0, 12), (62, 26, 18), (90, 58, 24)))
    if kind == 'k1':
        a = kid(160, 390, .95, skin=0, top=PINK, hair='puffs', pose='tray', face='smile') + rings(150, 250) + text(205, 110, '4 BIG BREATHS', 24, BLUE)
        bb = kid(205, 390, .95, skin=3, top=GREEN, hair='fade', pose='both', face='smile') + f'<circle cx="153" cy="198" r="16" fill="{ORNG}" stroke="{INK}" stroke-width="3"/><circle cx="257" cy="198" r="16" fill="{ORNG}" stroke="{INK}" stroke-width="3"/>' + text(205, 120, 'SQUEEZE · LET GO', 24, GREEN)
        b.append(panel(30, 'BREATHE', a, 'A') + panel(460, 'SQUEEZE', bb, 'B'))
    elif kind == '23':
        a = kid(140, 390, .9, skin=4, top=BLUE, hair='curly', pose='stand') + f'<rect x="230" y="150" width="140" height="210" rx="10" fill="#C6F6D5" stroke="{INK}" stroke-width="4"/>' + text(300, 200, 'CALM', 24, GREEN) + text(300, 232, 'CORNER', 24, GREEN) + f'<path d="M200 330 C220 320 230 320 240 330" stroke="{INK}" stroke-width="4" fill="none" stroke-dasharray="8 6"/>'
        bb = table(60, 300, 290) + kid(205, 390, .9, skin=2, top=RED, hair='braids', pose='tray') + text(205, 140, '1 · 2 · 3 … 10', 30, BLUE)
        b.append(panel(30, 'WALK TO CALM CORNER', a, 'A') + panel(460, 'COUNT TO 10 AT MY SEAT', bb, 'B'))
    elif kind == '45':
        a = kid(130, 390, .9, skin=1, top=ORNG, hair='ponytail', pose='stand', face='open') + kid(290, 390, .9, skin=5, top=PURP, hair='hijab', pose='stand', face='flat', flip=True) + text(205, 120, 'RIGHT NOW', 26, RED)
        bb = kid(130, 390, .9, skin=1, top=ORNG, hair='ponytail', pose='tray', face='smile') + rings(110, 250) + kid(300, 390, .9, skin=5, top=PURP, hair='hijab', pose='stand', face='smile', flip=True) + text(205, 110, 'COOL DOWN FIRST', 24, BLUE)
        b.append(panel(30, 'TALK IT OUT NOW', a, 'A') + panel(460, 'COOL DOWN, TALK LATER', bb, 'B'))
    else:
        a = kid(150, 390, .95, skin=0, top=TEAL, hair='fade', pose='stand', face='smile') + f'<path d="M230 300 H330 M300 280 l30 20 l-30 20" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>' + text(205, 120, 'LET IT GO', 28, GREEN)
        bb = kid(130, 390, .9, skin=3, top=RED, hair='puffs', pose='point') + kid(300, 410, 1.05, skin=2, top='#4A5568', hair='cap', pose='stand', face='smile', flip=True) + text(205, 120, 'GET AN ADULT', 28, BLUE)
        b.append(panel(30, 'WALK AWAY', a, 'A') + panel(460, 'GET AN ADULT TO HELP', bb, 'B'))
    return ''.join(b)


TUE = {'k1': blocks_down, '23': line_bump, '45': cool_plan, '68': phone_down}
WED = {'k1': talk_table, '23': talk_table, '45': talk_table, '68': talk_table}
