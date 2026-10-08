"""Topic web page, thumbnails, song, offline ZIP, and the toolkit home's topic menu."""
import os, re, shutil, subprocess, zipfile, html as H
from PIL import Image
from common import *

RECUR = '''<div class="recur">
      <div class="grp"><b>Weekly Videos</b>
        <a class="btn sm green" href="https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/relax.mp4" target="_blank" rel="noreferrer">Relax</a>
        <a class="btn sm yellow" href="https://marlithaw.github.io/CC-Teacher_Edition/resources/videos/excite.mp4" target="_blank" rel="noreferrer">Excite</a></div>
      <div class="grp"><b>Do Now – First 5</b>
        <a class="btn sm green" href="https://canva.link/bhu6ll009tiusud" target="_blank" rel="noreferrer">Relax</a>
        <a class="btn sm yellow" href="https://canva.link/jvexkr9edw021uy" target="_blank" rel="noreferrer">Excite</a></div>
    </div>'''


def shared_img(name):
    """Copy a web-sized version of an art file into the site's shared/img folder."""
    dst = os.path.join(SITE, 'shared', 'img', name + '.jpg')
    if not os.path.exists(dst):
        im = Image.open(os.path.join(ASSETS, 'img', name + '.jpg')).convert('RGB'); im.thumbnail((1000, 1000))
        im.save(dst, quality=82, optimize=True)
    return f'shared/img/{name}.jpg'


def page(t, N):
    S = t['site']; pe, ps, pk = t['promise']
    song = t.get('song')
    watch = ''
    if song:
        watch = f'''
  <section class="group" id="watch" aria-labelledby="watch-h">
    <div class="group-h"><span class="tag" style="background:var(--green)">Watch</span><h2 class="sec" id="watch-h">The {t['short']} song</h2></div>
    <div class="watch">
      <div class="video"><video controls preload="metadata" poster="thumbs/song-poster.jpg" src="{N['song']}"></video></div>
      <div class="note">
        <h3>How to use the song</h3>
        <ul>
          <li>Play it at the start as a preview of today's learning. It runs {song['length']}.</li>
          <li>Captions are on screen so students can read along. The echo parts are in yellow.</li>
          <li>The deck has a <b>Play the song</b> button on slide 1, so you can play it from the deck.</li>
          <li>Replay it during the week as a transition or a reminder.</li>
        </ul>
        <div class="btns" style="margin-top:12px"><a class="btn sm white" href="{N['song']}" download>Download video (MP4)</a></div>
      </div>
    </div>
  </section>
'''
    th = lambda f: f"thumbs/{f.rsplit('.', 1)[0]}-1.jpg"
    card = lambda thumb, meta, title, desc, btns, contain=True: f'''      <div class="card"><div class="th{' contain' if contain else ''}" style="background-image:url({thumb})"></div><div class="cb">
        <span class="meta">{meta}</span><h3>{title}</h3><p>{desc}</p>
        <div class="btns">{btns}</div></div></div>
'''
    pdf_btn = lambda f, label='Open PDF': f'<a class="btn sm" href="{f}" target="_blank" rel="noopener">{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']} · K–2 Behavior Toolkit | Morning Meeting</title>
<meta name="description" content="Topic {t['num']} of the K–2 Behavior Toolkit: {'song video, ' if song else ''}student deck, posters, center kit, Tier 2 mini book, teacher guide, and family half-sheets.">
<link rel="icon" href="../shared/img/flame-logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="../shared/toolkit.css">
</head>
<body>
<div class="kente"></div>
<div class="wrap">
  <div class="top">
    <a class="logo" href="../../../index.html"><img src="../shared/img/flame-logo.svg" alt="">Matchbook Learning</a>
    <div class="crumbs"><a href="../../../index.html">Morning Meeting</a><span>›</span><a href="../index.html#topics">K–2 Behavior Toolkit</a><span>›</span>Topic {t['num']}</div>
  </div>

  <div class="hero">
    <div>
      <div class="eb">K–2 Behavior Toolkit · Topic {t['num']} of 12 · {t['part']}</div>
      <h1 class="ttl">{' '.join(t['title_lines'])}</h1>
      <p class="sub">{t['sub']}</p>
      <div class="say">{pe}</div>
      <p class="langs"><b>ES</b>{ps}<br><b>KR</b>{pk}</p>
      <div class="btns" style="margin-top:20px">
        <a class="btn" href="{N['deck_html']}" target="_blank" rel="noopener">Open the deck</a>
        <a class="btn yellow" href="{N['zip']}" download>Download all (ZIP)</a>
      </div>
    </div>
    <div class="photo tilt" style="aspect-ratio:4/3"><span class="tape"></span><img src="../{shared_img(S['hero_img'])}" alt="{S['hero_alt']}" style="object-position:{S.get('hero_pos', 'center 20%')}"></div>
  </div>

  <section class="block" aria-labelledby="recur-h">
    <h2 class="sec" id="recur-h">Start the meeting as usual</h2>
    <p class="sec-sub">This topic replaces the lesson content only.</p>
    {RECUR}
  </section>
{watch}
  <section class="group" id="teach" aria-labelledby="teach-h">
    <div class="group-h"><span class="tag" style="background:var(--red)">Teach</span><h2 class="sec" id="teach-h">Student deck and teacher guide</h2></div>
    <div class="cards">
{card(th(N['deck_pdf']), 'Project it · 7 slides', 'Student deck', S['story_desc'] + ' Press N for the script and notes. Arrow keys move slides.', pdf_btn(N['deck_html'], 'Open deck') + f'<a class="btn sm white" href="{N["deck_pdf"]}" target="_blank" rel="noopener">PDF</a>', False)}{card(th(N['guide_pdf']), 'For the teacher · 4 pages', 'Teacher guide', S['guide_desc'], pdf_btn(N['guide_pdf']) + f'<a class="btn sm white" href="{N["guide_docx"]}" download>Word</a>', False)}    </div>
  </section>

  <section class="group" id="post" aria-labelledby="post-h">
    <div class="group-h"><span class="tag" style="background:var(--orange)">Post</span><h2 class="sec" id="post-h">Posters</h2></div>
    <div class="cards">
{card(th(N['poster_letter']), 'Color · 8.5 × 11', 'Poster, letter size', S['poster_hint'], pdf_btn(N['poster_letter']))}{card(th(N['poster_tabloid']), 'Color · 11 × 17', 'Poster, large', 'The same poster, sized for a hallway or the front of the room.', pdf_btn(N['poster_tabloid']))}    </div>
  </section>

  <section class="group" id="practice" aria-labelledby="practice-h">
    <div class="group-h"><span class="tag" style="background:var(--sky)">Practice</span><h2 class="sec" id="practice-h">Centers and Tier 2</h2></div>
    <div class="cards">
{card(th(N['centers']), 'Print one per group · 7 pages', 'Center kit', S['centers_desc'], pdf_btn(N['centers']))}{card(th(N['minibook']), 'Tier 2 · cut and staple', 'Mini book', S['minibook_desc'], pdf_btn(N['minibook']))}    </div>
  </section>

  <section class="group" id="families" aria-labelledby="fam-h">
    <div class="group-h"><span class="tag" style="background:var(--char)">Families</span><h2 class="sec" id="fam-h">Family half-sheets</h2></div>
    <div class="cards">
{card(th(N['family']), 'English · Español · Kreyòl', 'Family half-sheet', S['family_desc'], pdf_btn(N['family']))}    </div>
  </section>

  <section class="block" aria-labelledby="all-h">
    <div class="dl">
      <div><h3 id="all-h">Download everything</h3><p>All files for this topic in one ZIP{', including the song. Keep the deck and the song in the same folder' if song else ''}.</p></div>
      <a class="btn yellow" href="{N['zip']}" download>Download all (ZIP)</a>
    </div>
  </section>
</div>

<footer>
  <div class="wrap">
    <span class="logo"><img src="../shared/img/flame-logo.svg" alt="">Matchbook Learning · K–2 Behavior Toolkit</span>
    <span class="credit">{CREDIT}</span>
  </div>
</footer>
</body>
</html>
'''


def build(t, dest=None):
    """Assemble the publishable topic folder. dest defaults to out/<folder>/site (a preview, not the live site)."""
    N, od = names(t), out_dir(t)
    dest = dest or os.path.join(od, 'site')
    os.makedirs(os.path.join(dest, 'thumbs'), exist_ok=True)
    files = [N[k] for k in ['deck_html', 'deck_pdf', 'poster_letter', 'poster_tabloid', 'centers', 'minibook', 'guide_docx', 'guide_pdf', 'family']]
    for f in files:
        shutil.copy2(os.path.join(od, f), os.path.join(dest, f))
    for f in files:
        if f.endswith('.pdf'):
            subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-r', '50', '-jpeg', '-jpegopt', 'quality=80', os.path.join(dest, f),
                            os.path.join(dest, 'thumbs', f.rsplit('.', 1)[0])], check=True)
    if t.get('song'):
        src = os.path.normpath(os.path.join(KIT, t['song']['file']))
        if os.path.abspath(src) != os.path.abspath(os.path.join(dest, N['song'])):
            shutil.copy2(src, os.path.join(dest, N['song']))
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t['song'].get('poster_at', 2.5)), '-i', os.path.join(dest, N['song']),
                        '-frames:v', '1', '-q:v', '4', os.path.join(dest, 'thumbs', 'song-poster.jpg')], check=True)
        files.append(N['song'])
    open(os.path.join(dest, 'index.html'), 'w').write(page(t, N))
    # offline ZIP
    zp = os.path.join(dest, N['zip'])
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in [x for x in files if not x.endswith('Teacher-Guide.pdf')] + [N['guide_pdf']]:
            z.write(os.path.join(dest, f), f"{N['zip_folder']}/{f}")
        readme = (f"{t['title']} · K-2 Behavior Toolkit · Topic {t['num']} of 12\nMatchbook Learning Morning Meeting\n\n"
                  f"Open {N['deck_html']} in Chrome to teach. Press N for notes.\n")
        if t.get('song'):
            readme += f"Slide 1 has a Play the song button. Keep {N['song']} in this same folder so it plays.\n"
        readme += f"\n{CREDIT_TXT}\n"
        z.writestr(f"{N['zip_folder']}/README.txt", readme)
    return dest


def update_menu():
    """Regenerate the topic grid and the offline ZIP list on the toolkit home from topics/_menu.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('menu', os.path.join(KIT, 'topics', '_menu.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    idx = os.path.join(SITE, 'index.html'); s = open(idx).read()

    def tile(num, title, line, folder):
        live = os.path.exists(os.path.join(SITE, folder, 'index.html'))
        if not live:
            return f'''      <div class="topic soon"><div class="body"><span class="num">{num}</span><h3>{H.escape(title)}</h3><p>{H.escape(line)}</p><div class="foot"><span class="pill g">Coming soon</span></div></div></div>\n'''
        t = load_topic(folder)
        return f'''      <a class="topic live" href="{folder}/index.html"><div class="thumb" style="background-image:url({shared_img(t['site']['card_img'])})"></div><div class="body"><span class="num">{num}</span><h3>{H.escape(title)}</h3><p>{H.escape(line)}</p><div class="foot"><span class="pill">Ready to teach</span><span class="meta">Open ›</span></div></div></a>\n'''

    part1 = ''.join(tile(*x) for x in m.MENU[:6]); part2 = ''.join(tile(*x) for x in m.MENU[6:])
    grid = (f'''<!-- TOPICS:START (generated by _build/k2-toolkit/builder/site.py) -->
    <div class="phase" style="margin:6px 0 10px">Part 1 · Skills I can use</div>
    <div class="topics">
{part1}    </div>

    <div class="phase" style="margin:26px 0 10px">Part 2 · Safe choices</div>
    <div class="topics">
{part2}    </div>
    <!-- TOPICS:END -->''')
    s = re.sub(r'<!-- TOPICS:START.*?<!-- TOPICS:END -->', lambda _: grid, s, flags=re.S)
    dls = ''
    for num, title, line, folder in m.MENU:
        if os.path.exists(os.path.join(SITE, folder, 'index.html')):
            t = load_topic(folder); N = names(t)
            what = ('Deck, song video, posters, ' if t.get('song') else 'Deck, posters, ') + 'center kit, mini book, teacher guide, and family half-sheets.'
            dls += f'''    <div class="dl" style="margin-bottom:12px">
      <div><h3>{num:02d} · {H.escape(title)}</h3><p>{what}</p></div>
      <a class="btn yellow" href="{folder}/{N['zip']}" download>Download ZIP</a>
    </div>
'''
    s = re.sub(r'<!-- DOWNLOADS:START.*?<!-- DOWNLOADS:END -->',
               lambda _: f'<!-- DOWNLOADS:START (generated) -->\n{dls}    <!-- DOWNLOADS:END -->', s, flags=re.S)
    open(idx, 'w').write(s)
