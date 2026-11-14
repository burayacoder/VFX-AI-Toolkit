"""Slayt 9-16: eğitim, yerinde, durak, teşvik, referans, halka, yol, kapanış."""
import math
from d_common import *


# ====================================================================== 9 EĞİTİM
def art_egitim():
    s = paper('c')
    s += rosette_lace(1250, 560, 420, n=66, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    # fotoğrafın arkasında kayık çerçeve
    s += f'<rect x="1018" y="124" width="700" height="473" fill="none" stroke="{WINE}" stroke-width="1.4" stroke-opacity="0.85"/>'
    s += f'<rect x="1030" y="136" width="700" height="473" fill="none" stroke="{INK}" stroke-width="0.9" stroke-opacity="0.5"/>'
    return s, ''


def html_egitim():
    h = BK('egitim')
    h += P('k', 128, 76, 600, 'MESLEKİ EĞİTİM BELGESİ', i=0)
    h += TITLE('Eğitim,', 'kayıt altında.', 128, 112, 640, 96, 116, i0=0)
    h += P('body', 128, 336, 600, '6331 sayılı Kanun kapsamında, tehlikeli ve çok tehlikeli işlerde belirlenen mesleklerde Mesleki Eğitim Belgesi zorunludur. MEYEM bu kapsamda eğitim ve belgelendirme sunar.', 30, i=2)
    areas = ['Tehlikeli ve çok tehlikeli işler', 'Yüksekte çalışma', 'Makine ve üretim', 'Depolama ve sevkiyat', 'Kazan ve tesis işletme', 'Yapı ve inşaat']
    for k, t in enumerate(areas):
        col, row = divmod(k, 3)
        x, y = 128 + 310 * col, 630 + 100 * row
        h += RULE(x, y - 10, 290, 1.0, '#00244D', 0.45)
        h += P('mono', x, y + 4, 50, f'0{k + 1}', extra='color:#77183A;font-weight:700;')
        h += P('sm', x + 52, y, 238, t, 26, extra='line-height:1.2;font-weight:500;color:#00244D;', i=3 + k)
    h += IMG('train_big.jpg', 1000, 110, 680, 453, 'Koşum takımı ve baret ile yüksekte çalışma eğitimi',
             extra='border:10px solid #FFFFFF;box-sizing:content-box;box-shadow:0 16px 36px rgba(0,36,77,.20);', cls='pin ph', i=1)
    h += IMG('cert_train.jpg', 800, 500, 650, 460, 'Mesleki Eğitim Belgesi örneği',
             extra='transform:rotate(-2.5deg);box-shadow:0 22px 46px rgba(0,36,77,.26);', i=2)
    h += FOOT('Mesleki eğitim')
    return h


NOTES_EGITIM = ('MYK belgesiyle mesleki eğitim belgesi iki ayrı yükümlülüktür. 6331 sayılı Kanun kapsamında tehlikeli ve çok tehlikeli işlerde belirlenen mesleklerde Mesleki Eğitim Belgesi zorunludur. '
                'Altı alanı gösteriyoruz: tehlikeli işler, yüksekte çalışma, makine ve üretim, depolama ve sevkiyat, kazan ve tesis işletme, yapı ve inşaat. '
                'İşletmeye özel mesleki eğitim programları kuruyoruz; sağdaki örnek belge, Mersin Üniversitesi Kariyer Merkezi ile birlikte düzenlenen bir eğitim programının belgesidir. '
                'Eğitim yapılır, sınav yapılır, belge kayda geçer.')


# ====================================================================== 10 YERİNDE
def art_yerinde():
    s = paper('d')
    s += rosette_lace(1990, 1150, 420, n=66, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.14, sw=0.7)
    s += f'<rect x="764" y="158" width="1012" height="675" fill="none" stroke="{WINE}" stroke-width="1.4" stroke-opacity="0.85"/>'
    s += f'<rect x="752" y="170" width="1012" height="675" fill="none" stroke="{INK}" stroke-width="0.9" stroke-opacity="0.5"/>'
    s += wave_lines(128, 740, 930, 960, n=8, amp=6, wl=240, c=INK, op=0.25, sw=0.8, delta=0.3)
    return s, ''


def html_yerinde():
    h = BK('yerinde')
    h += P('k', 128, 76, 600, 'YERİNDE SINAV', i=0)
    h += TITLE('Sınav,', 'tezgâhın başında.', 128, 112, 640, 96, 92, i0=0)
    h += P('lead', 128, 340, 600, 'MEYEM belgelendirme ihtiyacınızı yerinde analiz eder; eğitim ve sınavı işyerinizde yaparak iş gücü kaybını en aza indirir.', 32, i=2)
    rows = ['Yerinde eğitim', 'Yerinde sınav', 'Yerinde belgelendirme']
    for k, t in enumerate(rows):
        y = 640 + 90 * k
        h += RULE(128, y - 12, 600, 1.2, '#00244D', 0.5)
        h += P('mono', 128, y + 14, 60, f'0{k + 1}', extra='color:#77183A;font-weight:700;')
        h += P('ct', 196, y, 540, t, 40, i=3 + k)
    h += IMG('onsite_big.jpg', 764, 158, 1012, 675, 'MYK sınavında iskele başında değerlendirici ve aday', extra='border-radius:4px;', cls='pin ph', i=1)
    h += IMG('sticker_yerinde.png', 790 - 112, 800 - 112, 224, 224, 'Yerinde eğitim, sınav ve belgelendirme mührü', i=4)
    h += IMG('logo_seal.png', 790 - 42, 800 - 41, 84, 82, 'MEYEM mührü')
    h += FOOT('Yerinde sınav')
    return h


NOTES_YERINDE = ('Markanın en güçlü cümlesi burada: çalışanı sınav merkezine göndermek yerine sınavı işyerine getiriyoruz. '
                 'Önce ihtiyaç analizi yerinde yapılır; sonra eğitim, sınav ve belgelendirme çalışanın tezgâhının başında tamamlanır. '
                 'Fotoğraftaki sahne bunu anlatıyor: değerlendirici elinde formla, aday iskelenin başında. '
                 'Böylece çalışanlar işten ayrılmaz, üretim durmaz ve iş gücü kaybı en aza iner.')


# ====================================================================== 11 DURAK
DK_X = [270, 615, 960, 1305, 1650]
DK_Y = 600


def art_durak():
    d = iris_defs('iris', 0, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('b')
    s += braid(-20, 1940, DK_Y, amp=34, wl=520, n=22, spread=3.0, delta=0.24, c1='url(#iris)', c2=WINE, op=0.55)
    for x in DK_X:
        s += f'<circle cx="{x}" cy="{DK_Y}" r="106" fill="{PAPER_B}"/>'
        s += circle(x, DK_Y, 106, WINE, 2.4, 0.95) + circle(x, DK_Y, 114, INK, 0.9, 0.55)
    return s, d


def html_durak():
    h = BK('durak')
    h += P('k', 128, 76, 600, 'SÜREÇ', i=0)
    h += TITLE('Beş durak,', 'bir belge.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Tek muhatapla, ihtiyaç analizinden belgelendirmeye.', 34, i=2)
    st = [('İhtiyaç analizi', 'Hangi çalışan, hangi belge?'), ('Planlama', 'Sınav günü, grup ve süre.'),
          ('Organizasyon', 'Sınav yeri, ekipman, görevliler.'), ('Değerlendirme', 'Teorik ve uygulamalı sınav.'),
          ('Belgelendirme', 'Karar, belge ve MYK kaydı.')]
    alts = ['Depoda ihtiyaç analizi yapan uzmanlar', 'Planlama toplantısında tahta başında uzman', 'Fabrika sahasında sınav organizasyonu',
            'Uygulamalı sınav değerlendirme formu', 'MYK mühürlü yeterlilik belgesi']
    for k, x in enumerate(DK_X):
        h += P('mono', x - 140, DK_Y - 186, 280, f'ADIM 0{k + 1}', extra='text-align:center;color:#77183A;font-weight:700;', i=2 + k)
        h += IMG(f'proc_p{k + 1}.png', x - 95, DK_Y - 95, 190, 190, alts[k], i=2 + k)
        h += P('ct', x - 140, DK_Y + 134, 280, st[k][0], 34, extra='text-align:center;', i=2 + k)
        h += P('sm', x - 140, DK_Y + 184, 280, st[k][1], 26, extra='text-align:center;', i=2 + k)
    h += P('mono', 128, 908, 1664, 'MYK YETKİLİ KURULUŞ · UYGUN YETERLİLİKLERDE ONLINE SINAV · ŞEFFAF · UZMAN · GÜVENİLİR', extra='line-height:1;')
    h += FOOT('Süreç')
    return h


NOTES_DURAK = ('Beş durak, tek muhatap. İhtiyaç analizi: hangi çalışan hangi belgeyi almalı? Planlama: sınav günü, grup ve süre. Organizasyon: sınav yeri, ekipman ve görevliler. '
               'Değerlendirme: teorik ve uygulamalı sınav. Belgelendirme: karar, belge ve MYK kaydı. '
               'Uygun yeterliliklerde online sınav da yapılabiliyor. Müşteri, her durakta kime ulaşacağını bilir; bu yüzden süreç şeffaf ve takip edilebilir kalır.')


# ====================================================================== 12 TEŞVİK
TV_C = (430, 650)
TV_R = [280, 220, 160, 100]
TV_F = [54, 48, 30, 24]
TV_COL = [WINE, WINE_L, INK, BLUE]


def art_tesvik():
    cx, cy = TV_C
    s = paper('c')
    s += rosette_lace(1995, 1175, 380, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.13, sw=0.7)
    for r, f, col in zip(TV_R, TV_F, TV_COL):
        s += arc_gauge(cx, cy, r, f / 60.0, col, 40, track=BLUSH, track_op=0.7)
    s += ticks(cx, cy, 310, 60, 8, 18, 5, INK, 1.0, 0.45)
    s += circle(cx, cy, 70, INK, 1.0, 0.5) + circle(cx, cy, 60, WINE, 0.8, 0.4)
    return s, ''


def html_tesvik():
    cx, cy = TV_C
    h = BK('tesvik')
    h += P('k', 128, 76, 700, '6111 SGK TEŞVİĞİ', i=0)
    h += TITLE('Teşvik süresi,', 'belgeyle uzar.', 128, 112, 900, 80, 98, i0=0)
    for r, f, col in zip(TV_R, TV_F, TV_COL):
        h += P('numb', cx - 150, cy - r - 17, 138, f'{f} ay', 30, extra=f'text-align:right;color:{col};letter-spacing:0;')
    h += P('mono', cx - 60, cy - 14, 120, '60 AY', extra='text-align:center;line-height:1;font-size:24px;color:#2C4868;')
    # sağ üst: iki rakam
    h += P('numb', 1000, 96, 400, '31.12.2026', 52, i=2)
    h += P('sm', 1000, 162, 380, 'işe giriş ve sisteme tanımlama için son gün', 26, i=2)
    h += P('numb', 1440, 96, 352, '5 puan', 52, i=3)
    h += P('sm', 1440, 162, 352, 'imalatta prim indirimi, 31.12.2026’ya kadar', 26, i=3)
    # tablo
    X0, X1, X2 = 820, 1240, 1530
    h += P('mono', X1, 380, 270, 'İŞKUR KAYDI YOK', extra='color:#2C4868;line-height:1;')
    h += P('mono', X2, 380, 262, 'İŞKUR KAYITLI', extra='color:#2C4868;line-height:1;')
    rows = [('18–29 yaş erkek,<br>18 yaş üstü kadın', '48 ay', '54 ay', WINE_L, WINE),
            ('29 yaş üstü erkek', '24 ay', '30 ay', BLUE, INK),
            ('Çalışırken belge alanlar', '+12 ay', '', WINE, WINE)]
    for k, (lab, a, b, ca, cb) in enumerate(rows):
        y = 430 + 170 * k
        h += RULE(X0, y, 972, 1.2, '#00244D', 0.5)
        h += P('ct', X0, y + 46, 380, lab, 32, raw=True, extra='font-weight:600;line-height:1.2;')
        h += P('num', X1, y + 18, 280, a, 100, extra=f'color:{ca};', i=3 + k)
        if b:
            h += P('num', X2, y + 18, 262, b, 100, extra=f'color:{cb};', i=3 + k)
        else:
            h += P('sm', X2, y + 56, 262, 'ek süre; diğer şartlar sağlanırsa', 26)
    h += RULE(X0, 430 + 170 * 3, 972, 1.2, '#00244D', 0.5)
    h += FOOT('Teşvik')
    return h


NOTES_TESVIK = ('MYK belgeli işçi alan işveren, 6111 sayılı teşvik kapsamında prim desteği süresinden yararlanır; belge, bu süreyi uzatabilir. '
                'Halka göstergesi altmış aylık bir daireyi temsil ediyor: on sekiz ile yirmi dokuz yaş arası erkekler ve on sekiz yaş üstü kadınlar için kırk sekiz ay, İŞKUR kaydı varsa elli dört ay; '
                'yirmi dokuz yaş üstü erkekler için yirmi dört ay, İŞKUR kaydı varsa otuz ay. Belgesini çalışırken alanlar için on iki ay ek süre imkânı var. '
                'Son tanımlama günü 31 Aralık 2026; imalatta prim indirimi de aynı tarihe kadar beş puan.')


# ====================================================================== 13 REFERANS
def art_referans():
    s = paper('a')
    s += rosette_lace(1990, -80, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    x0, y0, w, hh = 128, 352, 1664, 571
    s += f'<rect x="{x0 - 14}" y="{y0 - 14}" width="{w + 28}" height="{hh + 28}" fill="#FFFFFF" stroke="{INK}" stroke-width="1.4" stroke-opacity="0.7"/>'
    s += f'<rect x="{x0 - 26}" y="{y0 - 26}" width="{w + 52}" height="{hh + 52}" fill="none" stroke="{WINE}" stroke-width="0.9" stroke-opacity="0.7"/>'
    for (px, py) in ((x0 - 26, y0 - 26), (x0 + w + 26, y0 - 26), (x0 - 26, y0 + hh + 26), (x0 + w + 26, y0 + hh + 26)):
        s += f'<circle cx="{px}" cy="{py}" r="16" fill="{PAPER_A}" stroke="{WINE}" stroke-width="2"/>' + circle(px, py, 8, INK, 1.2, 0.8)
    return s, ''


def html_referans():
    h = BK('referans')
    h += P('k', 128, 76, 600, 'REFERANSLAR', i=0)
    h += TITLE('Referansımız,', 'saha.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Sanayiden gıdaya, enerjiden perakendeye; çalışanlarını MEYEM ile belgelendiren kuruluşlardan bazıları.', 33, i=2)
    h += IMG('wall.jpg', 128, 352, 1664, 571, 'Referans kuruluşların logoları', i=1)
    h += FOOT('Referanslar')
    return h


NOTES_REFERANS = ('Logo duvarını tek tek okumayın. Karşınızdaki müşterinin sektöründen bir iki isme dokunun: gıda ise gıda firmalarına, enerji ise enerji firmalarına. '
                  'Mesaj basit: sahada çalışan firmalar çalışanlarını MEYEM ile belgelendiriyor; referansımız bu sahadır.')


# ====================================================================== 14 HALKA
HK_X = [318, 638, 958, 1278, 1598]
HK_Y = [570, 660, 570, 660, 570]
HK_COL = [WINE, BLUE, INK, WINE_L, NAVY_M]


def art_halka():
    s = paper('d')
    s += wave_lines(0, 1920, 300, 1000, n=40, amp=14, wl=520, c=INK, op=0.06, sw=0.8, delta=0.14)
    for x, y, col in zip(HK_X, HK_Y, HK_COL):
        s += f'<circle cx="{x}" cy="{y}" r="152" fill="{PAPER_D}" fill-opacity="0.96"/>'
    for x, y, col in zip(HK_X, HK_Y, HK_COL):
        s += ring_bundle(x, y, 152, count=12, gap=2.6, a=3.4, nw=22, c1=col, c2=col, op=0.9, sw=1.0)
        s += circle(x, y, 190, col, 1.5, 0.95) + circle(x, y, 148, col, 1.0, 0.6)
    return s, ''


def html_halka():
    h = BK('halka')
    h += P('k', 128, 76, 600, 'VİZYON', i=0)
    h += TITLE('Tek çatı,', 'beş halka.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Mavi yaka ve beyaz yaka, belge ve eğitim, teşvik ve kariyer: tek muhatap, tek takvim.', 33, i=2)
    items = [('Yetki', 'Geniş MYK yetkisi'), ('Saha', 'İşyerinde sınav'), ('Dijital', 'Belge ve süre takibi'),
             ('Eğitim', '6331 eğitim ve MYK belgesi'), ('Kariyer yolu', 'Belgeden istihdama')]
    for k, ((t, d_), x, y) in enumerate(zip(items, HK_X, HK_Y)):
        h += P('num', x - 80, y - 82, 160, ['I', 'II', 'III', 'IV', 'V'][k], 60, extra='text-align:center;font-style:italic;', i=2 + k)
        h += P('ct', x - 110, y - 8, 220, t, 36, extra='text-align:center;', i=2 + k)
        h += P('sm', x - 150, y + 212, 300, d_, 26, extra='text-align:center;', i=2 + k)
    h += FOOT('Vizyon')
    return h


NOTES_HALKA = ('Vizyon beş halkadır ve halkalar birbirine geçer. Yetki: zorunlu mesleklerde geniş MYK yetkisi, kazan ve iş makineleri öncelikli. '
               'Saha: gezici sınav birimiyle işyerinde sınav. Dijital: belge, süre ve teşvik takibi, uygun yeterliliklerde online sınav. '
               'Eğitim: 6331 mesleki eğitim ve MYK belgesi aynı dosyada. Kariyer yolu: belgeden ustalığa ve istihdama, üniversite kariyer merkezi iş birliğiyle. '
               'Hedefimiz yalnız sınav yapmak değil; işletmenin mesleki yeterlilik ve eğitim yükümlülüklerini sektörler boyunca yöneten çözüm ortağı olmak.')


# ====================================================================== 15 YOL
YL_X = [128, 700, 1272]
YL_Y = 372


def art_yol():
    d = iris_defs('iris', 0, 1920, ((0, WINE), (0.5, BLUE), (1, INK)))
    s = paper('b')
    s += rosette_lace(1990, -100, 330, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.16, sw=0.7)
    for x in YL_X:
        s += arch_outline(x, YL_Y, 248, 300, WINE, 1.4, 0.9, off=12)
        s += arch_outline(x, YL_Y, 248, 300, INK, 0.8, 0.5, off=21)
    s += braid(120, 1480, 880, amp=14, wl=360, n=14, spread=2.8, delta=0.28, c1='url(#iris)', c2=WINE, op=0.6)
    s += f'<circle cx="1540" cy="880" r="30" fill="{PAPER_B}"/>' + circle(1540, 880, 30, WINE, 3, 1) + circle(1540, 880, 40, INK, 1, 0.55) + circle(1540, 880, 8, WINE, 0, 0, fill=WINE)
    return s, d


def html_yol():
    h = BK('yol')
    h += P('k', 128, 76, 600, 'İŞ BİRLİĞİ MODELİ', i=0)
    h += TITLE('Üç yol,', 'tek standart.', 128, 112, 900, 96, 116, i0=0)
    h += P('lead', 1000, 112, 792, 'Her bölgeye uyan üç model; hangisi seçilirse seçilsin sınav standardı aynı kalır.', 33, i=2)
    ms = [('A', 'Bilgilendirme ve yönlendirme', 'Sanayi odası, OSB veya dernek üyelerine duyuru ve seminer; firmalar MEYEM’e yönlendirilir.', 'arch_m1.png', 'Seminer salonunda sunum yapan uzman'),
          ('B', 'Toplu sınav günleri', 'Ortak noktada takvimli sınav günleri; başvuruyu firma yapar, sınavı MEYEM yürütür.', 'arch_m2.png', 'Fabrikada toplu sınav ve eğitim oturumu'),
          ('C', 'Ortak yapı veya şube', 'Bölgede MEYEM şubesi ya da ortak yapı; yetki MEYEM’de kalır.', 'arch_building.png', 'MEYEM Belgelendirme Merkezi binası')]
    for k, ((L, t, b, ph, alt), x) in enumerate(zip(ms, YL_X)):
        h += IMG(ph, x, YL_Y, 248, 300, alt, i=2 + k)
        h += P('num', x + 276, YL_Y - 6, 120, L, 84, extra='font-style:italic;', i=2 + k)
        h += P('ct', x + 276, YL_Y + 84, 250, t, 32, extra='line-height:1.1;', i=2 + k)
        h += P('sm', x + 276, YL_Y + 190, 250, b, 24, extra='line-height:1.3;', i=2 + k)
    h += P('sm', 1596, 850, 196, 'Yetki MEYEM’de kalır; standart her yerde aynı.', 24, extra='line-height:1.3;font-weight:600;color:#00244D;', i=6)
    h += FOOT('İş birliği')
    return h


NOTES_YOL = ('Üç model, tek standart. Model A bilgilendirme ve yönlendirme: sanayi odası, OSB yönetimi ya da dernek üyelerine duyuru ve seminer yapılır, firmalar MEYEM’e yönlendirilir. '
             'Model B toplu sınav günleri: ortak sınav noktasında takvimli sınav günleri; firmalar başvurusunu yapar, MEYEM sınavı yürütür. '
             'Model C ortak yapı ya da şube: bölgede MEYEM şubesi veya ortak yapı kurulur. Başlangıç Model A ile, ilk toplu sınav günüyle Model B’ye geçilir. '
             'Alttaki çizgi standardı gösterir: hangi yol seçilirse seçilsin MYK yetkisi MEYEM’de kalır ve sınav aynı kuralla yürür.')


# ====================================================================== 16 KAPANIŞ
KC = (440, 548)


def art_kapanis():
    cx, cy = KC
    d = iris_defs('iris', 0, 1100, ((0, INK), (0.5, BLUE), (1, WINE)))
    s = paper('b')
    s += rosette_flower(cx, cy, 1.0, 'url(#iris)', WINE, 0.55, 0.9)
    s += ring_bundle(cx, cy, 236, count=9, gap=3.0, a=4, nw=34, c1='url(#iris)', c2=WINE, op=0.5)
    s += f'<circle cx="{cx}" cy="{cy}" r="256" fill="{PAPER_B}"/>'
    s += circle(cx, cy, 256, WINE, 1.8, 0.9) + circle(cx, cy, 268, INK, 1.0, 0.7) + circle(cx, cy, 280, WINE, 0.8, 0.5)
    s += microring(cx, cy, 396, 'MEYEM MESLEKİ YETERLİLİK VE BELGELENDİRME MERKEZİ', 11, INK, 0.78, 'mrk')
    s += circle(cx, cy, 410, INK, 1.0, 0.55) + circle(cx, cy, 382, INK, 0.8, 0.45)
    s += ticks(cx, cy, 416, 120, 8, 16, 6, INK, 0.9, 0.35)
    s += rosette_lace(1990, 1150, 380, n=60, a=0.5, b=0.17, c=0.36, c1=INK, c2=WINE, op=0.15, sw=0.7)
    return s, d


def html_kapanis():
    cx, cy = KC
    h = BK('kapanis')
    h += IMG('eng_close.png', cx - 236, cy - 236, 472, 472, 'Gravür tekniğinde iki uzman, tablet ve dosya ile', i=1)
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
                 'Telefon, e-posta ve web adresini slayttan aktarın; QR kod doğrudan meyem.com.tr adresine gider. '
                 'Son söz açılışla aynı: ustalık sizden, mühür bizden.')


SLIDES3 = [
    ('egitim', 'c', art_egitim, html_egitim, NOTES_EGITIM, ''),
    ('yerinde', 'd', art_yerinde, html_yerinde, NOTES_YERINDE, ''),
    ('durak', 'b', art_durak, html_durak, NOTES_DURAK, ''),
    ('tesvik', 'c', art_tesvik, html_tesvik, NOTES_TESVIK, ''),
    ('referans', 'a', art_referans, html_referans, NOTES_REFERANS, ''),
    ('halka', 'd', art_halka, html_halka, NOTES_HALKA, ''),
    ('yol', 'b', art_yol, html_yol, NOTES_YOL, ''),
    ('kapanis', 'b', art_kapanis, html_kapanis, NOTES_KAPANIS, 'closing'),
]
