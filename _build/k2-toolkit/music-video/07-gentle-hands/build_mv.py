import subprocess, os, re
from PIL import Image, ImageDraw, ImageFont
os.chdir('/home/claude/mv')
W,H=1280,720
BEAT0,BEAT=0.19,60/92.285
def snap(t):
    if t<=0.05 or t>=83: return t
    k=round((t-BEAT0)/BEAT); return round(BEAT0+k*BEAT,3)

# (end_time, clip, src_in) ; start = previous end
SEG=[(6.04,'01',0.5),(9.6,'08',0.0),(12.6,'03',1.0),(16.0,'08',4.0),(17.6,'09',0.0),
     (21.5,'02',0.5),(24.1,'03',3.0),(27.5,'02',4.5),(30.2,'08',2.0),(33.0,'09',2.0),
     (37.6,'10',0.0),(43.4,'04',1.0),(44.9,'05',2.0),(46.4,'06',2.0),(49.6,'07',1.0),
     (54.2,'02',2.6),(57.0,'09',4.0),(59.6,'07',4.5),
     (64.4,'05',0.5),(68.0,'04',3.0),(69.5,'05',5.5),(71.0,'06',5.0),(75.6,'07',3.0),
     (78.2,'08',5.0),(83.6,'10',2.4)]
LYR=[(1.0,'Matchbook, are you ready? (Ready!)'),(2.5,'Hands up high, hands down low,'),(4.4,"Let's learn it, let's go!"),
 (6.0,'Gentle hands (gentle hands!) keep my friends safe,'),(9.5,'Hitting hurts (hitting hurts!), so I give them space.'),
 (12.5,'High five, fist bump, wave hello,'),(15.6,'Gentle hands everywhere I go!'),
 (17.6,'When my face gets hot and my fists get tight,'),(19.9,'I feel it in my chest, but I can make it right.'),
 (21.6,'Hitting hurts, hitting hurts, my friend feels sad,'),(24.0,"So I don't hit, not even when I'm mad."),
 (27.3,'Gentle hands: high five, fist bump, wave,'),(29.9,"That's how we play, that's how we stay safe."),
 (33.0,'When I feel mad, I can choose! (I can choose!)'),(37.6,'Breathe in slow, blow it out, whoo!'),
 (43.3,'Calm corner, break card, use my words,'),(46.3,"Ask a grown-up, I get help, that's how it works!"),
 (49.6,'Somebody took my truck and I wanted to shout,'),(51.4,'I stopped, took a breath, and I let it out.'),
 (52.8,'"Can I have a turn?" Yeah, I used my words,'),(56.9,"Calm voice, calm hands, now I'm being heard."),
 (59.4,'When I feel mad, I can choose! (I can choose!)'),(64.3,'Breathe in slow, blow it out, whoo!'),
 (67.9,'Calm corner, break card, use my words,'),(70.9,"Ask a grown-up, I get help, that's how it works!"),
 (75.4,'Hitting hurts! (We use gentle hands!)'),(78.0,'Hand on your heart, say it with me:'),
 (80.0,'I use gentle hands. I keep my friends safe.')]
END=83.6

# ---- caption images ----
os.makedirs('cap',exist_ok=True)
fb=ImageFont.truetype('fred7.ttf',44); ft=ImageFont.truetype('lilita.ttf',118); fl=ImageFont.truetype('fred7.ttf',24)
def wrap(txt,font,maxw):
    words=txt.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if font.getlength(t)>maxw and cur: lines.append(cur); cur=w
        else: cur=t
    lines.append(cur); return lines
def caption(i,txt):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    lines=wrap(txt,fb,1080); lh=56; total=lh*len(lines)
    y0=H-40-total
    # band
    pad=18
    bw=max(fb.getlength(l) for l in lines)+60
    d.rounded_rectangle(((W-bw)/2,y0-pad,(W+bw)/2,y0+total+pad-6),radius=26,fill=(35,35,35,200))
    for k,l in enumerate(lines):
        # color call-and-response parts yellow
        x=(W-fb.getlength(l))/2; y=y0+k*lh
        parts=re.split(r'(\([^)]*\)?|[^(]*\))',l)
        for p in parts:
            if not p: continue
            col=(249,220,124) if p.startswith('(') or p.endswith(')') else (255,255,255)
            d.text((x,y),p,font=fb,fill=col,stroke_width=3,stroke_fill=(20,20,20))
            x+=fb.getlength(p)
    im.save(f'cap/c{i:02d}.png')
for i,(t,txt) in enumerate(LYR): caption(i,txt)
# logo bug + title
logo=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(logo)
fl_img=Image.open('/home/claude/marlithaw/cc-teacher_edition/resources/student-decks/_shared/matchbook-flame.png').convert('RGBA')
fl_img.thumbnail((40,44));
d.rounded_rectangle((18,16,18+fl_img.width+238,16+52),radius=26,fill=(255,255,255,215))
logo.alpha_composite(fl_img,(30,20)); d.text((30+fl_img.width+10,28),'MATCHBOOK LEARNING',font=fl,fill=(35,35,35))
logo.save('cap/logo.png')
title=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(title)
tt='GENTLE HANDS'; tw=ft.getlength(tt); x=(W-tw)/2; y=70
d.text((x+8,y+8),tt,font=ft,fill=(35,35,35))
d.text((x,y),tt,font=ft,fill=(226,28,36),stroke_width=5,stroke_fill=(35,35,35))
sub='Morning Meeting · K–2'; sw=fl.getlength(sub)
d.rounded_rectangle(((W-sw)/2-16,y+140,(W+sw)/2+16,y+178),radius=18,fill=(31,138,76))
d.text(((W-sw)/2,y+145),sub,font=fl,fill=(255,255,255))
title.save('cap/title.png')

# ---- video segments ----
inputs=[]; fc=[]; start=0.0
for n,(end,clip,src) in enumerate(SEG):
    e=snap(end) if n<len(SEG)-1 else END
    dur=round(e-start,3)
    assert src+dur<=8.05, (n,clip,src,dur)
    inputs+=['-i',f'clips/{clip}.mp4']
    fc.append(f'[{n}:v]trim=start={src}:duration={dur},setpts=PTS-STARTPTS,scale={W}:{H},fps=24,format=yuv420p[v{n}]')
    start=e
nseg=len(SEG)
fc.append(''.join(f'[v{n}]' for n in range(nseg))+f'concat=n={nseg}:v=1:a=0[base]')
# overlays
ov_inputs=[]; idx=nseg
inputs+=['-i','song.mp4']; aidx=idx; idx+=1
inputs+=['-i','cap/logo.png']; logo_i=idx; idx+=1
inputs+=['-i','cap/title.png']; title_i=idx; idx+=1
cur='base'
fc.append(f'[{cur}][{logo_i}:v]overlay=0:0[o_logo]'); cur='o_logo'
fc.append(f'[{cur}][{title_i}:v]overlay=0:0:enable=\'between(t,0,5.6)\'[o_t]'); cur='o_t'
for i,(t,txt) in enumerate(LYR):
    t2=LYR[i+1][0] if i+1<len(LYR) else END
    inputs+=['-i',f'cap/c{i:02d}.png']
    fc.append(f'[{cur}][{idx}:v]overlay=0:0:enable=\'between(t,{t},{t2-0.04})\'[o{i}]'); cur=f'o{i}'; idx+=1
fc.append(f'[{cur}]fade=t=in:st=0:d=0.4,fade=t=out:st={END-1.2}:d=1.2[vout]')
fc.append(f'[{aidx}:a]atrim=0:{END},afade=t=out:st={END-1.5}:d=1.5[aout]')
cmd=['ffmpeg','-y','-v','error']+inputs+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]',
     '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','Gentle-Hands_Music-Video.mp4']
subprocess.run(cmd,check=True)
print('done')
