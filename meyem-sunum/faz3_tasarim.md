# Faz 3: Tasarım sistemi ve 3 örnek slayt

Tarih: 14 Kasım 2026. Temas sayfası: `faz3/faz3_temas.png`. Sayfada kapak, veri slaydı, fotoğraf slaydı ve sistem kartı var. Kullanıcı onayı bekleniyor.

## Sistem

### Yazı

Tek aile kullanılır: **Archivo** (Google Fonts). Değişken bir ailedir: genişlik 62–125, ağırlık 100–900. Latin-ext içerir ve Türkçe karakterlerin tamamını destekler. Mono ve italik yoktur.

| Rol | Boy | Ağırlık | Genişlik | Not |
|---|---|---|---|---|
| Büyük sayı | 240 px | 800 | %62 | Veri slaydında tek ana sayı |
| Başlık | 88 px | 700 | %78 | Satır aralığı 1,0; `text-wrap: balance` |
| Vurgu, veri etiketi | 48 px | 700 | %80 | |
| Gövde | 32 px | 400 | %100 | Vurgulu hâli 700 |
| Kaynak, etiket | 24 px | 500 | %100 | |

### Renk

Koyu zemin kullanılmaz.

| Belirteç | Değer | Rol |
|---|---|---|
| Lacivert | `#00244D` | Metin ve ana öğe |
| Şarap | `#77183A` | Tek vurgu |
| Açık ton | `#C9D2DD` | İkincil çubuk |
| Kâğıt | `#F8F4EC` | Zemin |
| Gövde | `#2C4868` | Gövde metni ve kaynak |

### Izgara

- 12 sütun; kenar 128 px, oluk 32 px, sütun genişliği 109,3 px.
- **Başlık:** x=128, y=112. Genişliği 10 sütun, en çok 2 satır.
- **İçerik:** y=360'tan başlar.
- **Kaynak satırı:** y=992, sol altta. Sayfa numarası sağ altta.

### Fotoğraf dili

- Fotoğraf düz dikdörtgendir ve sayfa kenarından taşar: kapakta sağ yarıyı kaplar, fotoğraf slaydında sağa ve alta taşar.
- Maske, çerçeve, gölge ve döndürme kullanılmaz.
- Tüm fotoğraflara aynı ton ayarı uygulanır (`v8_common.grade`):
  - doygunluk %90, hafif S eğrisi ve +2 sıcaklık;
  - gölgeler %6 oranında laciverte, açık tonlar %5 oranında kâğıda çekilir.
- Sunumda en fazla dört fotoğraf kullanılır.

### Guilloche

- Yalnızca mühür madalyonunda (kapak, kanıt, kapanış) ve vizyon açılış bandında kullanılır.
- Lacivert ve şarap renkte, iki zıt fazlı dalgalı halka demetinden oluşur. Çizgi kalınlığı 2 px'tir; projeksiyonda kaybolmaz.
- Kapakta mühür, fotoğrafın kenarına basılır; belgedeki fotoğrafa basılan mühür gibi. Bu, “belgelendirilmiş ustalık” fikrinin tek görsel ifadesidir.

### Veri ve hareket

- **Veri:** Her slaytta tek grafik ya da tek büyük sayı kullanılır. Çubuklar düzdür, vurgu yalnızca şarap renktir ve değer çubuğun ucunda yazar. Her rakamın altında kaynak satırı bulunur.
- **Hareket:** Yalnızca yumuşak belirme kullanılır (`rise`, `fadein`).

## Örnek slaytlar

1. **Kapak**
   - Başlık: “Ustalığı üretim durmadan belgeye dönüştürüyoruz.”
   - Sağ yarıda MEYEM saha fotoğrafı yer alır; mühür madalyonu fotoğrafın kenarına basılır.
2. **Kapsam (6)**
   - Dokuz alanın yatay çubuk grafiği, zorunlu paya göre sıralı.
   - Zorunlu pay şarap, gönüllü pay açık tonda.
   - Lejant: 27 zorunlu, 28 gönüllü ve onay sürecindeki 32 yeterlilik. Kaynak satırı var.
3. **Sınav işyerinde (5)**
   - Sabit konumda başlık. MEYEM'in sahada değerlendirme fotoğrafı sağa ve alta taşar.
   - Sol altta değer cümlesi: “Çalışan işinden ayrılmaz, üretim durmaz.”

Üç slayt da QA'dan geçti (`qa_v8.js`). Taşma, kenar ihlali, 24 px altı yazı ve örtüşme yok.

## Görseller

| Varlık | Kaynak | Lisans |
|---|---|---|
| `v8_kapak_foto.jpg` | MEYEM web sitesi ana sayfa görseli (v7 `cover_photo`) | MEYEM |
| `v8_isyeri_foto.jpg` | MEYEM web sitesi “myk-mesleki-yeterlilik” görseli (v7 `onsite_big`) | MEYEM |
| `logo_seal.png` | MEYEM mührü | MEYEM |
| `v8_muhur_halka.png` | `v8_common.seal_ring` ile üretildi | Özgün |

- MEYEM fotoğraflarının çözünürlüğü 1000×1000 ve 900×600. Kadrajlar, ekranda en fazla 1,25 kat büyütme gerekecek şekilde seçildi.
- CC0 adayları Openverse API ile tarandı. Saha temalı, olumlu ve yüksek çözünürlüklü uygun bir aday bulunamadı; MEYEM'in kendi görselleri marka rengini (şarap yelek) de taşıyor.

## Yeniden üretim

```bash
cd meyem-sunum/pipeline
python3 v8_fonts.py                                   # fonts/fonts_v8.css (Archivo)
python3 v8_build.py prep <MEYEM varlık klasörü>       # assets_v8/: ton ayarı, mühür, halka
python3 v8_build.py preview                           # out_v8/project/
NODE_PATH=/opt/node-tools/node_modules node qa_v8.js $PWD/out_v8 $PWD/out_v8/qa
NODE_PATH=/opt/node-tools/node_modules python3 v8_sheet.py $PWD/out_v8/qa $PWD/../faz3/faz3_temas.png
```

**MEYEM varlık klasörü:** v7 sunumundan `Artifact read url=<v7> path=<asset id>` ile indirilir. Gereken dosyalar:
- `e81c0d26764c146f3738e0893b9490a6.png`
- `1a0cb6a8bedfd7ab252f1e1722b55d8d.jpg`
- `432d3f3d2cae2a60ac6250ef5b10d0fb.png`

## Onaydan sonra (Faz 4)

- Yeni bir Slides dosyası açılır; v7'ye dokunulmaz.
- MEYEM varlıkları v7'den `from_url` ve `asset_ids` ile sunucu tarafında kopyalanır. v8 varlıkları yüklenir.
- 13 slayt, `faz2_hikaye.md` metinleri ve bu sistemle üretilir.
