# -*- coding: utf-8 -*-
# Amaç ve konu kataloğu — 1. kısım: genel bilgiler, kategoriler, tarım-gıda, sanayi
GIRIS = [
    "Limited şirkette TTK 576, anonim şirkette TTK 339 esas sözleşmede işletme konusunun “esaslı noktaları belirtilmiş ve açıkça tanımlanmış” olarak yer almasını istiyor. “Her türlü ticari faaliyet” gibi tek satır yetmez; sözleşmeyi okuyan, şirketin ne iş yaptığını anlamalı.",
    "Aşağıda sektör sektör hazır bentler var. İşinize uyan sektörü açın, ihtiyacınız olan bentleri işaretleyin, gerekirse başka sektörlerden de bent ekleyin. Seçtikleriniz alttaki kutuda sırayla birleşir; sonuna bütün şirketlerde kullanılan genel yetkiler eklenir. Metni kopyalayıp MERSİS’te esas sözleşmenin amaç ve konu maddesine yapıştırabilir ya da Word olarak indirebilirsiniz.",
    "NACE kodları 4 haneli sınıf düzeyinde, Türkiye’de 01.01.2025’ten beri kullanılan NACE Rev.2.1’e göre verildi. MERSİS ve vergi dairesinde 6 haneli alt sınıf seçilir; kodu MERSİS’teki güncel listeden, işinizi en iyi anlatan açıklamaya bakarak seçin."
]

KURALLAR = [
    "Asıl işinizi ilk bende yazın. MERSİS’te seçilen ana faaliyet kodu vergi dairesine de aktarılır; ilk bent ile ana NACE kodu birbirini tutmalı.",
    "Konuyu makul genişlikte tutun. Sonradan konu eklemek esas sözleşme değişikliğidir: ortaklar kurulu / genel kurul kararı, noter, tescil ve ilan masrafı çıkar. Yakın ve ileride yapabileceğiniz işleri baştan ekleyin.",
    "Ama birbiriyle hiç ilgisi olmayan onlarca sektörü tek sözleşmeye doldurmayın. Banka hesap açılışı, teşvik ve izin başvurularında “gerçek faaliyet” sorulur; dağınık konu açıklama ister.",
    "İzne ve özel şarta bağlı faaliyetleri (aşağıdaki tabloya bakın) gerekli izin, şirket türü ve sermaye şartını sağlamadan yazmayın; sicil müdürlüğü ilgili kurumun uygun görüşünü ister, yoksa tescil yapılmaz.",
    "Şirket konusunun dışında kalan bir işlemde bulunsa da işlem kural olarak şirketi bağlar (AŞ için TTK 371, limited için TTK 629 atfı). Konunun önemi daha çok ortaklar arası ilişki, yönetimin sorumluluğu, teşvik ve izinler bakımındandır.",
    "İştirak, menkul kıymet ve bağış bentlerine sermaye piyasası mevzuatı kaydını ekleyin (“yatırım hizmetleri ve faaliyetleri niteliğinde olmamak kaydıyla”). Aksi hâlde sicil müdürlüğü düzeltme isteyebilir.",
    "Ticaret unvanında geçen faaliyet ibaresi (ör. “İnşaat”, “Gıda”, “Yazılım”) amaç ve konuda mutlaka yer almalı.",
    "Asgari sermaye 2026 itibarıyla limited şirkette 50.000 TL, anonim şirkette 250.000 TL, kayıtlı sermaye sistemindeki halka açık olmayan anonim şirkette başlangıç sermayesi 500.000 TL (7887 sayılı CB Kararı). Bazı izinli faaliyetlerde çok daha yüksek sermaye aranır.",
    "Başvurudan önce kuruluşu yapacağınız ticaret sicili müdürlüğünün (İstanbul’da İTO) güncel örnek sözleşmesine ve istediği eklere bakın; müdürlükler arasında küçük uygulama farkları olabiliyor."
]

# [faaliyet, kurum / belge, şart notu]
IZINLI = [
    ["Bankacılık, finansal kiralama, faktoring, finansman, varlık yönetimi", "BDDK kuruluş ve faaliyet izni", "Anonim şirket ve yüksek asgari sermaye; konu yalnızca bu faaliyetle sınırlı tutulur."],
    ["Ödeme kuruluşu, elektronik para kuruluşu", "TCMB faaliyet izni", "Anonim şirket; sermaye ve ortaklık şartları var."],
    ["Yetkili müessese (döviz bürosu), kıymetli maden aracılığı", "Hazine ve Maliye Bakanlığı / TCMB mevzuatı", "Anonim şirket ve asgari sermaye şartı."],
    ["Aracı kurum, portföy yönetimi, kripto varlık hizmet sağlayıcı", "SPK izni", "Anonim şirket; konu bu faaliyetlerle sınırlı."],
    ["Sigorta, reasürans; sigorta ve reasürans brokerliği", "Hazine ve Maliye Bakanlığı / SEDDK", "Anonim şirket (sigorta acenteliği farklıdır; levhaya kayıt gerekir)."],
    ["Bağımsız denetim kuruluşu", "Kamu Gözetimi Kurumu (KGK) yetkisi", "Ortaklık ve yönetim şartları var."],
    ["Özel güvenlik şirketi", "İçişleri Bakanlığı faaliyet izni (5188 s. Kanun)", "Şirket yalnızca özel güvenlik alanında faaliyet gösterir; başka konu eklenemez."],
    ["Radyo, televizyon ve isteğe bağlı yayın", "RTÜK yayın lisansı / izni", "Anonim şirket ve ortaklık sınırlamaları."],
    ["Elektrik üretimi, ticareti, doğal gaz, akaryakıt, LPG dağıtım ve istasyonları", "EPDK lisansı", "Lisans türüne göre AŞ veya limited, sermaye ve pay şartları; bayilik için de lisans gerekir."],
    ["Elektronik haberleşme (internet servis sağlayıcı, GSM sanal operatör vb.)", "BTK yetkilendirmesi", "Yetki türüne göre şirket türü ve sermaye şartları."],
    ["Kargo, kurye ve posta hizmeti", "BTK posta hizmet sağlayıcı yetkisi", "Asgari sermaye ve teminat şartı."],
    ["Karayolu yük ve yolcu taşımacılığı, taşıma işleri organizatörlüğü", "Ulaştırma ve Altyapı Bakanlığı yetki belgesi (C, K, L, N, R, D, B türleri)", "Belge türüne göre öz mal, taşıt ve sermaye şartları."],
    ["Seyahat acentası", "Kültür ve Turizm Bakanlığı belgesi, TÜRSAB üyeliği", "Konu ve unvanda “seyahat acentası” ibaresi; belge alınmadan faaliyet yapılamaz."],
    ["Özel okul, kurs, etüt merkezi, sürücü kursu", "Millî Eğitim Bakanlığı kurum açma izni", "Kurucu ve bina şartları."],
    ["Özel hastane, tıp merkezi, poliklinik, laboratuvar, ağız ve diş sağlığı merkezi", "Sağlık Bakanlığı ruhsatı", "Mesul müdür ve kadro şartları. Muayenehane ve eczane şirket olarak açılamaz."],
    ["Kreş ve gündüz bakımevi, huzurevi, bakım merkezi", "Aile ve Sosyal Hizmetler Bakanlığı / MEB izni", "Bina ve personel şartları."],
    ["Özel istihdam bürosu, geçici iş ilişkisi", "İŞKUR izni", "Geçici iş ilişkisi kuracak büro için ayrıca teminat ve şartlar."],
    ["İş sağlığı ve güvenliği (OSGB), İSG eğitimi", "Çalışma ve Sosyal Güvenlik Bakanlığı yetkisi", "Kadro ve mekân şartları."],
    ["Madencilik", "MAPEG ruhsatı", "Ruhsat sahibi olabilmek için şirket konusunda madencilik yazılı olmalı."],
    ["Alkollü içki, tütün mamulleri üretimi ve toptan satışı", "Tarım ve Orman Bakanlığı (eski TAPDK) izni", "Perakende satış için ayrıca satış belgesi."],
    ["İlaç, tıbbi cihaz üretimi ve satışı, kozmetik üretimi", "TİTCK izin ve kayıtları", "Sorumlu müdür ve tesis şartları."],
    ["Gıda üretimi ve satışı, yem, veteriner ürünleri", "Tarım ve Orman Bakanlığı işletme kayıt veya onay belgesi", "Faaliyete başlamadan önce kayıt gerekir."],
    ["Taşınmaz ticareti (emlak danışmanlığı)", "Ticaret Bakanlığı taşınmaz ticareti yetki belgesi", "Mesleki yeterlilik belgesi şartı."],
    ["İkinci el motorlu kara taşıtı ticareti", "Ticaret Bakanlığı yetki belgesi", "İşyeri ve mesleki yeterlilik şartları."],
    ["Silah, mühimmat, patlayıcı madde üretimi ve ticareti", "MSB / İçişleri Bakanlığı izinleri", "Ayrıntılı güvenlik soruşturması ve özel şartlar."],
    ["Gümrük müşavirliği", "Ticaret Bakanlığı izni", "Gümrük müşavirliği gerçek kişilerce yapılır; şirket ancak mevzuattaki şartlarla kurulabilir."],
]

KATEGORILER = [
    ["tarim", "Tarım, hayvancılık ve gıda"],
    ["sanayi", "Sanayi ve imalat"],
    ["insaat", "İnşaat ve gayrimenkul"],
    ["ticaret", "Ticaret ve e-ticaret"],
    ["turizm", "Turizm, yeme-içme ve etkinlik"],
    ["lojistik", "Ulaştırma ve lojistik"],
    ["bilisim", "Bilişim, medya ve reklam"],
    ["profesyonel", "Danışmanlık ve profesyonel hizmetler"],
    ["egitim", "Eğitim, sağlık ve sosyal hizmet"],
    ["hizmet", "Kişisel ve işletme hizmetleri"],
    ["enerji", "Enerji, çevre ve madencilik"],
    ["yatirim", "Holding, yatırım ve finans"],
]

S = []
def s(id, k, ad, nace, m, notu=""):
    S.append({"id": id, "k": k, "ad": ad, "nace": nace, "m": m, **({"not": notu} if notu else {})})

# ---------------- TARIM, HAYVANCILIK VE GIDA ----------------
s("bitkisel-uretim", "tarim", "Bitkisel üretim, seracılık ve fidancılık",
  [["01.13", "Sebze, kavun-karpuz, kök ve yumru bitkileri yetiştiriciliği"], ["01.2", "Çok yıllık bitkiler (meyve, zeytin, fındık vb.)"], ["01.30", "Bitki üretimi (fide, fidan, çiçek)"], ["01.61", "Bitkisel üretimi destekleyici faaliyetler"]],
  ["Her türlü tarla bitkisi, sebze, meyve, zeytin, fındık, narenciye, kesme çiçek ve süs bitkisi yetiştirmek; açık alanda, serada, topraksız (hidroponik) ve dikey tarım yöntemleriyle üretim yapmak.",
   "Fide, fidan, tohum, aşı kalemi ve çoğaltım materyali üretmek; fidanlık ve sera kurmak, işletmek, kiralamak.",
   "Ürettiği veya satın aldığı tarımsal ürünleri yıkamak, ayıklamak, sınıflandırmak, paketlemek, soğuk hava deposunda muhafaza etmek, kurutmak ve işlemek; yurt içinde ve yurt dışında satmak, ihraç etmek.",
   "Sözleşmeli üretim yapmak; üreticilerle ürün alım, ön finansman ve girdi temini sözleşmeleri imzalamak.",
   "Tarım arazisi satın almak, kiralamak, toprak ıslahı, sulama, drenaj ve arazi düzenleme işleri yapmak; damla ve yağmurlama sulama sistemleri kurmak.",
   "Tohum, fide, gübre, zirai ilaç, sera malzemesi ve tarım makinelerinin alım satımını, ithalat ve ihracatını yapmak; mevzuatın izin verdiği ölçüde bayilik almak.",
   "İyi tarım, organik tarım ve benzeri sertifikasyon süreçlerini yürütmek; tarımsal danışmanlık, ilaçlama, budama, hasat ve harman hizmetleri vermek.",
   "Tarımsal destek, hibe ve kırsal kalkınma programlarına başvurmak; tarım sigortası yaptırmak."],
  "Zirai ilaç ve gübre bayiliği için Tarım ve Orman Bakanlığı’ndan bayilik belgesi; tohumculuk için ayrıca yetki belgesi gerekir.")

s("hayvancilik", "tarim", "Hayvancılık, süt ve besicilik",
  [["01.41", "Süt sığırcılığı"], ["01.42", "Diğer sığır ve manda yetiştiriciliği"], ["01.45", "Koyun ve keçi yetiştiriciliği"], ["01.47", "Kümes hayvancılığı"], ["01.62", "Hayvancılığı destekleyici faaliyetler"]],
  ["Büyükbaş ve küçükbaş hayvan yetiştiriciliği, süt hayvancılığı ve besicilik yapmak; damızlık hayvan üretmek, almak ve satmak.",
   "Kümes hayvanları, yumurta tavukçuluğu, etlik piliç, hindi, kaz ve diğer kanatlı yetiştiriciliği yapmak; kuluçkahane kurmak ve işletmek.",
   "Arıcılık, ipekböcekçiliği ve diğer hayvan yetiştiriciliği yapmak; bal, polen, propolis ve arı sütü üretmek ve satmak.",
   "Ahır, ağıl, kümes, yem deposu, silaj ve gübre tesisleri kurmak, kiralamak ve işletmek.",
   "Çiğ süt, et, yumurta ve diğer hayvansal ürünleri toplamak, soğutmak, depolamak ve satmak.",
   "Yem, yem katkı maddesi, veteriner ürünleri, sağım ve hayvancılık ekipmanının alım satımını ve ithalatını yapmak.",
   "Suni tohumlama, sürü yönetimi, kırkım ve benzeri hayvancılık destek hizmetleri vermek.",
   "Hayvancılık destekleri, kredi ve hibe programlarına başvurmak; hayvan hayat sigortası yaptırmak."],
  "Veteriner hekimlik hizmeti ve veteriner ilacı satışı mevzuattaki şartlara bağlıdır.")

s("su-urunleri", "tarim", "Su ürünleri, balıkçılık ve yetiştiricilik",
  [["03.11", "Deniz balıkçılığı"], ["03.21", "Deniz su ürünleri yetiştiriciliği"], ["03.22", "Tatlı su ürünleri yetiştiriciliği"], ["10.20", "Balık ve su ürünlerinin işlenmesi"]],
  ["Denizde, iç sularda ve kafeslerde balık ve diğer su ürünleri avlamak ve yetiştirmek; yavru (larva) üretim tesisi kurmak ve işletmek.",
   "Su ürünlerini işlemek, temizlemek, dondurmak, tütsülemek, marine etmek, konserve yapmak ve paketlemek.",
   "Su ürünlerinin toptan ve perakende ticaretini, ithalat ve ihracatını yapmak; soğuk hava deposu ve soğuk zincir araçları işletmek.",
   "Balıkçı gemisi, tekne, ağ ve av araç gereçlerini satın almak, kiralamak, satmak ve onarmak.",
   "Balık yemi ve su ürünleri yetiştiriciliği ekipmanının alım satımını ve ithalatını yapmak.",
   "Su ürünleri hal ve pazarlarında komisyonculuk yapmak, ihracat için kontrol ve sertifika işlemlerini yürütmek."],
  "Ticari balıkçılık ruhsat tezkeresi ve yetiştiricilik için Tarım ve Orman Bakanlığı izni gerekir.")

s("gida-imalati", "tarim", "Gıda üretimi ve paketleme (genel)",
  [["10.39", "Meyve ve sebzelerin işlenmesi ve saklanması"], ["10.84", "Baharat, sos ve çeşni üretimi"], ["10.85", "Hazır yemek üretimi"], ["10.89", "Başka yerde sınıflandırılmamış gıda üretimi"]],
  ["Her türlü gıda maddesini, kuru gıdayı, bakliyatı, baharatı, sosu, salçayı, turşuyu, reçeli, kuruyemişi, dondurulmuş ve hazır gıdayı üretmek, işlemek, paketlemek ve satmak.",
   "Gıda üretim tesisleri, paketleme ve dolum hatları, soğuk hava depoları kurmak, kiralamak ve işletmek; fason üretim yapmak ve yaptırmak.",
   "Kendi markası veya başkalarının markası adına (özel marka) gıda üretmek; ambalaj ve etiket tasarımı yaptırmak.",
   "Gıda hammaddesi, katkı maddesi ve ambalaj malzemesinin alım satımını, ithalat ve ihracatını yapmak.",
   "Ürünlerin market zincirleri, toptancılar, e-ticaret siteleri ve ihracat kanallarıyla satışını yapmak; bayilik ve distribütörlük vermek ve almak.",
   "Gıda güvenliği, kalite yönetimi, helal ve organik sertifikasyon süreçlerini yürütmek; laboratuvar kurmak.",
   "Gıda teknolojisi alanında Ar-Ge yapmak, yeni ürün geliştirmek."],
  "Tarım ve Orman Bakanlığı’ndan gıda işletme kayıt belgesi (bazı ürünlerde onay belgesi) alınmadan üretime başlanamaz.")

s("unlu-mamul", "tarim", "Fırın, pastane, unlu mamul ve şekerleme",
  [["10.71", "Ekmek, taze pastane ürünleri ve kek üretimi"], ["10.72", "Peksimet, bisküvi, dayanıklı pastane ürünleri"], ["10.82", "Kakao, çikolata ve şekerleme üretimi"], ["47.2", "Gıda perakende ticareti (grup)"]],
  ["Ekmek, simit, pide, poğaça, börek, pasta, kek, kurabiye, tatlı, baklava ve her türlü unlu mamul üretmek ve satmak.",
   "Çikolata, lokum, helva, şekerleme, bisküvi, gofret ve dayanıklı pastane ürünleri üretmek, paketlemek ve satmak.",
   "Fırın, pastane, butik pasta atölyesi ve satış noktaları açmak, işletmek, kiralamak; franchise vermek ve almak.",
   "Otel, restoran, kafe, market ve kurumlara toptan unlu mamul tedarik etmek; dondurulmuş hamur ürünleri üretmek.",
   "Un, şeker, yağ, kakao ve diğer hammaddelerin, fırın ve pastane ekipmanının alım satımını ve ithalatını yapmak.",
   "Ürünlerin internet ve paket servis yoluyla satışını yapmak; özel gün ve organizasyonlara ürün hazırlamak."],
  "Gıda işletme kayıt belgesi ve belediyeden işyeri açma ve çalışma ruhsatı gerekir.")

s("et-sut", "tarim", "Et, tavuk ve süt ürünleri işleme",
  [["10.11", "Etin işlenmesi ve saklanması (kümes hayvanları hariç)"], ["10.12", "Kümes hayvanı etinin işlenmesi"], ["10.13", "Et ve kümes hayvanı eti ürünleri üretimi"], ["10.51", "Süt ürünleri üretimi"], ["10.52", "Dondurma üretimi"]],
  ["Mezbaha ve kesimhane kurmak ve işletmek; kırmızı et ve kanatlı eti kesmek, parçalamak, işlemek, dondurmak ve paketlemek.",
   "Sucuk, salam, sosis, pastırma, kavurma, köfte ve diğer et ürünlerini üretmek ve satmak.",
   "Süt toplamak, soğutmak; süt, yoğurt, ayran, peynir, tereyağı, kaymak, dondurma ve diğer süt ürünlerini üretmek, paketlemek ve satmak.",
   "Et ve süt ürünlerinin toptan ve perakende ticaretini, ithalat ve ihracatını yapmak; kasap, şarküteri ve satış mağazaları açmak.",
   "Soğuk zincir araçları, soğuk hava depoları ve dağıtım ağı kurmak ve işletmek.",
   "Üreticilerle süt ve canlı hayvan alım sözleşmeleri yapmak; yem ve girdi desteği sağlamak."],
  "Kesimhane ve et-süt işleme tesisleri Tarım ve Orman Bakanlığı onay belgesine tabidir.")

s("icecek", "tarim", "İçecek, su dolum ve kahve-çay işleme",
  [["11.07", "Alkolsüz içecek, maden suyu ve şişelenmiş su üretimi"], ["10.83", "Çay ve kahve işleme"], ["10.32", "Meyve ve sebze suyu üretimi"]],
  ["Meyve suyu, gazlı ve gazsız alkolsüz içecek, enerji içeceği, soğuk çay ve benzeri içecekleri üretmek, dolum yapmak ve satmak.",
   "Kaynak suyu, içme suyu ve maden suyu dolum tesisi kurmak ve işletmek.",
   "Kahve çekirdeği kavurmak, öğütmek, paketlemek; çay harmanlamak ve paketlemek; bitki çayı ve aromalı içecek tozları üretmek.",
   "İçeceklerin bayi ve dağıtım ağı aracılığıyla, e-ticaret ve otomatlarla satışını yapmak; otomat yerleştirmek ve işletmek.",
   "İçecek hammaddesi, şişe, kapak, etiket ve dolum makinelerinin alım satımını ve ithalatını yapmak."],
  "Kaynak ve maden suyu için Sağlık Bakanlığı izni; alkollü içki üretimi için Tarım ve Orman Bakanlığı izni gerekir.")

# ---------------- SANAYİ VE İMALAT ----------------
s("tekstil-konfeksiyon", "sanayi", "Tekstil, konfeksiyon ve hazır giyim",
  [["13.20", "Dokuma"], ["13.30", "Tekstil terbiyesi (boya, baskı, apre)"], ["14.10", "Örgü giyim eşyası üretimi"], ["14.21", "Dış giyim üretimi"], ["14.23", "İş giysisi üretimi"]],
  ["İplik, kumaş, örme ve dokuma ürünleri üretmek; boyama, baskı, nakış, yıkama ve apre işlemleri yapmak.",
   "Her türlü kadın, erkek ve çocuk hazır giyim, iç giyim, iş elbisesi, üniforma, spor giyim ve ev tekstili ürünü dikmek, üretmek ve satmak.",
   "Konfeksiyon atölyesi ve fabrika kurmak, kiralamak ve işletmek; yurt içinde ve yurt dışında fason üretim yapmak ve yaptırmak.",
   "Model, kalıp ve koleksiyon tasarlamak; numune üretmek; marka oluşturmak ve tescil ettirmek.",
   "Tekstil hammaddesi, kumaş, aksesuar ve tekstil makinelerinin alım satımını, ithalat ve ihracatını yapmak.",
   "Ürünlerin toptan, perakende, mağaza ve e-ticaret yoluyla satışını yapmak; ihracat ve dış ticaret işlemlerini yürütmek.",
   "Kalite kontrol, ürün testleri ve sürdürülebilirlik sertifikasyonu süreçlerini yürütmek."])

s("deri-ayakkabi", "sanayi", "Deri, ayakkabı ve çanta",
  [["15.11", "Derinin tabaklanması ve işlenmesi"], ["15.12", "Bavul, el çantası, saraciye ürünleri"], ["15.20", "Ayakkabı üretimi"], ["14.24", "Deri ve kürk giyim eşyası"]],
  ["Ham deriyi işlemek, tabaklamak, boyamak ve satmak.",
   "Ayakkabı, bot, terlik, çanta, cüzdan, kemer, bavul ve saraciye ürünleri üretmek, tasarlamak ve satmak.",
   "Deri ve kürk giyim eşyası, eldiven ve aksesuar üretmek ve satmak.",
   "Atölye ve fabrika kurmak, işletmek; fason üretim yapmak ve yaptırmak.",
   "Deri, taban, aksesuar, kimyasal ve makinelerin alım satımını, ithalat ve ihracatını yapmak.",
   "Ürünlerin mağaza, bayi ve e-ticaret yoluyla satışını ve ihracatını yapmak; marka tescil ettirmek."])

s("mobilya-ahsap", "sanayi", "Mobilya, ahşap ve doğrama",
  [["31.00", "Mobilya üretimi"], ["16.23", "Diğer ahşap yapı ve doğrama ürünleri"], ["16.25", "Ahşap kapı ve pencere üretimi"], ["47.5", "Diğer ev eşyası perakende ticareti (grup)"]],
  ["Ev, ofis, otel, okul ve hastane mobilyası, mutfak dolabı, gömme dolap, vestiyer, bahçe mobilyası üretmek, tasarlamak ve monte etmek.",
   "Ahşap kapı, pencere, parke, lambri, merdiven ve doğrama ürünleri üretmek ve satmak.",
   "Kereste, sunta, MDF, kontrplak ve ahşap levha işlemek; CNC kesim, kaplama, cila ve boya hizmeti vermek.",
   "Mobilya mağazası ve showroom açmak, işletmek; bayilik ve franchise vermek ve almak.",
   "Proje bazlı iç mekân mobilyası ve dekorasyon işleri üstlenmek; anahtar teslim proje yapmak.",
   "Ahşap, aksesuar, kumaş, sünger ve mobilya makinelerinin alım satımını, ithalat ve ihracatını yapmak."])

s("plastik-ambalaj", "sanayi", "Plastik, ambalaj ve kâğıt ürünleri",
  [["22.21", "Plastik levha, tüp ve profil üretimi"], ["22.22", "Plastik ambalaj üretimi"], ["22.25", "Plastik ürünlerin işlenmesi ve son işlemleri"], ["17.21", "Oluklu mukavva ve kâğıt-karton ambalaj"]],
  ["Plastik enjeksiyon, şişirme, ekstrüzyon ve termoform yöntemleriyle her türlü plastik ürün, ambalaj, şişe, kap, poşet ve film üretmek.",
   "Karton kutu, oluklu mukavva, kâğıt torba, etiket ve her türlü ambalaj malzemesi üretmek ve basmak.",
   "Kalıp tasarlamak ve yaptırmak; fason üretim yapmak.",
   "Plastik hammadde (granül), geri dönüştürülmüş hammadde, boya ve katkı maddelerinin alım satımını ve ithalatını yapmak.",
   "Ambalaj atıklarını toplamak, ayırmak ve geri kazanmak (mevzuattaki izinlerle).",
   "Ürünlerin yurt içi ve yurt dışı satışını, ihracatını yapmak."])

s("metal-makine", "sanayi", "Metal işleme, makine ve ekipman imalatı",
  [["25.11", "Metal yapı ve yapı parçaları"], ["25.6", "Metallerin işlenmesi ve kaplanması (grup)"], ["28.2", "Genel amaçlı diğer makineler (grup)"], ["28.99", "Başka yerde sınıflandırılmamış özel amaçlı makineler"], ["33.12", "Makinelerin onarımı"]],
  ["Çelik konstrüksiyon, metal yapı, sundurma, hangar, depo, tank, silo ve metal kapı-pencere üretmek ve monte etmek.",
   "Talaşlı imalat, CNC işleme, kaynak, lazer ve plazma kesim, büküm, pres, döküm, galvaniz, boya ve kaplama işleri yapmak.",
   "Sanayi makineleri, üretim hatları, konveyör, yedek parça ve özel amaçlı makineler tasarlamak, üretmek, kurmak ve satmak.",
   "Makine ve ekipmanların montaj, bakım, onarım ve revizyon hizmetlerini vermek.",
   "Metal hammadde, profil, sac, boru ve hırdavat malzemelerinin alım satımını, ithalat ve ihracatını yapmak.",
   "Proje ve mühendislik çalışmaları yapmak; anahtar teslim tesis kurmak.",
   "Kalite belgeleri almak, test ve muayene süreçlerini yürütmek; Ar-Ge yapmak."])

s("kimya-kozmetik", "sanayi", "Kimya, kozmetik ve temizlik ürünleri",
  [["20.41", "Sabun, deterjan, temizlik ve parlatıcı ürünler"], ["20.42", "Parfüm, kozmetik ve kişisel bakım ürünleri"], ["20.59", "Başka yerde sınıflandırılmamış kimyasal ürünler"], ["20.30", "Boya, vernik ve benzeri kaplamalar"]],
  ["Sabun, deterjan, yüzey temizleyici, dezenfektan ve her türlü temizlik ürünü üretmek, dolum yapmak ve satmak.",
   "Parfüm, kozmetik, cilt ve saç bakım ürünü, kişisel hijyen ürünü üretmek, fason ürettirmek ve satmak.",
   "Boya, vernik, yapıştırıcı, endüstriyel kimyasal ve katkı maddesi üretmek ve satmak.",
   "Kimyasal hammaddelerin alım satımını, ithalat ve ihracatını yapmak; depolamak.",
   "Kendi markasıyla ve özel marka (private label) olarak üretim yapmak; ambalaj ve etiket tasarlatmak.",
   "Laboratuvar kurmak, formül geliştirmek, ürün güvenlik değerlendirmesi ve kayıt işlemlerini yürütmek."],
  "Kozmetik üretimi ve biyosidal ürünler TİTCK kayıt ve izinlerine; tehlikeli kimyasallar ayrıca çevre ve İSG mevzuatına tabidir.")

s("elektronik-imalat", "sanayi", "Elektrik-elektronik ve aydınlatma imalatı",
  [["26.11", "Elektronik bileşen ve kart üretimi"], ["27.12", "Elektrik dağıtım ve kontrol cihazları"], ["27.40", "Aydınlatma ekipmanı üretimi"], ["27.90", "Diğer elektrikli ekipman"]],
  ["Elektronik kart, devre, sensör, kontrol ve otomasyon cihazları tasarlamak, üretmek ve satmak.",
   "Elektrik panosu, kablo, şalt malzemesi, trafo ve elektrik dağıtım ekipmanı üretmek ve satmak.",
   "LED ve diğer aydınlatma armatürleri, aydınlatma sistemleri tasarlamak ve üretmek.",
   "Gömülü yazılım geliştirmek, nesnelerin interneti (IoT) ürünleri tasarlamak; Ar-Ge yapmak.",
   "Elektronik komponent ve malzemelerin alım satımını, ithalat ve ihracatını yapmak.",
   "Ürünlerin kurulum, bakım, onarım ve satış sonrası hizmetlerini vermek."])

s("matbaa", "sanayi", "Matbaa, baskı ve reklam ürünleri üretimi",
  [["18.12", "Diğer basım faaliyetleri"], ["18.13", "Baskı öncesi hizmetler"], ["18.14", "Ciltçilik"], ["18.20", "Kayıtlı medyanın çoğaltılması"]],
  ["Ofset, dijital, serigrafi, flekso ve geniş format baskı yöntemleriyle kitap, dergi, katalog, broşür, ambalaj, etiket ve her türlü basılı ürün basmak.",
   "Kurumsal kimlik ürünleri, promosyon ürünleri, tabela, totem, branda ve açık hava reklam malzemesi üretmek.",
   "Baskı öncesi tasarım, mizanpaj, kalıp ve prova hizmetleri; cilt, kesim, laminasyon ve diğer baskı sonrası işleri yapmak.",
   "Matbaa makineleri, kâğıt, mürekkep ve sarf malzemelerinin alım satımını ve ithalatını yapmak.",
   "Fason baskı yapmak ve yaptırmak; ürünleri internet üzerinden satmak."],
  "Matbaalar 5187 sayılı Basın Kanunu’na göre bilgi verme yükümlülüğüne tabidir.")

s("kuyum", "sanayi", "Kuyum, mücevher ve takı",
  [["32.12", "Mücevher ve benzeri ürünler"], ["32.13", "İmitasyon takı"], ["47.7", "Diğer ürünlerin perakende ticareti (grup)"]],
  ["Altın, gümüş, platin ve diğer kıymetli madenlerden mücevher, takı, saat ve süs eşyası tasarlamak, üretmek ve satmak.",
   "Değerli ve yarı değerli taşları işlemek, montürlemek; imitasyon takı ve bijuteri üretmek.",
   "Kuyumcu mağazası ve atölye açmak, işletmek; tamir, gravür ve ölçü hizmetleri vermek.",
   "Kıymetli madenlerin ve mücevherin toptan ve perakende ticaretini, ithalat ve ihracatını mevzuat çerçevesinde yapmak.",
   "Ürünlerin fuar, e-ticaret ve ihracat kanallarıyla satışını yapmak."],
  "Borsa İstanbul Kıymetli Madenler Piyasası üyeliği ve kıymetli maden aracılığı ayrı izin ve sermaye şartına bağlıdır.")

s("yapi-malzemesi", "sanayi", "Beton, mermer, cam ve yapı malzemesi üretimi",
  [["23.61", "İnşaat amaçlı beton ürünleri"], ["23.63", "Hazır beton üretimi"], ["23.70", "Taşların kesilmesi ve şekillendirilmesi"], ["23.1", "Cam ve cam ürünleri (grup)"]],
  ["Hazır beton, beton blok, briket, parke taşı, bordür, prefabrik yapı elemanı üretmek ve satmak.",
   "Mermer, granit, traverten ve doğal taşları kesmek, işlemek, cilalamak ve satmak; ocak işletmek veya işlettirmek.",
   "Düz cam, temperli cam, ısıcam ve cam ürünleri işlemek ve monte etmek.",
   "Seramik, karo, tuğla, kiremit, alçı ve yalıtım malzemesi üretmek ve satmak.",
   "Yapı malzemesi toptan ve perakende ticareti, ithalat ve ihracatı yapmak; şantiyelere tedarik etmek.",
   "Beton pompası, mikser ve iş makinesi kiralamak, nakliye hizmeti vermek."],
  "Ocak işletmesi için MAPEG ruhsatı; hazır beton tesisleri için çevre izni gerekir.")

s("otomotiv-yan-sanayi", "sanayi", "Otomotiv yan sanayi ve karoser",
  [["29.20", "Karoser, treyler ve yarı treyler üretimi"], ["29.3", "Motorlu kara taşıtları parça ve aksesuarları (grup)"], ["22.11", "Kauçuk lastik ve iç lastik"]],
  ["Motorlu taşıtlar için yedek parça, aksam, aksesuar ve komponent üretmek ve satmak.",
   "Karoser, kasa, damper, treyler, yarı treyler, frigorifik kasa ve özel amaçlı araç üstyapısı üretmek.",
   "Araç dönüşüm (ambulans, karavan, engelli aracı vb.) işleri yapmak; tip onayı ve homologasyon süreçlerini yürütmek.",
   "Otomotiv ana sanayisine ve yedek parça pazarına tedarik yapmak; ihracat yapmak.",
   "Hammadde, kalıp ve üretim ekipmanı alım satımını ve ithalatını yapmak."])

s("medikal-imalat", "sanayi", "Tıbbi cihaz ve medikal ürün üretimi",
  [["32.50", "Tıbbi ve dişçilik alet ve malzemeleri"], ["26.60", "Işınlama, elektromedikal ve elektroterapi cihazları"], ["46", "Toptan ticaret: tıbbi ürünlere ilişkin sınıf"]],
  ["Tıbbi cihaz, sarf malzemesi, ortopedik ürün, protez, diş ve laboratuvar malzemesi üretmek ve satmak.",
   "Hastane ve sağlık kuruluşlarına tıbbi cihaz ve sarf malzemesi tedarik etmek; kamu ihalelerine katılmak.",
   "Tıbbi cihazların kurulum, bakım, kalibrasyon ve teknik servis hizmetlerini vermek.",
   "Tıbbi cihaz ve medikal ürünlerin ithalat ve ihracatını yapmak; yetkili temsilcilik almak.",
   "Ürün tescil, ÜTS kayıt ve CE belgelendirme süreçlerini yürütmek; Ar-Ge yapmak."],
  "Tıbbi cihaz üretimi, satışı ve satış merkezleri TİTCK kayıt ve izinlerine tabidir.")

s("geri-donusum", "sanayi", "Geri dönüşüm ve atık işleme",
  [["38.1", "Atıkların toplanması (grup)"], ["38.2", "Atıkların geri kazanımı (grup)"], ["46", "Toptan ticaret: atık ve hurdaya ilişkin sınıf"]],
  ["Ambalaj atığı, hurda metal, plastik, kâğıt, cam, elektronik atık, atık yağ ve diğer atıkları toplamak, taşımak, ayrıştırmak ve geri kazanmak.",
   "Geri kazanım ve ayrıştırma tesisi kurmak ve işletmek; geri dönüştürülmüş hammadde üretmek ve satmak.",
   "Hurda ve atık ticareti, ithalat ve ihracatını mevzuat çerçevesinde yapmak.",
   "Belediyeler ve sanayi kuruluşlarıyla atık yönetimi sözleşmeleri yapmak; sıfır atık danışmanlığı vermek.",
   "Atık taşıma araçları, konteyner ve ekipman satın almak, kiralamak."],
  "Atık toplama, taşıma ve geri kazanım faaliyetleri Çevre, Şehircilik ve İklim Değişikliği Bakanlığı lisansına tabidir.")
