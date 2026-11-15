"""MEYEM v9 örnek slaytları: kapak (belge yüzü), takvim (hızlanan şerit + damga), kapsam (pul sayfası)."""
import html, json, os
import v9_art as A

M2 = A.M2
URLS = os.path.join(os.path.dirname(M2), 'data', 'assets_v9.json')
MODE = {'v': 'preview'}
USED = {}

FACES = {
    'instrument-serif': {'family': 'Instrument Serif', 'href': 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap'},
    'hanken-grotesk': {'family': 'Hanken Grotesk', 'href': 'https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400..800&display=swap'},
}

CSS = """
.s{position:relative;color:#00244D;background:#F8F4EC;font-family:'Hanken Grotesk',Arial,sans-serif;counter-increment:page;overflow:hidden}
.pc{background:#E9EFF6}.pb{background:#F4E8EB}
.s::after{content:counter(page);position:absolute;right:128px;bottom:64px;font-family:'Hanken Grotesk',Arial,sans-serif;font-size:24px;font-weight:600;line-height:1;color:#2C4868}
.cover::after,.closing::after{content:""}
.pin{position:absolute;margin:0}
.bk{position:absolute}
.ey{font-size:24px;font-weight:700;letter-spacing:4px;line-height:1;color:#77183A}
.tt{font-family:'Instrument Serif',Georgia,serif;font-size:96px;font-weight:400;line-height:1;letter-spacing:-.5px;color:#00244D}
.ds{font-family:'Instrument Serif',Georgia,serif;font-size:48px;font-weight:400;line-height:1.05;color:#00244D}
.bd{font-size:32px;font-weight:400;line-height:1.4;color:#2C4868}
.bb{font-size:32px;font-weight:600;line-height:1.2;color:#00244D}
.xs{font-size:24px;font-weight:500;line-height:1.3;color:#2C4868}
.lb{font-size:24px;font-weight:700;letter-spacing:3px;line-height:1.2;color:#77183A}
.wm{font-size:32px;font-weight:800;letter-spacing:8px;line-height:1;color:#00244D}
.ph{object-fit:cover}
@keyframes rise{from{opacity:0;transform:translateY(18px)}}
@keyframes fadein{from{opacity:0}}
.rise{animation:rise .6s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i,0)*90ms)}
.fadein{animation:fadein .8s ease both;animation-delay:calc(var(--i,0)*90ms)}
"""


def tq(s):
    return str(s).replace("'", '’')


def rich(s):
    t = html.escape(tq(s), quote=False).replace('\n', '<br>')
    t = t.replace('{{', '<i style="color:#77183A">').replace('}}', '</i>')
    return t.replace('[[', '<span style="color:#77183A">').replace(']]', '</span>')


def url_for(fn):
    USED[fn] = f'{A.ASSETS}/{fn}'
    return ('file://' + f'{A.ASSETS}/{fn}') if MODE['v'] == 'preview' else json.load(open(URLS))[fn]


def P(cls, x, y, w, text, extra='', tag='p', i=None):
    st = f'left:{x}px;top:{y}px;width:{w}px;{extra}'
    if i is not None:
        st += f'--i:{min(i, 5)};'
    return f'<{tag} class="pin {cls}{" rise" if i is not None else ""}" style="{st}">{rich(text)}</{tag}>'


def IMG(fn, x, y, w, h, alt='', cls='pin', extra='', i=None):
    st = f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}'
    if i is not None:
        st += f'--i:{min(i, 5)};'
    return f'<img class="{cls}{" fadein" if i is not None else ""}" src="{url_for(fn)}" alt="{html.escape(tq(alt))}" style="{st}">'


def BK(name):
    return f'<img class="bk" src="{url_for(name + ".jpg")}" alt="" style="left:0;top:0;width:1920px;height:1080px">'


def BOX(x, y, w, h, color, extra=''):
    return f'<div class="pin" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};{extra}"></div>'


def HEAD(eyebrow, title):
    return P('ey', 128, 112, 1200, eyebrow, i=0) + P('tt', 128, 152, 1400, title, tag='h2', i=0)


def SOURCE(t):
    return P('xs', 128, 992, 1300, t, extra='line-height:1;')


def SEC(sid, inner, notes, cls=''):
    assert len(tq(notes)) <= 4000
    return (f'<section id="{sid}" class="s{(" " + cls) if cls else ""}" data-transition="fade">\n{inner}\n'
            f'<aside>{html.escape(tq(notes), quote=False)}</aside>\n</section>\n')


# ------------------------------------------------------------------ kapak
def kapak():
    x, y, w, h = A.PH
    s = BK('bk_v9_kapak')
    s += IMG('v9_kapak_foto.jpg', x, y, w, h, alt='İşinin başındaki usta ve tabletle kayıt tutan MEYEM değerlendiricisi', cls='pin ph', i=1)
    s += IMG('v8_muhur_halka.png', x - 120, y + h - 120, 240, 240, alt='', i=3)
    s += IMG('logo_seal.png', x - 70, y + h - 68, 140, 137, alt='MEYEM mührü', i=3)
    s += P('wm', 128, 150, 600, 'MEYEM', i=0)
    s += P('xs', 128, 196, 700, 'Mesleki Yeterlilik ve Belgelendirme Merkezi', i=0)
    s += P('tt', 128, 320, 820, 'Ustalığı üretim\ndurmadan {{belgeye}}\ndönüştürüyoruz.', tag='h1', i=1)
    s += BOX(128, 640, 560, 2, A.INK)
    for k, (lab, val) in enumerate((('YETKİ', 'MYK YB-0079'), ('AKREDİTASYON', 'TÜRKAK AB-0126-P'),
                                    ('STANDART', 'TS EN ISO/IEC 17024'), ('TARİH', 'Kasım 2026'))):
        s += P('lb', 128, 672 + k * 52, 260, lab, i=2)
        s += P('bb', 400, 668 + k * 52, 440, val, i=2)
    return s


N_KAPAK = ("MEYEM; MYK'nın yetkilendirdiği, TÜRKAK'ın akredite ettiği bir mesleki yeterlilik sınav ve belgelendirme kuruluşudur. "
           "Bu kapak bir belgenin yüzü gibi tasarlandı: usta fotoğrafı belge penceresinde, köşesinde MEYEM mührü. "
           "Arkadaki rozetin 55 halkası 55 yeterliliğimizi gösteriyor; şarap rengindekiler zorunlu kapsamdaki 27 yeterlilik. "
           "Bugün tek bir fikri anlatacağız: ustalığı, üretimi durdurmadan belgeye dönüştürmek. "
           "Sunumun sonunda sizden tek bir şey isteyeceğiz: ilk toplu sınav gününü birlikte planlamak.")


# ------------------------------------------------------------------ takvim
def takvim():
    ex = A.EV_X
    s = BK('bk_v9_takvim')
    s += HEAD('NEDEN ŞİMDİ', 'Dört tarih işverenin\ntakvimini belirliyor.')
    s += P('ds', ex[0] - 24, 430, 380, '23.03.2026', i=1)
    s += P('bd', ex[0] - 24, 488, 380, '40 meslek zorunlu\nlisteye girdi', i=1)
    s += P('ds', ex[1] - 24, 700, 380, '13.07.2026', i=2)
    s += P('bd', ex[1] - 24, 758, 380, "MEYEM'de 19 yeterlilik\ndaha aktif", i=2)
    s += P('ds', ex[2] + 24 - 380, 430, 380, '31.12.2026', extra='text-align:right;', i=3)
    s += P('bd', ex[2] + 24 - 380, 488, 380, '6111 teşvikinde\nson tanımlama günü', extra='text-align:right;', i=3)
    s += P('ds', ex[3] - 150, A.RY - 52, 300, '23 Mart\n2027', extra='text-align:center;color:#77183A;', i=4)
    s += P('bd', ex[3] - 150, A.RY + A.STAMP_R + 22, 300, '40 meslekte\nbelge zorunlu', extra='text-align:center;color:#00244D;', i=4)
    s += SOURCE('Kaynak: Resmî Gazete 33202; MYK Portal; SGK, Kasım 2026')
    return s


N_TAKVIM = ("Takvimi dört tarih belirliyor ve şerit de bunu anlatıyor: tarih yaklaştıkça sıklaşıyor. "
            "23 Mart 2026'da 2026/1 sayılı Tebliğ yayımlandı ve 40 meslek zorunlu listeye girdi. "
            "13 Temmuz 2026'da MYK Portal'da 19 yeterlilikte yetkimiz aktif oldu; buhar kazanı ve sıcak su kazanı operatörlüğü de bunların arasında. "
            "31 Aralık 2026, belgeli işçi alımında 6111 teşviki için işe giriş ve sisteme tanımlama yapılabilecek son gün. "
            "23 Mart 2027'de bir yıllık geçiş süresi bitiyor ve bu 40 meslekte belge zorunlu hâle geliyor; damga bunu gösteriyor. "
            "Belgelendirmeyi şimdi planlayan işveren hem teşvikten hem zamandan kazanır.")


# ------------------------------------------------------------------ kapsam
def kapsam():
    s = BK('bk_v9_kapsam')
    s += HEAD('KAPSAM', 'Dokuz alanda 55 ulusal\nyeterlilikte belge veriyoruz.')
    for k, (name, n, z) in enumerate(A.FIELDS):
        y = A.SY0 + k * A.SPITCH
        s += P('bd', 128, y + 2, 392, name, extra='color:#00244D;line-height:1.2;white-space:nowrap;')
        s += P('ds', A.SX0 + n * A.SSTEP + 4, y - 4, 90, str(n), extra=('color:#77183A;' if z else ''))
    s += P('tt', 1384, 382, 110, '27', extra='color:#77183A;', i=1)
    s += P('bd', 1490, 412, 300, 'zorunlu\nkapsamda', extra='line-height:1.1;color:#00244D;', i=1)
    s += P('tt', 1384, 502, 110, '28', i=2)
    s += P('bd', 1490, 532, 300, 'gönüllü\nkapsamda', extra='line-height:1.1;color:#00244D;', i=2)
    s += P('lb', 1330, 670, 462, 'MYK ONAY SÜRECİNDE', i=3)
    s += P('bd', 1330, 708, 462, "+32 yeterlilik daha;\n16'sı zorunlu kapsamda.", i=3)
    s += SOURCE('Kaynak: MYK Portal, Kasım 2026')
    return s


N_KAPSAM = ("Her pul bir ulusal yeterlilik: dolu şarap pullar zorunlu kapsamda, açık pullar gönüllü. Yetki kapsamımız MYK Portal'a göre 55 ulusal yeterlilik; bunları dokuz alanda topladık. "
            "Tamamı zorunlu kapsamda olan alanlar: inşaat ve yapıda 13 yeterlilik, ki en büyük alan bu; ayrıca makine ve üretimde 5, metal ve kaynakta 3 yeterlilik. "
            "Bir kısmı zorunlu olan alanlar: enerji ve tesisatta 5 yeterliliğin 4'ü, taşıma ve kaldırmada 4 yeterliliğin 2'si. "
            "Gönüllü kapsamdaki alanlar: bilişim ve siberde 14, ticaret ve emlakta 6, yönetim ve insan kaynaklarında 4, gıda ve paketlemede 1 yeterlilik. "
            "Sağ alttaki kesik çizgili pullar MYK'da onay sürecindeki 32 yeterlilik; bunların 16'sı zorunlu kapsamda.")

# ------------------------------------------------------------------ vizyon
VIS = [('Geliştiriyoruz', 'MYK belgelendirme süreçlerimizi sürekli güçlendiriyoruz.'),
       ('Mesleğe yer açıyoruz', "MYK'da karşılığı olmayan mesleği MYK ile görüşerek uygun çerçeveye ve meslek koluna yerleştiriyoruz."),
       ('Öncülük ediyoruz', "Alanımızda Türkiye'ye yön veren, örnek gösterilen kuruluş olmayı hedefliyoruz.")]


def vizyon():
    s = BK('bk_v9_vizyon')
    s += P('ey', 128, 112, 1200, 'VİZYON', i=0)
    s += P('tt', 128, 152, 1664, "Türkiye'de mesleki belgelendirmenin\nöncü kuruluşu olmayı hedefliyoruz.", tag='h2', i=0)
    for k, (h, t) in enumerate(VIS):
        x = A.VCOL[k]
        s += P('ds', x, 440, 520, h, extra=('color:#77183A;' if k == 2 else ''), i=1 + k)
        s += P('bd', x, 690, 500, t, i=1 + k)
    return s


N_VIZYON = ("Vizyonumuz üç adımdan oluşuyor. Birincisi, MYK belgelendirme süreçlerimizi sürekli geliştiriyoruz. "
            "İkincisi, MYK'da henüz karşılığı olmayan meslek gruplarını MYK ile görüşmeler yaparak uygun çerçeveye yerleştiriyor, gerektiğinde uygun bir meslek kolu oluşturulmasına katkı sağlıyoruz. "
            "Üçüncüsü, bütün bunların sonunda Türkiye'de mesleki belgelendirmenin öncü lideri olmayı hedefliyoruz. "
            "Şimdi bu hedefin neden bugün önem kazandığına bakalım.")


SLIDES = [('kapak', kapak, N_KAPAK, 'cover'), ('vizyon', vizyon, N_VIZYON, 'pb'), ('takvim', takvim, N_TAKVIM, 'pc'), ('kapsam', kapsam, N_KAPSAM, '')]
