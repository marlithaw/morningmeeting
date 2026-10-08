"""Site pages: the topic page (out/<slug>/index.html) and the toolkit home, regenerated from toolkit.py."""
import os, glob, subprocess, importlib.util
from PIL import Image
from common import *

# Recurring Morning Meeting links (AGENTS.md: every page keeps Weekly Videos and Do Now – First 5 visible).
RECUR = '''<div class="recur">
      <div class="grp"><b>Weekly Videos</b>
        <a class="btn sm green" href="https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/relax.mp4" target="_blank" rel="noreferrer">Relax</a>
        <a class="btn sm yellow" href="https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/excite.mp4" target="_blank" rel="noreferrer">Excite</a></div>
      <div class="grp"><b>Do Now – First 5</b>
        <a class="btn sm green" href="https://canva.link/bhu6ll009tiusud" target="_blank" rel="noreferrer">Relax</a>
        <a class="btn sm yellow" href="https://canva.link/jvexkr9edw021uy" target="_blank" rel="noreferrer">Excite</a></div>
    </div>'''

FOOTER = f'''<footer>
  <div class="wrap">
    <span class="logo"><img src="{{p}}shared/img/flame-logo.svg" alt="">Matchbook Learning · K–2 Behavior Toolkit</span>
    <span class="credit">{CREDIT}</span>
  </div>
</footer>
</body>
</html>
'''

ZIP_DESC_SONG = 'Deck, song video, posters, center kit, mini book, teacher guide, and family half-sheets.'
ZIP_DESC = 'Deck, posters, center kit, mini book, teacher guide, and family half-sheets.'


def registry():
    spec = importlib.util.spec_from_file_location('toolkit', os.path.join(KIT, 'toolkit.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def pdf_pages(path, default):
    try:
        from pypdf import PdfReader
        return len(PdfReader(path).pages)
    except Exception:
        return default


def song_length(T, path):
    s = T.get('song') or {}
    if s.get('length'):
        return s['length']
    try:
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                                 capture_output=True, text=True, check=True).stdout)
    except Exception:
        return 'about a minute and a half'
    m, sec = divmod(round(d), 60)
    parts = ([f"{m} minute{'s' if m != 1 else ''}"] if m else []) + ([f"{sec} seconds"] if sec else [])
    return 'about ' + ' '.join(parts)


def topic_page(T, outdir, has_song=None):
    S, N, pr = T['site'], names(T), T['promise']
    if has_song is None:
        has_song = song_source(T, outdir) is not None
    th = lambda f: f"thumbs/{f.rsplit('.', 1)[0]}-1.jpg"
    guide_pages = pdf_pages(os.path.join(outdir, N['guide_pdf']), 4)
    kit_pages = pdf_pages(os.path.join(outdir, N['centers']), 7)
    meta = S.get('meta') or (f"Topic {T['num']} of the K–2 Behavior Toolkit: {'song video, ' if has_song else ''}student deck, "
                             'posters, center kit, Tier 2 mini book, teacher guide, and family half-sheets.')
    hero_style = f' style="object-position:{S["hero_pos"]}"' if S.get('hero_pos') else ''
    watch = ''
    if has_song:
        length = song_length(T, os.path.join(outdir, N['song']))
        watch = f'''
  <!-- WATCH -->
  <section class="group" id="watch" aria-labelledby="watch-h">
    <div class="group-h"><span class="tag" style="background:var(--green)">Watch</span><h2 class="sec" id="watch-h">The {T['title']} song</h2></div>
    <div class="watch">
      <div class="video"><video controls preload="metadata" poster="thumbs/song-poster.jpg" src="{N['song']}"></video></div>
      <div class="note">
        <h3>How to use the song</h3>
        <ul>
          <li>Play it at the start as a preview of today's learning. It runs {length}.</li>
          <li>Captions are on screen so students can read along. The echo parts are in yellow.</li>
          <li>The deck has a <b>Play the song</b> button on slide 1, so you can play it from the deck.</li>
          <li>Replay it during the week as a transition or a reminder.</li>
        </ul>
        <div class="btns" style="margin-top:12px"><a class="btn sm white" href="{N['song']}" download>Download video (MP4)</a></div>
      </div>
    </div>
  </section>
'''
    zip_note = ('All files for this topic in one ZIP, including the song. Keep the deck and the song in the same folder.'
                if has_song else 'All files for this topic in one ZIP.')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T['full_title']} · K–2 Behavior Toolkit | Morning Meeting</title>
<meta name="description" content="{meta}">
<link rel="icon" href="../shared/img/flame-logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="../shared/toolkit.css">
</head>
<body>
<div class="kente"></div>
<div class="wrap">
  <div class="top">
    <a class="logo" href="../../../index.html"><img src="../shared/img/flame-logo.svg" alt="">Matchbook Learning</a>
    <div class="crumbs"><a href="../../../index.html">Morning Meeting</a><span>›</span><a href="../index.html#topics">K–2 Behavior Toolkit</a><span>›</span>Topic {T['num']}</div>
  </div>

  <div class="hero">
    <div>
      <div class="eb">K–2 Behavior Toolkit · Topic {T['num']} of 12 · {T['part']}</div>
      <h1 class="ttl">{' '.join(T['title_lines'])}</h1>
      <p class="sub">{T['subtitle']}</p>
      <div class="say">{pr['en']}</div>
      <p class="langs"><b>ES</b>{pr['es']}<br><b>KR</b>{pr['kr']}</p>
      <div class="btns" style="margin-top:20px">
        <a class="btn" href="{N['deck_html']}" target="_blank" rel="noopener">Open the deck</a>
        <a class="btn yellow" href="{N['zip']}" download>Download all (ZIP)</a>
      </div>
    </div>
    <div class="photo tilt" style="aspect-ratio:4/3"><span class="tape"></span><img src="../shared/img/{S['hero_img']}.jpg" alt="{S['hero_alt']}"{hero_style}></div>
  </div>

  <section class="block" aria-labelledby="recur-h">
    <h2 class="sec" id="recur-h">Start the meeting as usual</h2>
    <p class="sec-sub">This topic replaces the lesson content only.</p>
    {RECUR}
  </section>
{watch}
  <!-- TEACH -->
  <section class="group" id="teach" aria-labelledby="teach-h">
    <div class="group-h"><span class="tag" style="background:var(--red)">Teach</span><h2 class="sec" id="teach-h">Student deck and teacher guide</h2></div>
    <div class="cards">
      <div class="card"><div class="th" style="background-image:url({th(N['deck_pdf'])})"></div><div class="cb">
        <span class="meta">Project it · 7 slides</span><h3>Student deck</h3>
        <p>{S['deck_desc']} Press N for the script and notes. Arrow keys move slides.</p>
        <div class="btns"><a class="btn sm" href="{N['deck_html']}" target="_blank" rel="noopener">Open deck</a><a class="btn sm white" href="{N['deck_pdf']}" target="_blank" rel="noopener">PDF</a></div></div></div>
      <div class="card"><div class="th" style="background-image:url({th(N['guide_pdf'])})"></div><div class="cb">
        <span class="meta">For the teacher · {guide_pages} pages</span><h3>Teacher guide</h3>
        <p>{S['guide_desc']}</p>
        <div class="btns"><a class="btn sm" href="{N['guide_pdf']}" target="_blank" rel="noopener">Open PDF</a><a class="btn sm white" href="{N['guide_docx']}" download>Word</a></div></div></div>
    </div>
  </section>

  <!-- POST -->
  <section class="group" id="post" aria-labelledby="post-h">
    <div class="group-h"><span class="tag" style="background:var(--orange)">Post</span><h2 class="sec" id="post-h">Posters</h2></div>
    <div class="cards">
      <div class="card"><div class="th contain" style="background-image:url({th(N['poster_letter'])})"></div><div class="cb">
        <span class="meta">Color · 8.5 × 11</span><h3>Poster, letter size</h3><p>{S['poster_hint']}</p>
        <div class="btns"><a class="btn sm" href="{N['poster_letter']}" target="_blank" rel="noopener">Open PDF</a></div></div></div>
      <div class="card"><div class="th contain" style="background-image:url({th(N['poster_tabloid'])})"></div><div class="cb">
        <span class="meta">Color · 11 × 17</span><h3>Poster, large</h3><p>{S['poster_large']}</p>
        <div class="btns"><a class="btn sm" href="{N['poster_tabloid']}" target="_blank" rel="noopener">Open PDF</a></div></div></div>
    </div>
  </section>

  <!-- PRACTICE -->
  <section class="group" id="practice" aria-labelledby="practice-h">
    <div class="group-h"><span class="tag" style="background:var(--sky)">Practice</span><h2 class="sec" id="practice-h">Centers and Tier 2</h2></div>
    <div class="cards">
      <div class="card"><div class="th contain" style="background-image:url({th(N['centers'])})"></div><div class="cb">
        <span class="meta">Print one per group · {kit_pages} pages</span><h3>Center kit</h3>
        <p>{S['centers_desc']}</p>
        <div class="btns"><a class="btn sm" href="{N['centers']}" target="_blank" rel="noopener">Open PDF</a></div></div></div>
      <div class="card"><div class="th contain" style="background-image:url({th(N['minibook'])})"></div><div class="cb">
        <span class="meta">Tier 2 · cut and staple</span><h3>Mini book</h3>
        <p>{S['minibook_desc']}</p>
        <div class="btns"><a class="btn sm" href="{N['minibook']}" target="_blank" rel="noopener">Open PDF</a></div></div></div>
    </div>
  </section>

  <!-- FAMILIES -->
  <section class="group" id="families" aria-labelledby="fam-h">
    <div class="group-h"><span class="tag" style="background:var(--char)">Families</span><h2 class="sec" id="fam-h">Family half-sheets</h2></div>
    <div class="cards">
      <div class="card"><div class="th contain" style="background-image:url({th(N['family'])})"></div><div class="cb">
        <span class="meta">English · Español · Kreyòl</span><h3>Family half-sheet</h3>
        <p>{S['family_desc']}</p>
        <div class="btns"><a class="btn sm" href="{N['family']}" target="_blank" rel="noopener">Open PDF</a></div></div></div>
    </div>
  </section>

  <section class="block" aria-labelledby="all-h">
    <div class="dl">
      <div><h3 id="all-h">Download everything</h3><p>{zip_note}</p></div>
      <a class="btn yellow" href="{N['zip']}" download>Download all (ZIP)</a>
    </div>
  </section>
</div>

''' + FOOTER.format(p='../')


def build(T, outdir):
    p = os.path.join(outdir, 'index.html')
    open(p, 'w').write(topic_page(T, outdir))
    return ['index.html']


# ---------------------------------------------------------------- toolkit home

def is_live(t, root):
    return t['status'] == 'live' or os.path.exists(os.path.join(root, t['slug'], 'index.html'))


def home(root=None):
    """Toolkit home index.html from the registry. `root` is the published toolkit folder (for live/song checks)."""
    root = root or publish_root()
    R = registry()
    groups, order = {}, []
    for t in R.TOPICS:
        if t['part'] not in groups:
            groups[t['part']] = []; order.append(t['part'])
        groups[t['part']].append(t)
    blocks = []
    for gi, part in enumerate(order, 1):
        rows = []
        for t in groups[part]:
            if is_live(t, root):
                thumb = f'<div class="thumb" style="background-image:url(shared/img/{t["thumb"]}.jpg)"></div>' if t.get('thumb') else ''
                rows.append(f'''      <a class="topic live" href="{t['slug']}/index.html">{thumb}<div class="body"><span class="num">{t['num']}</span><h3>{t['title']}</h3><p>{t['line']}</p><div class="foot"><span class="pill">Ready to teach</span><span class="meta">Open ›</span></div></div></a>''')
            else:
                rows.append(f'''      <div class="topic soon"><div class="body"><span class="num">{t['num']}</span><h3>{t['title']}</h3><p>{t['line']}</p><div class="foot"><span class="pill g">Coming soon</span></div></div></div>''')
        margin = '6px 0 10px' if gi == 1 else '26px 0 10px'
        blocks.append(f'''    <div class="phase" style="margin:{margin}">Part {gi} · {part}</div>
    <div class="topics">
''' + '\n'.join(rows) + '''
    </div>''')
    topics_html = '\n\n'.join(blocks)
    dls = []
    for t in R.TOPICS:
        if not is_live(t, root):
            continue
        z = f"{slugify(t['title'])}-k2-all-files.zip"
        song = glob.glob(os.path.join(root, t['slug'], '*-song.mp4'))
        desc = t.get('zip_desc') or (ZIP_DESC_SONG if song else ZIP_DESC)
        dls.append(f'''    <div class="dl">
      <div><h3>{t['num']:02d} · {t['title']}</h3><p>{desc}</p></div>
      <a class="btn yellow" href="{t['slug']}/{z}" download>Download ZIP</a>
    </div>''')
    downloads_html = '\n'.join(dls)
    n = len(R.TOPICS)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>K–2 Behavior Toolkit | Morning Meeting</title>
<meta name="description" content="Twelve optional K–2 Morning Meeting topics with Lee &amp; Tee: poster, deck, song, center kit, Tier 2 mini book, teacher guide, and family sheet for each.">
<link rel="icon" href="shared/img/flame-logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="shared/toolkit.css">
</head>
<body>
<div class="kente"></div>
<div class="wrap">
  <div class="top">
    <a class="logo" href="../../index.html"><img src="shared/img/flame-logo.svg" alt="">Matchbook Learning</a>
    <div class="crumbs"><a href="../../index.html">Morning Meeting</a><span>›</span>K–2 Behavior Toolkit</div>
  </div>

  <div class="hero">
    <div>
      <div class="eb">Morning Meeting · K–2 Optional Topic Library</div>
      <h1 class="ttl">K–2 BEHAVIOR TOOLKIT</h1>
      <p class="sub">Lee &amp; Tee teach the skills. Your class practices them together.</p>
      <p class="lead">Twelve topics for Kindergarten to 2nd grade. Teach any topic in place of that day's Morning Meeting content. Each one follows the same Morning Meeting phases your students already know and comes with everything you need to teach, practice, and send home.</p>
      <div class="btns" style="margin-top:20px">
        <a class="btn" href="#topics">See the {n} topics</a>
        <a class="btn white" href="#how">How to use it</a>
      </div>
    </div>
    <div class="photo tilt" style="aspect-ratio:4/3"><span class="tape"></span><img src="shared/img/welcome.jpg" alt="Lee and Tee waving hello"></div>
  </div>

  <section class="block" aria-labelledby="recur-h">
    <h2 class="sec" id="recur-h">Every meeting still starts here</h2>
    <p class="sec-sub">A toolkit topic replaces the lesson content only. Keep your Weekly Video and Do Now – First 5.</p>
    {RECUR}
  </section>

  <section class="block" id="how" aria-labelledby="how-h">
    <h2 class="sec" id="how-h">How to use it</h2>
    <p class="sec-sub">Teach the topics in order when you can. Skills come first, so students have calm-down tools before the safe-choice topics ask them to use those tools. If your class needs a topic now, teach it now. Each one stands on its own.</p>
    <div class="steps">
      <div class="step"><h3>Pick a topic</h3><p>Choose the topic your class needs. Teach it in place of that day's Morning Meeting content.</p></div>
      <div class="step"><h3>Play and teach</h3><p>Play the song as a preview, then teach the 7-slide deck. Press N for your script and notes.</p></div>
      <div class="step"><h3>Practice in centers</h3><p>Print one center kit per group. Students sort, sequence, role-play, and color.</p></div>
      <div class="step"><h3>Follow up</h3><p>Hang the poster. Send the family half-sheet home. Use the mini book with students who need Tier 2 practice.</p></div>
    </div>
    <h3 class="phase" style="margin:26px 0 10px">In every topic</h3>
    <div class="includes"><span>Poster (letter and 11×17)</span><span>7-slide student deck</span><span>Song video</span><span>Center kit</span><span>Tier 2 mini book</span><span>Teacher guide</span><span>Family half-sheet</span><span>English · Español · Kreyòl</span></div>
  </section>

  <section class="block" id="topics" aria-labelledby="topics-h">
    <h2 class="sec" id="topics-h">The {n} topics</h2>
    <p class="sec-sub">New topics open here as they are ready.</p>

{topics_html}
  </section>

  <section class="block" id="downloads" aria-labelledby="dl-h">
    <h2 class="sec" id="dl-h">Offline ZIPs</h2>
    <p class="sec-sub">One ZIP per topic. Download it once and teach without Wi-Fi. Keep the files together in their folder so the deck can play the song.</p>
{downloads_html}
  </section>
</div>

''' + FOOTER.format(p='')


def write_home(root=None):
    root = root or publish_root()
    p = os.path.join(root, 'index.html')
    open(p, 'w').write(home(root))
    return p


def shared_img(key, root=None):
    """Copy a web-sized (max 1000 px, quality 82) version of an image into <root>/shared/img/<key>.jpg."""
    root = root or publish_root()
    d = os.path.join(root, 'shared', 'img'); os.makedirs(d, exist_ok=True)
    dst = os.path.join(d, key + '.jpg')
    im = Image.open(img_path(key)).convert('RGB'); im.thumbnail((1000, 1000))
    im.save(dst, 'JPEG', quality=82, optimize=True)
    return dst
