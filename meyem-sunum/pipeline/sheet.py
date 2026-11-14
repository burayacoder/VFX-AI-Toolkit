import os
import sys,os,json
from PIL import Image
d=sys.argv[1]; prefix=sys.argv[2]; deckdir=sys.argv[3]
order=json.load(open(deckdir+'/project/deck.json'))['order']
per=int(sys.argv[4]) if len(sys.argv)>4 else 6
cols=2; tw,th=960,540
for k in range(0,len(order),per):
    chunk=order[k:k+per]
    rows=(len(chunk)+cols-1)//cols
    sh=Image.new('RGB',(cols*tw,rows*th),'white')
    for i,sid in enumerate(chunk):
        p=f'{d}/{sid}.png'
        if not os.path.exists(p): continue
        im=Image.open(p).convert('RGB').resize((tw,th),Image.LANCZOS)
        sh.paste(im,((i%cols)*tw,(i//cols)*th))
    sh.save(f'{prefix}_{k//per+1}.png')
    print(f'{prefix}_{k//per+1}.png',chunk)
