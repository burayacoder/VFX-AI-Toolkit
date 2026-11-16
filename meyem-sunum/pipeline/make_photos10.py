"""v10: fotoğraf yuvalarını CC0 kaynaklardan yeniden üretir -> assets/ (v7 ile aynı dosya adları).

Kaynaklar data/gorsel_kaynaklari.md (v10 bölümü) içinde. Girdiler pipeline/web/v10/ altına indirilir
(PxHere önbellek boyutu “!s2”, 800 px; PxHere tam boy dosyası sunucu zaman aşımına düştüğü için).
Kırpımda odak noktası (cx, cy) konunun yüzü/eli olacak şekilde seçilir: konu çerçevenin ortasında kalır.
"""
import os, sys, json, urllib.request
from PIL import Image
from photos import *

A = M2 + '/assets'
WEB = M2 + '/web/v10'
os.makedirs(A, exist_ok=True)
os.makedirs(WEB, exist_ok=True)
UA = {'User-Agent': 'deck-builder/1.0'}


def grade(im, sat=0.96, con=1.05, warm=0.8, bright=1.0):
    return tone(im, warm=warm, sat=sat, contrast=con, bright=bright)


def src(url):
    """İndir (yoksa) ve aç. url: PxHere !s2 bağlantısı ya da Openverse/rawpixel görsel adresi."""
    fn = WEB + '/' + url.split('/')[-1].split('?')[0].replace('!', '_')
    if not fn.endswith('.jpg'):
        fn += '.jpg'
    if not os.path.exists(fn):
        open(fn, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
    return Image.open(fn).convert('RGB')


def put(name, im, fmt='png'):
    p = f'{A}/{name}.{fmt}'
    if fmt == 'png':
        im.save(p, 'PNG', optimize=True)
    else:
        im.convert('RGB').save(p, 'JPEG', quality=92, subsampling=0, optimize=True)
    print(name, im.size)


SEL = json.load(open(os.path.join(os.path.dirname(M2), 'data', 'v10_foto_secim.json')))

for slot, s in SEL.items():
    im = grade(src(s['url']), *s.get('grade', []))
    kw = dict(cx=s.get('cx', 0.5), cy=s.get('cy', 0.5), zoom=s.get('zoom', 1.0))
    if slot in ('cover_photo', 'close_photo'):
        put(slot, circle_photo(im, 1000, **kw))
    elif slot.startswith('soz_a'):
        put(slot, arch_photo(im, 660, 800, **kw))
    elif slot.startswith('tile_'):
        put(slot, cover_crop(im, 560, 560, **kw), 'jpg')
    elif slot.startswith('step_d'):
        put(slot, medallion(im, 420, **kw))
    elif slot == 'onsite_big':
        put(slot, cover_crop(im, 1012, 675, **kw), 'jpg')
