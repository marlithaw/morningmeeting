// Teacher guide (.docx) for one topic.  node guide.js <guide.json> <out.docx>
// The JSON is written by guide.py from the topic's `guide` content (see topics/*.py).
const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,AlignmentType,
  ImageRun,HeadingLevel,LevelFormat,BorderStyle,PageBreak,Footer,Header,PageNumber,TableLayoutType}=require('docx');
const G=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const OUT=process.argv[3];
const RED='E21C24',CHAR='232323',YEL='F9DC7C',GRN='1F8A4C',GRY='666666';
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
const small=(s,c=GRY)=>new Paragraph({children:[t(s,{size:18,color:c})],spacing:{after:40},keepNext:true});
const boldLead=([lead,text])=>[t(lead,{bold:true}),t(text)];

// Header pictures: [{path,type,w,h}], separated by a spacer run.
const pics=[];
G.images.forEach((im,i)=>{ if(i) pics.push(t('   '));
  pics.push(new ImageRun({type:im.type,data:fs.readFileSync(im.path),transformation:{width:im.w,height:im.h}})); });

const body=[
   new Paragraph({children:[new TextRun({text:G.eyebrow,font:'Calibri',size:18,bold:true,color:GRY})],spacing:{after:40}}),
   new Paragraph({children:[new TextRun({text:G.full_title,font:'Calibri',size:52,bold:true,color:RED})],spacing:{after:40}}),
   new Paragraph({children:[t(G.subtitle,{size:24,bold:true,color:CHAR})],spacing:{after:160}}),
   new Paragraph({children:pics,spacing:{after:160}}),
   table([2400,W-2400],[['At a glance',''],...G.glance]),
   h1(G.before_title),
   ...G.before.map(x=>b(x)),
   h1(G.lesson_title),
   small(G.lesson_note),
   table([2300,4300,1900,W-8500],[['Slide','Say and do','Look for','Engagement move'],...G.slides]),
   h2(G.bridges_title),
   small(G.bridges_note),
   table([2300,W-2300],[['If the model is…','Say'],...G.bridges]),
   new Paragraph({children:[new PageBreak()]}),
   h1(G.centers_title),
   small(G.centers_note),
   table([1900,3000,3200,W-8100],[['Center','Set up','Read to students','Done looks like'],...G.centers]),
   h2(G.keys_title),
   ...G.keys.map(k=>b(boldLead(k))),
   h1(G.minibook_title),
   ...G.minibook.map(x=>b(x)),
   new Paragraph({children:[new PageBreak()]}),
   h1(G.when_title),
   small(G.when_intro),
   ...G.when.map(k=>n(boldLead(k))),
   ...(G.when_outro?[small(G.when_outro)]:[]),
   h1(G.family_title),
   ...G.family.map(x=>b(x)),
];

const doc=new Document({
 creator:'Matchbook Learning',title:G.doc_title,
 styles:{default:{document:{run:{font:'Calibri',size:22}}}},
 numbering:{config:[{reference:'bul',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:260}}}},{level:1,format:LevelFormat.BULLET,text:'–',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:260}}}}]},
   {reference:'num',levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:360,hanging:300}}}}]}]},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1000,bottom:1000,left:1080,right:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[t(G.footer,{size:16,color:GRY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GRY,font:'Calibri'})]}),new Paragraph({alignment:AlignmentType.RIGHT,children:[t(G.credit,{size:14,color:GRY})]})]})},
  children:body}]
});
Packer.toBuffer(doc).then(buf=>{fs.writeFileSync(OUT,buf);console.log('ok')});
