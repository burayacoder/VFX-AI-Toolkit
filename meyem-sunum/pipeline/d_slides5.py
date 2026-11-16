"""v10: v7 (Sonnet “MEYEM Vizyon Gravür”) üzerine revizyon.
- 13. slayt (yol: iş birliği modeli) çıkar, yerine vizyon slaydı gelir.
- Fotoğraflar CC0 kaynaklardan yenilenir (aynı dosya adları); değişen görsellerin alt metinleri burada güncellenir.
- Yetki kapsamı (yaprak) ve dokuz alan (alan) slaytlarına MYK onay sürecindeki 32 yeterlilik eklenir (data/meyem_pending.json).
Çalıştırma: MEYEM_VER=10 python3 d_build.py [preview|publish]
"""
import math
from d_common import *
import d_slides1 as S1
import d_slides2 as S2
import d_slides3 as S3
import d_slides4 as V7

ORDER_V2 = ['kapak', 'imza', 'soz', 'belge', 'takvim', 'alan', 'yaprak', 'yerinde', 'durak', 'tesvik', 'referans', 'halka', 'vizyon', 'kapanis']
OVERRIDES = dict(V7.OVERRIDES)
OVERRIDES.pop('yol', None)


# ====================================================================== 13 VİZYON
VZ = [  # (x, y, r, renk): yükselen şerit üzerindeki üç madalyon
    (330, 640, 86, INK),
    (960, 545, 86, BLUE),
    (1590, 450, 108, WINE),
]
VZ_ANG = math.degrees(math.atan2(VZ[2][1] - VZ[0][1], VZ[2][0] - VZ[0][0]))


def art_vizyon():
    d = iris_defs('iris', 0, 1920, ((0, INK), (0.5, BLUE), (1, WINE)))
    s = paper('a')
    s += wave_lines(0, 1920, 330, 1000, n=34, amp=12, wl=520, c=INK, op=0.05, sw=0.8, delta=0.14)
    cx, cy = VZ[1][0], VZ[1][1]
    rib = braid(-120, 2040, cy, amp=14, wl=380, n=12, spread=2.8, delta=0.28, c1='url(#iris)', c2=WINE, op=0.62)
    s += f'<g transform="rotate({VZ_ANG:.2f} {cx} {cy})">{rib}</g>'
    for x, y, r, col in VZ:
        s += f'<circle cx="{x}" cy="{y}" r="{r + 30}" fill="{PAPER_A}" fill-opacity="0.97"/>'
        s += ring_bundle(x, y, r, count=11, gap=2.6, a=3.2, nw=22, c1=col, c2=col, op=0.9, sw=1.0)
        s += circle(x, y, r + 30, col, 1.5, 0.95) + circle(x, y, r - 4, col, 1.0, 0.6)
    x, y, r, _ = VZ[2]
    s += microring(x, y, r + 46, 'TÜRKİYE · MESLEKİ BELGELENDİRME · ÖNCÜ KURULUŞ', fs=12, color=WINE, op=0.85, uid='vz', ls=2.2)
    s += circle(x, y, r + 62, WINE, 1.0, 0.7)
    return s, d


def html_vizyon():
    h = BK('vizyon')
    h += P('k', 128, 100, 700, 'VİZYON', i=0)
    h += TITLE('Yolu açan,', 'öncü kuruluş.', 128, 144, 860, 96, 116, i0=0)
    h += P('lead', 1000, 150, 792, 'Hedefimiz, Türkiye’de mesleki belgelendirmenin öncü ve lider kuruluşu olmak.', 34, i=2)
    items = [('I', 'Gelişim', 'Her yıl daha geniş MYK kapsamı: 55 yeterlilikten 87’ye.'),
             ('II', 'Yeni meslek kolu', 'MYK’da karşılığı olmayan mesleği, MYK ile görüşerek ulusal çerçevedeki yerine taşırız.'),
             ('III', 'Öncü lider', 'Mesleki belgelendirmede Türkiye’ye yol gösteren kuruluş.')]
    for k, ((rn, t, d_), (x, y, r, col)) in enumerate(zip(items, VZ)):
        h += P('num', x - 80, y - 50, 160, rn, 72 if k < 2 else 84, extra=f'text-align:center;font-style:italic;color:{col};', i=2 + k)
        ty = y + r + (78 if k == 2 else 46)
        h += P('ct', x - 190, ty, 380, t, 40, extra='text-align:center;' + ('color:#77183A;' if k == 2 else ''), i=2 + k)
        sw_ = 480 if k < 2 else 400
        h += P('sm', x - sw_ // 2, ty + 54, sw_, d_, 26, extra='text-align:center;', i=2 + k)
    h += FOOT('Vizyon')
    return h


NOTES_VIZYON = ('Vizyonumuzu üç adımda anlatıyoruz ve şerit soldan sağa yükseliyor. '
                'Birincisi gelişim: MYK belgelendirmesindeki kapsamımızı her yıl büyütüyoruz; bugün 55 ulusal yeterlilikte yetkiliyiz, onay sürecindeki 32 yeterlilikle bu sayı 87’ye çıkıyor. '
                'İkincisi yeni meslek kolu: sahada ihtiyaç olan ama MYK’da henüz karşılığı bulunmayan meslekleri boş bırakmıyoruz. '
                'MYK ile görüşmeler yürütüyor, mesleğin ulusal yeterlilik çerçevesinde doğru yere oturmasına ve uygun bir meslek kolunun oluşmasına öncülük ediyoruz. '
                'Üçüncüsü öncü liderlik: bütün bu birikimle Türkiye’de mesleki belgelendirmede yol gösteren, örnek alınan kuruluş olmayı hedefliyoruz.')

OVERRIDES['vizyon'] = ('a', art_vizyon, html_vizyon, NOTES_VIZYON, '')


# ====================================================================== 7 YAPRAK: 55 + 32
# 55 yetkili yeterlilik alan sırasıyla açıktan koyuya; MYK onay sürecindeki 32 yeterlilik en koyu tonla rozeti tamamlar.
N_ON, Z_ON = 32, 16                       # onay sürecindeki yeterlilik / bunların zorunlu olanları
N_ALL = 55 + N_ON
FILL10 = list(V7.FILL) + [True] * Z_ON + [False] * (N_ON - Z_ON)
assert len(FILL10) == N_ALL and sum(V7.FILL) == 27
YP10_C = (1250, 540)
YP10_R0, YP10_R1 = 138, 362


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def _mix(c0, c1, t):
    a, b = _hex(c0), _hex(c1)
    return '#%02X%02X%02X' % tuple(round(a[k] + (b[k] - a[k]) * t) for k in range(3))


def _ramp3(c0, c1, c2, t):
    return _mix(c0, c1, t / 0.5) if t <= 0.5 else _mix(c1, c2, (t - 0.5) / 0.5)


RAMP = [_ramp3('#EBAABE', '#C25B7F', '#7A1A3D', i / 54) for i in range(55)] + [_mix('#560722', '#24000A', i / (N_ON - 1)) for i in range(N_ON)]


def petal_ring_ramp(cx, cy, r0, r1, fills, colors, wid=1.12, veins=3, a0=-math.pi / 2, sw=0.9):
    n = len(fills)
    out = []
    for i in range(n):
        a = a0 + 2 * math.pi * i / n
        hw = (math.pi / n) * wid
        d = petal_path(cx, cy, r0, r1, a, hw)
        col = colors[i]
        if fills[i]:
            out.append(f'<path d="{d}" fill="{col}" fill-opacity="0.95" stroke="{col}" stroke-width="{sw}"/>')
            vc, vo = '#FFFFFF', 0.4
        else:
            out.append(f'<path d="{d}" fill="{col}" fill-opacity="0.58" stroke="{col}" stroke-width="{sw + 0.4}" stroke-opacity="1"/>')
            vc, vo = col, 0.7
        for v in range(1, veins + 1):
            f = v / (veins + 1)
            rr0 = r0 + (r1 - r0) * 0.10
            rr1 = r0 + (r1 - r0) * (0.52 + 0.30 * (1 - abs(f - 0.5) * 2))
            aa = a + (f - 0.5) * 2 * hw * 0.55
            out.append(line_path(f'M{f1(cx + rr0 * math.cos(aa))} {f1(cy + rr0 * math.sin(aa))}L{f1(cx + rr1 * math.cos(aa))} {f1(cy + rr1 * math.sin(aa))}', vc, 0.7, vo))
    return ''.join(out)


def _ang(idx):
    return -math.pi / 2 + 2 * math.pi * idx / N_ALL


def art_yaprak10():
    cx, cy = YP10_C
    s = paper('b')
    s += rosette_lace(cx, cy, 440, n=72, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.13, sw=0.7)
    s += petal_ring_ramp(cx, cy, YP10_R0, YP10_R1, FILL10, RAMP)
    s += f'<circle cx="{cx}" cy="{cy}" r="{YP10_R0 - 10}" fill="{PAPER_B}"/>'
    s += circle(cx, cy, YP10_R0 - 10, INK, 1.2, 0.7) + circle(cx, cy, YP10_R0 - 22, WINE, 0.9, 0.55)
    for g, _ in V7.GROUPS:                                  # alan sınırları
        a = _ang(V7.GSTART[g] - 0.5)
        s += line_path(f'M{f1(cx + (YP10_R1 + 12) * math.cos(a))} {f1(cy + (YP10_R1 + 12) * math.sin(a))}L{f1(cx + (YP10_R1 + 34) * math.cos(a))} {f1(cy + (YP10_R1 + 34) * math.sin(a))}', INK, 1.4, 0.8)
    a0, a1 = _ang(55 - 0.5), _ang(N_ALL - 0.5)            # +32 yayı
    s += line_path(f'M{f1(cx + (YP10_R1 + 12) * math.cos(a0))} {f1(cy + (YP10_R1 + 12) * math.sin(a0))}L{f1(cx + (YP10_R1 + 40) * math.cos(a0))} {f1(cy + (YP10_R1 + 40) * math.sin(a0))}', WINE_D, 2.4, 1)
    s += f'<path d="{arc_path(cx, cy, YP10_R1 + 26, a0, a1)}" fill="none" stroke="{WINE_D}" stroke-width="3.2" stroke-linecap="round"/>'
    s += ticks(cx, cy, YP10_R1 + 44, 110, 5, 10, 5, INK, 0.9, 0.35)
    return s, ''


def html_yaprak10():
    cx, cy = YP10_C
    h = BK('yaprak')
    h += P('k', 128, 100, 700, 'YETKİ KAPSAMI', i=0)
    h += TITLE('55 + 32 yaprak,', 'tek rozet.', 128, 144, 800, 84, 112, i0=0)
    h += P('lead', 128, 362, 640, 'Her yaprak bir ulusal yeterlilik; tam dolu yapraklar zorunlu, yarı dolu yapraklar gönüllü. En koyu 32 yaprak MYK onay sürecinde.', 30, i=2)
    y0 = 516
    cz, cg, cw = 500, 624, 124
    h += P('mono', 176, y0, 320, 'ALAN', extra='line-height:1;letter-spacing:1px;')
    h += P('mono', cz, y0, cw, 'ZORUNLU', extra='line-height:1;letter-spacing:1px;text-align:right;color:#77183A;')
    h += P('mono', cg, y0, cw, 'GÖNÜLLÜ', extra='line-height:1;letter-spacing:1px;text-align:right;')
    y1, dy = y0 + 34, 34
    for k, (g, name) in enumerate(V7.GROUPS):
        y = y1 + dy * k
        n, z = V7.CNT[g]
        h += RULE(128, y, 620, 1.0, '#00244D', 0.35)
        h += P('mono', 128, y + 7, 44, str(k + 1), extra='color:#77183A;font-weight:700;line-height:1;')
        h += P('sm', 176, y + 3, 320, name, 26, extra='line-height:1.15;', i=3)
        h += P('mono', cz, y + 7, cw, str(z) if z else '–', extra='line-height:1;text-align:right;color:#77183A;font-weight:700;letter-spacing:0;')
        h += P('mono', cg, y + 7, cw, str(n - z) if n - z else '–', extra='line-height:1;text-align:right;letter-spacing:0;')
    y = y1 + dy * 9
    h += RULE(128, y, 620, 2.0, '#580721', 0.9)
    h += f'<div class="pin" style="left:128px;top:{y + 9}px;width:30px;height:16px;border-radius:8px;background:#580721"></div>'
    h += P('sm', 176, y + 3, 320, 'MYK onay sürecinde', 26, extra='line-height:1.15;color:#580721;font-weight:700;', i=4)
    h += P('mono', cz, y + 7, cw, str(Z_ON), extra='line-height:1;text-align:right;color:#580721;font-weight:700;letter-spacing:0;')
    h += P('mono', cg, y + 7, cw, str(N_ON - Z_ON), extra='line-height:1;text-align:right;color:#580721;letter-spacing:0;')
    h += RULE(128, y + dy, 620, 1.0, '#00244D', 0.35)
    for k, (g, name) in enumerate(V7.GROUPS):
        n, z = V7.CNT[g]
        a = _ang(V7.GSTART[g] + (n - 1) / 2.0)
        r = YP10_R1 + 64
        x, yy = cx + r * math.cos(a), cy + r * math.sin(a)
        h += P('mono', int(x - 19), int(yy - 19), 38, str(k + 1),
               extra='text-align:center;line-height:38px;height:38px;border-radius:19px;background:#77183A;color:#FFFFFF;font-weight:700;letter-spacing:0;')
    a = _ang(55 + (N_ON - 1) / 2.0)
    r = YP10_R1 + 70
    x, yy = cx + r * math.cos(a), cy + r * math.sin(a)
    h += P('mono', int(x - 40), int(yy - 19), 80, '+32',
           extra='text-align:center;line-height:38px;height:38px;border-radius:19px;background:#580721;color:#FFFFFF;font-weight:700;letter-spacing:0;')
    h += P('num', cx - 140, cy - 116, 280, '55', 112, extra='text-align:center;', i=2)
    h += P('num', cx - 100, cy + 20, 200, '+32', 52, extra='text-align:center;color:#580721;', i=3)
    h += P('mono', cx - 100, cy + 78, 200, 'YETERLİLİK', extra='text-align:center;letter-spacing:1px;line-height:1;')
    h += FOOT()
    return h


NOTES_YAPRAK10 = ('Rozetteki her yaprak bir ulusal yeterlilik. Açıktan koyuya giden elli beş yaprak bugünkü yetki kapsamımız; numaralar dokuz alanı gösterir. '
                  'En koyu otuz iki yaprak MYK onay sürecindeki yeterlilikler; on altısı zorunlu kapsamda. Onaylarla rozet seksen yedi yaprağa tamamlanıyor. '
                  'Tablo her alanda kaç yeterliliğin zorunlu, kaçının gönüllü olduğunu gösterir. Bugün yirmi yedi yeterlilik zorunlu, yirmi sekizi gönüllü. '
                  'Zorunluluk yalnızca tehlikeli ve çok tehlikeli işlerde, Çalışma Bakanlığı tebliğleriyle getirilir. Bu yüzden inşaat, kaynak, makine, vinç ve forklift gibi saha meslekleri zorunlu; '
                  'bilişim ve siber güvenlik, ticaret ve yönetim yeterlilikleri hiçbir tebliğde yer almadığı için gönüllüdür. Bu belgeleri firmalar nitelik ve kariyer kanıtı olarak tercih eder.')

OVERRIDES['yaprak'] = ('b', art_yaprak10, html_yaprak10, NOTES_YAPRAK10, '')


# ====================================================================== 6 ALAN: zorunlu / gönüllü açık yazım, +32
def html_alan10():
    TX, TY, TS = V7.TX, V7.TY, V7.TS
    h = BK('alan')
    h += P('k', 128, 76, 600, 'KAPSAM', i=0)
    h += TITLE('Dokuz alan,', 'tek çatı.', 128, 112, 800, 80, 98, i0=0)
    h += P('lead', 1000, 112, 792, 'MYK Portal kaydındaki 55 yeterlilik dokuz alanda; 32 yeterlilik daha MYK onay sürecinde. Çubuk, alandaki zorunlu payı gösterir.', 33, i=2)
    alts = {'insaat': 'Kırmızı baretli ve eldivenli inşaat ustası çekiçle çalışıyor', 'metal': 'Kaynak maskesi ve eldiveniyle çalışan kaynakçı',
            'makine': 'Koruyucu gözlükle tezgâh başında çalışan operatör', 'enerji': 'Baretli tesisatçı ölçü aletiyle kontrol yapıyor',
            'tasima': 'Baretli ve reflektif yelekli forklift operatörü', 'gida': 'Bone takan çalışanlar gıda hattında ürün ayıklıyor',
            'ticaret': 'Market kasasında müşteriye hizmet veren kasiyer', 'yonetim': 'Toplantıda görüş paylaşan ekip', 'bilisim': 'Veri merkezinde sunucu kabinleri'}
    for k, (g, name) in enumerate(V7.GROUPS):
        r, c = divmod(k, 5)
        x, y = TX[c], TY[r]
        n, z = V7.CNT[g]
        h += IMG(f'tile_{g}.jpg', x, y, TS - 12, TS - 12, alts[g], extra='border:6px solid #FFFFFF;box-shadow:0 12px 26px rgba(0,36,77,.18);', cls='pin ph', i=2 + k)
        by = y + TS - 6 - 90
        h += f'<div class="pin" style="left:{x + 6}px;top:{by}px;width:{TS - 12}px;height:90px;background:rgba(255,255,255,.93)"></div>'
        h += P('ct', x + 18, by + 8, TS - 36, name, 26, extra='line-height:1.15;font-weight:700;')
        parts = ([f'{z} zorunlu'] if z else []) + ([f'{n - z} gönüllü'] if n - z else [])
        h += P('sm', x + 18, by + 40, TS - 36, ' · '.join(parts), 24, extra='line-height:1.2;white-space:nowrap;')
        h += RULE(x + 18, by + 76, TS - 36, 6, '#DAC1CA', 1.0)
        if z:
            h += RULE(x + 18, by + 76, round((TS - 36) * z / n), 6, '#77183A', 1.0)
    x, y = TX[4], TY[1]
    h += P('num', x, y + 2, 180, '55', 140)
    h += P('num', x + 164, y + 48, 124, '+32', 60, extra='color:#580721;')
    h += P('sm', x, y + 158, 288, 'yeterlilik; +32 onayda', 26)
    h += f'<div class="pin" style="left:{x}px;top:{y + 206}px;width:46px;height:14px;border-radius:7px;background:#77183A"></div>'
    h += P('sm', x + 60, y + 196, 228, '27 zorunlu', 26)
    h += f'<div class="pin" style="left:{x}px;top:{y + 250}px;width:43px;height:11px;border-radius:7px;border:1.5px solid #00244D"></div>'
    h += P('sm', x + 60, y + 240, 228, '28 gönüllü', 26)
    h += FOOT()
    return h


NOTES_ALAN10 = ('Dokuz alan, tek çatı. MYK Portal’daki 55 ulusal yeterliliğin tamamı bu dokuz alanda toplanıyor. '
                'Üst sıra sahanın zorunlu meslekleri: inşaat ve yapıda on üç, metal ve kaynakta üç, makine ve üretimde beş yeterliliğin hepsi zorunlu. '
                'Enerji ve tesisatta beş yeterliliğin dördü, taşıma ve kaldırmada dördün ikisi zorunlu. '
                'Alt sıradaki gıda ve paketleme, ticaret ve emlak, yönetim ve insan kaynakları, bilişim ve siber alanlarındaki yeterlilikler gönüllü: bu meslekler Bakanlığın zorunluluk tebliğlerinde yer almıyor. '
                'Toplamda yirmi yedi yeterlilik zorunlu, yirmi sekizi gönüllü. Otuz iki yeterlilik daha MYK onay sürecinde; onaylarla kapsam seksen yediye çıkıyor.')

OVERRIDES['alan'] = ('d', V7.art_alan, html_alan10, NOTES_ALAN10, '')


# ====================================================================== yenilenen fotoğrafların alt metinleri
ALT_FIX = {          # 'eski alt' -> 'yeni alt' (fotoğraflar: data/v10_foto_secim.json)
    'Güvenlik ekipmanlı iki saha çalışanı, biri tablet kullanıyor': 'Baret, yelek ve eldivenli ekip sahada birlikte çalışıyor',
    'Koruyucu maskeyle kaynak yapan usta, çevresinde kıvılcımlar': 'Baretli elektrikçi prizi dikkatle bağlıyor',
    'Birbirine kenetlenen iki el: güven': 'İş eldivenli eller ölçüyü kalemle işaretliyor',
    'Şantiyede plan ve kontrol listesi üzerinde yazı yazan el': 'Baretli mühendis sahada planı bilgisayarla karşılaştırıyor',
    'MYK sınavında iskele başında değerlendirici ve aday': 'Baretli iki denetçi sahada çizim ve formla kontrol yapıyor',
    'İşyerinde tablet üzerinden ihtiyaç analizi yapan iki uzman': 'Belge üzerinde ihtiyacı birlikte belirleyen eller',
    'Planlama notlarını yazan el ve dizüstü bilgisayar': 'Takvimde işaretlenmiş sınav günü',
    'Baretli çalışan grubu, sınav günü organizasyonu': 'Duvarda düzenli dizilmiş el aletleri: sınav ekipmanı',
    'Test cevap kâğıdı ve kurşun kalem: sınav değerlendirme': 'Kalemle yazılı sınav cevabı yazan el',
    'MEYEM uzmanı, katılımcı grubuna sunum yapıyor': 'Baretli, reflektif yelekli ve koruyucu gözlüklü, gülümseyen saha çalışanı',
    'Güvenlik yeleği ve bareti ile şantiyede çalışan işçi': 'Kırmızı baretli inşaat ustası çekiçle çalışıyor',
    'Atölyede maskeyle kaynak yapan usta': 'Atölyede kaynak maskesiyle çalışan kaynakçı',
    'Torna tezgâhında talaş kaldıran kesici uç': 'Tezgâh başında koruyucu gözlükle çalışan operatör',
    'Bareti ve gözlüğüyle prizde çalışan elektrikçi': 'Baretli tesisatçı ölçü aletiyle kontrol yapıyor',
    'Depoda paletli yük taşıyan forklift operatörü': 'Depoda forklift kullanan operatör',
    'Gıda üretim hattında şişelenen ürünler': 'Gıda işleme hattında ürün ayıklayan çalışanlar',
    'Cam cepheli kurumsal bina': 'Market kasasında müşteriye hizmet veren kasiyer',
    'Beş kişilik kurumsal ekip': 'Toplantıda görüş paylaşan ekip',
    'Ağ cihazına bağlanan kablolar': 'Veri merkezinde sunucu kabinleri',
}


def _patch(fn):
    def w():
        h = fn()
        for a, b in ALT_FIX.items():
            h = h.replace(f'alt="{esc(a)}"', f'alt="{esc(b)}"')
        return h
    return w


for sid, (tone, art_, htm_, notes_, cls_) in list(OVERRIDES.items()):
    OVERRIDES[sid] = (tone, art_, _patch(htm_), notes_, cls_)
