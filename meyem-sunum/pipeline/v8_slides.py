"""MEYEM v8 slaytları: 13 slayt. Metinler faz2_hikaye.md (A başlıklar), sistem faz3_tasarim.md."""
from v8_common import *

MEDAL = 400                     # mühür madalyonu kutusu (px)
SEAL_W, SEAL_H = 228, 223       # MEYEM mührü (585×573 oranı)
HALF = col(6)                   # sağ yarı fotoğrafın sol kenarı (976)


def seal_group(cx, cy, i=None):
    """Kâğıt madalyon + guilloche halka (pişmiş) + MEYEM mührü."""
    h = IMG('v8_muhur_halka.png', cx - MEDAL // 2, cy - MEDAL // 2, MEDAL, MEDAL, alt='', i=i)
    h += IMG('logo_seal.png', cx - SEAL_W // 2, cy - SEAL_H // 2, SEAL_W, SEAL_H, alt='MEYEM mührü', i=i)
    return h


def brand_row():
    return P('wm', 128, 112, 600, 'MEYEM') + P('xs', 128, 150, 640, 'Mesleki Yeterlilik ve Belgelendirme Merkezi')


# ------------------------------------------------------------------ 1 kapak
def kapak():
    h = IMG('v8_kapak_foto.jpg', HALF, 0, W - HALF, H, alt='İşinin başındaki usta ve tabletle kayıt tutan MEYEM değerlendiricisi', cls='pin ph', i=0)
    h += brand_row()
    h += P('tt', 128, 340, 760, 'Ustalığı üretim\ndurmadan belgeye\ndönüştürüyoruz.', tag='h1', i=1)
    h += P('bd', 128, 650, 640, 'MYK yetkili, TÜRKAK akrediteli mesleki yeterlilik sınav ve belgelendirme kuruluşu', i=2)
    h += P('xs', 128, FOOT_Y, 700, 'MYK YB-0079  ·  TÜRKAK AB-0126-P  ·  Kasım 2026', extra='line-height:1;')
    h += seal_group(HALF, 800, i=3)
    return h


N_KAPAK = ("MEYEM; MYK'nın yetkilendirdiği, TÜRKAK'ın akredite ettiği bir mesleki yeterlilik sınav ve belgelendirme kuruluşudur. "
           "Bugün tek bir fikri anlatacağız: ustalığı, üretimi durdurmadan belgeye dönüştürmek. Usta işini zaten bilir. "
           "Biz bu bilgiyi ulusal standartla ölçer ve MYK Mesleki Yeterlilik Belgesiyle resmî kayda geçiririz. "
           "Sunumun sonunda sizden tek bir şey isteyeceğiz: ilk toplu sınav gününü birlikte planlamak.")

# ------------------------------------------------------------------ 2 vizyon
PILLARS = ['Geniş MYK\nyetkisi', 'İşyerinde\nsınav', 'Dijital belge\nve süre takibi', 'Teşvik\ndanışmanlığı', 'Belgeden\nkariyere']


def vizyon():
    cw = (1664 - 4 * GUT) / 5
    by = 540                                   # bant merkezi
    h = TITLE('Hedefimiz işverenin belge yükünü\ntek elden taşımak.')
    h += IMG('v8_vizyon_bant.png', 128, by - 48, 1664, 96, alt='', i=1)
    for k, t in enumerate(PILLARS):
        x = round(128 + k * (cw + GUT))
        h += BOX(x, by - 14, 28, 28, WINE if k == 0 else INK, cls='pin dot rise', extra=f'--i:{min(1 + k, 4)};')
        h += P('md', x, by + 72, round(cw), t, i=min(2 + k, 4))
    return h


N_VIZYON = ("Vizyonumuz, işletmelerin mesleki yeterlilik yükümlülüklerini sektörler boyunca tek elden yöneten ortak olmak. Bunun beş parçası var. "
            "Birincisi, geniş MYK yetkisiyle zorunlu mesleklerin büyük bölümünü tek kuruluşta karşılamak. "
            "İkincisi, sınavı işyerine getirmek ve gezici sınav birimiyle her bölgeye ulaşmak. "
            "Üçüncüsü, belgeyi, geçerlilik süresini ve teşvik tarihlerini dijital olarak izlemek; uygun yeterliliklerde online sınav yapmak. "
            "Dördüncüsü, MYK belgesiyle 6111 teşvik uygunluğunu aynı dosyada ele almak. "
            "Beşincisi, belgeyi kariyere bağlamak: üniversite kariyer merkezleriyle birlikte belgeden ustalığa ve istihdama giden yolu açmak. "
            "Şimdi bu hedefin neden bugün önem kazandığına bakalım.")

# ------------------------------------------------------------------ 3 zorunluluk
def zorunluluk():
    h = TITLE("Türkiye'de 244 meslek\nartık belge istiyor.")
    h += P('nb', 120, 372, span(5), '+40', i=1)
    h += P('md', 128, 648, span(5), 'meslek 2026/1 Tebliği ile\nzorunlu listeye girdi', i=2)
    bx, bw = col(6), span(5)
    unit = bw / 244
    for k, (lab, n, z) in enumerate((('2026/1 Tebliği öncesi', 204, 0), ('2026/1 Tebliği sonrası', 244, 40))):
        y = 420 + k * 200
        h += P('bd', bx, y, bw, lab, extra='color:#00244D;', i=2 + k)
        base = round((n - z) * unit)
        h += BOX(bx, y + 56, base, 56, TINT if k == 0 else INK, cls='pin rise', extra=f'--i:{2 + k};')
        if z:
            h += BOX(bx + base, y + 56, round(z * unit), 56, WINE, cls='pin rise', extra='--i:4;')
        h += P('md', bx + round(n * unit) - 120, y + 124, 120, str(n), extra=f'text-align:right;color:{WINE if z else INK2};', i=2 + k)
    h += SOURCE('Kaynak: 2026/1 Tebliği, Resmî Gazete 33202 (23.03.2026); ÇSGB, Mart 2026')
    return h


N_ZORUNLULUK = ("Mesleki yeterlilik belgesi bazı mesleklerde artık çalışmanın koşulu. 5544 sayılı Kanun'un ek 1. maddesine göre belge zorunlu bir meslekte yalnızca belgeli kişi çalıştırılabilir. "
                "Bu liste büyüyor. 23 Mart 2026'da yayımlanan 2026/1 sayılı Tebliğ, tehlikeli ve çok tehlikeli işlerden 40 mesleği listeye ekledi ve sayı 204'ten 244'e çıktı. "
                "Belgelerin çoğu beş yıl geçerlidir. Sınav teorik ve uygulamalı olmak üzere iki aşamalıdır.")

# ------------------------------------------------------------------ 4 takvim
EVENTS = [  # (oran, tarih, metin, üstte mi)
    (0.000, '23.03.2026', '40 meslek zorunlu\nlisteye girdi', True),
    (0.307, '13.07.2026', "MEYEM'de 19 yeterlilik\ndaha aktif", False),
    (0.775, '31.12.2026', '6111 teşvikinde\nson tanımlama günü', True),
    (1.000, '23.03.2027', '40 meslekte\nbelge zorunlu', False),
]


def takvim():
    x0, x1, ly = 144, 1776, 600
    h = TITLE('Dört tarih işverenin\nönümüzdeki planını belirliyor.')
    h += BOX(x0, ly - 2, x1 - x0, 4, INK, cls='pin fadein', extra='--i:1;')
    for k, (p, d, t, up) in enumerate(EVENTS):
        x = round(x0 + p * (x1 - x0))
        last = k == len(EVENTS) - 1
        r = 18 if last else 12
        h += BOX(x - r, ly - r, 2 * r, 2 * r, WINE if last else INK, cls='pin dot rise', extra=f'--i:{1 + k};')
        w = 380
        tx = x - 16 if not last else x - w + 16
        al = 'text-align:right;' if last else ''
        dy, ty = (390, 448) if up else (650, 708)
        h += P('md', tx, dy, w, d, extra=al + (f'color:{WINE};' if last else ''), i=1 + k)
        h += P('bd', tx, ty, w, t, extra=al, i=1 + k)
    h += SOURCE('Kaynak: Resmî Gazete 33202; MYK Portal; SGK, Kasım 2026')
    return h


N_TAKVIM = ("Takvimi dört tarih belirliyor. 23 Mart 2026'da 2026/1 sayılı Tebliğ yayımlandı ve 40 meslek zorunlu listeye girdi. "
            "13 Temmuz 2026'da MYK Portal'da 19 yeterlilikte yetkimiz aktif oldu; buhar kazanı ve sıcak su kazanı operatörlüğü de bunların arasında. "
            "31 Aralık 2026, belgeli işçi alımında 6111 teşviki için işe giriş ve sisteme tanımlama yapılabilecek son gün. "
            "23 Mart 2027'de bir yıllık geçiş süresi bitiyor ve bu 40 meslekte belge zorunlu hâle geliyor. "
            "Belgelendirmeyi şimdi planlayan işveren hem teşvikten hem zamandan kazanır.")

# ------------------------------------------------------------------ 5 isyeri (fotoğraf)
ISYERI_PH = (col(5), 344, W - col(5), H - 344)   # sağa ve alta taşar


def isyeri():
    x, y, w, hh = ISYERI_PH
    h = IMG('v8_isyeri_foto.jpg', x, y, w, hh, alt='Sahada aday iskele kurarken MEYEM değerlendiricisi formla gözlem yapıyor', cls='pin ph', i=1)
    h += TITLE('Sınavı işyerine, tezgâhın\nbaşına getiriyoruz.')
    h += P('bd', 128, CONTENT_Y, span(4), 'İhtiyaç analizi, eğitim, sınav ve belge çalışanın kendi işinin başında. Türkiye genelinde.', i=1)
    h += P('md ac', 128, 790, span(4), 'Çalışan işinden ayrılmaz,\nüretim durmaz.', i=2)
    return h


N_ISYERI = ("Çalışanı sınav merkezine göndermek yerine sınavı işyerine getiriyoruz. Önce ihtiyaç analizi yerinde yapılır. "
            "Ardından eğitim, sınav ve belgelendirme çalışanın kendi işinin başında tamamlanır. İsteyen işveren için sınavı merkezimizde de planlıyoruz. "
            "Böylece çalışan işinden ayrılmaz, üretim durmaz ve iş gücü kaybı en aza iner. Bu hizmeti Türkiye genelinde veriyoruz.")

# ------------------------------------------------------------------ 6 kapsam (veri)
SCOPE_ROWS = [  # (alan, toplam, zorunlu): zorunlu paya göre sıralı
    ('İnşaat ve yapı', 13, 13), ('Makine ve üretim', 5, 5), ('Enerji ve tesisat', 5, 4),
    ('Metal ve kaynak', 3, 3), ('Taşıma ve kaldırma', 4, 2), ('Bilişim ve siber', 14, 0),
    ('Ticaret ve emlak', 6, 0), ('Yönetim ve İK', 4, 0), ('Gıda ve paketleme', 1, 0),
]
assert sum(r[1] for r in SCOPE_ROWS) == 55 and sum(r[2] for r in SCOPE_ROWS) == 27


def kapsam():
    y0, pitch, bh = 380, 62, 30
    x0 = col(3)
    unit = span(6) / 14
    h = TITLE('Dokuz alanda 55 ulusal\nyeterlilikte belge veriyoruz.')
    for k, (name, n, z) in enumerate(SCOPE_ROWS):
        ry = y0 + k * pitch
        h += P('bd', 128, ry - 4, span(3), name, extra='color:#00244D;line-height:1.2;white-space:nowrap;')
        if z:
            h += BOX(x0, ry, round(z * unit), bh, WINE)
        if n - z:
            h += BOX(x0 + round(z * unit), ry, round((n - z) * unit), bh, TINT)
        h += P('bb', x0 + round(n * unit) + 16, ry - 2, 80, str(n))
    lx = col(10)
    h += BOX(lx, y0 + 4, 24, 24, WINE)
    h += P('md', lx + 40, y0 - 8, span(2), '27 zorunlu', extra='color:#77183A;')
    h += BOX(lx, y0 + 72, 24, 24, TINT)
    h += P('md', lx + 40, y0 + 60, span(2), '28 gönüllü', extra='color:#2C4868;')
    h += P('xs', lx, y0 + 150, span(2), "+32 yeterlilik daha MYK onay sürecinde; 16'sı zorunlu kapsamda.")
    h += SOURCE('Kaynak: MYK Portal, Kasım 2026')
    return h


N_KAPSAM = ("Yetki kapsamımız MYK Portal'a göre 55 ulusal yeterlilik; bunları dokuz alanda topladık. "
            "Tamamı zorunlu kapsamda olan alanlar: inşaat ve yapıda 13 yeterlilik, ki en büyük alan bu; ayrıca metal ve kaynakta 3, makine ve üretimde 5 yeterlilik. "
            "Bir kısmı zorunlu olan alanlar: enerji ve tesisatta 5 yeterliliğin 4'ü, taşıma ve kaldırmada 4 yeterliliğin 2'si. "
            "Gönüllü kapsamdaki alanlar: bilişim ve siberde 14, ticaret ve emlakta 6, yönetim ve insan kaynaklarında 4, gıda ve paketlemede 1 yeterlilik. "
            "Toplamda 27 yeterlilik zorunlu, 28'i gönüllü kapsamda. MYK'da onay sürecinde 32 yeterlilik daha var ve bunların 16'sı zorunlu kapsamda.")

# ------------------------------------------------------------------ 7 surec
STEPS = [('İhtiyaç\nanalizi', 'Hangi çalışana\nhangi belge'), ('Planlama', 'Gün, grup, süre'),
         ('Organizasyon', 'Yer, ekipman,\ngörevli'), ('Değerlendirme', 'Teorik ve\nuygulamalı sınav'),
         ('Belgelendirme', 'Karar, belge,\nMYK kaydı')]


def surec():
    cw = (1664 - 4 * GUT) / 5
    ny = 420                                     # düğüm üst kenarı
    h = TITLE('Beş adımda ve tek muhatapla\nbelgelendiriyoruz.')
    h += BOX(160, ny + 30, round(4 * (cw + GUT)), 4, INK, cls='pin fadein', extra='--i:1;')
    for k, (name, det) in enumerate(STEPS):
        x = round(128 + k * (cw + GUT))
        last = k == len(STEPS) - 1
        h += (f'<div class="pin dot rise" style="{sty(x, ny, 64, 64)}background:{WINE if last else INK};display:flex;'
              f'align-items:center;justify-content:center;--i:{min(1 + k, 4)};">'
              f'<p class="bb" style="color:#F8F4EC;margin:0">{k + 1}</p></div>')
        h += P('md', x, ny + 104, round(cw), name, i=min(1 + k, 4))
        h += P('bd', x, ny + 230, round(cw), det, i=min(1 + k, 4))
    return h


N_SUREC = ("Süreç beş adımdır. Bir: ihtiyaç analizi; hangi çalışanın hangi belgeye ihtiyacı olduğunu birlikte çıkarırız. "
           "İki: planlama; sınav günü, grup ve süre belirlenir. Üç: organizasyon; sınav yeri, ekipman ve görevliler hazırlanır. "
           "Dört: değerlendirme; teorik ve uygulamalı sınav yapılır. Beş: belgelendirme; karar verilir, belge düzenlenir ve MYK kaydına işlenir. "
           "İşveren her adımda aynı muhatapla konuşur; süreç bu yüzden şeffaf ve izlenebilir kalır.")

# ------------------------------------------------------------------ 8 tesvik
def tesvik():
    ax0, aw = col(3), span(7)
    um = aw / 60                                 # px / ay
    h = TITLE('Belgeli istihdam prim desteğini\n54 aya kadar uzatıyor.')
    for m in (0, 12, 24, 36, 48, 60):
        x = round(ax0 + m * um)
        h += BOX(x - 1, 390, 2, 360, LINE)
        h += P('xs', x - 40, 762, 80, f'{m}', extra='text-align:center;line-height:1;')
    h += P('xs', ax0 + aw + 48, 762, 120, 'ay', extra='line-height:1;')
    rows = (('18–29 yaş erkek,\n18 yaş üstü kadın', 48), ('29 yaş üstü erkek', 24))
    for k, (lab, base) in enumerate(rows):
        y = 430 + k * 170
        h += P('bd', 128, y - 2, span(3), lab, extra='color:#00244D;line-height:1.2;', i=1 + k)
        bw = round(base * um)
        h += (f'<div class="pin rise" style="{sty(ax0, y, bw, 64)}background:{INK};display:flex;align-items:center;'
              f'justify-content:flex-end;padding-right:16px;box-sizing:border-box;--i:{1 + k};">'
              f'<p class="bb" style="color:#F8F4EC;margin:0">{base}</p></div>')
        h += BOX(ax0 + bw, y, round(6 * um), 64, WINE, cls='pin rise', extra=f'--i:{2 + k};')
        h += P('md', ax0 + bw + round(6 * um) + 20, y + 6, 200, f'{base + 6} ay', extra=f'color:{WINE};', i=2 + k)
    h += BOX(col(9), 352, 24, 24, WINE)
    h += P('xs', col(9) + 36, 352, span(3) - 36, "İŞKUR kaydıyla +6 ay", extra='line-height:1;')
    h += P('md ac', 128, 830, 300, '31.12.2026', i=3)
    h += P('bd', 128 + 300, 836, span(8), 'yeni işe alımlar için son tanımlama günü', i=3)
    h += SOURCE('Kaynak: 4447 sayılı Kanun geçici 10. madde (6111 teşviki); SGK, Kasım 2026')
    return h


N_TESVIK = ("MYK belgeli çalışanı işe alan işveren, 6111 teşviki kapsamında işveren prim payı desteğinden daha uzun süre yararlanır. "
            "18–29 yaş arası erkeklerde ve 18 yaş üstü kadınlarda bu süre 48 aydır; çalışan işe girişte İŞKUR'a kayıtlıysa 54 aya çıkar. "
            "29 yaş üstü erkeklerde süre 24 aydır; İŞKUR kaydıyla 30 aya çıkar. "
            "Yeni işe alımlar için son tanımlama günü 31 Aralık 2026. Bu tarihe kadar kapsama giren çalışanın kalan destek süresi sonraki yıllarda da sürer.")

# ------------------------------------------------------------------ 9 kazanc
GAINS = [('Uyum', 'Zorunlu meslekte ekip denetime hazır.'), ('Süreklilik', 'Sınav işyerinde; üretim sürüyor.'),
         ('Güven', 'Yetkinlik ulusal standartla kanıtlı.')]


def kazanc():
    h = IMG('v8_kazanc_foto.jpg', 0, 344, HALF - GUT, H - 344, alt='MEYEM değerlendiricisi sahada adaylara emniyet kemeri uygulamasını gösteriyor', cls='pin ph', i=1)
    h += TITLE('Belgeli ekip işverene uyum,\nsüreklilik ve güven kazandırıyor.')
    x, w = col(7), span(5)
    for k, (name, line) in enumerate(GAINS):
        y = 392 + k * 176
        if k:
            h += BOX(x, y - 30, w, 2, LINE)
        h += P('md', x, y, w, name, extra=(f'color:{WINE};' if k == 0 else ''), i=1 + k)
        h += P('bd', x, y + 62, w, line, i=1 + k)
    return h


N_KAZANC = ("Bütün bunlar işveren için üç kazanca dönüşüyor. Uyum: zorunlu meslekte çalışan ekip belgeli olur ve denetime hazırdır. "
            "Süreklilik: sınav işyerinde yapıldığı için üretim sürer, çalışan işinden ayrılmaz. "
            "Güven: çalışanın yetkinliği ulusal standartla ölçülür ve herkesin doğrulayabileceği bir kayda geçer. "
            "Bunlara bir önceki slayttaki prim desteği de eklenir.")

# ------------------------------------------------------------------ 10 kanit
def kanit():
    h = TITLE('Belgemiz resmî yetkiye ve\non yılı aşan sahaya dayanıyor.')
    h += P('nb', 120, 372, span(7), '50.000+', i=1)
    h += P('md', 128, 648, span(7), 'belgelendirilmiş aday, 10+ yılda', i=2)
    h += BOX(128, 736, span(6), 2, LINE)
    h += P('bd', 128, 760, span(7), 'MYK yetki no [[YB-0079]]', extra='color:#00244D;', i=3)
    h += P('bd', 128, 810, span(7), 'TÜRKAK akreditasyon no [[AB-0126-P]] · TS EN ISO/IEC 17024', extra='color:#00244D;', i=3)
    h += seal_group(col(9) + 120, 600, i=2)
    h += SOURCE('Kaynak: MYK Portal; TÜRKAK; MEYEM, Kasım 2026')
    return h


N_KANIT = ("Belgenin değeri arkasındaki yetkiden gelir. MEYEM, MYK'nın YB-0079 numarasıyla yetkilendirdiği bir belgelendirme kuruluşudur. "
           "TÜRKAK, personel belgelendirmede TS EN ISO/IEC 17024 standardına göre bizi AB-0126-P numarasıyla akredite etti. "
           "Bu kayıtları herkes açık kaynaklardan doğrulayabilir. On yılı aşkın sürede 50 binden fazla adayı belgelendirdik. "
           "Verdiğimiz her belge MYK kaydına işlenir.")

# ------------------------------------------------------------------ 11 isbirligi
MODELS = [('A', 'Başlangıç', 'Bilgilendirme ve\nyönlendirme'), ('B', 'Sonraki adım', 'Toplu sınav\ngünleri'),
          ('C', 'Kalıcı yapı', 'Ortak yapı\nya da şube')]


def isbirligi():
    h = TITLE('Her bölgeye uyan üç\niş birliği yolu sunuyoruz.')
    for k, (L, tag, name) in enumerate(MODELS):
        x, w = col(4 * k), span(4)
        hot = k == 1
        h += BOX(x, 372, w, 4 if hot else 2, WINE if hot else INK, cls='pin fadein', extra=f'--i:{1 + k};')
        h += P('xs', x, 400, w, tag, extra=('color:#77183A;font-weight:700;' if hot else ''), i=1 + k)
        h += P('tt', x, 444, w, L, extra=(f'color:{WINE};' if hot else ''), i=1 + k)
        h += P('md', x, 560, w, name, i=1 + k)
    h += BOX(128, 760, 1664, 2, LINE)
    h += P('md', 128, 790, 1664, "Her yolda sınavı MEYEM yapar, belgeyi MEYEM verir.", i=4)
    return h


N_ISBIRLIGI = ("Her bölgeye uyan üç model var. Model A, bilgilendirme ve yönlendirme: oda, OSB ya da dernek üyelerine duyuru ve seminer yapılır; firmalar MEYEM'e yönlendirilir. "
               "Model B, toplu sınav günleri: ortak bir noktada takvimli sınav günleri düzenlenir; başvuruyu firma yapar, sınavı MEYEM yürütür. "
               "Model C, ortak yapı ya da şube: bölgede kalıcı bir sınav noktası kurulur. "
               "Başlangıç Model A ile yapılır, ilk toplu sınav günüyle Model B'ye geçilir. "
               "MYK yetkisi devredilemez; bu yüzden hangi yol seçilirse seçilsin sınavı yapan ve belgeyi veren kuruluş MEYEM'dir.")

# ------------------------------------------------------------------ 12 cagri
ASKS = ['Çalışan ve\nmeslek listesi', 'İhtiyaç analizi\ngörüşmesi', 'İlk toplu\nsınav günü']


def cagri():
    h = TITLE('İlk toplu sınav gününü\nbirlikte planlayalım.')
    for k, t in enumerate(ASKS):
        x, w = col(4 * k), span(4)
        h += P('tt', x, 380, 120, str(k + 1), extra=f'color:{WINE};', i=1 + k)
        h += P('md', x, 500, w, t, i=1 + k)
    h += BOX(128, 740, 1664, 2, INK)
    h += P('md', 128, 770, 1664, "Hedef: [[23.03.2027'den önce]] belgeli ekipler.", i=4)
    h += SOURCE('Kaynak: 2026/1 Tebliği, Resmî Gazete 33202')
    return h


N_CAGRI = ("Sizden tek bir adım istiyoruz: ilk toplu sınav gününü birlikte planlamak. Önce çalışan ve meslek listesini alıyoruz. "
           "Ardından bir ihtiyaç analizi görüşmesiyle hangi çalışanın hangi belgeye ihtiyacı olduğunu çıkarıyoruz. "
           "Sonra ilk toplu sınav gününün tarihini birlikte belirliyoruz. Hedefimiz, ekiplerinizin 23 Mart 2027'den önce belgeli olması.")

# ------------------------------------------------------------------ 13 kapanis
def kapanis():
    h = IMG('v8_kapanis_foto.jpg', HALF, 0, W - HALF, H, alt='MEYEM uzmanı bir ekibe sunum yapıyor', cls='pin ph', i=0)
    h += brand_row()
    h += P('tt', 128, 230, 760, 'Ustalığı belgeye\ndönüştürmek için\nhazırız.', i=1)
    h += P('md ac', 128, 520, 760, 'Ustalık sizden, mühür bizden.', i=2)
    h += P('bd', 128, 610, 680, 'meyem.com.tr\nbelge@meyem.com.tr\n0 (505) 024 17 24  ·  0 (553) 908 92 33', extra='color:#00244D;', i=3)
    h += IMG('v8_qr.png', 128, 772, 140, 140, alt='meyem.com.tr adresine giden QR kod', i=3)
    h += P('xs', 292, 808, 400, 'Tarayın:\nmeyem.com.tr', i=3)
    h += P('xs', 128, FOOT_Y, 700, 'MYK YB-0079  ·  TÜRKAK AB-0126-P  ·  Yenişehir / Mersin', extra='line-height:1;')
    h += seal_group(HALF, 800, i=4)
    return h


N_KAPANIS = ("Teşekkür ederiz. Bir sonraki adım ihtiyaç analizi görüşmesi: çalışan listesi ve meslek bilgisi geldiğinde sınav takvimini birlikte planlarız. "
             "Bize meyem.com.tr adresinden, belge@meyem.com.tr e-posta adresinden ya da slayttaki telefonlardan ulaşabilirsiniz. "
             "QR kod doğrudan web sitemize gider. Son sözümüz açılıştakiyle aynı: ustalık sizden, mühür bizden.")

SLIDES_V8 = [
    ('kapak', kapak, N_KAPAK, 'cover'),
    ('vizyon', vizyon, N_VIZYON, 's2'),
    ('zorunluluk', zorunluluk, N_ZORUNLULUK, ''),
    ('takvim', takvim, N_TAKVIM, ''),
    ('isyeri', isyeri, N_ISYERI, 'phs'),
    ('kapsam', kapsam, N_KAPSAM, ''),
    ('surec', surec, N_SUREC, ''),
    ('tesvik', tesvik, N_TESVIK, ''),
    ('kazanc', kazanc, N_KAZANC, ''),
    ('kanit', kanit, N_KANIT, ''),
    ('isbirligi', isbirligi, N_ISBIRLIGI, ''),
    ('cagri', cagri, N_CAGRI, 's2'),
    ('kapanis', kapanis, N_KAPANIS, 'closing'),
]

SECTIONS = {
    's1': {'description': 'Vizyon: ustalığı üretim durmadan belgeye dönüştürmek', 'start': 'kapak'},
    's2': {'description': 'Neden şimdi: zorunluluk büyüyor ve takvim işliyor', 'start': 'zorunluluk'},
    's3': {'description': 'Ne yapıyoruz: işyerinde sınav, kapsam ve süreç', 'start': 'isyeri'},
    's4': {'description': 'İşverene değeri: teşvik ve üç kazanç', 'start': 'tesvik'},
    's5': {'description': 'Kanıt ve iş birliği', 'start': 'kanit'},
    's6': {'description': 'Çağrı ve iletişim', 'start': 'cagri'},
}
