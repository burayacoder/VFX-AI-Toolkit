// node ss.js "<query>" <outjson>  -> StockSnap'in kendi (cdn.stocksnap.io) küçük resimlerini listeler (sponsorlu Shutterstock hariç)
const {chromium}=require('playwright');const fs=require('fs');
const [q,out]=process.argv.slice(2);
(async()=>{
  const b=await chromium.launch({args:['--disable-blink-features=AutomationControlled']});
  const ctx=await b.newContext({viewport:{width:1600,height:1000},userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'});
  const p=await ctx.newPage();
  try{await p.goto('https://stocksnap.io/search/'+encodeURIComponent(q),{waitUntil:'domcontentloaded',timeout:45000});}catch(e){}
  await p.waitForTimeout(3500);
  for(let i=0;i<4;i++){await p.mouse.wheel(0,1400);await p.waitForTimeout(900);}
  const imgs=await p.evaluate(()=>[...document.querySelectorAll('a')].map(a=>{const i=a.querySelector('img');return i?{href:a.href,src:i.currentSrc||i.src,alt:i.alt}:null}).filter(x=>x&&x.src.includes('cdn.stocksnap.io/img-thumbs/')&&x.href.includes('/photo/')));
  const seen=new Set();const uniq=imgs.filter(x=>{if(seen.has(x.href))return false;seen.add(x.href);return true;});
  fs.writeFileSync(out,JSON.stringify({q,n:uniq.length,imgs:uniq},null,1));
  console.log(q,'->',uniq.length);
  await b.close();
})();
