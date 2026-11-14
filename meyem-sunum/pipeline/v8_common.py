"""MEYEM v8 tasarım sistemi: belirteçler, CSS, ızgara, yardımcılar, fotoğraf tonu ve pişirme.

Kurallar (faz1 ilkeleri):
- Tek yazı ailesi: Archivo (genişlik ekseniyle başlık, gövde ve büyük sayı).
- Beş boy: 24 / 32 / 48 / 88 / 240 px.
- Başlık her slaytta x=128, y=112; en fazla 2 satır; içerik y=360'tan başlar.
- 12 sütun: kenar 128, oluk 32.
- İki ana renk (lacivert, şarap) + kâğıt; vurgu yalnız şarap.
- Guilloche yalnızca kapak, bölüm açılışı, mühür ve kapanışta; çizgi en az 2 px.
"""
import html, os, json, subprocess
from math import cos, sin, pi

M2 = os.environ.get('MEYEM_WORK', os.path.dirname(os.path.abspath(__file__)))
ASSETS = M2 + '/assets_v8'          # yerel önizleme varlıkları (yayın adlarıyla)
ART = M2 + '/art_v8'                # pişirme çalışma klasörü
OUT = M2 + '/out_v8'
PROJ = OUT + '/project'
URLS = os.path.join(os.path.dirname(M2), 'data', 'assets_v8.json')
for d in (ASSETS, ART):
    os.makedirs(d, exist_ok=True)

W, H = 1920, 1080

# ------------------------------------------------------------------ renk belirteçleri
INK = '#00244D'      # lacivert: metin, ana öğe
INK2 = '#2C4868'     # ikincil metin
WINE = '#77183A'     # tek vurgu
TINT = '#C9D2DD'     # lacivert açık ton: ikincil çubuk
PAPER = '#F8F4EC'    # kâğıt zemin
PAPER2 = '#FBFAF6'   # açık kâğıt
LINE = '#D8D2C4'     # ince ayraç

# ------------------------------------------------------------------ ızgara
MARGIN, GUT = 128, 32
COLW = (W - 2 * MARGIN - 11 * GUT) / 12          # 109.33


def col(i):
    """i. sütunun sol kenarı (0..11)."""
    return round(MARGIN + i * (COLW + GUT))


def span(n):
    """n sütunluk genişlik."""
    return round(n * COLW + (n - 1) * GUT)


# ------------------------------------------------------------------ yazı ölçeği (px)
FS = {'xs': 24, 's': 32, 'm': 48, 'l': 88, 'xl': 240}
TITLE_X, TITLE_Y, TITLE_W = 128, 112, span(10)
CONTENT_Y = 360
FOOT_Y = 992

FACES = {
    'archivo': {'family': 'Archivo',
                'href': 'https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap'},
}

CSS = """
.s{position:relative;color:#00244D;background:#F8F4EC;font-family:'Archivo',Arial,sans-serif;font-stretch:100%;counter-increment:page;overflow:hidden}
.s::after{content:counter(page);position:absolute;right:128px;bottom:64px;font-family:'Archivo',Arial,sans-serif;font-size:24px;font-weight:500;line-height:1;color:#2C4868}
.cover::after,.closing::after{content:""}
.phs::after{color:#FFFFFF}
.pin{position:absolute;margin:0}
.bk{position:absolute}
.tt{font-size:88px;font-weight:700;font-stretch:78%;line-height:1;letter-spacing:-1px;color:#00244D;text-wrap:balance}
.nb{font-size:240px;font-weight:800;font-stretch:62%;line-height:.86;letter-spacing:-2px;color:#77183A}
.md{font-size:48px;font-weight:700;font-stretch:80%;line-height:1.05;color:#00244D}
.bd{font-size:32px;font-weight:400;line-height:1.38;color:#2C4868}
.bb{font-size:32px;font-weight:700;line-height:1.1;color:#00244D}
.xs{font-size:24px;font-weight:500;line-height:1.3;color:#2C4868}
.wm{font-size:24px;font-weight:800;font-stretch:110%;letter-spacing:4px;line-height:1;color:#00244D}
.ac{color:#77183A}
.ph{object-fit:cover}
@keyframes rise{from{opacity:0;transform:translateY(20px)}}
@keyframes fadein{from{opacity:0}}
.rise{animation:rise .8s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i,0)*100ms)}
.fadein{animation:fadein 1s ease both;animation-delay:calc(var(--i,0)*100ms)}
"""

MODE = {'v': 'preview'}          # 'preview' | 'publish'
USED = {}


def esc(s):
    return html.escape(str(s), quote=False)


def url_for(fn):
    USED[fn] = f'{ASSETS}/{fn}'
    if MODE['v'] == 'preview':
        return 'file://' + f'{ASSETS}/{fn}'
    return json.load(open(URLS))[fn]


def sty(x=None, y=None, w=None, h=None, extra=''):
    s = ''
    for k, v in (('left', x), ('top', y), ('width', w), ('height', h)):
        if v is not None:
            s += f'{k}:{v}px;'
    return s + extra


def P(cls, x, y, w, text, extra='', tag='p', raw=False, i=None):
    st = sty(x, y, w, None, extra)
    cl = 'pin ' + cls + (' rise' if i is not None else '')
    if i is not None:
        st += f'--i:{i};'
    return f'<{tag} class="{cl}" style="{st}">{text if raw else esc(text)}</{tag}>'


def TITLE(text, w=TITLE_W, i=0):
    return P('tt', TITLE_X, TITLE_Y, w, text, tag='h2', i=i)


def SOURCE(text):
    return P('xs', 128, FOOT_Y, span(9), text, extra='line-height:1;')


def IMG(fn, x, y, w, h, alt='', cls='pin', extra='', i=None):
    st = sty(x, y, w, h, extra)
    cl = cls + (' fadein' if i is not None else '')
    if i is not None:
        st += f'--i:{i};'
    return f'<img class="{cl}" src="{url_for(fn)}" alt="{esc(alt)}" style="{st}">'


def BOX(x, y, w, h, color, extra='', inner=''):
    return f'<div class="pin" style="{sty(x, y, w, h)}background:{color};{extra}">{inner}</div>'


def SEC(sid, inner, notes, cls=''):
    return (f'<section id="{sid}" class="s{(" " + cls) if cls else ""}" data-transition="fade">\n{inner}\n'
            f'<aside>{esc(notes)}</aside>\n</section>\n')


# ------------------------------------------------------------------ fotoğraf dili: tek renk ayarı
def grade(src, dst, box_w, box_h, focus=(0.5, 0.5), scale=1.5, q=90):
    """Kaynağı kutu oranına kırpar, tek renk ayarını uygular, JPG yazar.
    Renk ayarı: hafif S eğrisi, doygunluk %90, sıcaklık +2, gölgeler laciverte %6, açık tonlar kâğıda %5."""
    import numpy as np
    from PIL import Image
    im = Image.open(src).convert('RGB')
    sw, sh = im.size
    ar = box_w / box_h
    if sw / sh > ar:
        cw, ch = int(sh * ar), sh
    else:
        cw, ch = sw, int(sw / ar)
    cx = min(max(int(focus[0] * sw - cw / 2), 0), sw - cw)
    cy = min(max(int(focus[1] * sh - ch / 2), 0), sh - ch)
    im = im.crop((cx, cy, cx + cw, cy + ch)).resize((int(box_w * scale), int(box_h * scale)), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255.0
    lum = (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2])[..., None]
    a = lum + (a - lum) * 0.90                                   # doygunluk
    s = a * a * (3 - 2 * a)                                      # S eğrisi
    a = a * 0.82 + s * 0.18
    a[..., 0] *= 1.02
    a[..., 2] *= 0.98                                            # sıcaklık
    ink = np.array([0x00, 0x24, 0x4D], np.float32) / 255
    pap = np.array([0xF8, 0xF4, 0xEC], np.float32) / 255
    lum = (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2])[..., None]
    wsh = np.clip((0.42 - lum) / 0.42, 0, 1) * 0.06
    whi = np.clip((lum - 0.70) / 0.30, 0, 1) * 0.05
    a = a * (1 - wsh) + ink * wsh
    a = a * (1 - whi) + pap * whi
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype('uint8'))
    out.save(dst, 'JPEG', quality=q, subsampling=0, optimize=True)
    return dst


# ------------------------------------------------------------------ pişirme (şeffaf PNG)
def bake_alpha(name, svg_inner, w, h, dsf=2):
    fonts = open(M2 + '/fonts/fonts_v8.css').read().replace('url(fonts/', f'url(file://{M2}/fonts/')
    s = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg_inner}</svg>'
    hp = f'{ART}/_{name}.html'
    open(hp, 'w').write(f'<html><head><meta charset="utf-8"><style>{fonts} html,body{{margin:0;background:transparent}}</style></head>'
                        f'<body style="width:{w}px;height:{h}px;overflow:hidden">{s}</body></html>')
    jobs = f'{ART}/_jobs_{name}.json'
    json.dump([{'html': hp, 'out': f'{ASSETS}/{name}.png', 'w': w, 'h': h, 'dsf': dsf, 'wait': 300, 'transparent': True}], open(jobs, 'w'))
    subprocess.run(['node', M2 + '/shoot2.js', jobs], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})
    return f'{ASSETS}/{name}.png'


# ------------------------------------------------------------------ guilloche (mühür halkası)
def _f(x):
    return f'{x:.1f}'


def _wavy(cx, cy, R, a, nw, ph, steps=900):
    pts = []
    for k in range(steps + 1):
        t = 2 * pi * k / steps
        r = R + a * sin(nw * t + ph)
        pts.append(f'{_f(cx + r * cos(t))} {_f(cy + r * sin(t))}')
    return 'M' + ' L'.join(pts) + 'Z'


def seal_ring(cx, cy, r_in=124, r_out=170, n=7, amp=4.5, nw=40, sw=2.0):
    """İki zıt fazlı dalgalı halka demeti (lacivert + şarap), iç ve dış çember. Çizgiler 2 px."""
    out = []
    gap = (r_out - r_in - 2 * amp) / max(1, n - 1)
    for k in range(n):
        R = r_in + amp + k * gap
        out.append(f'<path d="{_wavy(cx, cy, R, amp, nw, k * 0.42)}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-opacity=".55"/>')
        out.append(f'<path d="{_wavy(cx, cy, R, amp, nw, pi + k * 0.42)}" fill="none" stroke="{WINE}" stroke-width="{sw}" stroke-opacity=".55"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r_in - 6}" fill="none" stroke="{WINE}" stroke-width="2"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r_out + 6}" fill="none" stroke="{INK}" stroke-width="2"/>')
    return ''.join(out)
