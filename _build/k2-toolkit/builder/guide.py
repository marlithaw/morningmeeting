"""Teacher guide: guide.py writes out/<slug>/_guide.json, guide.js (Node, `docx` package) builds the .docx,
and LibreOffice converts it to PDF."""
import os, json, subprocess
from common import *


def node_env():
    """Environment for node with the `docx` package resolvable (global install, /opt/npm-tools, or NODE_PATH)."""
    env = dict(os.environ)
    try:
        subprocess.run(['node', '-e', "require.resolve('docx')"], check=True, capture_output=True, env=env)
        return env
    except subprocess.CalledProcessError:
        pass
    root = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
    extra = [d for d in (root, '/opt/npm-tools/node_modules', os.path.join(KIT, 'node_modules')) if d and os.path.isdir(d)]
    env['NODE_PATH'] = os.pathsep.join(extra + [env.get('NODE_PATH', '')]).strip(os.pathsep)
    return env


def data(T):
    G = T['guide']
    d = {k: G[k] for k in ('glance', 'before_title', 'before', 'lesson_title', 'lesson_note', 'slides', 'bridges_title',
                           'bridges_note', 'bridges', 'centers_title', 'centers_note', 'centers', 'keys_title', 'keys',
                           'minibook_title', 'minibook', 'when_title', 'when_intro', 'when', 'when_outro',
                           'family_title', 'family')}
    d.update(
        eyebrow='K–2 BEHAVIOR TOOLKIT · MORNING MEETING',
        full_title=T['full_title'],
        subtitle=f"Teacher Guide · Topic {T['num']} of 12 · Value: {T['value']}",
        doc_title=f"{T['full_title']} · Teacher Guide",
        footer=f"Matchbook Learning · K–2 Behavior Toolkit · {T['full_title']} · Teacher Guide · page ",
        credit=CREDIT_TXT,
        images=[dict(path=img_path(k), type='png' if img_path(k).endswith('.png') else 'jpg', w=w, h=h) for k, w, h in G['images']],
    )
    for k in ('glance', 'slides', 'bridges', 'centers', 'keys', 'when'):
        d[k] = [list(r) for r in d[k]]
    return d


def build(T, outdir):
    N = names(T)
    jp = os.path.join(outdir, '_guide.json')
    json.dump(data(T), open(jp, 'w'), ensure_ascii=False, indent=1)
    docx = os.path.join(outdir, N['guide_docx'])
    subprocess.run(['node', os.path.join(BUILDER, 'guide.js'), jp, docx], check=True, env=node_env(),
                   stdout=subprocess.DEVNULL)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return [N['guide_docx'], N['guide_pdf']]
