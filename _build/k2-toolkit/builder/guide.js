const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,AlignmentType,
  ImageRun,HeadingLevel,LevelFormat,BorderStyle,PageBreak,Footer,Header,PageNumber,TableLayoutType}=require('docx');
const RED='E21C24',CHAR='232323',YEL='F9DC7C',GRN='1F8A4C',GRY='666666';
const G=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const IMG=n=>fs.readFileSync(G.img_dir+'/'+n+'.jpg');
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

const doc=new Document({
 creator:'Matchbook Learning',title:G.title+' · Teacher Guide',
 styles:{default:{document:{run:{font:'Calibri',size:22}}}},
 numbering:{config:[{reference:'bul',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:260}}}},{level:1,format:LevelFormat.BULLET,text:'–',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:260}}}}]},
   {reference:'num',levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:300}}}}]}]},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1000,bottom:1000,left:1080,right:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[t('Matchbook Learning · K–2 Behavior Toolkit · '+G.title+' · Teacher Guide · page ',{size:16,color:GRY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GRY,font:'Calibri'})]}),new Paragraph({alignment:AlignmentType.RIGHT,children:[t(G.credit,{size:14,color:GRY})]})]})},
  children:[
   new Paragraph({children:[new TextRun({text:'K–2 BEHAVIOR TOOLKIT · MORNING MEETING',font:'Calibri',size:18,bold:true,color:GRY})],spacing:{after:40}}),
   new Paragraph({children:[new TextRun({text:G.title,font:'Calibri',size:52,bold:true,color:RED})],spacing:{after:40}}),
   new Paragraph({children:[t('Teacher Guide · Topic '+G.num+' of 12 · Value: '+G.value,{size:24,bold:true,color:CHAR})],spacing:{after:160}}),
   new Paragraph({children:G.images.flatMap((im,i)=>{const r=new ImageRun({type:'jpg',data:IMG(im[0]),transformation:{width:im[1],height:im[2]}});return i?[t('   '),r]:[r]}),spacing:{after:160}}),
   table([2400,W-2400],[['At a glance',''],...G.glance]),
   h1('Before you teach'),
   ...G.before.map(x=>b(x)),
   h1('The lesson, slide by slide'),
   small('The same script is in the deck’s presenter notes. Press N while presenting.'),
   table([2300,4300,1900,W-8500],[['Slide','Say and do','Look for','Engagement move'],...G.slides]),
   h2('Practice bridges for slide 5'),
   small('Students model, not the teacher. The teacher narrates and asks the class what they saw.'),
   table([2300,W-2300],[['If the model is…','Say'],...G.bridges]),
   new Paragraph({children:[new PageBreak()]}),
   h1('Centers'),
   small('Print one kit per group. Laminate the mats and cards so they last. Students work in groups of 2 to 4.'),
   table([1900,3000,3200,W-8100],[['Center','Set up','Read to students','Done looks like'],...G.centers]),
   h2('Answer keys'),
   ...G.keys.map(k=>b([t(k[0],{bold:true}),t(k[1])])),
   h1('The mini book (one child, Tier 2)'),
   ...G.minibook.map(x=>b(x)),
   new Paragraph({children:[new PageBreak()]}),
   h1(G.when_title),
   small(G.when_intro),
   ...G.when.map(w=>n([t(w[0],{bold:true}),t(w[1])])),
   ...(G.when_outro?[small(G.when_outro)]:[]),
   h1('Family connection'),
   b('Send the family half-sheet home the day you teach. It is in English, Spanish, and Haitian Creole.'),
  ]}]
});
Packer.toBuffer(doc).then(buf=>{fs.writeFileSync(process.argv[3],buf);console.log('ok')});
