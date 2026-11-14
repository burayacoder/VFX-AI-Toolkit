import os
"""MEYEM Gravür: guilloche çizim kütüphanesi (SVG üretir, Chromium ile PNG/JPG'ye pişirir)."""
import math, os, json, subprocess
from math import cos, sin, pi, gcd

M2 = os.environ.get('MEYEM_WORK', os.path.dirname(os.path.abspath(__file__)))
ART = M2 + '/art'
os.makedirs(ART, exist_ok=True)

W, H = 1920, 1080

# ---- Broşür paleti (hepsi açık zemin için) ----
INK = '#00244D'; INK2 = '#2C4868'; NAVY_M = '#18395E'; BLUE = '#3E5E86'; SKY = '#7E9DC2'
WINE = '#77183A'; WINE_D = '#580721'; WINE_L = '#832D4C'; ROSE = '#AA6E84'; BLUSH = '#DAC1CA'; ROSE50 = '#F4EFF1'
PAPER_A = '#F8F4EC'   # fildişi (ana)
PAPER_B = '#F4E8EB'   # gül kâğıdı
PAPER_C = '#E9EFF6'   # sis mavisi
PAPER_D = '#FBFAF6'   # aydınlık
PAPERS = {'a': PAPER_A, 'b': PAPER_B, 'c': PAPER_C, 'd': PAPER_D}


def f1(x):
    return f'{x:.1f}'


def f2(x):
    return f'{x:.2f}'


def pth(pts, close=False):
    s = 'M' + ' L'.join(f'{f1(x)} {f1(y)}' for x, y in pts)
    return s + ('Z' if close else '')


def line_path(d, color, sw=0.9, op=0.5, extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-opacity="{op}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


# ------------------------------------------------------------------ iris (güllü-mavi geçişli baskı)
def iris_defs(idn='iris', x1=0, x2=W, stops=((0, WINE), (0.5, BLUE), (1, INK)), y1=0, y2=0):
    st = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{idn}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{st}</linearGradient>'


# ------------------------------------------------------------------ hipotrokoid rozet (sevilen çizgi dili)
def hypo_pts(cx, cy, R, r, d, n=1500, rot=0.0, turns=None, sx=1.0, sy=1.0):
    Ri, ri = int(round(R)), int(round(r))
    turns = turns or (ri // gcd(Ri, ri))
    pts = []
    for k in range(n + 1):
        t = 2 * pi * turns * k / n
        x = (R - r) * cos(t) + d * cos((R - r) / r * t)
        y = (R - r) * sin(t) - d * sin((R - r) / r * t)
        xr = (x * cos(rot) - y * sin(rot)) * sx
        yr = (x * sin(rot) + y * cos(rot)) * sy
        pts.append((cx + xr, cy + yr))
    return pts


def rosette_flower(cx, cy, s=1.0, c1=INK, c2=WINE, op=0.46, sw=0.9, n=1700):
    """Kullanıcının sevdiği üç katmanlı hipotrokoid rozet."""
    g = []
    g.append(line_path(pth(hypo_pts(cx, cy, 300 * s, 85 * s, 190 * s, n=n), True), c1, sw, op))
    g.append(line_path(pth(hypo_pts(cx, cy, 300 * s, 85 * s, 150 * s, n=n, rot=pi / 17), True), c1, sw, op * 0.8))
    g.append(line_path(pth(hypo_pts(cx, cy, 252 * s, 72 * s, 120 * s, n=int(n * 0.9)), True), c2, sw, op * 0.95))
    for rr, o in ((120 * s, 0.5), (60 * s, 0.4)):
        g.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(rr)}" fill="none" stroke="{c1}" stroke-width="{sw}" stroke-opacity="{o * op * 1.6:.2f}"/>')
    return ''.join(g)


def rosette_lace(cx, cy, R=300, n=60, a=0.46, b=0.16, c=0.30, c1=INK, c2=WINE, op=0.5, sw=0.8, tilt=0.0):
    """Üst üste binen elipsler: sık dantel/banknot rozeti."""
    out = []
    for k in range(n):
        ang = 360.0 * k / n + tilt
        col = c1 if k % 2 == 0 else c2
        out.append(f'<ellipse cx="{f1(cx + R * c)}" cy="{f1(cy)}" rx="{f1(R * a)}" ry="{f1(R * b)}" transform="rotate({ang:.2f} {f1(cx)} {f1(cy)})" '
                   f'fill="none" stroke="{col}" stroke-width="{sw}" stroke-opacity="{op}"/>')
    return ''.join(out)


def rose_mesh(cx, cy, R=260, k=7, n=5, c1=INK, c2=WINE, op=0.5, sw=0.8, pts=1400, rot=0.0):
    """Gül eğrisi (r = R cos kθ) üst üste: çiçek/yıldız örgüsü."""
    out = []
    for j in range(n):
        Rj = R * (1 - 0.13 * j)
        ph = rot + j * pi / (k * 2)
        P = []
        for i in range(pts + 1):
            t = 2 * pi * i / pts
            r = Rj * cos(k * t + ph) * (0.55 + 0.45 * cos(t * 2 + j))
            P.append((cx + r * cos(t), cy + r * sin(t)))
        out.append(line_path(pth(P, True), c1 if j % 2 == 0 else c2, sw, op))
    return ''.join(out)


# ------------------------------------------------------------------ dalgalı halka demeti
def wavy_ring(cx, cy, R, a=6, nw=24, ph=0.0, steps=720, sx=1.0, sy=1.0):
    P = []
    for i in range(steps + 1):
        t = 2 * pi * i / steps
        r = R + a * sin(nw * t + ph)
        P.append((cx + r * cos(t) * sx, cy + r * sin(t) * sy))
    return P


def ring_bundle(cx, cy, R0, count=14, gap=3.2, a=5, nw=28, delta=0.35, c1=INK, c2=WINE, op=0.5, sw=0.8, mix=False):
    out = []
    for k in range(count):
        col = c1 if (k % 2 == 0 or not c2) else c2
        out.append(line_path(pth(wavy_ring(cx, cy, R0 + k * gap, a, nw, k * delta), True), col, sw, op))
    return ''.join(out)


def circle(cx, cy, r, stroke=INK, sw=1.0, op=0.6, fill='none', dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{op}"{d}/>'


def ticks(cx, cy, r, n=120, tl=9, tl2=20, every=5, color=INK, sw=1.0, op=0.5, a0=-pi / 2, span=2 * pi):
    out = []
    for i in range(n):
        a = a0 + span * i / n
        L = tl2 if i % every == 0 else tl
        out.append(f'M{f1(cx + r * cos(a))} {f1(cy + r * sin(a))}L{f1(cx + (r + L) * cos(a))} {f1(cy + (r + L) * sin(a))}')
    return line_path(''.join(out), color, sw, op)


# ------------------------------------------------------------------ mikro yazı halkası
def microring(cx, cy, r, text, fs=9, color=INK, op=0.7, uid='mr', ls=1.2, start=0.0):
    d = f'M{f1(cx - r)} {f1(cy)} a{f1(r)} {f1(r)} 0 1 1 {f1(2 * r)} 0 a{f1(r)} {f1(r)} 0 1 1 {f1(-2 * r)} 0'
    circ = 2 * pi * r
    rep = text + '  ·  '
    # çevreyi dolduracak kadar tekrar
    est = fs * 0.62 + ls
    need = int(circ / (est * len(rep))) + 1
    t = rep * need
    return (f'<defs><path id="{uid}" d="{d}" transform="rotate({start} {f1(cx)} {f1(cy)})"/></defs>'
            f'<text font-family="JetBrains Mono" font-weight="500" font-size="{fs}" letter-spacing="{ls}" fill="{color}" fill-opacity="{op}">'
            f'<textPath href="#{uid}" textLength="{f1(circ - 4)}" lengthAdjust="spacing">{t[:int(circ / est)]}</textPath></text>')


# ------------------------------------------------------------------ örgülü şerit (zaman çizelgesi / süreç)
def band(x0, x1, y, amp=26, wl=360, n=22, spread=4.2, phase=0.0, delta=0.30, c1=INK, c2=WINE, op=0.5, sw=0.85, env=0.35, steps=None, alt=True):
    out = []
    steps = steps or max(40, int((x1 - x0) / 5))
    for k in range(n):
        P = []
        for i in range(steps + 1):
            x = x0 + (x1 - x0) * i / steps
            a = amp * (1 + env * sin(2 * pi * (x - x0) / (wl * 2.7) + k * 0.04))
            yy = y + (k - (n - 1) / 2) * spread + a * sin(2 * pi * (x - x0) / wl + phase + k * delta)
            P.append((x, yy))
        col = c1 if (k % 2 == 0 or not alt) else c2
        out.append(line_path(pth(P), col, sw, op))
    return ''.join(out)


def braid(x0, x1, y, **kw):
    """İki zıt fazlı şerit: örgü/dokuma görünümü."""
    kw2 = dict(kw)
    kw2['delta'] = -kw.get('delta', 0.30)
    kw2['phase'] = kw.get('phase', 0.0) + pi
    return band(x0, x1, y, **kw) + band(x0, x1, y, **kw2)


def wave_lines(x0, x1, y0, y1, n=40, amp=14, wl=300, c=INK, op=0.35, sw=0.8, delta=0.2):
    out = []
    for k in range(n):
        yy0 = y0 + (y1 - y0) * k / max(1, n - 1)
        P = [(x, yy0 + amp * sin(2 * pi * (x - x0) / wl + k * delta)) for x in range(int(x0), int(x1) + 1, 6)]
        out.append(line_path(pth(P), c, sw, op))
    return ''.join(out)


# ------------------------------------------------------------------ 55 yapraklı veri rozeti
def petal_path(cx, cy, r0, r1, a, hw):
    """Yaprak: tabanı r0, ucu r1, a yönünde; hw açısal yarım genişlik."""
    rm = r0 + (r1 - r0) * 0.55
    bx, by = cx + r0 * cos(a), cy + r0 * sin(a)
    tx, ty = cx + r1 * cos(a), cy + r1 * sin(a)
    l1 = (cx + rm * cos(a - hw), cy + rm * sin(a - hw))
    l2 = (cx + (r0 + (r1 - r0) * 0.88) * cos(a - hw * 0.35), cy + (r0 + (r1 - r0) * 0.88) * sin(a - hw * 0.35))
    r2 = (cx + (r0 + (r1 - r0) * 0.88) * cos(a + hw * 0.35), cy + (r0 + (r1 - r0) * 0.88) * sin(a + hw * 0.35))
    r1p = (cx + rm * cos(a + hw), cy + rm * sin(a + hw))
    return (f'M{f1(bx)} {f1(by)} C{f1(l1[0])} {f1(l1[1])} {f1(l2[0])} {f1(l2[1])} {f1(tx)} {f1(ty)} '
            f'C{f1(r2[0])} {f1(r2[1])} {f1(r1p[0])} {f1(r1p[1])} {f1(bx)} {f1(by)}Z')


def petal_ring(cx, cy, r0, r1, n, fills, fill=WINE, stroke=WINE, accent=None, accent_idx=(), wid=0.9, veins=3, a0=-pi / 2, sw=0.9):
    out = []
    for i in range(n):
        a = a0 + 2 * pi * i / n
        hw = (pi / n) * wid
        d = petal_path(cx, cy, r0, r1, a, hw)
        is_fill = i in fills
        col = accent if (accent and i in accent_idx) else (fill if is_fill else None)
        if col:
            out.append(f'<path d="{d}" fill="{col}" fill-opacity="0.94" stroke="{col}" stroke-width="{sw}"/>')
            # açık damar çizgileri
            for v in range(1, veins + 1):
                f = v / (veins + 1)
                rr0 = r0 + (r1 - r0) * 0.10
                rr1 = r0 + (r1 - r0) * (0.55 + 0.30 * (1 - abs(f - 0.5) * 2))
                aa = a + (f - 0.5) * 2 * hw * 0.55
                out.append(line_path(f'M{f1(cx + rr0 * cos(aa))} {f1(cy + rr0 * sin(aa))}L{f1(cx + rr1 * cos(aa))} {f1(cy + rr1 * sin(aa))}', '#FFFFFF', 0.8, 0.42))
        else:
            out.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-opacity="0.78"/>')
            for v in range(1, veins + 1):
                f = v / (veins + 1)
                rr0 = r0 + (r1 - r0) * 0.10
                rr1 = r0 + (r1 - r0) * (0.50 + 0.30 * (1 - abs(f - 0.5) * 2))
                aa = a + (f - 0.5) * 2 * hw * 0.55
                out.append(line_path(f'M{f1(cx + rr0 * cos(aa))} {f1(cy + rr0 * sin(aa))}L{f1(cx + rr1 * cos(aa))} {f1(cy + rr1 * sin(aa))}', stroke, 0.7, 0.34))
    return ''.join(out)


# ------------------------------------------------------------------ yay göstergesi (halka ölçeği)
def arc_path(cx, cy, r, a0, a1):
    x0, y0 = cx + r * cos(a0), cy + r * sin(a0)
    x1, y1 = cx + r * cos(a1), cy + r * sin(a1)
    large = 1 if (a1 - a0) % (2 * pi) > pi else 0
    return f'M{f1(x0)} {f1(y0)} A{f1(r)} {f1(r)} 0 {large} 1 {f1(x1)} {f1(y1)}'


def arc_gauge(cx, cy, r, frac, color=WINE, sw=26, track=BLUSH, track_op=0.55, a0=-pi / 2, hatch=True, hatch_color='#FFFFFF'):
    out = []
    out.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(r)}" fill="none" stroke="{track}" stroke-opacity="{track_op}" stroke-width="{sw}"/>')
    if frac >= 0.999:
        out.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(r)}" fill="none" stroke="{color}" stroke-width="{sw}"/>')
    else:
        out.append(f'<path d="{arc_path(cx, cy, r, a0, a0 + 2 * pi * frac)}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="butt"/>')
    if hatch:  # iç ince çizgiler (gravür dokusu)
        for k in (-0.30, -0.10, 0.10, 0.30):
            rr = r + k * sw
            if frac >= 0.999:
                out.append(f'<circle cx="{f1(cx)}" cy="{f1(cy)}" r="{f1(rr)}" fill="none" stroke="{hatch_color}" stroke-opacity="0.45" stroke-width="0.8"/>')
            else:
                out.append(f'<path d="{arc_path(cx, cy, rr, a0, a0 + 2 * pi * frac)}" fill="none" stroke="{hatch_color}" stroke-opacity="0.45" stroke-width="0.8"/>')
    return ''.join(out)


# ------------------------------------------------------------------ zemin kâğıdı
def paper(tone='a', vignette=True):
    c = PAPERS[tone]
    s = f'<rect width="{W}" height="{H}" fill="{c}"/>'
    if vignette:
        s += (f'<defs><radialGradient id="vg" cx="0.5" cy="0.45" r="0.85"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.38"/>'
              f'<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient></defs>'
              f'<rect width="{W}" height="{H}" fill="url(#vg)"/>')
    return s


def svg(inner, w=W, h=H, defs=''):
    d = f'<defs>{defs}</defs>' if defs else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{d}{inner}</svg>'


# ------------------------------------------------------------------ pişirme (Chromium)
def bake(jobs, dsf=2, jpg=True, q=90):
    """jobs: [(name, svg_string)]  ->  art/<name>.png (+ .jpg)"""
    fonts_css = open(M2 + '/fonts/fonts.css').read().replace('url(fonts/', f'url(file://{M2}/fonts/')
    todo = []
    for name, s in jobs:
        html = (f'<html><head><meta charset="utf-8"><style>{fonts_css} html,body{{margin:0;padding:0;background:transparent}}</style></head>'
                f'<body style="position:relative;width:{W}px;height:{H}px;overflow:hidden">{s}</body></html>')
        hp = f'{ART}/_{name}.html'
        open(hp, 'w').write(html)
        todo.append({'html': hp, 'out': f'{ART}/{name}.png', 'w': W, 'h': H, 'dsf': dsf, 'wait': 500})
    json.dump(todo, open(f'{ART}/jobs.json', 'w'))
    subprocess.run(['node', M2 + '/shoot2.js', f'{ART}/jobs.json'], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})
    if jpg:
        from PIL import Image
        for name, _ in jobs:
            im = Image.open(f'{ART}/{name}.png').convert('RGB')
            im.save(f'{ART}/{name}.jpg', 'JPEG', quality=q, subsampling=0, optimize=True)
            print(name, im.size, os.path.getsize(f'{ART}/{name}.png') // 1024, 'KB png;', os.path.getsize(f'{ART}/{name}.jpg') // 1024, 'KB jpg')


def bake_alpha(name, inner, w, h, dsf=2, defs='', out_dir=None):
    """Küçük şeffaf PNG varlığı (assets/<name>.png)."""
    out_dir = out_dir or (M2 + '/assets')
    fonts_css = open(M2 + '/fonts/fonts.css').read().replace('url(fonts/', f'url(file://{M2}/fonts/')
    html = (f'<html><head><meta charset="utf-8"><style>{fonts_css} html,body{{margin:0;padding:0;background:transparent}}</style></head>'
            f'<body style="position:relative;width:{w}px;height:{h}px;overflow:hidden">{svg(inner, w, h, defs)}</body></html>')
    hp = f'{ART}/_a_{name}.html'
    open(hp, 'w').write(html)
    json.dump([{'html': hp, 'out': f'{out_dir}/{name}.png', 'w': w, 'h': h, 'dsf': dsf, 'wait': 400, 'transparent': True}], open(f'{ART}/jobs_a.json', 'w'))
    subprocess.run(['node', M2 + '/shoot2.js', f'{ART}/jobs_a.json'], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})
