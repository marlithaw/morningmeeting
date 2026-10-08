"""Teacher guide: docx built by guide.js (docx 9.x) from the topic's guide content, plus a PDF via LibreOffice."""
import os, json, subprocess, shutil
from common import *


def build(t):
    G, N, od, td = t['guide'], names(t), out_dir(t), tmp_dir(t)
    data = dict(G, title=t['title'], num=t['num'], value=t['value'], credit=CREDIT_TXT,
                img_dir=os.path.join(ASSETS, 'img'))
    data['glance'] = [list(r) for r in G['glance']]
    jp = os.path.join(td, 'guide.json'); json.dump(data, open(jp, 'w'), ensure_ascii=False)
    docx = os.path.join(od, N['guide_docx'])
    env = dict(os.environ, NODE_PATH='/opt/npm-tools/node_modules:' + os.environ.get('NODE_PATH', ''))
    subprocess.run(['node', os.path.join(os.path.dirname(__file__), 'guide.js'), jp, docx], check=True, env=env)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', docx, '--outdir', od], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return [N['guide_docx'], N['guide_pdf']]
