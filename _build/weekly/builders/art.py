SKIN=['#8D5524','#C68642','#E0AC69','#5C3A21','#A0522D','#F1C27D']
SHIRT=['#E21C24','#7B4FBF','#2B6CB0','#F2A007','#2F855A','#D53F8C']
def person(x,y,s=1.0,skin=0,shirt=0,hair='short',arm=None,face='smile'):
    k=SKIN[skin%6];c=SHIRT[shirt%6];o=[]
    o.append(f'<g transform="translate({x},{y}) scale({s})">')
    o.append(f'<path d="M-34 120 V62 Q-34 34 0 34 Q34 34 34 62 V120 Z" fill="{c}"/>')
    if arm=='up': o.append(f'<path d="M26 52 Q52 20 46 -6" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="46" cy="-10" r="9" fill="{k}"/>')
    elif arm=='out': o.append(f'<path d="M26 56 Q56 60 82 50" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="86" cy="49" r="9" fill="{k}"/>')
    elif arm=='down': o.append(f'<path d="M26 56 Q48 80 54 104" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="55" cy="108" r="9" fill="{k}"/>')
    if hair=='puffs': o.append(f'<circle cx="-22" cy="-22" r="12" fill="#2a1a10"/><circle cx="22" cy="-22" r="12" fill="#2a1a10"/>')
    if hair=='long': o.append(f'<path d="M-26 -6 Q-30 40 -20 50 H20 Q30 40 26 -6 Z" fill="#3b2314"/>')
    o.append(f'<circle cx="0" cy="0" r="26" fill="{k}"/>')
    if hair in('short','puffs','long'): o.append('<path d="M-26 -4 Q-24 -30 0 -30 Q24 -30 26 -4 Q14 -16 0 -16 Q-14 -16 -26 -4Z" fill="#2a1a10"/>')
    if hair=='hijab': o.append(f'<path d="M-32 30 Q-36 -34 0 -34 Q36 -34 32 30 Q20 18 18 0 Q16 -18 0 -18 Q-16 -18 -18 0 Q-20 18 -32 30Z" fill="#7B4FBF"/>')
    if hair=='cap': o.append('<path d="M-26 -6 Q-24 -30 0 -30 Q24 -30 26 -6 Z M20 -10 H42" fill="#2B6CB0" stroke="#2B6CB0" stroke-width="6" stroke-linecap="round"/>')
    o.append('<circle cx="-9" cy="-2" r="3" fill="#1a1a1a"/><circle cx="9" cy="-2" r="3" fill="#1a1a1a"/>')
    if face=='smile': o.append('<path d="M-9 10 Q0 18 9 10" stroke="#1a1a1a" stroke-width="3" fill="none" stroke-linecap="round"/>')
    else: o.append('<path d="M-7 13 H7" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/>')
    o.append('</g>');return ''.join(o)

def svg(body,vb='0 0 900 560',bg='#f2e7cc',cls='',extra=''):
    c=f' class="{cls}"' if cls else ''
    return f'<svg{c} xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-hidden="true"{extra}><rect width="900" height="560" fill="{bg}"/>{body}</svg>'

def sign(x,y,w,h,txt,fs=26,fill='#fff'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#232323" stroke-width="5"/><text x="{x+w/2}" y="{y+h/2+fs*0.36}" font-family="Oswald,sans-serif" font-weight="700" font-size="{fs}" text-anchor="middle" fill="#232323">{txt}</text>'

def bubble(x,y,w,h,txt,fs=24,tail='left'):
    t=f'M{x+30} {y+h} L{x+18} {y+h+26} L{x+56} {y+h}' if tail=='left' else f'M{x+w-56} {y+h} L{x+w-18} {y+h+26} L{x+w-30} {y+h}'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#fff" stroke="#232323" stroke-width="4"/><path d="{t}" fill="#fff" stroke="#232323" stroke-width="4" stroke-linejoin="round"/><rect x="{x+20}" y="{y+h-6}" width="44" height="10" fill="#fff"/><text x="{x+w/2}" y="{y+h/2+fs*0.36}" font-family="Andika,sans-serif" font-weight="700" font-size="{fs}" text-anchor="middle" fill="#232323">{txt}</text>'

# --- Scenes ---
def hallway(sign_txt='WALK · RESPECT · ON THE RIGHT', labels=True):
    b=[]
    b.append('<rect y="430" width="900" height="130" fill="#d9c9a3"/><path d="M0 430 H900" stroke="#232323" stroke-width="5"/>')
    b.append('<rect x="40" y="40" width="820" height="70" fill="#fff" stroke="#232323" stroke-width="5" rx="10"/>')
    b.append(f'<text x="450" y="88" font-family="Oswald,sans-serif" font-weight="700" font-size="36" text-anchor="middle" fill="#232323">{sign_txt}</text>')
    # door
    b.append('<rect x="520" y="140" width="170" height="290" fill="#8bb8e8" stroke="#232323" stroke-width="6"/><rect x="550" y="170" width="110" height="90" fill="#fff" stroke="#232323" stroke-width="5"/>')
    b.append('<path d="M690 140 L780 170 V410 L690 430 Z" fill="#c9302c" stroke="#232323" stroke-width="6" stroke-linejoin="round"/><rect x="750" y="285" width="20" height="10" rx="4" fill="#232323"/>')
    b.append('<text x="605" y="225" font-family="Oswald,sans-serif" font-weight="700" font-size="24" text-anchor="middle" fill="#E21C24">ROOM 63</text>')
    # door holder at the door edge, arm out to door
    b.append(person(830,300,1.0,skin=1,shirt=4,hair='cap',arm=None))
    b.append('<path d="M806 356 Q790 350 772 326" stroke="#2F855A" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="768" cy="320" r="10" fill="#C68642"/>')
    # walkers
    b.append(person(140,300,1.0,skin=0,shirt=0,hair='puffs'))
    b.append(person(280,300,1.0,skin=3,shirt=2,hair='short'))
    b.append(person(420,300,1.0,skin=2,shirt=1,hair='hijab'))
    b.append('<path d="M80 470 H500 M470 452 L500 470 L470 488" stroke="#232323" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return ''.join(b)

def cafeteria():
    b=['<rect y="400" width="900" height="160" fill="#d9c9a3"/><path d="M0 400 H900" stroke="#232323" stroke-width="5"/>']
    b.append('<rect x="60" y="300" width="460" height="30" rx="8" fill="#F9DC7C" stroke="#232323" stroke-width="5"/><path d="M110 330 V460 M470 330 V460" stroke="#232323" stroke-width="10"/>')
    b.append(person(170,200,0.95,skin=4,shirt=3,hair='long'))
    b.append(person(330,200,0.95,skin=0,shirt=5,hair='short',arm='out'))
    b.append('<rect x="380" y="240" width="110" height="18" rx="5" fill="#cfd8dc" stroke="#232323" stroke-width="4"/>')
    b.append('<path d="M400 296 Q430 286 470 296" stroke="#2B6CB0" stroke-width="8" fill="none" stroke-linecap="round"/>')
    # bins
    b.append('<path d="M640 260 H740 L728 420 H652 Z" fill="#2F855A" stroke="#232323" stroke-width="5"/><text x="690" y="350" font-family="Oswald" font-weight="700" font-size="26" fill="#fff" text-anchor="middle">TRAY</text>')
    b.append('<path d="M760 260 H860 L848 420 H772 Z" fill="#4A4A4A" stroke="#232323" stroke-width="5"/><text x="810" y="350" font-family="Oswald" font-weight="700" font-size="26" fill="#fff" text-anchor="middle">TRASH</text>')
    b.append(sign(540,60,330,80,'CLEAN YOUR SPOT',32))
    return ''.join(b)

def ripple():
    b=['<rect y="420" width="900" height="140" fill="#d9c9a3"/>']
    xs=[120,300,480,660,820]
    for i,x in enumerate(xs):
        b.append(person(x,280,0.9,skin=i,shirt=i+1,hair=['puffs','short','hijab','long','cap'][i]))
        if i<4: b.append(f'<path d="M{x+50} 250 Q{x+90} 200 {x+130} 250" stroke="#E21C24" stroke-width="6" fill="none" stroke-dasharray="4 10" stroke-linecap="round"/><path d="M{x+118} 238 L{x+132} 252 L{x+114} 258" stroke="#E21C24" stroke-width="6" fill="none" stroke-linecap="round"/>')
    b.append('<circle cx="120" cy="150" r="34" fill="#F9DC7C" stroke="#232323" stroke-width="5"/><path d="M106 150 l10 10 18 -20" stroke="#232323" stroke-width="6" fill="none" stroke-linecap="round"/>')
    b.append('<text x="450" y="90" font-family="Oswald,sans-serif" font-weight="700" font-size="40" text-anchor="middle" fill="#232323">ONE CHOICE… THEN WHAT?</text>')
    return ''.join(b)

def checkin_reveal(txt='SAFE · RESPECTFUL · RESPONSIBLE'):
    b=['<rect y="420" width="900" height="140" fill="#d9c9a3"/>']
    b.append(sign(90,50,720,90,txt,38,'#F9DC7C'))
    b.append(person(200,290,1.05,skin=0,shirt=0,hair='puffs',arm='up'))
    b.append(person(450,290,1.05,skin=2,shirt=2,hair='short'))
    b.append(person(700,290,1.05,skin=4,shirt=1,hair='hijab',arm='up'))
    b.append(bubble(500,170,250,70,'Good morning!',28,'left'))
    return ''.join(b)
