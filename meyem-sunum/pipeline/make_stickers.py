from gx import *
# MYK belge mührü (logo ayrıca üstüne bindirilir)
c = 110
s = f'<circle cx="{c}" cy="{c}" r="104" fill="#FFFFFF"/>'
s += microring(c, c, 90, 'MESLEKİ YETERLİLİK BELGESİ · MYK ·', 11, WINE, 0.95, 'ms1', ls=1.0)
s += circle(c, c, 104, WINE, 2.2, 0.95) + circle(c, c, 70, INK, 1.0, 0.7) + circle(c, c, 108, WINE, 0.8, 0.5)
bake_alpha('sticker_myk', s, 220, 220, dsf=2)
print('ok')

c = 112
s = f'<circle cx="{c}" cy="{c}" r="108" fill="#FFFFFF"/>'
s += microring(c, c, 96, 'YERİNDE EĞİTİM · SINAV · BELGELENDİRME ·', 11, WINE, 0.95, 'ms2', ls=0.8)
s += circle(c, c, 108, WINE, 2.2, 0.95) + circle(c, c, 74, INK, 1.0, 0.7) + circle(c, c, 112, WINE, 0.8, 0.5)
bake_alpha('sticker_yerinde', s, 224, 224, dsf=2)
