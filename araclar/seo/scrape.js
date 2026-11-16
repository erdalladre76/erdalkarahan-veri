const {chromium}=require('playwright');const fs=require('fs');
const src=fs.readFileSync('dist/index.html','utf8');
const re=/\{g:'([^']+)',key:'([a-z0-9]+)',title:'((?:[^'\\]|\\.)*)',abbr:'[^']*',(lead|fields|body)(?::'((?:[^'\\]|\\.)*)')?/g;let m;const T=[];
while((m=re.exec(src))){T.push({g:m[1],key:m[2],title:m[3].replace(/\\'/g,"'"),type:m[4]==='lead'?'h':'d',lead:(m[5]||'').replace(/\\'/g,"'")});}
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:900}});await p.goto('http://localhost:8765/');await p.waitForTimeout(2500);
for(const t of T){await p.evaluate(h=>{location.hash=h},'#'+t.type+'-'+t.key);await p.waitForTimeout(450);
 const r=await p.evaluate(()=>{const vis=x=>x&&x.offsetParent;const labs=[...new Set([...document.querySelectorAll('section[data-view] label')].filter(vis).map(x=>x.innerText.replace(/\s+/g,' ').trim()).filter(x=>x.length>2&&x.length<140))];
  const res=[...document.querySelectorAll('.result')].filter(vis).map(x=>x.innerText).join('\n').split('\n').map(x=>x.trim()).filter(Boolean);
  const notes=[...document.querySelectorAll('.result ~ *, .res-note, .tnote, .note, .dtip, .tip')].filter(vis).map(x=>x.innerText.trim()).filter(x=>x.length>60&&x.length<6000);
  const h3=[...document.querySelectorAll('section[data-view] h3')].filter(vis).map(x=>x.innerText.trim())[0]||'';return {labs,res,notes:[...new Set(notes)],h3};});
 Object.assign(t,r);}
const V=['gecbeyan','duzeltme','sirket','apartman','amackonu','ortaklik','ozluk','arackdv','dvbeyan','kirasozlesme','takvim','pratik','beyanname','belgeler','programlar','kurumlar','hesaplamalar','dilekceler','tablolar','yazilar'];const views=[];
for(const v of V){await p.evaluate(h=>{location.hash=h},'#'+v);await p.waitForTimeout(500);
 const r=await p.evaluate(v=>{const s=[...document.querySelectorAll('section[data-view]')].filter(x=>x.offsetParent&&(x.dataset.view||'').split(' ').includes(v))[0];if(!s)return null;const h=(s.querySelector('h1,h2')||{}).innerText||'';const ps=[...s.querySelectorAll('p')].filter(x=>x.offsetParent).map(x=>x.innerText.replace(/\s+/g,' ').trim()).filter(x=>x.length>70).slice(0,6);const hs=[...s.querySelectorAll('h3,h4')].filter(x=>x.offsetParent).map(x=>x.innerText.replace(/\s+/g,' ').trim()).filter(x=>x.length>3&&x.length<110).slice(0,40);return {h,ps,hs:[...new Set(hs)],title:document.title};},v);
 if(r)views.push(Object.assign({view:v},r));}
fs.writeFileSync('seo/data.json',JSON.stringify({T,views}));console.log(T.length,views.length,T.filter(t=>t.type==='h'&&!t.res.length).map(t=>t.key).join(','),'| nolabs:',T.filter(t=>!t.labs.length).map(t=>t.key).join(','));
const k=T.find(t=>t.key==='kidem');console.log(JSON.stringify(k).slice(0,1800));console.log(JSON.stringify(views[0]).slice(0,900));await b.close();})();
