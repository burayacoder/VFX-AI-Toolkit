// node qa5_v8.js <qa_klasörü>  -> <qa>/olcum.json : başlık konumu, metin kutuları, renk, boyut, arka plan örneği, görseller
// qa_v8.js'in yazdığı _page.html ve slayt ekran görüntülerini kullanır.
const {chromium}=require('playwright');const fs=require('fs');
const qa=process.argv[2];
(async()=>{
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+qa+'/_page.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
  const data=await p.evaluate(()=>{
    const hex=c=>{const m=c.match(/\d+(\.\d+)?/g);return m?'#'+m.slice(0,3).map(v=>(+v).toString(16).padStart(2,'0')).join('').toUpperCase():c};
    return [...document.querySelectorAll('body > section')].map(sec=>{
      const sr=sec.getBoundingClientRect();
      const texts=[...sec.querySelectorAll('h1,h2,h3,p')].filter(e=>!e.closest('aside')&&(e.textContent||'').trim()).map(e=>{
        const r=document.createRange();r.selectNodeContents(e);const rs=[...r.getClientRects()].filter(x=>x.width>1&&x.height>1);
        const L=Math.min(...rs.map(x=>x.left))-sr.left,T=Math.min(...rs.map(x=>x.top))-sr.top,R=Math.max(...rs.map(x=>x.right))-sr.left,B=Math.max(...rs.map(x=>x.bottom))-sr.top;
        const cs=getComputedStyle(e);
        let pb=null;for(let a=e.parentElement;a&&a!==sec;a=a.parentElement){const bc=getComputedStyle(a).backgroundColor;if(bc&&!/rgba\(0, 0, 0, 0\)|transparent/.test(bc)){pb=hex(bc);break;}}
        return {pbg:pb,tag:e.tagName.toLowerCase(),cls:e.className,txt:e.innerText.replace(/\n/g,' ').trim(),fs:parseFloat(cs.fontSize),fw:cs.fontWeight,color:hex(cs.color),
          spans:[...e.querySelectorAll('span')].map(s=>hex(getComputedStyle(s).color)),L,T,R,B,boxTop:e.getBoundingClientRect().top-sr.top};
      });
      const imgs=[...sec.querySelectorAll('img')].map(i=>{const r=i.getBoundingClientRect();return {src:i.getAttribute('src').split('/').pop(),alt:i.alt,L:r.left-sr.left,T:r.top-sr.top,R:r.right-sr.left,B:r.bottom-sr.top}});
      return {id:sec.id,cls:sec.className,bg:hex(getComputedStyle(sec).backgroundColor),notes:(sec.querySelector('aside')||{}).textContent||'',texts,imgs};
    });
  });
  fs.writeFileSync(qa+'/olcum.json',JSON.stringify(data,null,1));
  console.log('olcum.json:',data.length,'slayt');
  await b.close();
})();
