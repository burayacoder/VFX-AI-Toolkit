import os
"""python3 d_build.py [preview|publish] [ids,...]  -> out/project/..."""
import sys, os, json, datetime, shutil, importlib
sys.path.insert(0, M2 := os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, M2 + '/pylib')
from d_common import *

mode = sys.argv[1] if len(sys.argv) > 1 else 'preview'
only = sys.argv[2].split(',') if len(sys.argv) > 2 else None
MODE['v'] = mode

mods = []
for name in ('d_slides1', 'd_slides2', 'd_slides3'):
    try:
        mods.append(importlib.import_module(name))
    except ModuleNotFoundError:
        pass
SL = []
for m in mods:
    SL += getattr(m, [k for k in dir(m) if k.startswith('SLIDES')][0])
by_id = {s[0]: s for s in SL}
VER = os.environ.get('MEYEM_VER', '7')
if VER == '10':
    import d_slides5 as V2
else:
    import d_slides4 as V2
final = []
for sid in V2.ORDER_V2:
    if sid in V2.OVERRIDES:
        tone, art_, htm_, notes_, cls_ = V2.OVERRIDES[sid]
        final.append((sid, tone, art_, htm_, notes_, cls_))
    else:
        final.append(by_id[sid])
SL = final
ORDER = [s[0] for s in SL]

# 1) arka planlar
jobs = []
for sid, tone, art, htm, notes, cls in SL:
    if only and sid not in only:
        continue
    inner, defs = art()
    jobs.append((f'{sid}', svg(inner, defs=defs)))
if jobs and mode == 'preview':
    # ART klasöründe bk_<sid> adıyla
    bake([(f'bk_{n}', s) for n, s in jobs], dsf=2, jpg=True, q=90)

# 2) slayt dosyaları
os.makedirs(PROJ + '/slides', exist_ok=True)
for sid, tone, art, htm, notes, cls in SL:
    if only and sid not in only:
        continue
    h = SEC(sid, tone, htm(), notes, cls)
    open(f'{PROJ}/slides/{sid}.html', 'w').write(h)

dj = {
    'v': 5,
    'createdOnFiles': {'v': 1, 'at': '2026-11-14T08:34:37Z'},
    'lists': 'css',
    'format': {'v': 1, 'shared': ['project/deck.css']},
    'title': 'MEYEM Vizyon Gravür v10' if VER == '10' else 'MEYEM Vizyon Gravür',
    'order': ORDER,
    'sections': {
        's1': {'description': 'Güven: kim olduğumuz ve hangi yetkiyle çalıştığımız', 'start': 'kapak'},
        's2': {'description': 'Gereklilik ve kapsam: takvim, meslek alanları ve 55 yeterlilik', 'start': 'takvim'},
        's3': {'description': 'Yöntem: yerinde sınav, süreç ve teşvik', 'start': 'yerinde'},
        's4': {'description': 'Kanıt ve eylem: referanslar, vizyon, model ve iletişim', 'start': 'referans'},
    },
    'faces': FACES,
    'designSystems': [],
}
open(f'{PROJ}/deck.json', 'w').write(json.dumps(dj, ensure_ascii=False, indent=1) + '\n')
open(f'{PROJ}/deck.css', 'w').write(CSS.strip() + '\n')
json.dump({k: v for k, v in USED.items()}, open(M2 + '/out/used.json', 'w'), indent=1)
print('slides:', ORDER)
print('assets used:', len(USED))
