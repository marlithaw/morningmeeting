#!/usr/bin/env python3
"""Insert MM Week 13 and Spark/Ember Week 5 into the hub (index.html), cloning last week's sections."""
import re, sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from content_se import *
import content_mm as M
from build_pkg import spark_task, FMT
e = lambda s: html.escape(s, quote=False)

def section(hub, lab):
    i = hub.index(f'<section aria-labelledby="{lab}"')
    # sections are not nested inside these weekly sections
    j = hub.index('</section>', i) + len('</section>')
    return i, j

def make(hub):
    SE4 = 'spark-ember/week-4-everyone-belongs'; SE5 = f'spark-ember/{SE_SLUG}'
    MM12 = 'week-12-everyone-belongs'; MM13 = M.SLUG
    TH = 'class="px-3 py-4 text-left align-top"'
    # ---------- Spark ----------
    i, j = section(hub, 'spark-week4-title'); s = hub[i:j]
    s = s.replace('spark-week4-title', f'spark-week{SE_WEEK}-title').replace(SE4, SE5).replace('week-4-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace('Week 4 · Four grade bands · Five formats · October 26–30, 2026', f'Week {SE_WEEK} · Four grade bands · Four formats · November 2–6, 2026')
    s = s.replace('>Everyone Belongs</h2>', f'>{THEME[0]}</h2>')
    s = re.sub(r'(<h2[^>]*spark-week5-title">[^<]*</h2>\s*<p class="text-sm text-slate-300 mt-2 max-w-2xl">)[^<]*', r'\1' + 'Four school days: no school Tuesday, November 3. Monday, Wednesday, and Thursday follow the usual formats on respect and responsibility and hand off to that day’s Morning Meeting lesson. Friday Wonder carries the same theme, then Friday Cypher.', s)
    s = s.replace('Morning Spark Week 4 - All Files.zip', f'Morning Spark Week {SE_WEEK} - All Files.zip')
    s = s.replace('one dated page for each day, Monday to Friday', 'one dated page for each school day')
    s = s.replace('Five dated prompts on the Everyone Belongs theme', f'Four dated prompts on the {THEME[0]} theme')
    s = s.replace('Presentation · Monday to Friday', 'Presentation · Monday, Wednesday, Thursday, Friday')
    s = re.sub(r'Five dated response pages[^<]*', 'Four dated response pages: a private check-in on Monday, then one page each for Wednesday, Thursday, and Friday.', s)
    s = re.sub(r'- Week 4 - Everyone Belongs\.html', f'- Week {SE_WEEK} - {THEME[0]}.html', s).replace('- Week 4 - Student Pages.pdf', f'- Week {SE_WEEK} - Student Pages.pdf')
    rows = ''
    for d in SDAYS:
        cells = ''
        for b in SBANDS:
            if d == 'fri': mm = '<p><strong>Then:</strong> Time for Friday Cypher.</p>'
            else:
                n, en, _ = MM[d]
                if b == '23': mm = f'<p><strong>Then Morning Meeting:</strong> <a href="./resources/{MM13}/lesson-{n}-k2.html">Grade 2: K–2 · {e(en)}</a><br/><a href="./resources/{MM13}/lesson-{n}-35.html">Grade 3: 3–5 · {e(en)}</a></p>'
                else:
                    mb = {'k1': 'k2', '45': '35', '68': '68'}[b]; lb = {'k2': 'K–2', '35': '3–5', '68': '6–8'}[mb]
                    mm = f'<p><strong>Then Morning Meeting:</strong> <a href="./resources/{MM13}/lesson-{n}-{mb}.html">{lb} · {e(en)}</a></p>'
            cells += f'<td {TH}><p>{e(spark_task(b, d))}</p><a href="./resources/{SE5}/morning-spark-{b}.html#{d}">Open dated deck</a>{mm}</td>'
        rows += f'<tr><th {TH}>{DATE[d][0]}<br/>{FMT[d][0]}</th>{cells}</tr>'
    s = re.sub(r'<tbody class="divide-y divide-\[var\(--hairline\)\]">.*?</tbody>', f'<tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody>', s, flags=re.S)
    assert MM12 not in s and 'October' not in s, 'spark leftovers'
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Ember ----------
    i, j = section(hub, 'ember-week4-title'); s = hub[i:j]
    s = s.replace('ember-week4-title', f'ember-week{SE_WEEK}-title').replace(SE4, SE5).replace('week-4-all-files', f'week-{SE_WEEK}-all-files')
    s = s.replace('Dismissal · Week 4 · October 26–30, 2026 · Four grade bands · Five days', f'Dismissal · Week {SE_WEEK} · November 2–6, 2026 · Four grade bands · Four days')
    s = re.sub(r'(<i class="fa-solid fa-fire-flame-curved mr-2" style="color:#E3602A"></i>)Everyone Belongs', r'\1' + THEME[0], s)
    rows = ''
    for k, d in enumerate(SDAYS):
        rows += f'<tr><th {TH}>{DATE[d][0]}</th>' + ''.join(
            f'<td {TH}><a href="https://www.youtube.com/watch?v={EMBER[b]["videos"][k][0]}" rel="noopener" target="_blank">{e(EMBER[b]["videos"][k][1])}</a><small> · {e(EMBER[b]["videos"][k][2])}</small><p>{e(EMBER[b]["prompts"][k][0])}</p><a href="./resources/{SE5}/ember-{b}.html#{d}">Open dated board</a></td>' for b in SBANDS) + '</tr>'
    s = re.sub(r'<tbody class="divide-y divide-\[var\(--hairline\)\]">.*?</tbody>', f'<tbody class="divide-y divide-[var(--hairline)]">{rows}</tbody>', s, flags=re.S)
    assert 'October' not in s and 'Everyone Belongs' not in s, 'ember leftovers'
    hub = hub[:i] + s + '\n\n                    ' + hub[i:]
    # ---------- Instructional Units ----------
    i, j = section(hub, 'week12-title'); s = hub[i:j]
    s = s.replace('week12-title', f'week{M.WEEK}-title').replace(MM12, MM13)
    s = s.replace('Week 12 · October 26–29, 2026', f'Week {M.WEEK} · November 2–5, 2026').replace('>Everyone Belongs</h2>', f'>{M.THEME[0]}</h2>')
    s = s.replace('Open Week 12 toolkit', f'Open Week {M.WEEK} toolkit')
    s = re.sub(r'(<p class="text-sm text-slate-300 mt-2 mb-5">)[^<]*', r'\1' + 'Three 15-minute lessons with the established six phases: what respect looks and sounds like, owning a mistake and repairing it, and keeping the same standard in every space at school. No school Tuesday, November 3. Friday, November 6: Friday Wonder runs as Morning Spark on the same theme, followed by Friday Cypher.', s)
    body = re.search(r'<tbody class="divide-y divide-slate-200">(.*?)</tbody>', s, re.S).group(1)
    first = re.search(r'<tr>.*?</tr>', body, re.S).group(0)
    rows = ''
    for n, dl, short in M.DAYS:
        r = first.replace('Mon Oct 26', {'mon': 'Mon Nov 2', 'wed': 'Wed Nov 4', 'thu': 'Thu Nov 5'}[short]).replace('>Everyone Belongs<', f'>{e(M.DAYINFO[n]["title"][0])}<')
        r = re.sub(r'lesson-1-', f'lesson-{n}-', r).replace('#day-1-k2', f'#day-{n}-k2')
        rows += r
    s = s.replace(body, rows)
    assert 'October' not in s and 'Oct ' not in s, 'mm leftovers'
    hub = hub[:i] + s + hub[i:]
    # intro paragraph
    hub = re.sub(r'(<p class="text-\[var\(--slate\)\] text-lg">)Week 12 · October 26–29:[^<]*', r'\1' + f'Week {M.WEEK} · November 2–5: {M.THEME[0]}. Lessons on what respect looks and sounds like, owning and repairing mistakes, and keeping the same standard in every space. Monday, Wednesday, and Thursday instruction (no school Tuesday); Friday Wonder runs in Morning Spark before Friday Cypher.', hub, count=1)
    return hub

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    out = make(open(src).read()); open(dst, 'w').write(out)
    print('hub written', dst)
