"""Tier 2 mini book: cover + 6 story pages + back, two half-pages per landscape sheet (4 sheets, cut and staple)."""
import os
from common import *

HEAD_CSS = '''
@page{size:11in 8.5in;margin:0}
html,body{margin:0;padding:0}
.sheet{width:11in;height:8.5in;box-sizing:border-box;position:relative;overflow:hidden;page-break-after:always;break-after:page;display:flex}
.half{width:5.5in;height:8.5in;box-sizing:border-box;padding:.35in .38in .3in;display:flex;flex-direction:column;position:relative}
.half+.half{border-left:2px dashed #b9b9b9}
.half .k{height:10px;margin:-.35in -.38in .22in}
.pic{background-size:cover;background-repeat:no-repeat;border:4px solid var(--char);border-radius:18px;box-shadow:5px 5px 0 var(--char);background-color:#fff}
.bp{flex:1;min-height:0}
.txt{font-family:var(--read);font-weight:700;font-size:27px;line-height:1.25;color:var(--ink);margin:.22in 0 .08in}
.lang{font-size:14px;margin-top:3px}
.pg{position:absolute;bottom:.14in;right:.3in;font-family:var(--disp);font-size:18px;color:#999}
.cut{position:absolute;top:2px;left:50%;transform:translateX(-50%);font-family:var(--round);font-size:10px;color:#999;background:#fff;padding:0 4px;z-index:5}
.cvt{font-size:66px;text-align:center;margin:.1in 0 .12in}
.ftr{display:flex;justify-content:space-between;align-items:center;font-family:var(--round);font-size:10px;color:#777;margin-top:.12in}
.ftr .logo{font-size:11px}
'''


def head():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{fontface()}{BASE_CSS}''' + HEAD_CSS + '''</style></head><body>'''


def page(n, image, en, es, ht, pos='center 35%', two=None):
    if two:
        p = f'''<div class="bp" style="display:grid;grid-template-rows:1fr 1fr;gap:.18in">
        <div class="pic" style="background-image:url({img(two[0])});background-position:{pos}"></div>
        <div class="pic" style="background-image:url({img(two[1])});background-position:{pos}"></div></div>'''
    else:
        p = f'<div class="pic bp" style="background-image:url({img(image)});background-position:{pos}"></div>'
    return f'''<div class="half paper"><div class="k kente"></div>{p}
    <div class="txt">{en}</div><div class="lang"><b>ES</b>{es}</div><div class="lang"><b>KR</b>{ht}</div><div class="pg">{n}</div></div>'''


def html(T):
    M = T['minibook']
    cover = f'''<div class="half paper"><div class="k kente"></div>
<div class="ttl cvt">{M['cover_title']}</div>
<div class="pic bp" style="background-image:url({img(M['cover_img'])});background-position:{M['cover_pos']}"></div>
<div class="lang" style="text-align:center;margin-top:.16in;font-size:16px"><b>ES</b>{M['cover_es']} · <b>KR</b>{M['cover_kr']}</div>
<div class="ftr"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>K–2 Behavior Toolkit</span></div></div>'''
    P = []
    for n, pg in enumerate(M['pages'], 1):
        pos = pg.get('pos', 'center 35%')
        if pg.get('fit') == 'contain':
            pos += ';background-size:contain'
        if pg.get('imgs'):
            P.append(page(n, None, pg['en'], pg['es'], pg['kr'], pos, two=pg['imgs']))
        else:
            P.append(page(n, pg['img'], pg['en'], pg['es'], pg['kr'], pos))
    stars = ''.join(f'<div style="text-align:center"><div style="font-size:74px;line-height:1;-webkit-text-stroke:2px #232323;color:#fff">★</div><div style="font-family:var(--disp);font-size:24px">{d}</div></div>' for d in M['days'])
    bt = lang3(M['back_title'])
    back = f'''<div class="half paper"><div class="k kente"></div>
<div class="ttl" style="font-size:58px;text-align:center;margin:.15in 0 .1in">{bt[0]}</div>
<div class="lang" style="text-align:center;font-size:16px"><b>ES</b>{bt[1]} · <b>KR</b>{bt[2]}</div>
<div class="pic" style="height:2.7in;margin:.25in 0;background-image:url({img(M['back_img'])});background-position:{M['back_pos']}"></div>
<div style="font-family:var(--read);font-weight:700;font-size:22px;text-align:center;margin-bottom:.12in">{M['back_prompt']}</div>
<div style="display:flex;justify-content:space-between">{stars}</div>
<div class="ftr" style="margin-top:auto"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>{T['title']} · Mini Book</span></div></div>'''
    halves = [cover] + P + [back]
    sheets = ''
    for i in range(0, 8, 2):
        sheets += f'<div class="sheet"><span class="cut">✂ cut on the dashed line</span>{halves[i]}{halves[i+1]}</div>'
    return head() + sheets + '</body></html>'


def build(T, outdir):
    N = names(T)
    p = os.path.join(work_dir(outdir), 'minibook.html')
    open(p, 'w').write(html(T))
    render_pdf(p, os.path.join(outdir, N['minibook']), '11in', '8.5in')
    return [N['minibook']]
