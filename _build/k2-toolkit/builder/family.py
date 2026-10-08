"""Family half-sheets: one page per language (EN, ES, KR), two half-sheets per page."""
import os
from common import *


def build(t):
    F, N, od, td = t['family'], names(t), out_dir(t), tmp_dir(t)
    C = F.get('choices') or t['choices']
    col = {'en': 1, 'es': 2, 'kr': 3}
    def half(d, lang):
        icons=''.join(f'''<div class="ic"><div class="pic" style="background-image:url({img(c[0])})"></div><div class="il">{c[col[lang]]}</div></div>''' for c in C)
        tips=''.join(f'<li>{x}</li>' for x in d['tips'])
        return f'''<div class="half paper"><div class="k kente"></div>
<div class="row"><div class="l">
 <div class="eb">{d['eb']}</div><div class="ttl">{d['t']}</div>
 <p class="in">{d['intro']}</p>
 <div class="say"><span>{d['sayh']}</span> {d['say']}</div>
 <div class="th">{d['th']}</div><ul>{tips}</ul>
</div><div class="r"><div class="pic hero" style="background-image:url({img(F['hero'])});background-position:{F.get('hero_pos','center 15%')}"></div>
 <div class="ch">{d['ch']}</div><div class="ics" style="grid-template-columns:repeat({len(C)},1fr)">{icons}</div></div></div>
<div class="ftr"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>{d['ft']}</span></div></div>'''
    CSS=f'''{fontface()}{BASE_CSS}
    @page{{size:8.5in 11in;margin:0}} html,body{{margin:0}}
    .sheet{{width:8.5in;height:11in;display:flex;flex-direction:column;page-break-after:always;break-after:page;position:relative}}
    .half{{height:5.5in;box-sizing:border-box;padding:.32in .4in .22in;display:flex;flex-direction:column}}
    .half+.half{{border-top:2px dashed #b9b9b9}}
    .k{{height:9px;margin:-.32in -.4in .16in}}
    .row{{flex:1;display:grid;grid-template-columns:1.35fr 1fr;gap:.25in;min-height:0}}
    .eb{{font-family:var(--round);font-weight:600;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#666}}
    .ttl{{font-size:54px;margin:2px 0 6px;-webkit-text-stroke:1.5px var(--char);text-shadow:3px 3px 0 var(--char)}}
    .in{{font-family:var(--read);font-size:15.5px;line-height:1.4;margin:0 0 .1in}}
    .say{{background:var(--red);color:#fff;border:3px solid var(--char);border-radius:12px;padding:7px 11px;font-family:var(--disp);font-size:20px;line-height:1.15}}
    .say span{{color:var(--yellow)}}
    .th{{font-family:var(--disp);font-size:23px;color:var(--green);margin:.12in 0 .02in}}
    ul{{margin:0;padding-left:18px;font-family:var(--read);font-size:14.5px;line-height:1.4}} li{{margin-bottom:3px}}
    .pic{{background-size:cover;background-position:center 25%;border:3px solid var(--char);border-radius:12px;background-color:#fff}}
    .hero{{height:2.15in;background-position:center 15%}}
    .ch{{font-family:var(--disp);font-size:21px;margin:.1in 0 .05in;color:var(--char)}}
    .ics{{display:grid;grid-template-columns:repeat(5,1fr);gap:5px}}
    .ic .pic{{height:.85in;border-width:2px;border-radius:8px}}
    .il{{font-family:var(--round);font-weight:600;font-size:10px;line-height:1.1;text-align:center;margin-top:3px}}
    .ftr{{display:flex;justify-content:space-between;align-items:center;font-family:var(--round);font-size:10px;color:#666;margin-top:.08in}}
    .ftr .logo{{font-size:10.5px}}
    .cut{{position:absolute;top:5.5in;left:50%;transform:translate(-50%,-50%);background:#fff;font-family:var(--round);font-size:9px;color:#999;padding:0 4px}}
    '''
    L = F['langs']
    body=''.join(f'<div class="sheet"><span class="cut">✂</span>{half(L[k],k)}{half(L[k],k)}</div>' for k in ['en','es','kr'])
    p=os.path.join(td,'family.html')
    open(p,'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
    render_pdf(p,os.path.join(od,N['family']),'8.5in','11in')
    return [N['family']]
