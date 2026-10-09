"""Student deck: one self-contained 7-slide HTML (1600x900 stage, presenter notes on N) plus a PDF."""
import os
from common import *


def html(T, has_song=True):
    D, t = T['deck'], T['title']
    N = names(T)

    def foot(n):
        return f'''<div class="ft"><span class="logo">{LOGO_SVG}Matchbook Learning</span>
    <span>Morning Meeting · K–2 Behavior Toolkit · {t}</span><span class="pn">{n:02d}</span></div>'''

    def head(eyebrow, title, color='var(--red)'):
        return f'''<div class="kente bar"></div><div class="eb">{eyebrow}</div><h2 class="ttl" style="color:{color}">{title}</h2>'''

    def pic(name, cls='', pos='center', extra=''):
        return f'<div class="pic {cls}" style="background-image:url({img(name)});background-position:{pos};{extra}"></div>'

    S = []
    # 1 Title & Promise
    s = D['s1']
    song_btn = '\n    <button class="song" id="songbtn" type="button"><span class="tri"></span>Play the song</button>' if has_song else ''
    S.append(f'''<section class="slide paper">
<div class="kente bar"></div>
<div class="s1">
  <div class="l">
    <div class="eb">{D['eyebrow']}</div>
    <h1 class="ttl big">{'<br>'.join(T['title_lines'])}</h1>
    <div class="sub">{T['subtitle']}</div>
    <div class="bub">{s['bubble']}</div>
    <div class="wb">{s['words']}</div>{song_btn}
  </div>
  <div class="r">{pic(s['img'],'tilt',s['pos'])}<span class="tape" style="top:-10px;left:42%"></span></div>
</div><div class="credit">{CREDIT}</div>{foot(1)}</section>''')
    # 2 Regulate
    s = D['s2']
    cards = ''.join(f'''
    <div class="card g"><div class="ic">{ic}</div><div><div class="lb">{lb}</div><div class="tx">{tx}</div></div></div>''' for ic, lb, tx in s['cards'])
    S.append(f'''<section class="slide paper">{head(s['eyebrow'],s['title'],s['color'])}
<div class="row2">
  <div class="big-pic">{pic(s['img'],'',s['pos'])}</div>
  <div class="stack">{cards}
    <div class="pill">{s['pill']}</div>
  </div>
</div>{foot(2)}</section>''')
    # 3 Orient: the story
    s = D['s3']
    cards = ''.join(f'''<div class="st" style="--b:{p['color']}">{pic(p['img'],'',p['pos'])}<div class="sn" style="background:{p['color']}">{p['num']}</div><div class="sl">{p['label']}</div></div>''' for p in s['panels'])
    S.append(f'''<section class="slide paper">{head(s['eyebrow'],s['title'],s['color'])}
<div class="story">{cards}</div>
<div class="say"><span>{s['say_label']}</span> {s['say']}</div>{foot(3)}</section>''')
    # 4 Connect
    s = D['s4']
    faces = ''.join(f'''<div class="fc">{pic(k,'face',s['face_pos'])}<div class="fl">{lab}</div></div>''' for k, lab in s['faces'])
    S.append(f'''<section class="slide paper">{head(s['eyebrow'],s['title'],s['color'])}
<div class="row2">
  <div class="big-pic">{pic(s['img'],'',s['pos'])}</div>
  <div class="stack">
    <div class="frame"><div class="fh">{s['frame']}</div><div class="stem">{s['stem']}</div>
    <div class="faces">{faces}</div></div>
    <div class="kk">{pic(s['talk_img'],'mini',s['talk_pos'])}<div>{s['talk_text']}</div></div>
  </div>
</div>{foot(4)}</section>''')
    # 5 Practice
    s = D['s5']
    fit = 'background-size:contain;background-repeat:no-repeat;background-color:#fff' if s.get('choice_fit') == 'contain' else ''
    cope = ''.join(f'''<div class="cp">{pic(c[0],'ci',s['choice_pos'],fit)}<div class="cl">{c[1]}</div></div>''' for c in s['choices'])
    S.append(f'''<section class="slide paper">{head(s['eyebrow'],s['title'],s['color'])}
<div class="scene"><div class="sc">{pic(s['img'],'',s['pos'])}</div>
<div class="prompt"><div class="q">{s['q']}</div><div class="q2">{s['q2']}</div></div></div>
<div class="cps"{grid_cols(len(s['choices']), 5)}>{cope}</div>{foot(5)}</section>''')
    # 6 Commit
    s = D['s6']
    choices = ''.join(f'''<div class="cc">{pic(c[0],'ci',s['choice_pos'])}<div class="cl">{c[1]}</div></div>''' for c in s['choices'])
    S.append(f'''<section class="slide yellowish">{head(s['eyebrow'],s['title'],s['color'])}
<div class="row2">
  <div class="big-pic tall">{pic(s['img'],'',s['pos'])}</div>
  <div class="stack">
    <div class="vow">{s['vow']}</div>
    <div class="frame"><div class="fh">{s['frame']}</div><div class="stem s6">{s['stem']}</div>
    <div class="ccs"{grid_cols(len(s['choices']), 3)}>{choices}</div></div>
  </div>
</div>{foot(6)}</section>''')
    # 7 Transition
    s = D['s7']
    steps = ''.join(f'''<div class="sp"><div class="n">{n}</div><div class="ic">{ic}</div><div class="sl">{l}</div></div>''' for n, (ic, l) in enumerate(s['steps'], 1))
    S.append(f'''<section class="slide paper">{head(s['eyebrow'],s['title'],s['color'])}
<div class="row2">
  <div class="big-pic">{pic(s['img'],'',s['pos'])}</div>
  <div class="stack"><div class="steps">{steps}</div><div class="pill r">{s['pill']}</div></div>
</div>{foot(7)}</section>''')

    nb = ''
    for i, n in enumerate(D['notes']):
        li = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
        nb += f'''<div class="note-block"><h3>Slide {i+1} · {n['name']} <span class="rub">{n['rubric']}</span></h3>
<p class="script">{n['script']}</p>
<div class="grid"><div><p class="k">Look for</p>{li(n['look'])}</div><div><p class="k">If it breaks</p>{li(n['breaks'])}</div>
<div><p class="k">Support adult</p>{li(n['support'])}</div><div><p class="k">Language support</p>{li(n['language'])}</div></div>
<p class="move"><b>Engagement move</b> {n['move']}</p>{f'<p class="aside">{n["aside"]}</p>' if n.get('aside') else ''}</div>'''

    song = N['song']
    vid_div = f'''
<div class="vid" id="vid"><video id="vplayer" controls preload="none" src="{song}"></video><div><button id="vclose" type="button">Close video (Esc)</button></div><div class="hint">If the video does not play, keep the file {song} in the same folder as this deck.</div></div>''' if has_song else ''
    if has_song:
        vid_js = '''
 var vid=document.getElementById('vid'),vp=document.getElementById('vplayer');
 function vopen(){vid.classList.add('show');try{vp.currentTime=0;vp.play();}catch(e){}}
 function vclose(){vp.pause();vid.classList.remove('show');}
 document.getElementById('songbtn').onclick=vopen;document.getElementById('vclose').onclick=vclose;'''
        vid_key = '''
  if(vid.classList.contains('show')){if(e.key==='Escape'){vclose();}return;}'''
    else:
        vid_js = ''
        vid_key = ''

    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t} · Grades K–2 | Morning Meeting</title><style>{fontface()}{BASE_CSS}{CSS}</style></head><body>
<div class="hud"><button id="prev">&larr;</button><button id="next">&rarr;</button><button id="nbtn">Notes (N)</button><button id="pbtn">Print / PDF</button><span class="cnt" id="cnt"></span></div>
<div class="viewport"><div class="stage" id="stage">{''.join(S)}</div></div>
<div class="notes" id="notes">{nb}</div>{vid_div}
<script>
(function(){{
 var slides=[].slice.call(document.querySelectorAll('.slide')),notes=[].slice.call(document.querySelectorAll('.note-block'));
 var panel=document.getElementById('notes'),cnt=document.getElementById('cnt'),stage=document.getElementById('stage'),i=0,open=false;
 function fit(){{var h=open?window.innerHeight*0.42:window.innerHeight;var s=Math.min(window.innerWidth/1600,h/900);stage.style.transform='scale('+s+')';
   document.querySelector('.viewport').style.bottom=open?(window.innerHeight*0.58)+'px':'0';}}
 function draw(){{slides.forEach(function(s,n){{s.classList.toggle('active',n===i)}});notes.forEach(function(s,n){{s.style.display=(n===i?'block':'none')}});cnt.textContent=(i+1)+' / '+slides.length;}}
 function go(d){{i=Math.max(0,Math.min(slides.length-1,i+d));draw();}}
 function toggle(){{open=!open;panel.classList.toggle('show',open);document.getElementById('nbtn').textContent=open?'Hide notes (N)':'Notes (N)';fit();}}{vid_js}
 document.addEventListener('keydown',function(e){{{vid_key}
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){{e.preventDefault();go(1);}}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();go(-1);}}
  else if(e.key==='n'||e.key==='N'){{e.preventDefault();toggle();}}
  else if(e.key==='Home'){{i=0;draw();}} else if(e.key==='End'){{i=slides.length-1;draw();}}}});
 document.getElementById('prev').onclick=function(){{go(-1)}};document.getElementById('next').onclick=function(){{go(1)}};
 document.getElementById('nbtn').onclick=toggle;document.getElementById('pbtn').onclick=function(){{window.print()}};
 window.addEventListener('resize',fit);fit();draw();
}})();
</script></body></html>'''


def grid_cols(n, default):
    """Inline column override when a choice row has a different count than the stylesheet expects."""
    return '' if n == default else f' style="grid-template-columns:repeat({n},1fr)"'


def build(T, outdir):
    N = names(T)
    has_song = song_source(T, outdir) is not None
    h = os.path.join(outdir, N['deck_html'])
    open(h, 'w').write(html(T, has_song))
    render_pdf(h, os.path.join(outdir, N['deck_pdf']), '1600px', '900px')
    return [N['deck_html'], N['deck_pdf']]


CSS = r'''
html,body{margin:0;height:100%;background:#111;font-family:var(--round);}
.viewport{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
.stage{width:1600px;height:900px;position:relative;transform-origin:center center;flex:none}
.slide{position:absolute;inset:0;display:none;flex-direction:column;padding:0 64px 0;box-sizing:border-box;overflow:hidden}
.slide.active{display:flex}
.yellowish{background:#FFF1BF;background-image:linear-gradient(rgba(242,183,5,.18) 1px,transparent 1px),linear-gradient(90deg,rgba(242,183,5,.18) 1px,transparent 1px);background-size:22px 22px}
.bar{height:22px;margin:0 -64px 18px}
.eb{font-family:var(--round);font-weight:600;text-transform:uppercase;letter-spacing:.14em;font-size:24px;color:#555}
h2.ttl{font-size:92px;margin:4px 0 22px;-webkit-text-stroke:3px var(--char);text-shadow:6px 6px 0 var(--char)}
.ttl.big{font-size:190px;margin:6px 0 0;-webkit-text-stroke:4px var(--char);text-shadow:9px 9px 0 var(--char)}
.pic{background-size:cover;background-repeat:no-repeat;border:5px solid var(--char);border-radius:26px;box-shadow:8px 8px 0 var(--char);background-color:#fff}
.ft{margin-top:auto;display:flex;justify-content:space-between;align-items:center;padding:14px 0 18px;font-size:18px;color:#666;letter-spacing:.04em}
.ft .logo{font-size:20px}.ft .pn{font-family:var(--disp);font-size:28px;color:var(--char)}
/* 1 */
.s1{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.s1 .r{position:relative;height:600px}.s1 .r .pic{position:absolute;inset:0}
.tilt{transform:rotate(2deg)}
.sub{font-weight:600;font-size:46px;color:var(--char);margin:10px 0 26px}
.bub{position:relative;display:inline-block;background:#fff;border:5px solid var(--char);border-radius:40px;padding:22px 34px;font-weight:700;font-size:42px;line-height:1.15;color:var(--char);box-shadow:6px 6px 0 var(--gold);max-width:640px}
.bub:after{content:'';position:absolute;right:-34px;top:40%;border:18px solid transparent;border-left:30px solid var(--char)}
.wb{margin-top:30px;font-family:var(--read);font-size:28px;color:#555}
/* shared */
.row2{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:54px;align-items:stretch;min-height:0;padding-bottom:10px}
.big-pic{position:relative}.big-pic .pic{position:absolute;inset:0}
.big-pic.tall .pic{background-position:center 20%!important}
.stack{display:flex;flex-direction:column;justify-content:center;gap:26px}
.card{display:flex;align-items:center;gap:26px;background:#fff;border:5px solid var(--char);border-radius:26px;padding:22px 28px;box-shadow:6px 6px 0 var(--green)}
.card .ic{font-size:84px;line-height:1}.card .lb{font-family:var(--disp);font-size:52px;color:var(--char);line-height:1}
.card .tx{font-size:34px;color:#444;margin-top:6px}
.pill{align-self:flex-start;background:var(--green);color:#fff;font-family:var(--disp);font-size:44px;padding:12px 30px;border-radius:60px;border:5px solid var(--char)}
.pill.r{background:var(--red)}
/* 3 */
.story{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:30px;min-height:0}
.st{position:relative;display:flex;flex-direction:column}
.st .pic{flex:1;border-color:var(--b)}
.sn{position:absolute;top:-14px;left:-14px;width:68px;height:68px;border-radius:50%;border:5px solid var(--char);color:#fff;font-family:var(--disp);font-size:44px;display:flex;align-items:center;justify-content:center;z-index:2}
.sl{font-family:var(--disp);font-size:46px;text-align:center;margin-top:16px;color:var(--char)}
.say{margin:22px 0 0;background:var(--red);color:#fff;border:5px solid var(--char);border-radius:22px;padding:14px 28px;font-family:var(--disp);font-size:46px}
.say span{color:var(--yellow);margin-right:12px}
/* 4 */
.frame{background:#fff;border:5px dashed var(--char);border-radius:26px;padding:20px 26px}
.fh{font-weight:600;text-transform:uppercase;letter-spacing:.14em;font-size:20px;color:#777}
.stem{font-family:var(--disp);font-size:58px;color:var(--char);margin:4px 0 14px}
.faces{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.fc{text-align:center}.face{height:160px;border-radius:50%!important;box-shadow:5px 5px 0 var(--char)}
.fl{font-family:var(--disp);font-size:38px;margin-top:8px;color:var(--char)}
.kk{display:flex;align-items:center;gap:22px;font-weight:700;font-size:34px;color:var(--char)}
.mini{width:220px;height:124px;flex:none;box-shadow:5px 5px 0 var(--char)}
/* 5 */
.scene{display:flex;gap:34px;align-items:center;height:300px}
.sc{position:relative;width:520px;height:100%;flex:none}.sc .pic{position:absolute;inset:0}
.q{font-family:var(--disp);font-size:66px;color:var(--char);line-height:1.05}
.q2{font-family:var(--disp);font-size:66px;color:var(--red);line-height:1.05;margin-top:12px}
.cps{display:grid;grid-template-columns:repeat(5,1fr);gap:26px;margin-top:34px}
.cp,.cc{text-align:center}
.ci{height:210px;box-shadow:6px 6px 0 var(--gold)}
.cl{font-family:var(--disp);font-size:34px;line-height:1.05;margin-top:12px;color:var(--char)}
/* 6 */
.vow{font-family:var(--disp);font-size:72px;color:var(--red);-webkit-text-stroke:2px var(--char);paint-order:stroke fill;text-shadow:4px 4px 0 var(--char)}
.ccs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.ccs .ci{height:150px}.ccs .cl{font-size:26px}
.ccs+x{} .frame .stem.s6{font-size:46px}
/* 7 */
.steps{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.sp{background:#fff;border:5px solid var(--char);border-radius:24px;padding:16px;text-align:center;box-shadow:6px 6px 0 var(--green)}
.sp .n{font-family:var(--disp);font-size:36px;color:#aaa;line-height:1}.sp .ic{font-size:70px;line-height:1.1}
.sp .sl{font-size:38px;margin-top:4px}
/* notes + hud */
.notes{position:fixed;left:0;right:0;bottom:0;max-height:58vh;overflow:auto;background:#0d0d0d;color:#f2f2f2;border-top:4px solid var(--red);padding:20px clamp(20px,4vw,56px) 28px;display:none;z-index:60;font-family:Inter,system-ui,sans-serif;font-size:14.5px;line-height:1.55}
.notes.show{display:block}
.notes h3{font-family:var(--round);text-transform:uppercase;letter-spacing:.12em;font-size:13px;margin:0 0 10px;color:var(--yellow)}
.notes .script{font-size:17px;line-height:1.55;margin:0 0 14px;padding:12px 14px;background:rgba(255,255,255,.07);border-left:4px solid var(--yellow);border-radius:0 8px 8px 0}
.notes .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.notes .k{font-family:var(--round);text-transform:uppercase;letter-spacing:.1em;font-size:11px;color:#94a3b8;margin:0 0 5px}
.notes ul{margin:0;padding-left:18px}.notes li{margin-bottom:4px}
.notes .rub{display:inline-block;background:var(--red);color:#fff;padding:2px 9px;border-radius:20px;font-size:11px;letter-spacing:.1em}
.notes .move{margin:14px 0 0;padding:10px 14px;background:rgba(31,138,76,.22);border-radius:8px}
.notes .move b{font-family:var(--round);text-transform:uppercase;letter-spacing:.1em;font-size:11px;color:#9be3b6;margin-right:6px}
.notes .aside{margin:10px 0 0;font-size:13px;color:#cbd5e1;font-style:italic}
.note-block{display:none}
.hud{position:fixed;top:14px;right:16px;z-index:70;display:flex;gap:8px;font-family:var(--round);font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.hud button{font:inherit;background:rgba(0,0,0,.62);color:#fff;border:0;border-radius:20px;padding:7px 13px;cursor:pointer}
.hud button:hover{background:var(--red)}.hud .cnt{background:rgba(0,0,0,.62);color:#fff;border-radius:20px;padding:7px 13px}
.song{margin-top:18px;display:inline-flex;align-items:center;gap:16px;font-family:var(--disp);font-size:34px;color:#fff;background:var(--green);border:4px solid var(--char);border-radius:999px;padding:12px 34px 12px 22px;box-shadow:5px 5px 0 var(--char);cursor:pointer}
.song:hover{background:var(--red)}
.song .tri{width:0;height:0;border-left:26px solid #fff;border-top:16px solid transparent;border-bottom:16px solid transparent}
.credit{position:absolute;right:64px;bottom:80px;text-align:right;font-family:var(--round);font-size:14px;color:#777}
.vid{position:fixed;inset:0;z-index:90;background:rgba(20,20,20,.94);display:none;align-items:center;justify-content:center;flex-direction:column;gap:14px}
.vid.show{display:flex}.vid video{width:min(92vw,160vh);max-height:84vh;background:#000;border-radius:10px}
.vid button{font-family:var(--round);font-size:15px;letter-spacing:.08em;text-transform:uppercase;background:#fff;color:#232323;border:0;border-radius:20px;padding:8px 18px;cursor:pointer}
.vid .hint{font-family:var(--round);color:#bbb;font-size:13px}
@media print{
  @page{size:1600px 900px;margin:0}
  html,body{background:#fff;height:auto}
  .viewport{position:static;display:block}.stage{transform:none!important;width:1600px;height:auto}
  .hud,.notes,.vid,.song{display:none!important}
  .slide{display:flex!important;position:relative;width:1600px;height:900px;page-break-after:always;break-after:page}
}
'''
