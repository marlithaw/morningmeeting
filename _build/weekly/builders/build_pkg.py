#!/usr/bin/env python3
import os, re, json, html, subprocess, sys, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import art
from build_se import OUT, W4, icon100, MMREL
e = lambda s: html.escape(s, quote=False)

FMT = {'mon': ('Check-In', '¿Cómo estás?'), 'wed': ('Zoom In', 'De cerca'), 'thu': ('Would You Rather?', '¿Qué prefieres?'), 'fri': ('Friday Wonder', 'La pregunta del viernes')}
FOOT = f'Week {SE_WEEK} | {THEME[0]} | November 2–6, 2026'
CSS = '''@font-face{font-family:Oswald;src:url(shared/c92b62da7f9d.woff2)}@font-face{font-family:Andika;src:url(shared/95ae4c899373.woff2)}@font-face{font-family:Andika;font-weight:700;src:url(shared/4591e06d5206.woff2)}
@page{size:letter;margin:.45in}*{box-sizing:border-box}body{margin:0;font-family:Andika,sans-serif;color:#232323}
.pg{height:10.05in;display:flex;flex-direction:column;page-break-after:always;position:relative}.pg:last-child{page-break-after:auto}
.bar{background:#232323;color:#fff;padding:10px 16px}.bar small{display:block;color:#F9DC7C;font:700 10px Oswald;letter-spacing:.12em}.bar b{font:700 26px Oswald}
.meta{font-size:11px;margin:10px 0 4px}.nm{margin:8px 0 12px;font-size:13px}.q{font-weight:700;font-size:17px;line-height:1.3}.qe{font-size:12.5px;color:#4a4a4a;margin:4px 0 10px}
.box{flex:1;border:1.5px solid #888;border-radius:10px;padding:8px;font-size:11px;color:#666;margin-top:10px}.foot{display:flex;justify-content:space-between;border-top:1px solid #999;padding-top:6px;font-size:9px;margin-top:10px}
.art{border:3px solid #232323;border-radius:14px;overflow:hidden;width:70%;margin:6px auto}.art svg{display:block;width:100%}
.cards{display:flex;gap:16px;justify-content:center;margin:8px 0}.cards div{border:3px solid #232323;border-radius:12px;width:2in;padding:10px;text-align:center}.cards .ab{font:700 26px Oswald;color:#E21C24;display:block}.cards svg{width:70px;height:70px}.cards b{display:block;font:700 15px Oswald;text-transform:uppercase}.cards span{font-size:11px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:6px 0 10px}.grid div{border:1.5px solid #ccc;border-radius:8px;padding:6px;text-align:center;font-size:11px}.grid svg{width:44px;height:44px}
h3{font:700 15px Oswald;margin:10px 0 4px;text-transform:uppercase}.opt{font-size:12.5px;margin:3px 0}.cb{display:inline-block;width:12px;height:12px;border:1.5px solid #232323;border-radius:50%;margin-right:6px;vertical-align:-2px}
.slip{flex:1;display:flex;flex-direction:column;padding-bottom:10px}.slip+.slip{border-top:2px dashed #888;padding-top:14px}.slip .box{min-height:1.8in}.fr{font-size:12.5px;margin:2px 0}
'''

def head(kind, band): return f'<div class="bar"><small>MATCHBOOK LEARNING | SAFE · RESPECTFUL · RESPONSIBLE</small><b>{kind} | {SBL[band]}</b></div>'

WXI = {
 'sun': '<circle cx="25" cy="25" r="10" fill="#F7B733"/><path d="M25 5v7M25 38v7M5 25h7M38 25h7M11 11l5 5M34 34l5 5M39 11l-5 5M16 34l-5 5" stroke="#F7B733" stroke-width="3" stroke-linecap="round"/>',
 'cloud': '<path d="M12 34 Q4 34 6 26 Q8 19 16 21 Q19 11 30 13 Q40 15 39 24 Q46 25 45 31 Q44 35 38 35 Z" fill="#cfd8dc" stroke="#232323" stroke-width="2"/>',
 'rain': '<path d="M12 28 Q4 28 6 21 Q8 14 16 16 Q19 7 30 9 Q40 11 39 19 Q46 20 45 25 Q44 29 38 29 Z" fill="#9fb3c8" stroke="#232323" stroke-width="2"/><path d="M15 34l-2 7M25 34l-2 7M35 34l-2 7" stroke="#2B6CB0" stroke-width="3" stroke-linecap="round"/>',
 'storm': '<path d="M12 26 Q4 26 6 19 Q8 12 16 14 Q19 5 30 7 Q40 9 39 17 Q46 18 45 23 Q44 27 38 27 Z" fill="#6b7280" stroke="#232323" stroke-width="2"/><path d="M26 28l-6 10h6l-4 9 10-13h-6l4-6z" fill="#F7B733"/>',
 'wind': '<path d="M6 18h26q8 0 6-7M6 27h34q8 0 6 7M6 36h20" fill="none" stroke="#2B6CB0" stroke-width="3" stroke-linecap="round"/>',
 'fog': '<path d="M8 16h34M4 25h40M8 34h34" stroke="#9ca3af" stroke-width="5" stroke-linecap="round"/>',
 'rainbow': '<path d="M6 40a19 19 0 0 1 38 0" fill="none" stroke="#E21C24" stroke-width="4"/><path d="M11 40a14 14 0 0 1 28 0" fill="none" stroke="#F7B733" stroke-width="4"/><path d="M16 40a9 9 0 0 1 18 0" fill="none" stroke="#2F855A" stroke-width="4"/>',
}
WX = [('sun', 'Sunny', 'happy / feliz'), ('cloud', 'Cloudy', 'okay / regular'), ('rain', 'Rainy', 'sad / triste'), ('storm', 'Stormy', 'mad / enojado/a'), ('wind', 'Windy', 'wiggly / inquieto/a'), ('fog', 'Foggy', 'tired / cansado/a'), ('rainbow', 'Rainbow', 'getting better / mejorando')]

def checkin(band):
    if band in ('k1', '23'):
        g = '<h3>My weather inside / Mi clima por dentro</h3><div class="grid">' + ''.join(f'<div><svg viewBox="0 0 50 50">{WXI[k]}</svg><br><b>{en}</b><br>{es}</div>' for k, en, es in WX) + '</div>'
        if band == '23':
            g += '<h3>My ready move / Mi paso para estar listo</h3>' + ''.join(f'<p class="opt"><i class="cb"></i>{x}</p>' for x in ['Take 3 slow breaths / Respira lento 3 veces', 'Get my materials ready / Alista mis materiales', 'Read the board / Lee el pizarrón', 'Ask a question / Haz una pregunta'])
            g += '<p class="fr">I feel ___. My ready move is ___. / Me siento ___. Mi paso es ___.</p>'
        return g + '<div class="box">Draw if you want / Dibuja si quieres</div><p class="opt"><i class="cb"></i><b>I want to talk to an adult. / Quiero hablar con un adulto.</b></p><p class="opt"><b>Circle. Fold. Put in the box. / Marca. Dobla. Pon en la caja.</b></p>'
    if band == '45':
        g = '<h3>My energy / Mi energía</h3><div class="grid" style="grid-template-columns:repeat(5,1fr)">' + ''.join(f'<div><b>{n}</b><br>{t}</div>' for n, t in [(1, 'Running on empty / Sin energía'), (2, 'Low / Baja'), (3, 'Okay / Regular'), (4, 'Good / Buena'), (5, 'Fully charged / A toda carga')]) + '</div>'
        g += '<h3>One small move / Un paso pequeño</h3>' + ''.join(f'<p class="opt"><i class="cb"></i>{x}</p>' for x in ['Drink water / Tomar agua', 'Comfortable breaths / Respirar cómodamente', 'Materials ready / Materiales listos', 'Read the board / Leer el pizarrón', 'Ask a question / Hacer una pregunta'])
        return g + '<div class="box">What would help? (optional) / ¿Qué ayudaría? (opcional)</div><p class="opt"><i class="cb"></i>I would like an adult check-in. / Quisiera hablar con un adulto.</p><p class="opt"><b>Circle. Fold. Put in the box. / Marca. Dobla. Pon en la caja.</b></p>'
    g = '<h3>Ready level / Nivel de preparación</h3><div class="grid" style="grid-template-columns:repeat(5,1fr)">' + ''.join(f'<div><b>{n}</b><br>{t}</div>' for n, t in [(1, 'Not at the line yet'), (2, 'Warming up'), (3, 'At the line'), (4, 'Set'), (5, 'Ready to go')]) + '</div>'
    g += '<h3>A word or two / Una o dos palabras</h3><p class="opt">calm · focused · content · excited · tired · stressed · anxious · frustrated · overwhelmed · not sure</p>'
    g += '<h3>One move in my control / Una acción bajo mi control</h3><div class="box" style="flex:.5">Write it / Escríbela</div>'
    return g + '<div class="box">Anything you want an adult to know (optional) / Algo que quieras que un adulto sepa (opcional)</div><p class="opt"><i class="cb"></i>Check in with an adult. / Hablar con un adulto.</p><p class="opt"><b>Fold. Put in the box. / Dobla. Pon en la caja.</b></p>'

def student_pages(band):
    pages = []
    for n, d in enumerate(SDAYS, 1):
        f = FMT[d]
        body = ''
        if d == 'mon':
            body = checkin(band)
        else:
            if d == 'wed': q = WED_DO[band]; vis = f'<div class="art"><svg viewBox="{WED_FROM[band]}" xmlns="http://www.w3.org/2000/svg"><rect width="900" height="560" fill="#f2e7cc"/>{art.hallway()}</svg></div>'
            elif d == 'thu':
                A, B, q, _ = THU[band]
                vis = '<div class="cards">' + ''.join(f'<div><span class="ab">{L}</span>{icon100(X[0])}<b>{e(X[1])}</b><span>{e(X[2])}</span></div>' for L, X in (('A', A), ('B', B))) + '</div>'
            else: q = FRI[band][0]; vis = f'<div class="art"><svg viewBox="0 0 900 560" xmlns="http://www.w3.org/2000/svg"><rect width="900" height="560" fill="#f2e7cc"/>{art.ripple()}</svg></div>'
            body = f'<p class="q">{e(q[0])}</p><p class="qe">{e(q[1])}</p>{vis}<div class="box">My response / Mi respuesta</div><p class="opt" style="font-size:10.5px">After reveal: one clue, check, or revision / Después: una pista o cambio</p>'
        pages.append(f'<div class="pg">{head("Morning Spark", band)}<div class="meta">{DATE[d][0]} | {f[0]}</div><div class="nm">Name / Nombre: ______________________</div>{body}<div class="foot"><span>{FOOT}</span><span>{n}</span></div></div>')
    return pages

def slips(band):
    pages = []
    for n, d in enumerate(SDAYS):
        p = EMBER[band]['prompts'][n]
        one = (f'<div class="slip"><div class="nm">Name / Nombre: ______________________</div><p class="q">{e(p[0])}</p><p class="qe">{e(p[1])}</p>'
               f'<p class="fr">{e(p[2])}</p><p class="fr" style="color:#4a4a4a">{e(p[3])}</p><div class="box">Draw / Write · Dibuja / Escribe</div>'
               '<p class="opt" style="font-size:10.5px"><i class="cb"></i>Adult check-in / Hablar con un adulto. Leave face down / Deja boca abajo.</p></div>')
        pages.append(f'<div class="pg">{head("Ember", band)}<div class="meta">{DATE[d][0]} | Private reflection / Reflexión privada</div>{one}{one}<div class="foot"><span>{FOOT}</span><span>{n+1}</span></div></div>')
    return pages

def write_pdf(name, pages):
    src = f'{OUT}/_tmp_{name}.html'
    open(src, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    subprocess.run(['node', '-e', f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{src}');await p.waitForTimeout(400);await p.pdf({{path:'{OUT}/{name}',format:'Letter',printBackground:true,margin:{{top:'0.45in',bottom:'0.45in',left:'0.45in',right:'0.45in'}}}});await b.close()}})()'''], check=True)
    os.remove(src)

# ---------------- package page / teacher guide ----------------
RELAX_V = 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/relax.mp4'
EXCITE_V = 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/excite.mp4'
TH = 'class="px-3 py-4 text-left align-top"'
SPARK_SUM = {
 'mon': {'k1': 'Weather pictures; private slip; optional adult check-in. Reveal: a respectful good morning.', '23': 'Weather pictures plus one ready move; private slip. Reveal: one respectful thing to do today.', '45': 'Energy scale 1–5; one small move; optional adult check-in. Reveal: one respectful or responsible move before lunch.', '68': 'Ready level 1–5; emotion vocabulary; one controllable action. Reveal: one choice in your control that shows respect.'},
}
def spark_task(band, d):
    if d == 'mon': return SPARK_SUM['mon'][band]
    if d == 'wed': return WED_DO[band][0]
    if d == 'thu': return THU[band][2][0]
    return FRI[band][0][0]
def spark_key(band, d):
    return {'mon': MON_REV, 'wed': WED_REV}.get(d, {}).get(band, (THU[band][3] if d == 'thu' else FRI[band][1]))[0]
def keyrow(band, d):
    return {'mon': MON_KEY, 'wed': WED_KEY, 'thu': THU_KEY, 'fri': FRI_KEY}[d][band]

def mm_links(band, d):
    if d == 'fri': return '<p><strong>Then:</strong> Time for Friday Cypher.</p>'
    n, en, _ = MM[d]
    if band == '23':
        return f'<p><strong>Then Morning Meeting:</strong> <a href="{MMREL}/lesson-{n}-k2.html">Grade 2: K–2 · {e(en)}</a><br/><a href="{MMREL}/lesson-{n}-35.html">Grade 3: 3–5 · {e(en)}</a></p>'
    mb = {'k1': 'k2', '45': '35', '68': '68'}[band]
    return f'<p><strong>Then Morning Meeting:</strong> <a href="{MMREL}/lesson-{n}-{mb}.html">{ {"k2":"K–2","35":"3–5","68":"6–8"}[mb]} · {e(en)}</a></p>'

def ember_table():
    rows = ''
    for i, d in enumerate(SDAYS):
        rows += f'<tr><th {TH}>{DATE[d][0]}</th>' + ''.join(
            f'<td {TH}><a href="https://www.youtube.com/watch?v={EMBER[b]["videos"][i][0]}" rel="noopener" target="_blank">{e(EMBER[b]["videos"][i][1])}</a><small> · {e(EMBER[b]["videos"][i][2])}</small><p>{e(EMBER[b]["prompts"][i][0])}</p><a href="ember-{b}.html#{d}">Open dated board</a></td>' for b in SBANDS) + '</tr>'
    return f'<div class="scroll"><table class="vt revision-week-table"><thead class="bg-[var(--charcoal)] text-white"><tr><th {TH}>Day</th>' + ''.join(f'<th {TH}>{SBL[b]}</th>' for b in SBANDS) + f'</tr></thead><tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody></table></div>'

def spark_table():
    rows = ''
    for d in SDAYS:
        rows += f'<tr><th {TH}>{DATE[d][0]}<br/>{FMT[d][0]}</th>' + ''.join(f'<td {TH}><p>{e(spark_task(b, d))}</p><a href="morning-spark-{b}.html#{d}">Open dated deck</a>{mm_links(b, d)}</td>' for b in SBANDS) + '</tr>'
    return f'<div class="scroll"><table class="revision-week-table"><thead class="bg-[var(--charcoal)] text-white"><tr><th {TH}>Day / format</th>' + ''.join(f'<th {TH}>{SBL[b]}</th>' for b in SBANDS) + f'</tr></thead><tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody></table></div>'

def ixl_line(band, d):
    from build_se import codes
    if band == 'k1': return ''
    parts = []
    for g in GRADES[band]:
        parts.append(f'Grade {g}: Math {" ".join(codes("math", g, d))} · Reading {" ".join(codes("ela", g, d))}')
    extra = ' Grade 2 reads a book.' if band == '23' else ''
    return f'<p><strong>IXL codes on the slide:</strong> {"; ".join(parts)}.{extra}</p>'

def band_keys(band):
    arts = ''
    for i, d in enumerate(SDAYS):
        q, stem, fac = keyrow(band, d)
        v = EMBER[band]['videos'][i]; p = EMBER[band]['prompts'][i]
        arts += (f'<article><h3>{DATE[d][0]}</h3><p><strong>Spark task:</strong> {e(spark_task(band, d))}</p><p><strong>Reveal / key:</strong> {e(spark_key(band, d))}</p>'
                 f'<p><strong>Differentiate / facilitate:</strong> {e(fac)}</p><p><strong>Equity stick (after 10 seconds of think time):</strong> “{e(q)}” <strong>Turn-and-talk stem:</strong> {e(stem)}</p>'
                 f'{ixl_line(band, d)}<p><strong>Ember video bridge:</strong> {e(EMBER[band]["bridges"][i])} ({e(v[1])})</p><p><strong>Reflection:</strong> {e(p[0])} {e(p[2])}</p>'
                 '<p><strong>Look for:</strong> a concrete, observable choice the student made or will make. Reflections stay about the student’s own actions; no one names a classmate. If a student has no real example, the morning model is enough.</p></article>')
    return f'<section><h2>Grades {SBL[band]} · Daily teaching key</h2>{arts}</section>'

def package():
    s = open(f'{W4}/index.html').read()
    headcss = s[:s.find('<body')]
    headcss = re.sub(r'<title>[^<]*</title>', f'<title>Morning Spark + Ember · Week {SE_WEEK} · November 2–6</title>', headcss)
    files = ''.join(f'<a href="{h}">{t}</a>' for h, t in
        [('teacher-guide.html', 'Dated teacher guide'), ('teacher-guide.pdf', 'Print guide'), (f'spark-ember-week-{SE_WEEK}-all-files.zip', 'Download all files')]
        + [(f'morning-spark-{b}-student-pages.pdf', f'Spark {SBL[b]} student pages') for b in SBANDS] + [(f'ember-{b}-reflection-slips.pdf', f'Ember {SBL[b]} slips') for b in SBANDS])
    guide = ('<section id="teacher-guide"><h2>Week 5 · Teacher delivery guide</h2>'
        '<p>November 2–6, 2026 has four school days: Monday, Wednesday, Thursday, and Friday. There is no school for students on Tuesday, November 3, so Tuesday’s Picture of the Day does not run this week. Morning Spark and Ember carry the same through-line as Morning Meeting: respect and responsibility. Spark keeps its fixed format rotation: Monday Check-In, Wednesday Zoom In, Thursday Would You Rather, and Friday Wonder, followed by the Time for Friday Cypher slide.</p>'
        '<h3>Spark leads straight into Morning Meeting</h3><p>Monday, Wednesday, and Thursday Spark end on a hand-off slide that names that day’s Morning Meeting lesson (Respect Is Something You Do, Own It, Fix It, and Respect and Responsibility Everywhere) with a button that opens your band’s Morning Meeting deck. Grades 2–3 rooms see two buttons: grade 2 uses the K–2 lesson and grade 3 uses the 3–5 lesson.</p>'
        '<h3>Preserve the daily routines</h3><p>Arrival at 7:15. Spark is a 3–5 minute independent task; then K–2 read and grades 3–8 use IXL. In the 2–3 deck, grade 2 reads and grade 3 uses IXL. The day’s IXL codes are on the slide, top right, from IXL Week 10 (November 2–6). Announcements are around 7:37, followed by a reveal of two minutes or less. Morning Meeting starts at 7:45; on Friday, advance to Time for Friday Cypher and students report to the hallway once the announcement is made.</p>'
        '<p>Use day keys 1–4 (Mon, Wed, Thu, Fri), arrows, bilingual read aloud, Repeat aloud for late arrivals, and Week view. Wednesday’s reveal zooms out before the answer appears; reduced-motion mode reveals immediately. Thursday votes start at zero; explanations matter more than vote totals.</p>'
        '<p>Ember: 2:05 seated pack-up, 2:08 watch and settle, 2:13 reflect, then seated waiting. Keep the existing release order and times on the rail. Chromebook stays closed on the desk until the group is called; return it to the numbered slot, then leave. No lining up. Use the board’s breathing fallback if streaming fails.</p>'
        '<h3>Equity sticks, talk moves, and LiveSchool</h3><p>Every reveal follows Show, Think (ten silent seconds), Call (one or two equity sticks), Talk (30-second turn and talk if time allows). The daily keys below give the exact cold-call question and stem for each band. Talk moves: “Say more.” “Who can add on?” “What did your partner say?” This is LiveSchool Store week: award points during the work period for the respectful and responsible choices students name, said out loud: “Respectful: Amara let her partner finish before she spoke.” “Responsible: Dante cleaned his spot without a reminder.” Never award points for being quiet or finishing first.</p>'
        '<h3>Respect and privacy</h3><p>Monday check-in slips stay private; the counselor collects them by 10:00 a.m. Feelings and readiness are information, not behavior grades. All week, students talk about their own choices or the examples on the slides, never a classmate’s behavior. If a student names a classmate, redirect in one calm sentence (“We only talk about our own choices.”), continue, and follow up privately. Any report of teasing or bullying is handled under campus reporting procedures the same day.</p>'
        '<h3>When behavior gets in the way</h3><p>Correct privately and briefly, with proximity and the expectation: “Do Now first, then IXL.” Offer a frame instead of an explanation to a student who has not started. Do not hold a student out of the reveal or Morning Meeting to finish the Do Now, and do not use LiveSchool deductions for Level 1 behavior.</p></section>')
    body = (f'<body><header><p>MATCHBOOK · WEEK {SE_WEEK} · NOVEMBER 2–6, 2026</p><h1>{THEME[0]}</h1><div>Four school days (no school Tuesday, November 3). Respect you can see and responsibility you can count on, in every space at school.</div></header><main>'
            f'<section><h2>Deliver this week</h2>{files}{ember_table()}</section>'
            f'<section><h2>Weekly Videos &amp; Do Now – First 5</h2><strong>Weekly Videos:</strong> <a href="{RELAX_V}">Relax</a><a href="{EXCITE_V}">Excite</a><br/><strong>Do Now – First 5:</strong> <a href="https://canva.link/bhu6ll009tiusud">Relax</a><a href="https://canva.link/jvexkr9edw021uy">Excite</a><br/></section>'
            f'<section><h2>Morning Spark · Week at a glance</h2>{spark_table()}</section>'
            f'<section><h2>Ember · Daily video + reflection</h2>{ember_table()}</section>{guide}'
            + ''.join(band_keys(b) for b in SBANDS) +
            f'<section id="photo-credits"><h2>Media credits</h2><p>Illustrations are original drawings. IXL codes: IXL at Home, Week {IXL_WEEK}. Ember videos play from YouTube; each channel is credited in the tables above.</p></section></main></body></html>')
    doc = headcss + body
    for f in ('index.html', 'teacher-guide.html'):
        open(f'{OUT}/{f}', 'w').write(doc)
    subprocess.run(['node', '-e', f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{OUT}/teacher-guide.html');await p.waitForTimeout(400);await p.pdf({{path:'{OUT}/teacher-guide.pdf',format:'Letter',printBackground:true,margin:{{top:'0.5in',bottom:'0.5in',left:'0.5in',right:'0.5in'}}}});await b.close()}})()'''], check=True)

def media_json():
    vids = {}; seq = {}
    for b in SBANDS:
        seq[b] = []
        for v in EMBER[b]['videos']:
            key = re.sub(r'[^a-z]', '', v[1].lower())[:14] or v[0]
            vids[key] = list(v); seq[b].append(key)
    d = {'videos': vids, 'daily_sequence': seq, 'school_days': SDAYS, 'photo_credits': [], 'review_note': 'Ember videos are new for every band and day and are not used in earlier weeks. Tuesday, November 3 is not a school day.'}
    json.dump(d, open(f'{OUT}/media-sources.json', 'w'), ensure_ascii=False, indent=1)

def zipit():
    z = f'{OUT}/spark-ember-week-{SE_WEEK}-all-files.zip'
    if os.path.exists(z): os.remove(z)
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, fs in os.walk(OUT):
            for f in sorted(fs):
                p = os.path.join(root, f)
                if p == z: continue
                zf.write(p, os.path.relpath(p, OUT))

if __name__ == '__main__':
    for b in SBANDS:
        write_pdf(f'morning-spark-{b}-student-pages.pdf', student_pages(b))
        write_pdf(f'ember-{b}-reflection-slips.pdf', slips(b))
    media_json(); package(); zipit()
    print('package built')
