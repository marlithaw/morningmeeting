"""Tier 2 mini book (cut and staple) and the center kit (sort, sequence, act it out, desk strips, coloring)."""
import os
from pypdf import PdfWriter
from common import *

MB_HEAD = '''<!doctype html><html><head><meta charset="utf-8"><style>{ff}{base}
@page{{size:11in 8.5in;margin:0}}
html,body{{margin:0;padding:0}}
.sheet{{width:11in;height:8.5in;box-sizing:border-box;position:relative;overflow:hidden;page-break-after:always;break-after:page;display:flex}}
.half{{width:5.5in;height:8.5in;box-sizing:border-box;padding:.35in .38in .3in;display:flex;flex-direction:column;position:relative}}
.half+.half{{border-left:2px dashed #b9b9b9}}
.half .k{{height:10px;margin:-.35in -.38in .22in}}
.pic{{background-size:cover;background-repeat:no-repeat;border:4px solid var(--char);border-radius:18px;box-shadow:5px 5px 0 var(--char);background-color:#fff}}
.bp{{flex:1;min-height:0}}
.txt{{font-family:var(--read);font-weight:700;font-size:27px;line-height:1.25;color:var(--ink);margin:.22in 0 .08in}}
.lang{{font-size:14px;margin-top:3px}}
.pg{{position:absolute;bottom:.14in;right:.3in;font-family:var(--disp);font-size:18px;color:#999}}
.cut{{position:absolute;top:2px;left:50%;transform:translateX(-50%);font-family:var(--round);font-size:10px;color:#999;background:#fff;padding:0 4px;z-index:5}}
.cvt{{font-size:66px;text-align:center;margin:.1in 0 .12in}}
.ftr{{display:flex;justify-content:space-between;align-items:center;font-family:var(--round);font-size:10px;color:#777;margin-top:.12in}}
.ftr .logo{{font-size:11px}}
</style></head><body>'''


def minibook(t):
    M, N, od, td = t['minibook'], names(t), out_dir(t), tmp_dir(t)

    def page(n, image, en, es, ht, pos):
        if isinstance(image, (tuple, list)):
            p = f'''<div class="bp" style="display:grid;grid-template-rows:1fr 1fr;gap:.18in">
        <div class="pic" style="background-image:url({img(image[0])});background-position:center 30%"></div>
        <div class="pic" style="background-image:url({img(image[1])});background-position:center 30%"></div></div>'''
        else:
            p = f'<div class="pic bp" style="background-image:url({img(image)});background-position:{pos}"></div>'
        return f'''<div class="half paper"><div class="k kente"></div>{p}
    <div class="txt">{en}</div><div class="lang"><b>ES</b>{es}</div><div class="lang"><b>KR</b>{ht}</div><div class="pg">{n}</div></div>'''

    cover = f'''<div class="half paper"><div class="k kente"></div>
<div class="ttl cvt">{M['cover_title']}</div>
<div class="pic bp" style="background-image:url({img(M['cover_img'])});background-position:{M['cover_pos']}"></div>
<div class="lang" style="text-align:center;margin-top:.16in;font-size:16px">{M['cover_lang']}</div>
<div class="ftr"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>K–2 Behavior Toolkit</span></div></div>'''
    P = [page(i + 1, *pg) for i, pg in enumerate(M['pages'])]
    assert len(P) == 6, 'mini book needs exactly 6 story pages'
    stars = ''.join(f'<div style="text-align:center"><div style="font-size:74px;line-height:1;-webkit-text-stroke:2px #232323;color:#fff">★</div><div style="font-family:var(--disp);font-size:24px">{d}</div></div>' for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
    back = f'''<div class="half paper"><div class="k kente"></div>
<div class="ttl" style="font-size:58px;text-align:center;margin:.15in 0 .1in">I did it!</div>
<div class="lang" style="text-align:center;font-size:16px"><b>ES</b>¡Lo logré! · <b>KR</b>Mwen fè l!</div>
<div class="pic" style="height:2.7in;margin:.25in 0;background-image:url({img(M['back_img'])});background-position:center 20%"></div>
<div style="font-family:var(--read);font-weight:700;font-size:22px;text-align:center;margin-bottom:.12in">{M['back_prompt']}</div>
<div style="display:flex;justify-content:space-between">{stars}</div>
<div class="ftr" style="margin-top:auto"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>{t['short']} · Mini Book</span></div></div>'''
    halves = [cover] + P + [back]
    sheets = ''.join(f'<div class="sheet"><span class="cut">✂ cut on the dashed line</span>{halves[i]}{halves[i + 1]}</div>' for i in range(0, 8, 2))
    p = os.path.join(td, 'minibook.html')
    open(p, 'w').write(MB_HEAD.format(ff=fontface(), base=BASE_CSS) + sheets + '</body></html>')
    render_pdf(p, os.path.join(od, N['minibook']), '11in', '8.5in')
    return [N['minibook']]


K_HEAD = '''<!doctype html><html><head><meta charset="utf-8"><style>{ff}{base}
@page{{size:{size};margin:0}}
html,body{{margin:0}}
.sheet{{width:8.5in;height:11in;box-sizing:border-box;padding:.4in .45in .35in;position:relative;overflow:hidden;page-break-after:always;break-after:page;display:flex;flex-direction:column}}
.sheet.land{{width:11in;height:8.5in}}
.top{{height:12px;margin:-.4in -.45in .22in}}
.hrow{{display:flex;align-items:center;justify-content:space-between;margin-bottom:.16in}}
.h{{font-family:var(--disp);font-size:40px;color:var(--red);-webkit-text-stroke:1.5px var(--char);paint-order:stroke fill;text-shadow:3px 3px 0 var(--char)}}
.tag{{font-family:var(--round);font-weight:700;font-size:14px;letter-spacing:.12em;text-transform:uppercase;background:var(--char);color:#fff;padding:5px 12px;border-radius:30px}}
.pic{{background-size:cover;background-repeat:no-repeat;border:3px solid var(--char);border-radius:14px;background-color:#fff}}
.cards{{flex:1;display:grid;gap:0}}
.card{{border:2px dashed #aaa;padding:.14in;display:flex;flex-direction:column;box-sizing:border-box;min-height:0}}
.card .pic{{flex:1;min-height:0}}
.cl{{font-family:var(--round);font-weight:700;font-size:20px;text-align:center;margin-top:.08in;color:var(--char)}}
.dir{{display:flex;gap:.12in;align-items:center;font-family:var(--round);font-weight:600;font-size:15px;color:#444}}
.dir .s{{display:flex;align-items:center;gap:6px;background:#fff;border:2px solid var(--char);border-radius:30px;padding:4px 12px}}
.dir .s i{{font-style:normal;font-size:20px}}
.ftr{{display:flex;justify-content:space-between;align-items:center;font-family:var(--round);font-size:10px;color:#777;margin-top:.12in}}
.ftr .logo{{font-size:11px}}
.lang{{font-size:12px}}
</style></head><body>'''


def centers(t):
    Cn, N, od, td = t['centers'], names(t), out_dir(t), tmp_dir(t)
    C = t['choices']
    ftr = lambda name: f'<div class="ftr"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>{t["short"]} · Center Kit · {name}</span></div>'

    # A. Sort mat + cards
    s = Cn['sort']
    ysym, yen, yes_, ykr = s['yes']; nsym, nen, nes, nkr = s['no']
    mat = f'''<div class="sheet land paper"><div class="top kente"></div>
<div class="hrow"><div class="h"{f' style="font-size:{s["title_size"]}"' if s.get('title_size') else ''}>{s['title']}</div><div class="dir"><span class="s"><i>✂️</i>cut</span><span class="s"><i>👀</i>look</span><span class="s"><i>👉</i>sort</span></div></div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:.3in">
 <div style="border:6px solid var(--green);border-radius:22px;background:var(--green-l);display:flex;flex-direction:column;align-items:center;padding:.2in">
  <div style="display:flex;align-items:center;gap:.15in"><span class="badge" style="width:64px;height:64px;font-size:40px;background:var(--green);flex:none">{ysym}</span><span style="font-family:var(--disp);font-size:44px;color:var(--green);line-height:1">{yen}</span></div>
  <div class="lang" style="margin-top:6px"><b>ES</b>{yes_} · <b>KR</b>{ykr}</div></div>
 <div style="border:6px solid var(--red);border-radius:22px;background:var(--red-l);display:flex;flex-direction:column;align-items:center;padding:.2in">
  <div style="display:flex;align-items:center;gap:.15in"><span class="badge" style="width:64px;height:64px;font-size:36px;background:var(--red);flex:none">{nsym}</span><span style="font-family:var(--disp);font-size:44px;color:var(--red);line-height:1">{nen}</span></div>
  <div class="lang" style="margin-top:6px"><b>ES</b>{nes} · <b>KR</b>{nkr}</div></div>
</div>{ftr('Picture Sort Mat')}</div>'''
    cards = ''.join(f'<div class="card"><div class="pic" style="background-image:url({img(n)});background-position:{p}"></div></div>' for n, p in s['cards'])
    sortp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:32px">SORT IT: PICTURE CARDS</div><div class="tag">✂ cut</div></div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr)">{cards}</div>{ftr('Picture Sort Cards')}</div>'''

    # B. Sequencing mat + cards
    q = Cn['seq']
    slots = ''.join(f'''<div style="border:4px dashed var(--char);border-radius:16px;background:#fff;position:relative">
 <div style="position:absolute;top:-16px;left:-12px;display:flex;align-items:center;gap:8px"><span class="badge" style="width:46px;height:46px;font-size:28px;background:var(--red)">{n}</span>
 <span style="font-family:var(--disp);font-size:24px;background:var(--paper);padding:0 6px">{w}</span></div></div>''' for n, w in [('1', 'First'), ('2', 'Next'), ('3', 'Then'), ('4', 'Last')])
    sc = ''.join(f'<div class="card"><div class="pic" style="background-image:url({img(q["cards"][i])});background-position:center 35%"></div></div>' for i in q['shuffle'])
    seqp = f'''<div class="sheet land paper"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:34px">PUT IT IN ORDER</div><div class="dir"><span class="s"><i>👀</i>look</span><span class="s"><i>🔢</i>1 2 3 4</span><span class="s"><i>🗣️</i>tell it</span></div></div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.4in .3in;padding:.25in .1in .1in">{slots}</div>{ftr('Sequencing Mat')}</div>
<div class="sheet land"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:32px">PUT IT IN ORDER: CARDS</div><div class="tag">✂ cut</div></div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr">{sc}</div>{ftr('Sequencing Cards')}</div>'''

    # C. Role-play cards
    r = Cn['roleplay']
    rc = r.get('choices') or C
    mini = ''.join(f'<div class="pic" style="height:.62in;background-image:url({img(k)});background-position:center 30%;border-width:2px;border-radius:8px"></div>' for k, *_ in rc)
    rp = ''.join(f'''<div class="card" style="padding:.16in">
 <div class="pic" style="background-image:url({img(n)});background-position:{p}"></div>
 <div style="font-family:var(--disp);font-size:26px;color:var(--char);margin-top:.1in;line-height:1.05">{en}</div>
 <div class="lang"><b>ES</b>{es}</div><div class="lang"><b>KR</b>{ht}</div>
 <div style="font-family:var(--disp);font-size:21px;color:var(--red);margin:.08in 0 .06in">{r['prompt']}</div>
 <div style="display:grid;grid-template-columns:repeat({len(rc)},1fr);gap:5px">{mini}</div></div>''' for n, p, en, es, ht in r['scenes'])
    dirs = r.get('dirs', [('🃏', 'pick'), ('😠', 'show mad'), ('😌', 'show calm')])
    rpp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:34px">ACT IT OUT</div><div class="dir">{''.join(f'<span class="s"><i>{i}</i>{w}</span>' for i, w in dirs)}</div></div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr">{rp}</div>{ftr('Role-Play Cards')}</div>'''

    # D. Desk strips
    d = Cn['strip']
    sc_ = d.get('choices') or C
    he, hs, hk = d.get('head') or t['choices_head']
    cope = ''.join(f'''<div style="text-align:center"><div class="pic" style="height:1.05in;background-image:url({img(k)});background-position:center 30%;border-radius:10px"></div>
 <div style="font-family:var(--round);font-weight:700;font-size:13px;line-height:1.05;margin-top:4px">{en}</div></div>''' for k, en, *_ in sc_)
    strip = f'''<div class="card" style="border:2px dashed #aaa;padding:.12in .16in;flex-direction:row;gap:.14in;align-items:stretch">
 <div style="width:1.25in;display:flex;flex-direction:column;justify-content:center;flex:none">
  <div style="font-family:var(--disp);font-size:22px;line-height:1;color:var(--red);-webkit-text-stroke:1px var(--char);paint-order:stroke fill">{he}</div>
  <div class="lang" style="font-size:10px;margin-top:4px">ES {hs}<br>KR {hk}</div></div>
 <div style="flex:1;display:grid;grid-template-columns:repeat({len(sc_)},1fr);gap:.08in;align-items:center">{cope}</div></div>'''
    dsp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:30px">{d['title']}</div><div class="tag">✂ cut · tape to desk</div></div>
<div class="cards" style="grid-template-columns:1fr;grid-template-rows:repeat(4,1fr)">{strip * 4}</div>{ftr('Desk Strips')}</div>'''

    # E. Coloring page
    c = Cn['coloring']
    colp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:40px">{c['title']}</div><div class="tag">🖍 color</div></div>
<div style="flex:1;border:4px solid var(--char);border-radius:20px;background:#fff url({b64('img/' + c['art'])}) center/contain no-repeat;margin-bottom:.15in"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:.2in">
<div><div style="font-family:var(--read);font-weight:700;font-size:24px">{c['prompt']}</div>
<div class="lang" style="font-size:13px">{c['prompt_lang']}</div></div></div>
<div style="height:2.2in;border:4px dashed var(--char);border-radius:20px;background:#fff;margin-top:.1in"></div>
{ftr('Coloring Page')}</div>'''

    w = PdfWriter()
    for k, (h, o) in enumerate([(mat, 'L'), (sortp, 'P'), (seqp, 'L'), (rpp, 'P'), (dsp, 'P'), (colp, 'P')]):
        hp = os.path.join(td, f'_c{k}.html')
        open(hp, 'w').write(K_HEAD.format(ff=fontface(), base=BASE_CSS, size='8.5in 11in' if o == 'P' else '11in 8.5in') + h + '</body></html>')
        pp = os.path.join(td, f'_c{k}.pdf')
        render_pdf(hp, pp, '8.5in' if o == 'P' else '11in', '11in' if o == 'P' else '8.5in')
        w.append(pp)
    w.write(os.path.join(od, N['centers']))
    return [N['centers']]


def build(t):
    return minibook(t) + centers(t)
