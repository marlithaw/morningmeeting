import sys; sys.path.insert(0,'/home/claude/k2/build')
from common import *
L={
'en':dict(t='Gentle Hands',eb='This week in Morning Meeting · Kindergarten to 2nd Grade',
  intro='Your child is learning that hitting hurts and that gentle hands keep everyone safe. Big feelings are okay. Children are practicing calm choices for when they feel mad.',
  sayh='At school we say:',say='Hitting hurts. We use gentle hands.',ch='Calm choices',
  cl=[c[1] for c in COPING],th='Try at home',
  tips=['<b>Breathe together:</b> smell the flower, blow out the candle. Three times.','<b>Ask:</b> “What can you do when you feel mad?” Let your child point to a calm choice.','<b>Notice it:</b> “You used gentle hands with your sister!”'],
  ft='Questions? Talk with your child’s teacher.'),
'es':dict(t='Manos suaves',eb='Esta semana en la Reunión de la Mañana · Kínder a 2.º grado',
  intro='Su hijo o hija está aprendiendo que pegar duele y que las manos suaves nos mantienen seguros. Está bien tener sentimientos fuertes. Los niños practican opciones de calma para cuando se enojan.',
  sayh='En la escuela decimos:',say='Pegar duele. Usamos manos suaves.',ch='Opciones de calma',
  cl=[c[2] for c in COPING],th='Practiquen en casa',
  tips=['<b>Respiren juntos:</b> huelan la flor, soplen la vela. Tres veces.','<b>Pregunte:</b> “¿Qué puedes hacer cuando te enojas?” Deje que su hijo o hija señale una opción de calma.','<b>Fíjese y felicite:</b> “¡Usaste manos suaves con tu hermana!”'],
  ft='¿Preguntas? Hable con el maestro o la maestra de su hijo o hija.'),
'kr':dict(t='Men dous',eb='Semèn sa a nan Reyinyon Maten · Kindègadenn rive 2yèm ane',
  intro='Pitit ou ap aprann ke frape fè mal, epi men dous pwoteje tout moun. Li nòmal pou yon timoun santi gwo santiman. Timoun yo ap pratike chwa pou yo kalme lè yo fache.',
  sayh='Nan lekòl la nou di:',say='Frape fè mal. Nou sèvi ak men dous.',ch='Chwa pou kalme',
  cl=[c[3] for c in COPING],th='Eseye lakay ou',
  tips=['<b>Respire ansanm:</b> pran sant flè a, soufle bouji a. Twa fwa.','<b>Mande:</b> “Kisa ou ka fè lè ou fache?” Kite pitit ou montre yon chwa pou kalme.','<b>Remake l:</b> “Ou te sèvi ak men dous ak sè w!”'],
  ft='Ou gen kesyon? Pale ak pwofesè pitit ou a.'),
}
def half(d):
    icons=''.join(f'''<div class="ic"><div class="pic" style="background-image:url({img(k)})"></div><div class="il">{lab}</div></div>''' for (k,*_),lab in zip(COPING,d['cl']))
    tips=''.join(f'<li>{x}</li>' for x in d['tips'])
    return f'''<div class="half paper"><div class="k kente"></div>
<div class="row"><div class="l">
 <div class="eb">{d['eb']}</div><div class="ttl">{d['t']}</div>
 <p class="in">{d['intro']}</p>
 <div class="say"><span>{d['sayh']}</span> {d['say']}</div>
 <div class="th">{d['th']}</div><ul>{tips}</ul>
</div><div class="r"><div class="pic hero" style="background-image:url({img('high_five')})"></div>
 <div class="ch">{d['ch']}</div><div class="ics">{icons}</div></div></div>
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
body=''.join(f'<div class="sheet"><span class="cut">✂</span>{half(L[k])}{half(L[k])}</div>' for k in ['en','es','kr'])
p='/home/claude/k2/build/family.html'
open(p,'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
render_pdf(p,'/home/claude/k2/out/Gentle-Hands_Family-Half-Sheet.pdf','8.5in','11in')
print('ok')
