import sys; sys.path.insert(0,'/home/claude/k2/build')
from common import *

T='Gentle Hands'
def foot(n):
    return f'''<div class="ft"><span class="logo">{LOGO_SVG}Matchbook Learning</span>
    <span>Morning Meeting · K–2 Behavior Toolkit · {T}</span><span class="pn">{n:02d}</span></div>'''
def head(eyebrow, title, color='var(--red)'):
    return f'''<div class="kente bar"></div><div class="eb">{eyebrow}</div><h2 class="ttl" style="color:{color}">{title}</h2>'''
def pic(name, cls='', pos='center', extra=''):
    return f'<div class="pic {cls}" style="background-image:url({img(name)});background-position:{pos};{extra}"></div>'

S=[]
# 1 Title & Promise
S.append(f'''<section class="slide paper">
<div class="kente bar"></div>
<div class="s1">
  <div class="l">
    <div class="eb">Morning Meeting · Safe</div>
    <h1 class="ttl big">GENTLE<br>HANDS</h1>
    <div class="sub">with my friends</div>
    <div class="bub">Our hands keep our friends safe!</div>
    <div class="wb">gentle · suave · dous</div>
    <button class="song" id="songbtn" type="button"><span class="tri"></span>Play the song</button>
  </div>
  <div class="r">{pic('welcome','tilt',"center 20%")}<span class="tape" style="top:-10px;left:42%"></span></div>
</div><div class="credit">Lee &amp; Tee characters © AH-HA Coaching and Consulting, used with permission.</div>{foot(1)}</section>''')
# 2 Regulate
S.append(f'''<section class="slide paper">{head('First, We Get Calm','GET CALM FIRST','var(--green)')}
<div class="row2">
  <div class="big-pic">{pic('calm','',"center 30%")}</div>
  <div class="stack">
    <div class="card g"><div class="ic">🌸</div><div><div class="lb">Smell the flower</div><div class="tx">Slow breath in.</div></div></div>
    <div class="card g"><div class="ic">🕯️</div><div><div class="lb">Blow the candle</div><div class="tx">Long breath out.</div></div></div>
    <div class="pill">3 times together</div>
  </div>
</div>{foot(2)}</section>''')
# 3 Orient: the story
story=[('malik_fists','1','Mad!','var(--red)','68% 40%'),('nadege_hurt','2','Ouch.','var(--sky)','40% 35%'),
       ('high_five','3','Gentle hands.','var(--green)','center 15%'),('building','4','Safe and fun!','var(--orange)','center 40%')]
cards=''.join(f'''<div class="st" style="--b:{c}">{pic(i,'',p)}<div class="sn" style="background:{c}">{n}</div><div class="sl">{l}</div></div>''' for i,n,l,c,p in story)
S.append(f'''<section class="slide paper">{head('Watch the Story','WHAT HAPPENED?')}
<div class="story">{cards}</div>
<div class="say"><span>We say:</span> Hitting hurts. We use gentle hands.</div>{foot(3)}</section>''')
# 4 Connect
faces=''.join(f'''<div class="fc">{pic('lee_'+f,'face','center 30%')}<div class="fl">{lab}</div></div>''' for f,lab in [('happy','happy'),('sad','sad'),('mad','mad')])
S.append(f'''<section class="slide paper">{head('Turn and Talk','HOW DOES SHE FEEL?','var(--sky)')}
<div class="row2">
  <div class="big-pic">{pic('nadege_hurt','',"center 35%")}</div>
  <div class="stack">
    <div class="frame"><div class="fh">Say this</div><div class="stem">She feels ___.</div>
    <div class="faces">{faces}</div></div>
    <div class="kk">{pic('talk','mini',"center 30%")}<div>Knee to knee.<br>Take turns.</div></div>
  </div>
</div>{foot(4)}</section>''')
# 5 Practice
cope=''.join(f'''<div class="cp">{pic(k,'ci','center 30%')}<div class="cl">{en}</div></div>''' for k,en,es,ht in COPING)
S.append(f'''<section class="slide paper">{head('Watch Me, Then Show Me','WHEN I FEEL MAD, I CAN','var(--orange)')}
<div class="scene"><div class="sc">{pic('malik_fists','',"center 40%")}</div>
<div class="prompt"><div class="q">A friend takes my truck.</div><div class="q2">I feel mad. I can...</div></div></div>
<div class="cps">{cope}</div>{foot(5)}</section>''')
# 6 Commit
choices=''.join(f'''<div class="cc">{pic(k,'ci','center 30%')}<div class="cl">{en}</div></div>''' for k,en,es,ht in [COPING[1],COPING[0],COPING[4]])
S.append(f'''<section class="slide yellowish">{head('One Thing I Will Do','MY PROMISE TODAY')}
<div class="row2">
  <div class="big-pic tall">{pic('promise','',"center 25%")}</div>
  <div class="stack">
    <div class="vow">I use gentle hands.</div>
    <div class="frame"><div class="fh">Point to one</div><div class="stem s6">When I feel mad, I will ___.</div>
    <div class="ccs">{choices}</div></div>
  </div>
</div>{foot(6)}</section>''')
# 7 Transition
steps=''.join(f'''<div class="sp"><div class="n">{n}</div><div class="ic">{ic}</div><div class="sl">{l}</div></div>''' for n,ic,l in [('1','🧍','Stand up'),('2','🤲','Gentle hands'),('3','👣','Walk'),('4','⭐','Ready to learn')])
S.append(f'''<section class="slide paper">{head('How We Leave','HOW WE LEAVE','var(--green)')}
<div class="row2">
  <div class="big-pic">{pic('leave','',"center 40%")}</div>
  <div class="stack"><div class="steps">{steps}</div><div class="pill r">Gentle hands all day!</div></div>
</div>{foot(7)}</section>''')

NOTES=[
('Title &amp; Promise','R2',
 'Hold up both open hands, palms out, and wiggle the fingers. “These are my hands. Today we learn how our hands keep our friends safe. Show me your hands.” Wait until every hand is up before moving on.',
 ['Every student shows open hands','Eyes on the slide or on you'],
 ['Silly hands: model again, slowly and silently, then invite them back. No lecture.'],
 ['Sit beside any student who has had a hard morning; keep this lesson warm, not corrective'],
 ['“Gentle” is new for many students: say it while softly patting your own arm','Spanish: suave · Kreyòl: dous'],
 'Equity stick: pull one name and ask, “Show me gentle hands.” Any calm open hands earns praise.',
 'Tier note: teach this before trouble, not the morning after a hitting incident in this room. If a child was hit today, wait a day. Never cast a real student as the child in the story.'),
('Regulate · Get Calm First','R1',
 'Model the gesture with them every time. “Smell the flower. Blow out the candle. Long and slow. Three times.” Do it with the class, not from the front.',
 ['Exhale longer than inhale','Shoulders drop','Gesture copied'],
 ['If silliness: model silently once, then invite them back.'],
 ['Breathe audibly beside any student who cannot settle'],
 ['No language demand; gesture carries it','Same two gestures used in every K–2 lesson'],
 'LiveSchool: award a point to a student who breathes all three times with you. Name the behavior: “You breathed slow three times.”',
 ''),
('Orient · The Story','R2, R3',
 'Point to each picture as you tell it. “Malik was mad. He hit Nadege. Ouch! Nadege got hurt and felt sad. Malik could use gentle hands. Then everyone can play safe and have fun.” Then have the class say together: “Hitting hurts. We use gentle hands.”',
 ['Students follow the pictures in order','Whole class repeats the We say line'],
 ['If students laugh at the hurt picture: pause, point to Nadege’s face, ask “How does her face look?”'],
 ['Point to each panel as the teacher narrates'],
 ['Four pictures, three words each; numbers carry the order','Act out “Ouch” by holding your own arm'],
 'Equity stick: “Which picture shows gentle hands? Point.” Pointing is a full answer.',
 'Keep the focus on what Malik can do next time. He is learning, just like us.'),
('Connect · Turn and Talk','R3, R4',
 'Show knee to knee with a student partner. “Turn knee to knee. Look at Nadege. Tell your partner: She feels ___.” Give 30 seconds, then ring back.',
 ['Partners face each other','Most students say “sad” or point to the sad face','Partners take turns'],
 ['If a pair is stuck: kneel in and say the stem with them.','If partners argue: “Take turns. You go first, then you.”'],
 ['Pair any student who needs support with a steady partner before the lesson starts'],
 ['Pointing to a face is a complete answer','Spanish: triste · Kreyòl: tris'],
 'Equity stick: call two names to share. Praise the frame: “You said: She feels sad. Full sentence!”',
 ''),
('Practice · Watch Me, Then Show Me','R3, R4, R5',
 'Read the scene. “A friend takes my truck. I feel mad. I can…” Invite one student to model: show a mad face, then pick a calm move from the row and do it. Narrate what you see and ask the class, “What did they do?” Then the whole class practices together.',
 ['A student models a mad face and then a calm move','Class names the calm move','Whole class rehearses deep breaths and “Can I have a turn?”'],
 ['Excellent model: “Show the class again. Everyone, what calm move did you see?”','Partly right model: “You showed the mad face. Now show us the calm move. Try again.”','Silly model: “Thank you. Let’s see it the safe way.” Call a new student; no commentary.'],
 ['Stand near the calm corner so students can point to the real one'],
 ['Five pictures; students can point instead of naming','Model “Can I have a turn?” as a sentence everyone says'],
 'LiveSchool: award the student model a point for showing a calm move. Name it out loud.',
 'Students model, not the teacher. The teacher narrates and asks the class what they saw.'),
('Commit · My Promise Today','R2, R5',
 'Put your hand on your heart. “Say it with me: I use gentle hands.” Then: “Point to the calm move you will use today when you feel mad.”',
 ['Every student says the promise','Every student points to one choice'],
 ['If a student does not choose: offer two pictures and let them point.'],
 ['Notice and name a student’s promise later in the day'],
 ['Hand on heart carries the promise','Spanish: Uso manos suaves · Kreyòl: Mwen sèvi ak men dous'],
 'Equity stick: pull three names: “Which one did you pick?” Pointing counts.',
 ''),
('Transition · How We Leave','R1, R4, R5',
 '“How we leave is how we start our learning. Stand up. Gentle hands. Walk. Ready to learn. Let’s practice.” Do not time this at K–2.',
 ['Hands to self while moving','Calm walking, not rushing'],
 ['“Let’s try that again. Back to your spot.” Rebuild clean, no commentary on individuals.'],
 ['Stand at the destination, not behind the group'],
 ['Four icons, four words','No timing pressure at this age'],
 'LiveSchool: award a point to the table that walks with gentle hands the whole way.',
 'Gentle hands all day: look for it at centers, in line, and at recess, and name it when you see it.'),
]
nb=''
for i,(name,rub,script,look,brk,sup,lang,move,aside) in enumerate(NOTES):
    li=lambda xs:'<ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
    nb+=f'''<div class="note-block"><h3>Slide {i+1} · {name} <span class="rub">{rub}</span></h3>
<p class="script">{script}</p>
<div class="grid"><div><p class="k">Look for</p>{li(look)}</div><div><p class="k">If it breaks</p>{li(brk)}</div>
<div><p class="k">Support adult</p>{li(sup)}</div><div><p class="k">Language support</p>{li(lang)}</div></div>
<p class="move"><b>Engagement move</b> {move}</p>{f'<p class="aside">{aside}</p>' if aside else ''}</div>'''

CSS=r'''
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
html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gentle Hands · Grades K–2 | Morning Meeting</title><style>{fontface()}{BASE_CSS}{CSS}</style></head><body>
<div class="hud"><button id="prev">&larr;</button><button id="next">&rarr;</button><button id="nbtn">Notes (N)</button><button id="pbtn">Print / PDF</button><span class="cnt" id="cnt"></span></div>
<div class="viewport"><div class="stage" id="stage">{''.join(S)}</div></div>
<div class="notes" id="notes">{nb}</div>
<div class="vid" id="vid"><video id="vplayer" controls preload="none" src="gentle-hands-song.mp4"></video><div><button id="vclose" type="button">Close video (Esc)</button></div><div class="hint">If the video does not play, keep the file gentle-hands-song.mp4 in the same folder as this deck.</div></div>
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
 document.getElementById('songbtn').onclick=vopen;document.getElementById('vclose').onclick=vclose;
 document.addEventListener('keydown',function(e){{
  if(vid.classList.contains('show')){{if(e.key==='Escape'){{vclose();}}return;}}
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){{e.preventDefault();go(1);}}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();go(-1);}}
  else if(e.key==='n'||e.key==='N'){{e.preventDefault();toggle();}}
  else if(e.key==='Home'){{i=0;draw();}} else if(e.key==='End'){{i=slides.length-1;draw();}}}});
 document.getElementById('prev').onclick=function(){{go(-1)}};document.getElementById('next').onclick=function(){{go(1)}};
 document.getElementById('nbtn').onclick=toggle;document.getElementById('pbtn').onclick=function(){{window.print()}};
 window.addEventListener('resize',fit);fit();draw();
}})();
</script></body></html>'''
open('/home/claude/k2/out/gentle-hands-student-deck-k2.html','w').write(html)
print(len(html)//1024,'KB')
