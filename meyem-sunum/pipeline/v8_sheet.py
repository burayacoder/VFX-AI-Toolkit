"""python3 v8_sheet.py <qa_klasörü> <çıktı.png>
Tasarım sistemi kartını üretir ve 3 örnek slaytla birlikte tek temas sayfasına dizer (Archivo ile, DSF 1)."""
import sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_common import *

qa, out = sys.argv[1], sys.argv[2]
fonts = open(M2 + '/fonts/fonts_v8.css').read().replace('url(fonts/', f'url(file://{M2}/fonts/')
base = f'<meta charset="utf-8"><style>{fonts}\n*{{margin:0;padding:0;box-sizing:border-box}}\n{CSS}</style>'


def shoot(html_path, png, w, h):
    jobs = f'{ART}/_jobs_sheet.json'
    json.dump([{'html': html_path, 'out': png, 'w': w, 'h': h, 'dsf': 1, 'wait': 500}], open(jobs, 'w'))
    subprocess.run(['node', M2 + '/shoot2.js', jobs], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'})


# ---- tasarım sistemi kartı (1920×1080)
gx = ''.join(f'<div style="position:absolute;left:{col(i)}px;top:0;width:{span(1)}px;height:1080px;background:#00244D;opacity:.045"></div>' for i in range(12))
sw = [('#00244D', 'Lacivert', 'metin'), ('#77183A', 'Şarap', 'tek vurgu'), ('#C9D2DD', 'Açık ton', 'ikincil'),
      ('#F8F4EC', 'Kâğıt', 'zemin'), ('#2C4868', 'Gövde', 'kaynak')]
sws = ''.join(
    f'<div style="position:absolute;left:{col(6) + k * 162}px;top:420px;width:140px;height:140px;background:{c};border:2px solid #D8D2C4"></div>'
    f'<p class="pin xs" style="left:{col(6) + k * 162}px;top:576px;width:150px;color:#00244D;font-weight:700">{n}</p>'
    f'<p class="pin xs" style="left:{col(6) + k * 162}px;top:610px;width:150px">{c}<br>{r}</p>' for k, (c, n, r) in enumerate(sw))
card = f"""<section class="s cover" style="width:1920px;height:1080px">{gx}
<p class="pin xs" style="left:128px;top:72px;width:900px;color:#77183A;font-weight:700">TASARIM SİSTEMİ · v8</p>
<p class="pin nb" style="left:128px;top:150px;width:700px">244</p>
<p class="pin xs" style="left:560px;top:180px;width:300px">240 · büyük sayı<br>Archivo, %62 genişlik</p>
<h2 class="pin tt" style="left:128px;top:400px;width:840px">Başlık tek cümledir.</h2>
<p class="pin xs" style="left:128px;top:500px;width:600px">88 · başlık · y=112, en çok 2 satır</p>
<p class="pin md" style="left:128px;top:580px;width:840px">27 zorunlu · 28 gönüllü</p>
<p class="pin xs" style="left:128px;top:644px;width:600px">48 · vurgu ve veri etiketi</p>
<p class="pin bd" style="left:128px;top:720px;width:840px">Gövde metni slaytta en fazla 25 kelimedir.</p>
<p class="pin xs" style="left:128px;top:774px;width:600px">32 · gövde</p>
<p class="pin xs" style="left:128px;top:850px;width:840px">Kaynak: MYK Portal, Kasım 2026 · 24 · kaynak satırı, y=992</p>
<p class="pin md" style="left:{col(6)}px;top:150px;width:{span(6)}px">Tek aile, beş boy, iki renk.</p>
<p class="pin bd" style="left:{col(6)}px;top:230px;width:{span(6)}px">12 sütun · kenar 128 · oluk 32. Fotoğraf düz dikdörtgen, tek ton ayarı, kenardan taşar. Guilloche yalnızca kapak, bölüm açılışı, mühür ve kapanışta; çizgi en az 2 px.</p>
{sws}
<img class="pin" src="file://{ASSETS}/v8_muhur_halka.png" style="left:{col(9)}px;top:700px;width:300px;height:300px">
<img class="pin" src="file://{ASSETS}/logo_seal.png" style="left:{col(9) + 150 - 85}px;top:{700 + 150 - 83}px;width:171px;height:167px">
<p class="pin xs" style="left:{col(6)}px;top:780px;width:{span(3)}px">Mühür halkası: lacivert ve şarap, 2 px dalgalı çizgi</p>
</section>"""
hp = f'{ART}/_sistem.html'
open(hp, 'w').write(f'<html><head>{base}</head><body style="width:1920px;height:1080px">{card}</body></html>')
shoot(hp, f'{qa}/sistem.png', 1920, 1080)

# ---- temas sayfası: 2×2, başlıklı
tiles = [('kapak', '1 · Kapak'), ('kapsam', '6 · Veri: kapsam'), ('isyeri', '5 · Fotoğraf: sınav işyerinde'), ('sistem', 'Tasarım sistemi')]
cells = ''.join(
    f'<div style="position:absolute;left:{(k % 2) * 968 + 16}px;top:{(k // 2) * 600 + 16}px;width:944px">'
    f'<p style="font:700 24px/1 Archivo,sans-serif;color:#00244D;height:40px">{t}</p>'
    f'<img src="file://{qa}/{sid}.png" style="width:944px;height:531px;display:block;box-shadow:0 0 0 1px #D8D2C4"></div>'
    for k, (sid, t) in enumerate(tiles))
hp = f'{ART}/_sheet.html'
open(hp, 'w').write(f'<html><head>{base}</head><body style="width:1952px;height:1216px;background:#FFFFFF;position:relative">{cells}</body></html>')
shoot(hp, out, 1952, 1216)
print(out)
