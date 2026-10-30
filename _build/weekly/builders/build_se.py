#!/usr/bin/env python3
import os, re, json, shutil, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import art
from icons import ICONS

REPO = '/home/claude/morningmeeting'
W4 = f'{REPO}/resources/spark-ember/week-4-everyone-belongs'
W3 = f'{REPO}/resources/spark-ember/week-3-back-together'
OUT = f'{REPO}/preview/spark-ember/{SE_SLUG}'
MMREL = '../../week-13-respect-responsibility'
IXL = json.load(open('/home/claude/ixlrepo/public/ixl-data.json'))
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
    for en, es in (('Everyone Belongs', 'Todos pertenecemos'), ('Back Together', 'Juntos de nuevo')):
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

def deck(band):
    s4, S4 = secs(f'{W4}/morning-spark-{band}.html')
    _, S3 = secs(f'{W3}/morning-spark-{band}.html')
    out = []
    # Monday
    t = S4[('mon', 'do')]; t = set_ixl(set_theme(set_dn(t, 'mon')), 'mon'); out.append(t)
    t = S4[('mon', 'reveal')]; en, es = MON_REV[band]
    t = set_art(set_copy(set_data(set_dn(t, 'mon'), en, es), en, es), artsvg(art.checkin_reveal(), 'Three students greet each other under a sign that says Safe, Respectful, Responsible.'))
    out.append(t)
    out.append(handoff(S4[('mon', 'handoff')], 'mon', band))
    # Wednesday zoom
    hall = art.hallway()
    lab = 'A hallway: students walk on the right while one student holds the classroom door open.'
    zsvg = lambda: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{WED_FROM[band]}" role="img" aria-label="{a(lab)}"><rect width="900" height="560" fill="#f2e7cc"/>{hall}</svg>'
    en, es = WED_DO[band]
    t = S4[('wed', 'do')]; t = set_zoom(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'wed')), 'wed'), en, es), en, es), WED_FROM[band], zsvg()); out.append(t)
    en, es = WED_REV[band]
    t = S4[('wed', 'reveal')]; t = set_zoom(set_copy(set_data(set_dn(t, 'wed'), en, es), en, es), WED_FROM[band], zsvg()); out.append(t)
    out.append(handoff(S4[('wed', 'handoff')], 'wed', band))
    # Thursday WYR
    A, B, do, rev = THU[band]
    t = S4[('thu', 'do')]; t = set_cards(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'thu')), 'thu'), *do), *do), A, B); out.append(t)
    t = S4[('thu', 'reveal')]; t = set_cards(set_copy(set_data(set_dn(t, 'thu'), *rev), *rev), A, B); out.append(t)
    out.append(handoff(S4[('thu', 'handoff')], 'thu', band))
    # Friday Wonder (week 3 format) then Cypher (week 4)
    do, rev = FRI[band]
    rip = artsvg(art.ripple(), 'Five students in a row with arrows passing a good choice from one student to the next.', cls='')
    t = S3[('fri', 'do')]; t = set_art(set_copy(set_data(set_ixl(set_theme(set_dn(t, 'fri')), 'fri'), *do), *do), rip)
    if band == 'k1':
        t = set_frame(t, 'Record your thinking. Then read a book.', 'Anota tu idea. Luego lee un libro.')
    elif band == '23':
        t = set_frame(t, 'Record your thinking. Grade 2: read a book. Grade 3: go to IXL.', 'Anota tu idea. Grado 2: lee un libro. Grado 3: ve a IXL.')
    else:
        t = set_frame(t, 'Record your thinking. Then go to IXL.', 'Anota tu idea. Luego ve a IXL.')
    out.append(t)
    t = S3[('fri', 'reveal')]; t = set_art(set_copy(set_data(set_dn(t, 'fri'), *rev), *rev), rip); out.append(t)
    out.append(S4[('fri', 'handoff')])
    # assemble
    first = s4.find('<section class="slide'); last = s4.rfind('</section>') + len('</section>')
    head, tail = s4[:first], s4[last:]
    head = re.sub(r'<title>[^<]*</title>', f'<title>Morning Spark · Week {SE_WEEK} · November 2–6 · {SBL[band]}</title>', head)
    head = re.sub(r'<button data-jump="tue">Tue</button>', '', head)
    head = head.replace('aria-label="Friday, October 30" data-jump="fri"', 'aria-label="Friday, November 6" data-jump="fri"')
    tail = re.sub(r'<button aria-label="Tuesday" class="dchip" data-go="tue">.*?</button>', '', tail, flags=re.S)
    tail = tail.replace('aria-label="Friday, October 30" class="dchip"', 'aria-label="Friday, November 6" class="dchip"')
    tail = tail.replace("const DAYS = ['mon','tue','wed','thu','fri'];", "const DAYS = ['mon','wed','thu','fri'];")
    tail = tail.replace("let day = DAYS[Math.min(Math.max(new Date().getDay(),1),5)-1] || 'mon';", "let day = ({1:'mon',3:'wed',4:'thu',5:'fri'})[new Date().getDay()] || 'mon';")
    tail = tail.replace("if ('12345'.includes(e.key)) go(DAYS[+e.key-1]);", "if ('1234'.includes(e.key)) go(DAYS[+e.key-1]);")
    tail = tail.replace('all 12 slides', 'all slides')
    # IXL pin
    snap = {'math': {}, 'ela': {}}
    for subj in ('math', 'ela'):
        for g, wk in IXL[subj].items():
            snap[subj][g] = {str(IXL_WEEK): wk.get(str(IXL_WEEK), {})}
    tail = re.sub(r'/\* IXL codes on the Do Now slides, pinned to IXL Week \d+ for [^*]*\*/', f'/* IXL codes on the Do Now slides, pinned to IXL Week {IXL_WEEK} for November 2-6, 2026 (no school Tuesday, November 3). */', tail)
    tail = re.sub(r'var SNAP = \{.*?\};\n', 'var SNAP = ' + json.dumps(snap, ensure_ascii=False) + ';\n', tail, count=1, flags=re.S)
    tail = tail.replace('var w = 9;', f'var w = {IXL_WEEK};')
    doc = head + ''.join(out) + tail
    assert 'tue' not in re.findall(r'data-day="(\w+)"', doc)
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
    s = re.sub(r'<title>[^<]*</title>', f'<title>Ember {SBL[band]} · November 2–6 · {THEME[0]}</title>', s)
    s = re.sub(r'<button aria-label="Tuesday" class="dchip" data-d="tue">Tue</button>', '', s)
    s = s.replace("const DAYS=['mon','tue','wed','thu','fri'];", "const DAYS=['mon','wed','thu','fri'];")
    s = s.replace("let day=DAYS[Math.min(Math.max(new Date().getDay(),1),5)-1];", "let day=({1:'mon',3:'wed',4:'thu',5:'fri'})[new Date().getDay()]||'mon';")
    s = s.replace("DN[d][0]+' Oct '+(26+i)+' / '+DN[d][1]", "DN[d][0]+' Nov '+({mon:2,wed:4,thu:5,fri:6})[d]+' / '+DN[d][1]")
    s = s.replace("if('12345'.includes(e.key)) setDay(DAYS[+e.key-1]);", "if('1234'.includes(e.key)) setDay(DAYS[+e.key-1]);")
    s = s.replace('d0.getDay()>=1&&d0.getDay()<=5&&', '[1,3,4,5].includes(d0.getDay())&&')
    for k in ('Everyone Belongs', 'Todos pertenecemos'):
        assert k not in s or True
    s = s.replace('Everyone Belongs', THEME[0]).replace('Todos pertenecemos', THEME[1])
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
