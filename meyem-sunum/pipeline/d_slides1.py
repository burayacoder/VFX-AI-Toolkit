"""Slayt 1-4: kapak, imza, söz, belge."""
from d_common import *

# ====================================================================== 1 KAPAK
def art_kapak():
    cx, cy = 1430, 548
    d = iris_defs('iris', 880, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('a')
    s += rosette_flower(cx, cy, 1.38, 'url(#iris)', WINE, 0.55, 0.9)
    s += ring_bundle(cx, cy, 318, count=10, gap=3.0, a=4, nw=36, c1='url(#iris)', c2=WINE, op=0.5)
    s += f'<circle cx="{cx}" cy="{cy}" r="272" fill="{PAPER_A}"/>'
    s += circle(cx, cy, 272, WINE, 1.8, 0.9) + circle(cx, cy, 284, INK, 1.0, 0.7) + circle(cx, cy, 296, WINE, 0.8, 0.5)
    s += microring(cx, cy, 504, 'MEYEM MESLEKİ YETERLİLİK VE BELGELENDİRME MERKEZİ', 11, INK, 0.78, 'mr1')
    s += circle(cx, cy, 518, INK, 1.0, 0.55) + circle(cx, cy, 490, INK, 0.8, 0.45)
    s += ticks(cx, cy, 524, 144, 8, 16, 6, INK, 0.9, 0.35)
    s += rosette_lace(-20, 1110, 300, n=48, a=0.5, b=0.16, c=0.36, c1=INK, c2=WINE, op=0.30, sw=0.7)
    return s, d


def html_kapak():
    cx, cy = 1430, 548
    h = BK('kapak')
    h += IMG('logo_seal.png', 128, 92, 86, 84, 'MEYEM mührü')
    h += P('t1', 234, 96, 700, 'MEYEM', 40, extra='letter-spacing:1px;', i=0)
    h += P('sm', 234, 142, 760, 'Mesleki Yeterlilik ve Belgelendirme Merkezi', 26, i=0)
    h += TITLE('Ustalığın', 'resmî adı.', 128, 316, 1000, 168, 200, i0=1)
    h += P('lead', 128, 744, 760, 'Mesleki yeterlilik, mesleki eğitim ve helal belgelendirmede; Türkiye’nin her yerinde, tek çatı altında.', 34, i=3)
    h += CHIPS(['MYK YB-0079', 'TÜRKAK AB-0126-P'], 128, 920)
    h += IMG('eng_cover.png', cx - 250, cy - 250, 500, 500, 'Gravür tekniğinde iki saha çalışanı', i=2)
    h += P('mono', 128, 992, 600, 'KASIM 2026', extra='line-height:1;')
    return h


NOTES_KAPAK = ('Açılış cümlesi: MEYEM, TÜRKAK akreditasyonlu ve MYK yetkili bir sınav ve belgelendirme kuruluşudur. '
               'Slayttaki gravür, ekibimizin sahada yaptığı işi anlatır: kazan dairesinden üretim hattına kadar çalışanın bilgisini ve becerisini resmî kayda geçirmek. '
               'Başlık sözü bu yüzden “ustalığın resmî adı”: usta olan zaten bilir, biz bunu belgelendiririz. '
               'Alt satırdaki iki kod, MYK yetki numarası ve TÜRKAK akreditasyon numarasıdır.')


# ====================================================================== 2 İMZA
IMZA_L, IMZA_R, IMZA_C = 1140, 1550, 1345


def art_imza():
    cy = 548
    s = paper('b')
    s += rosette_lace(IMZA_C, cy, 470, n=72, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.17, sw=0.7)
    for x, col in ((IMZA_L, WINE), (IMZA_R, INK)):
        s += f'<circle cx="{x}" cy="{cy}" r="204" fill="#FFFFFF" fill-opacity="0.96"/>'
        s += ring_bundle(x, cy, 206, count=14, gap=2.6, a=3.4, nw=30, c1=col, c2=col, op=0.6)
        s += circle(x, cy, 246, col, 1.4, 0.8) + circle(x, cy, 202, col, 1.0, 0.5)
    s += f'<circle cx="{IMZA_C}" cy="{cy}" r="112" fill="#FFFFFF"/>'
    s += circle(IMZA_C, cy, 112, WINE, 2.0, 0.95) + circle(IMZA_C, cy, 122, INK, 0.9, 0.6) + circle(IMZA_C, cy, 130, WINE, 0.7, 0.45)
    return s, ''


def html_imza():
    cy = 548
    h = BK('imza')
    h += P('k', 128, 112, 600, 'YETKİ', i=0)
    h += TITLE('İki resmî imza,', 'tek mühür.', 128, 156, 740, 88, 112, i0=0)
    h += P('lead', 128, 392, 700, 'Belgenin değeri, arkasındaki yetkiden gelir. MYK yetkisi ve TÜRKAK akreditasyonu iki resmî dayanak; üçüncüsü MEYEM mührü.', 33, i=2)
    rows = [('MYK YETKİ NO', 'YB-0079'), ('TÜRKAK AKREDİTASYON NO', 'AB-0126-P'),
            ('HAK · OIC/SMIIC 2:2019', '2022-013'), ('HAK · OIC/SMIIC 34:2020', '2023-038')]
    y0 = 648
    for n, (a, b) in enumerate(rows):
        y = y0 + n * 56
        h += RULE(128, y, 720, 1.2, '#00244D', 0.55)
        h += P('mono', 128, y + 14, 520, a, extra='line-height:1;')
        h += P('mono', 648, y + 14, 200, b, extra='line-height:1;text-align:right;color:#77183A;font-weight:700;')
    h += RULE(128, y0 + 224, 720, 1.2, '#00244D', 0.55)
    h += P('mono', 128, 906, 760, '10+ YIL · 50.000+ BELGELENDİRİLMİŞ ADAY', extra='line-height:1;')
    # logolar
    h += IMG('logo_myk.png', IMZA_L - 82, cy - 106, 156, 202, 'MYK logosu ve YB-0079 yetki numarası', i=1)
    h += IMG('logo_turkak.png', IMZA_R - 70, cy - 106, 150, 203, 'TÜRKAK logosu ve AB-0126-P akreditasyon numarası', i=2)
    h += IMG('logo_seal.png', IMZA_C - 96, cy - 94, 192, 188, 'MEYEM mührü', i=3)
    # alt yazılar
    h += P('sm', IMZA_L - 190, 836, 380, '<b>MYK</b> · Yetkilendirilmiş Belgelendirme Kuruluşu', 26, extra='text-align:center;', raw=True)
    h += P('sm', IMZA_R - 190, 836, 380, '<b>TÜRKAK</b> · Personel belgelendirme akreditasyonu', 26, extra='text-align:center;', raw=True)
    h += FOOT('Yetki')
    return h


NOTES_IMZA = ('Belgenin değeri arkasındaki yetkiden gelir. Soldaki daire MYK yetkisidir: Yetkilendirilmiş Belgelendirme Kuruluşu, YB-0079. '
              'Sağdaki daire TÜRKAK akreditasyonudur: personel belgelendirmede TS EN ISO/IEC 17024, AB-0126-P. İkisinin kesiştiği yerde MEYEM mührü durur. '
              'Helal belgelendirmede ise iki HAK akreditasyonumuz var: OIC/SMIIC 2:2019 ve OIC/SMIIC 34:2020. '
              'Bu kayıtlar herkesin açık kaynaklardan doğrulayabileceği kayıtlardır.')


# ====================================================================== 3 SÖZ
ARCH_X = [128, 573, 1017, 1462]
ARCH_Y, ARCH_W, ARCH_H = 380, 330, 400


def art_soz():
    s = paper('a')
    s += rosette_lace(1975, -90, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.20, sw=0.7)
    for i, x in enumerate(ARCH_X):
        s += arch_outline(x, ARCH_Y, ARCH_W, ARCH_H, WINE, 1.4, 0.9, off=14)
        s += arch_outline(x, ARCH_Y, ARCH_W, ARCH_H, INK, 0.8, 0.5, off=24)
    # dördüncü kemer: büyüme basamakları
    x = ARCH_X[3]
    s += (f'<defs><clipPath id="ac"><path d="M{x} {ARCH_Y + ARCH_H} L{x} {ARCH_Y + 165} A165 165 0 0 1 {x + ARCH_W} {ARCH_Y + 165} L{x + ARCH_W} {ARCH_Y + ARCH_H}Z"/></clipPath></defs>')
    s += f'<g clip-path="url(#ac)"><rect x="{x}" y="{ARCH_Y}" width="{ARCH_W}" height="{ARCH_H}" fill="#FFFFFF" fill-opacity="0.85"/>'
    s += wave_lines(x, x + ARCH_W, ARCH_Y + 20, ARCH_Y + ARCH_H, n=44, amp=9, wl=210, c=BLUSH, op=0.8, sw=0.9, delta=0.18)
    bars = [(60, WINE_L), (118, WINE_L), (178, WINE), (240, WINE), (306, WINE_D)]
    for k, (hh, col) in enumerate(bars):
        bx = x + 28 + k * 58
        s += f'<rect x="{bx}" y="{ARCH_Y + ARCH_H - hh}" width="44" height="{hh}" fill="{col}"/>'
        for ln in range(1, 5):
            s += f'<line x1="{bx + ln * 8.8}" y1="{ARCH_Y + ARCH_H - hh}" x2="{bx + ln * 8.8}" y2="{ARCH_Y + ARCH_H}" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="0.8"/>'
    pts = [(x + 28 + k * 58 + 22, ARCH_Y + ARCH_H - hh - 14) for k, (hh, _) in enumerate(bars)]
    s += line_path(pth(pts), INK, 2.2, 0.95)
    for (px, py) in pts:
        s += f'<circle cx="{px}" cy="{py}" r="6" fill="{PAPER_A}" stroke="{INK}" stroke-width="2"/>'
    s += '</g>'
    return s, ''


def html_soz():
    h = BK('soz')
    h += P('k', 128, 100, 600, 'NEDEN BELGE', i=0)
    h += TITLE('Bir belgenin', 'dört sözü.', 128, 144, 900, 92, 112, i0=0)
    h += P('lead', 1020, 130, 772, 'Mesleki yeterlilik belgesi; çalışanın yetkinliğini, işverenin güvencesini ve sektörün uyumunu aynı kayda bağlar.', 33, i=2)
    photos = ['arch_a1.png', 'arch_a2.png', 'arch_a3.png']
    alts = ['Koşum takımıyla yüksekte çalışma güvenliği kontrolü', 'Tablet ile denetim yapan uzman', 'Depoda tablet ile kayıt tutan uzman']
    for i, x in enumerate(ARCH_X[:3]):
        h += IMG(photos[i], x, ARCH_Y, ARCH_W, ARCH_H, alts[i], i=i + 1)
    items = [('I', 'Yetkinlik', 'Bilgi ve beceri ulusal standartla ölçülür.'),
             ('II', 'Güven', 'Doğrulanabilir, tarafsız güvence.'),
             ('III', 'Uyum', 'Meslek kodu, görev ve belge birbirini tutar.'),
             ('IV', 'Avantaj', 'Uygun şartlarda daha uzun prim desteği.')]
    for i, (rn, t, b) in enumerate(items):
        x = ARCH_X[i]
        h += P('num', x, 800, 70, rn, 52, extra='font-style:italic;')
        h += P('ct', x + 76, 806, 260, t, 40)
        h += P('sm', x, 866, 330, b, 26)
    h += FOOT('Neden belge')
    return h


NOTES_SOZ = ('Dört söz, dört kemer. Yetkinlik: kişinin bilgi, beceri ve uygulama yeterliliği ulusal standartlara göre ölçülür. '
             'Güven: işveren, çalışan ve müşteri için objektif ve doğrulanabilir bir yeterlilik güvencesi oluşur. '
             'Uyum: meslek kodu, görev tanımı ve belge alanı birbirini tutar. '
             'Avantaj: uygun şartlarda SGK prim teşviklerinden daha uzun süre yararlanma imkânı doğar; son kemerdeki basamaklar bunu gösterir.')


# ====================================================================== 4 BELGE
def art_belge():
    s = paper('c')
    s += rosette_lace(446, 548, 420, n=72, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.22, sw=0.7)
    return s, ''


def html_belge():
    h = BK('belge')
    h += IMG('cert_myk.jpg', 176, 150, 540, 764, 'MYK Mesleki Yeterlilik Belgesi örneği',
             extra='transform:rotate(-3deg);box-shadow:0 22px 46px rgba(0,36,77,.24);', i=1)
    h += IMG('sticker_myk.png', 664 - 110, 842 - 110, 220, 220, 'MYK belge mührü', i=2)
    h += IMG('logo_myk.png', 664 - 30, 842 - 38, 60, 78, 'MYK logosu')
    h += P('k', 900, 112, 700, 'MYK BELGESİ', i=0)
    h += TITLE('Mesleğin,', 'resmî kimliği.', 900, 156, 892, 108, 128, i0=0)
    h += P('lead', 900, 408, 860, 'MYK Belgesi; kişinin mesleki bilgi, beceri ve yetkinliğini resmî olarak doğrular.', 34, i=2)
    cols = [('244', 'meslekte MYK belgesi zorunlu'), ('5 yıl', 'çoğu belgenin geçerlilik süresi'), ('2', 'aşamalı sınav: teorik ve uygulamalı')]
    for i, (v, l) in enumerate(cols):
        x = 900 + i * 300
        if i:
            h += VRULE(x - 22, 596, 190, 1.2, '#00244D', 0.4)
        h += P('num', x, 590, 270, v, 128, i=3 + i)
        h += P('sm', x, 736, 250, l, 26, i=3 + i)
    h += RULE(900, 884, 892, 1.2, '#00244D', 0.5)
    h += P('mono', 900, 904, 892, '5544 SAYILI KANUN · EK MD. 1', extra='line-height:1;')
    h += P('sm', 900, 944, 892, 'Belge zorunlu olan meslekte çalışan, belgelidir.', 28)
    h += FOOT('MYK belgesi')
    return h


NOTES_BELGE = ('MYK Belgesi, kişinin mesleki bilgi, beceri ve yetkinliğini resmî olarak doğrulayan belgedir; mesleğin kimlik kartı gibi düşünebilirsiniz. '
               'Üç rakam yeter: 244 meslekte belge zorunludur, belgelerin çoğu beş yıl geçerlidir ve sınav iki aşamalıdır: teorik ve uygulamalı. '
               'Zorunluluk 5544 sayılı Kanun’un Ek madde 1 hükmüne dayanır: belge zorunlu olan meslekte çalışan belgeli olur.')


SLIDES1 = [
    ('kapak', 'a', art_kapak, html_kapak, NOTES_KAPAK, 'cover'),
    ('imza', 'b', art_imza, html_imza, NOTES_IMZA, ''),
    ('soz', 'a', art_soz, html_soz, NOTES_SOZ, ''),
    ('belge', 'c', art_belge, html_belge, NOTES_BELGE, ''),
]
