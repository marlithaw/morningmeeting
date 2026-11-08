#!/usr/bin/env python3
"""Insert MM Week 14 and Spark/Ember Week 6 into the hub (index.html), cloning last week's sections (MM Week 13, SE Week 5)."""
import re, sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import content_mm as M
from build_pkg import spark_task
e = lambda s: html.escape(s, quote=False)

PREV_SE, PREV_MM = 5, 13
PREV_SE_SLUG = 'spark-ember/week-5-respect-responsibility'; PREV_MM_SLUG = 'week-13-respect-responsibility'
PREV_THEME = ('Respect and Responsibility', 'Respeto y responsabilidad')

def section(hub, lab):
    i = hub.index(f'<section aria-labelledby="{lab}"')
    j = hub.index('</section>', i) + len('</section>')
    return i, j

LEETEE = M.LEETEE

def add_leetee(hub):
    """Add the day-matched Lee & Tee option for K-2 to the Week 14 unit rows and the Spark K-1 and 2-3 hand-offs. Safe to run twice."""
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

def make(hub):
    SE = f'spark-ember/{SE_SLUG}'; MMS = M.SLUG
    TH = 'class="px-3 py-4 text-left align-top"'
    # ---------- Spark ----------
    i, j = section(hub, f'spark-week{PREV_SE}-title'); s = hub[i:j]
    s = s.replace(f'spark-week{PREV_SE}-title', f'spark-week{SE_WEEK}-title').replace(PREV_SE_SLUG, SE).replace(f'week-{PREV_SE}-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace('Week 5 · Four grade bands · Four formats · November 2–6, 2026', f'Week {SE_WEEK} · Four grade bands · Five formats · {RANGE}, 2026')
    s = s.replace(f'>{PREV_THEME[0]}</h2>', f'>{THEME[0]}</h2>')
    s = re.sub(r'(id="spark-week%d-title">[^<]*</h2>\s*<p class="text-sm text-slate-300 mt-2 max-w-2xl">)[^<]*' % SE_WEEK, r'\1' + 'Five school days. Monday through Thursday follow the usual formats on Reset and Return, the classroom response levels and the written reflection, and hand off to that day’s Morning Meeting lesson. Friday Wonder carries the same theme, then Friday Cypher.', s)
    s = s.replace(f'Morning Spark Week {PREV_SE} - All Files.zip', f'Morning Spark Week {SE_WEEK} - All Files.zip')
    s = s.replace(f'Four dated prompts on the {PREV_THEME[0]} theme', f'Five dated prompts on the {THEME[0]} theme')
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
    assert PREV_MM_SLUG not in s and PREV_THEME[0] not in s and 'November 2' not in s, 'spark leftovers'
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Ember ----------
    i, j = section(hub, f'ember-week{PREV_SE}-title'); s = hub[i:j]
    s = s.replace(f'ember-week{PREV_SE}-title', f'ember-week{SE_WEEK}-title').replace(PREV_SE_SLUG, SE).replace(f'week-{PREV_SE}-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace('Dismissal · Week 5 · November 2–6, 2026 · Four grade bands · Four days', f'Dismissal · Week {SE_WEEK} · {RANGE}, 2026 · Four grade bands · Five days')
    s = re.sub(r'(<i class="fa-solid fa-fire-flame-curved mr-2" style="color:#E3602A"></i>)' + PREV_THEME[0], r'\1' + THEME[0], s)
    rows = ''
    for k, d in enumerate(SDAYS):
        rows += f'<tr><th {TH}>{DATE[d][0]}</th>' + ''.join(
            f'<td {TH}><a href="https://www.youtube.com/watch?v={EMBER[b]["videos"][k][0]}" rel="noopener" target="_blank">{e(EMBER[b]["videos"][k][1])}</a><small> · {e(EMBER[b]["videos"][k][2])}</small><p>{e(EMBER[b]["prompts"][k][0])}</p><a href="./resources/{SE}/ember-{b}.html#{d}">Open dated board</a></td>' for b in SBANDS) + '</tr>'
    s = re.sub(r'<tbody class="divide-y divide-\[var\(--hairline\)\]">.*?</tbody>', lambda m: f'<tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody>', s, flags=re.S)
    assert 'November 2' not in s and PREV_THEME[0] not in s, 'ember leftovers'
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Instructional Units ----------
    i, j = section(hub, f'week{PREV_MM}-title'); s = hub[i:j]
    s = s.replace(f'week{PREV_MM}-title', f'week{M.WEEK}-title').replace(PREV_MM_SLUG, MMS)
    s = s.replace('Week 13 · November 2–5, 2026', f'Week {M.WEEK} · {M.DATES}').replace(f'>{PREV_THEME[0]}</h2>', f'>{M.THEME[0]}</h2>')
    s = s.replace(f'Open Week {PREV_MM} toolkit', f'Open Week {M.WEEK} toolkit')
    s = re.sub(r'(<p class="text-sm text-slate-300 mt-2 mb-5">)[^<]*', r'\1' + 'Four 15-minute lessons with the established six phases that introduce the classroom response process: action and impact, the Level 1 steps (warning, seat change, written reflection), practicing the Reset and Return written reflection, and Tap In, Tap Out, and the return to learning. Friday, November 13: Friday Wonder runs as Morning Spark on bouncing back, followed by Friday Cypher.', s)
    s = s.replace('respect and privacy guidance', 'level-by-level scripts and privacy guidance')
    body = re.search(r'<tbody[^>]*>(.*?)</tbody>', s, re.S).group(1)
    first = re.search(r'<tr>.*?</tr>', body, re.S).group(0)
    rows = ''
    for n, dl, short in M.DAYS:
        r = first.replace('Mon Nov 2', {'mon': 'Mon Nov 9', 'tue': 'Tue Nov 10', 'wed': 'Wed Nov 11', 'thu': 'Thu Nov 12'}[short])
        r = r.replace('>Respect Is Something You Do<', f'>{e(M.DAYINFO[n]["title"][0])}<')
        r = re.sub(r'lesson-1-', f'lesson-{n}-', r).replace('#day-1-', f'#day-{n}-')
        rows += r
    s = s.replace(body, rows)
    assert 'November 2' not in s and 'Nov 2<' not in s and 'Respect Is Something' not in s, 'mm leftovers'
    hub = hub[:i] + s + hub[i:]
    hub = re.sub(r'(<p class="text-\[var\(--slate\)\] text-lg">)Week 13 · November 2–5:[^<]*', lambda m: m.group(1) + f'Week {M.WEEK} · November 9–12: {M.THEME[0]}. Lessons that introduce the levels, the written reflection, and the return to learning. Monday through Thursday instruction; Friday Wonder runs in Morning Spark before Friday Cypher.', hub, count=1)
    return add_leetee(hub)

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != '--leetee-only']
    src, dst = args[0], args[1]
    hub = open(src).read()
    out = add_leetee(hub) if '--leetee-only' in sys.argv else make(hub)
    open(dst, 'w').write(out)
    print('hub written', dst)
