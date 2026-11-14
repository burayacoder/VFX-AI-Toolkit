// node qa_v8.js (qa2.js kopyası; v8 yazı tipi) <deckdir> <outdir> [ids]  — yerel önizleme + sabit konumlu metin denetimi
const {chromium}=require('playwright');const fs=require('fs');
const M=__dirname;
const deck=process.argv[2], outdir=process.argv[3], only=process.argv[4]?process.argv[4].split(','):null;
(async()=>{
  fs.mkdirSync(outdir,{recursive:true});
  const dj=JSON.parse(fs.readFileSync(deck+'/project/deck.json','utf8'));
  const css=fs.readFileSync(deck+'/project/deck.css','utf8');
  const fonts=fs.readFileSync(M+'/fonts/fonts_v8.css','utf8').replace(/url\(fonts\//g,'url(file://'+M+'/fonts/');
  const ids=dj.order.filter(i=>!only||only.includes(i));
  const secs=ids.map(id=>fs.readFileSync(deck+'/project/slides/'+id+'.html','utf8')).join('\n');
  const viewer=`* { margin: 0 } body { font: 32px/1.2 sans-serif }
body > section { width: 1920px !important; height: 1080px !important; overflow: hidden !important; box-sizing: border-box !important; position: relative; isolation: isolate }
section[hidden], aside, noscript { display: none !important }
h1 { font-size: 96px; font-weight: 600 } h2 { font-size: 64px; font-weight: 600 } h3 { font-size: 44px; font-weight: 600 }
p, li, h1, h2, h3, td, th { overflow-wrap: break-word; text-wrap: pretty }
x-shape, x-icon, x-embed { display: block }
.rise,.fadein{animation:none !important}`;
  const html=`<!doctype html><html><head><meta charset="utf-8"><style>${fonts}\n${viewer}\n${css}</style></head><body>${secs}</body></html>`;
  fs.writeFileSync(outdir+'/_page.html',html);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+outdir+'/_page.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(700);
  const rep=await p.evaluate(()=>{
    const out=[];
    document.querySelectorAll('body > section').forEach(sec=>{
      const sr=sec.getBoundingClientRect();
      const items=[];
      sec.querySelectorAll('p,h1,h2,h3,li').forEach(e=>{
        if(e.closest('aside'))return;
        const txt=(e.textContent||'').trim(); if(!txt)return;
        // metin satırlarının gerçek sınırları
        const range=document.createRange(); range.selectNodeContents(e);
        const rs=[...range.getClientRects()].filter(r=>r.width>1&&r.height>1);
        if(!rs.length)return;
        const L=Math.min(...rs.map(r=>r.left))-sr.left, T=Math.min(...rs.map(r=>r.top))-sr.top;
        const R=Math.max(...rs.map(r=>r.right))-sr.left, B=Math.max(...rs.map(r=>r.bottom))-sr.top;
        const box=e.getBoundingClientRect();
        const cs=getComputedStyle(e);
        items.push({el:e,txt:txt.slice(0,34),cls:e.className.replace('pin ','').replace(' rise',''),L,T,R,B,
          hov:e.scrollWidth>e.clientWidth+2, fs:parseFloat(cs.fontSize)});
      });
      const issues=[];
      items.forEach(a=>{
        if(a.hov)issues.push('yatay taşma: '+a.txt);
        if(a.R>1800)issues.push('sağ kenar '+Math.round(a.R)+': '+a.txt);
        if(a.L<120&&a.L>=0)issues.push('sol kenar '+Math.round(a.L)+': '+a.txt);
        if(a.B>1024)issues.push('alt taşma '+Math.round(a.B)+': '+a.txt);
        if(a.fs<24)issues.push('yazı <24px ('+a.fs+'): '+a.txt);
      });
      for(let i=0;i<items.length;i++)for(let j=i+1;j<items.length;j++){
        const a=items[i],b=items[j];
        const ox=Math.min(a.R,b.R)-Math.max(a.L,b.L), oy=Math.min(a.B,b.B)-Math.max(a.T,b.T);
        if(a.cls.includes('t1')&&b.cls.includes('t2'))continue; if(ox>6&&oy>6&&ox*oy>150)issues.push('örtüşme: «'+a.txt+'» × «'+b.txt+'» ('+Math.round(ox)+'×'+Math.round(oy)+')');
      }
      out.push({id:sec.id,n:items.length,issues,imgs:sec.querySelectorAll('img').length,els:sec.querySelectorAll('*').length});
    });
    return out;
  });
  let bad=0;
  for(const r of rep){
    if(r.issues.length)bad++;
    console.log((r.issues.length?'!! ':'ok ')+r.id.padEnd(10)+' metin '+r.n+' img '+r.imgs+' öğe '+r.els);
    r.issues.forEach(s=>console.log('     - '+s));
  }
  console.log('sorunlu slayt:',bad,'/',rep.length);
  const handles=await p.$$('body > section');
  for(let i=0;i<handles.length;i++){await handles[i].screenshot({path:`${outdir}/${ids[i]}.png`});}
  await b.close();
})();
