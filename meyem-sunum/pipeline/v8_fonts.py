"""v8 yazı ailesi: Archivo (değişken; genişlik 62–125, ağırlık 100–900), latin + latin-ext.
fonts/fonts_v8.css yazar. Yalnızca yerel önizleme ve pişirme içindir; sunum Google Fonts adresini kullanır."""
import os, re, urllib.request, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
FAM = {'archivo': 'Archivo:wdth,wght@62..125,100..900'}
os.makedirs(HERE + '/fonts', exist_ok=True)
out = []
for key, fam in FAM.items():
    css = urllib.request.urlopen(urllib.request.Request(f'https://fonts.googleapis.com/css2?family={fam}&display=swap', headers=UA)).read().decode()
    for blk, sub in re.findall(r'(/\* ([a-z-]+) \*/\s*@font-face \{.*?\})', css, flags=re.S):
        if sub not in ('latin', 'latin-ext'):
            continue
        url = re.search(r'url\((https://[^)]+)\)', blk).group(1)
        fn = f'{key}-{sub}-' + hashlib.md5(url.encode()).hexdigest()[:8] + '.woff2'
        if not os.path.exists(f'{HERE}/fonts/{fn}'):
            open(f'{HERE}/fonts/{fn}', 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read())
        out.append(re.sub(r'/\* [a-z-]+ \*/\s*', '', blk.replace(url, 'fonts/' + fn)))
open(HERE + '/fonts/fonts_v8.css', 'w').write('\n'.join(out) + '\n')
print('fonts_v8.css:', len(out), 'blok')
