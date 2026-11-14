import os
"""v2: yalnız MYK belgelendirme. Revize edilen slaytlar (kapak, imza, söz, takvim, alan, yaprak, durak, halka, yol, kapanış)."""
import json, math
from d_common import *
import d_slides1 as S1
import d_slides2 as S2
import d_slides3 as S3

SCOPE = json.load(open(os.path.join(os.path.dirname(M2), 'data', 'meyem_scope.json')))

RULES = [
    ('insaat', ['Ahşap Kalıpçı', 'Alçı Levha', 'Alçı Sıva', 'Betonarme', 'Duvarcı', 'Isı Yalıtımcısı', 'İnşaat Boyacısı', 'İnşaat İşçisi', 'İskele', 'Panel Kalıpçı', 'PVC Doğrama', 'Seramik', 'Sıvacı']),
    ('metal', ['Çelik Kaynakçısı', 'Direnç Kaynak', 'Endüstriyel Boru']),
    ('makine', ['Makine Bakımcı', 'Makine Montajcısı', 'Elektro-Mekanik', 'Tornacı']),
    ('enerji', ['Buhar Kazanı', 'Sıcak Su Kazanı', 'Sıhhi Tesisatçı', 'Elektrik Tesisatçısı', 'İşletme Elektrik']),
    ('tasima', ['Köprülü Vinç', 'Endüstriyel Taşımacı', 'Servis Aracı', 'Motosikletli Kurye']),
    ('gida', ['Dolum/Ambalajlama']),
    ('ticaret', ['BT Satış', 'Kasiyer', 'Motorlu Kara', 'Satış Danışmanı', 'Satış Sorumlusu', 'Emlak']),
    ('yonetim', ['İnsan Kaynakları', 'Proje Yöneticisi']),
]
GROUPS = [('insaat', 'İnşaat ve yapı'), ('metal', 'Metal ve kaynak'), ('makine', 'Makine ve üretim'), ('enerji', 'Enerji ve tesisat'),
          ('tasima', 'Taşıma ve kaldırma'), ('gida', 'Gıda ve paketleme'), ('ticaret', 'Ticaret ve emlak'),
          ('yonetim', 'Yönetim ve İK'), ('bilisim', 'Bilişim ve siber')]


def group_of(n):
    for g, keys in RULES:
        if any(k in n for k in keys):
            return g
    return 'bilisim'


CNT = {k: [0, 0] for k, _ in GROUPS}      # [yeterlilik, zorunlu]
for x in SCOPE:
    g = group_of(x['n'])
    CNT[g][0] += 1
    CNT[g][1] += 1 if x['z'] != 'gönüllü' else 0
assert sum(v[0] for v in CNT.values()) == 55 and sum(v[1] for v in CNT.values()) == 27
N_NEW = sum(1 for x in SCOPE if x['date'] == '13/07/2026')       # 13.07.2026'da aktifleşen yeterlilik sayısı

FILL = []                                  # yaprak dizisi: alan sırası, her alanda önce zorunlu
GSTART = {}
for g, _ in GROUPS:
    GSTART[g] = len(FILL)
    n, z = CNT[g]
    FILL += [True] * z + [False] * (n - z)


# ====================================================================== 1 KAPAK
def html_kapak():
    cx, cy = 1430, 548
    h = BK('kapak')
    h += IMG('logo_seal.png', 128, 92, 86, 84, 'MEYEM mührü')
    h += P('t1', 234, 96, 700, 'MEYEM', 40, extra='letter-spacing:1px;', i=0)
    h += P('sm', 234, 142, 760, 'Mesleki Yeterlilik ve Belgelendirme Merkezi', 26, i=0)
    h += TITLE('Ustalığın', 'resmî adı.', 128, 316, 1000, 168, 200, i0=1)
    h += P('lead', 128, 744, 760, 'Mesleki yeterlilik sınavı ve belgelendirmesi; Türkiye’nin her yerinde, işyerinizde.', 34, i=3)
    h += CHIPS(['MYK YB-0079', 'TÜRKAK AB-0126-P'], 128, 920)
    h += IMG('cover_photo.png', cx - 250, cy - 250, 500, 500, 'Güvenlik ekipmanlı iki saha çalışanı, biri tablet kullanıyor', i=2)
    h += P('mono', 128, 992, 600, 'KASIM 2026', extra='line-height:1;')
    return h


NOTES_KAPAK = ('Açılış cümlesi: MEYEM, TÜRKAK akreditasyonlu ve MYK yetkili bir sınav ve belgelendirme kuruluşudur. '
               'Fotoğraftaki iki kişi sahayı anlatıyor: biri tezgâhta işini yapıyor, diğeri kaydı tutuyor. Biz de tam bu ikilinin arasındayız: ustalığı resmî kayda geçiriyoruz. '
               'Başlık sözü bu yüzden “ustalığın resmî adı”: usta zaten bilir, biz bunu MYK Mesleki Yeterlilik Belgesi ile belgelendiririz. '
               'Alt satırdaki iki kod, MYK yetki numarası ve TÜRKAK akreditasyon numarasıdır.')


# ====================================================================== 2 İMZA
def html_imza():
    cy = 548
    h = BK('imza')
    h += P('k', 128, 112, 600, 'YETKİ', i=0)
    h += TITLE('İki resmî imza,', 'tek mühür.', 128, 156, 740, 88, 112, i0=0)
    h += P('lead', 128, 392, 700, 'Belgenin değeri, arkasındaki yetkiden gelir. MYK yetkisi ve TÜRKAK akreditasyonu iki resmî dayanak; üçüncüsü MEYEM mührü.', 33, i=2)
    rows = [('MYK YETKİ NO', 'YB-0079'), ('TÜRKAK AKREDİTASYON NO', 'AB-0126-P'),
            ('STANDART', 'TS EN ISO/IEC 17024'), ('YETKİ KAPSAMI', '55 ULUSAL YETERLİLİK')]
    y0 = 648
    for n, (a, b) in enumerate(rows):
        y = y0 + n * 56
        h += RULE(128, y, 720, 1.2, '#00244D', 0.55)
        h += P('mono', 128, y + 14, 380, a, extra='line-height:1;')
        h += P('mono', 480, y + 14, 368, b, extra='line-height:1;text-align:right;color:#77183A;font-weight:700;')
    h += RULE(128, y0 + 224, 720, 1.2, '#00244D', 0.55)
    h += P('mono', 128, 906, 760, '10+ YIL · 50.000+ BELGELENDİRİLMİŞ ADAY', extra='line-height:1;')
    h += IMG('logo_myk.png', S1.IMZA_L - 82, cy - 106, 156, 202, 'MYK logosu ve YB-0079 yetki numarası', i=1)
    h += IMG('logo_turkak.png', S1.IMZA_R - 70, cy - 106, 150, 203, 'TÜRKAK logosu ve AB-0126-P akreditasyon numarası', i=2)
    h += IMG('logo_seal.png', S1.IMZA_C - 96, cy - 94, 192, 188, 'MEYEM mührü', i=3)
    h += P('sm', S1.IMZA_L - 190, 836, 380, '<b>MYK</b> · Yetkilendirilmiş Belgelendirme Kuruluşu', 26, extra='text-align:center;', raw=True)
    h += P('sm', S1.IMZA_R - 190, 836, 380, '<b>TÜRKAK</b> · Personel belgelendirme akreditasyonu', 26, extra='text-align:center;', raw=True)
    h += FOOT()
    return h


NOTES_IMZA = ('Belgenin değeri arkasındaki yetkiden gelir. Soldaki daire MYK yetkisidir: Yetkilendirilmiş Belgelendirme Kuruluşu, YB-0079. '
              'Sağdaki daire TÜRKAK akreditasyonudur: personel belgelendirmede TS EN ISO/IEC 17024, AB-0126-P. İkisinin kesiştiği yerde MEYEM mührü durur. '
              'Yetki kapsamımız MYK Portal kaydına göre 55 ulusal yeterliliği içerir. Bu kayıtlar herkesin açık kaynaklardan doğrulayabileceği kayıtlardır.')


# ====================================================================== 3 SÖZ
def html_soz():
    h = BK('soz')
    h += P('k', 128, 100, 600, 'NEDEN BELGE', i=0)
    h += TITLE('Bir belgenin', 'dört sözü.', 128, 144, 900, 92, 112, i0=0)
    h += P('lead', 1020, 130, 772, 'Mesleki yeterlilik belgesi; çalışanın yetkinliğini, işverenin güvencesini ve sektörün uyumunu aynı kayda bağlar.', 33, i=2)
    photos = ['soz_a1.png', 'soz_a2.png', 'soz_a3.png']
    alts = ['Koruyucu maskeyle kaynak yapan usta, çevresinde kıvılcımlar', 'Birbirine kenetlenen iki el: güven', 'Şantiyede plan ve kontrol listesi üzerinde yazı yazan el']
    for i, x in enumerate(S1.ARCH_X[:3]):
        h += IMG(photos[i], x, S1.ARCH_Y, S1.ARCH_W, S1.ARCH_H, alts[i], i=i + 1)
    items = [('I', 'Yetkinlik', 'Bilgi ve beceri ulusal standartla ölçülür.'),
             ('II', 'Güven', 'Doğrulanabilir, tarafsız güvence.'),
             ('III', 'Uyum', 'Meslek kodu, görev ve belge birbirini tutar.'),
             ('IV', 'Avantaj', 'Uygun şartlarda daha uzun prim desteği.')]
    for i, (rn, t, b) in enumerate(items):
        x = S1.ARCH_X[i]
        h += P('num', x, 800, 70, rn, 52, extra='font-style:italic;')
        h += P('ct', x + 76, 806, 260, t, 40)
        h += P('sm', x, 866, 330, b, 26)
    h += FOOT()
    return h


# ====================================================================== 5 TAKVİM
def html_takvim():
    h = BK('takvim')
    h += P('k', 128, 100, 700, 'ZORUNLULUK TAKVİMİ', i=0)
    h += TITLE('Liste büyüyor,', 'takvim işliyor.', 128, 144, 1000, 92, 112, i0=0)
    h += P('num', 1380, 92, 412, '+40', 196, extra='text-align:right;', i=2)
    h += P('sm', 1380, 308, 412, 'meslek, 2026/1 Tebliği ile zorunlu listeye eklendi', 26, extra='text-align:right;', i=3)
    ev = [('23.03.2026', '2026/1 Tebliği', '40 meslek zorunlu listesine eklendi. Resmî Gazete 33202.'),
          ('13.07.2026', 'Kapsam 55’e çıktı', f'MYK Portal’da {N_NEW} yeterlilikte yetki aktif oldu.'),
          ('31.12.2026', 'Teşvikte son gün', 'Belgeli işçi alımında işe giriş ve sisteme tanımlama günü.'),
          ('23.03.2027', 'Geçiş süresi biter', '2026/1 kapsamındaki 40 meslekte belge zorunlu olur.')]
    for i, (dt, t, b) in enumerate(ev):
        x = S2.TK_X[i]
        h += P('numb', x, 424, 380, dt, 54, i=2 + i)
        h += P('ct', x, 774, 340, t, 34, i=2 + i)
        h += P('sm', x, 826, 340, b, 26, i=2 + i)
    h += FOOT()
    return h


NOTES_TAKVIM = ('Dört tarih yeter. 23 Mart 2026’da 2026/1 sayılı Tebliğ yayımlandı: 40 meslek zorunlu listesine eklendi. '
                f'13 Temmuz 2026’da {N_NEW} yeterlilikte yetkimiz MYK Portal’da aktif hale geldi ve kapsamımız 55 ulusal yeterliliğe ulaştı. '
                '31 Aralık 2026, 6111 teşvikinde belgeli işçi alımı için son tanımlama günü. '
                '23 Mart 2027’de geçiş süresi bitiyor ve 2026/1 kapsamındaki 40 meslekte belge zorunlu oluyor. '
                'Yani firmalar için pencere açık ve takvim işliyor: belgelendirmeyi şimdi planlayan, hem teşvikten hem zamandan kazanır.')


# ====================================================================== 6 ALAN (5x2 kare karo)
TX = [128, 470, 812, 1154, 1496]
TY = [348, 664]
TS = 288


def art_alan():
    s = paper('d')
    s += wave_lines(100, 1820, 330, 962, n=38, amp=10, wl=430, c=INK, op=0.08, sw=0.8, delta=0.16)
    s += rosette_lace(1975, -70, 300, n=48, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    for k in range(9):
        r, c = divmod(k, 5)
        x, y = TX[c], TY[r]
        s += f'<rect x="{x + 12}" y="{y + 12}" width="{TS}" height="{TS}" fill="none" stroke="{WINE}" stroke-width="1.3" stroke-opacity="0.85"/>'
    return s, ''


def html_alan():
    h = BK('alan')
    h += P('k', 128, 76, 600, 'KAPSAM', i=0)
    h += TITLE('Dokuz alan,', 'tek çatı.', 128, 112, 800, 80, 98, i0=0)
    h += P('lead', 1000, 112, 792, 'MYK Portal kaydındaki 55 yeterlilik, dokuz meslek alanında toplanıyor. Çubuk, alandaki zorunlu payı gösterir.', 33, i=2)
    alts = {'insaat': 'Güvenlik yeleği ve bareti ile şantiyede çalışan işçi', 'metal': 'Atölyede maskeyle kaynak yapan usta',
            'makine': 'Torna tezgâhında talaş kaldıran kesici uç', 'enerji': 'Bareti ve gözlüğüyle prizde çalışan elektrikçi',
            'tasima': 'Depoda paletli yük taşıyan forklift operatörü', 'gida': 'Gıda üretim hattında şişelenen ürünler',
            'ticaret': 'Cam cepheli kurumsal bina', 'yonetim': 'Beş kişilik kurumsal ekip', 'bilisim': 'Ağ cihazına bağlanan kablolar'}
    for k, (g, name) in enumerate(GROUPS):
        r, c = divmod(k, 5)
        x, y = TX[c], TY[r]
        n, z = CNT[g]
        h += IMG(f'tile_{g}.jpg', x, y, TS - 12, TS - 12, alts[g], extra='border:6px solid #FFFFFF;box-shadow:0 12px 26px rgba(0,36,77,.18);', cls='pin ph', i=2 + k)
        by = y + TS - 6 - 90
        h += f'<div class="pin" style="left:{x + 6}px;top:{by}px;width:{TS - 12}px;height:90px;background:rgba(255,255,255,.93)"></div>'
        h += P('ct', x + 18, by + 8, TS - 36, name, 26, extra='line-height:1.15;font-weight:700;')
        h += P('mono', x + 18, by + 42, TS - 36, f'{n} · {z} ZORUNLU', extra='line-height:1;font-size:24px;letter-spacing:1px;')
        h += RULE(x + 18, by + 76, TS - 36, 6, '#DAC1CA', 1.0)
        if z:
            h += RULE(x + 18, by + 76, round((TS - 36) * z / n), 6, '#77183A', 1.0)
    x, y = TX[4], TY[1]
    h += P('num', x, y + 4, 288, '55', 150)
    h += P('sm', x, y + 162, 288, 'yeterlilik', 26)
    h += f'<div class="pin" style="left:{x}px;top:{y + 206}px;width:46px;height:14px;border-radius:7px;background:#77183A"></div>'
    h += P('sm', x + 60, y + 196, 228, '27 zorunlu', 26)
    h += f'<div class="pin" style="left:{x}px;top:{y + 250}px;width:43px;height:11px;border-radius:7px;border:1.5px solid #00244D"></div>'
    h += P('sm', x + 60, y + 240, 228, '28 gönüllü', 26)
    h += FOOT()
    return h


NOTES_ALAN = ('Dokuz alan, tek çatı. Bu dokuz alan, MYK Portal’daki 55 ulusal yeterliliğin meslek ailelerine göre toplanmış halidir; tek bir yeterlilik dışarıda kalmıyor. '
              'Üst sıra sahanın zorunlu meslekleri: inşaat ve yapı on üç, metal ve kaynak üç, makine ve üretim beş, enerji ve tesisat beş, taşıma ve kaldırma dört yeterlilik. '
              'Alt sıra: gıda ve paketleme bir, ticaret ve emlak altı, yönetim ve insan kaynakları dört, bilişim ve siber on dört yeterlilik; bunlar gönüllü kapsamda. '
              'Kartlardaki çubuk, alandaki zorunlu payı gösterir. Toplamda yirmi yedi yeterlilik zorunlu, yirmi sekizi gönüllü. '
              'Konuşmanızı müşterinin mesleğinin durduğu karede tutun.')


# ====================================================================== 7 YAPRAK (55 yaprak, alanlara göre)
YP_C = (1250, 540)
YP_R0, YP_R1 = 125, 360


def art_yaprak():
    cx, cy = YP_C
    s = paper('b')
    s += rosette_lace(cx, cy, 440, n=72, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.13, sw=0.7)
    s += petal_ring(cx, cy, YP_R0, YP_R1, 55, set(i for i, f in enumerate(FILL) if f), fill=WINE, stroke=INK, accent=None, wid=1.12)
    s += f'<circle cx="{cx}" cy="{cy}" r="{YP_R0 - 10}" fill="{PAPER_B}"/>'
    s += circle(cx, cy, YP_R0 - 10, INK, 1.2, 0.7) + circle(cx, cy, YP_R0 - 22, WINE, 0.9, 0.55)
    # alan sınırları
    for g, _ in GROUPS:
        a = -math.pi / 2 + 2 * math.pi * (GSTART[g] - 0.5) / 55
        s += line_path(f'M{f1(cx + (YP_R1 + 12) * math.cos(a))} {f1(cy + (YP_R1 + 12) * math.sin(a))}L{f1(cx + (YP_R1 + 34) * math.cos(a))} {f1(cy + (YP_R1 + 34) * math.sin(a))}', INK, 1.4, 0.8)
    s += ticks(cx, cy, YP_R1 + 40, 110, 5, 10, 5, INK, 0.9, 0.35)
    return s, ''


def html_yaprak():
    cx, cy = YP_C
    h = BK('yaprak')
    h += P('k', 128, 100, 700, 'YETKİ KAPSAMI', i=0)
    h += TITLE('55 yaprak,', 'tek rozet.', 128, 144, 700, 96, 116, i0=0)
    h += P('lead', 128, 372, 640, 'Her yaprak bir ulusal yeterlilik; dolu yapraklar zorunlu, boş yapraklar gönüllü kapsamda.', 32, i=2)
    y0 = 536
    for k, (g, name) in enumerate(GROUPS):
        y = y0 + 42 * k
        n, z = CNT[g]
        h += RULE(128, y, 620, 1.0, '#00244D', 0.35)
        h += P('mono', 128, y + 9, 44, str(k + 1), extra='color:#77183A;font-weight:700;line-height:1;')
        h += P('sm', 176, y + 6, 330, name, 26, extra='line-height:1.15;', i=3)
        h += P('mono', 500, y + 9, 248, f'{n} · {z} ZORUNLU', extra='line-height:1;text-align:right;font-size:24px;letter-spacing:1px;')
    h += RULE(128, y0 + 42 * 9, 620, 1.0, '#00244D', 0.35)
    h += P('mono', 128, 948, 700, 'MYK ONAY SÜRECİNDE 32 YETERLİLİK DAHA', extra='line-height:1;')
    for k, (g, name) in enumerate(GROUPS):
        n, z = CNT[g]
        mid = GSTART[g] + (n - 1) / 2.0
        a = -math.pi / 2 + 2 * math.pi * mid / 55
        r = YP_R1 + 64
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        h += P('mono', int(x - 19), int(y - 19), 38, str(k + 1),
               extra='text-align:center;line-height:38px;height:38px;border-radius:19px;background:#77183A;color:#FFFFFF;font-weight:700;letter-spacing:0;')
    h += P('num', cx - 140, cy - 100, 280, '55', 140, extra='text-align:center;', i=2)
    h += P('mono', cx - 100, cy + 42, 200, 'YETERLİLİK', extra='text-align:center;letter-spacing:1px;line-height:1;')
    h += FOOT()
    return h


NOTES_YAPRAK = ('Rozetteki her yaprak bir ulusal yeterlilik; elli beş yaprak, dokuz alana bölünmüş durumda. Numaralar alanları gösterir: '
                'bir inşaat ve yapı, iki metal ve kaynak, üç makine ve üretim, dört enerji ve tesisat, beş taşıma ve kaldırma, altı gıda ve paketleme, yedi ticaret ve emlak, sekiz yönetim ve insan kaynakları, dokuz bilişim ve siber. '
                'Dolu yirmi yedi yaprak zorunlu kapsamdaki yeterlilikler, boş yirmi sekiz yaprak gönüllü olanlar. '
                'Rozetin ilk yarısı sahanın zorunlu meslekleri, ikinci yarısı bilişim, ticaret ve yönetim gibi gönüllü alanlar. '
                'MYK’da onay sürecinde olan otuz iki yeterlilik daha var; kapsam büyüdükçe rozet büyür ve müşterinin tek muhatabı aynı kalır.')


# ====================================================================== 9 DURAK
def html_durak():
    h = BK('durak')
    h += P('k', 128, 76, 600, 'SÜREÇ', i=0)
    h += TITLE('Beş durak,', 'bir belge.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Tek muhatapla, ihtiyaç analizinden belgelendirmeye.', 34, i=2)
    st = [('İhtiyaç analizi', 'Hangi çalışan, hangi belge?'), ('Planlama', 'Sınav günü, grup ve süre.'),
          ('Organizasyon', 'Sınav yeri, ekipman, görevliler.'), ('Değerlendirme', 'Teorik ve uygulamalı sınav.'),
          ('Belgelendirme', 'Karar, belge ve MYK kaydı.')]
    alts = ['İşyerinde tablet üzerinden ihtiyaç analizi yapan iki uzman', 'Planlama notlarını yazan el ve dizüstü bilgisayar',
            'Baretli çalışan grubu, sınav günü organizasyonu', 'Test cevap kâğıdı ve kurşun kalem: sınav değerlendirme', 'MEYEM mührü: belgelendirme']
    for k, x in enumerate(S3.DK_X):
        y = S3.DK_Y
        h += P('mono', x - 140, y - 186, 280, f'ADIM 0{k + 1}', extra='text-align:center;color:#77183A;font-weight:700;', i=2 + k)
        h += IMG(f'step_d{k + 1}.png', x - 100, y - 100, 200, 200, alts[k], i=2 + k)
        h += P('ct', x - 140, y + 134, 280, st[k][0], 34, extra='text-align:center;', i=2 + k)
        h += P('sm', x - 140, y + 184, 280, st[k][1], 26, extra='text-align:center;', i=2 + k)
    h += P('mono', 128, 908, 1664, 'MYK YETKİLİ KURULUŞ · UYGUN YETERLİLİKLERDE ONLINE SINAV · ŞEFFAF · UZMAN · GÜVENİLİR', extra='line-height:1;')
    h += FOOT()
    return h


# ====================================================================== 12 HALKA
def html_halka():
    h = BK('halka')
    h += P('k', 128, 76, 600, 'VİZYON', i=0)
    h += TITLE('Tek çatı,', 'beş halka.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Mavi yaka ve beyaz yaka, belge ve teşvik, sınav ve kariyer: tek muhatap, tek takvim.', 33, i=2)
    items = [('Yetki', 'Geniş MYK yetkisi'), ('Saha', 'İşyerinde sınav'), ('Dijital', 'Belge ve süre takibi'),
             ('Teşvik', '6111 SGK danışmanlığı'), ('Kariyer yolu', 'Belgeden istihdama')]
    for k, ((t, d_), x, y) in enumerate(zip(items, S3.HK_X, S3.HK_Y)):
        h += P('num', x - 80, y - 82, 160, ['I', 'II', 'III', 'IV', 'V'][k], 60, extra='text-align:center;font-style:italic;', i=2 + k)
        h += P('ct', x - 110, y - 8, 220, t, 36, extra='text-align:center;', i=2 + k)
        h += P('sm', x - 150, y + 212, 300, d_, 26, extra='text-align:center;', i=2 + k)
    h += FOOT()
    return h


NOTES_HALKA = ('Vizyon beş halkadır ve halkalar birbirine geçer. Yetki: zorunlu mesleklerde geniş MYK yetkisi. '
               'Saha: gezici sınav birimiyle işyerinde sınav. Dijital: belge, süre ve teşvik takibi, uygun yeterliliklerde online sınav. '
               'Teşvik: MYK belgesi ile 6111 SGK teşvik uygunluk analizi ve danışmanlık tek dosyada. Kariyer yolu: belgeden ustalığa ve istihdama, üniversite kariyer merkezi iş birliğiyle. '
               'Hedefimiz yalnız sınav yapmak değil; işletmenin mesleki yeterlilik yükümlülüklerini sektörler boyunca yöneten çözüm ortağı olmak.')


# ====================================================================== 13 YOL
def art_yol():
    d = iris_defs('iris', 0, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('b')
    s += rosette_lace(1990, -100, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    for x in S3.YL_X:
        s += arch_outline(x, S3.YL_Y, 248, 300, WINE, 1.4, 0.9, off=12)
        s += arch_outline(x, S3.YL_Y, 248, 300, INK, 0.8, 0.5, off=21)
    s += braid(120, 1740, 930, amp=12, wl=360, n=12, spread=2.8, delta=0.28, c1='url(#iris)', c2=WINE, op=0.6)
    s += f'<circle cx="1800" cy="930" r="26" fill="{PAPER_B}"/>' + circle(1800, 930, 26, WINE, 3, 1) + circle(1800, 930, 36, INK, 1, 0.55) + circle(1800, 930, 7, WINE, 0, 0, fill=WINE)
    return s, d


def html_yol():
    h = BK('yol')
    h += P('k', 128, 76, 600, 'İŞ BİRLİĞİ MODELİ', i=0)
    h += TITLE('Üç yol,', 'tek standart.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Her bölgeye uyan üç model; hangisi seçilirse seçilsin sınav standardı aynı kalır.', 33, i=2)
    ms = [('A', 'Bilgilendirme ve yönlendirme', 'Sanayi odası, OSB veya dernek üyelerine duyuru ve seminer; firmalar MEYEM’e yönlendirilir.', 'model_a.png', 'Büyük bir salonda perdeye bakan seminer katılımcıları'),
          ('B', 'Toplu sınav günleri', 'Ortak noktada takvimli sınav günleri; başvuruyu firma yapar, sınavı MEYEM yürütür.', 'model_b.png', 'İşyerinde grup eğitimi ve sınav oturumu'),
          ('C', 'Ortak yapı veya şube', 'Bölgede MEYEM şubesi ya da ortak yapı; sınav ve belge MEYEM adına yürür.', 'arch_building.png', 'MEYEM Belgelendirme Merkezi binası')]
    for k, ((L, t, b, ph, alt), x) in enumerate(zip(ms, S3.YL_X)):
        h += IMG(ph, x, S3.YL_Y, 248, 300, alt, i=2 + k)
        h += P('num', x + 276, S3.YL_Y - 6, 120, L, 84, extra='font-style:italic;', i=2 + k)
        h += P('ct', x + 276, S3.YL_Y + 84, 250, t, 32, extra='line-height:1.1;', i=2 + k)
        h += P('sm', x + 276, S3.YL_Y + 190, 250, b, 24, extra='line-height:1.3;', i=2 + k)
    h += P('ct', 128, 800, 1500, 'Hangi yol seçilirse seçilsin, sınavı yapan ve belgeyi veren kuruluş MEYEM’dir.', 34, extra='line-height:1.2;font-weight:600;', i=6)
    h += FOOT()
    return h


NOTES_YOL = ('Üç model, tek standart. Model A bilgilendirme ve yönlendirme: sanayi odası, OSB yönetimi ya da dernek üyelerine duyuru ve seminer yapılır, firmalar MEYEM’e yönlendirilir. '
             'Model B toplu sınav günleri: ortak sınav noktasında takvimli sınav günleri; firmalar başvurusunu yapar, MEYEM sınavı yürütür. '
             'Model C ortak yapı ya da şube: bölgede MEYEM şubesi veya ortak yapı kurulur. Başlangıç Model A ile, ilk toplu sınav günüyle Model B’ye geçilir. '
             'Alttaki cümle üç modelin ortak sözüdür: MYK yetkisi MEYEM’dedir; bu yüzden hangi yol seçilirse seçilsin sınavı yapan ve belgeyi veren kuruluş MEYEM olur. '
             'Firma açısından anlamı şu: her bölgede aynı sınav kuralı, aynı belge, aynı resmî kayıt.')


# ====================================================================== 14 KAPANIŞ
def html_kapanis():
    cx, cy = S3.KC
    h = BK('kapanis')
    h += IMG('close_photo.png', cx - 236, cy - 236, 472, 472, 'MEYEM uzmanı, katılımcı grubuna sunum yapıyor', i=1)
    h += P('k', 900, 100, 700, 'BAŞLAYALIM', i=0)
    h += TITLE('Ustalık sizden,', 'mühür bizden.', 900, 144, 892, 100, 124, i0=0)
    rows = [('WEB', 'meyem.com.tr'), ('E-POSTA', 'belge@meyem.com.tr'), ('TELEFON', '0 (505) 024 17 24'), ('MOBİL', '0 (553) 908 92 33')]
    for k, (a, b) in enumerate(rows):
        y = 472 + 72 * k
        h += RULE(900, y - 10, 700, 1.2, '#00244D', 0.5)
        h += P('mono', 900, y + 10, 200, a, extra='color:#77183A;font-weight:700;line-height:1;', i=2 + k)
        h += P('ct', 1100, y, 500, b, 36, extra='font-weight:600;', i=2 + k)
    h += RULE(900, 472 + 72 * 4 - 10, 700, 1.2, '#00244D', 0.5)
    h += P('sm', 900, 776, 700, 'Gazi Mahallesi 1307 Sokak, Şimşek Apt. No:20 Zemin Kat, Yenişehir / Mersin', 26, i=6)
    h += CHIPS(['MYK YB-0079', 'TÜRKAK AB-0126-P'], 900, 880)
    h += IMG('qr_meyem.png', 1640, 472, 152, 152, 'meyem.com.tr adresine giden QR kod', extra='border-radius:6px;box-shadow:0 10px 24px rgba(0,36,77,.18);', i=6)
    h += P('mono', 1620, 640, 196, 'TARAYIN', extra='text-align:center;line-height:1;color:#77183A;font-weight:700;')
    return h


NOTES_KAPANIS = ('Kapanış ve çağrı: bir sonraki adım, ihtiyaç analizi görüşmesi. Çalışan listesi ve meslek bilgisi geldiğinde sınav takvimini birlikte planlarız. '
                 'Fotoğraftaki sahne bu işbirliğini anlatıyor: karşıda MEYEM uzmanı, önünde işini bilen ekip. '
                 'Telefon, e-posta ve web adresini slayttan aktarın; QR kod doğrudan meyem.com.tr adresine gider. '
                 'Son söz açılışla aynı: ustalık sizden, mühür bizden.')


# ---------------------------------------------------------------------- birleştirme
ORDER_V2 = ['kapak', 'imza', 'soz', 'belge', 'takvim', 'alan', 'yaprak', 'yerinde', 'durak', 'tesvik', 'referans', 'halka', 'yol', 'kapanis']
OVERRIDES = {
    'kapak': ('a', S1.art_kapak, html_kapak, NOTES_KAPAK, 'cover'),
    'imza': ('b', S1.art_imza, html_imza, NOTES_IMZA, ''),
    'soz': ('a', S1.art_soz, html_soz, S1.NOTES_SOZ, ''),
    'takvim': ('a', S2.art_takvim, html_takvim, NOTES_TAKVIM, ''),
    'alan': ('d', art_alan, html_alan, NOTES_ALAN, ''),
    'yaprak': ('b', art_yaprak, html_yaprak, NOTES_YAPRAK, ''),
    'durak': ('b', S3.art_durak, html_durak, S3.NOTES_DURAK, ''),
    'halka': ('d', S3.art_halka, html_halka, NOTES_HALKA, ''),
    'yol': ('b', art_yol, html_yol, NOTES_YOL, ''),
    'kapanis': ('b', S3.art_kapanis, html_kapanis, NOTES_KAPANIS, 'closing'),
}
SLIDES4 = None   # d_build bu modülü doğrudan kullanır
