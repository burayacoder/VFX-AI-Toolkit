// node shoot2.js jobs.json  -> jobs: [{html, out, w, h, dsf, wait, transparent}]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const b=await chromium.launch();
for(const j of jobs){
  const ctx=await b.newContext({viewport:{width:j.w||1920,height:j.h||1080},deviceScaleFactor:j.dsf||1});
  const p=await ctx.newPage();
  await p.goto('file://'+j.html);
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(j.wait||250);
  await p.screenshot({path:j.out,omitBackground:!!j.transparent});
  await ctx.close();
}
await b.close();})();
