"""python3 v8_build.py prep <kaynak_klasör>   -> assets_v8/ (fotoğraf tonu, mühür, halka)
python3 v8_build.py [preview|publish]      -> out_v8/project/ (deck.json, deck.css, slides/)

prep kaynakları (v7 sunumundan indirilen MEYEM varlıkları, dosya adı = asset id):
  e81c0d26764c146f3738e0893b9490a6.png  kapak fotoğrafı (MEYEM web sitesi)
  1a0cb6a8bedfd7ab252f1e1722b55d8d.jpg  işyerinde sınav fotoğrafı (MEYEM web sitesi)
  432d3f3d2cae2a60ac6250ef5b10d0fb.png  MEYEM mührü
"""
import sys, os, json, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v8_common import *
import v8_slides as S

mode = sys.argv[1] if len(sys.argv) > 1 else 'preview'

if mode == 'prep':
    src = sys.argv[2]
    kx, ky, kw, kh = col(6), 0, W - col(6), H
    grade(f'{src}/e81c0d26764c146f3738e0893b9490a6.png', f'{ASSETS}/v8_kapak_foto.jpg', kw, kh, focus=(0.52, 0.5), scale=1.5)
    x, y, w, h = S.ISYERI_PH
    grade(f'{src}/1a0cb6a8bedfd7ab252f1e1722b55d8d.jpg', f'{ASSETS}/v8_isyeri_foto.jpg', w, h, focus=(0.5, 0.45), scale=1.5)
    shutil.copy(f'{src}/432d3f3d2cae2a60ac6250ef5b10d0fb.png', f'{ASSETS}/logo_seal.png')
    c = S.MEDAL / 2
    ring = f'<circle cx="{c}" cy="{c}" r="{c - 12}" fill="{PAPER}"/>' + seal_ring(c, c, r_in=124, r_out=170)
    bake_alpha('v8_muhur_halka', ring, S.MEDAL, S.MEDAL, dsf=2)
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
    'createdOnFiles': {'v': 1, 'at': '2026-11-14T12:00:00Z'},
    'lists': 'css',
    'format': {'v': 1, 'shared': ['project/deck.css']},
    'title': 'MEYEM Vizyon 2027',
    'order': order,
    'sections': {},
    'faces': FACES,
    'designSystems': [],
}
open(f'{PROJ}/deck.json', 'w').write(json.dumps(dj, ensure_ascii=False, indent=1) + '\n')
open(f'{PROJ}/deck.css', 'w').write(CSS.strip() + '\n')
print('slaytlar:', order, '| varlık:', sorted(USED))
