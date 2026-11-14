// node browse.js <url> <outprefix> [scrolls] [waitMs]  -> <outprefix>.png (viewport+scroll shots), <outprefix>.json (title, img urls)
const {chromium}=require('playwright');const fs=require('fs');
const [url,out,scrolls='2',waitMs='3500']=process.argv.slice(2);
(async()=>{
  const b=await chromium.launch({args:['--disable-blink-features=AutomationControlled']});
  const ctx=await b.newContext({viewport:{width:1600,height:1000},locale:'tr-TR',
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'});
  const p=await ctx.newPage();
  let status='';
  try{const r=await p.goto(url,{waitUntil:'domcontentloaded',timeout:45000});status=r?r.status():'';}catch(e){status='ERR '+e.message.slice(0,80);}
  await p.waitForTimeout(+waitMs);
  for(let i=0;i<+scrolls;i++){await p.mouse.wheel(0,900);await p.waitForTimeout(1200);}
  await p.evaluate(()=>window.scrollTo(0,0));
  await p.screenshot({path:out+'.png'});
  const info=await p.evaluate(()=>({title:document.title,
    imgs:[...document.images].map(i=>({s:i.currentSrc||i.src,w:i.naturalWidth,h:i.naturalHeight,a:i.alt})).filter(i=>i.s&&i.w>150).slice(0,120)}));
  info.status=status;info.url=p.url();
  fs.writeFileSync(out+'.json',JSON.stringify(info,null,1));
  console.log(status,info.title,'| img:',info.imgs.length);
  await b.close();
})();
