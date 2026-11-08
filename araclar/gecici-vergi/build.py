import math, sys
sys.path.insert(0, '.')
import json, os
from items2 import S
RJ = json.load(open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gv_oranlar.json'), encoding='utf-8'))
YIL = RJ['yil']; DON = RJ['donemler']; SEC = RJ.get('secili', 1)
def dlabel(d): return f"{YIL} / {d['no']}. dönem ({d['aylar']})"
TO = "'Tarihler ve Oranlar'!"
def TU(x): return x.replace('i','İ').replace('ı','I').upper()
NSEC=len(S); NITEM=sum(len(x[1]) for x in S)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.worksheet.pagebreak import Break, RowBreak

OUT = sys.argv[1] if len(sys.argv) > 1 else 'Gecici_Vergi_Kontrol_Listesi_2026_3_Donem.xlsx'
F = 'Arial'
PUR = '14304F'; PUR2 = '1F4E79'; LAV = 'E8EFF6'; LAV2 = 'F5F8FB'; GOLD = '2A9D8F'; INK = '1B2533'; GRY = '5F6B7A'
BOX_E, BOX_F = '☐', '☑'

def fill(c): return PatternFill('solid', start_color=c, end_color=c)
thin = Side(style='thin', color='D3DEE9'); hair = Side(style='hair', color='B4C3D3'); med = Side(style='medium', color=PUR)
B_ALL = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()
ws = wb.active
ws.title = 'Kontrol Listesi'
ws.sheet_view.showGridLines = False
widths = {'A': 5, 'B': 42, 'C': 7.6, 'D': 10.4, 'E': 10.8, 'F': 10.2, 'G': 11}
for k, v in widths.items(): ws.column_dimensions[k].width = v

def merge(r, c1, c2, val, font, fl=None, al=None, h=None):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    cell = ws.cell(r, c1, val); cell.font = font
    if fl:
        for c in range(c1, c2 + 1): ws.cell(r, c).fill = fl
    cell.alignment = al or Alignment(vertical='center', wrap_text=True)
    if h: ws.row_dimensions[r].height = h
    return cell

# Başlık
merge(1, 1, 7, 'GEÇİCİ VERGİ KONTROL LİSTESİ', Font(name=F, size=18, bold=True, color='FFFFFF'), fill(PUR), Alignment(horizontal='left', vertical='center', indent=1), 36)
MX = f'MATCH($C$6,{TO}$B$5:$B$8,0)'
merge(2, 1, 5, f'="Beyan ve ödeme son günü: "&IFERROR(INDEX({TO}$D$5:$D$8,{MX}),"—")&"   ·   {NSEC} bölüm, {NITEM} madde"', Font(name=F, size=10, bold=True, color=PUR), fill(LAV), Alignment(horizontal='left', vertical='center', indent=1), 22)
ws.merge_cells('F2:G2'); ws['F2'] = f'=IFERROR(IF(INDEX({TO}$E$5:$E$8,{MX})="","Y. değerleme: —",INDEX({TO}$E$5:$E$8,{MX})),"—")'
ws['F2'].number_format = '"Y. değerleme: "0.00%'; ws['F2'].font = Font(name=F, size=9.5, bold=True, color='FFFFFF'); ws['F2'].alignment = Alignment(horizontal='center', vertical='center')
for cc in (6, 7): ws.cell(2, cc).fill = fill(GOLD)
ws.merge_cells('A3:G3'); ws['A3'] = 'Hazırlayan: Erdal Karahan · Serbest Muhasebeci Mali Müşavir · erdalkarahan.com'
ws['A3'].font = Font(name=F, size=9, italic=True, color=GRY); ws['A3'].alignment = Alignment(horizontal='right', vertical='center')
ws.row_dimensions[3].height = 18

# Mükellef bilgileri (doldurulacak alanlar)
for r, (l, ph) in enumerate([('Mükellef unvanı', ''), ('Vergi dairesi / VKN', ''), ('Dönem (listeden seçin)', dlabel(DON[SEC - 1]))], start=4):
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    c = ws.cell(r, 1, l); c.font = Font(name=F, size=9.5, bold=True, color=PUR); c.alignment = Alignment(vertical='center', indent=1)
    for cc in (1, 2): ws.cell(r, cc).fill = fill(LAV2); ws.cell(r, cc).border = Border(bottom=Side(style='thin', color='DDE5EE'))
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
    v = ws.cell(r, 3, ph); v.font = Font(name=F, size=10.5, color=INK); v.alignment = Alignment(vertical='center', indent=1)
    for cc in range(3, 8):
        ws.cell(r, cc).fill = fill('EEF7F5'); ws.cell(r, cc).border = Border(bottom=Side(style='thin', color='7FBFB5'))
    ws.row_dimensions[r].height = 22
dvd = DataValidation(type='list', formula1=f'{TO}$B$5:$B$8', allow_blank=False); ws.add_data_validation(dvd); dvd.add('C6')
ws.row_dimensions[7].height = 6
merge(8, 1, 7, 'Kullanım: Her satırda uygun sütundaki ☐ kutusuna tıklayıp listeden ☑ seçin (geri almak için ☐ seçin). '
      'Dönemi 6. satırdaki listeden seçin; son gün ve yeniden değerleme oranı “Tarihler ve Oranlar” sayfasından gelir. Kâğıda basıp kalemle de doldurabilirsiniz. Renkli alanlar doldurulur.',
      Font(name=F, size=8.5, italic=True, color=GRY), None, Alignment(vertical='center', wrap_text=True), 30)
ws.row_dimensions[9].height = 6

HDR = 10
heads = ['No', 'Kontrol', 'Tamam', 'Düzeltilecek', 'Araştırılacak', 'Gerekmiyor', 'Not']
for i, h in enumerate(heads, start=1):
    c = ws.cell(HDR, i, h); c.font = Font(name=F, size=8.5, bold=True, color=PUR)
    c.fill = fill(LAV); c.border = Border(bottom=med, top=thin)
    c.alignment = Alignment(horizontal='left' if i in (2, 7) else 'center', vertical='center', wrap_text=True)
ws.row_dimensions[HDR].height = 24
ws.print_title_rows = f'{HDR}:{HDR}'

dv = DataValidation(type='list', formula1=f'"{BOX_E},{BOX_F}"', allow_blank=True, showDropDown=False)
dv.promptTitle = 'İşaretle'; dv.prompt = '☑ seçin'; dv.showInputMessage = False
dv.errorTitle = 'Geçersiz'; dv.error = 'Listeden ☐ ya da ☑ seçin.'
ws.add_data_validation(dv)

def lines(t, cpl=52): return max(1, math.ceil(len(t) / cpl))

# Sayfa düzeni hesabı (A4 dikey, %92 ölçek; satırlar sayfa arasında bölünmez, başlıklar sayfa sonunda yalnız kalmaz)
PAGE_PT = 795   # yazdırılabilir yükseklik ölçeğe göre, tekrar eden başlık satırı düşülerek
used = sum((ws.row_dimensions[r].height or 15) for r in range(1, HDR + 1))
breaks = []
r = HDR + 1
n = 0
sec_rows = []
for si, (title, items) in enumerate(S, start=1):
    hh = 22
    first_h = max(21, 11.8 * lines(items[0]) + 8)
    if used + hh + first_h * 2 > PAGE_PT:
        breaks.append(r - 1); used = 0
    merge(r, 1, 7, f'  {si}   {title}', Font(name=F, size=10, bold=True, color='FFFFFF'), fill(PUR2), Alignment(vertical='center'), hh)
    ws.cell(r, 1).value = f'{si}'
    ws.unmerge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    ws.cell(r, 1).value = si; ws.cell(r, 1).font = Font(name=F, size=10, bold=True, color='FFFFFF'); ws.cell(r, 1).fill = fill(GOLD)
    ws.cell(r, 1).alignment = Alignment(horizontal='center', vertical='center')
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    ws.cell(r, 2).value = TU(title); ws.cell(r, 2).font = Font(name=F, size=10, bold=True, color='FFFFFF')
    ws.cell(r, 2).alignment = Alignment(vertical='center', indent=1)
    for cc in range(2, 8): ws.cell(r, cc).fill = fill(PUR2)
    used += hh; r += 1
    start = r
    for t in items:
        n += 1
        h = max(21, 11.8 * lines(t) + 8)
        if used + h > PAGE_PT:
            breaks.append(r - 1); used = 0
        zebra = fill(LAV2) if n % 2 == 0 else None
        c = ws.cell(r, 1, n); c.font = Font(name=F, size=8.5, bold=True, color=PUR); c.alignment = Alignment(horizontal='center', vertical='center')
        c = ws.cell(r, 2, t); c.font = Font(name=F, size=9.5, color=INK); c.alignment = Alignment(vertical='center', wrap_text=True)
        for cc in range(3, 7):
            b = ws.cell(r, cc, BOX_E); b.font = Font(name=F, size=13, color=PUR)
            b.alignment = Alignment(horizontal='center', vertical='center'); dv.add(b)
        g = ws.cell(r, 7); g.font = Font(name=F, size=8.5, color=INK); g.alignment = Alignment(vertical='center', wrap_text=True)
        for cc in range(1, 8):
            cell = ws.cell(r, cc)
            if zebra: cell.fill = zebra
            cell.border = Border(bottom=Side(style='thin', color='DDE5EE'))
        ws.cell(r, 7).border = Border(bottom=Side(style='hair', color='9FB1C4'))
        ws.row_dimensions[r].height = h
        used += h; r += 1
    sec_rows.append((si, title, start, r - 1))

# Onay
r += 1; used += 15
if used + 22 + 70 > PAGE_PT: breaks.append(r - 6); used = 0
ws.cell(r, 1, '✓').font = Font(name=F, size=11, bold=True, color='FFFFFF'); ws.cell(r, 1).fill = fill(GOLD)
ws.cell(r, 1).alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
ws.cell(r, 2, 'ONAY').font = Font(name=F, size=10, bold=True, color='FFFFFF'); ws.cell(r, 2).alignment = Alignment(vertical='center', indent=1)
for cc in range(2, 8): ws.cell(r, cc).fill = fill(PUR)
ws.row_dimensions[r].height = 22; r += 1
ONAY = r
ws.cell(r, 2, 'Hazırlayan · Ad Soyad · Tarih · İmza').font = Font(name=F, size=9, bold=True, color=PUR2)
ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
ws.cell(r, 3, 'Kontrol eden · Ad Soyad · Tarih · İmza').font = Font(name=F, size=9, bold=True, color=PUR2)
ws.row_dimensions[r].height = 18; r += 1
ws.row_dimensions[r].height = 46
ws.cell(r, 2).border = Border(bottom=Side(style='medium', color=PUR2))
ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
for cc in range(3, 8): ws.cell(r, cc).border = Border(bottom=Side(style='medium', color=PUR2))
for cc in range(2, 8): ws.cell(r, cc).fill = fill('EEF7F5')
r += 2
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
ws.cell(r, 1, 'Bu liste, geçici vergi dönem sonu kontrollerinde çalışma kâğıdı olarak kullanılmak üzere hazırlanmıştır; her mükellefin durumuna göre uyarlanmalıdır. Tutar, oran ve sürelerde güncel mevzuat esas alınmalıdır. — Erdal Karahan, Serbest Muhasebeci Mali Müşavir · erdalkarahan.com').font = Font(name=F, size=7.5, italic=True, color=GRY)
ws.cell(r, 1).alignment = Alignment(wrap_text=True, vertical='top'); ws.row_dimensions[r].height = 24
LAST = r

# Koşullu biçim: işaretli kutu rengini alır
first_item = HDR + 1
for col, color, fc in (('C', 'D7F5DF', '1E7B3C'), ('D', 'FBD9D9', 'B42318'), ('E', 'FDEFC8', '9A6700'), ('F', 'E6E6EE', '51506A')):
    ws.conditional_formatting.add(f'{col}{first_item}:{col}{LAST}', FormulaRule(formula=[f'{col}{first_item}="{BOX_F}"'], fill=fill(color), font=Font(name=F, color=fc, bold=True)))
# satırdaki madde metni, Hatalı ya da İncelenecek işaretliyse vurgulanır
ws.conditional_formatting.add(f'B{first_item}:B{LAST}', FormulaRule(formula=[f'$D{first_item}="{BOX_F}"'], font=Font(name=F, color='B42318', bold=True)))
ws.conditional_formatting.add(f'B{first_item}:B{LAST}', FormulaRule(formula=[f'$E{first_item}="{BOX_F}"'], font=Font(name=F, color='9A6700', bold=True)))

for b in breaks: ws.row_breaks.append(Break(id=b))
ps = ws.page_setup
ps.paperSize = ws.PAPERSIZE_A4; ps.orientation = 'portrait'; ps.scale = 92
ws.sheet_properties.pageSetUpPr.fitToPage = False
ws.page_margins.left = ws.page_margins.right = 0.45; ws.page_margins.top = 0.55; ws.page_margins.bottom = 0.6
ws.page_margins.header = 0.25; ws.page_margins.footer = 0.3
ws.print_options.horizontalCentered = True
ws.oddFooter.left.text = f'Geçici Vergi Kontrol Listesi · {YIL} · Erdal Karahan, SMMM · erdalkarahan.com'; ws.oddFooter.left.size = 7; ws.oddFooter.left.font = 'Arial'
ws.oddFooter.right.text = 'Sayfa &P / &N'; ws.oddFooter.right.size = 7; ws.oddFooter.right.font = 'Arial'
ws.print_area = f'A1:G{LAST}'
ws.freeze_panes = f'A{HDR + 1}'

# ---------- Özet ----------
o = wb.create_sheet('Özet')
o.sheet_view.showGridLines = False
for k, v in {'A': 5, 'B': 42, 'C': 9, 'D': 9, 'E': 12.5, 'F': 12.5, 'G': 12, 'H': 10, 'I': 12}.items(): o.column_dimensions[k].width = v
o.merge_cells('A1:I1'); o['A1'] = 'KONTROL ÖZETİ'; o['A1'].font = Font(name=F, size=16, bold=True, color='FFFFFF')
o['A1'].alignment = Alignment(vertical='center', indent=1)
for c in range(1, 10): o.cell(1, c).fill = fill(PUR)
o.row_dimensions[1].height = 32
o.merge_cells('A2:I2'); o['A2'] = '="Mükellef: "&IF(\'Kontrol Listesi\'!C4="","—",\'Kontrol Listesi\'!C4)&"   ·   Dönem: "&\'Kontrol Listesi\'!C6'
o['A2'].font = Font(name=F, size=9.5, bold=True, color=PUR); o['A2'].alignment = Alignment(vertical='center', indent=1)
for c in range(1, 10): o.cell(2, c).fill = fill(LAV)
o.row_dimensions[2].height = 22
h = ['No', 'Bölüm', 'Madde', 'Tamam', 'Düzeltilecek', 'Araştırılacak', 'Gerekmiyor', 'İşaretli', 'Tamamlanma']
for i, t in enumerate(h, start=1):
    c = o.cell(4, i, t); c.font = Font(name=F, size=8.5, bold=True, color=PUR); c.fill = fill(LAV)
    c.alignment = Alignment(horizontal='left' if i == 2 else 'center', vertical='center', wrap_text=True); c.border = Border(bottom=med)
o.row_dimensions[4].height = 26
KL = "'Kontrol Listesi'!"
rr = 5
for si, title, a, b in sec_rows:
    o.cell(rr, 1, si); o.cell(rr, 2, title)
    o.cell(rr, 3, f'=COUNTA({KL}B{a}:B{b})')
    for j, col in enumerate('CDEF', start=4):
        o.cell(rr, j, f'=COUNTIF({KL}{col}{a}:{col}{b},"{BOX_F}")')
    o.cell(rr, 8, f'=SUMPRODUCT(--((({KL}C{a}:C{b}="{BOX_F}")+({KL}D{a}:D{b}="{BOX_F}")+({KL}E{a}:E{b}="{BOX_F}")+({KL}F{a}:F{b}="{BOX_F}"))>0))')
    o.cell(rr, 9, f'=IF(C{rr}=0,0,H{rr}/C{rr})')
    for c in range(1, 10):
        cell = o.cell(rr, c); cell.font = Font(name=F, size=9.5, color=INK, bold=(c == 1))
        cell.alignment = Alignment(horizontal='left' if c == 2 else 'center', vertical='center', wrap_text=True)
        cell.border = Border(bottom=Side(style='thin', color='DDE5EE'))
        if si % 2 == 0: cell.fill = fill(LAV2)
    o.cell(rr, 1).font = Font(name=F, size=9.5, bold=True, color=PUR)
    o.cell(rr, 9).number_format = '0%'
    o.row_dimensions[rr].height = 20
    rr += 1
T = rr
o.cell(T, 2, 'TOPLAM')
for j in range(3, 9):
    col = 'ABCDEFGHI'[j - 1]
    o.cell(T, j, f'=SUM({col}5:{col}{T - 1})')
o.cell(T, 9, f'=IF(C{T}=0,0,H{T}/C{T})'); o.cell(T, 9).number_format = '0%'
for c in range(1, 10):
    cell = o.cell(T, c); cell.font = Font(name=F, size=10, bold=True, color='FFFFFF'); cell.fill = fill(PUR)
    cell.alignment = Alignment(horizontal='left' if c == 2 else 'center', vertical='center', indent=1 if c == 2 else 0)
o.row_dimensions[T].height = 24
from openpyxl.formatting.rule import DataBarRule, CellIsRule
o.conditional_formatting.add(f'I5:I{T - 1}', DataBarRule(start_type='num', start_value=0, end_type='num', end_value=1, color='2A9D8F', showValue=True))
o.conditional_formatting.add(f'E5:E{T - 1}', CellIsRule(operator='greaterThan', formula=['0'], font=Font(name=F, bold=True, color='B42318'), fill=fill('FBD9D9')))
o.conditional_formatting.add(f'F5:F{T - 1}', CellIsRule(operator='greaterThan', formula=['0'], font=Font(name=F, bold=True, color='9A6700'), fill=fill('FDEFC8')))
o.merge_cells(start_row=T + 2, start_column=1, end_row=T + 2, end_column=9)
o.cell(T + 2, 1, 'Bu sayfaya bir şey yazmanıza gerek yoktur; sayılar “Kontrol Listesi” sayfasındaki ☑ işaretlerinden hesaplanır. '
       '“Düzeltilecek” ya da “Araştırılacak” sütununda sıfırdan büyük sayı olan bölümler kapanıştan önce yeniden ele alınmalıdır.').font = Font(name=F, size=8, italic=True, color=GRY)
o.cell(T + 2, 1).alignment = Alignment(wrap_text=True, vertical='top'); o.row_dimensions[T + 2].height = 30
o.page_setup.paperSize = o.PAPERSIZE_A4; o.page_setup.orientation = 'portrait'
o.sheet_properties.pageSetUpPr.fitToPage = True; o.page_setup.fitToWidth = 1; o.page_setup.fitToHeight = 1
o.page_margins.left = o.page_margins.right = 0.45
o.print_options.horizontalCentered = True

# ---------- Tarihler ve oranlar ----------
t = wb.create_sheet('Tarihler ve Oranlar')
t.sheet_view.showGridLines = False
for k, v in {'A': 4, 'B': 30, 'C': 15, 'D': 19, 'E': 17, 'F': 34}.items(): t.column_dimensions[k].width = v
t.merge_cells('A1:F1'); t['A1'] = f'{YIL} GEÇİCİ VERGİ · TARİHLER VE ORANLAR'; t['A1'].font = Font(name=F, size=14, bold=True, color='FFFFFF')
t['A1'].alignment = Alignment(vertical='center', indent=1)
for c in range(1, 7): t.cell(1, c).fill = fill(PUR)
t.row_dimensions[1].height = 30
t.merge_cells('A2:F2'); t['A2'] = 'Renkli oran hücrelerine, GİB açıkladıkça yeni dönemin oranını yazabilirsiniz. “Kontrol Listesi” sayfasında seçtiğiniz dönemin son günü ve oranı buradan okunur. Kaynak sütunundaki bağlantılar resmî duyuruya gider.'
t['A2'].font = Font(name=F, size=8.5, italic=True, color=GRY); t['A2'].alignment = Alignment(wrap_text=True, vertical='center'); t.row_dimensions[2].height = 30
def hdr(r, labels):
    for i, x in enumerate(labels, start=1):
        c = t.cell(r, i, x); c.font = Font(name=F, size=8.5, bold=True, color=PUR); c.fill = fill(LAV); c.border = Border(bottom=med)
        c.alignment = Alignment(horizontal='left' if i in (2, 6) else 'center', vertical='center', wrap_text=True)
    t.row_dimensions[r].height = 30
hdr(4, ['No', 'Dönem', 'Kapsadığı aylar', 'Beyan ve ödeme son günü', 'Yeniden değerleme oranı (VUK mük. 298/Ç)', 'Kaynak'])
for k, d in enumerate(DON):
    r = 5 + k
    vals = [d['no'], dlabel(d), d['aylar'], d['songun'], (d['oran'] / 100 if d.get('oran') is not None else None), d.get('kaynak') or 'Açıklandığında yazın']
    for i, x in enumerate(vals, start=1):
        c = t.cell(r, i, x); c.font = Font(name=F, size=10, color=INK, bold=(i in (1, 5)))
        c.alignment = Alignment(horizontal='left' if i in (2, 6) else 'center', vertical='center', wrap_text=True)
        c.border = Border(bottom=Side(style='thin', color='DDE5EE'))
    e = t.cell(r, 5); e.number_format = '0.00%'; e.fill = fill('EEF7F5'); e.border = Border(bottom=Side(style='thin', color='7FBFB5'))
    if d.get('url'):
        f6 = t.cell(r, 6); f6.hyperlink = d['url']; f6.font = Font(name=F, size=9.5, color='1F4E79', underline='single')
    else:
        t.cell(r, 6).font = Font(name=F, size=9, italic=True, color=GRY)
    t.row_dimensions[r].height = 24
t.conditional_formatting.add('A5:F8', FormulaRule(formula=["$B5='Kontrol Listesi'!$C$6"], fill=fill('DFF1EE'), font=Font(name=F, bold=True, color='1F7A6E')))
hdr(10, ['', 'Geçici vergi oranları', '', '', 'Oran', 'Dayanak'])
for k, (lab_, oran_, day_, url_) in enumerate(RJ['oranlar']):
    r = 11 + k
    t.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    t.cell(r, 2, lab_).font = Font(name=F, size=10, color=INK); t.cell(r, 2).alignment = Alignment(vertical='center', wrap_text=True)
    c = t.cell(r, 5, oran_); c.number_format = '0%'; c.font = Font(name=F, size=10, bold=True, color=PUR); c.alignment = Alignment(horizontal='center', vertical='center')
    l = t.cell(r, 6, day_); l.hyperlink = url_; l.font = Font(name=F, size=9.5, color='1F4E79', underline='single'); l.alignment = Alignment(vertical='center')
    for cc in range(1, 7): t.cell(r, cc).border = Border(bottom=Side(style='thin', color='DDE5EE'))
    t.row_dimensions[r].height = 24
nr = 11 + len(RJ['oranlar']) + 1
t.merge_cells(start_row=nr, start_column=1, end_row=nr, end_column=6)
t.cell(nr, 1, '2025 yılından itibaren 4. dönem (Ekim–Aralık) için de geçici vergi beyannamesi verilir. 2025, 2026 ve 2027’de enflasyon düzeltmesi yapılmaz (7571 s. Kanun); bu yıllarda amortismana tabi varlıklar için VUK mük. 298/Ç yeniden değerlemesi isteğe bağlı olarak yapılabilir. Önceki bir dönemde yeniden değerleme yapıldıysa oran tekrar uygulanmaz; yıl başı değerlerinden hesaplanıp fark kaydedilir.').font = Font(name=F, size=9, bold=True, color='1F7A6E')
t.cell(nr, 1).fill = fill('E3F2EF'); t.row_dimensions[nr].height = 48; t.cell(nr, 1).alignment = Alignment(vertical='center', indent=1, wrap_text=True)
t.merge_cells(start_row=nr + 2, start_column=1, end_row=nr + 2, end_column=6)
t.cell(nr + 2, 1, f"Son güncelleme: {RJ.get('guncelleme', '')}. Hazırlayan: Erdal Karahan, Serbest Muhasebeci Mali Müşavir · erdalkarahan.com").font = Font(name=F, size=8, italic=True, color=GRY)
t.page_setup.paperSize = t.PAPERSIZE_A4; t.page_setup.orientation = 'portrait'
t.sheet_properties.pageSetUpPr.fitToPage = True; t.page_setup.fitToWidth = 1; t.page_setup.fitToHeight = 0; t.print_options.horizontalCentered = True

wb.active = 0
wb.save(OUT)
print('ok', OUT, 'breaks', breaks, 'last', LAST)
