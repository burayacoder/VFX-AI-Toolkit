"""MEYEM · Gebze sunumu: python3 g_build.py [preview|publish] [ids,...]  -> out_g/project/..."""
import sys, os, json
sys.path.insert(0, M2 := os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, M2 + '/pylib')
os.environ.setdefault('MEYEM_URLS', os.path.join(os.path.dirname(M2), 'data', 'assets_gebze.json'))
from d_common import *
import d_common
import g_slides as G

mode = sys.argv[1] if len(sys.argv) > 1 else 'preview'
only = sys.argv[2].split(',') if len(sys.argv) > 2 else None
MODE['v'] = mode
OUTG = M2 + '/out_g'
PROJG = OUTG + '/project'
REUSED_BK = {'kapak', 'kapanis'}          # v10 ile aynı arka plan (yeniden pişirilmez)

if mode == 'preview':
    jobs = []
    for sid, tone, bk, art, htm, notes, cls in G.SLIDES:
        if bk in REUSED_BK or (only and sid not in only):
            continue
        inner, defs = art()
        jobs.append((f'bk_{bk}', svg(inner, defs=defs)))
    if jobs:
        bake(jobs, dsf=2, jpg=True, q=90)

os.makedirs(PROJG + '/slides', exist_ok=True)
for sid, tone, bk, art, htm, notes, cls in G.SLIDES:
    if only and sid not in only:
        continue
    open(f'{PROJG}/slides/{sid}.html', 'w').write(SEC(sid, tone, htm(), notes, cls))

ORDER = [s[0] for s in G.SLIDES]
dj = {
    'v': 5,
    'createdOnFiles': {'v': 1, 'at': '2026-11-16T03:00:00Z'},
    'lists': 'css',
    'format': {'v': 1, 'shared': ['project/deck.css']},
    'title': 'MEYEM · Gebze',
    'order': ORDER,
    'sections': {
        's1': {'description': 'Bölge: dört ilçede 309 üretici fabrika', 'start': 'kapak'},
        's2': {'description': 'Avantaj: kazan belgeleri ve bölgede az bulunan yetkiler', 'start': 'kazan'},
        's3': {'description': 'Firmalar: kazan, gıda ve metal segmentlerinde ilk ziyaretler', 'start': 'gfkazan'},
        's4': {'description': 'Yöntem ve takvim: yerinde sınav günü ve iki tarih', 'start': 'gun'},
    },
    'faces': FACES,
    'designSystems': [],
}
open(f'{PROJG}/deck.json', 'w').write(json.dumps(dj, ensure_ascii=False, indent=1) + '\n')
open(f'{PROJG}/deck.css', 'w').write(CSS.strip() + '\n')
json.dump(dict(USED), open(OUTG + '/used.json', 'w'), indent=1)
print('slides:', ORDER)
print('assets used:', len(USED))
