# Richer illustration kit for Spark Week 5: full-body kids with varied hair, skin, clothes; school settings.
SK = ['#6B3E22', '#8D5524', '#A0612E', '#C68642', '#4A2A17', '#D9A066']
HAIR = '#1E130C'
INK = '#232323'
RED = '#E21C24'; YEL = '#F9DC7C'; BLUE = '#2B6CB0'; GREEN = '#2F855A'; PURP = '#7B4FBF'; ORNG = '#F2A007'; PINK = '#D53F8C'; TEAL = '#1F8A8A'

def kid(x, y, s=1.0, skin=0, top=RED, pants='#2D3748', hair='fade', pose='stand', face='smile', shoes='#fff', flip=False, extra=''):
    """Full-body kid. (x,y) = feet center. Height ~ 230*s."""
    k = SK[skin % len(SK)]
    f = -1 if flip else 1
    o = [f'<g transform="translate({x},{y}) scale({s * f},{s})">']
    # legs + shoes
    o.append(f'<path d="M-16 -70 L-18 -8 M16 -70 L18 -8" stroke="{pants}" stroke-width="20" stroke-linecap="round"/>')
    o.append(f'<path d="M-32 -2 Q-30 -14 -14 -12 L-6 -2 Z M6 -2 L14 -12 Q30 -14 32 -2 Z" fill="{shoes}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    # body
    o.append(f'<path d="M-34 -70 Q-38 -142 0 -146 Q38 -142 34 -70 Z" fill="{top}" stroke="{INK}" stroke-width="3"/>')
    # arms
    arms = {
        'stand': ('M-30 -130 Q-46 -100 -42 -78', 'M30 -130 Q46 -100 42 -78', (-42, -74), (42, -74)),
        'wave': ('M-30 -130 Q-46 -100 -42 -78', 'M30 -132 Q60 -150 58 -190', (-42, -74), (58, -194)),
        'hold': ('M-30 -130 Q-46 -100 -42 -78', 'M30 -130 Q64 -124 84 -128', (-42, -74), (88, -128)),
        'both': ('M-30 -132 Q-56 -150 -54 -190', 'M30 -132 Q56 -150 54 -190', (-54, -194), (54, -194)),
        'tray': ('M-30 -128 Q-40 -104 -20 -98', 'M30 -128 Q40 -104 20 -98', (-16, -98), (16, -98)),
        'point': ('M-30 -130 Q-46 -100 -42 -78', 'M30 -130 Q62 -136 86 -150', (-42, -74), (90, -152)),
        'phone': ('M-30 -128 Q-44 -104 -14 -110', 'M30 -130 Q46 -100 42 -78', (-10, -112), (42, -74)),
    }[pose]
    for d in arms[:2]:
        o.append(f'<path d="{d}" stroke="{top}" stroke-width="17" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".25"/>')
    for hx, hy in arms[2:]:
        o.append(f'<circle cx="{hx}" cy="{hy}" r="9" fill="{k}" stroke="{INK}" stroke-width="2"/>')
    # neck + head
    o.append(f'<rect x="-8" y="-158" width="16" height="16" fill="{k}"/>')
    hy = -186
    if hair == 'puffs':
        o.append(f'<circle cx="-26" cy="{hy-26}" r="15" fill="{HAIR}"/><circle cx="26" cy="{hy-26}" r="15" fill="{HAIR}"/>')
    if hair == 'locs':
        for dx in (-26, -18, 18, 26):
            o.append(f'<path d="M{dx} {hy-10} Q{dx*1.15} {hy+20} {dx*1.05} {hy+44}" stroke="{HAIR}" stroke-width="8" stroke-linecap="round" fill="none"/>')
    if hair == 'braids':
        o.append(f'<path d="M-24 {hy} Q-34 {hy+40} -28 {hy+62} M24 {hy} Q34 {hy+40} 28 {hy+62}" stroke="{HAIR}" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="-28" cy="{hy+66}" r="5" fill="{RED}"/><circle cx="28" cy="{hy+66}" r="5" fill="{YEL}"/>')
    if hair == 'ponytail':
        o.append(f'<path d="M20 {hy-18} Q52 {hy-6} 40 {hy+30}" stroke="{HAIR}" stroke-width="14" stroke-linecap="round" fill="none"/>')
    if hair == 'hijab':
        o.append(f'<path d="M-34 {hy+44} Q-40 {hy-36} 0 {hy-38} Q40 {hy-36} 34 {hy+44} Z" fill="{PURP}" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<circle cx="0" cy="{hy}" r="27" fill="{k}" stroke="{INK}" stroke-width="3"/>')
    if hair in ('fade', 'puffs', 'braids', 'ponytail', 'locs', 'curly'):
        if hair == 'curly':
            for cx_, cy_ in ((-20, -18), (-8, -26), (6, -27), (19, -19), (-25, -6), (25, -6)):
                o.append(f'<circle cx="{cx_}" cy="{hy+cy_}" r="10" fill="{HAIR}"/>')
        else:
            o.append(f'<path d="M-27 {hy-2} Q-26 {hy-30} 0 {hy-30} Q26 {hy-30} 27 {hy-2} Q16 {hy-16} 0 {hy-16} Q-16 {hy-16} -27 {hy-2} Z" fill="{HAIR}"/>')
    if hair == 'cap':
        o.append(f'<path d="M-27 {hy-6} Q-25 {hy-32} 0 {hy-32} Q25 {hy-32} 27 {hy-6} Z" fill="{BLUE}" stroke="{INK}" stroke-width="3"/><path d="M20 {hy-10} H46" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/>')
    if hair == 'hijab':
        o.append(f'<path d="M-27 {hy+6} Q-28 {hy-28} 0 {hy-30} Q28 {hy-28} 27 {hy+6} Q20 {hy-14} 0 {hy-16} Q-20 {hy-14} -27 {hy+6} Z" fill="{PURP}"/>')
    o.append(f'<circle cx="-9" cy="{hy-2}" r="3.2" fill="{INK}"/><circle cx="9" cy="{hy-2}" r="3.2" fill="{INK}"/>')
    mouth = {'smile': f'<path d="M-9 {hy+10} Q0 {hy+18} 9 {hy+10}" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>',
             'open': f'<path d="M-8 {hy+9} Q0 {hy+22} 8 {hy+9} Z" fill="{INK}"/>',
             'flat': f'<path d="M-7 {hy+12} H7" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>',
             'worried': f'<path d="M-8 {hy+15} Q0 {hy+9} 8 {hy+15}" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'}[face]
    o.append(mouth)
    o.append(extra)
    o.append('</g>')
    return ''.join(o)

def text(x, y, t, fs=28, fill=INK, anchor='middle', weight=700, fam='Oswald,Impact,sans-serif'):
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{weight}" font-size="{fs}" text-anchor="{anchor}" fill="{fill}">{t}</text>'

def bubble(x, y, w, h, t, fs=24, tail='left'):
    tx = x + 34 if tail == 'left' else x + w - 34
    return (f'<path d="M{tx-12} {y+h-2} L{tx-4 if tail=="left" else tx+4} {y+h+28} L{tx+12} {y+h-2}" fill="#fff" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#fff" stroke="{INK}" stroke-width="4"/><rect x="{tx-14}" y="{y+h-8}" width="28" height="10" fill="#fff"/>'
            + text(x + w / 2, y + h / 2 + fs * .36, t, fs, INK, fam='Andika,sans-serif'))

def flame(x, y, s=1):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0 -40 C18 -20 30 -6 22 14 C16 30 -16 30 -22 14 C-28 -2 -14 -12 -6 -26 C-2 -14 6 -10 8 -2 C14 -14 8 -28 0 -40 Z" fill="{RED}" stroke="{INK}" stroke-width="3"/>'

def points(x, y, t='+1 RESPECTFUL', fill=GREEN):
    return f'<g transform="translate({x},{y})"><rect x="-82" y="-24" width="164" height="48" rx="24" fill="{fill}" stroke="{INK}" stroke-width="4"/>{text(0, 9, t, 22, "#fff")}</g>'

def wall(color='#EAD9B8', floor='#C9A979'):
    return (f'<rect width="900" height="560" fill="{color}"/><rect y="430" width="900" height="130" fill="{floor}"/>'
            f'<path d="M0 430 H900" stroke="{INK}" stroke-width="5"/>' + ''.join(f'<path d="M{x} 430 L{x-60} 560" stroke="{INK}" stroke-width="2" opacity=".18"/>' for x in range(60, 960, 90)))

def svg(body, vb='0 0 900 560', label='', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>'

# ---------------- scenes ----------------
def arrival():
    b = [wall('#F3E3C3', '#C9A979')]
    b.append(f'<rect x="40" y="36" width="820" height="86" rx="12" fill="{INK}"/>' + flame(96, 84, .9) + text(480, 96, 'GOOD MORNING, MATCHBOOK', 42, YEL))
    b.append(f'<rect x="620" y="150" width="210" height="280" fill="#7FB3E6" stroke="{INK}" stroke-width="6"/><rect x="646" y="176" width="158" height="96" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(725, 236, 'ROOM 63', 30, RED))
    b.append(kid(150, 470, 1.05, skin=0, top=RED, hair='puffs', pose='wave'))
    b.append(kid(330, 470, 1.05, skin=3, top=BLUE, hair='fade', pose='hold', flip=False))
    b.append(kid(450, 470, 1.05, skin=1, top=ORNG, hair='braids', pose='stand', flip=True))
    b.append(kid(720, 470, 1.0, skin=5, top=GREEN, hair='curly', pose='wave', flip=True))
    b.append(bubble(60, 150, 210, 64, '¡Buenos días!', 26))
    b.append(bubble(390, 150, 190, 64, 'Morning!', 26, 'left'))
    b.append(points(780, 470, '+1 RESPECTFUL'))
    return ''.join(b)

def cafeteria_k1():
    b = [wall('#EFE2C8', '#BFD3C1')]
    b.append(f'<rect x="40" y="40" width="300" height="110" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/>' + text(190, 86, 'CLEAN SPOT', 34, RED) + text(190, 128, 'CLEAN TABLE', 30))
    b.append(f'<rect x="90" y="300" width="560" height="34" rx="10" fill="{YEL}" stroke="{INK}" stroke-width="5"/><path d="M140 334 V440 M600 334 V440" stroke="{INK}" stroke-width="12"/>')
    # tray, milk, crumbs, sponge
    b.append(f'<rect x="180" y="270" width="170" height="30" rx="6" fill="#9FB3C8" stroke="{INK}" stroke-width="4"/><rect x="380" y="240" width="40" height="60" rx="4" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(400, 280, 'MILK', 12))
    b.append(''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#B7791F"/>' for x, y in ((470, 296), (488, 292), (505, 297), (520, 293))))
    b.append(f'<rect x="530" y="276" width="70" height="26" rx="8" fill="{ORNG}" stroke="{INK}" stroke-width="4"/>')
    b.append(kid(620, 470, 1.0, skin=1, top=PINK, hair='puffs', pose='point', flip=True))
    b.append(f'<path d="M700 260 H860 L846 430 H714 Z" fill="{GREEN}" stroke="{INK}" stroke-width="5"/>' + text(780, 360, 'TRAYS', 26, '#fff'))
    return ''.join(b)

def hallway_line():
    b = [wall('#E9DCC0', '#D4B990')]
    for i, x in enumerate(range(40, 900, 110)):
        b.append(f'<rect x="{x}" y="120" width="96" height="300" fill="{["#3B82F6", "#E21C24", "#F2A007"][i % 3]}" stroke="{INK}" stroke-width="5"/><path d="M{x+20} 150 h56 M{x+20} 166 h56" stroke="{INK}" stroke-width="4"/><rect x="{x+70}" y="260" width="12" height="28" rx="4" fill="{INK}"/>')
    b.append(f'<rect y="476" width="900" height="16" fill="{BLUE}" opacity=".85"/>')
    b.append(kid(170, 484, 1.0, skin=0, top=GREEN, hair='locs', pose='stand', shoes=RED))
    b.append(kid(330, 484, 1.0, skin=2, top=RED, hair='ponytail', pose='stand', shoes='#fff'))
    b.append(kid(490, 484, 1.0, skin=4, top=PURP, hair='hijab', pose='stand', shoes=YEL))
    b.append(kid(650, 484, 1.0, skin=3, top=ORNG, hair='fade', pose='stand', shoes=BLUE))
    b.append(f'<rect x="40" y="40" width="820" height="60" rx="10" fill="#fff" stroke="{INK}" stroke-width="5"/>' + text(450, 82, 'ON THE LINE · VOICES OFF · HANDS TO SELF', 30))
    return ''.join(b)

def store():
    b = [wall('#F4E6C8', '#C9A979')]
    b.append(f'<rect x="40" y="36" width="820" height="80" rx="12" fill="{GREEN}" stroke="{INK}" stroke-width="5"/>' + text(450, 92, 'LIVESCHOOL STORE · NOV 4–6', 40, '#fff'))
    b.append(f'<rect x="60" y="290" width="560" height="40" rx="8" fill="#8B5A2B" stroke="{INK}" stroke-width="5"/><rect x="80" y="330" width="520" height="100" fill="#A9743F" stroke="{INK}" stroke-width="5"/>')
    items = [(120, 'PENCIL', '50', BLUE), (240, 'SNACK', '150', ORNG), (360, 'FRONT OF LINE', '200', PURP), (500, 'LUNCH W/ TEACHER', '400', RED)]
    for x, name, price, c in items:
        b.append(f'<rect x="{x-46}" y="200" width="92" height="90" rx="10" fill="{c}" stroke="{INK}" stroke-width="4"/>' + text(x, 252, '★', 34, '#fff'))
        b.append(f'<g transform="translate({x},176) rotate(-6)"><rect x="-50" y="-22" width="100" height="40" rx="6" fill="#fff" stroke="{INK}" stroke-width="3"/>{text(0, 6, price + " pts", 20)}</g>')
        b.append(text(x, 316, name, 13, '#fff'))
    b.append(kid(740, 470, 1.05, skin=1, top=BLUE, hair='curly', pose='point', flip=True))
    b.append(bubble(640, 140, 230, 64, 'For the class?', 24, 'right'))
    return ''.join(b)

def phone_hall():
    b = [wall('#E3D6BC', '#C7AE86')]
    for x in range(40, 900, 120):
        b.append(f'<rect x="{x}" y="130" width="100" height="290" fill="#94A3B8" stroke="{INK}" stroke-width="5"/>')
    b.append(kid(140, 470, .9, skin=5, top=YEL, hair='curly', pose='stand', face='worried', pants='#4A5568'))
    b.append(kid(400, 470, 1.08, skin=0, top='#4A5568', hair='fade', pose='phone', face='flat'))
    b.append(kid(560, 470, 1.08, skin=3, top=RED, hair='braids', pose='hold', flip=True))
    # phone with REC
    b.append(f'<g transform="translate(386,356) rotate(-8)"><rect x="-22" y="-38" width="44" height="76" rx="8" fill="{INK}"/><rect x="-17" y="-30" width="34" height="56" rx="4" fill="#cbd5e1"/><circle cx="-6" cy="-20" r="5" fill="{RED}"/>{text(8, -16, "REC", 10, RED)}</g>')
    b.append(bubble(600, 150, 250, 64, 'Nah. Not like that.', 24, 'left'))
    b.append(f'<rect x="680" y="250" width="160" height="70" rx="10" fill="#fff" stroke="{INK}" stroke-width="4"/>' + text(760, 294, 'MAIN OFFICE →', 22))
    return ''.join(b)

def wyr_scene(kind):
    """Two-panel would-you-rather art, 900x560."""
    b = [f'<rect width="900" height="560" fill="#F2E7CC"/>']
    def panel(x, title, inner, letter):
        return (f'<g transform="translate({x},30)"><rect width="410" height="500" rx="22" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="46" cy="46" r="30" fill="{RED}"/>{text(46, 58, letter, 34, "#fff")}<g>{inner}</g>'
                f'<rect x="20" y="410" width="370" height="70" rx="14" fill="{YEL}" stroke="{INK}" stroke-width="4"/>{text(205, 456, title, 28)}</g>')
    if kind == 'k1':
        a = kid(140, 390, .95, skin=0, top=RED, hair='puffs', pose='point') + f'<rect x="230" y="110" width="140" height="70" rx="10" fill="{BLUE}"/>' + text(300, 154, 'LINE', 28, '#fff')
        bb = f'<rect x="60" y="110" width="150" height="280" fill="#7FB3E6" stroke="{INK}" stroke-width="5"/>' + kid(290, 390, .95, skin=3, top=GREEN, hair='fade', pose='hold', flip=True)
        b.append(panel(30, 'LINE LEADER', a, 'A') + panel(460, 'DOOR HOLDER', bb, 'B'))
    elif kind == '23':
        a = kid(140, 390, .95, skin=1, top=ORNG, hair='braids', pose='both') + f'<rect x="230" y="150" width="120" height="110" rx="12" fill="{PURP}" stroke="{INK}" stroke-width="4"/>' + text(290, 214, 'FOR ME', 22, '#fff')
        bb = ''.join(kid(x, 390, .62, skin=i, top=c, hair=h, pose='both') for i, (x, c, h) in enumerate(((90, RED, 'puffs'), (175, BLUE, 'fade'), (260, GREEN, 'hijab'), (345, PINK, 'curly')))) + text(205, 110, 'CLASS PARTY', 30, RED)
        b.append(panel(30, 'SOMETHING FOR ME', a, 'A') + panel(460, 'SOMETHING FOR ALL', bb, 'B'))
    elif kind == '45':
        a = kid(110, 390, .8, skin=0, top=RED, hair='locs', pose='both') + kid(220, 390, .8, skin=2, top=BLUE, hair='ponytail', pose='both') + kid(320, 390, .8, skin=4, top=GREEN, hair='fade', pose='wave') + text(205, 110, 'HALLWAY HOLLERS!', 30, RED)
        bb = f'<rect x="150" y="110" width="110" height="200" rx="18" fill="{INK}"/><rect x="162" y="128" width="86" height="150" rx="8" fill="#E2E8F0"/>' + text(205, 190, 'HOME', 20) + text(205, 222, '“So proud', 16, fam='Andika,sans-serif') + text(205, 244, 'of you!”', 16, fam='Andika,sans-serif') + f'<circle cx="205" cy="296" r="8" fill="#94A3B8"/>'
        b.append(panel(30, 'HALLWAY HOLLERS', a, 'A') + panel(460, 'CALL HOME', bb, 'B'))
    else:
        a = kid(205, 390, .95, skin=0, top='#4A5568', hair='fade', pose='both', face='open') + ''.join(f'<path d="M{110+i*50} 140 l0 26 l22 -13 z" fill="{RED}"/>' for i in range(4)) + text(205, 110, '1.2M VIEWS', 30, RED)
        bb = kid(205, 390, .95, skin=3, top=TEAL, hair='curly', pose='wave') + f'<circle cx="205" cy="250" r="160" fill="none" stroke="{YEL}" stroke-width="10" stroke-dasharray="14 12"/>' + text(205, 110, 'THE CYPHER', 30, GREEN)
        b.append(panel(30, 'VIRAL BUT DISRESPECTFUL', a, 'A') + panel(460, 'RESPECTFUL, NO VIEWS', bb, 'B'))
    return ''.join(b)

def cypher():
    b = [f'<rect width="900" height="560" fill="#2A1B12"/>', f'<ellipse cx="450" cy="470" rx="420" ry="70" fill="#3D2A1E"/>']
    b.append(f'<circle cx="450" cy="300" r="250" fill="none" stroke="{YEL}" stroke-width="6" stroke-dasharray="10 14" opacity=".8"/>')
    ring = [(170, 0, RED, 'puffs', 'both'), (290, 3, BLUE, 'fade', 'stand'), (610, 1, GREEN, 'hijab', 'both'), (730, 4, ORNG, 'locs', 'wave')]
    for x, sk, c, h, p in ring:
        b.append(kid(x, 500, .82, skin=sk, top=c, hair=h, pose=p, face='open', flip=x > 450))
    b.append(kid(450, 500, 1.05, skin=2, top=PURP, hair='braids', pose='point', face='open'))
    b.append(f'<g transform="translate(540,350)"><rect x="-8" y="-6" width="16" height="50" rx="4" fill="#9CA3AF"/><circle cx="0" cy="-16" r="18" fill="#4B5563" stroke="#111" stroke-width="3"/></g>')
    b.append(text(450, 80, 'FRIDAY CYPHER', 54, YEL))
    b.append(text(450, 124, 'SAFE · RESPECTFUL · RESPONSIBLE', 26, '#fff'))
    return ''.join(b)

def hollers():
    b = [wall('#F6E7C9', '#D2B48C')]
    b.append(f'<path d="M40 60 Q450 140 860 60" stroke="{INK}" stroke-width="3" fill="none"/>' + ''.join(f'<path d="M{x} {66+int(28*(1-((x-450)/410)**2))} l20 40 l20 -40 z" fill="{[RED, YEL, BLUE, GREEN][i % 4]}"/>' for i, x in enumerate(range(60, 860, 60))))
    for i, (x, sk, c, h, p) in enumerate([(120, 0, RED, 'puffs', 'both'), (250, 3, BLUE, 'fade', 'both'), (380, 1, YEL, 'braids', 'wave'), (520, 5, GREEN, 'curly', 'both'), (650, 4, PURP, 'hijab', 'wave'), (780, 2, ORNG, 'locs', 'both')]):
        b.append(kid(x, 480, .9, skin=sk, top=c, hair=h, pose=p, face='open'))
    b.append(text(450, 210, 'HALLWAY HOLLERS', 52, RED))
    return ''.join(b)
