#!/usr/bin/env python3
"""Pre-publish checks for a weekly Morning Meeting unit and a Spark/Ember week.

Checks the rules in AGENTS.md plus the mistakes the last three weekly uploads had to fix
(copied-forward text from the week before, an out-of-date ZIP, a Friday with no button,
hub styling that drifted from earlier weeks).

    python3 _build/weekly/check_week.py                 # newest Morning Meeting unit and Spark/Ember week
    python3 _build/weekly/check_week.py --mm 11 --se 3  # name the weeks

It reads files only. FAIL lines must be fixed before publishing; WARN lines need a look.
It cannot replace the visual check of the live tabs and projected decks (see WORKFLOW.md).
"""
import argparse
import datetime as dt
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
HUB = ROOT / 'index.html'
RES = ROOT / 'resources'

# The recurring links every unit row and weekly section keeps (AGENTS.md).
RECURRING = {
    'Weekly Videos · Relax': 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/relax.mp4',
    'Weekly Videos · Excite': 'https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/excite.mp4',
    'Do Now – First 5 · Relax': 'https://canva.link/bhu6ll009tiusud',
    'Do Now – First 5 · Excite': 'https://canva.link/jvexkr9edw021uy',
}
MM_BANDS = ['k2', '35', '68']
SE_BANDS = ['k1', '23', '45', '68']
SE_BAND_LABELS = ['K–1', '2–3', '4–5', '6–8']
PHASES = ['Regulate', 'Orient', 'Connect', 'Practice', 'Commit', 'Transition']
DAY_KEYS = ['mon', 'tue', 'wed', 'thu', 'fri']
DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
IXL_WEEK_1 = dt.date(2026, 8, 31)  # Week 1 starts Monday, Aug 31, 2026 (the rule in the Spark decks)

results = []


def report(level, msg):
    results.append((level, msg))


def ok(msg):
    report('PASS', msg)


def warn(msg):
    report('WARN', msg)


def fail(msg):
    report('FAIL', msg)


def read(p):
    return p.read_text(encoding='utf-8', errors='replace')


def section(html, labelledby):
    """Return the <section aria-labelledby=...> ... </section> text (sections are not nested)."""
    m = re.search(r'<section[^>]*aria-labelledby="%s"' % re.escape(labelledby), html)
    if not m:
        return None
    end = html.find('</section>', m.end())
    return html[m.start():end if end != -1 else len(html)]


def tab(html, tab_id):
    m = re.search(r'<div id="%s" class="tab-content' % re.escape(tab_id), html)
    if not m:
        return ''
    nxt = re.search(r'<div id="[a-z0-9-]+" class="tab-content', html[m.end():])
    return html[m.start():m.end() + nxt.start() if nxt else len(html)]


def text(fragment):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', fragment)).strip()


def rows(table_html):
    body = table_html.split('<tbody', 1)[-1]
    return re.findall(r'<tr[^>]*>(.*?)</tr>', body, re.S)


def first_table(fragment):
    m = re.search(r'<table.*?</table>', fragment, re.S)
    return m.group(0) if m else ''


def table_class(fragment):
    m = re.search(r'<table class="([^"]*)"', fragment)
    return m.group(1) if m else ''


# ---------------------------------------------------------------- folders

def newest(pattern, rx):
    best = None
    for p in RES.glob(pattern):
        m = re.match(rx, p.name)
        if m and p.is_dir():
            n = int(m.group(1))
            if not best or n > best[0]:
                best = (n, p)
    return best


def mm_folder(n):
    hits = sorted(RES.glob('week-%d-*' % n))
    return hits[0] if hits else None


def se_folder(n):
    hits = sorted((RES / 'spark-ember').glob('week-%d-*' % n))
    return hits[0] if hits else None


# ---------------------------------------------------------------- links

def local_targets(html):
    for attr, url in re.findall(r'\b(href|src)="([^"]+)"', html):
        if re.match(r'^(https?:|mailto:|tel:|data:|javascript:|#)', url) or '{' in url or "'" in url:
            continue
        yield url


def check_links(page, label):
    html = read(page)
    missing, bad_anchor = [], []
    for url in local_targets(html):
        path, _, anchor = url.partition('#')
        path = unquote(path.split('?')[0])
        target = (page.parent / path).resolve() if path else page
        if not target.exists():
            missing.append(url)
            continue
        # Deck day hashes (#mon, #week) are read by script; only check real id anchors on non-deck pages.
        if anchor and target.suffix == '.html' and anchor not in DAY_KEYS + ['week'] \
                and not re.search(r'^(morning-spark|ember)-', target.name):
            if not re.search(r'id="%s"' % re.escape(anchor), read(target)):
                bad_anchor.append(url)
    for u in sorted(set(missing)):
        fail('%s: broken local link %s' % (label, u))
    for u in sorted(set(bad_anchor)):
        warn('%s: link target has no id for anchor %s' % (label, u))
    if not missing and not bad_anchor:
        ok('%s: every local link resolves' % label)


def check_recurring(fragment, label, level=fail):
    gone = [k for k, url in RECURRING.items() if url not in fragment]
    if gone:
        level('%s: missing recurring link(s): %s' % (label, ', '.join(gone)))
    else:
        ok('%s: Weekly Videos and Do Now – First 5 (Relax and Excite) present' % label)


# ---------------------------------------------------------------- ready-to-run copy

# Published pages are finished curriculum: no person is named, and no production notes
# (where copies are, what the material was adapted from, what was made for whom).
PLANNING = re.compile(
    r"\bmailbox(?:es)?\b|\bsource(?:’s|'s)? (?:lesson|lessons|video|videos|clip|routine|theme)s?\b"
    r"|\btranslates? the\b|\boriginal (?:artwork|materials) (?:made|created) for\b"
    r"|\bdo not have the packet\b|\bcopies are in\b|\bplaceholder\b", re.I)
MARKERS = re.compile(r"\bTODO\b|\bTBD\b|\b(?:Mr|Ms|Mrs|Dr)\.? [A-Z][a-z]+"
                     r"|\b[A-Z][a-z]+ [A-Z][a-z]+, (?:[A-Z][a-z]+ )*(?:Coordinator|Director|Principal|Specialist|Coach|Counselor|Teacher|Dean)\b")  # case-sensitive: Spanish "todo" is fine
NAMED = re.compile(r"“([A-Z][a-z]+), (?:you|what|which|how|who|why|can|tell|show|point|read|share)\b"
                   r"|“(?:Respectful|Safe|Responsible): ([A-Z][a-z]+) [a-z]+")
NOT_NAMES = {'You', 'Your', 'We', 'Our', 'Everyone', 'Today', 'Now', 'Next', 'Yes', 'No', 'Okay', 'Thank', 'Great'}


def page_text(p):
    if p.suffix == '.pdf':
        try:
            import subprocess
            return subprocess.run(['pdftotext', str(p), '-'], capture_output=True, text=True).stdout
        except OSError:
            return ''
    s = re.sub(r'<style.*?</style>|<script.*?</script>', ' ', read(p), flags=re.S)
    attrs = ' '.join(re.findall(r'data-(?:en|es)="([^"]*)"', s))
    return text(s) + ' ' + attrs


def check_ready_to_run(folder, label):
    hits = []
    for p in sorted(list(folder.glob('*.html')) + list(folder.glob('*.pdf'))):
        t = page_text(p)
        named = [m for m in NAMED.finditer(t) if (m.group(1) or m.group(2)) not in NOT_NAMES]
        for m in list(PLANNING.finditer(t)) + list(MARKERS.finditer(t)) + named:
            hits.append('%s: "%s"' % (p.name, t[max(0, m.start() - 30):m.end() + 30].strip()))
    for h in hits[:12]:
        fail('%s: names a person or carries a production note, %s' % (label, h))
    if not hits:
        ok('%s: no person named and no production notes' % label)


# ---------------------------------------------------------------- stale text

def check_stale(folder, label, prev_week_strings):
    """Flag text copied forward from the week before (the Week 10 → Week 11 lesson regression)."""
    hits = {}
    for p in sorted(folder.glob('*.html')):
        s = read(p)
        for needle in prev_week_strings:
            if needle and needle in s:
                hits.setdefault(needle, []).append(p.name)
    if hits:
        for needle, files in hits.items():
            warn('%s: text from the previous week "%s" in %s' % (label, needle, ', '.join(files[:6]) + (' …' if len(files) > 6 else '')))
    else:
        ok('%s: no text carried over from the previous week' % label)


def titles(folder):
    out = {}
    for p in folder.glob('*.html'):
        m = re.search(r'<title>([^<]*)</title>', read(p))
        if m:
            out[p.name] = m.group(1).strip()
    return out


# ---------------------------------------------------------------- dates

def dates_in(s):
    """Monday October 19 → date (year 2026 unless the month is January to July, then 2027)."""
    found = []
    for day, month, num in re.findall(r'(%s)(?:,| ·)? (%s)[a-z]*\.? (\d{1,2})\b' % ('|'.join(DAY_NAMES), '|'.join(m[:3] for m in MONTHS)), s):
        mi = [m[:3] for m in MONTHS].index(month) + 1
        year = 2026 if mi >= 8 else 2027
        try:
            d = dt.date(year, mi, int(num))
        except ValueError:
            continue
        found.append((day, d))
    return found


def check_weekdays(found, label):
    wrong = [(day, d) for day, d in found if DAY_NAMES[d.weekday()] != day if d.weekday() < 5] + \
            [(day, d) for day, d in found if d.weekday() >= 5]
    if wrong:
        for day, d in wrong:
            fail('%s: "%s %s %d" is a %s' % (label, day, MONTHS[d.month - 1], d.day, d.strftime('%A')))
    elif found:
        ok('%s: weekday names match the dates' % label)


# ---------------------------------------------------------------- Morning Meeting unit

def check_mm(n, hub):
    folder = mm_folder(n)
    if not folder:
        fail('Morning Meeting Week %d: no resources/week-%d-* folder' % (n, n))
        return
    label = 'MM Week %d' % n
    rel = folder.relative_to(ROOT).as_posix()

    units = tab(hub, 'instructional-units')
    sec = section(units, 'week%d-title' % n)
    if not sec:
        fail('%s: no hub section aria-labelledby="week%d-title" in Instructional Units' % (label, n))
        sec = ''  # still check the unit folder
    newest_mm = mm_folder(n + 1) is None and bool(sec)
    first = re.search(r'<section[^>]*aria-labelledby="(week\d+-title)"', units)
    if not newest_mm:
        pass  # archived week: a newer unit sits above it
    elif first and first.group(1) != 'week%d-title' % n:
        fail('%s: hub section is not the first unit in Instructional Units (first is %s)' % (label, first.group(1)))
    else:
        ok('%s: hub section is first in Instructional Units' % label)
    for older in range(n - 1, max(n - 4, 0), -1):
        if mm_folder(older) and not section(units, 'week%d-title' % older):
            fail('%s: earlier Week %d section is missing from the hub (archive must stay)' % (label, older))
    intro = re.search(r'<div class="mb-8">\s*<p[^>]*>(.*?)</p>', units, re.S)
    if not newest_mm:
        pass
    elif intro and ('Week %d' % n) not in intro.group(1):
        fail('%s: Instructional Units intro paragraph still names another week: "%s"' % (label, text(intro.group(1))[:90]))
    elif intro:
        ok('%s: Instructional Units intro names Week %d' % (label, n))

    unit_bands = sorted({m.group(1) for p in folder.glob('lesson-*.html') for m in [re.match(r'lesson-\d+-(\w+)\.html', p.name)] if m})
    if unit_bands != sorted(MM_BANDS):
        warn('%s: deck bands %s differ from the K–2 / 3–5 / 6–8 set used since Week 10' % (label, ', '.join(unit_bands)))
    menu = rows(first_table(sec))
    if sec and not menu:
        fail('%s: hub section has no daily menu rows' % label)
    for i, r in enumerate(menu, 1):
        cells = text(r)[:40]
        gone = [k for k, url in RECURRING.items() if url not in r]
        bands = [b for b in unit_bands if '%s/lesson-' % rel not in r or not re.search(r'lesson-\d+-%s\.html' % b, r)]
        if gone:
            fail('%s: menu row %d (%s) missing %s' % (label, i, cells, ', '.join(gone)))
        if bands and 'cypher' not in r.lower():
            fail('%s: menu row %d (%s) missing deck link(s) for %s' % (label, i, cells, ', '.join(bands)))
    if menu and all(all(u in r for u in RECURRING.values()) for r in menu):
        ok('%s: all %d menu rows carry Videos and Do Now – First 5 (Relax and Excite)' % (label, len(menu)))
    cards = len(re.findall(r'Print toolkit', sec))
    if sec:
        (ok if cards >= 3 and 'Teacher scripts' in sec else fail)(
            '%s: hub cards: Teacher scripts %s, %d print toolkit card(s)' % (label, 'present' if 'Teacher scripts' in sec else 'MISSING', cards))

    unit_hub = folder / 'index.html'
    if unit_hub.exists():
        uh = read(unit_hub)
        check_recurring(uh, '%s unit hub' % label)
        if 'weekly videos' not in uh.lower() or 'do now' not in uh.lower():
            fail('%s unit hub: no visible "Weekly Videos" / "Do Now" section heading' % label)
    else:
        fail('%s: %s/index.html missing' % (label, rel))

    decks = sorted(folder.glob('lesson-*.html'))
    if not decks:
        fail('%s: no lesson-*.html decks' % label)
    short = []
    for d in decks:
        s = text(read(d))
        lacking = [ph for ph in PHASES if ph not in s]
        if lacking:
            short.append('%s (%s)' % (d.name, ', '.join(lacking)))
    if short:
        fail('%s: decks missing six-phase labels: %s' % (label, '; '.join(short)))
    elif decks:
        ok('%s: all %d decks show the six phases' % (label, len(decks)))
    for b in unit_bands:
        if not (folder / ('printables-%s.html' % b)).exists():
            fail('%s: no printables-%s.html for the %s decks' % (label, b, b))
    wrong_week = [f for f, t in titles(folder).items() if f.startswith('lesson-') and not t.startswith('Week %d' % n)]
    if wrong_week:
        fail('%s: deck <title> does not start with "Week %d": %s' % (label, n, ', '.join(sorted(wrong_week))))

    check_weekdays(dates_in(text(sec)) + [x for d in decks for x in dates_in(text(read(d)))], label)

    check_ready_to_run(folder, label)

    prev = mm_folder(n - 1)
    if prev:
        prev_titles = {t.split(' · ', 1)[-1].rsplit(' · ', 1)[0] for f, t in titles(prev).items() if f.startswith('lesson-')}
        check_stale(folder, label, ['Week %d ·' % (n - 1)] + sorted(t for t in prev_titles if len(t.split()) >= 3))

    for p in [unit_hub] + decks + sorted(folder.glob('printables-*.html')) + [folder / 'teacher-guide.html', folder / 'media.html']:
        if p.exists():
            check_links(p, '%s/%s' % (label, p.name))


# ---------------------------------------------------------------- Spark / Ember week

def ixl_week(monday):
    return (monday - IXL_WEEK_1).days // 7 + 1


def ember_data(html):
    m = re.search(r'const EMBER=(\{.*?\});\s*\n', html, re.S)
    try:
        return json.loads(m.group(1)) if m else None
    except ValueError:
        return None


def rail(html):
    """Visible text and release times of the dismissal rail, ignoring attribute order."""
    m = re.search(r'<aside class="rail".*?</aside>', html, re.S)
    if not m:
        return None
    return re.findall(r'data-t="([^"]+)"', m.group(0)), text(m.group(0))


def check_se(n, hub):
    folder = se_folder(n)
    label = 'Spark/Ember Week %d' % n
    if not folder:
        fail('%s: no resources/spark-ember/week-%d-* folder' % (label, n))
        return
    rel = folder.relative_to(ROOT).as_posix()

    for tab_id, prefix, word in (('morning-spark', 'spark', 'Spark'), ('ember', 'ember', 'Ember')):
        t = tab(hub, tab_id)
        sec = section(t, '%s-week%d-title' % (prefix, n))
        lab = '%s tab Week %d' % (word, n)
        if not sec:
            fail('%s: no section aria-labelledby="%s-week%d-title"' % (lab, prefix, n))
            continue
        order = re.findall(r'aria-labelledby="%s-(week\d+-title|title)"' % prefix, t)
        if se_folder(n + 1):
            pass  # archived week: a newer week sits above it
        elif order and order[0] != 'week%d-title' % n:
            fail('%s: not the first weekly section (first is %s)' % (lab, order[0]))
        else:
            ok('%s: first weekly section in the tab' % lab)
        for older in range(n - 1, 1, -1):
            if 'week%d-title' % older not in order:
                fail('%s: archived Week %d section missing' % (lab, older))
        head = text(re.search(r'<div[^>]*uppercase mb-2"[^>]*>(.*?)</div>', sec, re.S).group(1)) if 'uppercase mb-2' in sec else ''
        if ('Week %d' % n) not in head or not re.search(r'(%s) \d' % '|'.join(MONTHS), head):
            fail('%s: header must show "Week %d" and the school dates (found "%s")' % (lab, n, head))
        else:
            ok('%s: header shows week number and dates (%s)' % (lab, head))
        check_recurring(sec, lab)
        missing_bands = [b for b in SE_BAND_LABELS if 'Grades %s' % b not in sec]
        (fail if missing_bands else ok)('%s: grade-band cards %s' % (lab, ('missing ' + ', '.join(missing_bands)) if missing_bands else 'K–1, 2–3, 4–5, 6–8'))
        for need, what in (('teacher-guide.pdf', 'teacher guide PDF'), ('#teacher-guide', 'dated teacher guide'), ('.zip', 'download-all ZIP')):
            if need not in sec:
                fail('%s: no %s link' % (lab, what))
        if prefix == 'spark' and '-student-pages.pdf' not in sec:
            fail('%s: no printable student pages' % lab)
        if prefix == 'ember' and '-reflection-slips.pdf' not in sec:
            fail('%s: no printable reflection slips' % lab)

        table = first_table(sec[sec.find('<table'):]) if '<table' in sec else ''
        days = rows(table)
        if not days:
            fail('%s: no week-at-a-glance table' % lab)
            continue
        found = dates_in(text(table))
        check_weekdays(found, lab)
        kind = 'morning-spark' if prefix == 'spark' else 'ember'
        for r in days:
            cell = re.search(r'<(th|td)[^>]*>(.*?)</\1>', r, re.S)
            head_cell = text(cell.group(2)) if cell else '?'
            key = next((k for k, name in zip(DAY_KEYS, DAY_NAMES) if head_cell.startswith(name)), None)
            want = ['%s/%s-%s.html#%s' % (rel, kind, b, key) for b in SE_BANDS]
            gone = [w.split('/')[-1] for w in want if w not in r]
            if gone:
                fail('%s: row "%s" lacks direct band links: %s' % (lab, head_cell[:30], ', '.join(gone)))
            if prefix == 'ember' and len(re.findall(r'youtube\.com/watch\?v=|youtu\.be/', r)) < 4:
                fail('%s: row "%s" needs the actual video link for each band' % (lab, head_cell[:30]))
        if prefix == 'spark':
            formats = ['Check-In', 'Picture of the Day', 'Zoom In', 'Would You Rather', 'Friday Wonder']
            for r, f in zip(days, formats):
                if f not in text(r):
                    fail('%s: row "%s" should be %s' % (lab, text(r)[:30], f))
        has_fri = any(day == 'Friday' for day, _ in found)
        if not has_fri and 'No school Friday' not in sec and 'no school' not in sec.lower():
            warn('%s: no Friday row and no "No school Friday" note; confirm against the school calendar' % lab)
        if found:
            ok('%s: %d dated days (%s)' % (lab, len(days), ', '.join('%s %d/%d' % (d[:3], x.month, x.day) for d, x in found)))

    # ---- package folder
    for b in SE_BANDS:
        for f in ('morning-spark-%s.html', 'morning-spark-%s-student-pages.pdf', 'ember-%s.html', 'ember-%s-reflection-slips.pdf'):
            if not (folder / (f % b)).exists():
                fail('%s: missing %s' % (label, f % b))
    for f in ('index.html', 'teacher-guide.html', 'teacher-guide.pdf', 'media-sources.json'):
        if not (folder / f).exists():
            fail('%s: missing %s' % (label, f))

    # Friday button on every deck when Friday is taught (the Week 3 "visible control" fix).
    spark_tab = section(tab(hub, 'morning-spark'), 'spark-week%d-title' % n) or ''
    if not spark_tab and (folder / 'index.html').exists():
        spark_tab = read(folder / 'index.html')  # hub not edited yet: use the package page's Spark glance table
    week_days = [k for k, name in zip(DAY_KEYS, DAY_NAMES) if '%s ' % name in text(first_table(spark_tab[spark_tab.find('<table'):]) if '<table' in spark_tab else '')]
    for b in SE_BANDS:
        p = folder / ('morning-spark-%s.html' % b)
        if not p.exists():
            continue
        s = read(p)
        chips = set(re.findall(r'data-go="([a-z]+)"', s))
        extra, lacking = chips - set(week_days), set(week_days) - chips
        if lacking:
            fail('%s: %s has no day button for %s' % (label, p.name, ', '.join(sorted(lacking))))
        if extra and week_days:
            fail('%s: %s has a day button for a non-school day: %s' % (label, p.name, ', '.join(sorted(extra))))
        if week_days and not lacking and not extra:
            ok('%s: %s has a day button for each school day' % (label, p.name))
        if b == 'k1':
            continue  # K–1 reads a book after the Do Now; no IXL codes
        m = re.search(r'var w = (\d+);', s)
        mondays = [x for d, x in dates_in(text(spark_tab)) if d == 'Monday']
        if mondays and m:
            want = ixl_week(mondays[0])
            if int(m.group(1)) != want:
                fail('%s: %s pins IXL week %s; %s is IXL week %d (Aug 31 rule)' % (label, p.name, m.group(1), mondays[0], want))
            elif not re.search(r'"%d":\s*\{' % want, s):
                fail('%s: %s embedded IXL snapshot has no week %d' % (label, p.name, want))
            else:
                stale = re.search(r'pinned to IXL Week (\d+) for ([^*]+?)\s*\(', s)
                if stale and int(stale.group(1)) != want:
                    warn('%s: %s comment still says "pinned to IXL Week %s for %s" (data is week %d)' % (label, p.name, stale.group(1), stale.group(2), want))
                ok('%s: %s pins IXL week %d for %s' % (label, p.name, want, mondays[0]))
        elif not m:
            warn('%s: %s has no IXL week pin (var w = N)' % (label, p.name))
    ixl = list(folder.glob('ixl-week-*-source.json'))
    if not ixl:
        warn('%s: no ixl-week-N-source.json saved with the package' % label)

    # Ember boards: one video per school day; dismissal text and release rail unchanged from last week.
    prev = se_folder(n - 1)
    for b in SE_BANDS:
        p = folder / ('ember-%s.html' % b)
        if not p.exists():
            continue
        s = read(p)
        data = ember_data(s)
        if data is None:
            warn('%s: %s has no EMBER data block' % (label, p.name))
            continue
        vids = len(data.get('videos', []))
        if week_days and vids != len(week_days):
            fail('%s: %s has %d videos for %d school days' % (label, p.name, vids, len(week_days)))
        old = prev / p.name if prev else None
        if old and old.exists():
            od = ember_data(read(old)) or {}
            changed = [k for k in ('pack', 'slip') if od.get(k) != data.get(k)]
            if rail(read(old)) != rail(s):
                changed.append('release rail (groups, times, or order)')
            if changed:
                fail('%s: %s changed fixed dismissal content vs Week %d: %s' % (label, p.name, n - 1, ', '.join(changed)))
            else:
                ok('%s: %s keeps last week\'s seated pack-up, Chromebook return, and release rail' % (label, p.name))
        else:
            for phrase in ('Chromebook', 'number in the cart', 'No lining up'):
                if phrase not in s:
                    fail('%s: %s lost the fixed dismissal text "%s"' % (label, p.name, phrase))

    # Download-all ZIP must match the files on disk (the Week 3 "keep downloadable week current" fix).
    check_ready_to_run(folder, label)

    zips = list(folder.glob('*.zip'))
    if not zips:
        fail('%s: no download-all ZIP' % label)
    for z in zips:
        with zipfile.ZipFile(z) as zf:
            names = {i.filename: i for i in zf.infolist() if not i.is_dir()}
            stale, absent = [], []
            for name, info in names.items():
                disk = folder / name
                if not disk.exists():
                    absent.append(name)
                elif zf.read(name) != disk.read_bytes():
                    stale.append(name)
            on_disk = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and p.suffix != '.zip'}
            not_zipped = sorted(on_disk - set(names))
        if stale:
            fail('%s: %s is out of date for %s' % (label, z.name, ', '.join(sorted(stale)[:8])))
        if absent:
            warn('%s: %s holds files not in the folder: %s' % (label, z.name, ', '.join(sorted(absent)[:8])))
        if not_zipped:
            fail('%s: %s is missing %s' % (label, z.name, ', '.join(not_zipped[:8])))
        if not stale and not not_zipped:
            ok('%s: %s matches the folder (%d files)' % (label, z.name, len(names)))

    prev = se_folder(n - 1)
    if prev:
        prev_strings = []
        ph = read(prev / 'index.html') if (prev / 'index.html').exists() else ''
        t = re.search(r'<title>([^<]*)</title>', ph)
        if t and '·' in t.group(1):
            prev_strings.append(t.group(1).split('·')[-1].strip())
        for day, d in dates_in(text(ph))[:1]:
            prev_strings.append('%s %d' % (MONTHS[d.month - 1], d.day))
        check_stale(folder, label, [s for s in prev_strings if s])

    for p in [folder / 'index.html', folder / 'teacher-guide.html'] + sorted(folder.glob('morning-spark-*.html')) + sorted(folder.glob('ember-*.html')):
        if p.exists():
            check_links(p, '%s/%s' % (label, p.name))


# ---------------------------------------------------------------- hub style parity

def check_style(hub, mm, se):
    """New tables and sections should reuse the classes the earlier weeks use (the Ember table restyle)."""
    for prefix, word in (('spark', 'Spark'), ('ember', 'Ember')):
        t = tab(hub, 'morning-spark' if prefix == 'spark' else 'ember')
        new, old = section(t, '%s-week%d-title' % (prefix, se)), section(t, '%s-week%d-title' % (prefix, se - 1))
        if new and old:
            a, b = table_class(new[new.find('<table'):]), table_class(old[old.find('<table'):])
            if a != b:
                css_known = re.search(r'\.%s\b' % re.escape(a.split()[0]), hub) if a else None
                warn('%s tab: Week %d table class "%s" differs from Week %d "%s"%s; compare them on screen'
                     % (word, se, a, se - 1, b, '' if css_known or '[' in a or '-' not in a else ' and has no CSS rule in index.html'))
            else:
                ok('%s tab: Week %d table styling matches Week %d' % (word, se, se - 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--mm', type=int, help='Morning Meeting unit week number (default: newest folder)')
    ap.add_argument('--se', type=int, help='Spark/Ember week number (default: newest folder)')
    ap.add_argument('--quiet', action='store_true', help='show only WARN and FAIL')
    a = ap.parse_args()
    mm = a.mm or (newest('week-*', r'week-(\d+)-') or (None,))[0]
    se = a.se or (newest('spark-ember/week-*', r'week-(\d+)-') or (None,))[0]
    hub = read(HUB)

    if mm:
        check_mm(mm, hub)
    if se:
        check_se(se, hub)
        check_style(hub, mm, se)
    check_links(HUB, 'index.html')

    counts = {k: 0 for k in ('PASS', 'WARN', 'FAIL')}
    for level, msg in results:
        counts[level] += 1
        if not (a.quiet and level == 'PASS'):
            print('%-4s  %s' % (level, msg))
    print('\nMorning Meeting Week %s · Spark/Ember Week %s: %d pass, %d warn, %d fail'
          % (mm, se, counts['PASS'], counts['WARN'], counts['FAIL']))
    sys.exit(1 if counts['FAIL'] else 0)


if __name__ == '__main__':
    main()
