#!/usr/bin/env python3
"""Build every deliverable for one K-2 toolkit topic.

    python3 build.py topics/07-gentle-hands.py                    # everything into out/07-gentle-hands/
    python3 build.py topics/07-gentle-hands.py --only deck,poster # some parts
    python3 build.py topics/07-gentle-hands.py --publish          # build, then copy into the site and refresh the toolkit home
    python3 build.py topics/07-gentle-hands.py --only site --publish --publish-root /tmp/k2-test   # test publish

Parts, in build order: deck, poster, minibook, centers, family, guide, song, thumbs, zip, site.
--publish-root (or the K2_PUBLISH_ROOT environment variable) replaces resources/k2-behavior-toolkit.
"""
import argparse, os, sys, shutil, subprocess, time, zipfile, importlib.util

KIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(KIT, 'builder'))
from common import *                                     # noqa: E402
import deck, poster, minibook, centers, family, guide    # noqa: E402

# builder/site.py shares its name with Python's startup module `site`, so load it by path.
_spec = importlib.util.spec_from_file_location('k2site', os.path.join(KIT, 'builder', 'site.py'))
site = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(site)

PDF_KEYS = ['deck_pdf', 'poster_letter', 'poster_tabloid', 'centers', 'minibook', 'family', 'guide_pdf']
ZIP_KEYS = ['deck_html', 'deck_pdf', 'guide_docx', 'guide_pdf', 'poster_letter', 'poster_tabloid',
            'centers', 'minibook', 'family', 'song']


def build_song(T, od):
    """Copy the song video next to the deck (the deck's Play the song button and the ZIP need it)."""
    src, dst = song_source(T, od), os.path.join(od, names(T)['song'])
    if not src:
        return []
    if os.path.abspath(src) != os.path.abspath(dst):
        shutil.copy2(src, dst)
    return [names(T)['song']]


def build_thumbs(T, od):
    N, td, made = names(T), os.path.join(od, 'thumbs'), []
    os.makedirs(td, exist_ok=True)
    for k in PDF_KEYS:
        pdf = os.path.join(od, N[k])
        if os.path.exists(pdf):
            stem = N[k].rsplit('.', 1)[0] + '-1'
            subprocess.run(['pdftoppm', '-r', '50', '-jpeg', '-jpegopt', 'quality=80', '-f', '1', '-l', '1',
                            '-singlefile', pdf, os.path.join(td, stem)], check=True)
            made.append(f'thumbs/{stem}.jpg')
    song = os.path.join(od, N['song'])
    if T.get('song') and os.path.exists(song):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(T['song'].get('poster_at', 2.5)), '-i', song,
                        '-frames:v', '1', '-q:v', '4', os.path.join(td, 'song-poster.jpg')], check=True)
        made.append('thumbs/song-poster.jpg')
    return made


def readme(T, has_song):
    N = names(T)
    lines = [f"{T['full_title']} · K-2 Behavior Toolkit · Topic {T['num']} of 12",
             'Matchbook Learning Morning Meeting', '',
             f"Open {N['deck_html']} in Chrome to teach. Press N for notes."]
    if has_song:
        lines.append(f"Slide 1 has a Play the song button. Keep {N['song']} in this same folder so it plays.")
    lines += ['', 'Lee & Tee characters (c) AH-HA Coaching and Consulting, used with permission.']
    return '\n'.join(lines) + '\n'


def build_zip(T, od):
    N = names(T)
    folder = N['zip_folder']
    has_song = os.path.exists(os.path.join(od, N['song'])) and bool(T.get('song'))
    zp = os.path.join(od, N['zip'])
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(folder + '/', '')
        for k in ZIP_KEYS:
            f = os.path.join(od, N[k])
            if os.path.exists(f) and (k != 'song' or has_song):
                z.write(f, f'{folder}/{N[k]}')
        z.writestr(f'{folder}/README.txt', readme(T, has_song))
    return [N['zip']]


PARTS = {
    'deck': deck.build, 'poster': poster.build, 'minibook': minibook.build, 'centers': centers.build,
    'family': family.build, 'guide': guide.build, 'song': build_song, 'thumbs': build_thumbs,
    'zip': build_zip, 'site': site.build,
}


def publish(T, od, root):
    """Copy the topic folder into <root>/<slug>/, web-size the page images into shared/img, refresh the home."""
    dest = os.path.join(root, T['slug'])
    os.makedirs(dest, exist_ok=True)
    for name in sorted(os.listdir(od)):
        if name.startswith('_'):
            continue                      # _work/ and _guide.json stay in out/
        s, d = os.path.join(od, name), os.path.join(dest, name)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    keys = {T['site']['hero_img']}
    for t in site.registry().TOPICS:
        if t.get('thumb') and (site.is_live(t, root) or t['slug'] == T['slug']):
            keys.add(t['thumb'])
    for k in sorted(keys):
        site.shared_img(k, root)
    entry = site.registry().find(T['slug'])
    if not entry:
        print(f"  ! {T['slug']} is not in toolkit.py; add it so the toolkit home lists it")
    else:
        if entry['status'] != 'live':
            print(f"  ! toolkit.py still says status='soon' for {T['slug']}; it shows as live because it is published. Set status='live'.")
        if entry['title'] != T['full_title'] or entry['line'] != T['card_line']:
            print('  ! toolkit.py title/line differ from the topic file (full_title/card_line)')
    return dest, site.write_home(root)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('topic', help='topic file, e.g. topics/07-gentle-hands.py')
    ap.add_argument('--only', help='comma-separated parts: ' + ','.join(PARTS))
    ap.add_argument('--out', help='output folder (default out/<slug>)')
    ap.add_argument('--publish', action='store_true', help='copy into the site and regenerate the toolkit home')
    ap.add_argument('--publish-root', help='site toolkit folder (default resources/k2-behavior-toolkit or $K2_PUBLISH_ROOT)')
    a = ap.parse_args()
    if a.publish_root:
        os.environ['K2_PUBLISH_ROOT'] = os.path.abspath(a.publish_root)
    T = load_topic(a.topic)
    od = out_dir(T, a.out and os.path.abspath(a.out))
    only = a.only.split(',') if a.only else list(PARTS)
    bad = [p for p in only if p not in PARTS]
    if bad:
        ap.error(f'unknown part(s): {", ".join(bad)}')
    print(f"Topic {T['num']}: {T['full_title']} -> {od}")
    if not song_source(T, od):
        print('  (no song video yet: the deck has no Play the song button and the page has no Watch section)')
    for name in PARTS:
        if name in only:
            s = time.time()
            made = PARTS[name](T, od)
            print(f'  {name:<9} {", ".join(made) or "-"}  ({time.time() - s:.1f}s)')
    if a.publish:
        dest, home = publish(T, od, publish_root())
        print(f'  published to {dest}\n  toolkit home {home}')


if __name__ == '__main__':
    main()
