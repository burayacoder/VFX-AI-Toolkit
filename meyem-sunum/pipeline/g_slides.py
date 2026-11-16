"""MEYEM · Gebze: Gebze, Çayırova, Darıca ve Dilovası'ndaki üretici fabrikalarda MEYEM'in avantajı.
Görsel dil: MEYEM Vizyon Gravür (v7/v10) ile aynı.
Veri: data/gebze_fabrikalar.json (MEYEM Marmara Adayları sayfasından; Google Haritalar taraması + İSO 500 listeleri)
      ve MYK Portal yetki kapsamları (Kasım 2026).
Çalıştırma: python3 g_build.py [preview|publish]
"""
import json, math
from d_common import *
import d_slides1 as S1
import d_slides3 as S3

GZ = json.load(open(os.path.join(os.path.dirname(M2), 'data', 'gebze_fabrikalar.json')))
ILCE = GZ['ilce']                    # [[ad, sayı], ...]
SEK = GZ['sektor']                   # [[ad, sayı, kazan(0/1)], ...]
N_FAB = sum(n for _, n in ILCE)
N_KAZAN = GZ['kazan']
assert N_FAB == 309 and sum(n for _, n, _ in SEK) == N_FAB


def BKG(name):
    return f'<img class="bk" src="{url_for("bk_" + name + ".jpg")}" alt="" style="left:0;top:0;width:1920px;height:1080px">'


def SRC(text, y=884):
    return P('sm', 128, y, 1664, text, 24, extra='line-height:1.25;color:#2C4868;')


# ====================================================================== 1 KAPAK
def html_kapak():
    cx, cy = 1430, 548
    h = BK('kapak')
    h += IMG('logo_seal.png', 128, 92, 86, 84, 'MEYEM mührü')
    h += P('t1', 234, 96, 700, 'MEYEM', 40, extra='letter-spacing:1px;', i=0)
    h += P('sm', 234, 142, 760, 'Mesleki Yeterlilik ve Belgelendirme Merkezi', 26, i=0)
    h += P('k', 128, 268, 900, 'GEBZE · ÇAYIROVA · DARICA · DİLOVASI', i=1)
    h += TITLE('Gebze’de', 'MEYEM farkı.', 128, 322, 1000, 168, 138, i0=1)
    h += P('lead', 128, 744, 780, f'Dört ilçede {N_FAB} üretici fabrika: hangi belgede öne çıkıyoruz, hangi firmalarla başlıyoruz.', 34, i=3)
    h += CHIPS(['MYK YB-0079', 'TÜRKAK AB-0126-P'], 128, 920)
    h += IMG('cover_photo.png', cx - 250, cy - 250, 500, 500, 'Tulum, yüz siperi, eldiven ve dizlikle taşlama yapan usta', i=2)
    h += P('mono', 128, 992, 600, 'KASIM 2026', extra='line-height:1;')
    return h


NOTES_KAPAK = ('Bu sunum tek bir soruya cevap veriyor: Gebze çevresindeki üretici fabrikalarda MEYEM hangi belgelerde öne çıkıyor ve hangi firmalarla başlamalıyız. '
               'Bölge Gebze, Çayırova, Darıca ve Dilovası; Google Haritalar’da üretici olarak görünen üç yüz dokuz fabrikayı inceledik. '
               'Önce bölgenin sektör yapısını, sonra MEYEM’in az bulunan yetkilerini, en sonda da segment segment firma listelerini göreceğiz.')


# ====================================================================== 2 BÖLGE
def art_bolge():
    s = paper('d')
    s += rosette_lace(1975, -80, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.18, sw=0.7)
    s += wave_lines(90, 860, 540, 960, n=30, amp=10, wl=380, c=INK, op=0.07, sw=0.8, delta=0.16)
    for x, y in ((128, 548), (470, 548), (128, 748), (470, 748)):
        s += line_path(f'M{x} {y}L{x + 300} {y}', WINE, 1.4, 0.8)
    return s, ''


def html_bolge():
    h = BKG('gbolge')
    h += P('k', 128, 100, 700, 'BÖLGE', i=0)
    h += TITLE('Dört ilçe,', f'{N_FAB} fabrika.', 128, 144, 820, 92, 112, i0=0)
    h += P('lead', 128, 384, 700, 'Google Haritalar’da üretici olarak görünen fabrikalar; sektöre göre dağılım sağda.', 30, i=2)
    for k, (ad, n) in enumerate(ILCE):
        x = 128 + 342 * (k % 2)
        y = 548 + 200 * (k // 2)
        h += P('num', x, y + 12, 300, str(n), 112, i=2 + k)
        h += P('mono', x, y + 140, 300, tr_upper(ad), extra='line-height:1;letter-spacing:2px;')
    mx = max(n for _, n, _ in SEK)
    y0, dy = 300, 62
    h += P('mono', 1000, y0 - 52, 400, 'SEKTÖR', extra='line-height:1;letter-spacing:2px;')
    h += P('mono', 1592, y0 - 52, 200, 'FABRİKA', extra='line-height:1;letter-spacing:2px;text-align:right;')
    for k, (ad, n, kz) in enumerate(SEK):
        y = y0 + dy * k
        col = '#77183A' if kz else '#3E5E86'
        h += P('sm', 1000, y + 4, 330, ad, 26, extra='line-height:1.15;', i=3)
        h += RULE(1340, y + 12, round(340 * n / mx), 18, col, 1.0)
        h += P('mono', 1692, y + 4, 100, str(n), extra='line-height:1.2;text-align:right;font-weight:700;letter-spacing:0;')
    y = y0 + dy * len(SEK) + 8
    h += f'<div class="pin" style="left:1000px;top:{y + 7}px;width:40px;height:16px;border-radius:8px;background:#77183A"></div>'
    h += P('sm', 1054, y, 738, 'Buhar ve sıcak su kazanı yaygın sektörler', 24, extra='line-height:1.25;')
    h += FOOT()
    return h


NOTES_BOLGE = (f'Bölgemiz dört ilçe: Gebze yüz on altı, Çayırova yetmiş, Darıca altmış üç, Dilovası altmış fabrika; toplam {N_FAB}. '
               'Sektörlere bakınca kimya ilk sırada, ardından metalurji, metal ürünleri ve gıda geliyor. '
               'Kırmızı çubuklar buhar ve sıcak su kazanının yaygın olduğu sektörler: kimya, gıda, tekstil, kağıt ve ambalaj. '
               f'Bu sektörlerin toplamı {N_KAZAN} fabrika ediyor ve bir sonraki sayfanın konusu bu.')


# ====================================================================== 3 KAZAN
KZ = [(1030, 560, '1', 'Buhar kazanı', 'Seviye 4 · Marmara’da MEYEM dışında yetkili kuruluş', WINE),
      (1335, 560, '2', 'Sıcak su kazanı', 'Seviye 3 · Marmara’da MEYEM dışında yetkili kuruluş', WINE),
      (1640, 560, None, 'Kızgın yağ kazanı', 'Seviye 4 · MEYEM’de MYK onay sürecinde', WINE_D)]
KZ_R = 124


def art_kazan():
    d = iris_defs('iris', 860, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('b')
    s += rosette_lace(-40, 1120, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.18, sw=0.7)
    s += braid(860, 1960, 560, amp=18, wl=320, n=14, spread=2.8, delta=0.26, c1='url(#iris)', c2=WINE, op=0.5)
    for x, y, _, _, _, col in KZ:
        s += f'<circle cx="{x}" cy="{y}" r="{KZ_R + 26}" fill="{PAPER_B}" fill-opacity="0.97"/>'
        s += ring_bundle(x, y, KZ_R, count=10, gap=2.6, a=3.2, nw=24, c1=col, c2=col, op=0.85, sw=1.0)
        s += circle(x, y, KZ_R + 26, col, 1.5, 0.95)
        s += circle(x, y, KZ_R - 6, col, 1.0, 0.6, dash='6 6' if col == WINE_D else '')
    return s, d


def html_kazan():
    h = BKG('gkazan')
    h += P('k', 128, 100, 700, 'FIRSAT 1 · KAZAN DAİRESİ', i=0)
    h += TITLE('Kazan dairesi:', f'{N_KAZAN} fabrika.', 128, 144, 760, 92, 112, i0=0)
    h += P('lead', 128, 384, 700, 'Kimya, gıda, tekstil, kağıt ve ambalaj başta olmak üzere bu fabrikaların sektöründe buhar ve sıcak su kazanı yaygın. Kazan operatörlerinde belge 23 Mart 2027’den itibaren zorunlu.', 30, i=2)
    h += RULE(128, 640, 640, 1.2, '#00244D', 0.5)
    h += P('num', 128, 664, 160, '0', 150, i=3)
    h += P('ct', 300, 690, 468, 'Kocaeli’de kazan belgesi veren yetkili kuruluş', 32, extra='line-height:1.15;', i=3)
    for k, (x, y, num, t, d_, col) in enumerate(KZ):
        if num:
            h += P('num', x - 90, y - 78, 180, num, 150, extra='text-align:center;', i=2 + k)
        else:
            h += P('t2', x - 100, y - 36, 200, 'onayda', 56, extra='text-align:center;color:#580721;', i=2 + k)
        ty = y + KZ_R + 44
        h += P('ct', x - 150, ty, 300, t, 32, extra='text-align:center;' + ('color:#580721;' if not num else ''), i=2 + k)
        h += P('sm', x - 150, ty + 44, 300, d_, 24, extra='text-align:center;line-height:1.3;', i=2 + k)
    h += SRC('Kaynak: MYK Portal yetkili kuruluş kapsamları, Kasım 2026; 2026/1 Tebliği, Resmî Gazete 33202.', 892)
    h += FOOT()
    return h


NOTES_KAZAN = (f'İlk fırsat kazan dairesi. Bölgedeki {N_KAZAN} fabrika kimya, gıda, tekstil, kağıt ve ambalaj gibi kazanın yaygın olduğu sektörlerde. '
               '2026/1 Tebliği ile buhar ve sıcak su kazanı operatörlüğünde belge 23 Mart 2027’den itibaren zorunlu oluyor. '
               'MEYEM buhar kazanında seviye dört, sıcak su kazanında seviye üç yetkili. Kocaeli’de bu belgeleri veren başka yetkili kuruluş yok; '
               'Marmara’da MEYEM dışında buhar kazanında bir, sıcak su kazanında iki kuruluş var ve hepsi İstanbul’da. '
               'Üçüncü kazan türü olan kızgın yağ kazanı operatörlüğü MEYEM’de MYK onay sürecinde; onaylandığında üç kazan türünün tamamını tek kuruluştan vermiş olacağız.')


# ====================================================================== 4 NADİR
NADIR = [('Buhar Kazanı Operatörü', 'SEVİYE 4', '23.03.2027', 0, 1, 'Kimya, gıda, tekstil, kağıt · 161 fabrika'),
         ('Sıcak Su Kazanı Operatörü', 'SEVİYE 3', '23.03.2027', 0, 2, 'Aynı 161 fabrikanın kazan dairesi'),
         ('Dolum, Ambalajlama ve Paketleme Operatörü (Gıda)', 'SEVİYE 4', 'Gönüllü', 0, 0, 'Gıda · 39 fabrika'),
         ('Tornacı', 'SEVİYE 4', 'Zorunlu', 1, 5, 'Metal ve metalurji · 83 fabrika'),
         ('Elektro-Mekanik Montaj İşçisi', 'SEVİYE 4', '23.03.2027', 3, 9, 'Elektrikli teçhizat üreticileri')]


def art_nadir():
    s = paper('c')
    s += rosette_lace(1985, 1160, 380, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.15, sw=0.7)
    s += wave_lines(0, 1920, 40, 250, n=22, amp=10, wl=420, c=INK, op=0.06, sw=0.8, delta=0.18)
    return s, ''


def html_nadir():
    h = BKG('gnadir')
    h += P('k', 128, 76, 700, 'FIRSAT 2 · AZ BULUNAN YETKİ', i=0)
    h += TITLE('Bölgede az bulunan,', 'MEYEM’de var.', 128, 112, 1000, 80, 98, i0=0)
    h += P('lead', 1100, 120, 692, 'Beş belgede bölgedeki yetkili kuruluş sayısı çok az; hepsi MEYEM’in yetki kapsamında.', 30, i=2)
    cols = [(128, 540, 'BELGE', 'left'), (700, 230, 'ZORUNLULUK', 'left'), (950, 170, 'KOCAELİ’DE', 'center'),
            (1140, 190, 'MARMARA’DA', 'center'), (1360, 432, 'GEBZE’DE NEREDE', 'left')]
    yh = 318
    for x, w, t, al in cols:
        h += P('mono', x, yh, w, t, extra=f'line-height:1;letter-spacing:1px;text-align:{al};')
    h += RULE(128, yh + 40, 1664, 1.6, '#00244D', 0.7)
    y0, dy = yh + 52, 100
    for k, (ad, sev, zr, koc, mar, ner) in enumerate(NADIR):
        y = y0 + dy * k
        h += P('ct', 128, y + 6, 540, ad, 28, extra='line-height:1.12;', i=2 + k)
        h += P('mono', 128, y + 6 + (66 if len(ad) > 34 else 36), 540, sev, extra='line-height:1;font-size:24px;letter-spacing:1px;')
        h += P('sm', 700, y + 10, 230, zr, 26, extra='line-height:1.2;' + ('color:#77183A;font-weight:700;' if zr[0].isdigit() else ''))
        h += P('num', 950, y - 6, 170, str(koc), 76, extra='text-align:center;' + ('' if koc == 0 else 'color:#3E5E86;'), i=2 + k)
        h += P('num', 1140, y - 6, 190, str(mar), 76, extra='text-align:center;' + ('' if mar <= 2 else 'color:#3E5E86;'), i=2 + k)
        h += P('sm', 1360, y + 10, 432, ner, 26, extra='line-height:1.25;')
        h += RULE(128, y + dy - 6, 1664, 1.0, '#00244D', 0.3)
    h += SRC('Kaynak: MYK Portal yetkili kuruluş kapsamları, Kasım 2026. Kocaeli ve Marmara sütunları MEYEM dışındaki yetkili kuruluşları sayar.', 882)
    h += FOOT()
    return h


NOTES_NADIR = ('İkinci fırsat, bölgede az bulunan yetkiler. Tabloda beş belge var ve her satırda Kocaeli’de ve Marmara’da MEYEM dışında kaç yetkili kuruluş olduğunu görüyorsunuz. '
               'Buhar ve sıcak su kazanında Kocaeli’de hiç yok, Marmara’da bir ve iki. Gıda dolum, ambalajlama ve paketleme operatörlüğünü Marmara’da bizden başka veren yok. '
               'Tornacı seviye dört zorunlu bir belge; Kocaeli’de bir, Marmara’da beş kuruluş veriyor. Elektro-mekanik montaj işçisi 2026/1 ile zorunlu hale geliyor ve Marmara’da dokuz kuruluşta var. '
               'Bu belgeler kapıyı açar; aynı ziyaret içinde kaynak, bakım ve forklift gibi yaygın belgeler de aynı sınav gününe eklenir.')


# ====================================================================== 5 SEKTÖR
SEKTOR = [('Kimya', 56, '<span style="color:#77183A"><b>Buhar kazanı operatörü · Sıcak su kazanı operatörü</b></span>'),
          ('Gıda', 39, '<span style="color:#77183A"><b>Buhar kazanı · Sıcak su kazanı · Dolum, ambalajlama ve paketleme operatörü</b></span>'),
          ('Metal ve metalurji', 83, '<span style="color:#77183A"><b>Tornacı</b></span> · Makine bakımcı · Çelik kaynakçısı · Direnç kaynak ayarcısı · Endüstriyel boru montajcısı · Makine montajcısı'),
          ('Tekstil', 30, '<span style="color:#77183A"><b>Buhar kazanı operatörü · Sıcak su kazanı operatörü</b></span>'),
          ('Kağıt ve ambalaj', 25, '<span style="color:#77183A"><b>Buhar kazanı · Sıcak su kazanı</b></span> · Makine bakımcı'),
          ('Lojistik ve depo', 29, 'Endüstriyel taşımacı (forklift) · Köprülü vinç operatörü')]


def art_sektor():
    s = paper('a')
    s += rosette_lace(1985, -90, 340, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.18, sw=0.7)
    s += wave_lines(0, 1920, 940, 1080, n=14, amp=8, wl=420, c=INK, op=0.06, sw=0.8, delta=0.18)
    return s, ''


def html_sektor():
    h = BKG('gsektor')
    h += P('k', 128, 76, 700, 'SEKTÖR · BELGE', i=0)
    h += TITLE('Hangi sektörde,', 'hangi belge?', 128, 112, 1000, 80, 98, i0=0)
    h += P('lead', 1100, 120, 692, 'Her sektörün çalışan profiline göre MEYEM’in verebildiği zorunlu ve az bulunan belgeler.', 30, i=2)
    y0, dy = 330, 92
    h += RULE(128, y0 - 12, 1664, 1.6, '#00244D', 0.7)
    for k, (ad, n, txt) in enumerate(SEKTOR):
        y = y0 + dy * k
        h += P('ct', 128, y + 6, 420, ad, 34, extra='line-height:1.1;', i=2 + k)
        h += P('mono', 128, y + 50, 420, f'{n} FABRİKA', extra='line-height:1;letter-spacing:1px;')
        h += P('sm', 580, y + 8, 1212, txt, 26, extra='line-height:1.32;', raw=True)
        h += RULE(128, y + dy - 8, 1664, 1.0, '#00244D', 0.3)
    y = y0 + dy * len(SEKTOR) + 12
    h += f'<div class="pin" style="left:128px;top:{y + 7}px;width:40px;height:16px;border-radius:8px;background:#77183A"></div>'
    h += P('sm', 182, y, 1200, 'Koyu kırmızı: bölgede az bulunan belge', 24, extra='line-height:1.25;')
    h += FOOT()
    return h


NOTES_SEKTOR = ('Sektör ve belge eşleşmesi. Kimya, tekstil, kağıt ve ambalajda kapıyı kazan belgeleri açıyor. '
                'Gıdada buna dolum, ambalajlama ve paketleme operatörlüğü ekleniyor; bu belgeyi Marmara’da bizden başka veren yok. '
                'Metal ve metalurjide ana belge tornacı; yanında makine bakımcı, çelik kaynakçısı, direnç kaynak ayarcısı, endüstriyel boru ve makine montajcısı var ve hepsi zorunlu. '
                'Lojistik ve depolarda forklift için endüstriyel taşımacı ve köprülü vinç operatörlüğü. Sonraki üç sayfa bu segmentlerin firma listeleri.')


# ====================================================================== 6-8 FİRMA LİSTELERİ
FIRMA_SEG = {
    'gfkazan': dict(tone='d', k='FİRMALAR · KAZAN DAİRESİ', t1='Kimya, kağıt,', t2='tekstil.',
                    neden=[('I', 'Nadir yetki', 'Buhar ve sıcak su kazanı belgesini Kocaeli’de veren yetkili kuruluş yok; Marmara’da MEYEM dışında iki kuruluş var.'),
                           ('II', 'Takvim', '23 Mart 2027’den itibaren kazan operatörlerinde belge zorunlu.'),
                           ('III', 'Yerinde sınav', 'Kazan dairesinde, vardiya düzeni bozulmadan; bakım ve forklift sınavları aynı gün.')]),
    'gfgida': dict(tone='c', k='FİRMALAR · GIDA', t1='Gıda', t2='fabrikaları.',
                   neden=[('I', 'İki kazan belgesi', 'Buhar ve sıcak su kazanı operatörlüğü; Kocaeli’de veren başka yetkili kuruluş yok.'),
                          ('II', 'Dolum ve paketleme', 'Gıda dolum, ambalajlama ve paketleme operatörlüğünü Marmara’da yalnızca MEYEM veriyor.'),
                          ('III', 'Tek gün, tek muhatap', 'Kazan, paketleme hattı ve forklift sınavları aynı gün fabrikada.')]),
    'gfmetal': dict(tone='a', k='FİRMALAR · METAL VE METALURJİ', t1='Metal ve', t2='çelik.',
                    neden=[('I', 'Tornacı, seviye 4', 'Zorunlu belge; Kocaeli’de bir, Marmara’da beş yetkili kuruluş veriyor.'),
                           ('II', 'Bakım, kaynak, montaj', 'Makine bakımcı, çelik kaynakçısı, direnç kaynak ayarcısı, boru ve makine montajcısı: hepsi zorunlu, hepsi kapsamımızda.'),
                           ('III', 'Aynı gün sınav', 'Talaşlı imalat, kaynak ve bakım ekipleri tek planla, fabrikada.')]),
}


def art_firma(tone):
    def f():
        s = paper(tone)
        s += rosette_lace(-60, 1140, 360, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
        s += line_path('M780 120L780 930', WINE, 1.2, 0.55) + line_path('M790 120L790 930', INK, 0.8, 0.35)
        return s, ''
    return f


def html_firma(sid):
    seg = FIRMA_SEG[sid]
    rows = GZ['firmalar'][sid]

    def f():
        h = BKG(sid)
        h += P('k', 128, 100, 620, seg['k'], i=0)
        h += TITLE(seg['t1'], seg['t2'], 128, 144, 620, 88, 108, i0=0)
        h += P('mono', 128, 400, 600, 'NEDEN MEYEM', extra='line-height:1;letter-spacing:2px;color:#77183A;font-weight:700;')
        for k, (rn, t, d_) in enumerate(seg['neden']):
            y = 448 + 156 * k
            h += P('num', 128, y - 6, 80, rn, 52, extra='font-style:italic;', i=2 + k)
            h += P('ct', 216, y, 520, t, 30, extra='line-height:1.12;', i=2 + k)
            h += P('sm', 216, y + 42, 540, d_, 24, extra='line-height:1.32;', i=2 + k)
        x0 = 840
        h += P('mono', x0, 130, 520, 'FİRMA', extra='line-height:1;letter-spacing:2px;')
        h += P('mono', 1376, 130, 150, 'İLÇE', extra='line-height:1;letter-spacing:2px;')
        h += P('mono', 1540, 130, 252, 'ÖLÇEK', extra='line-height:1;letter-spacing:2px;text-align:right;')
        h += RULE(x0, 166, 952, 1.6, '#00244D', 0.7)
        dy = min(74, int(740 / len(rows)))
        for k, r in enumerate(rows):
            y = 176 + dy * k
            h += P('ct', x0, y + 4, 520, r['ad'], 28, extra='line-height:1.1;', i=3)
            h += P('sm', x0, y + 38, 520, r['tur'], 24, extra='line-height:1.2;')
            h += P('mono', 1376, y + 10, 150, tr_upper(r['ilce']), extra='line-height:1;font-size:24px;letter-spacing:1px;')
            if r.get('olcek'):
                h += P('sm', 1540, y + 4, 252, r['olcek'], 24, extra='line-height:1.2;text-align:right;color:#77183A;font-weight:700;')
            if r.get('calisan'):
                h += P('sm', 1540, y + 36, 252, r['calisan'], 24, extra='line-height:1.2;text-align:right;')
            h += RULE(x0, y + dy - 4, 952, 1.0, '#00244D', 0.3)
        h += FOOT()
        return h
    return f


def notes_firma(sid):
    rows = GZ['firmalar'][sid]
    big = [r['ad'] for r in rows if r.get('olcek')]
    seg = FIRMA_SEG[sid]
    txt = {
        'gfkazan': 'Kimya, kağıt, ambalaj ve tekstil fabrikalarında kapıyı kazan belgesi açar. ',
        'gfgida': 'Gıda fabrikalarında iki kapı var: kazan dairesi ve dolum-paketleme hattı. ',
        'gfmetal': 'Metal ve çelikte ana belge tornacı; yanında bakım, kaynak ve montaj belgeleri gelir. ',
    }[sid]
    s = txt + 'Sağdaki liste bölgedeki üretici fabrikalardan seçildi. '
    if big:
        s += 'İSO 500 listelerinde yer alan büyük işverenler: ' + ', '.join(big) + '. Ölçek sütununda sıra ve çalışan sayısı var. '
    s += 'Soldaki üç gerekçe her ziyarette söylenecek cümleler: ' + '; '.join(f'{t.lower()}' for _, t, _ in seg['neden']) + '.'
    return s


# ====================================================================== 9 SINAV GÜNÜ
GUN = [(300, '09.00', 'Kazan operatörü', 'Buhar ve sıcak su kazanı', 'tile_enerji.jpg', 'Baretli teknisyen ölçü aletiyle kontrol yapıyor'),
       (740, '11.00', 'Makine bakımcı', 'Bakım ve montaj ekibi', 'tile_makine.jpg', 'Koruyucu gözlükle tezgâh başında çalışan operatör'),
       (1180, '13.30', 'Çelik kaynakçısı', 'Kaynak atölyesi', 'tile_metal.jpg', 'Kaynak maskesi ve eldiveniyle çalışan kaynakçı'),
       (1620, '15.30', 'Endüstriyel taşımacı', 'Forklift ve transpalet', 'tile_tasima.jpg', 'Baretli ve reflektif yelekli forklift operatörü')]
GUN_Y, GUN_R = 560, 130


def art_gun():
    d = iris_defs('iris', 0, 1920, ((0, INK), (0.5, BLUE), (1, WINE)))
    s = paper('b')
    s += rosette_lace(1985, -80, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    s += braid(-20, 1940, GUN_Y, amp=16, wl=360, n=14, spread=2.8, delta=0.26, c1='url(#iris)', c2=WINE, op=0.5)
    for x, *_ in GUN:
        s += f'<circle cx="{x}" cy="{GUN_Y}" r="{GUN_R + 24}" fill="{PAPER_B}"/>'
        s += circle(x, GUN_Y, GUN_R + 10, WINE, 1.6, 0.9) + circle(x, GUN_Y, GUN_R + 24, INK, 1.0, 0.6)
    return s, d


def html_gun():
    h = BKG('ggun')
    h += P('k', 128, 76, 700, 'YERİNDE SINAV', i=0)
    h += TITLE('Tek sınav günü,', 'dört belge.', 128, 112, 1000, 80, 98, i0=0)
    h += P('lead', 1100, 120, 692, 'Örnek gün: sınav fabrikada yapılır, çalışan fabrikadan ayrılmaz, vardiya düzeni korunur.', 30, i=2)
    for k, (x, saat, t, d_, img, alt) in enumerate(GUN):
        h += IMG(img, x - GUN_R, GUN_Y - GUN_R, 2 * GUN_R, 2 * GUN_R, alt, extra='border-radius:50%;', i=2 + k)
        ty = GUN_Y + GUN_R + 44
        h += P('mono', x - 160, ty, 320, saat, extra='text-align:center;line-height:1;color:#77183A;font-weight:700;letter-spacing:2px;')
        h += P('ct', x - 180, ty + 40, 360, t, 34, extra='text-align:center;', i=2 + k)
        h += P('sm', x - 180, ty + 88, 360, d_, 26, extra='text-align:center;', i=2 + k)
    h += RULE(128, 870, 1664, 1.2, '#00244D', 0.4)
    h += P('sm', 128, 888, 1664, 'Sınav alanı, ekipman ve görevliler MEYEM planıyla hazırlanır; teorik ve uygulamalı sınav fabrikada yapılır, belge MYK kaydıyla düzenlenir.', 26, extra='line-height:1.2;', i=6)
    h += FOOT()
    return h


NOTES_GUN = ('Yerinde sınav, Gebze için en güçlü pratik avantajımız. Örnek bir günü anlatın: sabah kazan operatörleri, öğleden önce bakım ekibi, öğleden sonra kaynak atölyesi, gün sonunda forklift operatörleri. '
             'Sınav alanı, ekipman ve görevliler MEYEM planıyla hazırlanır; teorik ve uygulamalı sınavlar fabrikada yapılır. '
             'Çalışan fabrikadan ayrılmaz, ulaşım ve vardiya kaybı olmaz; dört farklı belge tek muhatapla, tek planla tamamlanır.')


# ====================================================================== 10 TAKVİM
TK = [(128, '31.12.2026', '6111 teşvikinde son gün', 'Belgeli işçi alımında işe giriş ve sisteme tanımlama için son tarih.'),
      (1000, '23.03.2027', 'Kazanda belge zorunlu', 'Buhar, sıcak su ve kızgın yağ kazanı operatörlüğü ile elektro-mekanik montajda geçiş süresi biter.')]


def art_takvim():
    d = iris_defs('iris', 0, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('a')
    s += rosette_lace(1990, 1170, 400, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    s += braid(-20, 1940, 560, amp=36, wl=480, n=22, spread=3.2, delta=0.22, c1='url(#iris)', c2=WINE, op=0.5)
    for x0, *_ in TK:
        x = x0 + 34
        s += f'<circle cx="{x}" cy="560" r="38" fill="{PAPER_A}"/>'
        s += circle(x, 560, 38, WINE, 3, 1) + circle(x, 560, 50, INK, 1, 0.55) + circle(x, 560, 8, WINE, 0, 0, fill=WINE)
    return s, d


def html_takvim():
    h = BKG('gtakvim')
    h += P('k', 128, 100, 700, 'TAKVİM', i=0)
    h += TITLE('İki tarih,', 'tek plan.', 128, 144, 1000, 92, 112, i0=0)
    for k, (x, dt, t, d_) in enumerate(TK):
        h += P('numb', x, 648, 760, dt, 96, i=2 + k)
        h += P('ct', x, 768, 700, t, 40, i=2 + k)
        h += P('sm', x, 826, 700, d_, 26, extra='line-height:1.32;', i=2 + k)
    h += P('lead', 1000, 150, 792, 'Kızgın yağ kazanı operatörlüğü MEYEM’de MYK onay sürecinde; onayla üç kazan türü tek kuruluşta.', 30, i=2)
    h += FOOT()
    return h


NOTES_TAKVIM = ('İki tarih var. Otuz bir Aralık 2026, 6111 teşvikinde belgeli işçi alımı için işe giriş ve sisteme tanımlamanın son günü; imalatta prim indirimi de bu tarihe kadar. '
                'Yirmi üç Mart 2027’de 2026/1 Tebliği’nin geçiş süresi bitiyor: buhar, sıcak su ve kızgın yağ kazanı operatörlüğü ile elektro-mekanik montajda belge zorunlu oluyor. '
                'Kızgın yağ kazanı operatörlüğü MEYEM’de MYK onay sürecinde. Gebze ziyaretlerinde mesaj tek: kazan ve bakım ekiplerinin sınav takvimini şimdi birlikte kuralım.')


# ====================================================================== 11 KAPANIŞ
def html_kapanis():
    cx, cy = S3.KC
    h = BK('kapanis')
    h += IMG('close_photo.png', cx - 236, cy - 236, 472, 472, 'Kulak koruyucu, koruyucu gözlük ve reflektif yelekli, tebessüm eden çalışan', i=1)
    h += P('k', 900, 100, 700, 'BAŞLAYALIM', i=0)
    h += TITLE('Gebze’de ilk', 'sınav günü.', 900, 144, 892, 100, 124, i0=0)
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


NOTES_KAPANIS = ('Kapanış ve çağrı. İlk adım, listedeki fabrikalardan biriyle ihtiyaç analizi görüşmesi: hangi çalışan, hangi belge. '
                 'Çalışan listesi geldiğinde ilk sınav gününü kazan ve bakım ekipleriyle birlikte planlarız. '
                 'Telefon, e-posta ve web adresi slaytta; QR kod meyem.com.tr adresine gider.')


# ---------------------------------------------------------------------- birleştirme
SLIDES = [
    ('kapak', 'a', 'kapak', S1.art_kapak, html_kapak, NOTES_KAPAK, 'cover'),
    ('bolge', 'd', 'gbolge', art_bolge, html_bolge, NOTES_BOLGE, ''),
    ('kazan', 'b', 'gkazan', art_kazan, html_kazan, NOTES_KAZAN, ''),
    ('nadir', 'c', 'gnadir', art_nadir, html_nadir, NOTES_NADIR, ''),
    ('sektor', 'a', 'gsektor', art_sektor, html_sektor, NOTES_SEKTOR, ''),
] + [(sid[2:] if False else sid, FIRMA_SEG[sid]['tone'], sid, art_firma(FIRMA_SEG[sid]['tone']), html_firma(sid), notes_firma(sid), '')
     for sid in ('gfkazan', 'gfgida', 'gfmetal')] + [
    ('gun', 'b', 'ggun', art_gun, html_gun, NOTES_GUN, ''),
    ('takvim', 'a', 'gtakvim', art_takvim, html_takvim, NOTES_TAKVIM, ''),
    ('kapanis', 'b', 'kapanis', S3.art_kapanis, html_kapanis, NOTES_KAPANIS, 'closing'),
]
