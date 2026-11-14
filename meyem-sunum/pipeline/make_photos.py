"""Tüm fotoğraf varlıklarını üretir -> m2/assets/ (png/jpg)"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from photos import *

A = M2 + '/assets'
os.makedirs(A, exist_ok=True)
SITE = M2 + '/site/home'
BRO = S + '/mdeck/assets/nat'
HEL = M2 + '/helal'
MADE = {}


def site(n):
    return Image.open(f'{SITE}/home-{n}.jpg').convert('RGB')


def bro(n):
    return Image.open(f'{BRO}/ph_{n}.jpg').convert('RGB')


def put(name, im, fmt='png'):
    p = f'{A}/{name}.{fmt}'
    if fmt == 'png':
        im.save(p, 'PNG', optimize=True)
    else:
        im.convert('RGB').save(p, 'JPEG', quality=91, subsampling=0, optimize=True)
    MADE[name] = (p, im.size)


def soft(im, up=2.0):
    """Küçük kaynakları 2× büyütüp hafif keskinleştir."""
    w, h = im.size
    r = im.resize((int(w * up), int(h * up)), Image.LANCZOS)
    return r.filter(ImageFilter.UnsharpMask(radius=1.4, percent=60, threshold=2))


def harmonize(im, sat=0.92, contrast=1.04, warm=1.0):
    return tone(im, warm=warm, sat=sat, contrast=contrast)


# ---------- 1) kapak gravürü (yuvarlak)
hero = site('hero')
eg = engrave(hero, 1000, 1000, pitch=7, gamma=1.9, lo=0.12, hi=0.90, hatch=False, zoom=1.30, cx=0.785, cy=0.455, amp=3.0, wl=280)
m = circle_mask(1000)
eg.putalpha(ImageChops.multiply(eg.getchannel('A'), m))
put('eng_cover', eg)

# ---------- 2) dokuz damga (pul)
STAMPS = [
    ('boiler', bro('boiler'), dict(cx=0.55, cy=0.5, zoom=1.0)),
    ('fork', bro('fork1'), dict(cx=0.45, cy=0.5, zoom=1.0)),
    ('weld', bro('weld'), dict(cx=0.62, cy=0.5, zoom=1.0)),
    ('cnc', bro('cnc2'), dict(cx=0.62, cy=0.5, zoom=1.0)),
    ('elec', bro('elec'), dict(cx=0.60, cy=0.5, zoom=1.0)),
    ('food', Image.open(f'{HEL}/h-000.png').convert('RGB').crop((900, 0, 1390, 262)), dict(cx=0.45, cy=0.5, zoom=1.0)),
    ('cyber', bro('cyber'), dict(cx=0.45, cy=0.5, zoom=1.0)),
    ('building', bro('building'), dict(cx=0.5, cy=0.45, zoom=1.0)),
    ('team', bro('team'), dict(cx=0.60, cy=0.5, zoom=1.0)),
]
for key, im, kw in STAMPS:
    im2 = harmonize(soft(im, 2.0 if im.width < 500 else 1.4))
    st = with_shadow(stamp(im2, 464, 550, **kw))
    put(f'stamp_{key}', st)

# ---------- 3) kemer pencereler (dört söz)
arch_src = [
    ('a1', site('mesleki-egitim'), dict(cx=0.78, cy=0.42, zoom=1.7)),
    ('a2', site('helal-tetkikci'), dict(cx=0.40, cy=0.50, zoom=1.25)),
    ('a3', site('denetim-hizmetleri'), dict(cx=0.68, cy=0.42, zoom=1.35)),
]
for key, im, kw in arch_src:
    a = arch_photo(harmonize(im, 0.95, 1.05), 660, 800, **kw)
    put(f'arch_{key}', a)

# ---------- 4) helal madalyonları
med_src = [
    ('m1', site('helal-personel'), 600, dict(cx=0.42, cy=0.45, zoom=1.15)),
    ('m2', site('helal-urun'), 700, dict(cx=0.60, cy=0.50, zoom=1.10)),
    ('m3', Image.open(f'{HEL}/h-000.png').convert('RGB').crop((780, 480, 1260, 745)), 520, dict(cx=0.5, cy=0.5, zoom=1.0)),
]
for key, im, d, kw in med_src:
    put(f'med_{key}', medallion(harmonize(soft(im, 1.0 if im.width > 600 else 1.8)), d, **kw))

# ---------- 5) süreç madalyonları (5)
proc = [
    ('p1', site('denetim-hizmetleri'), dict(cx=0.62, cy=0.38, zoom=1.8)),
    ('p2', site('helal-academy'), dict(cx=0.62, cy=0.30, zoom=1.7)),
    ('p3', bro('team'), dict(cx=0.60, cy=0.45, zoom=1.2)),
    ('p4', bro('clip'), dict(cx=0.50, cy=0.40, zoom=1.0)),
    ('p5', bro('cert'), dict(cx=0.55, cy=0.50, zoom=1.0)),
]
for key, im, kw in proc:
    put(f'proc_{key}', medallion(harmonize(soft(im, 1.0 if im.width > 600 else 2.0)), 360, **kw))

# ---------- 6) yerinde (büyük), eğitim
put('onsite_big', harmonize(site('myk-mesleki-yeterlilik'), 0.95, 1.04), 'jpg')
put('train_big', harmonize(site('mesleki-egitim'), 0.95, 1.04), 'jpg')
put('train_room', harmonize(site('meyem-academy'), 0.95, 1.04), 'jpg')
cert = Image.open(os.path.join(S, 'uploads', '4de97dd8-image.jpg')).convert('RGB')
put('cert_train', cert, 'jpg')

# ---------- 7) MYK belgesi (perspektif düzeltme)
page = Image.open(f'{HEL}/h-072.png').convert('RGB')
src = [(1275, 84), (1662, 52), (1593, 742), (1172, 692)]   # sol-üst, sağ-üst, sağ-alt, sol-alt


def persp_coeffs(src, dst):
    A_ = []
    for (x, y), (u, v) in zip(dst, src):
        A_.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); A_.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    B = np.array([c for p in src for c in p], dtype=np.float64)
    res = np.linalg.solve(np.array(A_, dtype=np.float64), B)
    return res.tolist()


OW, OH = 700, 990
co = persp_coeffs(src, [(0, 0), (OW, 0), (OW, OH), (0, OH)])
flat = page.transform((OW, OH), Image.PERSPECTIVE, co, Image.BICUBIC)
# ad satırını bulanıklaştır (örnek belgedeki kişi adı)
bl = flat.crop((255, 462, 445, 497)).filter(ImageFilter.GaussianBlur(6))
flat.paste(bl, (255, 462))
put('cert_myk', flat, 'jpg')

# ---------- 8) logolar (beyaz -> saydam)


def white_to_alpha(im, k=2.4):
    im = im.convert('RGB')
    a = np.asarray(im, dtype=np.float32)
    mn = a.min(axis=2)
    alpha = np.clip((255 - mn) * k, 0, 255)
    out = np.dstack([a, alpha]).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')


for n in ('seal', 'myk', 'turkak'):
    im = Image.open(f'{PH}/logo_{n}.png').convert('RGB')
    put(f'logo_{n}', white_to_alpha(im) if n != 'seal' else white_to_alpha(im, 2.0))

# ---------- 9) kapanış: bina
bld = bro('building')
put('arch_building', arch_photo(harmonize(soft(bld, 2.0)), 660, 800, cx=0.5, cy=0.5, zoom=1.0))

# ---------- 9b) model kemerleri, kapanış gravürü, QR
put('arch_m1', arch_photo(harmonize(site('meyem-academy'), 0.95, 1.05), 660, 800, cx=0.52, cy=0.45, zoom=1.6))
put('arch_m2', arch_photo(harmonize(site('hero'), 0.95, 1.05), 660, 800, cx=0.29, cy=0.345, zoom=1.9))
eg2 = engrave(site('helal-tetkikci'), 1000, 1000, pitch=7, gamma=1.9, lo=0.12, hi=0.90, hatch=False, zoom=1.25, cx=0.46, cy=0.46, amp=3.0, wl=280)
eg2.putalpha(ImageChops.multiply(eg2.getchannel('A'), circle_mask(1000)))
put('eng_close', eg2)
import sys
sys.path.insert(0, M2 + '/pylib')
import qrcode
qr = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
qr.add_data('https://www.meyem.com.tr')
qr.make(fit=True)
mat = qr.get_matrix()
n = len(mat)
mod = 12
pad = 4 * mod
qim = Image.new('RGBA', (n * mod + 2 * pad, n * mod + 2 * pad), (255, 255, 255, 255))
dq = ImageDraw.Draw(qim)
for yy, row in enumerate(mat):
    for xx, v in enumerate(row):
        if v:
            dq.rectangle((pad + xx * mod, pad + yy * mod, pad + (xx + 1) * mod - 1, pad + (yy + 1) * mod - 1), fill=(0, 36, 77, 255))
put('qr_meyem', qim)

# ---------- 10) referans duvarı
wall = Image.open(S + '/mdeck/assets/wall.jpg').convert('RGB')
put('wall', wall, 'jpg')

for k, (p, sz) in MADE.items():
    print(f'{k:16s} {sz}  {os.path.getsize(p)//1024} KB')

# iletişim sayfası
names = list(MADE)
cols = 8
tw = 240
rows = (len(names) + cols - 1) // cols
sh = Image.new('RGB', (cols * tw, rows * 260), (236, 230, 224))
for i, n in enumerate(names):
    im = Image.open(MADE[n][0]).convert('RGBA')
    im.thumbnail((tw - 10, 240))
    bg = Image.new('RGBA', im.size, (244, 232, 235, 255))
    bg.alpha_composite(im)
    sh.paste(bg.convert('RGB'), ((i % cols) * tw + 5, (i // cols) * 260 + 5))
sh.save(A + '/_sheet.jpg', quality=85)
print('sheet ok')
