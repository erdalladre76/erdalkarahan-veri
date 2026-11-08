# Geçici vergi kontrol listesi

Sitenin Excel bölümündeki "Geçici vergi kontrol listesi" bu klasörden üretilir.

- `items2.py`: bölüm ve maddeler
- `gv_oranlar.json`: yıl, dönemler, son günler, yeniden değerleme oranları ve kaynak bağlantıları; `secili` alanı PDF'te gösterilen dönemdir
- `build.py`: Excel'i üretir

Güncelleme:

```
cd araclar/gecici-vergi
python3 build.py ../../dosyalar/gecici-vergi-kontrol-listesi.xlsx gv_oranlar.json
cd ../../dosyalar && soffice --headless --convert-to pdf gecici-vergi-kontrol-listesi.xlsx
```

PDF'ten önce formüllerin hesaplanması için dosya LibreOffice ile bir kez açılıp kaydedilir (`soffice --convert-to xlsx` ya da xlsx skill'indeki recalc.py).
