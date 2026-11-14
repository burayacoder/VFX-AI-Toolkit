"""MEYEM v8 slaytları (Faz 3 örnekleri: kapak, isyeri, kapsam). Metinler faz2_hikaye.md'den."""
from v8_common import *

SCOPE_ROWS = [  # (alan, toplam, zorunlu): zorunlu paya göre sıralı
    ('İnşaat ve yapı', 13, 13), ('Makine ve üretim', 5, 5), ('Enerji ve tesisat', 5, 4),
    ('Metal ve kaynak', 3, 3), ('Taşıma ve kaldırma', 4, 2), ('Bilişim ve siber', 14, 0),
    ('Ticaret ve emlak', 6, 0), ('Yönetim ve İK', 4, 0), ('Gıda ve paketleme', 1, 0),
]
assert sum(r[1] for r in SCOPE_ROWS) == 55 and sum(r[2] for r in SCOPE_ROWS) == 27

MEDAL = 400                     # mühür madalyonu kutusu (px)
SEAL_W, SEAL_H = 228, 223       # MEYEM mührü (585×573 oranı)


def seal_group(cx, cy, i=None):
    """Kâğıt madalyon + guilloche halka (pişmiş) + MEYEM mührü."""
    h = IMG('v8_muhur_halka.png', cx - MEDAL // 2, cy - MEDAL // 2, MEDAL, MEDAL, alt='', i=i)
    h += IMG('logo_seal.png', cx - SEAL_W // 2, cy - SEAL_H // 2, SEAL_W, SEAL_H, alt='MEYEM mührü', i=i)
    return h


# ------------------------------------------------------------------ 1 kapak
def kapak():
    h = IMG('v8_kapak_foto.jpg', col(6), 0, W - col(6), H, alt='İşinin başındaki usta ve tabletle kayıt tutan MEYEM değerlendiricisi', cls='pin ph', i=0)
    h += P('wm', 128, 112, 600, 'MEYEM', i=0)
    h += P('xs', 128, 150, 640, 'Mesleki Yeterlilik ve Belgelendirme Merkezi', i=0)
    h += P('tt', 128, 340, 760, 'Ustalığı üretim durmadan belgeye dönüştürüyoruz.', tag='h1', i=1)
    h += P('bd', 128, 650, 640, 'MYK yetkili, TÜRKAK akrediteli mesleki yeterlilik sınav ve belgelendirme kuruluşu', i=2)
    h += P('xs', 128, FOOT_Y, 700, 'MYK YB-0079  ·  TÜRKAK AB-0126-P  ·  Kasım 2026', extra='line-height:1;')
    h += seal_group(col(6), 830, i=3)
    return h


NOTES_KAPAK = ("MEYEM; MYK'nın yetkilendirdiği, TÜRKAK'ın akredite ettiği bir mesleki yeterlilik sınav ve belgelendirme kuruluşudur. "
               "Bugün tek bir fikri anlatacağız: ustalığı, üretimi durdurmadan belgeye dönüştürmek. Usta işini zaten bilir. "
               "Biz bu bilgiyi ulusal standartla ölçer ve MYK Mesleki Yeterlilik Belgesiyle resmî kayda geçiririz. "
               "Sunumun sonunda sizden tek bir şey isteyeceğiz: ilk toplu sınav gününü birlikte planlamak.")


# ------------------------------------------------------------------ 5 isyeri (fotoğraf)
ISYERI_PH = (col(5), 344, W - col(5), H - 344)   # x, y, w, h: sağa ve alta taşar


def isyeri():
    x, y, w, hh = ISYERI_PH
    h = TITLE('Sınavı işyerine, tezgâhın başına getiriyoruz.')
    h += P('bd', 128, CONTENT_Y, span(4), 'İhtiyaç analizi, eğitim, sınav ve belge çalışanın kendi işinin başında. Türkiye genelinde.', i=1)
    h += P('md ac', 128, 836, span(4), 'Çalışan işinden ayrılmaz, üretim durmaz.', i=2)
    h += IMG('v8_isyeri_foto.jpg', x, y, w, hh, alt='Sahada aday iskele kurarken MEYEM değerlendiricisi formla gözlem yapıyor', cls='pin ph', i=1)
    return h


NOTES_ISYERI = ("Çalışanı sınav merkezine göndermek yerine sınavı işyerine getiriyoruz. Önce ihtiyaç analizi yerinde yapılır. "
                "Ardından eğitim, sınav ve belgelendirme çalışanın kendi işinin başında tamamlanır. İsteyen işveren için sınavı merkezimizde de planlıyoruz. "
                "Böylece çalışan işinden ayrılmaz, üretim durmaz ve iş gücü kaybı en aza iner. Bu hizmeti Türkiye genelinde veriyoruz.")


# ------------------------------------------------------------------ 6 kapsam (veri)
def kapsam():
    y0, pitch, bh = 380, 62, 30
    x0 = col(3)
    unit = span(6) / 14
    h = TITLE('Dokuz alanda 55 ulusal yeterlilikte belge veriyoruz.')
    for k, (name, n, z) in enumerate(SCOPE_ROWS):
        ry = y0 + k * pitch
        row = P('bd', 128, -4, span(3), name, extra='color:#00244D;line-height:1.2;white-space:nowrap;')
        if z:
            row += BOX(x0, 0, round(z * unit), bh, WINE)
        if n - z:
            row += BOX(x0 + round(z * unit), 0, round((n - z) * unit), bh, TINT)
        row += P('bb', x0 + round(n * unit) + 16, -2, 80, str(n))
        h += f'<div class="pin rise" style="left:0;top:{ry}px;width:{W}px;height:{bh}px;--i:{1 + k};">{row}</div>'
    lx = col(10)
    h += BOX(lx, y0 + 4, 24, 24, WINE)
    h += P('md', lx + 40, y0 - 8, span(2), '27 zorunlu', extra='color:#77183A;')
    h += BOX(lx, y0 + 72, 24, 24, TINT)
    h += P('md', lx + 40, y0 + 60, span(2), '28 gönüllü', extra='color:#2C4868;')
    h += P('xs', lx, y0 + 150, span(2), '+32 yeterlilik daha MYK onay sürecinde; 16’sı zorunlu kapsamda.')
    h += SOURCE('Kaynak: MYK Portal, Kasım 2026')
    return h


NOTES_KAPSAM = ("Yetki kapsamımız MYK Portal'a göre 55 ulusal yeterlilik; bunları dokuz alanda topladık. "
                "Tamamı zorunlu kapsamda olan alanlar: inşaat ve yapıda 13 yeterlilik, ki en büyük alan bu; ayrıca metal ve kaynakta 3, makine ve üretimde 5 yeterlilik. "
                "Bir kısmı zorunlu olan alanlar: enerji ve tesisatta 5 yeterliliğin 4'ü, taşıma ve kaldırmada 4 yeterliliğin 2'si. "
                "Gönüllü kapsamdaki alanlar: bilişim ve siberde 14, ticaret ve emlakta 6, yönetim ve insan kaynaklarında 4, gıda ve paketlemede 1 yeterlilik. "
                "Toplamda 27 yeterlilik zorunlu, 28'i gönüllü kapsamda. MYK'da onay sürecinde 32 yeterlilik daha var ve bunların 16'sı zorunlu kapsamda.")

SLIDES_V8 = [
    ('kapak', kapak, NOTES_KAPAK, 'cover'),
    ('isyeri', isyeri, NOTES_ISYERI, 'phs'),
    ('kapsam', kapsam, NOTES_KAPSAM, ''),
]
