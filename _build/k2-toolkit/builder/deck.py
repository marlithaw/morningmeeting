"""Student deck: 7 slides in the Morning Meeting phases, single-file HTML + PDF."""
import os
from common import *
from deck_css import CSS


def build(t):
    D, N = t['deck'], names(t)
    T = t['short']

    def foot(n):
        return f'''<div class="ft"><span class="logo">{LOGO_SVG}Matchbook Learning</span>
    <span>Morning Meeting · K–2 Behavior Toolkit · {T}</span><span class="pn">{n:02d}</span></div>'''

    def head(eyebrow, title, color='var(--red)'):
        return f'''<div class="kente bar"></div><div class="eb">{eyebrow}</div><h2 class="ttl" style="color:{color}">{title}</h2>'''

    def pic(name, cls='', pos='center', extra=''):
        return f'<div class="pic {cls}" style="background-image:url({img(name)});background-position:{pos};{extra}"></div>'

    C = t['choices']
    song = bool(t.get('song'))
    S = []
    s1 = D['s1']
    big = '<br>'.join(t['title_lines'])
    big_size = s1.get('title_size', '')
    S.append(f'''<section class="slide paper">
<div class="kente bar"></div>
<div class="s1">
  <div class="l">
    <div class="eb">{s1['eyebrow']}</div>
    <h1 class="ttl big"{f' style="font-size:{big_size}"' if big_size else ''}>{big}</h1>
    <div class="sub">{t['sub']}</div>
    <div class="bub">{s1['bubble']}</div>
    <div class="wb">{s1['words']}</div>
    {'<button class="song" id="songbtn" type="button"><span class="tri"></span>Play the song</button>' if song else ''}
  </div>
  <div class="r">{pic(s1['img'], 'tilt', s1['pos'])}<span class="tape" style="top:-10px;left:42%"></span></div>
</div><div class="credit">{CREDIT}</div>{foot(1)}</section>''')

    s2 = D['s2']
    S.append(f'''<section class="slide paper">{head('First, We Get Calm', 'GET CALM FIRST', 'var(--green)')}
<div class="row2">
  <div class="big-pic">{pic(s2['img'], '', s2['pos'])}</div>
  <div class="stack">
    <div class="card g"><div class="ic">🌸</div><div><div class="lb">Smell the flower</div><div class="tx">Slow breath in.</div></div></div>
    <div class="card g"><div class="ic">🕯️</div><div><div class="lb">Blow the candle</div><div class="tx">Long breath out.</div></div></div>
    <div class="pill">3 times together</div>
  </div>
</div>{foot(2)}</section>''')

    s3 = D['s3']
    cards = ''.join(f'''<div class="st" style="--b:{c}">{pic(i, '', p)}<div class="sn" style="background:{c}">{n + 1}</div><div class="sl">{l}</div></div>'''
                    for n, (i, l, c, p) in enumerate(s3['panels']))
    S.append(f'''<section class="slide paper">{head('Watch the Story', s3.get('title', 'WHAT HAPPENED?'))}
<div class="story">{cards}</div>
<div class="say"><span>We say:</span> {s3['say']}</div>{foot(3)}</section>''')

    s4 = D['s4']
    faces = ''.join(f'''<div class="fc">{pic(f, 'face', 'center 30%')}<div class="fl">{lab}</div></div>''' for f, lab in s4['faces'])
    S.append(f'''<section class="slide paper">{head('Turn and Talk', s4['title'], 'var(--sky)')}
<div class="row2">
  <div class="big-pic">{pic(s4['img'], '', s4['pos'])}</div>
  <div class="stack">
    <div class="frame"><div class="fh">Say this</div><div class="stem">{s4['stem']}</div>
    <div class="faces">{faces}</div></div>
    <div class="kk">{pic('talk', 'mini', 'center 30%')}<div>Knee to knee.<br>Take turns.</div></div>
  </div>
</div>{foot(4)}</section>''')

    s5 = D['s5']
    row = s5.get('row') or [(C[i][0], C[i][1]) for i in s5['choices']]
    cope = ''.join(f'''<div class="cp">{pic(k, 'ci', 'center 30%')}<div class="cl">{en}</div></div>''' for k, en in row)
    S.append(f'''<section class="slide paper">{head('Watch Me, Then Show Me', s5['title'], 'var(--orange)')}
<div class="scene"><div class="sc">{pic(s5['img'], '', s5['pos'])}</div>
<div class="prompt"><div class="q">{s5['q']}</div><div class="q2">{s5['q2']}</div></div></div>
<div class="cps" style="grid-template-columns:repeat({len(row)},1fr)">{cope}</div>{foot(5)}</section>''')

    s6 = D['s6']
    choices = ''.join(f'''<div class="cc">{pic(C[i][0], 'ci', 'center 30%')}<div class="cl">{C[i][1]}</div></div>''' for i in s6['choices'])
    S.append(f'''<section class="slide yellowish">{head('One Thing I Will Do', 'MY PROMISE TODAY')}
<div class="row2">
  <div class="big-pic tall">{pic(s6['img'], '', 'center 25%')}</div>
  <div class="stack">
    <div class="vow">{s6['vow']}</div>
    <div class="frame"><div class="fh">Point to one</div><div class="stem s6">{s6['stem']}</div>
    <div class="ccs">{choices}</div></div>
  </div>
</div>{foot(6)}</section>''')

    s7 = D['s7']
    steps = ''.join(f'''<div class="sp"><div class="n">{n + 1}</div><div class="ic">{ic}</div><div class="sl">{l}</div></div>''' for n, (ic, l) in enumerate(s7['steps']))
    S.append(f'''<section class="slide paper">{head('How We Leave', 'HOW WE LEAVE', 'var(--green)')}
<div class="row2">
  <div class="big-pic">{pic(s7['img'], '', 'center 40%')}</div>
  <div class="stack"><div class="steps">{steps}</div><div class="pill r">{s7['pill']}</div></div>
</div>{foot(7)}</section>''')

    nb = ''
    li = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    for i, (name, rub, script, look, brk, sup, lang, move, aside) in enumerate(D['notes']):
        nb += f'''<div class="note-block"><h3>Slide {i + 1} · {name} <span class="rub">{rub}</span></h3>
<p class="script">{script}</p>
<div class="grid"><div><p class="k">Look for</p>{li(look)}</div><div><p class="k">If it breaks</p>{li(brk)}</div>
<div><p class="k">Support adult</p>{li(sup)}</div><div><p class="k">Language support</p>{li(lang)}</div></div>
<p class="move"><b>Engagement move</b> {move}</p>{f'<p class="aside">{aside}</p>' if aside else ''}</div>'''

    vid = (f'''<div class="vid" id="vid"><video id="vplayer" controls preload="none" src="{N['song']}"></video><div><button id="vclose" type="button">Close video (Esc)</button></div><div class="hint">If the video does not play, keep the file {N['song']} in the same folder as this deck.</div></div>''' if song else '')
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T} · Grades K–2 | Morning Meeting</title><style>{fontface()}{BASE_CSS}{CSS}</style></head><body>
<div class="hud"><button id="prev">&larr;</button><button id="next">&rarr;</button><button id="nbtn">Notes (N)</button><button id="pbtn">Print / PDF</button><span class="cnt" id="cnt"></span></div>
<div class="viewport"><div class="stage" id="stage">{''.join(S)}</div></div>
<div class="notes" id="notes">{nb}</div>
{vid}
<script>
(function(){{
 var slides=[].slice.call(document.querySelectorAll('.slide')),notes=[].slice.call(document.querySelectorAll('.note-block'));
 var panel=document.getElementById('notes'),cnt=document.getElementById('cnt'),stage=document.getElementById('stage'),i=0,open=false;
 function fit(){{var h=open?window.innerHeight*0.42:window.innerHeight;var s=Math.min(window.innerWidth/1600,h/900);stage.style.transform='scale('+s+')';
   document.querySelector('.viewport').style.bottom=open?(window.innerHeight*0.58)+'px':'0';}}
 function draw(){{slides.forEach(function(s,n){{s.classList.toggle('active',n===i)}});notes.forEach(function(s,n){{s.style.display=(n===i?'block':'none')}});cnt.textContent=(i+1)+' / '+slides.length;}}
 function go(d){{i=Math.max(0,Math.min(slides.length-1,i+d));draw();}}
 function toggle(){{open=!open;panel.classList.toggle('show',open);document.getElementById('nbtn').textContent=open?'Hide notes (N)':'Notes (N)';fit();}}
 var vid=document.getElementById('vid'),vp=document.getElementById('vplayer');
 function vopen(){{vid.classList.add('show');try{{vp.currentTime=0;vp.play();}}catch(e){{}}}}
 function vclose(){{vp.pause();vid.classList.remove('show');}}
 if(vid){{document.getElementById('songbtn').onclick=vopen;document.getElementById('vclose').onclick=vclose;}}
 document.addEventListener('keydown',function(e){{
  if(vid&&vid.classList.contains('show')){{if(e.key==='Escape'){{vclose();}}return;}}
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){{e.preventDefault();go(1);}}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();go(-1);}}
  else if(e.key==='n'||e.key==='N'){{e.preventDefault();toggle();}}
  else if(e.key==='Home'){{i=0;draw();}} else if(e.key==='End'){{i=slides.length-1;draw();}}}});
 document.getElementById('prev').onclick=function(){{go(-1)}};document.getElementById('next').onclick=function(){{go(1)}};
 document.getElementById('nbtn').onclick=toggle;document.getElementById('pbtn').onclick=function(){{window.print()}};
 window.addEventListener('resize',fit);fit();draw();
}})();
</script></body></html>'''
    od = out_dir(t)
    hp = os.path.join(od, N['deck_html'])
    open(hp, 'w').write(html)
    render_pdf(hp, os.path.join(od, N['deck_pdf']), '1600px', '900px')
    return [N['deck_html'], N['deck_pdf']]
