# -*- coding: utf-8 -*-
import json,sys
G={}
for f in ['ak1.py','ak2.py','ak3.py','ak4.py','ak5.py']:
    exec(open(f,encoding='utf-8').read(),G)
S=G['S'];ids=[x['id'] for x in S];assert len(ids)==len(set(ids)),'dup'
cats=[k for k,_ in G['KATEGORILER']]
for x in S: assert x['k'] in cats,x['id']
out={"guncelleme":"2026-11-08","baslik":"Şirket Amaç ve Konu Maddeleri","giris":G['GIRIS'],"kurallar":G['KURALLAR'],
 "izinli":G['IZINLI'],"kategoriler":G['KATEGORILER'],"sektorler":S,"genel":G['GENEL'],"kapanis":G['KAPANIS']}
json.dump(out,open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False,indent=1)
n=sum(len(x['m']) for x in S);w=sum(len(t.split()) for x in S for t in x['m'])
print('sektör',len(S),'bent',n,'kelime',w,{c:sum(1 for x in S if x['k']==c) for c in cats})
