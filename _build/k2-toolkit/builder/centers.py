"""Center kit (7 pages, mixed orientation): sort mat + sort cards, sequencing mat + cards, role-play cards,
desk strips, coloring page. Each page group renders to its own PDF, then they are joined in order."""
import os, math
from common import *
import lineart

CSS = '''
@page{size:8.5in 11in;margin:0}
html,body{margin:0}
.sheet{width:8.5in;height:11in;box-sizing:border-box;padding:.4in .45in .35in;position:relative;overflow:hidden;page-break-after:always;break-after:page;display:flex;flex-direction:column}
.sheet.land{width:11in;height:8.5in}
.top{height:12px;margin:-.4in -.45in .22in}
.hrow{display:flex;align-items:center;justify-content:space-between;margin-bottom:.16in}
.h{font-family:var(--disp);font-size:40px;color:var(--red);-webkit-text-stroke:1.5px var(--char);paint-order:stroke fill;text-shadow:3px 3px 0 var(--char)}
.tag{font-family:var(--round);font-weight:700;font-size:14px;letter-spacing:.12em;text-transform:uppercase;background:var(--char);color:#fff;padding:5px 12px;border-radius:30px}
.pic{background-size:cover;background-repeat:no-repeat;border:3px solid var(--char);border-radius:14px;background-color:#fff}
.cards{flex:1;display:grid;gap:0}
.card{border:2px dashed #aaa;padding:.14in;display:flex;flex-direction:column;box-sizing:border-box;min-height:0}
.card .pic{flex:1;min-height:0}
.cl{font-family:var(--round);font-weight:700;font-size:20px;text-align:center;margin-top:.08in;color:var(--char)}
.dir{display:flex;gap:.12in;align-items:center;font-family:var(--round);font-weight:600;font-size:15px;color:#444}
.dir .s{display:flex;align-items:center;gap:6px;background:#fff;border:2px solid var(--char);border-radius:30px;padding:4px 12px}
.dir .s i{font-style:normal;font-size:20px}
.ftr{display:flex;justify-content:space-between;align-items:center;font-family:var(--round);font-size:10px;color:#777;margin-top:.12in}
.ftr .logo{font-size:11px}
.lang{font-size:12px}
'''


def head():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{fontface()}{BASE_CSS}{CSS}</style></head><body>'''


def dirs(items):
    return '<div class="dir">' + ''.join(f'<span class="s"><i>{i}</i>{w}</span>' for i, w in items) + '</div>'


def pages(T, outdir):
    """[(html body, 'P' | 'L')] in print order."""
    C, t = T['centers'], T['title']

    def ftr(name):
        return f'<div class="ftr"><span class="logo">{LOGO_SVG}Matchbook Learning</span><span>{t} · Center Kit · {name}</span></div>'

    # A. Sort mat (landscape) + cards
    s = C['sort']

    def side(d):
        return f''' <div style="border:6px solid {d['color']};border-radius:22px;background:{d['bg']};display:flex;flex-direction:column;align-items:center;padding:.2in">
  <div style="display:flex;align-items:center;gap:.15in"><span class="badge" style="width:64px;height:64px;font-size:{d['size']};background:{d['color']}">{d['symbol']}</span><span style="font-family:var(--disp);font-size:44px;color:{d['color']}">{d['en']}</span></div>
  <div class="lang" style="margin-top:6px"><b>ES</b>{d['es']} · <b>KR</b>{d['kr']}</div></div>'''
    hstyle = f' style="font-size:{s["title_size"]}"' if s.get('title_size') else ''
    mat = f'''<div class="sheet land paper"><div class="top kente"></div>
<div class="hrow"><div class="h"{hstyle}>{s['title']}</div>{dirs(s['dirs'])}</div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:.3in">
{side(s['yes'])}
{side(s['no'])}
</div>{ftr('Picture Sort Mat')}</div>'''
    cards = ''.join(f'<div class="card"><div class="pic" style="background-image:url({img(n)});background-position:{p}"></div></div>' for n, p, _ in s['cards'])
    sortp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:32px">{s['cards_title']}</div><div class="tag">✂ cut</div></div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:repeat({math.ceil(len(s['cards']) / 2)},1fr)">{cards}</div>{ftr('Picture Sort Cards')}</div>'''

    # B. Sequencing (mat + cards, both landscape)
    q = C['seq']
    seq = q['cards']
    slots = ''.join(f'''<div style="border:4px dashed var(--char);border-radius:16px;background:#fff;position:relative">
 <div style="position:absolute;top:-16px;left:-12px;display:flex;align-items:center;gap:8px"><span class="badge" style="width:46px;height:46px;font-size:28px;background:var(--red)">{n}</span>
 <span style="font-family:var(--disp);font-size:24px;background:var(--paper);padding:0 6px">{w}</span></div></div>''' for n, w in [(str(i), w) for i, w in enumerate(q['slots'], 1)])
    sc = ''.join(f'<div class="card"><div class="pic" style="background-image:url({img(seq[k][0])});background-position:{q["pos"]}"></div></div>' for k in q['print_order'])
    seqp = f'''<div class="sheet land paper"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:34px">{q['title']}</div>{dirs(q['dirs'])}</div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:.4in .3in;padding:.25in .1in .1in">{slots}</div>{ftr('Sequencing Mat')}</div>
<div class="sheet land"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:32px">{q['cards_title']}</div><div class="tag">✂ cut</div></div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr">{sc}</div>{ftr('Sequencing Cards')}</div>'''

    # C. Role-play cards
    r = C['roleplay']
    nc = len(r['choices'])
    mini = ''.join(f'<div class="pic" style="height:.62in;background-image:url({img(k)});background-position:center 30%;border-width:2px;border-radius:8px"></div>' for k, *_ in r['choices'])
    rp = ''.join(f'''<div class="card" style="padding:.16in">
 <div class="pic" style="background-image:url({img(n)});background-position:{p}"></div>
 <div style="font-family:var(--disp);font-size:26px;color:var(--char);margin-top:.1in;line-height:1.05">{en}</div>
 <div class="lang"><b>ES</b>{es}</div><div class="lang"><b>KR</b>{ht}</div>
 <div style="font-family:var(--disp);font-size:21px;color:var(--red);margin:.08in 0 .06in">{r['prompt']}</div>
 <div style="display:grid;grid-template-columns:repeat({nc},1fr);gap:5px">{mini}</div></div>''' for n, p, en, es, ht in r['scenes'])
    rpp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:34px">{r['title']}</div>{dirs(r['dirs'])}</div>
<div class="cards" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr">{rp}</div>{ftr('Role-Play Cards')}</div>'''

    # D. Desk strips
    d = C['strips']
    hd = d['head']
    cope = ''.join(f'''<div style="text-align:center"><div class="pic" style="height:1.05in;background-image:url({img(k)});background-position:center 30%;border-radius:10px"></div>
 <div style="font-family:var(--round);font-weight:700;font-size:13px;line-height:1.05;margin-top:4px">{en}</div></div>''' for k, en, es, ht in d['choices'])
    strip = f'''<div class="card" style="border:2px dashed #aaa;padding:.12in .16in;flex-direction:row;gap:.14in;align-items:stretch">
 <div style="width:1.25in;display:flex;flex-direction:column;justify-content:center;flex:none">
  <div style="font-family:var(--disp);font-size:22px;line-height:1;color:var(--red);-webkit-text-stroke:1px var(--char);paint-order:stroke fill">{hd['en']}</div>
  <div class="lang" style="font-size:10px;margin-top:4px">ES {hd['es']}<br>KR {hd['kr']}</div></div>
 <div style="flex:1;display:grid;grid-template-columns:repeat({len(d['choices'])},1fr);gap:.08in;align-items:center">{cope}</div></div>'''
    dsp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:30px">{d['title']}</div><div class="tag">✂ cut · tape to desk</div></div>
<div class="cards" style="grid-template-columns:1fr;grid-template-rows:repeat({d['count']},1fr)">{strip*d['count']}</div>{ftr('Desk Strips')}</div>'''

    # E. Coloring page
    c = C['color']
    art = coloring_art(c, outdir)
    colp = f'''<div class="sheet"><div class="top kente"></div>
<div class="hrow"><div class="h" style="font-size:40px">{c['title']}</div><div class="tag">{c['tag']}</div></div>
<div style="flex:1;border:4px solid var(--char);border-radius:20px;background:#fff url(file://{art}) center/contain no-repeat;margin-bottom:.15in"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:.2in">
<div><div style="font-family:var(--read);font-weight:700;font-size:24px">{c['prompt']}</div>
<div class="lang" style="font-size:13px">ES {c['prompt_es']} · KR {c['prompt_kr']}</div></div></div>
<div style="height:2.2in;border:4px dashed var(--char);border-radius:20px;background:#fff;margin-top:.1in"></div>
{ftr('Coloring Page')}</div>'''
    return [(mat, 'L'), (sortp, 'P'), (seqp, 'L'), (rpp, 'P'), (dsp, 'P'), (colp, 'P')]


def coloring_art(c, outdir):
    """Absolute path of the coloring line art: a ready png from assets/img, or a trace of an image key."""
    if c.get('png'):
        return img_path(c['png'])
    out = os.path.join(work_dir(outdir), f"color_{c['trace']}.png")
    lineart.trace(img_path(c['trace']), out, **c.get('trace_opts', {}))
    return out


def build(T, outdir):
    from pypdf import PdfWriter
    N, wd = names(T), work_dir(outdir)
    w = PdfWriter()
    for k, (h, o) in enumerate(pages(T, outdir)):
        hp = os.path.join(wd, f'_c{k}.html')
        css = head() if o == 'P' else head().replace('size:8.5in 11in', 'size:11in 8.5in')
        open(hp, 'w').write(css + h + '</body></html>')
        pp = os.path.join(wd, f'_c{k}.pdf')
        render_pdf(hp, pp, '8.5in' if o == 'P' else '11in', '11in' if o == 'P' else '8.5in')
        w.append(pp)
    w.write(os.path.join(outdir, N['centers']))
    return [N['centers']]
