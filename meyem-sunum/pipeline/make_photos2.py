"""v2: doğal renkli fotoğraf varlıkları (CC0/PD kaynaklar + MEYEM'in kendi görselleri)."""
import os, sys
from PIL import Image, ImageOps
from photos import *

A = M2 + '/assets'
W = M2 + '/web'
SITE = M2 + '/site/home'
HEL = M2 + '/helal'
BRO = S + '/mdeck/assets/nat'
MADE = {}


def px(pid):
    return Image.open(f'{W}/full/px_{pid}.jpg').convert('RGB')


def ss(pid):
    return Image.open(f'{W}/full/ss_{pid}.jpg').convert('RGB')


def rp(name):
    return Image.open(f'{W}/rp/{name}.jpg').convert('RGB')


def site(n):
    return Image.open(f'{SITE}/home-{n}.jpg').convert('RGB')


def bro(n):
    return Image.open(f'{BRO}/ph_{n}.jpg').convert('RGB')


def put(name, im, fmt='png'):
    p = f'{A}/{name}.{fmt}'
    if fmt == 'png':
        im.save(p, 'PNG', optimize=True)
    else:
        im.convert('RGB').save(p, 'JPEG', quality=92, subsampling=0, optimize=True)
    MADE[name] = (p, im.size)


def grade(im, sat=0.96, con=1.05, warm=0.8, bright=1.0):
    return tone(im, warm=warm, sat=sat, contrast=con, bright=bright)


def square(im, n, cx=0.5, cy=0.5, zoom=1.0, pad_white=False):
    if pad_white:
        w, h = im.size
        s = max(w, h)
        bg = Image.new('RGB', (s, s), (255, 255, 255))
        bg.paste(im, ((s - w) // 2, (s - h) // 2))
        im = bg
    return cover_crop(im, n, n, cx, cy, zoom)


# ---------- kapak ve kapanış (yuvarlak, doğal renk)
put('cover_photo', circle_photo(grade(site('hero'), 1.0, 1.04, 0.5), 1000, cx=0.80, cy=0.45, zoom=1.30))
put('close_photo', circle_photo(grade(site('meyem-academy'), 1.0, 1.04, 0.4), 1000, cx=0.56, cy=0.46, zoom=1.30))

# ---------- dört söz: kemer pencereler (660x800)
put('soz_a1', arch_photo(grade(px('1142060'), 1.0, 1.06, 0.3), 660, 800, cx=0.46, cy=0.50, zoom=1.12))
put('soz_a2', arch_photo(grade(ss('WQ2JMRIIQB'), 1.0, 1.05, 0.5), 660, 800, cx=0.52, cy=0.52, zoom=1.0))
put('soz_a3', arch_photo(grade(ss('69YZFGFBSY'), 1.0, 1.05, 0.5), 660, 800, cx=0.42, cy=0.52, zoom=1.05))

# ---------- dokuz kare karo (560x560); sıra: inşaat, metal, makine, enerji, taşıma, gıda, ticaret, yönetim, bilişim
T = {
    'insaat': square(grade(px('1087305')), 560, cx=0.38, cy=0.50, zoom=1.0),
    'metal': square(grade(rp('welder_5')), 560, cx=0.46, cy=0.46, zoom=1.0),
    'makine': square(grade(px('771478')), 560, cx=0.50, cy=0.50, zoom=1.0),
    'enerji': square(grade(px('1324058')), 560, cx=0.64, cy=0.56, zoom=1.0),
    'tasima': square(grade(rp('forklift_operator_warehouse_0')), 560, cx=0.34, cy=0.52, zoom=1.0),
    'gida': square(grade(Image.open(f'{HEL}/h-000.png').convert('RGB').crop((900, 0, 1390, 262))), 560, cx=0.55, cy=0.5, zoom=1.0),
    'ticaret': square(grade(px('449062')), 560, cx=0.50, cy=0.50, zoom=1.0),
    'yonetim': square(grade(px('868210'), 1.0, 1.0, 0.0), 560, pad_white=True),
    'bilisim': square(grade(ss('6Z663NNH9K')), 560, cx=0.50, cy=0.50, zoom=1.0),
}
for k, im in T.items():
    put(f'tile_{k}', im, 'jpg')

# ---------- süreç madalyonları (d=420 px)
seal = Image.open(A + '/logo_seal.png').convert('RGBA')
seal_img = Image.new('RGB', (700, 700), (255, 255, 255))
sl = seal.resize((520, int(520 * seal.height / seal.width)), Image.LANCZOS)
seal_img.paste(sl, ((700 - sl.width) // 2, (700 - sl.height) // 2), sl)
PR = [
    ('d1', site('denetim-hizmetleri'), dict(cx=0.64, cy=0.40, zoom=1.7)),
    ('d2', px('596254'), dict(cx=0.52, cy=0.50, zoom=1.25)),
    ('d3', px('680669'), dict(cx=0.46, cy=0.52, zoom=1.35)),
    ('d4', px('685238'), dict(cx=0.40, cy=0.50, zoom=1.25)),
    ('d5', seal_img, dict(cx=0.5, cy=0.5, zoom=1.0)),
]
for k, im, kw in PR:
    put(f'step_{k}', medallion(grade(im, 1.0, 1.04, 0.4), 420, **kw))

# ---------- model kemerleri (660x800)
put('model_a', arch_photo(grade(px('1246944')), 660, 800, cx=0.50, cy=0.48, zoom=1.55))
put('model_b', arch_photo(grade(site('helal-academy')), 660, 800, cx=0.60, cy=0.42, zoom=1.45))

for k, (p, sz) in MADE.items():
    print(f'{k:14s} {sz}  {os.path.getsize(p)//1024} KB')

names = list(MADE)
cols = 8
tw = 230
rows = (len(names) + cols - 1) // cols
sh = Image.new('RGB', (cols * tw, rows * 250), (236, 230, 224))
for i, n in enumerate(names):
    im = Image.open(MADE[n][0]).convert('RGBA')
    im.thumbnail((tw - 8, 236))
    bg = Image.new('RGBA', im.size, (244, 232, 235, 255))
    bg.alpha_composite(im)
    sh.paste(bg.convert('RGB'), ((i % cols) * tw + 4, (i // cols) * 250 + 4))
sh.save(A + '/_sheet2.jpg', quality=85)
print('sheet ok')
