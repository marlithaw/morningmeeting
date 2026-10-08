import base64, os, json
ROOT='/home/claude/k2'
def b64(path, mime=None):
    p=path if path.startswith('/') else f'{ROOT}/{path}'
    ext=p.rsplit('.',1)[-1].lower()
    mime=mime or {'jpg':'image/jpeg','jpeg':'image/jpeg','png':'image/png','svg':'image/svg+xml','woff2':'font/woff2'}[ext]
    return f"data:{mime};base64,"+base64.b64encode(open(p,'rb').read()).decode()
def img(name, embed=True):
    return b64(f'img/{name}.jpg') if embed else f'file://{ROOT}/img/{name}.jpg'
LOGO_SVG=open(f'{ROOT}/img/flame-logo.svg').read()
def fontface(embed=True):
    fs=[('Lilita One','lilita-one-latin-400-normal',400),
        ('Fredoka','fredoka-latin-400-normal',400),('Fredoka','fredoka-latin-500-normal',500),
        ('Fredoka','fredoka-latin-600-normal',600),('Fredoka','fredoka-latin-700-normal',700),
        ('Andika','andika-latin-400-normal',400),('Andika','andika-latin-700-normal',700)]
    out=[]
    for fam,f,w in fs:
        src=b64(f'fonts/{f}.woff2') if embed else f'file://{ROOT}/fonts/{f}.woff2'
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
COPING=[('c_corner','Go to the calm corner','Ir al rincón de calma','Ale nan kwen kalm nan'),
 ('c_breathe','Take deep breaths','Respirar profundo','Respire fon'),
 ('c_break','Ask for a break','Pedir un descanso','Mande yon ti repo'),
 ('c_words','Use my words','Usar mis palabras','Sèvi ak pawòl mwen'),
 ('c_grownup','Ask a grown-up','Pedir ayuda a un adulto','Mande yon granmoun èd')]

def render_pdf(html_path, pdf_path, width, height):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page()
        pg.goto(f'file://{html_path}'); pg.wait_for_timeout(600)
        pg.pdf(path=pdf_path, width=width, height=height, print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
        b.close()
def shot(html_path, png_path, w, h, full=False):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':w,'height':h})
        pg.goto(f'file://{html_path}'); pg.wait_for_timeout(600)
        pg.screenshot(path=png_path, full_page=full); b.close()
