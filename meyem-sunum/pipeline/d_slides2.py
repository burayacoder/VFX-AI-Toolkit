"""Slayt 5-8: takvim, alan, yaprak, helal."""
import math
from d_common import *


def rot_pt(cx, cy, dx, dy, deg):
    a = math.radians(deg)
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


# ====================================================================== 5 TAKVİM
TK_X = [128, 568, 1008, 1448]


def art_takvim():
    d = iris_defs('iris', 0, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('a')
    s += rosette_lace(1990, 1170, 400, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    s += braid(-20, 1940, 650, amp=40, wl=480, n=24, spread=3.2, delta=0.22, c1='url(#iris)', c2=WINE, op=0.55)
    for k, x0 in enumerate(TK_X):
        x = x0 + 34
        s += f'<circle cx="{x}" cy="650" r="38" fill="{PAPER_A}"/>'
        if k == 3:
            s += f'<circle cx="{x}" cy="650" r="38" fill="{WINE}"/>' + circle(x, 650, 28, '#FFFFFF', 1.4, 0.8) + circle(x, 650, 50, WINE, 1.2, 0.8)
        else:
            s += circle(x, 650, 38, WINE, 3, 1) + circle(x, 650, 50, INK, 1, 0.55) + circle(x, 650, 8, WINE, 0, 0, fill=WINE)
    return s, d


def html_takvim():
    h = BK('takvim')
    h += P('k', 128, 100, 700, 'ZORUNLULUK TAKVİMİ', i=0)
    h += TITLE('Liste büyüyor,', 'takvim işliyor.', 128, 144, 1000, 92, 112, i0=0)
    h += P('num', 1380, 92, 412, '+40', 196, extra='text-align:right;', i=2)
    h += P('sm', 1380, 308, 412, 'meslek, 2026/1 Tebliği ile zorunlu listeye eklendi', 26, extra='text-align:right;', i=3)
    ev = [('23.03.2026', '2026/1 Tebliği', '40 meslek zorunlu listesine eklendi. Resmî Gazete 33202.'),
          ('13.07.2026', 'Kazan yetkisi aktif', 'Buhar Kazanı (S4) ve Sıcak Su Kazanı (S3) operatörlüğü, MYK Portal kaydı.'),
          ('31.12.2026', 'Teşvikte son gün', 'Belgeli işçi alımında işe giriş ve sisteme tanımlama günü.'),
          ('23.03.2027', 'Geçiş süresi biter', '2026/1 kapsamındaki 40 meslekte belge zorunlu olur.')]
    for i, (dt, t, b) in enumerate(ev):
        x = TK_X[i]
        h += P('numb', x, 424, 380, dt, 54, i=2 + i)
        h += P('ct', x, 774, 340, t, 34, i=2 + i)
        h += P('sm', x, 826, 340, b, 26, i=2 + i)
    h += FOOT('Takvim')
    return h


NOTES_TAKVIM = ('Dört tarih yeter. 23 Mart 2026’da 2026/1 sayılı Tebliğ yayımlandı: 40 meslek zorunlu listesine eklendi. '
                '13 Temmuz 2026’da buhar kazanı ve sıcak su kazanı operatörlüğü yetkilerimiz MYK Portal’da aktif hale geldi. '
                '31 Aralık 2026, 6111 teşvikinde belgeli işçi alımı için son tanımlama günü. '
                '23 Mart 2027’de geçiş süresi bitiyor ve 2026/1 kapsamındaki 40 meslekte belge zorunlu oluyor. '
                'Yani firmalar için pencere açık ve takvim işliyor: belgelendirmeyi şimdi planlayan, hem teşvikten hem zamandan kazanır.')


# ====================================================================== 6 ALAN
STX = [128, 486, 844, 1202, 1560]
STY = [352, 652]
SW_, SH_ = 232, 275
TILT = [-2.0, 1.4, -1.0, 2.0, -1.4, 1.0, -2.0, 1.5, -1.0]


def art_alan():
    s = paper('d')
    s += wave_lines(100, 1820, 330, 962, n=38, amp=10, wl=430, c=INK, op=0.09, sw=0.8, delta=0.16)
    s += f'<rect x="100" y="326" width="1720" height="636" fill="none" stroke="{INK}" stroke-width="1.4" stroke-opacity="0.55"/>'
    s += f'<rect x="108" y="334" width="1704" height="620" fill="none" stroke="{WINE}" stroke-width="0.9" stroke-opacity="0.6"/>'
    s += rosette_lace(1975, -70, 300, n=48, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    return s, ''


def html_alan():
    h = BK('alan')
    h += P('k', 128, 76, 600, 'KAPSAM', i=0)
    h += TITLE('Dokuz alan,', 'tek çatı.', 128, 112, 800, 80, 98, i0=0)
    h += P('lead', 1000, 112, 792, 'Mavi yakadan beyaz yakaya; kazan dairesinden bilişime, MEYEM’in yetki kapsamındaki meslek alanları.', 33, i=2)
    secs = [('boiler', 'Kazan ve enerji', 'Kazan operatörü'), ('fork', 'Forklift ve depo', 'Forklift operatörü'),
            ('weld', 'Kaynak ve metal', 'Kaynakçı'), ('cnc', 'Makine ve torna', 'CNC tezgâh operatörü'),
            ('elec', 'Elektrik ve inşaat', 'Elektrik bakımcısı'), ('food', 'Gıda ve içecek', 'Gıda üretim hattı'),
            ('cyber', 'Bilişim ve siber', 'Bilişim uzmanı'), ('building', 'Ticaret ve emlak', 'Kurumsal bina'),
            ('team', 'Proje ve İK', 'Proje ekibi')]
    for k, (key, lab, alt) in enumerate(secs):
        r, c = divmod(k, 5)
        x, y = STX[c], STY[r]
        th = TILT[k]
        h += IMG(f'stamp_{key}.png', x - 24, y - 24, SW_ + 48, SH_ + 48, alt, extra=f'transform:rotate({th}deg);', i=2 + k)
        # etiket: damganın merkezi etrafında aynı açıyla döner
        Cx, Cy = x + SW_ / 2, y + SH_ / 2
        lx, ly = rot_pt(Cx, Cy, 0, 85.5, th)
        h += P('sm', int(lx - 99), int(ly - 36), 178, lab, 24,
               extra=f'background:rgba(251,248,241,.95);padding:8px 10px;text-align:center;line-height:1.2;font-weight:600;color:#00244D;transform:rotate({th}deg);', i=2 + k)
    # onuncu hücre: sayı
    x, y = STX[4], STY[1]
    h += P('num', x, y + 6, 232, '55', 150)
    h += P('sm', x, y + 166, 232, 'ulusal yeterlilik; 27’si zorunlu, 28’i gönüllü', 26)
    h += FOOT('Kapsam')
    return h


NOTES_ALAN = ('Dokuz alan, tek çatı: kazan ve enerji, forklift ve depolama, kaynak ve metal, makine ve torna, elektrik ve inşaat, gıda ve içecek, '
              'bilişim ve siber güvenlik, ticaret ve emlak, proje yönetimi ve insan kaynakları. Mavi yakadan beyaz yakaya uzanan bir yelpaze. '
              'MYK Portal kaydına göre MEYEM’in 55 ulusal yeterlilik yetkisi var; bunların 27’si zorunlu, 28’i gönüllü kapsamda. '
              'Konuşmanızı müşterinin mesleğinin durduğu damgada tutun.')


# ====================================================================== 7 YAPRAK
YP_C = (1250, 548)


def art_yaprak():
    cx, cy = YP_C
    s = paper('b')
    s += rosette_lace(cx, cy, 480, n=72, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.13, sw=0.7)
    s += petal_ring(cx, cy, 150, 408, 55, set(range(27)), fill=WINE, stroke=INK, accent=INK, accent_idx=(8, 9), wid=1.12)
    s += f'<circle cx="{cx}" cy="{cy}" r="142" fill="{PAPER_B}"/>'
    s += circle(cx, cy, 142, INK, 1.2, 0.7) + circle(cx, cy, 130, WINE, 0.9, 0.55)
    for k in range(32):
        a = -math.pi / 2 + 2 * math.pi * k / 32
        x, y = cx + 442 * math.cos(a), cy + 442 * math.sin(a)
        if k < 16:
            s += f'<circle cx="{f1(x)}" cy="{f1(y)}" r="8" fill="{WINE}"/>'
        else:
            s += f'<circle cx="{f1(x)}" cy="{f1(y)}" r="7.4" fill="{PAPER_B}" stroke="{WINE}" stroke-width="1.6"/>'
    s += ticks(cx, cy, 464, 110, 6, 12, 5, INK, 0.9, 0.4)
    return s, ''


def html_yaprak():
    cx, cy = YP_C
    h = BK('yaprak')
    h += P('k', 128, 100, 700, 'YETKİ KAPSAMI', i=0)
    h += TITLE('55 yaprak,', 'tek rozet.', 128, 144, 700, 96, 116, i0=0)
    h += P('lead', 128, 372, 600, 'Her ulusal yeterlilik, rozete bir yaprak ekler. MYK Portal kaydına göre 55 yeterlilikte yetkiliyiz.', 33, i=2)
    leg = [('wine', '27 zorunlu kapsamdaki yeterlilik'), ('line', '28 gönüllü kapsamdaki yeterlilik'),
           ('ink', 'Buhar Kazanı (S4) ve Sıcak Su Kazanı (S3) operatörlüğü; yetki 13.07.2026’dan itibaren aktif'),
           ('dot', 'MYK onay sürecindeki 32 yeterlilik; 16’sı zorunlu kapsamda')]
    y = 598
    hs = [52, 52, 120, 80]
    for i, (kind, t) in enumerate(leg):
        if kind == 'wine':
            h += f'<div class="pin" style="left:128px;top:{y + 8}px;width:46px;height:18px;border-radius:9px;background:#77183A"></div>'
        elif kind == 'line':
            h += f'<div class="pin" style="left:128px;top:{y + 8}px;width:43px;height:15px;border-radius:9px;border:1.5px solid #00244D"></div>'
        elif kind == 'ink':
            h += f'<div class="pin" style="left:128px;top:{y + 8}px;width:46px;height:18px;border-radius:9px;background:#00244D"></div>'
        else:
            h += f'<div class="pin" style="left:128px;top:{y + 9}px;width:14px;height:14px;border-radius:7px;background:#77183A"></div>'
            h += f'<div class="pin" style="left:152px;top:{y + 9}px;width:11px;height:11px;border-radius:7px;border:1.6px solid #77183A"></div>'
        h += P('sm', 196, y, 540, t, 26, i=3 + i)
        y += hs[i]
    h += P('num', cx - 140, cy - 112, 280, '55', 148, extra='text-align:center;', i=2)
    h += P('mono', cx - 100, cy + 44, 200, 'ULUSAL<br>YETERLİLİK', extra='text-align:center;letter-spacing:1px;line-height:1.15;', raw=True)
    h += FOOT('Yetki kapsamı')
    return h


NOTES_YAPRAK = ('Rozetteki her yaprak bir ulusal yeterlilik. Elli beş yaprağın yirmi yedisi dolu: bunlar zorunlu kapsamdaki yeterlilikler. '
                'Boş yirmi sekiz yaprak gönüllü kapsamda. Lacivert iki yaprak, buhar kazanı operatörlüğü seviye 4 ve sıcak su kazanı operatörlüğü seviye 3; '
                'bu yetkiler 13 Temmuz 2026’dan beri aktif. Dış halkadaki otuz iki nokta, MYK’da onay sürecinde olan yeterlilikleri gösterir; on altısı zorunlu kapsamda. '
                'Rozet büyüdükçe müşterinin tek muhatabı aynı kalır.')


# ====================================================================== 8 HELAL
HL_C = (300, 706)
HL_R = 150


def art_helal():
    cx, cy = HL_C
    s = paper('a')
    s += rosette_lace(1560, 520, 400, n=66, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.15, sw=0.7)
    s += ring_bundle(cx, cy, HL_R - 18, count=12, gap=3.0, a=3, nw=26, c1=WINE, c2=INK, op=0.5)
    s += rosette_lace(cx, cy, 120, n=36, a=0.5, b=0.16, c=0.36, c1=INK, c2=WINE, op=0.30, sw=0.7)
    for k in range(8):
        a = -math.pi / 2 + 2 * math.pi * k / 8
        x, y = cx + HL_R * math.cos(a), cy + HL_R * math.sin(a)
        s += f'<circle cx="{f1(x)}" cy="{f1(y)}" r="24" fill="#FFFFFF"/>' + circle(x, y, 24, WINE, 2.2, 0.95) + circle(x, y, 30, INK, 0.8, 0.5)
    return s, ''


def html_helal():
    cx, cy = HL_C
    h = BK('helal')
    h += P('k', 128, 100, 700, 'HELAL BELGELENDİRME', i=0)
    h += TITLE('Sekiz adım,', 'sürekli güvence.', 128, 144, 880, 92, 112, i0=0)
    h += P('lead', 128, 372, 800, 'HAK akreditasyonuyla helal belgelendirme: ürün ve personel için aynı sekiz adımlı yol.', 33, i=2)
    for k in range(8):
        a = -math.pi / 2 + 2 * math.pi * k / 8
        x, y = cx + HL_R * math.cos(a), cy + HL_R * math.sin(a)
        h += P('mono', int(x - 16), int(y - 12), 32, str(k + 1), extra='text-align:center;font-weight:700;color:#77183A;line-height:1;')
    steps = ['Başvuru alınır', 'Kapsam belirlenir', 'Dokümanlar incelenir', 'Denetim planlanır', 'Saha denetimi yapılır',
             'Uygunsuzluklar kapatılır', 'Belgelendirme kararı verilir', 'Gözetimle süreklilik sağlanır']
    for k, t in enumerate(steps):
        col, row = divmod(k, 4)
        x, y = 520 + 250 * col, 580 + 84 * row
        h += RULE(x, y - 8, 226, 1.0, '#00244D', 0.4)
        h += P('mono', x, y + 4, 40, f'{k + 1}', extra='color:#77183A;font-weight:700;')
        h += P('sm', x + 40, y, 190, t, 26, extra='line-height:1.25;', i=3 + k)
    h += IMG('med_m1.png', 1050, 118, 300, 300, 'Helal mutfakta ekip eğitimi', i=2)
    h += IMG('med_m2.png', 1400, 232, 350, 350, 'Ambalaj hattında helal denetim', i=3)
    h += IMG('med_m3.png', 1090, 444, 260, 260, 'Konteyner limanı ve ihracat', i=4)
    h += P('k', 1050, 742, 700, 'KAPSAM')
    h += P('sm', 1050, 782, 742, 'Gıda üretimi · Et kesim ve işleme · Yemek üretimi ve sunumu · Ambalaj · Kozmetik · Turizm · Gıda katkı maddeleri', 26)
    h += P('sm', 1050, 886, 742, '<b>Helal personel:</b> denetçi, kalite yöneticisi, kesim ve üretim personeli', 26, raw=True)
    h += FOOT('Helal')
    return h


NOTES_HELAL = ('MYK’dan ayrı ikinci hat: helal belgelendirme, HAK akreditasyonuyla. Süreç sekiz adımdır ve bir halka gibidir, çünkü son adım gözetimdir: belge verildikten sonra süreklilik denetlenir. '
               'Kapsamımız gıda üretimi, et kesim ve işleme, yemek üretimi ve sunumu, ambalaj, kozmetik, turizm ve gıda katkı maddeleri. '
               'Ürün ve hizmet belgesinin yanında helal denetçi, kalite yöneticisi, kesim ve üretim personeli için personel belgelendirme de yapıyoruz. '
               'Konteyner görseli ihracat bağlantısını hatırlatır: helal belge, yabancı pazarlarda güvenin kaydıdır.')


SLIDES2 = [
    ('takvim', 'a', art_takvim, html_takvim, NOTES_TAKVIM, ''),
    ('alan', 'd', art_alan, html_alan, NOTES_ALAN, ''),
    ('yaprak', 'b', art_yaprak, html_yaprak, NOTES_YAPRAK, ''),
    ('helal', 'a', art_helal, html_helal, NOTES_HELAL, ''),
]
