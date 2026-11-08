#!/usr/bin/env python3
import os, shutil, html, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_mm import *
from icons import ICONS

REPO = '/home/claude/morningmeeting'
T12 = f'{REPO}/resources/week-12-everyone-belongs'
T11 = f'{REPO}/resources/week-11-back-on-the-one'
OUT = f'{REPO}/preview/{SLUG}'
FIRST5 = 'https://canva.link/bhu6ll009tiusud'
RELAX_V = 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/relax.mp4'
EXCITE_V = 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/excite.mp4'
F5_EXCITE = 'https://canva.link/jvexkr9edw021uy'

e = lambda s: html.escape(s, quote=False)
a = lambda s: html.escape(s, quote=True)

def setup():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + '/assets')
    shutil.copytree(f'{T12}/shared', OUT + '/shared')
    for src in (T11, T12):
        for f in os.listdir(src + '/assets'):
            if 'scene' in f: continue
            shutil.copy(f'{src}/assets/{f}', f'{OUT}/assets/{f}')
    for k, v in ICONS.items():
        open(f'{OUT}/assets/{k}.svg', 'w').write(v)

L12 = open(f'{T12}/lesson-1-35.html').read().split('\n')
HEAD = '\n'.join(L12[:167]) + '\n</style>'
HEAD = HEAD[HEAD.index('<style>'):]
TAIL = L12[167][L12[167].index('<script>'):] + '\n' + '\n'.join(L12[168:])
# body opening line 168 contains hud+main+notes; we rebuild it.

def es(t): return f'<span class="es" lang="es">{e(t)}</span>'

def foot(day, band, n):
    t = DAYINFO[day]['title'][0]
    return (f'<div class="foot"><span>Matchbook Morning Meeting · {e(t)} · {THEME[0]}</span><span class="say">'
            '<button class="spk" data-lang="en" aria-label="Read aloud in English">EN ▶</button>'
            '<button class="spk" data-lang="es" aria-label="Leer en español">ES ▶</button></span>'
            f'<span class="band">{BANDGRADES[band]} · {n:02d}</span></div>')

def slide(cls, band, label, en, es_, eyebrow, body, day, n):
    k2 = ' k2' if band == 'k2' else ''
    return (f'<section class="slide {cls}{k2}" aria-label="{a(label)}" data-en="{a(en)}" data-es="{a(es_)}">'
            f'<p class="eyebrow">{eyebrow}</p><div class="body-wrap">{body}</div>{foot(day, band, n)}</section>')

def img(icon, cls='icon'): return f'<img class="{cls}" src="assets/{icon}.svg" alt="">'

def items(lst):
    return '<div class="items">' + ''.join(f'<div class="item">{img(i)}<div class="lab">{e(en)}</div><div class="txt" lang="es">{e(s)}</div></div>' for i, en, s in lst) + '</div>'

def iconsrow(lst):
    return '<div class="icons-row" style="margin-top:14px">' + ''.join(f'<figure>{img(i)}{e(en)}<small lang="es">{e(s)}</small></figure>' for i, en, s in lst) + '</div>'

def notes_for(day, band):
    D = DAYINFO[day]; X = L[(day, band)]; n1, n2, n3, n4 = X['names']
    title = D['title'][0]
    vt, vc = X['video'][1], X['video'][2]
    w = X['watch'][0]
    out = []
    out.append(('Welcome · ready screen', f'Say: “Good morning. {D["welcome"][0]} Today’s focus is {title}.” Use the usual greeting. The recurring First 5 video may play before the timed meeting. {D["ground"]}'))
    out.append(('Regulate · 2:00', f'Say: “Let’s get our bodies ready to learn together. Breathe in slowly. Breathe out slowly.” Model three comfortable breaths. Students may breathe, look at the slide, or rest their hands; no one has to close their eyes. Then read the third card aloud: “{D["reg3"][0]}.” Keep individual supports such as fidgets, seats, and visual schedules available as usual.'))
    rep = 'Have students repeat each label with a hand motion.' if band == 'k2' else 'Ask students to read the goal with you.'
    out.append(('Orient · 2:00', f'Say: “Today’s goal: {X["target"][0]}” Point to each picture and read its label. {rep} Check for understanding with an equity stick: “{n1}, which picture shows something you could do today?” Accept pointing. Say: “Yes. We will practice that right now.”'))
    out.append(('Connect · Look · 2:00', f'Read the message on the slide aloud, then press the read-aloud button for Spanish if your class needs it. Before the clip, say: “Watch for this question: {w}” Press “Watch 60 seconds.” The clip opens with captions on and stops at 1:00 ({vt}, {vc}). If the video does not load, read the message on the slide a second time and go straight to the question. After the clip, give five seconds of think time, then pull an equity stick: “{n2}, {w[0].lower() + w[1:]}” Talk move: “Can you say more?” Then: “Who can add on to that?”'))
    if band == 'k2':
        out.append(('Connect · Share · 1:00', f'Read the situation aloud: “{X["share"][0]}” Point to choice A, then choice B, and read each one. Say: “Think. Do not call out. Point when I say go.” Give ten seconds of think time, then say “Go.” Students point to the slide or hold up a Show-Me card. Equity stick: pull a stick and ask, “{n3}, which choice did you point to?” Then pull a second stick: “Tell us why.” Accept pointing, signing, or a whispered answer to a partner. Answer: {X["answer_share"]} Name it: “{X["name_it"]}” Talk move: “Who can say it in their own words?”'))
    else:
        q1, q2 = X['qs'][0][0], X['qs'][1][0]
        out.append(('Connect · Share · 1:00', f'Read the situation aloud: “{X["share"][0]}” Then read each question: {q1} {q2} Give ten seconds of silent think time. Turn and talk: “Partner A answers the first question. Partner B answers the second. Go.” After 30 seconds, say “Switch.” Equity stick: pull two sticks. Ask {n3}, “What did your partner say?” Ask {n4}, “Do you agree or want to add on? Say more.” Close with the slide line: “{X["callout"][0]}” Strong response: {X["strong"]}'))
    model = 'Model the first step on a copy under the document camera, or hold up the page and point.' if band == 'k2' else 'Model the first step in one sentence, then release.'
    out.append(('Practice · Do It · 3:00', f'Students use the {X["ws"]} page from the {BANDLABEL[band]} toolkit. {X.get("wsnote", "")} Read each step on the slide aloud and point to where it is on the page. {model} 0:00–0:30 model. 0:30–2:30 students work; circulate and read the page aloud for anyone who wants it. 2:30–3:00 two students share. LiveSchool · {X["live"]} Award points for the behavior while circulating, not for finishing first. Look for: {X["evidence"]} Access: {X["diff"]}'))
    out.append(('Commit · 3:00', f'Say: “The bottom of your page is a take-home card: {X["home"][0]}. Tonight, ask your family the family chat question.” Read the family chat question and the frame aloud. Model: “{X["model"]}” Give 90 seconds to finish the frame by drawing, writing, or telling a partner. Commitments stay private unless a student chooses to share. Pull one equity stick for a volunteer share; a student may pass by saying “I am still thinking.” Students fold the page and put it in their take-home folder.'))
    out.append(('Transition · 2:00', f'Say: “{X["trans"][0]}” Name the next class task and where to start. Use your established release cue. Behavior support: {X["behavior"]}'))
    return out

def lesson(day, band):
    D = DAYINFO[day]; X = L[(day, band)]
    lnum, dlabel, _ = DAYS[day - 1]
    title_en, title_es = D['title']
    eb = lambda ph: f'Week {WEEK} · {dlabel} · {ph}'
    S = []
    # 1 Welcome
    body = (f'<h1>{e(title_en)}{es(title_es)}</h1><p class="lede">{e(D["welcome"][0])}{es(D["welcome"][1])}</p>'
            f'<div class="titlerow">{img(D["hero"], "hero-img icon")}<a class="vid" target="_blank" rel="noopener" href="{FIRST5}">▶ Watch the First 5</a></div>')
    S.append(slide('red', band, f'Welcome: {title_en}', f'{title_en}. {D["welcome"][0]}', f'{title_es}. {D["welcome"][1]}', eb('Welcome · ready screen'), body, day, 1))
    # 2 Regulate
    r3 = D['reg3']
    body = '<h2>Breathe and Settle' + es('Respira y cálmate') + '</h2>' + items([('lungs', 'Breathe in', 'Inhala'), ('lungs', 'Breathe out', 'Exhala'), ('heart', r3[0], r3[1])])
    S.append(slide('', band, 'Regulate: Breathe and Settle', f'Breathe and settle. Breathe in slowly. Breathe out slowly. {r3[0]}.', f'Respira y cálmate. Inhala despacio. Exhala despacio. {r3[1]}.', eb('Regulate · 2:00'), body, day, 2))
    # 3 Orient
    t = X['target']; oi = X['oitems']
    body = f'<h2>{e(t[0])}{es(t[1])}</h2>' + items(oi)
    S.append(slide('dark', band, f'Orient: {t[0]}', t[0] + ' ' + ' '.join(x[1] + '.' for x in oi), t[1] + ' ' + ' '.join(x[2] + '.' for x in oi), eb('Orient · 2:00'), body, day, 3))
    # 4 Look
    vid, vt, vc = X['video']; w = X['watch']; lk = X['look']
    left = f'<p class="lede">{e(lk[0])}{es(lk[1])}</p>' + (iconsrow(X['lookicons']) if 'lookicons' in X else '')
    right = (f'<div class="vidcard"><a class="vid" target="_blank" rel="noopener" href="https://www.youtube.com/embed/{vid}?start=0&end=60&cc_load_policy=1&rel=0"><span class="pl"></span>Watch 60 seconds</a>'
             f'<span class="vsrc">Video: {e(vt)} · {e(vc)} · captions on</span></div>'
             f'<div class="frame"><div class="flab">Watch for · Busca</div><div class="stem">{e(w[0])}{es(w[1])}</div></div>')
    body = f'<h2>{e(title_en)}{es(title_es)}</h2><div class="lookgrid"><div>{left}</div><div>{right}</div></div>'
    S.append(slide('look', band, f'Connect · Look: {title_en}', f'{lk[0]} Watch for this: {w[0]}', f'{lk[1]} Busca esto: {w[1]}', eb('Connect · Look · 2:00'), body, day, 4))
    # 5 Share
    sh = X['share']
    if band == 'k2':
        A, B, fr = X['A'], X['B'], X['sframe']
        body = (f'<h2>{e(sh[0])}{es(sh[1])}</h2><div class="choices2">'
                f'<div class="choice-big">{img(A[0])}<div><div class="ab">A</div><div class="ct">{e(A[1])}{es(A[2])}</div></div></div>'
                f'<div class="choice-big">{img(B[0])}<div><div class="ab">B</div><div class="ct">{e(B[1])}{es(B[2])}</div></div></div></div>'
                f'<div class="frame"><div class="flab">Think · point · share</div><div class="stem">{e(fr[0])}{es(fr[1])}</div></div>')
        en = f'{sh[0]} A: {A[1]} B: {B[1]} {fr[0]}'; es_ = f'{sh[1]} A: {A[2]} B: {B[2]} {fr[1]}'
    else:
        qs = X['qs']; co = X['callout']
        body = (f'<h2>{e(sh[0])}{es(sh[1])}</h2><div class="qlist">' +
                ''.join(f'<div class="qrow"><span class="num">{i+1}</span><span>{e(q[0])}{es(q[1])}</span></div>' for i, q in enumerate(qs)) +
                f'</div><p class="callout">{e(co[0])}{es(co[1])}</p>')
        en = f'{sh[0]} {qs[0][0]} {qs[1][0]} {co[0]}'; es_ = f'{sh[1]} {qs[0][1]} {qs[1][1]} {co[1]}'
    S.append(slide('', band, f'Connect · Share: {sh[0]}', en, es_, eb('Connect · Share · 1:00'), body, day, 5))
    # 6 Practice
    st = X['steps']
    stepsh = '<div class="steps">' + ''.join(f'<div class="step"><span class="n">{i+1}</span>{img(s[0])}<span class="sl">{e(s[1])}</span><span class="ss" lang="es">{e(s[2])}</span></div>' for i, s in enumerate(st)) + '</div>'
    extra = iconsrow(X['picons']) if band == 'k2' else '<div class="chips">' + ''.join(f'<span>{e(c[0])}<small lang="es">{e(c[1])}</small></span>' for c in X['chips']) + '</div>'
    if 'story' in X:
        extra = f'<div class="frame"><div class="flab">Story · Historia</div><div class="stem">{e(X["story"][0])}{es(X["story"][1])}</div></div>' + extra
    body = f'<h2>{e(X["ws"])}</h2><div class="wsbar"><b>Worksheet · Hoja</b><span>{BANDLABEL[band]} toolkit · {dlabel.split()[0]} page · página del {["lunes","martes","miércoles","jueves","viernes"][["Monday","Tuesday","Wednesday","Thursday","Friday"].index(dlabel.split()[0])]}</span></div>' + stepsh + extra
    S.append(slide('yellow', band, f'Practice: {X["ws"]}', f'Use your {X["ws"]} page. ' + ' '.join(s[1] for s in st), f'Usa tu hoja {X["ws"]}. ' + ' '.join(s[2] for s in st), eb('Practice · Do It · 3:00'), body, day, 6))
    # 7 Commit
    c = X['commit']; h = X['home']
    body = (f'<h2>My Commitment{es("Mi compromiso")}</h2><div class="frame"><div class="flab">Think · say · draw · write</div><div class="stem">{e(c[0])}{es(c[1])}</div></div>'
            f'<div class="homecard">{img("home")}<div><div class="hk">Take home · Para la casa: {e(h[0])}</div><div class="ht">Family chat: {e(h[1])}{es("Charla en familia: " + h[2])}</div></div></div>')
    S.append(slide('dark', band, f'Commit: {h[0]}', f'My commitment. {c[0]} Take home: {h[0]}. Family chat: {h[1]}', f'Mi compromiso. {c[1]} Para la casa: {h[0]}. Charla en familia: {h[2]}', eb('Commit · 3:00'), body, day, 7))
    # 8 Transition
    th, tp, tl = X['trans_h'], X['trans'], X['trans_l']
    body = f'<h2>{e(th[0])}{es(th[1])}</h2><p class="large-prompt">{e(tp[0])}{es(tp[1])}</p><div class="titlerow">{img(X["trans_icon"], "hero-img icon")}<p class="lede">{e(tl[0])}{es(tl[1])}</p></div>'
    S.append(slide('red', band, f'Transition: {th[0]}', f'{th[0]}. {tp[0]} {tl[0]}', f'{th[1]}. {tp[1]} {tl[1]}', eb('Transition · 2:00'), body, day, 8))
    notes = ''.join(f'<div class="note-block"><h3>{e(h)}</h3><p class="script">{e(t)}</p></div>' for h, t in notes_for(day, band))
    hud = (f'<nav class="hud" aria-label="Presentation controls"><a href="index.html">Week hub</a><a href="printables-{band}.html#day-{lnum}">Toolkit</a>'
           f'<a href="teacher-guide.html#day-{lnum}-{band}">Guide</a><button id="prev" aria-label="Previous slide">←</button><button id="next" aria-label="Next slide">→</button>'
           '<button id="nbtn" aria-controls="notes" aria-expanded="false">Notes (N)</button><span class="cnt" id="cnt" aria-live="polite"></span></nav>')
    doc = (f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week {WEEK} · {e(title_en)} · {BANDLABEL[band]}</title>'
           + HEAD + '\n<body>' + hud + '<main class="deck">' + ''.join(S) + '</main><aside class="notes" id="notes" aria-label="Teacher notes">' + notes + '</aside>' + TAIL)
    open(f'{OUT}/lesson-{lnum}-{band}.html', 'w').write(doc)

# ---------- site pages ----------
PAGEHEAD = open(f'{T12}/teacher-guide.html').read()
PAGEHEAD = PAGEHEAD[PAGEHEAD.index('<link rel="stylesheet"'):PAGEHEAD.index('</head>')]
def page(title, kicker_sub, h1, sub, main):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>{PAGEHEAD}</head><body>'
            f'<header class="hero"><div class="shell"><div class="brand"><img src="shared/matchbook-flame.png" alt="Matchbook flame">MATCHBOOK LEARNING · MORNING MEETING</div>'
            f'<div class="kicker">Week {WEEK} · {DATES}</div><h1>{e(h1)}</h1><p>{e(sub)}</p><div class="actions"><a class="btn small" href="index.html">Week hub</a>'
            f'<a class="btn small light" href="teacher-guide.html">Teacher guide</a><button class="btn small yellow" onclick="window.print()">Print</button></div></div></header>'
            f'<main><div class="shell">{main}</div></main></body></html>')

REC = ('<section class="section" id="weekly-videos"><h2>Weekly Videos &amp; Do Now – First 5</h2><div class="grid two"><article class="card"><div class="meta">Weekly Videos</div><h3>Relax &amp; Excite</h3><div class="actions">'
       f'<a class="btn small " href="{RELAX_V}" target="_blank" rel="noopener">▶ Relax</a><a class="btn small yellow" href="{EXCITE_V}" target="_blank" rel="noopener">▶ Excite</a></div></article>'
       '<article class="card"><div class="meta">Do Now – First 5</div><h3>Relax &amp; Excite</h3><div class="actions">'
       f'<a class="btn small " href="{FIRST5}" target="_blank" rel="noopener">▶ Relax</a><a class="btn small yellow" href="{F5_EXCITE}" target="_blank" rel="noopener">▶ Excite</a></div></article></div></section>')
RECROW = f'<h4>Weekly Videos</h4><a href="{RELAX_V}">Relax</a> · <a href="{EXCITE_V}">Excite</a><h4>Do Now – First 5</h4><a href="{FIRST5}">Relax</a> · <a href="{F5_EXCITE}">Excite</a>'

def index():
    cards = ''
    for lnum, dlabel, _ in DAYS:
        D = DAYINFO[lnum]
        ws = ' · '.join(f'{BANDLABEL[b]} {L[(lnum, b)]["ws"]}' for b in BANDS)
        cards += (f'<article class="card"><div class="meta">{dlabel}</div><h3>{e(D["title"][0])}</h3><p>{e(D["summary"])}</p><div class="actions">'
                  + ''.join(f'<a class="btn small" href="lesson-{lnum}-{b}.html">{BANDLABEL[b]}</a>' for b in BANDS)
                  + f'</div><p><b>Worksheets:</b> {e(ws)}</p>{RECROW}</article>')
    main = (f'<section class="section"><h2>{e(INTRO_H)}</h2><p>{e(INTRO_P)}</p>'
            '<p><b>Six phases:</b> Regulate 2 · Orient 2 · Connect 3 · Practice 3 · Commit 3 · Transition 2 minutes. Welcome is the ready screen.</p>'
            + ''.join(f'<p>{p}</p>' for p in SCHEDULE_PS) + '</section>'
            + REC +
            f'<section class="section"><h2>{CARDS_H}</h2><div class="grid two">{cards}</div></section>'
            '<section class="section"><h2>Keep the learning visible</h2><div class="grid three">'
            + ''.join(f'<article class="card"><h3>{BANDGRADES[b]}</h3><p>Show-Me response cards for the daily think-and-talk, plus the worksheet and take-home card for each day.</p><a class="btn small" href="printables-{b}.html">Open toolkit</a></article>' for b in BANDS)
            + '</div></section><section class="section"><h2>Prepare for Monday</h2><p>Print the toolkit for your band: one Show-Me card set per student (or use fingers for A and B) and one worksheet page per student for each day. Students complete the top of the page in Practice and take the bottom card home after Commit.</p>'
            '<p>Each video button opens the clip on YouTube with captions on and stops at one minute. Online video links require internet; each lesson also works by reading the key message aloud.</p><p><a href="media.html">Weekly media</a></p></section>')
    open(f'{OUT}/index.html', 'w').write(page(THEME[0], '', THEME[0], SUBTITLE, main))

def media():
    rows = ''
    for lnum, dlabel, _ in DAYS:
        rows += f'<tr><th>{dlabel}<br>{e(DAYINFO[lnum]["title"][0])}</th>' + ''.join(
            f'<td><a href="https://www.youtube.com/watch?v={L[(lnum,b)]["video"][0]}" target="_blank" rel="noopener">{e(L[(lnum,b)]["video"][1])}</a><br><small>{e(L[(lnum,b)]["video"][2])}</small></td>' for b in BANDS) + '</tr>'
    main = REC + ('<section class="section"><h2>This week’s videos</h2><p>Each lesson deck opens the first 60 seconds of each video with captions on. The full videos below can extend the lesson at another time of day.</p>'
                  f'<div style="overflow-x:auto"><table class="daymap"><thead><tr><th>Day</th><th>K–2</th><th>3–5</th><th>6–8</th></tr></thead><tbody>{rows}</tbody></table></div></section>')
    open(f'{OUT}/media.html', 'w').write(page('Weekly Media', '', 'Weekly Media', 'Recurring resources and this week’s videos', main))

def guide():
    top = (f'<section class="section"><h2>{e(GUIDE_H)}</h2><p>{e(GUIDE_P)}</p>'
           '<p><b>Timing:</b> Welcome ready screen; Regulate 2, Orient 2, Connect 3 (Look 2 and Share 1), Practice 3, Commit 3, Transition 2 minutes.</p>'
           f'<p>{PRIVACY_P}</p>'
           '<p><b>Video clips:</b> each “Watch 60 seconds” button opens the YouTube video with captions on and stops at one minute. If a video will not load, read the key message aloud a second time and continue.</p></section>'
           '<section class="section"><h2>Participation moves for every lesson</h2><p><b>Equity sticks (cold call):</b> keep one stick per student in a “not yet called” cup. Always give think time first, then say, “Everyone has an answer. I will pull a stick.” Pull, read the name, ask the question, and move the stick to the “called” cup. If a student needs a moment, say “I will come back to you,” call one more student, and return. Accept pointing, signing, or a device response. The scripts name exactly when to pull a stick.</p>'
           '<p><b>Turn and talk:</b> partners A and B. “Partner A answers first. Partner B, listen so you can repeat it.” After 30 seconds: “Switch.” Then cold call: “Tell us what your partner said.” K–2 partners sit knee to knee for 10 to 15 seconds.</p>'
           '<p><b>Talk moves:</b> “Say more.” “Who can add on?” “Do you agree or disagree? Why?” “Say it in your own words.” “What in the video or slide makes you think that?”</p>'
           f'<p>{LIVESCHOOL_P}</p><p>{BEHAVIOR_P}</p></section>'
           '<section class="section"><h2>Jump to a lesson</h2>'
           + ''.join(f'<p>{dl}: ' + ' · '.join(f'<a href="#day-{n}-{b}">{BANDLABEL[b]}</a>' for b in BANDS) + '</p>' for n, dl, _ in DAYS)
           + ''.join(f'<p>{p}</p>' for p in JUMP_EXTRA) + '</section>')
    secs = ''
    for lnum, dlabel, _ in DAYS:
        D = DAYINFO[lnum]
        for b in BANDS:
            X = L[(lnum, b)]
            steps = ''.join(f'<div class="teacher-step"><h3>{e(h)}</h3><p class="script">{e(t)}</p></div>' for h, t in notes_for(lnum, b))
            secs += (f'<section class="section" id="day-{lnum}-{b}"><div class="meta">{dlabel} · {BANDGRADES[b]} · {D["tag"]}</div><h2>{e(D["title"][0])}</h2>'
                     f'<p><b>Target:</b> {e(X["target"][0])}</p><p><b>Key message:</b> {e(X["look"][0])}</p>'
                     f'<p><b>Prepare:</b> {e(X["ws"])} page from the {BANDLABEL[b]} toolkit (one per student); pencils and crayons; equity sticks; LiveSchool open; Show-Me cards from the toolkit. Video: {e(X["video"][1])} ({e(X["video"][2])}).</p>'
                     f'<p><b>Evidence:</b> {e(X["evidence"])}</p><p><b>Differentiate:</b> {e(X["diff"])}</p>'
                     f'<div class="keybox"><b>Answer notes:</b> {e(X["answer"])}</div>'
                     f'<p><b>Take home:</b> {e(X["home"][0])}. Family chat: {e(X["home"][1])}</p>'
                     f'<p><a href="lesson-{lnum}-{b}.html">Open the {BANDLABEL[b]} deck</a> · <a href="printables-{b}.html#day-{lnum}">Open the worksheet</a></p>{steps}</section>')
    open(f'{OUT}/teacher-guide.html', 'w').write(page('Teacher Guide', '', 'Teacher Guide', GUIDE_SUB, top + secs))


def printables():
    for b in BANDS:
        cards = ''.join(f'<div>{"<span class=big>"+k+"</span>" if k else ""}<img src="assets/{i}.svg" alt=""><b>{e(en)}</b><span lang="es">{e(s)}</span></div>' for k, i, en, s in SHOWME[b])
        main = (f'<section class="tool-sheet" id="show-me"><div class="meta">{BANDGRADES[b]} · every day</div><h2>Show-Me Cards · Tarjetas para mostrar</h2>'
                '<p>Cut on the lines. Students hold up a card during Connect · Share so every student answers at the same time, with or without speaking.</p>'
                f'<div class="showme">{cards}</div></section>')
        for lnum, dlabel, _ in DAYS:
            X = L[(lnum, b)]
            icons = ''.join(f'<img class="icon" src="assets/{i}.svg" alt="">' for i, _, _ in X['oitems'])
            fields = ''
            if 'story' in X:
                fields += f'<div class="keybox"><b>Story:</b> {e(X["story"][0])}<br><span lang="es">{e(X["story"][1])}</span></div>'
            for i, fl in enumerate(X['pfields']):
                draw = b == 'k2' and fl.startswith('Draw')
                fields += f'<div class="tool-field"><b>{e(fl)}</b>' + ('<div class="drawing"></div>' if draw else '<div class="line"></div>' + ('' if b == 'k2' else '<div class="line"></div>')) + '</div>'
            if b == 'k2':
                fields = (f'<div class="tool-field"><div class="tool-icons" style="justify-content:space-around">' + ''.join(
                    f'<figure style="margin:0;text-align:center"><img class="icon" src="assets/{i}.svg" alt="" style="width:80px;height:80px"><figcaption><b>{e(en)}</b><br><span lang="es">{e(s)}</span></figcaption></figure>' for i, en, s in X['picons']) + '</div></div>') + fields
            st = ' '.join(s[1] for s in X['steps']); sts = ' '.join(s[2] for s in X['steps'])
            main += (f'<section class="tool-sheet" id="day-{lnum}"><div class="meta">{dlabel} · {BANDGRADES[b]}</div><h2>{e(X["ws"])}</h2><p>Name: _____________________</p>'
                     f'<div class="tool-icons">{icons}</div><p><b>Students:</b> {e(st)}</p><p lang="es"><b>Estudiantes:</b> {e(sts)}</p>{fields}'
                     f'<p><b>My commitment:</b> {e(X["commit"][0])}<br><span lang="es">{e(X["commit"][1])}</span></p><div class="line"></div>'
                     f'<div class="cut"><b>Take home: {e(X["home"][0])}</b><br>Family chat: {e(X["home"][1])}<br><span lang="es">Charla en familia: {e(X["home"][2])}</span></div>'
                     '<p>Point, say, draw, dictate, or write.</p></section>')
        t = f'{BANDGRADES[b]} · {TOOLKIT}'
        open(f'{OUT}/printables-{b}.html', 'w').write(page(t, '', t, 'Show-Me cards, daily worksheets, and take-home cards', main))

if __name__ == '__main__':
    setup()
    for d, _, _ in DAYS:
        for b in BANDS: lesson(d, b)
    index(); media(); guide(); printables()
    print('MM built', OUT)
