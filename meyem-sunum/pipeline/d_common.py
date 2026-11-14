import os
"""MEYEM Vizyon Gravür: ortak yardımcılar, CSS ve varlık çözümleyici."""
import html, os, json, shutil
from gx import *

OUT = M2 + '/out'
PROJ = OUT + '/project'
STAGE = M2 + '/stage'
ASSETS = M2 + '/assets'
URLS = os.path.join(os.path.dirname(M2), 'data', 'assets.json')

MODE = {'v': 'preview'}          # 'preview' | 'publish'
USED = {}                        # yayın adı -> kaynak dosya


def esc(s):
    return html.escape(str(s), quote=False)


def tr_upper(s):
    return s.replace('i', 'İ').replace('ı', 'I').upper()


def url_for(fn):
    """fn: yayın dosya adı (ör. bk_kapak.jpg, eng_cover.png)."""
    src = f'{ART}/{fn}' if fn.startswith('bk_') else f'{ASSETS}/{fn}'
    USED[fn] = src
    if MODE['v'] == 'preview':
        return 'file://' + src
    return json.load(open(URLS))[fn]


# ------------------------------------------------------------------ CSS
CSS = """
.s{position:relative;color:#00244D;font-family:'Hanken Grotesk',Arial,sans-serif;counter-increment:page;overflow:hidden}
.pa{background:#F8F4EC}.pb{background:#F4E8EB}.pc{background:#E9EFF6}.pd{background:#FBFAF6}
.s::after{content:counter(page);position:absolute;right:128px;bottom:64px;font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;letter-spacing:2px;color:#2C4868}
.cover::after,.closing::after{content:""}
.bk{position:absolute}
.pin{position:absolute}
.k{font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;letter-spacing:3px;color:#77183A;line-height:1.2}
.fl{font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;letter-spacing:2px;color:#2C4868;line-height:1}
.t1{font-family:'Bricolage Grotesque',Arial,sans-serif;font-weight:800;color:#00244D;letter-spacing:-2px;line-height:1.02}
.t2{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;color:#77183A;line-height:1.0;letter-spacing:0}
.lead{font-size:34px;line-height:1.42;color:#2C4868;font-weight:400}
.body{font-size:30px;line-height:1.42;color:#2C4868;font-weight:400}
.sm{font-size:26px;line-height:1.38;color:#2C4868;font-weight:400}
.ct{font-family:'Bricolage Grotesque',Arial,sans-serif;font-weight:700;font-size:40px;line-height:1.08;color:#00244D;letter-spacing:-0.5px}
.mono{font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;letter-spacing:2px;color:#2C4868;line-height:1.32}
.num{font-family:'Instrument Serif',Georgia,serif;font-weight:400;color:#77183A;line-height:.92}
.numb{font-family:'Bricolage Grotesque',Arial,sans-serif;font-weight:800;color:#00244D;line-height:1;letter-spacing:-2px}
.chip{font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;letter-spacing:1.5px;color:#00244D;border:1.5px solid #77183A;border-radius:999px;padding:11px 24px;line-height:1.1;background:rgba(255,255,255,.55)}
.ph{object-fit:cover}
@keyframes rise{from{opacity:0;transform:translateY(26px)}}
@keyframes fadein{from{opacity:0}}
.rise{animation:rise .85s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i,0)*110ms)}
.fadein{animation:fadein 1.1s ease both;animation-delay:calc(var(--i,0)*110ms)}
"""

FACES = {
    'bricolage-grotesque': {'family': 'Bricolage Grotesque', 'href': 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@300..800&display=swap'},
    'hanken-grotesk': {'family': 'Hanken Grotesk', 'href': 'https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300..700&display=swap'},
    'instrument-serif': {'family': 'Instrument Serif', 'href': 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap'},
    'jetbrains-mono': {'family': 'JetBrains Mono', 'href': 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400..700&display=swap'},
}


# ------------------------------------------------------------------ yerleşim yardımcıları
def sty(x=None, y=None, w=None, h=None, extra=''):
    s = ''
    if x is not None:
        s += f'left:{x}px;'
    if y is not None:
        s += f'top:{y}px;'
    if w is not None:
        s += f'width:{w}px;'
    if h is not None:
        s += f'height:{h}px;'
    return s + extra


def P(cls, x, y, w, text, fs=None, extra='', tag='p', raw=False, i=None):
    st = sty(x, y, w, None, extra)
    if fs:
        st += f'font-size:{fs}px;'
    cl = 'pin ' + cls + (' rise' if i is not None else '')
    if i is not None:
        st += f'--i:{i};'
    body = text if raw else esc(text)
    return f'<{tag} class="{cl}" style="{st}">{body}</{tag}>'


def IMG(fn, x, y, w, h, alt='', extra='', cls='pin', i=None):
    st = sty(x, y, w, h, extra)
    cl = cls + (' fadein' if i is not None else '')
    if i is not None:
        st += f'--i:{i};'
    return f'<img class="{cl}" src="{url_for(fn)}" alt="{esc(alt)}" style="{st}">'


def BK(sid):
    return f'<img class="bk" src="{url_for("bk_" + sid + ".jpg")}" alt="" style="left:0;top:0;width:1920px;height:1080px">'


def TITLE(l1, l2, x=128, y=112, w=1100, s1=104, s2=124, i0=0):
    """İki sesli başlık: Bricolage 800 + Instrument Serif italik (ayrı bloklar)."""
    h1 = P('t1', x, y, w, l1, s1, tag='h2', i=i0)
    y2 = y + int(s1 * 1.02) - 4
    h2 = P('t2', x, y2, w, l2, s2, tag='h2', i=i0 + 1)
    return h1 + '\n' + h2


def FOOT(label=None):
    return P('fl', 128, 992, 1000, 'MEYEM · MYK YB-0079 · TÜRKAK AB-0126-P', extra='bottom:auto;')


def SEC(sid, tone, inner, notes, cls=''):
    return (f'<section id="{sid}" class="s p{tone}{(" " + cls) if cls else ""}" data-transition="fade">\n{inner}\n'
            f'<aside>{esc(notes)}</aside>\n</section>\n')


def CHIPS(items, x, y, gap=14, fs=None):
    """Satır içi çipler (akış yerine sabit konum: genişlik tahmini)."""
    out = []
    cx = x
    for t in items:
        w = int(len(t) * 14.6 + 52)
        out.append(P('chip', cx, y, None, t, extra='white-space:nowrap;'))
        cx += w + gap
    return ''.join(out)


def RULE(x, y, w, h=1.5, color='#00244D', op=1.0):
    return f'<div class="pin" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};opacity:{op}"></div>'


def VRULE(x, y, h, w=1.5, color='#00244D', op=1.0):
    return RULE(x, y, w, h, color, op)


def arch_outline(x, y, w, h, color=WINE, sw=1.4, op=0.9, off=0, fill='none'):
    x0, y0, w2, h2 = x - off, y - off, w + 2 * off, h + 2 * off
    r = w2 / 2
    d = f'M{f1(x0)} {f1(y0 + h2)} L{f1(x0)} {f1(y0 + r)} A{f1(r)} {f1(r)} 0 0 1 {f1(x0 + w2)} {f1(y0 + r)} L{f1(x0 + w2)} {f1(y0 + h2)}'
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-opacity="{op}" stroke-linejoin="round"/>'
