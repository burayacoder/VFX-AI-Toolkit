import os
"""Fotoğraf işleme: gravür (banknot portresi), kemer pencere, pul, madalyon."""
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops

M2 = os.environ.get('MEYEM_WORK', os.path.dirname(os.path.abspath(__file__)))
S = os.environ.get('MEYEM_SRC', os.path.join(os.path.dirname(M2), 'kaynak'))
PH = M2 + '/photos'
os.makedirs(PH, exist_ok=True)


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def cover_crop(im, w, h, cx=0.5, cy=0.5, zoom=1.0):
    """w×h'e kapla; (cx, cy) odak noktası (0-1), zoom>1 yakınlaştırır."""
    iw, ih = im.size
    sc = max(w / iw, h / ih) * zoom
    nw, nh = int(round(iw * sc)), int(round(ih * sc))
    r = im.resize((nw, nh), Image.LANCZOS)
    x0 = int(round(cx * nw - w / 2)); y0 = int(round(cy * nh - h / 2))
    x0 = max(0, min(nw - w, x0)); y0 = max(0, min(nh - h, y0))
    return r.crop((x0, y0, x0 + w, y0 + h))


# ------------------------------------------------------------------ gravür
def engrave(im, w, h, pitch=6.0, ink='#00244D', ink2='#77183A', amp=1.5, wl=110, gamma=1.15, ss=3, hatch=True,
            cx=0.5, cy=0.5, zoom=1.0, lo=0.06, hi=0.94, bg=None, strength=1.0, tilt=0.0):
    """Fotoğrafı banknot gravürüne çevirir: kalınlığı koyuluğa göre değişen dalgalı çizgiler.
    w,h çıkış px (2× baskı için çağıran ölçeği verir). Şeffaf RGBA döner (bg verilirse düz zemin)."""
    base = cover_crop(im.convert('RGB'), w, h, cx, cy, zoom)
    gl = base.convert('L').filter(ImageFilter.GaussianBlur(max(0.8, w / 520)))
    g = np.asarray(ImageOps.autocontrast(gl, cutoff=0.6), dtype=np.float32) / 255.0
    # yerel kontrast: büyük bulanıktan çıkar
    bl = np.asarray(Image.fromarray((g * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(max(6, w / 12))), dtype=np.float32) / 255.0
    g = np.clip(g + 0.45 * (g - bl), 0, 1)
    dark = np.clip((1 - g - lo) / (hi - lo), 0, 1) ** gamma
    dark = dark * strength
    W2, H2 = w * ss, h * ss
    mask = Image.new('L', (W2, H2), 0)
    dr = ImageDraw.Draw(mask)
    xs = np.arange(0, W2, 2)
    n = int(h / pitch) + 3
    for i in range(-1, n):
        y0 = i * pitch * ss
        ph = 0.0
        yy = y0 + amp * ss * np.sin(2 * math.pi * xs / (wl * ss) + ph) + tilt * (xs - W2 / 2) / W2 * pitch * ss
        px = np.clip((xs / ss).astype(int), 0, w - 1)
        py = np.clip((yy / ss).astype(int), 0, h - 1)
        d = dark[py, px]
        half = 0.5 * pitch * ss * np.clip(d * 1.05, 0, 0.90)
        top = np.stack([xs, yy - half], 1)
        bot = np.stack([xs[::-1], (yy + half[::-1] if False else (yy + half))[::-1]], 1)
        poly = [tuple(p) for p in top] + [tuple(p) for p in bot]
        dr.polygon(poly, fill=255)
    # çapraz tarama (koyu bölgeler)
    if hatch:
        ang = 58
        big = int(math.hypot(w, h)) + 4
        dk = Image.fromarray((dark * 255).astype(np.uint8)).resize((w, h))
        canvas = Image.new('L', (big, big), 0)
        canvas.paste(dk, ((big - w) // 2, (big - h) // 2))
        rot = canvas.rotate(ang, resample=Image.BICUBIC)
        rd = np.asarray(rot, dtype=np.float32) / 255.0
        m2 = Image.new('L', (big * ss, big * ss), 0)
        d2 = ImageDraw.Draw(m2)
        xs2 = np.arange(0, big * ss, 3)
        p2 = pitch * 1.25
        for i in range(0, int(big / p2) + 1):
            y0 = i * p2 * ss
            px = np.clip((xs2 / ss).astype(int), 0, big - 1)
            py = np.clip(int(y0 / ss), 0, big - 1)
            dv = rd[py, px]
            dv = np.clip((dv - 0.52) / 0.48, 0, 1)
            half = 0.5 * p2 * ss * 0.8 * dv
            if half.max() < 0.3:
                continue
            top = np.stack([xs2, y0 - half], 1)
            bot = np.stack([xs2[::-1], (y0 + half)[::-1]], 1)
            d2.polygon([tuple(p) for p in top] + [tuple(p) for p in bot], fill=255)
        m2 = m2.resize((big, big), Image.LANCZOS).rotate(-ang, resample=Image.BICUBIC)
        ox, oy = (big - w) // 2, (big - h) // 2
        m2 = m2.crop((ox, oy, ox + w, oy + h))
    else:
        m2 = Image.new('L', (w, h), 0)
    m1 = mask.resize((w, h), Image.LANCZOS)
    col1, col2 = hexrgb(ink), hexrgb(ink2)
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    l2 = Image.new('RGBA', (w, h), col2 + (0,)); l2.putalpha(m2)
    l1 = Image.new('RGBA', (w, h), col1 + (0,)); l1.putalpha(m1)
    out = Image.alpha_composite(out, l2)
    out = Image.alpha_composite(out, l1)
    if bg:
        b = Image.new('RGBA', (w, h), hexrgb(bg) + (255,))
        out = Image.alpha_composite(b, out)
    return out


# ------------------------------------------------------------------ biçimli pencereler
def arch_mask(w, h, ss=3, top_r=None):
    r = top_r or w / 2
    m = Image.new('L', (w * ss, h * ss), 0)
    d = ImageDraw.Draw(m)
    d.rectangle((0, r * ss, w * ss, h * ss), fill=255)
    d.ellipse((0, 0, w * ss, 2 * r * ss), fill=255)
    return m.resize((w, h), Image.LANCZOS)


def circle_mask(d, ss=3):
    m = Image.new('L', (d * ss, d * ss), 0)
    ImageDraw.Draw(m).ellipse((0, 0, d * ss - 1, d * ss - 1), fill=255)
    return m.resize((d, d), Image.LANCZOS)


def tone(im, warm=0.0, sat=1.0, contrast=1.0, bright=1.0):
    from PIL import ImageEnhance
    im = im.convert('RGB')
    if sat != 1.0:
        im = ImageEnhance.Color(im).enhance(sat)
    if contrast != 1.0:
        im = ImageEnhance.Contrast(im).enhance(contrast)
    if bright != 1.0:
        im = ImageEnhance.Brightness(im).enhance(bright)
    if warm:
        r, g, b = im.split()
        r = r.point(lambda v: min(255, int(v * (1 + warm * 0.06))))
        b = b.point(lambda v: int(v * (1 - warm * 0.05)))
        im = Image.merge('RGB', (r, g, b))
    return im


def duotone(im, dark, light, contrast=1.0):
    g = ImageOps.autocontrast(im.convert('L'), cutoff=1)
    d, l = hexrgb(dark), hexrgb(light)
    lut = [[int(d[c] + (l[c] - d[c]) * ((i / 255.0) ** contrast)) for i in range(256)] for c in range(3)]
    return Image.merge('RGB', (g.point(lut[0]), g.point(lut[1]), g.point(lut[2])))


def arch_photo(im, w, h, cx=0.5, cy=0.5, zoom=1.0, ss=3):
    """w×h (px, 2× baskı) kemer penceresi, şeffaf RGBA."""
    ph = cover_crop(im, w, h, cx, cy, zoom).convert('RGBA')
    ph.putalpha(arch_mask(w, h, ss))
    return ph


def circle_photo(im, d, cx=0.5, cy=0.5, zoom=1.0):
    ph = cover_crop(im, d, d, cx, cy, zoom).convert('RGBA')
    ph.putalpha(circle_mask(d))
    return ph


def stamp(im, w, h, margin=None, perf=None, paper=(251, 248, 241), cx=0.5, cy=0.5, zoom=1.0, ink='#00244D', ss=3):
    """Dişli pul: kenarları delikli kâğıt + ince çerçeveli fotoğraf (RGBA)."""
    margin = margin or int(w * 0.075)
    perf = perf or max(6, int(w * 0.030))
    W3, H3 = w * ss, h * ss
    m = Image.new('L', (W3, H3), 255)
    d = ImageDraw.Draw(m)
    step = perf * 2.6 * ss
    # delikler: kenar boyunca eşit aralıklı daireler
    def holes(length, fixed, horizontal):
        cnt = max(3, int(round(length / step)))
        sp = length / cnt
        for i in range(cnt + 1):
            p = i * sp
            r = perf * ss
            if horizontal:
                d.ellipse((p - r, fixed - r, p + r, fixed + r), fill=0)
            else:
                d.ellipse((fixed - r, p - r, fixed + r, p + r), fill=0)
    holes(W3, 0, True); holes(W3, H3, True); holes(H3, 0, False); holes(H3, W3, False)
    m = m.resize((w, h), Image.LANCZOS)
    out = Image.new('RGBA', (w, h), paper + (255,))
    inner = (margin, margin, w - margin, h - margin)
    ph = cover_crop(im, inner[2] - inner[0], inner[3] - inner[1], cx, cy, zoom).convert('RGBA')
    out.paste(ph, (inner[0], inner[1]))
    dd = ImageDraw.Draw(out)
    dd.rectangle((inner[0] - 1, inner[1] - 1, inner[2], inner[3]), outline=hexrgb(ink) + (255,), width=max(2, int(w * 0.006)))
    out.putalpha(m)
    return out


def medallion(im, d, ring='#77183A', ring2='#00244D', cx=0.5, cy=0.5, zoom=1.0, ss=3, pad=None):
    """Yuvarlak fotoğraf + iki ince halka (RGBA). Çıkış d×d, halkalar kenarda."""
    pad = pad or int(d * 0.06)
    inner = d - 2 * pad
    ph = circle_photo(im, inner, cx, cy, zoom)
    out = Image.new('RGBA', (d, d), (0, 0, 0, 0))
    out.paste(ph, (pad, pad), ph)
    big = Image.new('RGBA', (d * ss, d * ss), (0, 0, 0, 0))
    dr = ImageDraw.Draw(big)
    c = d * ss / 2
    for r, col, wd in ((d / 2 - 2, ring, 2), (d / 2 - pad * 0.45, ring2, 1.2)):
        rr = r * ss
        dr.ellipse((c - rr, c - rr, c + rr, c + rr), outline=hexrgb(col) + (255,), width=int(wd * ss))
    # küçük çentikler
    for k in range(72):
        a = 2 * math.pi * k / 72
        r0, r1 = (d / 2 - pad * 0.45 - 6) * ss, (d / 2 - pad * 0.45 - (14 if k % 6 == 0 else 8)) * ss
        dr.line((c + r0 * math.cos(a), c + r0 * math.sin(a), c + r1 * math.cos(a), c + r1 * math.sin(a)), fill=hexrgb(ring2) + (200,), width=int(1.2 * ss))
    big = big.resize((d, d), Image.LANCZOS)
    return Image.alpha_composite(out, big)


def save_png(im, name, optimize=True):
    p = f'{PH}/{name}.png'
    im.save(p, 'PNG', optimize=optimize)
    return p


def save_jpg(im, name, q=90):
    p = f'{PH}/{name}.jpg'
    im.convert('RGB').save(p, 'JPEG', quality=q, subsampling=0, optimize=True)
    return p


def with_shadow(im, pad=48, blur=14, dy=10, op=0.30, color=(0, 36, 77)):
    w, h = im.size
    W2, H2 = w + 2 * pad, h + 2 * pad
    canvas = Image.new('RGBA', (W2, H2), (0, 0, 0, 0))
    mask = Image.new('L', (W2, H2), 0)
    mask.paste(im.getchannel('A'), (pad, pad + dy))
    mask = mask.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * op))
    sh = Image.new('RGBA', (W2, H2), color + (0,))
    sh.putalpha(mask)
    canvas = Image.alpha_composite(canvas, sh)
    canvas.alpha_composite(im, (pad, pad))
    return canvas
