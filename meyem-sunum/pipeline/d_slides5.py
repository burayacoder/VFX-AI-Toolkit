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


# ====================================================================== yenilenen fotoğrafların alt metinleri
ALT_FIX = {          # 'eski alt' -> 'yeni alt' (fotoğraflar: data/v10_foto_secim.json)
    'Güvenlik ekipmanlı iki saha çalışanı, biri tablet kullanıyor': 'Baretli iki usta şantiyede birlikte çalışıyor',
    'Koruyucu maskeyle kaynak yapan usta, çevresinde kıvılcımlar': 'Baretli elektrikçi prizi dikkatle bağlıyor',
    'Birbirine kenetlenen iki el: güven': 'Su terazisiyle ölçüyü doğrulayan el',
    'Şantiyede plan ve kontrol listesi üzerinde yazı yazan el': 'Baretli mühendis sahada planı bilgisayarla karşılaştırıyor',
    'MYK sınavında iskele başında değerlendirici ve aday': 'Baretli iki denetçi sahada çizim ve formla kontrol yapıyor',
    'İşyerinde tablet üzerinden ihtiyaç analizi yapan iki uzman': 'Belge üzerinde ihtiyacı birlikte belirleyen eller',
    'Planlama notlarını yazan el ve dizüstü bilgisayar': 'Takvimde işaretlenmiş sınav günü',
    'Baretli çalışan grubu, sınav günü organizasyonu': 'Duvarda düzenli dizilmiş el aletleri: sınav ekipmanı',
    'Test cevap kâğıdı ve kurşun kalem: sınav değerlendirme': 'Kalemle yazılı sınav cevabı yazan el',
    'MEYEM uzmanı, katılımcı grubuna sunum yapıyor': 'Şantiyede baretli, gülümseyen inşaat ustası',
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
