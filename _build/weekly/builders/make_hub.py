#!/usr/bin/env python3
"""Insert the selected week (MMWEEK) into the hub (index.html), cloning the previous week's sections. Winter weeks get a frosty section band."""
import re, sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import content_mm as M
from build_pkg import spark_task
e = lambda s: html.escape(s, quote=False)

import importlib, datetime
_prev_n = M.WEEK - 1
try:
    PM = importlib.import_module(f'content_mm_w{_prev_n}'); PS = importlib.import_module(f'content_se_w{_prev_n - 8}')
    PREV_SE, PREV_MM = PS.SE_WEEK, PM.WEEK
    PREV_SE_SLUG = f'spark-ember/{PS.SE_SLUG}'; PREV_MM_SLUG = PM.SLUG
    PREV_THEME = PM.THEME
    PREV_SE_RANGE, PREV_MM_DATES = PS.RANGE, PM.DATES
    PREV_FIRST_TITLE = PM.DAYINFO[1]['title'][0]
    PREV_MON = PM.DAYS[0][1]
except ModuleNotFoundError:  # Week 15 / Spark-Ember Week 7 predate the per-week content files
    PREV_SE, PREV_MM = 7, 15
    PREV_SE_SLUG = 'spark-ember/week-7-thankful-together'; PREV_MM_SLUG = 'week-15-thankful-together'
    PREV_THEME = ('Thankful Together', 'Agradecidos juntos')
    PREV_SE_RANGE, PREV_MM_DATES = 'November 16–20', 'November 16–19, 2026'
    PREV_FIRST_TITLE = 'Notice the Good'
    PREV_MON = 'Monday November 16'
PREV_START = PREV_SE_RANGE.split('–')[0]           # e.g. 'November 16'
def short(label):                                  # 'Monday November 30' -> 'Mon Nov 30'
    d, mo, n = label.split()
    return f'{d[:3]} {mo[:3]} {n}'
PREV_ROW = short(PREV_MON)

def section(hub, lab):
    i = hub.index(f'<section aria-labelledby="{lab}"')
    j = hub.index('</section>', i) + len('</section>')
    return i, j

LEETEE = M.LEETEE

def add_leetee(hub):
    """Add the day-matched Lee & Tee option for K-2 to the Week 16 unit rows and the Spark K-1 and 2-3 hand-offs. Safe to run twice."""
    i, j = section(hub, f'week{M.WEEK}-title'); s = hub[i:j]
    for n, (slug, title) in LEETEE.items():
        k2 = f'href="./resources/{M.SLUG}/lesson-{n}-k2.html">K–2</a>'
        link = (f'<a class="block mt-2 text-xs font-bold underline text-[var(--spark-red)]" href="./resources/k2-behavior-toolkit/{slug}/index.html">'
                f'Lee &amp; Tee option: {title}</a>')
        if link in s: continue
        assert s.count(k2) == 1, f'K-2 button for lesson {n} not found'
        s = s.replace(k2, k2 + link)
    hub = hub[:i] + s + hub[j:]
    i, j = section(hub, f'spark-week{SE_WEEK}-title'); s = hub[i:j]
    for d in ('mon', 'tue', 'wed', 'thu'):
        n, en, _ = MM[d]; slug, title = LEETEE[n]
        href = f'./resources/k2-behavior-toolkit/{slug}/index.html'
        for lead, who in ((f'lesson-{n}-k2.html">K–2 · {e(en)}</a>', 'K–2'), (f'lesson-{n}-k2.html">Grade 2: K–2 · {e(en)}</a>', 'Grade 2')):
            link = f'<br/><a href="{href}">Or {who} Lee &amp; Tee option: {title}</a>'
            if lead + link in s: continue
            assert s.count(lead) == 1, f'Spark hand-off {lead} not found'
            s = s.replace(lead, lead + link)
    return hub[:i] + s + hub[j:]

import winter
def winterize(sec):
    if not getattr(M, 'WINTER', False): return sec
    return re.sub(r'^<section aria-labelledby="([^"]+)"( class="[^"]*")?( style="[^"]*")?', lambda m: f'<section aria-labelledby="{m.group(1)}"{m.group(2) or ""} style="{winter.HUB_SECTION_STYLE};padding:18px"', sec, count=1)

def make(hub):
    SE = f'spark-ember/{SE_SLUG}'; MMS = M.SLUG
    TH = 'class="px-3 py-4 text-left align-top"'
    # ---------- Spark ----------
    i, j = section(hub, f'spark-week{PREV_SE}-title'); s = hub[i:j]
    s = s.replace(f'spark-week{PREV_SE}-title', f'spark-week{SE_WEEK}-title').replace(PREV_SE_SLUG, SE).replace(f'week-{PREV_SE}-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace(f'Week {PREV_SE} · Four grade bands · Five formats · {PREV_SE_RANGE}, 2026', f'Week {SE_WEEK} · Four grade bands · Five formats · {RANGE}, 2026')
    s = s.replace(f'>{PREV_THEME[0]}</h2>', f'>{THEME[0]}</h2>')
    s = re.sub(r'(id="spark-week%d-title">[^<]*</h2>\s*<p class="text-sm text-slate-300 mt-2 max-w-2xl">)[^<]*' % SE_WEEK, r'\1' + HUB_SPARK_P, s)
    s = s.replace(f'Morning Spark Week {PREV_SE} - All Files.zip', f'Morning Spark Week {SE_WEEK} - All Files.zip')
    s = s.replace(f'Four dated prompts on the {PREV_THEME[0]} theme', f'Five dated prompts on the {THEME[0]} theme')
    s = s.replace(f'Five dated prompts on the {PREV_THEME[0]} theme', f'Five dated prompts on the {THEME[0]} theme')
    s = s.replace('Presentation · Monday, Wednesday, Thursday, Friday', 'Presentation · Monday to Friday')
    s = s.replace('Four dated response pages: a private check-in on Monday, then one page each for Wednesday, Thursday, and Friday.', 'Five dated response pages: a private check-in on Monday, then one page each for Tuesday through Friday.')
    s = s.replace(f'- Week {PREV_SE} - {PREV_THEME[0]}.html', f'- Week {SE_WEEK} - {THEME[0]}.html').replace(f'- Week {PREV_SE} - Student Pages.pdf', f'- Week {SE_WEEK} - Student Pages.pdf')
    rows = ''
    for d in SDAYS:
        cells = ''
        for b in SBANDS:
            if d == 'fri': mm = '<p><strong>Then:</strong> Time for Friday Cypher.</p>'
            else:
                n, en, _ = MM[d]
                if b == '23': mm = f'<p><strong>Then Morning Meeting:</strong> <a href="./resources/{MMS}/lesson-{n}-k2.html">Grade 2: K–2 · {e(en)}</a><br/><a href="./resources/{MMS}/lesson-{n}-35.html">Grade 3: 3–5 · {e(en)}</a></p>'
                else:
                    mb = {'k1': 'k2', '45': '35', '68': '68'}[b]; lb = {'k2': 'K–2', '35': '3–5', '68': '6–8'}[mb]
                    mm = f'<p><strong>Then Morning Meeting:</strong> <a href="./resources/{MMS}/lesson-{n}-{mb}.html">{lb} · {e(en)}</a></p>'
            cells += f'<td {TH}><p>{e(spark_task(b, d))}</p><a href="./resources/{SE}/morning-spark-{b}.html#{d}">Open dated deck</a>{mm}</td>'
        rows += f'<tr><th {TH}>{DATE[d][0]}<br/>{FMT[d][0]}</th>{cells}</tr>'
    s = re.sub(r'<tbody class="divide-y divide-\[var\(--hairline\)\]">.*?</tbody>', lambda m: f'<tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody>', s, flags=re.S)
    assert PREV_MM_SLUG not in s and PREV_THEME[0] not in s and PREV_START not in s, 'spark leftovers'
    s = winterize(s)
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Ember ----------
    i, j = section(hub, f'ember-week{PREV_SE}-title'); s = hub[i:j]
    s = s.replace(f'ember-week{PREV_SE}-title', f'ember-week{SE_WEEK}-title').replace(PREV_SE_SLUG, SE).replace(f'week-{PREV_SE}-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace(f'Dismissal · Week {PREV_SE} · {PREV_SE_RANGE}, 2026 · Four grade bands · Five days', f'Dismissal · Week {SE_WEEK} · {RANGE}, 2026 · Four grade bands · Five days')
    s = re.sub(r'(<i class="fa-solid fa-fire-flame-curved mr-2" style="color:#E3602A"></i>)' + PREV_THEME[0], r'\1' + THEME[0], s)
    rows = ''
    for k, d in enumerate(SDAYS):
        rows += f'<tr><th {TH}>{DATE[d][0]}</th>' + ''.join(
            f'<td {TH}><a href="https://www.youtube.com/watch?v={EMBER[b]["videos"][k][0]}" rel="noopener" target="_blank">{e(EMBER[b]["videos"][k][1])}</a><small> · {e(EMBER[b]["videos"][k][2])}</small><p>{e(EMBER[b]["prompts"][k][0])}</p><a href="./resources/{SE}/ember-{b}.html#{d}">Open dated board</a></td>' for b in SBANDS) + '</tr>'
    s = re.sub(r'<tbody class="divide-y divide-\[var\(--hairline\)\]">.*?</tbody>', lambda m: f'<tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody>', s, flags=re.S)
    assert PREV_START not in s and PREV_THEME[0] not in s, 'ember leftovers'
    s = winterize(s)
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Instructional Units ----------
    i, j = section(hub, f'week{PREV_MM}-title'); s = hub[i:j]
    s = s.replace(f'week{PREV_MM}-title', f'week{M.WEEK}-title').replace(PREV_MM_SLUG, MMS)
    s = s.replace(f'Week {PREV_MM} · {PREV_MM_DATES}', f'Week {M.WEEK} · {M.DATES}').replace(f'>{PREV_THEME[0]}</h2>', f'>{M.THEME[0]}</h2>')
    s = s.replace(f'Open Week {PREV_MM} toolkit', f'Open Week {M.WEEK} toolkit')
    s = re.sub(r'(<p class="text-sm text-slate-300 mt-2 mb-5">)[^<]*', r'\1' + M.HUB_MM_P, s)
    body = re.search(r'<tbody[^>]*>(.*?)</tbody>', s, re.S).group(1)
    first = re.search(r'<tr>.*?</tr>', body, re.S).group(0)
    rows = ''
    for n, dl, _sh in M.DAYS:
        r = first.replace(PREV_ROW, short(dl))
        r = r.replace(f'>{e(PREV_FIRST_TITLE)}<', f'>{e(M.DAYINFO[n]["title"][0])}<')
        r = re.sub(r'lesson-1-', f'lesson-{n}-', r).replace('#day-1-', f'#day-{n}-')
        rows += r
    s = s.replace(body, rows)
    assert PREV_START not in s and PREV_ROW + '<' not in s and f'>{e(PREV_FIRST_TITLE)}<' not in s, 'mm leftovers'
    s = winterize(s)
    hub = hub[:i] + s + hub[i:]
    hub = re.sub(r'(<p class="text-\[var\(--slate\)\] text-lg">)Week ' + str(PREV_MM) + ' · ' + re.escape(PREV_MM_DATES.replace(', 2026', '')) + r':[^<]*', lambda m: m.group(1) + f'Week {M.WEEK} · {M.DATES.replace(", 2026", "")}: {M.THEME[0]}. {M.HUB_INTRO}', hub, count=1)
    return add_leetee(hub)

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != '--leetee-only']
    src, dst = args[0], args[1]
    hub = open(src).read()
    out = add_leetee(hub) if '--leetee-only' in sys.argv else make(hub)
    open(dst, 'w').write(out)
    print('hub written', dst)
