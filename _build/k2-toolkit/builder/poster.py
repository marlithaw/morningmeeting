"""Poster: letter and 11x17, four captioned panels, calm choices row, promise footer."""
import os
from common import *


def html(t, size):
    P = t['poster']
    fs = 16 if size == 'letter' else 20.7
    W, H = ('8.5in', '11in') if size == 'letter' else ('11in', '17in')
    panels = ''
    for i, (im, col, sym, en, es, ht, pos) in enumerate(P['panels']):
        rot = [-1.2, 1, 0.8, -0.9][i]
        panels += f'''<div class="pan" style="--b:{col};transform:rotate({rot}deg)">
          <span class="tape" style="top:-.55em;left:38%;transform:rotate({-rot * 3}deg)"></span>
          <div class="ph" style="background-image:url({img(im)});background-position:{pos}"></div>
          <div class="cap"><span class="badge" style="background:{col}">{sym}</span>
            <div><div class="en">{en}</div>
            <div class="lang"><b>ES</b>{es}</div><div class="lang"><b>KR</b>{ht}</div></div></div>
        </div>'''
    C = P.get('choices') or t['choices']
    cope = ''.join(f'''<div class="cp"><div class="ci" style="background-image:url({img(k)})"></div>
        <div class="cl">{en}</div><div class="lang sm">{es}</div><div class="lang sm">{ht}</div></div>''' for k, en, es, ht in C)
    ch_en, ch_es, ch_kr = P.get('choices_head') or t['choices_head']
    pe, ps, pk = t['promise']
    title = ' '.join(t['title_lines'])
    tsize = P.get('title_size', '4.6em')
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
{fontface()}
{BASE_CSS}
@page{{size:{W} {H};margin:0}}
html,body{{margin:0;padding:0}}
body{{width:{W};height:{H};font-size:{fs}px;overflow:hidden}}
.pg{{width:100%;height:100%;box-sizing:border-box;display:flex;flex-direction:column;position:relative}}
.top{{height:.8em}}
.hd{{display:flex;align-items:center;justify-content:space-between;padding:.7em 1.6em .2em}}
.hd .t{{display:flex;flex-direction:column}}
.ttl{{font-size:{tsize}}}
.sub{{font-family:var(--round);font-weight:600;font-size:1.5em;color:var(--char);margin-top:.15em}}
.sub em{{font-style:normal;background:var(--green);color:#fff;border-radius:.4em;padding:.05em .45em;margin-left:.3em;font-size:.8em;vertical-align:middle;border:2px solid var(--char)}}
.hd .lt{{width:9.5em;height:6.2em;background:url({img(P['header_img'])}) center/cover;border-radius:1em;border:3px solid var(--char);flex:none}}
.grid{{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:1.1em 1.2em;padding:.9em 1.6em .6em;min-height:0}}
.pan{{position:relative;background:#fff;border:4px solid var(--b);border-radius:1em;box-shadow:5px 5px 0 var(--char);display:flex;flex-direction:column;overflow:visible;min-height:0}}
.ph{{flex:1;background-size:cover;background-position:center 35%;border-radius:.7em .7em 0 0;min-height:0}}
.cap{{display:flex;gap:.55em;align-items:flex-start;padding:.55em .7em .6em;border-top:3px solid var(--b)}}
.cap .badge{{width:1.9em;height:1.9em;font-size:1.05em;flex:none}}
.en{{font-family:var(--round);font-weight:700;font-size:1.22em;line-height:1.12;color:var(--ink);margin-bottom:.15em}}
.lang{{font-size:.74em}}
.cope{{margin:.5em 1.6em 0;background:#fff;border:4px solid var(--char);border-radius:1em;padding:.5em .7em .65em;box-shadow:5px 5px 0 var(--gold)}}
.ch{{display:flex;align-items:baseline;gap:.6em;flex-wrap:wrap;margin-bottom:.4em}}
.ch .h{{font-family:var(--disp);font-size:1.7em;color:var(--char)}}
.ch .lang{{font-size:.8em}}
.cps{{display:grid;grid-template-columns:repeat({len(C)},1fr);gap:.55em}}
.cp{{text-align:center}}
.ci{{height:6.2em;border-radius:.6em;border:3px solid var(--char);background-size:cover;background-position:center 30%;background-color:#fff}}
.cl{{font-family:var(--round);font-weight:700;font-size:.92em;line-height:1.08;margin:.3em 0 .1em}}
.lang.sm{{font-size:.62em}}
.ft{{display:flex;align-items:center;justify-content:space-between;margin:.8em 1.6em .3em;padding:.5em .9em;background:var(--red);border:4px solid var(--char);border-radius:1em;color:#fff}}
.ft .say{{font-family:var(--disp);font-size:1.55em;line-height:1.05}}
.ft .lang{{color:#fff;opacity:.92;font-size:.72em}} .ft .lang b{{color:#ffe7a6}}
.ft .tu{{width:6em;height:4.4em;background:url({img(P['foot_img'])}) center/cover;border-radius:.6em;border:3px solid var(--char);flex:none}}
.meta{{display:flex;justify-content:space-between;align-items:center;padding:.15em 1.6em .55em;font-family:var(--round);font-size:.62em;color:#555}}
.logo{{font-size:1.15em}}
</style></head><body><div class="pg paper">
<div class="top kente"></div>
<div class="hd"><div class="t"><div class="ttl">{title}</div>
<div class="sub">{t['sub']} <em>{t['value'].upper()}</em></div></div><div class="lt"></div></div>
<div class="grid">{panels}</div>
<div class="cope"><div class="ch"><span class="h">{ch_en}</span>
<span class="lang"><b>ES</b>{ch_es}</span><span class="lang"><b>KR</b>{ch_kr}</span></div>
<div class="cps">{cope}</div></div>
<div class="ft"><div><div class="say">{pe}</div>
<div class="lang"><b>ES</b>{ps}</div>
<div class="lang"><b>KR</b>{pk}</div></div><div class="tu"></div></div>
<div class="meta"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>K–2 Behavior Toolkit · {t['title']} · Safe · Respectful · Responsible</span></div>
</div></body></html>'''


def build(t):
    N, od, td = names(t), out_dir(t), tmp_dir(t)
    for size, (w, h), key in [('letter', ('8.5in', '11in'), 'poster_letter'), ('tabloid', ('11in', '17in'), 'poster_tabloid')]:
        p = os.path.join(td, f'poster_{size}.html')
        open(p, 'w').write(html(t, size))
        render_pdf(p, os.path.join(od, N[key]), w, h)
    return [N['poster_letter'], N['poster_tabloid']]
