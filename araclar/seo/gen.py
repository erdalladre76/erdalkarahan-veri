import json,re,os,html,shutil,datetime,sys
D=os.path.dirname(os.path.abspath(__file__));OUT=os.path.join(D,'out');B='https://www.erdalkarahan.com'
data=json.load(open(os.path.join(D,'data.json'),encoding='utf-8'));Y=json.load(open('/home/claude/erdalkarahan-veri/yazilar.json',encoding='utf-8'))['yazilar']
TODAY=datetime.date.today().isoformat()
def e(x):return html.escape(str(x or ''),quote=True)
TR=str.maketrans('çğıöşüÇĞİÖŞÜâîûÂÎÛ’','cgiosuCGIOSUaiuAIU ')
def slug(t):
    t=t.translate(TR).lower();t=re.sub(r'[^a-z0-9]+','-',t).strip('-');return t[:80].strip('-')
def cap(t):
    def w(m):
        s=m.group(0);c=s[0];c='İ' if c=='i' else 'I' if c=='ı' else c.upper();return c+s[1:]
    return re.sub(r"(?<![\w’'])[a-zçğıöşü][\wçğıöşü]*",w,t)
CSS=""":root{--bg:#f6f4fb;--card:#fff;--ink:#141a33;--mut:#5a607a;--rule:#dcd8ea;--ac:#5B3FA8;--ac2:#eee9fb}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1226;--card:#171b36;--ink:#eef0fa;--mut:#a8aecb;--rule:#2b3157;--ac:#a58bf0;--ac2:#231f45}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--ac)}header.t{background:#141a33;color:#fff}header.t .w{display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px;padding:14px 16px}
header.t a{color:#fff;text-decoration:none;font-weight:700}header.t nav{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:14px}header.t nav a{font-weight:600;opacity:.85}
.w{max-width:860px;margin:0 auto;padding:0 16px}.bc{font-size:13px;color:var(--mut);margin:18px 0 6px}.bc a{color:var(--mut)}
h1{font-size:clamp(24px,5vw,34px);line-height:1.2;margin:6px 0 12px;text-wrap:balance}h2{font-size:20px;margin:26px 0 8px}
.lead{font-size:18px;color:var(--mut);margin:0 0 16px}.card{background:var(--card);border:1px solid var(--rule);border-radius:16px;padding:18px;margin:16px 0}
.cta{display:inline-block;background:var(--ac);color:#fff!important;text-decoration:none;font-weight:800;border-radius:999px;padding:13px 22px;margin:6px 0}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .cta{color:#141a33!important}}
table{border-collapse:collapse;width:100%;font-size:15px}td{border-top:1px solid var(--rule);padding:8px 6px;vertical-align:top}td:last-child{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
ul{padding-left:20px}li{margin:4px 0}.tags{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}.tags span{font-size:12px;background:var(--ac2);border-radius:999px;padding:3px 10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;padding:0;list-style:none}.grid a{display:block;background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:10px 12px;text-decoration:none;font-weight:600;font-size:15px}
footer{margin:36px 0 0;border-top:1px solid var(--rule);padding:18px 0 30px;font-size:13px;color:var(--mut)}.kay{font-size:13px;word-break:break-word}.sm{font-size:13px;color:var(--mut)}"""
def page(path,title,desc,h1,body,crumb,key,ld=None):
    url=B+'/'+path
    j={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':B+'/'+u} for i,(n,u) in enumerate([('Ana Sayfa','')]+crumb+[(h1,path)])]}
    lds='<script type="application/ld+json">'+json.dumps(j,ensure_ascii=False)+'</script>'+(('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>') if ld else '')
    bc=' › '.join(['<a href="/">Ana Sayfa</a>']+['<a href="/%s">%s</a>'%(u,e(n)) for n,u in crumb])
    h='''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="article"><meta property="og:url" content="%s"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="SMMM Erdal Karahan"><link rel="icon" href="/favicon.ico"><style>%s</style>%s</head><body><header class="t"><div class="w"><a href="/">Erdal Karahan · SMMM</a><nav><a href="/hesaplama/">Hesaplamalar</a><a href="/dilekce/">Dilekçeler</a><a href="/yazi/">Yazılar</a><a href="/rehber/">Rehberler</a></nav></div></header><main class="w"><p class="bc">%s</p><h1>%s</h1>%s</main><footer><div class="w">SMMM Erdal Karahan · Kadıköy / İstanbul · Bu sayfa genel bilgilendirme amaçlıdır. · <a href="/site-haritasi.html">Site Haritası</a></div></footer><script>(function(){try{if(navigator.webdriver||localStorage.getItem("ek-ben")==="1")return;var r="";try{var h=document.referrer?new URL(document.referrer).hostname:"";if(h&&h!==location.hostname)r=h.replace(/^www\\./,"");}catch(e){}var s=sessionStorage.getItem("ek-hit");if(!s){sessionStorage.setItem("ek-hit","1");fetch("/sayac.php?hit=1",{cache:"no-store",keepalive:true});}fetch("/sayac.php?p=%s"+(r?"&r="+encodeURIComponent(r):""),{cache:"no-store",keepalive:true});}catch(e){}})();</script></body></html>'''%(e(title),e(desc),url,e(title),e(desc),url,CSS,lds,bc,e(h1),body,key)
    f=os.path.join(OUT,path if not path.endswith('/') and path else path+'index.html');os.makedirs(os.path.dirname(f),exist_ok=True);open(f,'w',encoding='utf-8').write(h);URLS.append(url)
URLS=[];shutil.rmtree(OUT,ignore_errors=True)
def trunc(t,n=155):
    t=re.sub(r'\s+',' ',t).strip();return t if len(t)<=n else t[:n-1].rsplit(' ',1)[0]+'…'
def resrows(res):
    L=res[:];
    for k in ('Detaylı','Hesaplama Sonucu'):
        if k in L:L=L[L.index(k)+1:];break
    for k in ('＋','Firma ve Çalışan Bilgisi Ekle','Sonucu Kopyala'):
        if k in L:L=L[:L.index(k)]
    rows=[];notes=[];i=0
    while i<len(L):
        a=L[i]
        if len(a)>95:notes.append(a);i+=1;continue
        if i+1<len(L) and len(L[i+1])<=160 and not a.endswith('.'):rows.append((a,L[i+1]));i+=2
        else:notes.append(a);i+=1
    return rows[:24],[n for n in notes if len(n)>40][:8]
H=[];Dl=[];_seen=set()
for t in data['T']:
    if (t['type'],t['key']) in _seen:continue
    _seen.add((t['type'],t['key']))
    ttl=cap(t['title']);labs=[cap(x.replace('I','ı').replace('İ','i').lower()) if x.isupper() else x for x in t['labs']]
    labs=[x for x in labs if not re.match(r'^(Hane|Özet|Detaylı)$',x)]
    if t['type']=='h':
        sl=slug(t['title']);sl=sl if 'hesap' in sl else sl+'-hesaplama';path='hesaplama/%s.html'%sl
        rows,notes=resrows(t['res'])
        body='<p class="lead">%s</p><a class="cta" href="/#h-%s">Hesaplamayı Aç →</a>'%(e(t['lead']),t['key'])
        if labs:body+='<h2>Hangi Bilgiler Giriliyor?</h2><ul>'+''.join('<li>%s</li>'%e(x) for x in labs[:22])+'</ul>'
        if rows:body+='<h2>Örnek Sonuç</h2><p class="sm">Araç açıldığında gelen örnek değerlerle hesaplanmıştır; kendi rakamlarınızı girince sonuç değişir.</p><div class="card"><table>'+''.join('<tr><td>%s</td><td>%s</td></tr>'%(e(a),e(b)) for a,b in rows)+'</table></div>'
        if notes:body+='<h2>Hesap Nasıl Yapılıyor?</h2>'+''.join('<p>%s</p>'%e(n) for n in notes)
        body+='<p><a class="cta" href="/#h-%s">%s: Hesaplamayı Aç →</a></p><p class="sm">Hesaplama ücretsizdir, üyelik istemez; girdiğiniz bilgiler yalnızca kendi tarayıcınızda kalır.</p>'%(t['key'],e(ttl))
        nm=ttl if re.search('hesap',ttl,re.I) else ttl+' Hesaplama'
        page(path,trunc(nm+' (2026) | Erdal Karahan SMMM',70),trunc(t['lead'] or ttl),nm,body,[('Hesaplamalar','hesaplama/')],'s-h-'+t['key'],{'@context':'https://schema.org','@type':'WebApplication','name':nm,'url':B+'/'+path,'applicationCategory':'FinanceApplication','operatingSystem':'Web','inLanguage':'tr','offers':{'@type':'Offer','price':'0','priceCurrency':'TRY'},'description':t['lead']})
        H.append((t['g'],nm,path))
    else:
        sl=slug(t['title']);sl=sl if 'dilekce' in sl else sl+'-dilekce-ornegi';path='dilekce/%s.html'%sl
        if B+'/'+path in URLS:path='dilekce/%s-%s.html'%(sl,t['key'])
        nm=ttl if re.search('dilekçe|sözleşme|tutanak|beyan|yazı|form|karar|ibraname|bordro|makbuz|senet|protokol|belge|bildirim|ihtar|vekâlet|taahhüt|mutabakat',ttl,re.I) else ttl+' Dilekçesi'
        ds='%s: bilgilerinizi yazın, hazır metni yazdırın ya da Word ve PDF olarak indirin. Ücretsiz, üyelik gerekmez.'%nm
        body='<p class="lead">%s</p><a class="cta" href="/#d-%s">Belgeyi Doldur →</a>'%(e('Doldurulabilir örnek: bilgilerinizi yazın, hazır metni yazdırın ya da Word ve PDF olarak indirin.'),t['key'])
        if labs:body+='<h2>Hangi Bilgiler İsteniyor?</h2><ul>'+''.join('<li>%s</li>'%e(x) for x in labs[:24])+'</ul>'
        for n in t['notes'][:3]:body+='<p>%s</p>'%e(n)
        body+='<p class="sm">Örnek metin genel bilgilendirme amaçlıdır; kendi durumunuza göre gözden geçirin. Girdiğiniz bilgiler yalnızca kendi tarayıcınızda kalır.</p>'
        page(path,trunc(nm+' (Word, PDF) | Erdal Karahan SMMM',70),trunc(ds),nm,body,[('Dilekçeler','dilekce/')],'s-d-'+t['key'])
        Dl.append((t['g'],nm,path))
AY=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
YZ=[]
for y in Y:
    path='yazi/%s.html'%y['slug'][:90];b='<p class="lead">%s</p>'%e(y.get('ozet'))
    try:d=datetime.date.fromisoformat(y['tarih'][:10]);b+='<p class="sm">Erdal Karahan · %d %s %d</p>'%(d.day,AY[d.month-1],d.year)
    except Exception:d=None
    if y.get('etiketler'):b+='<div class="tags">'+''.join('<span>%s</span>'%e(x) for x in y['etiketler'])+'</div>'
    for s in y.get('bolumler',[]):
        if s.get('baslik'):b+='<h2>%s</h2>'%e(cap(s['baslik']))
        for p in s.get('paragraflar',[]) or []:b+='<p>%s</p>'%e(p)
        if s.get('liste'):b+='<ul>'+''.join('<li>%s</li>'%e(x) for x in s['liste'])+'</ul>'
        k=s.get('kayit')
        if k:
            try:
                rows=k if isinstance(k,list) else k.get('satirlar',[])
                b+='<div class="card"><table>'+''.join('<tr>'+''.join('<td>%s</td>'%e(c) for c in (r if isinstance(r,list) else r.values()))+'</tr>' for r in rows)+'</table></div>'
            except Exception:pass
    if y.get('kaynaklar'):b+='<h2>Kaynaklar</h2><ul class="kay">'+''.join('<li><a href="%s" rel="nofollow noopener">%s</a></li>'%(e(u),e(u)) if str(u).startswith('http') else '<li>%s</li>'%e(u) for u in y['kaynaklar'])+'</ul>'
    b+='<p><a class="cta" href="/#yz-%s">Yazıyı Sitede Aç →</a></p>'%e(y['slug'])
    ld={'@context':'https://schema.org','@type':'Article','headline':y['baslik'][:110],'description':y.get('ozet',''),'inLanguage':'tr','author':{'@type':'Person','name':'Erdal Karahan'},'publisher':{'@type':'Person','name':'Erdal Karahan'},'mainEntityOfPage':B+'/'+path}
    if d:ld['datePublished']=d.isoformat()
    page(path,trunc(y['baslik']+' | Erdal Karahan',70),trunc(y.get('ozet') or y['baslik']),cap(y['baslik']),b,[('Yazılar','yazi/')],'s-yz-'+re.sub(r'[^a-z0-9-]','',y['slug'])[:60],ld)
    YZ.append((cap(y['baslik']),path,y.get('tarih','')))
RH=[]
for v in data['views']:
    if v['view'] in ('hesaplamalar','dilekceler','yazilar') or not v['h']:continue
    nm=cap(v['h'].rstrip('.'));path='rehber/%s.html'%slug(v['h'])
    b=''.join('<p%s>%s</p>'%(' class="lead"' if i==0 else '',e(p)) for i,p in enumerate(v['ps'][:4]))+'<a class="cta" href="/#%s">Sayfayı Aç →</a>'%v['view']
    if v['hs']:b+='<h2>Bu Sayfada Neler Var?</h2><ul>'+''.join('<li>%s</li>'%e(cap(x.replace('I','ı').replace('İ','i').lower()) if x.isupper() else x) for x in v['hs'][:30])+'</ul>'
    page(path,trunc(nm+' | Erdal Karahan SMMM',70),trunc(v['ps'][0] if v['ps'] else nm),nm,b,[('Rehberler','rehber/')],'s-'+v['view']);RH.append((nm,path))
def hub(path,h1,desc,items,grouped=False):
    b='<p class="lead">%s</p>'%e(desc)
    if grouped:
        gs=[]
        for g,_,_ in items:
            if g not in gs:gs.append(g)
        for g in gs:b+='<h2>%s</h2><ul class="grid">'%e(cap(g))+''.join('<li><a href="/%s">%s</a></li>'%(p,e(n)) for gg,n,p in items if gg==g)+'</ul>'
    else:b+='<ul class="grid">'+''.join('<li><a href="/%s">%s</a></li>'%(x[1],e(x[0])) for x in items)+'</ul>'
    page(path,trunc(h1+' | Erdal Karahan SMMM',70),trunc(desc),h1,b,[],'s-hub-'+path.strip('/'))
hub('hesaplama/','Ücretsiz Hesaplama Araçları (2026)','Maaş, kıdem ve ihbar tazminatı, vergi, SGK, KDV, kira, kredi ve ticari hesaplamalar: 2026 oranlarıyla, muhasebe kaydıyla birlikte, üyeliksiz.',H,True)
hub('dilekce/','Doldurulabilir Dilekçe Ve Belge Örnekleri','Vergi dairesi, SGK, ticaret sicili, personel ve icra işleri için dilekçe, tutanak ve sözleşme örnekleri: doldurun, yazdırın, Word ya da PDF indirin.',Dl,True)
hub('yazi/','Vergi Ve Muhasebe Yazıları','Güncel vergi, SGK ve muhasebe konularında örnek kayıtlarla anlatılan yazılar.',sorted(YZ,key=lambda x:x[2],reverse=True))
hub('rehber/','Rehberler Ve Sihirbazlar','Şirket işlemleri, beyanname, düzeltme, apartman yönetimi ve diğer konularda adım adım rehberler.',RH)
b=''
for t,items in (('Hesaplamalar',[(n,p) for _,n,p in H]),('Dilekçeler',[(n,p) for _,n,p in Dl]),('Yazılar',[(a,p) for a,p,_ in YZ]),('Rehberler',RH)):
    b+='<h2>%s</h2><ul class="grid">'%t+''.join('<li><a href="/%s">%s</a></li>'%(p,e(n)) for n,p in items)+'</ul>'
page('site-haritasi.html','Site Haritası | Erdal Karahan SMMM','erdalkarahan.com üzerindeki bütün hesaplama araçları, dilekçe örnekleri, yazılar ve rehberler.','Site Haritası',b,[],'s-harita')
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>%s/</loc><lastmod>%s</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>\n'%(B,TODAY)+''.join('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>%s</priority></url>\n'%(u,TODAY,'0.6' if u.endswith('/') or 'site-haritasi' in u else '0.8') for u in URLS)+'</urlset>\n'
open(os.path.join(OUT,'sitemap.xml'),'w',encoding='utf-8').write(sm)
from collections import Counter
assert not [u for u,c in Counter(URLS).items() if c>1]
print(len(URLS),'sayfa',len(H),len(Dl),len(YZ),len(RH))
