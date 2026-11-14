# Faz 5: Kalite kontrolü

Tarih: 14 Kasım 2026.

- **Sunum (v8):** https://claude.ai/artifact/6eGMatyJb7GowuNoftVan5, 13 slayt.
- **v7:** karşılaştırma için olduğu gibi duruyor (https://claude.ai/artifact/558FZyn6ShCbjLaEZBt66r).
- **Temas sayfaları:** `faz5/v8_temas_1.jpg` … `v8_temas_4.jpg`.

## Denetimler

| Denetim | Araç | Sonuç |
|---|---|---|
| Taşma, kenar, 24 px altı yazı, örtüşme | `qa_v8.js` | 13 slaytta 0 sorun |
| Kontrast (44 px altı ≥4,5:1, 44 px ve üstü ≥3:1) | `qa5_v8.py` | Tümü geçti. En düşük değer 7,1:1: fotoğraf slaytındaki sayfa numarası. |
| Başlık konumu | `qa5_v8.py` | İçerik slaytlarının tamamında (128, 112) |
| “55” tekrarı | `qa5_v8.py` | 1 slayt (sınır 2) |
| Konuşma notu | `qa5_v8.py` | 13/13 slaytta var; en uzunu 694 karakter (sınır 4000) |
| Koyu zemin, gündem ve içindekiler slaytı | elle ve tarama | Yok. Zeminler `#F8F4EC` ve `#EDF1F5`. |
| “Gebze TSO”, “Gebze MÜSİAD”, helal | metin taraması | Geçmiyor |

## Puan kartı

Kriterler:
- **K1:** Başlık tek cümledir, en fazla 9 kelimedir ve noktayla biter.
- **K2:** Gövde metni en fazla 25 kelimedir. Grafik etiketleri ve tek harfli etiketler sayılmaz.
- **K3:** Rakam varsa kaynak satırı vardır.
- **K4:** Yazı boyları ölçektedir (24/32/48/88/240).
- **K5:** Yalnızca palet renkleri kullanılır ve vurgu tektir.
- **K6:** Metin kenar boşluklarının içinde kalır; y=920'nin altında yalnız alt satır bulunur.
- **K7:** Slaytta tek ana öğe vardır (elle değerlendirildi).
- **K8:** Guilloche yalnızca kapak, vizyon, kanıt ve kapanışta kullanılır.
- **K9:** Taşma ve örtüşme yoktur.
- **K10:** Kontrast eşikleri karşılanır.

| Slayt | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | Puan | Başlık kelime | Gövde kelime | En düşük kontrast | Ana öğe |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kapak | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 5 | 16 | 8.6:1 | fotoğraf + mühür |
| vizyon | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 7 | 14 | 7.6:1 | tek cümle + bant |
| zorunluluk | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 5 | 6 | 7.8:1 | büyük sayı (+40) |
| takvim | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 6 | 15 | 7.9:1 | zaman çizelgesi |
| isyeri | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 5 | 17 | 7.1:1 | fotoğraf |
| kapsam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 6 | 8 | 7.7:1 | çubuk grafik |
| surec | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 6 | 24 | 8.0:1 | beş durak |
| tesvik | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 7 | 7 | 7.7:1 | çubuk grafik |
| kazanc | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 8 | 16 | 7.7:1 | fotoğraf + üç satır |
| kanit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 9 | 14 | 7.3:1 | büyük sayı (50.000+) |
| isbirligi | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 8 | 24 | 7.5:1 | üç sütun |
| cagri | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 6 | 16 | 7.1:1 | tek cümle + üç adım |
| kapanis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 10/10 | 5 | 14 | 8.6:1 | fotoğraf + mühür |

- Ortalama: 10.0/10.
- İçerik slaytlarında başlık konumu: [(128, 112)]; hepsi aynı.
- “55” geçen slayt sayısı: 1 (sınır 2).
- Konuşma notu: 13/13 slaytta var; en uzunu 694 karakter (sınır 4000).

## Kalite kontrolünde bulunan ve düzeltilenler

1. **Sayfa numarası:** Fotoğraf slaytında açık renkli sayfa numarası açık zemine düşüyordu (1,1:1). Gövde rengine çekildi; kontrast 7,1:1 oldu.
2. **Kapanış başlığı:** Başlık etiketi (`h2`) değildi; düzeltildi.
3. **Kapanış düzeni:** Başlık üç satıra taşıp imza satırıyla çakışıyordu. Düzen yeniden kuruldu: adres alt satıra indi, QR kodu y=920'nin üstüne alındı.
4. **Büyük sayılar:** “+40” ve “50.000+” ile etiketleri arasındaki boşluk artırıldı (örtüşme uyarısı).
5. **Satır sonları:** “on yılı” ve “iş birliği” ifadeleri satır sonunda bölünmeyecek şekilde düzenlendi.

## Bilinen sınırlar

- **Fotoğraf çözünürlüğü:** MEYEM fotoğrafları 900×600 ve 1000×1000 piksel. Kadrajlar en fazla 1,25 kat büyütmeyle seçildi, ama 4K ekranda hafif yumuşak görünebilirler. MEYEM'den yüksek çözünürlüklü saha fotoğrafları gelirse aynı kadrajlara konur (`v8_build.py prep`).
- **“10+ yıl” ve “50.000+ aday”:** Bu iki rakam v7'ye MEYEM tanıtım materyalinden girdi. Doğrulamaları MEYEM'e aittir.
- **Yazı tipi:** PowerPoint dışa aktarımında Archivo ve Archivo Narrow yüklü değilse yedek yüzler (Arial Narrow, Arial) kullanılır.
- **Önizleme:** Görsel kontrol yerel Chromium'da, Slides görüntüleyicisinin CSS'iyle yapıldı. Slides uygulamasındaki görüntü aynı dosyaları okuyor, ancak uygulama içinde ayrıca doğrulanmadı.

## Yeniden çalıştırma

```bash
cd meyem-sunum/pipeline
python3 v8_build.py preview
NODE_PATH=/opt/node-tools/node_modules node qa_v8.js $PWD/out_v8 $PWD/out_v8/qa
NODE_PATH=/opt/node-tools/node_modules node qa5_v8.js $PWD/out_v8/qa
python3 qa5_v8.py $PWD/out_v8/qa ../faz5_puan_karti.md
```
