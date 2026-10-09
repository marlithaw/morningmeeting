"""Shared helpers for the K-2 SEL Toolkit builder: kit paths, fonts, base CSS, image embedding, PDF rendering.

Every path is computed from this file's location, so the kit can live anywhere.
"""
import base64, os, re, copy, importlib.util, sys

BUILDER = os.path.dirname(os.path.abspath(__file__))          # _build/k2-toolkit/builder
KIT = os.path.dirname(BUILDER)                                # _build/k2-toolkit
ASSETS = os.path.join(KIT, 'assets')
IMG_DIR = os.path.join(ASSETS, 'img')
FONT_DIR = os.path.join(ASSETS, 'fonts')
OUT = os.path.join(KIT, 'out')
REPO = os.path.dirname(os.path.dirname(KIT))                  # morningmeeting repo root
DEFAULT_PUBLISH_ROOT = os.path.join(REPO, 'resources', 'k2-behavior-toolkit')

if BUILDER not in sys.path:
    sys.path.insert(0, BUILDER)

CREDIT = 'Lee &amp; Tee characters © AH-HA Coaching and Consulting, used with permission.'
CREDIT_TXT = 'Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.'
MIME = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png', 'svg': 'image/svg+xml', 'woff2': 'font/woff2'}


def publish_root():
    """Where --publish writes. Override with the K2_PUBLISH_ROOT environment variable (used for test publishes)."""
    return os.environ.get('K2_PUBLISH_ROOT') or DEFAULT_PUBLISH_ROOT


def b64(path, mime=None):
    p = path if os.path.isabs(path) else os.path.join(ASSETS, path)
    ext = p.rsplit('.', 1)[-1].lower()
    return f"data:{mime or MIME[ext]};base64," + base64.b64encode(open(p, 'rb').read()).decode()


def img_path(key):
    """assets/img/<key>.jpg, falling back to <key>.png. A key may also be an absolute path to an image."""
    if os.path.isabs(key):
        return key
    for ext in ('jpg', 'png'):
        p = os.path.join(IMG_DIR, f'{key}.{ext}')
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f'No image for key "{key}" in {IMG_DIR} (.jpg or .png)')


def img(key, embed=True):
    """Image as a data URI (default) or a file:// URL."""
    p = img_path(key)
    return b64(p) if embed else f'file://{p}'


LOGO_SVG = open(os.path.join(IMG_DIR, 'flame-logo.svg')).read()

FONTS = [('Lilita One', 'lilita-one-latin-400-normal', 400),
         ('Fredoka', 'fredoka-latin-400-normal', 400), ('Fredoka', 'fredoka-latin-500-normal', 500),
         ('Fredoka', 'fredoka-latin-600-normal', 600), ('Fredoka', 'fredoka-latin-700-normal', 700),
         ('Andika', 'andika-latin-400-normal', 400), ('Andika', 'andika-latin-700-normal', 700)]


def fontface(embed=True):
    out = []
    for fam, f, w in FONTS:
        p = os.path.join(FONT_DIR, f + '.woff2')
        src = b64(p) if embed else f'file://{p}'
        out.append(f"@font-face{{font-family:'{fam}';src:url({src}) format('woff2');font-weight:{w};font-style:normal;font-display:block}}")
    return '\n'.join(out)


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
        pg.goto(f'file://{html_path}'); pg.wait_for_timeout(600)
        pg.pdf(path=pdf_path, width=width, height=height, print_background=True,
               margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()


def shot(html_path, png_path, w, h, full=False):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto(f'file://{html_path}'); pg.wait_for_timeout(600)
        pg.screenshot(path=png_path, full_page=full); b.close()


# ---------------------------------------------------------------- topics

def deep_merge(base, over):
    """Recursively merge dict `over` onto a copy of `base` (lists and scalars in `over` replace)."""
    out = copy.deepcopy(base)
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def load_topic(path):
    """Load a topic file (path, or a name under topics/) and return its TOPIC dict with shared defaults filled in."""
    import shared
    if not path.endswith('.py'):
        path = os.path.join(KIT, 'topics', path + '.py')
    path = os.path.abspath(path)
    spec = importlib.util.spec_from_file_location('topic_' + os.path.basename(path)[:-3].replace('-', '_'), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return shared.resolve(m.TOPIC)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def names(T):
    """Every output file name for a topic, in one place."""
    P, d = T['file_prefix'], T['deck_slug']
    zip_base = slugify(T['full_title'])
    return dict(
        deck_html=f'{d}-student-deck-k2.html', deck_pdf=f'{d}-student-deck-k2.pdf',
        poster_letter=f'{P}_Poster_Letter.pdf', poster_tabloid=f'{P}_Poster_Tabloid.pdf',
        minibook=f'{P}_Mini-Book.pdf', centers=f'{P}_Center-Kit.pdf', family=f'{P}_Family-Half-Sheet.pdf',
        guide_docx=f'{P}_Teacher-Guide.docx', guide_pdf=f'{P}_Teacher-Guide.pdf',
        song=f'{d}-song.mp4',
        zip=f'{zip_base}-k2-all-files.zip',
        zip_folder=f"{T['num']:02d}_{T['full_title'].replace(' ', '-')}_K-2",
    )


def out_dir(T, outdir=None):
    d = outdir or os.path.join(OUT, T['slug'])
    os.makedirs(d, exist_ok=True)
    return d


def work_dir(outdir):
    d = os.path.join(outdir, '_work')
    os.makedirs(d, exist_ok=True)
    return d


def song_source(T, outdir=None):
    """The topic's song video, or None. Looks at song.video, then out/<slug>/<deck>-song.mp4 (where
    music/build_mv.py writes), then the published copy. A topic with song=None never has a song."""
    s = T.get('song')
    if not s:
        return None
    n = names(T)['song']
    cands = []
    if s.get('video'):
        v = s['video']
        cands.append(v if os.path.isabs(v) else os.path.join(KIT, v))
    cands.append(os.path.join(outdir or os.path.join(OUT, T['slug']), n))
    cands.append(os.path.join(publish_root(), T['slug'], n))
    for c in cands:
        if os.path.exists(c):
            return c
    return None


def lang3(x):
    """(en, es, kr) from a tuple or a dict with en/es/kr keys."""
    if isinstance(x, dict):
        return x['en'], x['es'], x['kr']
    return tuple(x)
