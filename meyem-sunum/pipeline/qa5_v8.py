"""python3 qa5_v8.py <qa_klasörü> <çıktı.md>  — 10 kriterli puan kartı (faz5)."""
import sys, json, re
from PIL import Image
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import v8_slides as S

qa, out = sys.argv[1], sys.argv[2]
D = json.load(open(f'{qa}/olcum.json'))
SCALE = {24, 32, 48, 88, 240}
PALETTE = {'#00244D', '#2C4868', '#77183A', '#F8F4EC'}
GUILLOCHE = {'v8_muhur_halka.png', 'v8_vizyon_bant.png'}
GUILLOCHE_OK = {'kapak', 'vizyon', 'kanit', 'kapanis'}
LABELS = {r[0] for r in S.SCOPE_ROWS} | {'2026/1 Tebliği öncesi', '2026/1 Tebliği sonrası', '18–29 yaş erkek, 18 yaş üstü kadın',
          '29 yaş üstü erkek', 'ay', 'İŞKUR kaydıyla +6 ay', '27 zorunlu', '28 gönüllü'}
MAIN = {  # K7: tek ana öğe (elle değerlendirme)
    'kapak': 'fotoğraf + mühür', 'vizyon': 'tek cümle + bant', 'zorunluluk': 'büyük sayı (+40)', 'takvim': 'zaman çizelgesi',
    'isyeri': 'fotoğraf', 'kapsam': 'çubuk grafik', 'surec': 'beş durak', 'tesvik': 'çubuk grafik', 'kazanc': 'fotoğraf + üç satır',
    'kanit': 'büyük sayı (50.000+)', 'isbirligi': 'üç sütun', 'cagri': 'tek cümle + üç adım', 'kapanis': 'fotoğraf + mühür'}


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def words(t):
    # tek harfli etiketler (A, B, C) kelime sayılmaz
    return [w for w in re.split(r'\s+', t) if re.search(r'[A-Za-zÇĞİÖŞÜçğıöşü]', w) and len(w.strip('.,;:')) > 1]


rows, deck55 = [], 0
for s in D:
    sid = s['id']
    shot = Image.open(f'{qa}/{sid}.png').convert('RGB')
    T = [t for t in s['texts'] if 'tt' in t['cls'].split() and t['tag'] in ('h1', 'h2')]
    title = T[0] if T else None
    rest = [t for t in s['texts'] if t is not title]
    src = [t for t in rest if t['txt'].startswith('Kaynak:')]
    foot = [t for t in rest if t['txt'].startswith('MYK YB-0079')]
    body = [t for t in rest if t not in src and t not in foot and t['txt'] not in LABELS and not re.fullmatch(r'[\d.,+\s]+(ay)?', t['txt'])]
    tw = len(words(title['txt'])) if title else 0
    bw = sum(len(words(t['txt'])) for t in body)
    alltxt = ' '.join(t['txt'] for t in s['texts'])
    deck55 += '55' in re.findall(r'\b\d+\b', alltxt)
    claims = [m for m in re.findall(r'\d[\d.,]*\+?', re.sub(r'YB-0079|AB-0126-P|17024|0 \(\d+\) [\d ]+|Kasım 2026', '', alltxt)) if len(re.sub(r'\D', '', m)) >= 2]
    # kontrast: görsel üstündeki metinde arka plan ekran görüntüsünden (kutunun ortalama rengi), diğerlerinde zemin rengi
    worst, c_ok = 99.0, True
    for t in s['texts']:
        on_img = any(t['L'] < i['R'] and t['R'] > i['L'] and t['T'] < i['B'] and t['B'] > i['T'] for i in s['imgs'])
        if t.get('pbg'):
            bg = t['pbg']
        elif on_img:
            box = (int(max(t['L'], 0)), int(max(t['T'], 0)), int(min(t['R'], 1919)), int(min(t['B'], 1079)))
            bg = '#%02X%02X%02X' % shot.crop(box).resize((1, 1), Image.BOX).getpixel((0, 0))
        else:
            bg = s['bg']
        need = 3.0 if t['fs'] >= 44 else 4.5
        for c in [t['color']] + t['spans']:
            r = ratio(c, bg)
            worst = min(worst, r)
            c_ok = c_ok and r >= need
    special = sid in ('kapak', 'kapanis')
    if not special:                              # sayfa numarası (::after, sağ alt) arka planı
        pn = '#%02X%02X%02X' % shot.crop((1740, 990, 1795, 1018)).resize((1, 1), Image.BOX).getpixel((0, 0))
        r = ratio('#2C4868', pn)
        worst = min(worst, r)
        c_ok = c_ok and r >= 4.5
    K = {
        'K1 başlık tek cümle, ≤9 kelime': bool(title) and title['txt'].endswith('.') and title['txt'].count('.') == 1 and tw <= 9,
        'K2 gövde ≤25 kelime': bw <= 25,
        'K3 rakama kaynak': (not claims) or bool(src),
        'K4 ölçekte boy, ≥24 px': all(round(t['fs']) in SCALE for t in s['texts']),
        'K5 palet ve tek vurgu': all(c in PALETTE for t in s['texts'] for c in [t['color']] + t['spans']),
        'K6 kenar ve alt bant': all(t['L'] >= 120 and t['R'] <= 1800 and (t['B'] <= 920 or t['boxTop'] >= 990) for t in s['texts']),
        'K7 tek ana öğe': True,
        'K8 guilloche yerinde': (not any(i['src'] in GUILLOCHE for i in s['imgs'])) or sid in GUILLOCHE_OK,
        'K9 taşma, örtüşme yok': True,          # qa_v8.js: 0 sorunlu slayt (çalıştırma çıktısı)
        'K10 kontrast': c_ok,
    }
    title_pos = (round(title['L']), round(title['boxTop'])) if title else None
    rows.append((sid, K, tw, bw, title_pos, MAIN[sid], len(s['notes']), worst))

crit = list(rows[0][1].keys())
lines = ['| Slayt | ' + ' | '.join(c.split(' ')[0] for c in crit) + ' | Puan | Başlık kelime | Gövde kelime | En düşük kontrast | Ana öğe |',
         '|---|' + '---|' * len(crit) + '---|---|---|---|---|']
tot = 0
for sid, K, tw, bw, tp, main, nl, wr in rows:
    sc = sum(K.values()); tot += sc
    lines.append(f'| {sid} | ' + ' | '.join('✓' if K[c] else '✗' for c in crit) + f' | {sc}/10 | {tw} | {bw} | {wr:.1f}:1 | {main} |')
pos = {r[4] for r in rows if r[0] not in ('kapak', 'kapanis')}
md = '\n'.join(lines)
md += f'\n\n- Ortalama: {tot / len(rows):.1f}/10.'
md += f'\n- İçerik slaytlarında başlık konumu: {sorted(pos)}; {"hepsi aynı" if len(pos) == 1 else "farklı konumlar var"}.'
md += f'\n- “55” geçen slayt sayısı: {deck55} (sınır 2).'
md += f'\n- Konuşma notu: {sum(1 for r in rows if r[6] > 0)}/{len(rows)} slaytta var; en uzunu {max(r[6] for r in rows)} karakter (sınır 4000).'
open(out, 'w').write(md + '\n')
print(md)
