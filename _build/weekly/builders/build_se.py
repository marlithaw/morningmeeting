#!/usr/bin/env python3
import os, re, json, shutil, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import art
import art2
import art3
from icons import ICONS

REPO = '/home/claude/morningmeeting'
W4 = f'{REPO}/resources/spark-ember/week-4-everyone-belongs'
W3 = f'{REPO}/resources/spark-ember/week-3-back-together'
OUT = f'{REPO}/preview/spark-ember/{SE_SLUG}'
MMREL = f'../../{MMSLUG}'
_IXLP = '/home/claude/ixlrepo/public/ixl-data.json'
if not os.path.exists(_IXLP):
    _IXLP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'resources', 'spark-ember', 'week-5-respect-responsibility', 'ixl-week-10-source.json')
_IXLP = '/home/claude/Matchbook_Learning_IXL/public/ixl-data.json' if os.path.exists('/home/claude/Matchbook_Learning_IXL/public/ixl-data.json') else _IXLP
IXL = json.load(open(_IXLP)) if os.path.exists(_IXLP) else {'math': {}, 'ela': {}}
e = lambda s: html.escape(s, quote=False)
a = lambda s: html.escape(s, quote=True)

def codes(subj, g, day):
    return [x[2] for x in IXL[subj][g].get(str(IXL_WEEK), {}).get(str(DAYN[day]), [])]

def secs(path):
    s = open(path).read()
    out = {}
    for m in re.finditer(r'<section class="slide[^"]*"[^>]*>.*?</section>', s, re.S):
        t = m.group(0)
        d = re.search(r'data-day="(\w+)"', t).group(1); k = re.search(r'data-kind="(\w+)"', t).group(1)
        out[(d, k)] = t
    return s, out

def set_data(t, en, es):
    t = re.sub(r'data-en="[^"]*"', 'data-en="' + a(en) + '"', t, count=1)
    return re.sub(r'data-es="[^"]*"', 'data-es="' + a(es) + '"', t, count=1)

def set_dn(t, day):
    return re.sub(r'<span class="dn">[^<]*</span>', f'<span class="dn">{DATE[day][0]} / {DATE[day][1]}</span>', t)

def set_theme(t):
    for en, es in (('Everyone Belongs', 'Todos pertenecemos'), ('Back Together', 'Juntos de nuevo'), ('Respect and Responsibility', 'Respeto y responsabilidad')):
        t = t.replace(f'<div><span class="en">{en}</span><span class="es">{es}</span></div>', f'<div><span class="en">{THEME[0]}</span><span class="es">{THEME[1]}</span></div>')
    return t

def set_ixl(t, day):
    def rep(m):
        g = m.group(2)
        mc = ''.join(f'<span class="cd">{c}</span>' for c in codes('math', g, day))
        rc = ''.join(f'<span class="cd">{c}</span>' for c in codes('ela', g, day))
        return m.group(1) + mc + m.group(4) + rc + m.group(6)
    t = re.sub(r'(<a aria-label="Grade (\d) IXL codes".*?<span class="ixc m">)(.*?)(</span><span class="ixl">Reading</span><span class="ixc r">)(.*?)(</span></a>)', rep, t, flags=re.S)
    t = re.sub(r'<div class="ixw" data-week="1">[^<]*</div>', f'<div class="ixw" data-week="1">Week {IXL_WEEK} · today\'s codes · códigos de hoy</div>', t)
    return t

def set_copy(t, en, es):
    i = t.find('class="w3copy')
    head, tail = t[:i], t[i:]
    tail = re.sub(r'<span class="en">[^<]*</span><span class="es" lang="es">[^<]*</span>', f'<span class="en">{e(en)}</span><span class="es" lang="es">{e(es)}</span>', tail, count=1)
    return head + tail

def set_frame(t, en, es):
    return re.sub(r'(<div class="frame w3small"><span class="en">)[^<]*(</span><span class="es" lang="es">)[^<]*(</span>)', lambda m: m.group(1) + e(en) + m.group(2) + e(es) + m.group(3), t)

def artsvg(body, label, vb='0 0 900 560', cls='w4full'):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{a(label)}"><rect x="-2000" y="-2000" width="5000" height="5000" fill="#f2e7cc"/>{body}</svg>'

def set_art(t, svgtxt):
    i = t.find('class="w3art"'); j = t.find('<svg', i); k = t.find('</svg>', j) + 6
    return t[:j] + svgtxt + t[k:]

def set_zoom(t, frm, svgtxt):
    t = re.sub(r'data-from="[^"]*"', f'data-from="{frm}"', t, count=1)
    return set_art(t, svgtxt)

def icon100(name):
    v = ICONS.get(name)
    if v is None:
        for d in ('week-12-everyone-belongs', 'week-11-back-on-the-one'):
            p = f'{REPO}/resources/{d}/assets/{name}.svg'
            if os.path.exists(p): v = open(p).read(); break
    return v.replace('<svg ', '<svg aria-hidden="true" ', 1)

def set_w3art(t, svgtxt):
    i = t.find('<div class="w3art">') + len('<div class="w3art">')
    j = t.find('</div></div><div class="w3copy', i)
    return t[:i] + svgtxt + t[j + len('</div>'):]

def add_bar(t, day, band):
    en, es = BARS[day][band]
    lab = 'Chant of the day · Canto del día' if band in ('k1', '23') else 'Bar of the day · Rima del día'
    blk = f'<div class="w5bar"><span class="w5k">{lab}</span><span class="en">“{e(en)}”</span><span class="es" lang="es">“{e(es)}”</span></div>'
    m = re.search(r'data-en="([^"]*)"', t); t = t.replace(m.group(0), f'data-en="{m.group(1)} {a(en)}"', 1)
    m = re.search(r'data-es="([^"]*)"', t); t = t.replace(m.group(0), f'data-es="{m.group(1)} {a(es)}"', 1)
    i = t.rfind('</main>')
    j = t.rfind('</div>', 0, i)
    return t[:j] + blk + t[j:]

W5CSS = '<style>.w5bar{margin-top:16px;background:#232323;color:#fff;border-radius:18px;padding:14px 20px;box-shadow:6px 6px 0 #E21C24;transform:rotate(-1deg)}.w5bar .w5k{display:block;font:600 16px var(--disp);letter-spacing:.14em;text-transform:uppercase;color:#F9DC7C}.w5bar .en{color:#fff;font:700 30px var(--disp);line-height:1.15}.w5bar .es{color:#F9DC7C;font-size:20px}.w3art svg.w5art{width:100%;height:100%;max-height:none;display:block}.zoom-answer .w5bar{margin-top:12px}</style>'

SCENE = art3.WED_RR
SCENE_LAB = {'k1': 'A Reset and Return reflection sheet with feeling faces and My next move lies on a desk next to a Reset 1 sign.', '23': 'A classroom poster shows the Reset and Return ladder: warning, seat change, written reflection, Tap In, Tap Out, with Level 1 and Level 2 labels.',
             '45': 'A classroom poster shows the Reset and Return ladder: warning, seat change, written reflection, Tap In, Tap Out, with Level 1 and Level 2 labels.', '68': 'A classroom poster shows the Reset and Return ladder with Level labels; a student says, Return is the goal.'}

def set_cards(t, A, B):
    def card(m, X, letter):
        return f'<div><span class="ab">{letter}</span>{icon100(X[0])}<b>{e(X[1])}</b><span lang="es">{e(X[2])}</span></div>'
    blocks = re.findall(r'<div><span class="ab">[AB]</span>.*?</div>', t, re.S)
    t = t.replace(blocks[0], card(None, A, 'A'), 1)
    t = t.replace(blocks[1], card(None, B, 'B'), 1)
    return t

def handoff(t, day, band):
    n, en, es = MM[day]
    t = set_data(t, f'Next: Morning Meeting. {en}.', f'Sigue: Reunión de la mañana. {es}.')
    t = re.sub(r'<p class="eyebrow">[^<]*</p>', f'<p class="eyebrow">{SHORT[day][0]} / {SHORT[day][1]}</p>', t, count=1)
    t = re.sub(r'<span class="mmt">[^<]*</span>', f'<span class="mmt">{e(en)}</span>', t)
    if band == '23':
        btn = f'<a class="mmbtn" href="{MMREL}/lesson-{n}-k2.html">▶ Grade 2: K–2</a><a class="mmbtn" href="{MMREL}/lesson-{n}-35.html">▶ Grade 3: 3–5</a>'
    else:
        mb = {'k1': 'k2', '45': '35', '68': '68'}[band]
        btn = f'<a class="mmbtn" href="{MMREL}/lesson-{n}-{mb}.html">▶ { {"k2": "K–2", "35": "3–5", "68": "6–8"}[mb]}</a>'
    t = re.sub(r'<span class="mmbtns">.*?</span></div>', f'<span class="mmbtns">{btn}</span></div>', t, count=1, flags=re.S)
    return t

FRI_BADGE = ('<div class="badge"><svg aria-label="Friday Wonder" height="64" role="img" viewbox="0 0 100 100" width="64" xmlns="http://www.w3.org/2000/svg"><g style="color:#F9DC7C">'
             '<circle cx="50" cy="50" fill="none" r="40" stroke="currentColor" stroke-width="9"></circle>'
             '<path d="M35 34 Q35 18 52 20 Q74 22 63 43 L50 54 V62" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="9"></path>'
             '<circle cx="50" cy="78" fill="currentColor" r="6"></circle></g></svg></div>')

def fri_badge(t):
    return re.sub(r'<div class="badge"><svg aria-label="Would You Rather".*?</svg></div>', FRI_BADGE, t, count=1, flags=re.S)

def deck(band):
    s4, S4 = secs(f'{W4}/morning-spark-{band}.html')
    _, S3 = secs(f'{W3}/morning-spark-{band}.html')
    out = []
    # Monday
    t = S4[('mon', 'do')]; t = set_ixl(set_theme(set_dn(t, 'mon')), 'mon'); out.append(t)
    t = S4[('mon', 'reveal')]; en, es = MON_REV[band]
    t = set_art(set_copy(set_data(set_dn(t, 'mon'), en, es), en, es), art2.svg(art3.huddle_rr(), label='Students gather by Room 63 under a Reset and Return banner, saying Welcome back and Bienvenido.', cls='w5art'))
    out.append(add_bar(t, 'mon', band))
    out.append(handoff(S4[('mon', 'handoff')], 'mon', band))
    # Tuesday Picture of the Day
    pic = art2.svg(art3.TUE_RR[band](), label=TUE_LAB[band], cls='w5art')
    en, es = TUE_DO[band]
    t = S4[('tue', 'do')]; t = set_art(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'tue')), 'tue'), en, es), en, es), pic); out.append(t)
    en, es = TUE_REV[band]
    t = S4[('tue', 'reveal')]; t = add_bar(set_art(set_copy(set_data(set_dn(t, 'tue'), en, es), en, es), pic), 'tue', band); out.append(t)
    out.append(handoff(S4[('tue', 'handoff')], 'tue', band))
    # Wednesday zoom
    hall = SCENE[band]()
    lab = SCENE_LAB[band]
    zsvg = lambda: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{WED_FROM[band]}" role="img" aria-label="{a(lab)}">{hall}</svg>'
    en, es = WED_DO[band]
    t = S4[('wed', 'do')]; t = set_zoom(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'wed')), 'wed'), en, es), en, es), WED_FROM[band], zsvg()); out.append(t)
    en, es = WED_REV[band]
    t = S4[('wed', 'reveal')]; t = add_bar(set_zoom(set_copy(set_data(set_dn(t, 'wed'), en, es), en, es), WED_FROM[band], zsvg()), 'wed', band); out.append(t)
    out.append(handoff(S4[('wed', 'handoff')], 'wed', band))
    # Thursday WYR
    do, rev = THU[band], THU_REV[band]
    wyr = art2.svg(art3.wyr_rr(band), label=WYR_LAB[band], cls='w5art')
    t = S4[('thu', 'do')]; t = set_w3art(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'thu')), 'thu'), *do), *do), wyr); out.append(t)
    t = S4[('thu', 'reveal')]; t = add_bar(set_w3art(set_copy(set_data(set_dn(t, 'thu'), *rev), *rev), wyr), 'thu', band); out.append(t)
    out.append(handoff(S4[('thu', 'handoff')], 'thu', band))
    # Friday Wonder (week 3 format) then Cypher (week 4)
    do, rev = FRI[band]
    rip = art2.svg(art2.hollers() if band in ('k1', '23') else art2.cypher(), label=('Students cheer under bunting at Hallway Hollers.' if band in ('k1', '23') else 'Students stand in a Friday Cypher circle, hyping the student on the mic.'), cls='w5art')
    t = S3[('fri', 'do')]; t = set_art(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'fri')), 'fri'), *do), *do), rip)
    if band == 'k1':
        t = set_frame(t, 'Record your thinking. Then read a book.', 'Anota tu idea. Luego lee un libro.')
    elif band == '23':
        t = set_frame(t, 'Record your thinking. Grade 2: read a book. Grade 3: go to IXL.', 'Anota tu idea. Grado 2: lee un libro. Grado 3: ve a IXL.')
    else:
        t = set_frame(t, 'Record your thinking. Then go to IXL.', 'Anota tu idea. Luego ve a IXL.')
    out.append(fri_badge(t))
    t = S3[('fri', 'reveal')]; t = add_bar(set_art(set_copy(set_data(set_dn(t, 'fri'), *rev), *rev), rip), 'fri', band); out.append(fri_badge(t))
    out.append(S4[('fri', 'handoff')])
    # assemble
    first = s4.find('<section class="slide'); last = s4.rfind('</section>') + len('</section>')
    head, tail = s4[:first], s4[last:]
    head = head.replace('</head>', W5CSS + '</head>', 1)
    head = re.sub(r'<title>[^<]*</title>', f'<title>Morning Spark · Week {SE_WEEK} · {RANGE} · {SBL[band]}</title>', head)
    head = head.replace('aria-label="Friday, October 30" data-jump="fri"', 'aria-label="Friday, November 13" data-jump="fri"')
    tail = tail.replace('aria-label="Friday, October 30" class="dchip"', 'aria-label="Friday, November 13" class="dchip"')
    # IXL pin
    snap = {'math': {}, 'ela': {}}
    for subj in ('math', 'ela'):
        for g, wk in IXL[subj].items():
            snap[subj][g] = {str(IXL_WEEK): wk.get(str(IXL_WEEK), {})}
    tail = re.sub(r'/\* IXL codes on the Do Now slides, pinned to IXL Week \d+ for [^*]*\*/', f'/* IXL codes on the Do Now slides, pinned to IXL Week {IXL_WEEK} for November 9-13, 2026. */', tail)
    tail = re.sub(r'var SNAP = \{.*?\};\n', 'var SNAP = ' + json.dumps(snap, ensure_ascii=False) + ';\n', tail, count=1, flags=re.S)
    tail = tail.replace('var w = 9;', f'var w = {IXL_WEEK};')
    doc = head + ''.join(out) + tail
    open(f'{OUT}/morning-spark-{band}.html', 'w').write(doc)
    return snap

def ember(band):
    s = open(f'{W4}/ember-{band}.html').read()
    E = EMBER[band]
    m = re.search(r'const EMBER=(\{.*?\});\n', s, re.S)
    old = json.loads(m.group(1))
    new = dict(old)
    new['videos'] = [list(v) for v in E['videos']]
    new['prompts'] = [list(p) for p in E['prompts']]
    new['bridges'] = E['bridges']
    s = s[:m.start(1)] + json.dumps(new, ensure_ascii=False) + s[m.end(1):]
    s = re.sub(r'<title>[^<]*</title>', f'<title>Ember {SBL[band]} · {RANGE} · {THEME[0]}</title>', s)
    s = s.replace("DN[d][0]+' Oct '+(26+i)+' / '+DN[d][1]", "DN[d][0]+' Nov '+(9+i)+' / '+DN[d][1]")
    for k in ('Everyone Belongs', 'Todos pertenecemos'):
        assert k not in s or True
    s = s.replace('Everyone Belongs', THEME[0]).replace('Todos pertenecemos', THEME[1])
    s, k = re.subn(r'<div class="called">.*?</div></div>', '', s, count=1, flags=re.S)
    assert k == 1, 'Ember called strip not found'
    old_rule = ('<span class="en">Plug in your Chromebook at your number as you leave.</span>'
                '<span class="es">Conecta tu Chromebook en tu número al salir.</span>')
    assert old_rule in s, 'Ember Chromebook rule not found'
    s = s.replace(old_rule, '<span class="en">Group called? Plug your Chromebook into your number in the cart.</span>'
                            '<span class="es">¿Llamaron a tu grupo? Conecta tu Chromebook en tu número del carrito.</span>')
    assert '.r .en{font-size:20px;line-height:1.1}' in s, 'Ember rule CSS not found'
    s = s.replace('.r .en{font-size:20px;line-height:1.1}', '.r .en{font-size:20px;line-height:1.1}.r .es{line-height:1.15}.rules{grid-template-columns:.8fr 1.4fr 1fr}', 1)
    if band == '23':  # the longest 2-3 reflection question needs a little less type to clear the panel
        s = s.replace('.rules{grid-template-columns:.8fr 1.4fr 1fr}', '.rules{grid-template-columns:.8fr 1.4fr 1fr}.p2{gap:10px}.pq .en{font-size:27px}', 1)
    open(f'{OUT}/ember-{band}.html', 'w').write(s)

if __name__ == '__main__':
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(f'{W4}/shared', f'{OUT}/shared')
    snap = None
    for b in SBANDS:
        snap = deck(b); ember(b)
    json.dump(snap, open(f'{OUT}/ixl-week-{IXL_WEEK}-source.json', 'w'), ensure_ascii=False, indent=1)
    print('SE decks built')
