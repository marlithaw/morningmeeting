"""Shared helpers for the K-2 SEL Toolkit builder."""
import base64, os, json, importlib.util

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # _build/k2-toolkit
ASSETS = os.path.join(KIT, 'assets')
REPO = os.path.dirname(os.path.dirname(KIT))                          # morningmeeting repo root
SITE = os.path.join(REPO, 'resources', 'k2-behavior-toolkit')
CREDIT = 'Lee &amp; Tee characters © AH-HA Coaching and Consulting, used with permission.'
CREDIT_TXT = 'Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.'

def b64(path, mime=None):
    p = path if os.path.isabs(path) else os.path.join(ASSETS, path)
    ext = p.rsplit('.', 1)[-1].lower()
    mime = mime or {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png', 'svg': 'image/svg+xml', 'woff2': 'font/woff2'}[ext]
    return f"data:{mime};base64," + base64.b64encode(open(p, 'rb').read()).decode()

def img(name):
    """Embed an art file from assets/img by name (jpg by default, png if name ends .png)."""
    return b64(f'img/{name}' if '.' in name else f'img/{name}.jpg')

LOGO_SVG = open(os.path.join(ASSETS, 'img', 'flame-logo.svg')).read()

def fontface():
    fs = [('Lilita One', 'lilita-one-latin-400-normal', 400),
          ('Fredoka', 'fredoka-latin-400-normal', 400), ('Fredoka', 'fredoka-latin-500-normal', 500),
          ('Fredoka', 'fredoka-latin-600-normal', 600), ('Fredoka', 'fredoka-latin-700-normal', 700),
          ('Andika', 'andika-latin-400-normal', 400), ('Andika', 'andika-latin-700-normal', 700)]
    return '\n'.join(f"@font-face{{font-family:'{fam}';src:url({b64(f'fonts/{f}.woff2')}) format('woff2');font-weight:{w};font-style:normal;font-display:block}}"
                     for fam, f, w in fs)

BASE_CSS = r"""
:root{
  --red:#E21C24; --ember:#C8161D; --yellow:#F9DC7C; --gold:#F2B705; --char:#232323;
  --green:#1F8A4C; --green-l:#DDF3E4; --orange:#F28C28; --sky:#2F80ED; --sky-l:#E3EEFD;
  --red-l:#FDE3E4; --paper:#FFF8EA; --grid:rgba(47,128,237,.10); --ink:#1d1d1f;
  --disp:'Lilita One','Fredoka',system-ui,sans-serif; --round:'Fredoka',system-ui,sans-serif;
  --read:'Andika','Fredoka',system-ui,sans-serif;
}
.paper{background-color:var(--paper);
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:22px 22px;}
.kente{background:repeating-linear-gradient(90deg,var(--green) 0 26px,var(--gold) 26px 40px,var(--red) 40px 66px,var(--char) 66px 72px,var(--gold) 72px 86px,var(--orange) 86px 112px,var(--char) 112px 118px);}
.ttl{font-family:var(--disp);color:var(--red);letter-spacing:.01em;line-height:.95;
  -webkit-text-stroke:2px var(--char);paint-order:stroke fill;text-shadow:4px 4px 0 var(--char);}
.tape{position:absolute;width:74px;height:22px;background:rgba(249,220,124,.88);
  box-shadow:0 1px 2px rgba(0,0,0,.15);z-index:3}
.lang{font-family:var(--read);color:#444;line-height:1.25}
.lang b{font-family:var(--round);font-weight:600;font-size:.72em;letter-spacing:.06em;color:#888;margin-right:.35em;text-transform:uppercase}
.badge{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;
  font-family:var(--disp);color:#fff;border:3px solid var(--char);}
.logo{display:inline-flex;align-items:center;gap:.4em;font-family:var(--round);font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;color:var(--char)}
.logo svg{height:1.6em;width:auto}
"""

def render_pdf(html_path, pdf_path, width, height):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto(f'file://{html_path}'); pg.wait_for_timeout(700)
        pg.pdf(path=pdf_path, width=width, height=height, print_background=True,
               margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()

def load_topic(ref):
    """Load topics/<ref>.py (ref like '02-calm-corner' or a path) and return its TOPIC dict."""
    path = ref if ref.endswith('.py') else os.path.join(KIT, 'topics', ref + '.py')
    spec = importlib.util.spec_from_file_location('topic', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    t = m.TOPIC
    t.setdefault('song', None)
    return t

def out_dir(t):
    d = os.path.join(KIT, 'out', t['folder']); os.makedirs(d, exist_ok=True); return d

def tmp_dir(t):
    d = os.path.join(KIT, 'tmp', t['folder']); os.makedirs(d, exist_ok=True); return d

def names(t):
    """Every output file name for a topic, in one place."""
    P, s = t['prefix'], t['slug']
    return dict(
        poster_letter=f'{P}_Poster_Letter.pdf', poster_tabloid=f'{P}_Poster_Tabloid.pdf',
        deck_html=f'{s}-student-deck-k2.html', deck_pdf=f'{s}-student-deck-k2.pdf',
        minibook=f'{P}_Mini-Book.pdf', centers=f'{P}_Center-Kit.pdf',
        family=f'{P}_Family-Half-Sheet.pdf', guide_docx=f'{P}_Teacher-Guide.docx', guide_pdf=f'{P}_Teacher-Guide.pdf',
        song=f'{s}-song.mp4', zip=f"{t['zip_slug']}-k2-all-files.zip", zip_folder=f"{t['num']:02d}_{t['zip_folder']}_K-2",
    )

def L3(x):
    """Normalize a language triple: accepts (en, es, kr) tuple or dict."""
    if isinstance(x, dict): return x['en'], x['es'], x['kr']
    return x
