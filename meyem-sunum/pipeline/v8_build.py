"""python3 v8_build.py prep <kaynak_klasör>   -> assets_v8/ (fotoğraf tonu, mühür, halka, bant, QR)
python3 v8_build.py [preview|publish]      -> out_v8/project/ (deck.json, deck.css, slides/)

prep kaynakları (v7 sunumundan indirilen MEYEM varlıkları, dosya adı = asset id):
  e81c0d26764c146f3738e0893b9490a6.png  kapak fotoğrafı (MEYEM web sitesi)
  1a0cb6a8bedfd7ab252f1e1722b55d8d.jpg  işyerinde sınav fotoğrafı (MEYEM web sitesi)
  c94dc59178b821f32c39c9287e0f2eaf.jpg  ekip eğitimi fotoğrafı (MEYEM web sitesi)
  ce38f7bec46f3acb29ce968555d93e6b.png  kapanış fotoğrafı (MEYEM web sitesi)
  432d3f3d2cae2a60ac6250ef5b10d0fb.png  MEYEM mührü
publish modu data/assets_v8.json (yayın adı -> /_blob/<id>) ister.
"""
import sys, os, json, shutil, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_common import *
import v8_slides as S

mode = sys.argv[1] if len(sys.argv) > 1 else 'preview'

if mode == 'prep':
    src = sys.argv[2]
    grade(f'{src}/e81c0d26764c146f3738e0893b9490a6.png', f'{ASSETS}/v8_kapak_foto.jpg', W - S.HALF, H, focus=(0.52, 0.5))
    x, y, w, h = S.ISYERI_PH
    grade(f'{src}/1a0cb6a8bedfd7ab252f1e1722b55d8d.jpg', f'{ASSETS}/v8_isyeri_foto.jpg', w, h, focus=(0.5, 0.45))
    grade(f'{src}/c94dc59178b821f32c39c9287e0f2eaf.jpg', f'{ASSETS}/v8_kazanc_foto.jpg', S.HALF - GUT, H - 344, focus=(0.55, 0.45))
    grade(f'{src}/ce38f7bec46f3acb29ce968555d93e6b.png', f'{ASSETS}/v8_kapanis_foto.jpg', W - S.HALF, H, focus=(0.55, 0.5))
    shutil.copy(f'{src}/432d3f3d2cae2a60ac6250ef5b10d0fb.png', f'{ASSETS}/logo_seal.png')
    c = S.MEDAL / 2
    bake_alpha('v8_muhur_halka', f'<circle cx="{c}" cy="{c}" r="{c - 12}" fill="{PAPER}"/>' + seal_ring(c, c), S.MEDAL, S.MEDAL)
    bake_alpha('v8_vizyon_bant', braid_band(1664, 96), 1664, 96)
    import qrcode
    from PIL import Image
    q = qrcode.QRCode(border=0, box_size=20, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data('https://meyem.com.tr')
    q.make(fit=True)
    q.make_image(fill_color=INK, back_color=PAPER).convert('RGB').resize((280, 280), Image.NEAREST).save(f'{ASSETS}/v8_qr.png')
    print('prep tamam:', sorted(os.listdir(ASSETS)))
    sys.exit(0)

MODE['v'] = mode
os.makedirs(PROJ + '/slides', exist_ok=True)
order = []
for sid, fn, notes, cls in S.SLIDES_V8:
    open(f'{PROJ}/slides/{sid}.html', 'w').write(SEC(sid, fn(), notes, cls))
    order.append(sid)
dj = {
    'v': 5,
    'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},
    'lists': 'css',
    'format': {'v': 1, 'shared': ['project/deck.css']},
    'title': 'MEYEM Vizyon 2027',
    'cover': 'kapak',
    'order': order,
    'sections': S.SECTIONS,
    'faces': FACES,
    'designSystems': [],
}
if os.path.exists(f'{PROJ}/deck.json'):                      # ilk yazımın zaman damgası korunur
    old = json.load(open(f'{PROJ}/deck.json'))
    dj['createdOnFiles'] = old.get('createdOnFiles', dj['createdOnFiles'])
open(f'{PROJ}/deck.json', 'w').write(json.dumps(dj, ensure_ascii=False, indent=1) + '\n')
open(f'{PROJ}/deck.css', 'w').write(CSS.strip() + '\n')
print('slaytlar:', order)
print('varlık:', sorted(USED))
