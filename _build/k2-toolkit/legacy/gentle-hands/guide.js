const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,AlignmentType,
  ImageRun,HeadingLevel,LevelFormat,BorderStyle,PageBreak,Footer,Header,PageNumber,TableLayoutType}=require('docx');
const RED='E21C24',CHAR='232323',YEL='F9DC7C',GRN='1F8A4C',GRY='666666';
const IMG=n=>fs.readFileSync('/home/claude/k2/img/'+n+'.jpg');
const W=12240-2*1080; // content width (0.75in margins)
const t=(text,o={})=>new TextRun({text,font:'Calibri',size:o.size||22,bold:o.bold,italics:o.it,color:o.color||'1d1d1f'});
const p=(runs,o={})=>new Paragraph({children:Array.isArray(runs)?runs:[t(runs,o)],spacing:{after:o.after??100,before:o.before??0},alignment:o.align,keepNext:o.keepNext});
const h1=s=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun({text:s,font:'Calibri',size:32,bold:true,color:RED})],spacing:{before:240,after:120},keepNext:true,
  border:{bottom:{style:BorderStyle.SINGLE,size:12,color:YEL,space:4}}});
const h2=s=>new Paragraph({heading:HeadingLevel.HEADING_2,children:[new TextRun({text:s,font:'Calibri',size:25,bold:true,color:CHAR})],spacing:{before:180,after:80},keepNext:true});
const b=(s,lvl=0)=>new Paragraph({numbering:{reference:'bul',level:lvl},children:Array.isArray(s)?s:[t(s)],spacing:{after:60}});
const n=(s)=>new Paragraph({numbering:{reference:'num',level:0},children:Array.isArray(s)?s:[t(s)],spacing:{after:60}});
const border={style:BorderStyle.SINGLE,size:4,color:'BBBBBB'};
const borders={top:border,bottom:border,left:border,right:border};
function table(widths,rows,head=true){
  return new Table({width:{size:W,type:WidthType.DXA},columnWidths:widths,layout:TableLayoutType.FIXED,
    rows:rows.map((r,i)=>new TableRow({cantSplit:true,tableHeader:head&&i===0,children:r.map((c,j)=>new TableCell({
      width:{size:widths[j],type:WidthType.DXA},borders,margins:{top:80,bottom:80,left:110,right:110},
      shading:head&&i===0?{type:ShadingType.CLEAR,fill:CHAR,color:'auto'}:(j===0?{type:ShadingType.CLEAR,fill:'FFF6DA',color:'auto'}:undefined),
      children:(Array.isArray(c)?c:[c]).map(x=>typeof x==='string'?new Paragraph({children:[t(x,{bold:(head&&i===0)||j===0,color:head&&i===0?'FFFFFF':undefined,size:20})],spacing:{after:40}}):x)}))}))});
}
const say=s=>new Paragraph({children:[t(s,{it:true,size:21})],spacing:{after:60},indent:{left:220},border:{left:{style:BorderStyle.SINGLE,size:18,color:YEL,space:8}}});
const small=(s,c=GRY)=>new Paragraph({children:[t(s,{size:18,color:c})],spacing:{after:40},keepNext:true});
const cp=(s)=>new Paragraph({children:[t(s,{size:19})],spacing:{after:40}});

const slides=[
 ['1 · Title & Promise (R2)','Hold up both open hands and wiggle the fingers. “These are my hands. Today we learn how our hands keep our friends safe. Show me your hands.”','Every student shows open hands.','Equity stick: “Show me gentle hands.” Praise any calm open hands.'],
 ['2 · Get Calm First (R1)','Do it with them. “Smell the flower. Blow out the candle. Long and slow. Three times.”','Exhale longer than inhale; shoulders drop.','LiveSchool point: “You breathed slow three times.”'],
 ['3 · What Happened? (R2, R3)','Point to each picture. “Malik was mad. He hit Nadege. Ouch! Nadege got hurt and felt sad. Malik could use gentle hands. Then everyone can play safe.” Class says: “Hitting hurts. We use gentle hands.”','Students follow the pictures; whole class repeats the line.','Equity stick: “Which picture shows gentle hands? Point.”'],
 ['4 · Turn and Talk (R3, R4)','Model knee to knee. “Look at Nadege. Tell your partner: She feels ___.” 30 seconds, then ring back.','Partners face each other and take turns; most say or point to “sad.”','Equity stick: two shares. Praise the full sentence.'],
 ['5 · Watch Me, Then Show Me (R3, R4, R5)','Read: “A friend takes my truck. I feel mad. I can…” A student models a mad face, then a calm move. Ask the class, “What did they do?” Then everyone rehearses deep breaths and “Can I have a turn?”','A student models; class names the calm move; whole class rehearses.','LiveSchool point for the student model. Name the calm move out loud.'],
 ['6 · My Promise Today (R2, R5)','Hand on heart. “Say it with me: I use gentle hands.” Then: “Point to the calm move you will use today.”','Every student says the promise and points to one choice.','Equity stick: three names. Pointing counts.'],
 ['7 · How We Leave (R1, R4, R5)','“Stand up. Gentle hands. Walk. Ready to learn.” Do not time this at K–2.','Hands to self while moving; calm walking.','LiveSchool point for the table that walks with gentle hands the whole way.'],
];
const doc=new Document({
 creator:'Matchbook Learning',title:'Gentle Hands with Friends · Teacher Guide',
 styles:{default:{document:{run:{font:'Calibri',size:22}}}},
 numbering:{config:[{reference:'bul',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:260}}}},{level:1,format:LevelFormat.BULLET,text:'–',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:260}}}}]},
   {reference:'num',levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:300}}}}]}]},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1000,bottom:1000,left:1080,right:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[t('Matchbook Learning · K–2 Behavior Toolkit · Gentle Hands with Friends · Teacher Guide · page ',{size:16,color:GRY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GRY,font:'Calibri'})]}),new Paragraph({alignment:AlignmentType.RIGHT,children:[t('Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.',{size:14,color:GRY})]})]})},
  children:[
   new Paragraph({children:[new TextRun({text:'K–2 BEHAVIOR TOOLKIT · MORNING MEETING',font:'Calibri',size:18,bold:true,color:GRY})],spacing:{after:40}}),
   new Paragraph({children:[new TextRun({text:'Gentle Hands with Friends',font:'Calibri',size:52,bold:true,color:RED})],spacing:{after:40}}),
   new Paragraph({children:[t('Teacher Guide · Topic 7 of 12 · Value: Safe',{size:24,bold:true,color:CHAR})],spacing:{after:160}}),
   new Paragraph({children:[new ImageRun({type:'jpg',data:IMG('high_five'),transformation:{width:170,height:170}}),t('   '),new ImageRun({type:'jpg',data:IMG('malik_fists'),transformation:{width:300,height:168}})],spacing:{after:160}}),
   table([2400,W-2400],[
     ['At a glance',''],
     ['Goal','Students say “Hitting hurts. We use gentle hands” and choose a calm move when they feel mad.'],
     ['Time','15 minutes in Morning Meeting, in place of the general lesson. Centers run during the week.'],
     ['When','Teach before trouble. If a child in this room was hit today, wait a day.'],
     ['In the bundle','Student deck (7 slides, press N for notes) · Poster (letter and 11×17) · Center kit (sort, sequence, act it out, desk strips, coloring) · Mini book · Family half-sheet'],
     ['Words we use','“Hitting hurts. We use gentle hands.” · “When I feel mad, I can…” · “Can I have a turn?”'],
   ]),
   h1('Before you teach'),
   b('Hang the poster at child height near the calm corner. Students point to it all week.'),
   b('The story uses Malik and Nadege, the toolkit’s classmates. Never cast a real student as the child who hits.'),
   b('Tape a desk strip at the table of any student who needs the calm choices close by.'),
   b('Pair students who need support with a steady turn-and-talk partner before the lesson starts.'),
   h1('The lesson, slide by slide'),
   small('The same script is in the deck’s presenter notes. Press N while presenting.'),
   table([2300,4300,1900,W-8500],[['Slide','Say and do','Look for','Engagement move'],...slides.map(s=>[s[0],s[1],s[2],s[3]])]),
   h2('Practice bridges for slide 5'),
   small('Students model, not the teacher. The teacher narrates and asks the class what they saw.'),
   table([2300,W-2300],[['If the model is…','Say'],
     ['Excellent','“Show the class again. Everyone, what calm move did you see?” Then the whole class does it together.'],
     ['Partly right','“You showed the mad face. Now show us the calm move. Try again.”'],
     ['Silly','“Thank you. Let’s see it the safe way.” Call a new student. No commentary.']]),
   new Paragraph({children:[new PageBreak()]}),
   h1('Centers'),
   small('Print one kit per group. Laminate the mats and cards so they last. Students work in groups of 2 to 4.'),
   table([1900,3000,3200,W-8100],[['Center','Set up','Read to students','Done looks like'],
     ['Sort It','Sort mat (landscape page) and 8 cut picture cards.','“Look at each picture. Is it gentle hands or not gentle? Put it on the side where it goes.”','5 cards on Gentle, 3 on Not gentle.'],
     ['Put It in Order','Sequencing mat and 4 cut cards.','“Put the pictures in order: first, next, then, last. Tell your partner the story.”','Students retell: mad, calm corner, back to the rug, play.'],
     ['Act It Out','4 role-play cards in a stack.','“Pick a card. Read it with me. Show a mad face. Then show a calm move from the pictures.”','Each student shows one calm move.'],
     ['Calm Choices','Desk strips, one per student.','“Point to the calm choice you like best. Show me how you do it.”','Each student points and acts out one choice.'],
     ['Color','Coloring page and crayons.','“Color Lee and Tee. In the box, draw a gentle hands move you can do.”','A drawing of a high five, a wave, or a fist bump.']]),
   h2('Answer keys'),
   b([t('Sort, Gentle hands: ',{bold:true}),t('Lee and Tee high five · friends building with blocks · Tee and Malik tossing a ball · Tee and Nadege doing a puzzle · Tee handing Kiara a block.')]),
   b([t('Sort, Not gentle: ',{bold:true}),t('Malik with tight fists over the truck · Nadege about to throw a block · Diego with fists at the teacher.')]),
   b([t('Put It in Order: ',{bold:true}),t('1 Tee walks to the calm corner, mad · 2 Tee calms down in the corner · 3 Tee walks back to the rug · 4 friends play together.')]),
   h1('The mini book (one child, Tier 2)'),
   b('For a child who has hit more than once. Read it one-on-one, at a calm time, before the hardest part of the day.'),
   b('Read it every day for a week. Let the child turn the pages and point to the calm choices.'),
   b('Never read it as a consequence or right after an incident.'),
   b('On the back, the child colors a star each day they use gentle hands. Celebrate every star.'),
   new Paragraph({children:[new PageBreak()]}),
   h1('When it happens'),
   small('Follows the Responsive Behavior Plan: the adult response is the intervention. Fewer words as escalation rises.'),
   n([t('Safety first. ',{bold:true}),t('Calmly step between. Care for the hurt child first: “Are you okay? Let’s get you help.”')]),
   n([t('Few words. ',{bold:true}),t('To the child who hit: “Hands down. Come with me.” Offer a break: break, reset, return. If hitting continues or anyone is in danger, call for support.')]),
   n([t('Address, once calm. ',{bold:true}),t('Point to the poster. “Hitting hurts. Next time, pick a calm choice.” Correct the routine, not the child.')]),
   n([t('Document. ',{bold:true}),t('Fill out the Live Card right away: facts only, in bullet points.')]),
   n([t('Repair, after regulation. ',{bold:true}),t('“I can see you were mad. Who got hurt? What can we do to help?” K–2 repair can be checking on the friend, helping rebuild, or drawing a picture. Never force an apology.')]),
   n([t('Reflect. ',{bold:true}),t('If it happens again, share the Live Cards with your coach and the counseling team.')]),
   small('If a student hits an adult, use Topic 8, Gentle Hands with Grown-Ups, and the same pathway.'),
   h1('Family connection'),
   b('Send the family half-sheet home the day you teach. It is in English, Spanish, and Haitian Creole.'),
  ]}]
});
Packer.toBuffer(doc).then(buf=>{fs.writeFileSync('/home/claude/k2/out/Gentle-Hands_Teacher-Guide.docx',buf);console.log('ok')});
