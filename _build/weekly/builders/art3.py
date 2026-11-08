# Spark Week 6 scenes: Stronger Together (teamwork in places students know).
from art2 import kid, text, bubble, flame, points, wall, svg, INK, RED, YEL, BLUE, GREEN, PURP, ORNG, PINK, TEAL

def banner(t, fill=INK, col=YEL, y=36, h=80, fs=40):
    return f'<rect x="40" y="{y}" width="820" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="4"/>' + flame(96, y + h / 2 + 8, .8) + text(480, y + h / 2 + fs * .36, t, fs, col)

def table(x=120, y=330, w=660):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" fill="#B7814A" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M{x+40} {y+32} V440 M{x+w-40} {y+32} V440" stroke="{INK}" stroke-width="12"/>')

def huddle():
    b = [wall('#F3E3C3', '#C9A979'), banner('STRONGER TOGETHER · MÁS FUERTES JUNTOS', fs=34)]
    ring = [(160, 0, RED, 'puffs'), (300, 3, BLUE, 'fade'), (600, 1, ORNG, 'braids'), (740, 5, GREEN, 'curly')]
    for x, sk, c, h in ring:
        b.append(kid(x, 480, 1.0, skin=sk, top=c, hair=h, pose='hold', flip=x > 450))
    b.append(kid(450, 480, 1.05, skin=4, top=PURP, hair='hijab', pose='both', face='open'))
    b.append(f'<circle cx="450" cy="345" r="34" fill="{YEL}" stroke="{INK}" stroke-width="4"/>' + text(450, 356, '63', 30, RED))
    b.append(bubble(40, 150, 230, 64, 'Every voice!', 26))
    b.append(bubble(630, 150, 230, 64, '¡Cada voz!', 26, 'right'))
    return ''.join(b)

def carry_box():
    b = [wall('#EFE2C8', '#C9A979'), banner('LIBRARY · BIBLIOTECA', BLUE, '#fff', fs=36)]
    for x in (60, 760):
        b.append(f'<rect x="{x}" y="140" width="90" height="290" fill="#8B5A2B" stroke="{INK}" stroke-width="5"/>' + ''.join(f'<rect x="{x+8+i*16}" y="{160+r*70}" width="12" height="54" fill="{[RED, YEL, GREEN, BLUE, ORNG][(i+r) % 5]}"/>' for r in range(4) for i in range(5)))
    b.append(kid(300, 480, 1.05, skin=0, top=RED, hair='puffs', pose='hold'))
    b.append(kid(560, 480, 1.05, skin=3, top=GREEN, hair='fade', pose='hold', flip=True))
    b.append(f'<rect x="370" y="290" width="120" height="90" rx="6" fill="#D69E2E" stroke="{INK}" stroke-width="5"/>' + text(430, 342, 'BOOKS', 22))
    b.append(bubble(300, 160, 270, 64, '1, 2, 3, lift!', 26))
    return ''.join(b)

def tower():
    b = [wall('#F4E6C8', '#C9A979'), banner('BUILD TOGETHER · CONSTRUYAMOS', fs=36)]
    b.append(table(170, 360, 560))
    blocks = [(380, 320, RED), (440, 320, BLUE), (500, 320, GREEN), (410, 280, YEL), (470, 280, ORNG), (440, 240, PURP)]
    for x, y, c in blocks:
        b.append(f'<rect x="{x}" y="{y}" width="56" height="40" fill="{c}" stroke="{INK}" stroke-width="4"/>')
    b.append(kid(160, 480, .95, skin=1, top=TEAL, hair='braids', pose='point'))
    b.append(kid(330, 480, .95, skin=0, top=RED, hair='fade', pose='hold'))
    b.append(kid(620, 480, .95, skin=4, top=PINK, hair='curly', pose='hold', flip=True))
    b.append(kid(770, 480, .95, skin=2, top=BLUE, hair='ponytail', pose='both', face='open', flip=True))
    b.append(f'<rect x="60" y="150" width="150" height="100" rx="8" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(135, 186, 'PLAN', 22, RED) + f'<path d="M100 236 h70 M115 216 h40 M125 198 h20" stroke="{INK}" stroke-width="8"/>')
    b.append(bubble(640, 150, 220, 64, 'You got it!', 24, 'right'))
    return ''.join(b)

def poster_roles():
    b = [wall('#F3E3C3', '#C9A979'), banner('GROUP WORK · TRABAJO EN EQUIPO', fs=34)]
    b.append(table(110, 340, 680))
    b.append(f'<rect x="300" y="250" width="300" height="90" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(450, 290, 'OUR PLANET', 26, GREEN) + f'<circle cx="360" cy="318" r="14" fill="{BLUE}"/><path d="M400 318 h150" stroke="{INK}" stroke-width="5"/>')
    roles = [(130, 'READER', 0, RED, 'puffs', 'hold'), (290, 'RECORDER', 3, BLUE, 'fade', 'stand'), (610, 'TIMEKEEPER', 1, ORNG, 'braids', 'stand'), (770, 'MATERIALS', 5, GREEN, 'hijab', 'point')]
    for x, r, sk, c, h, p in roles:
        b.append(kid(x, 480, .92, skin=sk, top=c, hair=h, pose=p, flip=x > 450))
        b.append(f'<rect x="{x-58}" y="356" width="116" height="30" rx="8" fill="{YEL}" stroke="{INK}" stroke-width="3"/>' + text(x, 378, r, 16))
    b.append(f'<g transform="translate(610,190)"><circle r="26" fill="#fff" stroke="{INK}" stroke-width="4"/><path d="M0 0 V-16 M0 0 L12 6" stroke="{INK}" stroke-width="4"/></g>')
    b.append(bubble(120, 150, 300, 64, 'What do you think?', 24))
    return ''.join(b)

def laptop_team():
    b = [wall('#E8DCC6', '#C7AE86'), banner('TEAM PROJECT · DUE FRIDAY', fs=36)]
    b.append(table(110, 340, 680))
    b.append(kid(440, 480, 1.0, skin=0, top='#4A5568', hair='fade', pose='hold', face='flat'))
    b.append(f'<path d="M500 338 L514 292 H600 L614 338 Z" fill="#CBD5E1" stroke="{INK}" stroke-width="4"/><rect x="522" y="300" width="70" height="30" fill="#93C5FD"/>')
    b.append(kid(230, 480, .95, skin=3, top=TEAL, hair='curly', pose='phone', face='flat'))
    b.append(f'<g transform="translate(222,366) rotate(-10)"><rect x="-13" y="-22" width="26" height="44" rx="5" fill="{INK}"/><rect x="-9" y="-17" width="18" height="32" rx="2" fill="#93C5FD"/></g>')
    b.append(kid(670, 480, .95, skin=1, top=ORNG, hair='ponytail', pose='stand', face='flat', flip=True))
    b.append(kid(810, 480, .9, skin=4, top=PURP, hair='braids', pose='wave', face='open', flip=True))
    b.append(bubble(140, 150, 280, 64, 'I’ll just do it all.', 24))
    b.append(bubble(600, 150, 260, 64, 'I have an idea!', 24, 'right'))
    return ''.join(b)

def cleanup():
    b = [wall('#EFE2C8', '#BFD3C1'), banner('CLEAN-UP TIME · A LIMPIAR', GREEN, '#fff', fs=36)]
    b.append(table(80, 330, 420))
    b.append(kid(160, 480, .95, skin=1, top=PINK, hair='puffs', pose='hold'))
    b.append(f'<rect x="250" y="310" width="70" height="22" rx="6" fill="{ORNG}" stroke="{INK}" stroke-width="3"/>')
    b.append(kid(380, 480, .95, skin=0, top=BLUE, hair='fade', pose='tray'))
    b.append(f'<rect x="360" y="368" width="64" height="40" fill="#fff" stroke="{INK}" stroke-width="4"/>')
    b.append(f'<rect x="600" y="300" width="190" height="130" rx="8" fill="#9FB3C8" stroke="{INK}" stroke-width="5"/>' + ''.join(f'<rect x="{620+i*28}" y="{270 - (i % 2) * 8}" width="14" height="44" rx="4" fill="{[RED, YEL, GREEN, BLUE, PURP, ORNG][i]}" stroke="{INK}" stroke-width="2"/>' for i in range(6)) + text(695, 380, 'CRAYONS', 22, '#fff'))
    b.append(kid(560, 480, .9, skin=3, top=YEL, hair='braids', pose='point', flip=True))
    b.append(points(780, 480, '+1 RESPONSIBLE'))
    return ''.join(b)

def relay():
    b = [f'<rect width="900" height="560" fill="#BEE3F8"/><rect y="380" width="900" height="180" fill="#68A063"/>',
         f'<path d="M0 470 H900 M0 520 H900" stroke="#fff" stroke-width="6" opacity=".8"/>', banner('RECESS RELAY · CARRERA DE RELEVOS', BLUE, '#fff', fs=34)]
    b.append(kid(300, 500, 1.0, skin=0, top=RED, hair='locs', pose='hold'))
    b.append(kid(470, 500, 1.0, skin=2, top=ORNG, hair='ponytail', pose='hold', flip=True))
    b.append(f'<rect x="376" y="360" width="34" height="12" rx="5" fill="{YEL}" stroke="{INK}" stroke-width="3"/>')
    b.append(kid(680, 500, .9, skin=4, top=GREEN, hair='fade', pose='both', face='open'))
    b.append(kid(120, 500, .9, skin=5, top=PURP, hair='hijab', pose='wave', face='open'))
    b.append(bubble(600, 150, 220, 64, 'Go, team!', 26, 'right'))
    return ''.join(b)

def job_chart():
    b = [wall('#F3E3C3', '#C9A979')]
    b.append(f'<rect x="60" y="40" width="380" height="370" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/>' + text(250, 90, 'TEAM JOBS', 36, RED))
    jobs = [('Reader', 'book'), ('Recorder', 'pencil'), ('Timekeeper', 'clock'), ('Materials', 'box'), ('Encourager', 'star')]
    for i, (j, _) in enumerate(jobs):
        y = 130 + i * 54
        b.append(f'<rect x="90" y="{y}" width="320" height="42" rx="8" fill="{[YEL, "#C6F6D5", "#BEE3F8", "#FED7E2", "#E9D8FD"][i]}" stroke="{INK}" stroke-width="3"/>' + text(200, y + 29, j, 22, anchor='middle') + f'<circle cx="360" cy="{y+21}" r="13" fill="{GREEN}" stroke="{INK}" stroke-width="3"/><path d="M353 {y+21} l5 6 l10 -12" stroke="#fff" stroke-width="4" fill="none"/>')
    b.append(table(470, 330, 400))
    b.append(kid(560, 480, .92, skin=1, top=BLUE, hair='curly', pose='hold'))
    b.append(f'<rect x="620" y="300" width="60" height="30" fill="#fff" stroke="{INK}" stroke-width="3"/>')
    b.append(kid(770, 480, .92, skin=3, top=PINK, hair='puffs', pose='point', flip=True))
    b.append(bubble(500, 150, 360, 64, 'Two minutes left, team!', 24))
    return ''.join(b)

def court_huddle():
    b = [f'<rect width="900" height="560" fill="#D69E2E"/>', f'<path d="M0 360 H900" stroke="#fff" stroke-width="6"/><circle cx="450" cy="560" r="160" fill="none" stroke="#fff" stroke-width="6"/>',
         f'<rect x="40" y="30" width="820" height="70" rx="12" fill="{INK}"/>' + text(450, 78, 'MATCHBOOK GYM · TEAM TIMEOUT', 34, YEL)]
    for x, sk, c, h in ((170, 0, RED, 'fade'), (310, 3, RED, 'braids'), (590, 1, RED, 'locs'), (730, 5, RED, 'curly')):
        b.append(kid(x, 520, 1.0, skin=sk, top=c, hair=h, pose='hold', flip=x > 450))
    from art2 import SK
    for (x0, y0), sk, rot in (((250, 380), 0, -12), ((650, 380), 1, 12), ((330, 360), 3, -6), ((570, 360), 5, 6)):
        b.append(f'<path d="M{x0} {y0} L450 {326 + (sk % 2) * 8}" stroke="{RED}" stroke-width="26" stroke-linecap="round"/>')
    for i, (sk, dx, dy, rot) in enumerate(((0, -18, 14, -10), (1, 18, 8, 12), (3, -10, -2, -4), (5, 12, -12, 8))):
        b.append(f'<g transform="translate({450+dx},{326+dy}) rotate({rot})"><rect x="-34" y="-16" width="68" height="32" rx="14" fill="{SK[sk]}" stroke="{INK}" stroke-width="4"/><path d="M-18 -16 V-4 M-4 -16 V-4 M10 -16 V-4" stroke="{INK}" stroke-width="2" opacity=".5"/></g>')
    b.append(f'<rect x="390" y="140" width="120" height="140" rx="8" fill="#fff" stroke="{INK}" stroke-width="5"/>' + text(450, 172, 'PLAY', 22, RED) + f'<circle cx="420" cy="210" r="8" fill="none" stroke="{INK}" stroke-width="4"/><path d="M432 214 L470 250 M470 200 l10 10 M480 200 l-10 10" stroke="{INK}" stroke-width="4"/>')
    b.append(bubble(560, 130, 300, 64, 'Everybody has a job.', 24, 'right'))
    return ''.join(b)

def wyr_scene(kind):
    b = [f'<rect width="900" height="560" fill="#F2E7CC"/>']
    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{RED}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="{YEL}" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 26)}</g>')
    if kind == 'k1':
        a = kid(130, 390, .85, skin=0, top=RED, hair='puffs', pose='hold') + kid(290, 390, .85, skin=3, top=BLUE, hair='fade', pose='hold', flip=True) + ''.join(f'<rect x="{180+i*36}" y="{300-(i%2)*36}" width="34" height="34" fill="{[YEL, GREEN, ORNG][i]}" stroke="{INK}" stroke-width="3"/>' for i in range(3))
        bb = kid(120, 390, .85, skin=1, top=PINK, hair='braids', pose='point') + kid(300, 390, .85, skin=4, top=GREEN, hair='curly', pose='point', flip=True) + f'<rect x="150" y="150" width="120" height="90" fill="#fff" stroke="{INK}" stroke-width="4"/><circle cx="190" cy="190" r="16" fill="{YEL}"/><path d="M160 228 Q210 196 262 228" stroke="{GREEN}" stroke-width="6" fill="none"/>'
        b.append(panel(30, 'BUILD TOGETHER', a, 'A') + panel(460, 'DRAW TOGETHER', bb, 'B'))
    elif kind == '23':
        a = kid(205, 390, .95, skin=1, top=ORNG, hair='ponytail', pose='point') + f'<circle cx="300" cy="140" r="36" fill="{YEL}" stroke="{INK}" stroke-width="4"/>' + text(300, 152, 'IDEA', 20)
        bb = kid(205, 390, .95, skin=0, top=TEAL, hair='locs', pose='both', face='open') + text(205, 110, 'YOU GOT THIS!', 30, RED)
        b.append(panel(30, 'IDEA STARTER', a, 'A') + panel(460, 'ENCOURAGER', bb, 'B'))
    elif kind == '45':
        a = kid(140, 390, .85, skin=3, top=BLUE, hair='fade', pose='hold') + kid(270, 390, .85, skin=2, top=RED, hair='braids', pose='hold', flip=True) + f'<path d="M205 140 C190 116 160 128 170 150 L205 180 L240 150 C250 128 220 116 205 140 Z" fill="{RED}"/>'
        bb = kid(140, 390, .85, skin=5, top=GREEN, hair='hijab', pose='wave') + kid(270, 390, .85, skin=0, top=ORNG, hair='curly', pose='wave', flip=True) + text(205, 140, 'HI, I’M NEW!', 26, BLUE)
        b.append(panel(30, 'MY BEST FRIEND', a, 'A') + panel(460, 'SOMEONE NEW', bb, 'B'))
    else:
        a = ''.join(kid(x, 390, .7, skin=i, top=c, hair=h, pose='stand') for i, (x, c, h) in enumerate(((110, BLUE, 'fade'), (205, BLUE, 'curly'), (300, BLUE, 'ponytail')))) + text(205, 130, 'AGREE FAST', 30, GREEN) + f'<path d="M150 170 l20 20 l40 -40" stroke="{GREEN}" stroke-width="10" fill="none"/>'
        bb = ''.join(kid(x, 390, .7, skin=i + 2, top=c, hair=h, pose='point', face='open', flip=i == 1) for i, (x, c, h) in enumerate(((120, RED, 'braids'), (290, PURP, 'locs')))) + text(205, 130, 'ARGUE IT OUT', 30, RED) + f'<circle cx="205" cy="200" r="30" fill="{YEL}" stroke="{INK}" stroke-width="4"/>' + text(205, 210, '!', 30)
        b.append(panel(30, 'AGREE FAST', a, 'A') + panel(460, 'ARGUE, THEN BUILD', bb, 'B'))
    return ''.join(b)

TUE = {'k1': carry_box, '23': tower, '45': poster_roles, '68': laptop_team}
WED = {'k1': cleanup, '23': relay, '45': job_chart, '68': court_huddle}

# ================= Reset and Return scenes =================
def huddle_rr():
    s = huddle().replace('STRONGER TOGETHER · MÁS FUERTES JUNTOS', 'RESET AND RETURN · REINICIA Y REGRESA')
    return s.replace('Every voice!', 'Welcome back!').replace('¡Cada voz!', '¡Bienvenido!')

def ladder_poster(x=40, y=40, w=520, h=360):
    steps = [('WARNING', YEL, '1'), ('SEAT CHANGE', YEL, '1'), ('WRITTEN REFLECTION', YEL, '1'), ('TAP IN', '#FBD38D', '2'), ('TAP OUT', '#FBD38D', '2')]
    b = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/>', text(x + w / 2, y + 44, 'RESET AND RETURN', 30, RED)]
    sh = (h - 90) / 5
    for i, (t, c, lv) in enumerate(steps):
        yy = y + 64 + i * sh
        b.append(f'<rect x="{x+24}" y="{yy}" width="{w-130}" height="{sh-8}" rx="8" fill="{c}" stroke="{INK}" stroke-width="3"/>' + text(x + 24 + (w - 130) / 2, yy + sh / 2 + 4, t, 20))
        b.append(f'<rect x="{x+w-96}" y="{yy}" width="74" height="{sh-8}" rx="8" fill="{INK}"/>' + text(x + w - 59, yy + sh / 2 + 4, 'LEVEL ' + lv, 14, '#fff'))
    return ''.join(b)

def classroom_ladder():
    b = [wall('#F3E3C3', '#C9A979'), ladder_poster(40, 30, 500, 380)]
    b.append(kid(700, 480, 1.0, skin=1, top=GREEN, hair='braids', pose='point', flip=True))
    b.append(bubble(600, 150, 270, 64, 'Return is the goal.', 24, 'right'))
    return ''.join(b)

def reflection_desk():
    b = [wall('#EFE2C8', '#C9A979')]
    b.append(table(80, 340, 520))
    b.append(f'<g transform="translate(330,250) rotate(-4)"><rect x="-120" y="-150" width="240" height="230" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(0, -122, 'RESET AND RETURN', 18, RED)
             + ''.join(f'<circle cx="{-84+i*42}" cy="-80" r="16" fill="{["#FC8181", "#90CDF4", "#B794F4", "#F6E05E", "#9AE6B4"][i]}" stroke="{INK}" stroke-width="2"/>' for i in range(5))
             + ''.join(f'<path d="M-100 {-40+i*26} H100" stroke="#A0AEC0" stroke-width="3"/>' for i in range(4)) + text(0, 70, 'MY NEXT MOVE', 16) + '</g>')
    b.append(kid(160, 480, .95, skin=3, top=BLUE, hair='fade', pose='hold'))
    b.append(f'<rect x="640" y="160" width="200" height="90" rx="10" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(740, 200, 'RESET 1', 32, RED) + text(740, 234, 'calm seat', 18))
    b.append(kid(740, 480, .95, skin=0, top=PURP, hair='puffs', pose='stand', flip=True))
    return ''.join(b)

def breathe_desk():
    b = [wall('#F4E6C8', '#C9A979'), banner('RESET AT MY SEAT · ME CALMO EN MI LUGAR', GREEN, '#fff', fs=30)]
    b.append(table(200, 350, 500))
    b.append(kid(450, 480, 1.05, skin=1, top=PINK, hair='puffs', pose='stand', face='smile'))
    b.append(''.join(f'<circle cx="{450+dx}" cy="{230-dy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" opacity=".7"/>' for dx, dy, r in ((60, 10, 14), (84, 34, 20), (112, 64, 26))))
    b.append(bubble(560, 150, 300, 64, 'In… and out.', 26, 'right'))
    b.append(kid(170, 480, .9, skin=4, top=BLUE, hair='fade', pose='hold'))
    return ''.join(b)

def reset_seat():
    b = [wall('#F3E3C3', '#C9A979')]
    b.append(f'<rect x="560" y="110" width="250" height="100" rx="10" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(685, 158, 'RESET 1', 40, RED) + text(685, 194, 'Bring your paper', 18))
    b.append(table(560, 330, 260))
    b.append(kid(330, 480, 1.0, skin=2, top=ORNG, hair='curly', pose='tray', face='smile'))
    b.append(f'<rect x="306" y="366" width="48" height="34" fill="#fff" stroke="{INK}" stroke-width="3"/>')
    b.append(f'<path d="M400 420 C470 440 520 430 560 400" stroke="{INK}" stroke-width="4" fill="none" stroke-dasharray="10 8"/><path d="M548 392 l14 8 l-12 10" stroke="{INK}" stroke-width="4" fill="none"/>')
    b.append(kid(120, 480, .9, skin=0, top=GREEN, hair='braids', pose='hold'))
    b.append(bubble(60, 130, 330, 64, 'Calm and quick. No big deal.', 22))
    return ''.join(b)

def lap_paper():
    b = [wall('#EFE2C8', '#C9A979')]
    b.append(f'<rect x="80" y="40" width="380" height="440" fill="#fff" stroke="{INK}" stroke-width="5"/>' + text(270, 84, 'MATH · NOV 10', 24))
    marks = [('✓', GREEN), ('★', '#D69E2E'), ('○', BLUE), ('●', RED), ('✓', GREEN)]
    for i, (m, c) in enumerate(marks):
        y = 130 + i * 68
        b.append(text(120, y + 8, f'{i+1}.', 26, anchor='start') + f'<path d="M170 {y+4} H360" stroke="#A0AEC0" stroke-width="4"/>' + text(410, y + 14, m, 40, c))
    b.append(f'<rect x="520" y="60" width="330" height="250" rx="12" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(685, 100, 'LAP MARKS', 28, RED)
             + text(560, 148, '✓ on task', 22, GREEN, anchor='start') + text(560, 186, '★ correct', 22, '#B7791F', anchor='start') + text(560, 224, '○ look again', 22, BLUE, anchor='start') + text(560, 262, '● start here', 22, RED, anchor='start'))
    b.append(kid(700, 480, .9, skin=5, top=TEAL, hair='locs', pose='point', flip=True))
    return ''.join(b)

def tapin_room():
    b = [wall('#E8DCC6', '#C7AE86')]
    b.append(f'<rect x="760" y="120" width="110" height="310" fill="#7FB3E6" stroke="{INK}" stroke-width="6"/>')
    b.append(f'<rect x="40" y="40" width="330" height="80" rx="10" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(205, 92, 'Pencil on number one.', 24))
    b.append(kid(180, 480, 1.0, skin=3, top=RED, hair='ponytail', pose='point'))
    b.append(table(320, 360, 360))
    b.append(kid(400, 480, .8, skin=0, top=BLUE, hair='fade', pose='tray'))
    b.append(kid(560, 480, .8, skin=4, top=YEL, hair='hijab', pose='tray'))
    b.append(kid(780, 480, 1.0, skin=1, top='#4A5568', hair='cap', pose='hold', flip=True))
    b.append(f'<rect x="700" y="330" width="40" height="54" rx="4" fill="#F6E05E" stroke="{INK}" stroke-width="3"/>')
    b.append(bubble(560, 150, 200, 64, 'Tap In.', 26, 'right'))
    return ''.join(b)

def wyr_rr(kind):
    b = [f'<rect width="900" height="560" fill="#F2E7CC"/>']
    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{RED}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="{YEL}" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 24)}</g>')
    if kind == 'k1':
        a = kid(205, 390, .95, skin=0, top=PINK, hair='puffs', pose='stand') + ''.join(f'<circle cx="{270+i*24}" cy="{170-i*24}" r="{10+i*5}" fill="none" stroke="{BLUE}" stroke-width="4"/>' for i in range(3))
        bb = kid(205, 390, .95, skin=3, top=GREEN, hair='fade', pose='wave') + text(300, 130, '?', 60, RED)
        b.append(panel(30, 'DEEP BREATH', a, 'A') + panel(460, 'ASK FOR HELP', bb, 'B'))
    elif kind == '23':
        a = kid(205, 390, .95, skin=1, top=ORNG, hair='braids', pose='stand') + f'<circle cx="300" cy="140" r="40" fill="#fff" stroke="{INK}" stroke-width="4"/><path d="M300 140 V112 M300 140 L320 152" stroke="{INK}" stroke-width="4"/>' + text(300, 210, '1 MIN', 22)
        bb = kid(140, 390, .9, skin=4, top=BLUE, hair='curly', pose='stand') + kid(290, 390, 1.05, skin=2, top=RED, hair='ponytail', pose='point', flip=True)
        b.append(panel(30, 'ONE-MINUTE RESET', a, 'A') + panel(460, 'QUICK TEACHER CHECK', bb, 'B'))
    elif kind == '45':
        a = f'<rect x="110" y="110" width="190" height="240" fill="#fff" stroke="{INK}" stroke-width="4"/>' + ''.join(f'<path d="M130 {150+i*44} H260" stroke="#A0AEC0" stroke-width="4"/>' for i in range(5)) + text(285, 202, '●', 34, RED)
        bb = kid(205, 390, .95, skin=5, top=PURP, hair='hijab', pose='wave') + text(300, 130, '?', 60, RED)
        b.append(panel(30, 'DOT IT, GO ON', a, 'A') + panel(460, 'ASK RIGHT AWAY', bb, 'B'))
    else:
        a = kid(140, 390, .9, skin=0, top=TEAL, hair='fade', pose='stand') + kid(280, 390, 1.0, skin=3, top=RED, hair='braids', pose='hold', flip=True) + text(205, 120, 'QUICK + PRIVATE', 26, GREEN)
        bb = kid(140, 390, .9, skin=0, top=TEAL, hair='fade', pose='stand') + kid(280, 390, 1.0, skin=3, top=RED, hair='braids', pose='stand', flip=True) + text(205, 120, '2-MINUTE TALK', 26, BLUE)
        b.append(panel(30, 'A QUICK SIGNAL', a, 'A') + panel(460, 'A SHORT TALK', bb, 'B'))
    return ''.join(b)

TUE_RR = {'k1': breathe_desk, '23': reset_seat, '45': lap_paper, '68': tapin_room}
WED_RR = {'k1': reflection_desk, '23': classroom_ladder, '45': classroom_ladder, '68': classroom_ladder}
