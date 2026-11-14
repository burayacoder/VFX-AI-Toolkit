"""python3 v9_build.py prep <MEYEM varlık klasörü>  -> assets_v9/ (pişmiş arka planlar, kapak fotoğrafı, mühür)
python3 v9_build.py [preview|publish]               -> out_v9/project/
"""
import sys, os, json, shutil, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v9_art as A
import v9_slides as S

mode = sys.argv[1] if len(sys.argv) > 1 else 'preview'
OUT = A.M2 + '/out_v9'
PROJ = OUT + '/project'

if mode == 'prep':
    from v8_common import grade
    src = sys.argv[2]
    x, y, w, h = A.PH
    grade(f'{src}/e81c0d26764c146f3738e0893b9490a6.png', f'{A.ASSETS}/v9_kapak_foto.jpg', w, h, focus=(0.55, 0.5), scale=2)
    for f in ('logo_seal.png', 'v8_muhur_halka.png'):
        shutil.copy(f'{A.M2}/assets_v8/{f}', f'{A.ASSETS}/{f}')
    A.bake(sys.argv[3].split(',') if len(sys.argv) > 3 else None)
    print('prep tamam:', sorted(os.listdir(A.ASSETS)))
    sys.exit(0)

S.MODE['v'] = mode
os.makedirs(PROJ + '/slides', exist_ok=True)
order = []
for sid, fn, notes, cls in S.SLIDES:
    open(f'{PROJ}/slides/{sid}.html', 'w').write(S.SEC(sid, fn(), notes, cls))
    order.append(sid)
dj = {'v': 5, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},
      'lists': 'css', 'format': {'v': 1, 'shared': ['project/deck.css']}, 'title': 'MEYEM Vizyon v9 (örnek)', 'cover': 'kapak',
      'order': order, 'sections': {'s1': {'description': 'Örnek: kapak, takvim ve kapsam', 'start': 'kapak'}},
      'faces': S.FACES, 'designSystems': []}
if os.path.exists(f'{PROJ}/deck.json'):
    dj['createdOnFiles'] = json.load(open(f'{PROJ}/deck.json')).get('createdOnFiles', dj['createdOnFiles'])
open(f'{PROJ}/deck.json', 'w').write(json.dumps(dj, ensure_ascii=False, indent=1) + '\n')
open(f'{PROJ}/deck.css', 'w').write(S.CSS.strip() + '\n')
print('slaytlar:', order, '| varlık:', sorted(S.USED))
