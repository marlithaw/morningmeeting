"""Build every deliverable for one topic.

    python3 build_topic.py 02-calm-corner            # build into out/02-calm-corner (draft, plus a site preview in out/.../site)
    python3 build_topic.py 02-calm-corner --publish  # also copy the topic folder into resources/k2-behavior-toolkit and refresh the menu
    python3 build_topic.py 02-calm-corner --only deck,poster   # rebuild some parts

Parts: deck, poster, printables (mini book + center kit), family, guide, site.
"""
import sys, os, time, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import deck, poster, printables, family, guide, site

PARTS = {'deck': deck.build, 'poster': poster.build, 'printables': printables.build,
         'family': family.build, 'guide': guide.build}


def main():
    args = sys.argv[1:]
    ref = args[0]
    only = None
    if '--only' in args:
        only = args[args.index('--only') + 1].split(',')
    t = load_topic(ref)
    print(f"Building Topic {t['num']}: {t['title']}")
    for name, fn in PARTS.items():
        if only and name not in only:
            continue
        s = time.time(); made = fn(t)
        print(f'  {name:<11} {", ".join(made)}  ({time.time() - s:.0f}s)')
    if not only or 'site' in only:
        prev = site.build(t)
        print(f'  site preview {prev}')
    if '--publish' in args:
        dest = os.path.join(SITE, t['folder'])
        if t.get('song'):   # the published song may live inside dest: keep a copy before clearing the folder
            src = os.path.normpath(os.path.join(KIT, t['song']['file']))
            if src.startswith(dest):
                keep = os.path.join(tmp_dir(t), os.path.basename(src)); shutil.copy2(src, keep)
                t['song']['file'] = keep
        if os.path.exists(dest):
            shutil.rmtree(dest)
        site.build(t, dest)
        site.update_menu()
        print(f'  published to {dest} and refreshed the toolkit menu')


if __name__ == '__main__':
    main()
