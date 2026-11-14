"""MEYEM v9 “güvenlik baskısı” görselleri: veriyle örülmüş guilloche, belge çerçevesi, zaman şeridi, pul sayfası.
Her çizim 1920×1080 SVG olarak kurulur ve Chromium ile DSF 2'de pişirilir (metin etiketleri slaytta gerçek metindir)."""
import os, json, subprocess
from math import cos, sin, pi

M2 = os.path.dirname(os.path.abspath(__file__))
ART = M2 + '/art_v9'
ASSETS = M2 + '/assets_v9'
for d in (ART, ASSETS):
    os.makedirs(d, exist_ok=True)

W, H = 1920, 1080
INK, INK2, BLUE, WINE = '#00244D', '#2C4868', '#3E5E86', '#77183A'
PAPER_A, PAPER_B, PAPER_C = '#F8F4EC', '#F4E8EB', '#E9EFF6'
TINT = '#6F8AAE'                # gönüllü pul: kâğıda karşı 3:1'in üstünde

# 55 yeterlilik, alan sırasıyla: (alan, toplam, zorunlu)
FIELDS = [('İnşaat ve yapı', 13, 13), ('Makine ve üretim', 5, 5), ('Enerji ve tesisat', 5, 4), ('Metal ve kaynak', 3, 3),
          ('Taşıma ve kaldırma', 4, 2), ('Bilişim ve siber', 14, 0), ('Ticaret ve emlak', 6, 0), ('Yönetim ve İK', 4, 0),
          ('Gıda ve paketleme', 1, 0)]
assert sum(f[1] for f in FIELDS) == 55 and sum(f[2] for f in FIELDS) == 27
FLAGS = [k < z for _, n, z in FIELDS for k in range(n)]          # True = zorunlu


def f1(x):
    return f'{x:.1f}'


def path(pts, close=False):
    return 'M' + ' L'.join(f'{f1(x)} {f1(y)}' for x, y in pts) + ('Z' if close else '')


def line(d, c, sw=1.8, op=0.6, extra=''):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-opacity="{op}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


def circle(cx, cy, r, stroke=INK, sw=1.6, op=0.7, fill='none'):
    return f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{op}"/>'


def arc_text(cx, cy, r, text, fs=14, color=INK, op=0.75, uid='t', ls=2.0, start=-90, weight=600, fill_circle=True):
    """Daire üzerinde yazı (mikro yazı / damga yazısı). Metin çevreyi dolduracak kadar tekrarlanır."""
    d = f'M{f1(cx - r)} {f1(cy)} a{f1(r)} {f1(r)} 0 1 1 {f1(2 * r)} 0 a{f1(r)} {f1(r)} 0 1 1 {f1(-2 * r)} 0'
    circ = 2 * pi * r
    est = fs * 0.62 + ls
    t = text
    if fill_circle:                              # yalnızca tam tekrarlar; aralık textLength ile çevreye yayılır
        t = text * max(1, int(circ / (est * len(text))))
    tl = f' textLength="{f1(circ - 6)}" lengthAdjust="spacing"' if fill_circle else ''
    return (f'<defs><path id="{uid}" d="{d}" transform="rotate({start + 180} {f1(cx)} {f1(cy)})"/></defs>'
            f'<text font-family="Hanken Grotesk" font-weight="{weight}" font-size="{fs}" letter-spacing="{ls}" fill="{color}" fill-opacity="{op}">'
            f'<textPath href="#{uid}"{tl}>{t}</textPath></text>')


def underprint(x0, y0, x1, y1, gap=14, amp=5, wl=230, c=INK, op=0.06, sw=1.2):
    """Güvenlik kâğıdı alt baskısı: ince dalgalı yatay çizgiler."""
    out = []
    k = 0
    y = y0
    while y <= y1:
        pts = [(x, y + amp * sin(2 * pi * (x - x0) / wl + k * 0.55)) for x in range(int(x0), int(x1) + 1, 8)]
        out.append(line(path(pts), c, sw, op))
        y += gap
        k += 1
    return ''.join(out)


def band_h(x0, x1, yc, amp=8, wl=64, n=4, spread=2.6, sw=1.5, op=0.55):
    out = []
    for col, ph0 in ((INK, 0.0), (WINE, pi)):
        for k in range(n):
            pts = [(x, yc + (k - (n - 1) / 2) * spread + amp * sin(2 * pi * (x - x0) / wl + ph0 + k * 0.5)) for x in range(int(x0), int(x1) + 1, 3)]
            out.append(line(path(pts), col, sw, op))
    return ''.join(out)


def band_v(y0, y1, xc, **kw):
    """Dikey bant: yatay bandı 90° döndürerek."""
    g = band_h(y0, y1, 0, **kw)
    return f'<g transform="translate({f1(xc)} 0) rotate(90)">{g}</g>'


def corner_rosette(cx, cy, R=15, r=6, d=10, n=900, c=WINE, sw=1.4, op=0.8):
    pts = []
    for i in range(n + 1):
        t = 2 * pi * 6 * i / n
        x = (R - r) * cos(t) + d * cos((R - r) / r * t)
        y = (R - r) * sin(t) - d * sin((R - r) / r * t)
        pts.append((cx + x, cy + y))
    return line(path(pts, True), c, sw, op)


def data_rosette(cx, cy, d=262, r=108, sw=1.8):
    """55 halkalı rozet: her halka bir yeterlilik; zorunlu = şarap, gönüllü = mavi."""
    out = []
    for k, z in enumerate(FLAGS):
        a = -pi / 2 + 2 * pi * k / 55
        out.append(circle(cx + d * cos(a), cy + d * sin(a), r, WINE if z else BLUE, sw, 0.55 if z else 0.45))
    return ''.join(out)


# ------------------------------------------------------------------ 1 kapak: belge yüzü
PH = (1180, 250, 460, 550)          # fotoğraf penceresi x, y, w, h
RC = (PH[0] + PH[2] / 2, PH[1] + PH[3] / 2)


def art_kapak():
    s = f'<rect width="{W}" height="{H}" fill="{PAPER_A}"/>'
    s += underprint(84, 92, W - 84, H - 92)
    # belge çerçevesi: iki çizgi, arada örgü bant, köşelerde rozet
    for ins, sw in ((40, 2.0), (84, 2.0)):
        s += f'<rect x="{ins}" y="{ins}" width="{W - 2 * ins}" height="{H - 2 * ins}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-opacity=".75"/>'
    s += band_h(84, W - 84, 62) + band_h(84, W - 84, H - 62)
    s += band_v(84, H - 84, 62) + band_v(84, H - 84, W - 62)
    for cx, cy in ((62, 62), (W - 62, 62), (62, H - 62), (W - 62, H - 62)):
        s += f'<rect x="{cx - 22}" y="{cy - 22}" width="44" height="44" fill="{PAPER_A}"/>' + corner_rosette(cx, cy)
    # veri rozeti + mikro yazı
    cx, cy = RC
    s += circle(cx, cy, 384, INK, 1.6, 0.6) + circle(cx, cy, 392, INK, 1.6, 0.6)
    micro = ' · '.join(f'{n.upper()} {t}' for n, t, _ in FIELDS) + ' · '
    s += arc_text(cx, cy, 404, micro.replace('İ', 'İ'), fs=13, color=INK, op=0.7, uid='mk', ls=1.6)
    s += data_rosette(cx, cy)
    s += circle(cx, cy, 150, INK, 1.6, 0.6)
    # fotoğraf paspartusu ve çift çizgi
    x, y, w, h = PH
    s += f'<rect x="{x - 18}" y="{y - 18}" width="{w + 36}" height="{h + 36}" fill="{PAPER_A}"/>'
    s += f'<rect x="{x - 18}" y="{y - 18}" width="{w + 36}" height="{h + 36}" fill="none" stroke="{INK}" stroke-width="2" stroke-opacity=".8"/>'
    s += f'<rect x="{x - 9}" y="{y - 9}" width="{w + 18}" height="{h + 18}" fill="none" stroke="{WINE}" stroke-width="1.4" stroke-opacity=".8"/>'
    return s


# ------------------------------------------------------------------ 4 takvim: hızlanan şerit ve damga
X0, X1, RY = 128, 1792, 640
EV_X = [round(200 + p * 1360) for p in (0.0, 0.307, 0.775, 1.0)]     # orantılı tarih konumları
STAMP_R = 128


def ribbon(x0, x1, yc, n=8, spread=3.2, wl=150, sw=1.8, op=0.55):
    out = []
    for col, ph0 in ((INK, 0.0), (WINE, pi)):
        for k in range(n):
            pts = []
            for x in range(x0, x1 + 1, 3):
                u = (x - x0) / (x1 - x0)
                a = 5 + 42 * u ** 1.6                              # tarih yaklaştıkça genlik artar
                pts.append((x, yc + (k - (n - 1) / 2) * spread * (1 + u) + a * sin(2 * pi * (x - x0) / wl * (1 + 0.6 * u) + ph0 + k * 0.32)))
            out.append(line(path(pts), col, sw, op))
    return ''.join(out)


def node(cx, cy):
    return (circle(cx, cy, 28, INK, 0, 0, PAPER_C) + circle(cx, cy, 28, INK, 2.0, 0.9) + circle(cx, cy, 19, INK, 1.4, 0.7)
            + f'<circle cx="{cx}" cy="{cy}" r="7" fill="{INK}"/>')


def postmark(cx, cy, rot=-9):
    s = circle(cx, cy, STAMP_R, WINE, 0, 0, PAPER_C)
    g = circle(cx, cy, STAMP_R - 4, WINE, 3.0, 0.95) + circle(cx, cy, STAMP_R - 16, WINE, 1.6, 0.9)
    g += arc_text(cx, cy, STAMP_R - 33, 'GEÇİŞ SÜRESİ BİTER  ·  BELGE ZORUNLU  ·  ', fs=17, color=WINE, op=0.95, uid='pm', ls=2.4, weight=700)
    g += circle(cx, cy, STAMP_R - 46, WINE, 1.4, 0.85)
    return s + f'<g transform="rotate({rot} {cx} {cy})">{g}</g>'


def art_takvim():
    s = f'<rect width="{W}" height="{H}" fill="{PAPER_C}"/>'
    s += underprint(0, 380, W, 900, gap=16, amp=4, wl=260, op=0.045)
    s += ribbon(X0, X1, RY)
    for x in EV_X[:-1]:
        s += node(x, RY)
    s += postmark(EV_X[-1], RY)
    return s


# ------------------------------------------------------------------ 6 kapsam: pul sayfası
SY0, SPITCH, SW_, SH_, SSTEP, SX0 = 400, 58, 36, 44, 46, 540


def stamp(x, y, w, h, fill, paper, perf=2.4, gap=7.4, inner=True, dashed=None):
    if dashed:
        return (f'<rect x="{f1(x)}" y="{f1(y)}" width="{w}" height="{h}" rx="2" fill="none" stroke="{dashed}" stroke-width="1.6" '
                f'stroke-dasharray="3.5 3" stroke-opacity=".85"/>')
    s = f'<rect x="{f1(x)}" y="{f1(y)}" width="{w}" height="{h}" rx="1.5" fill="{fill}"/>'
    for i in range(int(w // gap) + 1):          # tırtıklar: üst ve alt kenar
        px = x + 3 + i * gap
        if px <= x + w - 2:
            s += f'<circle cx="{f1(px)}" cy="{f1(y)}" r="{perf}" fill="{paper}"/><circle cx="{f1(px)}" cy="{f1(y + h)}" r="{perf}" fill="{paper}"/>'
    for i in range(int(h // gap) + 1):          # sol ve sağ kenar
        py = y + 3 + i * gap
        if py <= y + h - 2:
            s += f'<circle cx="{f1(x)}" cy="{f1(py)}" r="{perf}" fill="{paper}"/><circle cx="{f1(x + w)}" cy="{f1(py)}" r="{perf}" fill="{paper}"/>'
    if inner:
        s += f'<rect x="{f1(x + 6)}" y="{f1(y + 6)}" width="{w - 12}" height="{h - 12}" fill="none" stroke="{paper}" stroke-width="1.2" stroke-opacity=".7"/>'
    return s


def art_kapsam():
    s = f'<rect width="{W}" height="{H}" fill="{PAPER_A}"/>'
    for k, (_, n, z) in enumerate(FIELDS):
        y = SY0 + k * SPITCH
        for i in range(n):
            s += stamp(SX0 + i * SSTEP, y, SW_, SH_, WINE if i < z else TINT, PAPER_A)
    # lejant pulları
    s += stamp(1330, 404, SW_, SH_, WINE, PAPER_A) + stamp(1330, 524, SW_, SH_, TINT, PAPER_A)
    # onay sürecindeki 32 yeterlilik: kesik çizgili pullar (16 zorunlu kapsamda)
    for i in range(32):
        r, c = divmod(i, 16)
        s += stamp(1330 + c * 28, 840 + r * 34, 20, 26, None, PAPER_A, dashed=WINE if i < 16 else TINT)
    return s


ARTS = {'bk_v9_kapak': art_kapak, 'bk_v9_takvim': art_takvim, 'bk_v9_kapsam': art_kapsam}


def bake(names=None, dsf=2, q=90):
    fonts = open(M2 + '/fonts/fonts.css').read().replace('url(fonts/', f'url(file://{M2}/fonts/')
    jobs = []
    for name, fn in ARTS.items():
        if names and name not in names:
            continue
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{fn()}</svg>'
        hp = f'{ART}/_{name}.html'
        open(hp, 'w').write(f'<html><head><meta charset="utf-8"><style>{fonts} html,body{{margin:0}}</style></head><body style="width:{W}px;height:{H}px;overflow:hidden">{svg}</body></html>')
        jobs.append({'html': hp, 'out': f'{ART}/{name}.png', 'w': W, 'h': H, 'dsf': dsf, 'wait': 500})
    json.dump(jobs, open(f'{ART}/jobs.json', 'w'))
    subprocess.run(['node', M2 + '/shoot2.js', f'{ART}/jobs.json'], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})
    from PIL import Image
    for j in jobs:
        name = os.path.basename(j['out'])[:-4]
        Image.open(j['out']).convert('RGB').save(f'{ASSETS}/{name}.jpg', 'JPEG', quality=q, subsampling=0, optimize=True)
        print(name, os.path.getsize(f'{ASSETS}/{name}.jpg') // 1024, 'KB')
