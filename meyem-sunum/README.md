# MEYEM Vizyon Sunumu: devir dosyası

Bu klasör, MEYEM vizyon sunumu çalışmasını yeni bir Claude Code oturumunda baştan araştırma yapmadan sürdürmek için gereken her şeyi tutar. Son güncelleme: 14 Kasım 2026.

## 1. Durum

- **Canlı sunum:** https://claude.ai/artifact/558FZyn6ShCbjLaEZBt66r. Slides türünde, sürüm 7, 14 slayt.
- **v10 yayında (16.11.2026):** https://claude.ai/artifact/DTp39tdv3DsdPMXSHWUqeS. v7 üzerine: 13. slayt (iş birliği modeli) yerine vizyon, tüm fotoğraflar CC0/kamu malı kaynaklardan yenilendi. Kaynak kopyası `deck_v10/`, varlık eşlemesi `data/assets_v10.json`. 16.11.2026 revizyonu: yetki kapsamı rozeti 55 + 32 yaprak (açıktan koyuya, onay sürecindeki 32 en koyu), zorunlu/gönüllü sayıları ayrı sütunda; koruyucu ekipmanlı fotoğraflar. Zorunluluk, Resmî Gazete 2026/1 eki ve 2015–2021 tebliğ listesiyle doğrulandı: 27 zorunlu, bilişim dahil 28 gönüllü. 32 yeterliliğin adları liste gelince eklenecek.
  - Kaynak kopyası `deck_v7/` klasöründe. Slayt metinlerini okumak için Artifact okumaya gerek yok.
  - Sıra: kapak, imza, soz, belge, takvim, alan, yaprak, yerinde, durak, tesvik, referans, halka, yol, kapanis.
- **Kullanıcının 4. tur geri bildirimleri** v7'de karşılandı. Sıradaki iş v3 yeniden tasarımı (bölüm 5). Kullanıcının 5 soruya yanıtları bölüm 6'da.
- **Faz 1 tamamlandı (14.11.2026):** `faz1_referanslar.md`: 28 referanslık 2026 panosu ve 10 tasarım ilkesi.
- **Faz 2 tamamlandı (14.11.2026):** `faz2_hikaye.md`: hedef kitle, ana mesaj ve 13 slaytlık akış. Her slayt için A/B başlık, slayt metni, kaynak satırı ve konuşma notu var.
- **v9 örnekleri onay bekliyor (14.11.2026):** https://claude.ai/artifact/NMdLq7trYCPeZTXdUtyLhi. Üç slayt: kapak, takvim ve kapsam.
  - **Neden v9:** Kullanıcı, v8'i Sonnet'le yapılan v7'den daha vasat buldu. v9, v8'in hikâyesini korur ve v7'nin güvenlik baskısı dilini veriyle yeniden kurar.
  - **Görsel dil:** Kapak bir belge yüzü gibidir: çerçeve, 55 halkalı veri rozeti ve fotoğraf penceresine basılmış mühür. Takvimde şerit, son tarihe yaklaştıkça sıklaşır ve geçiş süresinin bittiği gün bir damgayla işaretlenir. Kapsam slaydında her yeterlilik bir pul olarak gösterilir.
  - **Yazı:** Instrument Serif ve Hanken Grotesk.
  - **Dosyalar:** kaynak `deck_v9/`, `pipeline/v9_*.py`, varlık eşlemesi `data/assets_v9.json`.
  - **Onaydan sonra:** kalan 10 slayt aynı dille üretilir.
- **v8 yayında (14.11.2026):** https://claude.ai/artifact/6eGMatyJb7GowuNoftVan5. Slides türünde, 13 slayt. Kaynak kopyası `deck_v8/`, varlık eşlemesi `data/assets_v8.json`. v7 karşılaştırma için olduğu gibi duruyor.
- **Faz 3 (14.11.2026):** `faz3_tasarim.md` ve `faz3/faz3_temas.png`. Tek aile (Archivo), 5 boy, 12 sütun. Örnek slaytlar: kapak, kapsam ve sınav işyerinde. v8 boru hattı `pipeline/v8_*.py` ve `qa_v8.js`. Kullanıcı örnekleri görmeden tamamına geçilmesini istedi.
- **Faz 5 tamamlandı (14.11.2026):** `faz5_kalite.md`. Denetimlerde 0 sorun kaldı, puan kartı ortalaması 10/10. Temas sayfaları `faz5/` klasöründe. Sıradaki iş kullanıcının geri bildirimi.
- **Faz 4 tamamlandı (14.11.2026):** 13 slayt üretildi ve yayınlandı. Başlık ve sayılarda Archivo Narrow, gövdede Archivo kullanıldı; Slides `font-stretch` desteklemediği için dar kesim ayrı ailedir.
- **Eski sunumlar:** aynı hesapta 8 sunum daha var (4 tasarım × Gebze analizi + Türkiye vizyonu). Bunlara dokunulmaz.
- **Hedef kitle** Faz 2'de netleşecek. v7 işverene konuşuyor: belge zorunluluğu, yerinde sınav ve teşvik.

## 2. Kullanıcının değişmez kuralları

- Koyu sayfa yok. İçindekiler veya anlatım sırası slaytı yok.
- Slayta ve konuşma notuna kullanıcıya yönelik uyarı ya da çekince yazılmaz (örnek: “tam doğrulama olmadan sınav açılamaz”).
- Kapsam yalnızca MEYEM MYK belgelendirmesi. Helal belgelendirme sunumda yer almaz.
- “Gebze TSO” ve “Gebze MÜSİAD” adları geçmez.
- Görseller olumlu ve doğal olmalı. Kapak ve kapanışta negatif, karanlık ya da gravür efektli görsel olmaz.
- Guilloche çizgileri beğenildi ve korunur, ama süs olarak değil anlam taşıdığı yerlerde kullanılır.
- Takvim slaytındaki kronolojik zaman çizelgesi beğenildi.
- Görsel lisansı:
  - Yalnızca CC0 ya da kamu malı kaynaklar: StockSnap (sponsorlu Shutterstock sonuçları hariç), PxHere, Openverse/rawpixel CC0.
  - Bunlara ek olarak MEYEM'in kendi materyali kullanılabilir.
  - Pinterest ve Behance yalnızca referans içindir; oradaki görseller sunuma girmez.
- Bot korumasını aşmak yasak; bu daha önce sınıflandırıcı tarafından reddedildi. Unsplash, Pexels ve Pixabay Cloudflare arkasında.
- Kullanıcı hesaplarına giriş yapılmaz. API anahtarı yalnızca `request_credential` formuyla istenir, sohbete yazdırılmaz.
- Kullanıcının e-postası ve kişisel bilgileri dış servislere gönderilmez.
- Commit ve push yalnızca kullanıcı isteyince yapılır. Dal: `claude/marmara-mevzuat-sertifikasyon-bi6rnp`.

## 3. İçerik gerçekleri

Bunlar v7'de kullanıldı ve doğrulandı. Kaynak satırı için “MYK Portal, Kasım 2026” kullanılabilir.

- **MEYEM:**
  - Mersin merkezli, MYK yetkili personel belgelendirme kuruluşu.
  - Yetki no YB-0079, TÜRKAK akreditasyonu AB-0126-P, standart TS EN ISO/IEC 17024.
- **Kapsam:** 55 ulusal yeterlilik.
  - 27'si zorunlu belge kapsamında, 28'i gönüllü.
  - Kayıtlar `data/meyem_scope.json` dosyasında. Alanlar: `c` kod, `rev`, `n` ad, `units`, `date` yetki tarihi, `st` durum, `z` zorunlu.
- **Takvim:**
  - 23.03.2026: 2026/1 sayılı Tebliğ yayımlandı (Resmî Gazete 33202). 40 meslek zorunlu listeye eklendi.
  - 13.07.2026: 19 yeterlilikte yetki MYK Portal'da aktif oldu ve kapsam 55'e çıktı. Buhar Kazanı (S4) ve Sıcak Su Kazanı (S3) operatörlüğü bunların içinde.
  - 31.12.2026: 6111 teşvikinde belgeli işçi alımı için son tanımlama günü. İmalatta 5 puanlık prim indirimi de bu tarihe kadar geçerli.
  - 23.03.2027: Geçiş süresi bitiyor. 2026/1 kapsamındaki 40 meslekte belge zorunlu oluyor.
- **Onay sürecinde:** MYK'da 32 yeterlilik daha bekliyor, 16'sı zorunlu kapsamda.
  - 32 yeterliliğin adları açık kaynakta yok. 16.11.2026'da şu kaynaklar tarandı ve listeye ulaşılamadı:
    - MYK Portal kapsam ve tarife sayfaları: yalnızca 55 aktif yeterlilik var.
    - meyem.com.tr: bot doğrulama sayfası açılıyor; aşılmadı.
    - TÜRKAK kapsam portalı (secure.turkak.org.tr) ve Wayback Machine: bu ortamdan erişilemedi.
    - Önceki Claude oturumları, MEYEM artifact'ları, Drive ve Gmail: yalnızca sayı geçiyor.
  - Liste kullanıcıdan gelecek. Gelince `data/meyem_pending.json` dosyasına yazılır.
- **9 alan:** 55 yeterlilik 9 gruba ayrıldı. Gruplama kuralları `pipeline/d_slides4.py` içindeki `RULES` listesinde.

  | Alan | Toplam | Zorunlu |
  |---|---|---|
  | İnşaat ve yapı | 13 | 13 |
  | Metal ve kaynak | 3 | 3 |
  | Makine ve üretim | 5 | 5 |
  | Enerji ve tesisat | 5 | 4 |
  | Taşıma ve kaldırma | 4 | 2 |
  | Gıda ve paketleme | 1 | 0 |
  | Ticaret ve emlak | 6 | 0 |
  | Yönetim ve İK | 4 | 0 |
  | Bilişim ve siber | 14 | 0 |

- **Buhar kazanı vurgusu neden vardı:**
  - Rakip az: Marmara'da buhar kazanında 1, sıcak su kazanında 2 kuruluş var; Türkiye genelinde 3 ve 4.
  - Belge 23.03.2027'den itibaren zorunlu.
  - Strateji “kapı açıcı” yetkiyle girip çapraz satış yapmaktı. Rakip ayrıntısı `data/` dışında, önceki oturumda kaldı.
  - Ulusal vizyon sunumunda bu özel vurgu kaldırıldı.
- **“Yetki MEYEM'de kalır” ne demek:** MYK yetkisi devredilemez. İş birliği modeli ne olursa olsun sınavı yapan ve belgeyi veren MEYEM'dir. v7'de cümle buna göre yeniden yazıldı.

## 4. v7 öz eleştirisi (not: 6/10)

1. **Hikâye yok, katalog var.** Vizyon 12. slayta kalıyor. Sunum vizyonla açılmalı, “neden şimdi” rakamla kurulmalı, net bir talep ile bitmeli.
2. **Başlıklar formüle dönmüş.** 14 başlığın hepsi “A, B.” kalıbında ve ikinci yarısı italik. Çoğu mesaj taşımıyor.
3. **Tipografi kalabalık.** 4 yazı ailesi var: Bricolage Grotesque, Hanken Grotesk, Instrument Serif ve JetBrains Mono.
   - Bricolage oyunbaz kaçıyor, mono etiketler girişim havası veriyor.
   - Başlık boyu 80 ile 200 px arasında oynuyor.
4. **Görsel dili dağınık.** Beş ayrı çerçeve dili var: pul, kemer, madalyon, kare ve döndürülmüş kart. El sıkışma ve kıvılcımlı kaynakçı klişe.
5. **Guilloche süse dönmüş.** Köşe rozetleri ve şeritler gürültü yapıyor, ince çizgiler projeksiyonda kayboluyor.
6. **Veri grafikleri dekoratif.** 55 yapraklı rozet hızlı okunmuyor. Teşvik halkasını basit bir çubuk grafik daha iyi anlatır. “55” dört slaytta tekrar ediyor.
7. **Slaytta fazla metin var.** 24–26 px'lik çok sütunlu metinlerin yeri konuşma notu.
8. **Ritim ve ızgara zayıf.** Her slayt aynı iskelette. Tam sayfa fotoğraf, tek cümle ya da büyük sayı slaytı yok.
9. **Rakamlarda kaynak satırı yok.**
10. **Düzenlemesi zor.** Tüm öğeler sabit konumlu.

## 5. v3 çalışma planı

Kullanıcı bu planı gördü. Yeni oturum, kullanıcının yanıtlarıyla Faz 1'den başlar.

**Faz 1: 2026 kıyas araştırması**
- Bakılacak kaynaklar:
  - Behance'te 2026'da yayımlanmış en çok takdir almış sunum, pitch, kurumsal kimlik ve yıllık rapor projeleri.
  - Dribbble ve Pinterest'teki 2026 trendleri.
  - 2026 ödül sonuçları: Red Dot, German Design Award, European Design Awards, ADC Europe, D&AD.
  - Avrupa şirketlerinin 2026 strateji sunumları.
- Çıktı `faz1_referanslar.md` dosyasına yazılır:
  - 25–30 referanslık pano: bağlantı, yıl, beğeni sayısı ve neyi iyi yaptığı.
  - Bu panodan çıkan 8–10 tasarım ilkesi.

**Faz 2: Hikâye ve metin**
- Hedef kitle ve tek cümlelik ana mesaj netleşir.
- Akış: vizyon → neden şimdi → ne yapıyoruz → kapsam → nasıl → işverene değeri → kanıt → iş birliği → çağrı. Toplam 12–14 slayt.
- Başlıklar tek gramerde ve mesaj taşır; her slayt için 2 alternatif yazılır.
- Fazla metin konuşma notuna taşınır, her rakama kaynak satırı eklenir.
- Çıktı: `faz2_hikaye.md`.

**Faz 3: Tasarım sistemi ve 3 örnek slayt (onay noktası)**
- En fazla 2 yazı ailesi, 5 boyutluk ölçek, sabit başlık yüksekliği, 12 sütunlu ızgara.
- Tek fotoğraf dili: az görsel, büyük kadraj, tek renk ayarı.
- Guilloche yalnızca kapakta, bölüm açılışlarında, mühürde ve kapanışta.
- Veride büyük sayı ve çubuk grafik kullanılır.
- Kapak, bir veri slaytı ve bir fotoğraf slaytı tek temas sayfasında gösterilir. Kullanıcı onaylamadan devam edilmez.

**Faz 4: Üretim.** Tüm slaytlar, görseller ve konuşma metni hazırlanır.

**Faz 5: Kalite kontrolü**
- Taşma, kontrast ve hizalama denetlenir.
- Her slayt 10 kriterli bir puan kartıyla değerlendirilir.
- Sonuç yeni bağlantıyla teslim edilir; v7 karşılaştırma için kalır.

## 6. Kullanıcının yanıtları (14.11.2026)

1. Ağ erişimi sınırsız kalır.
2. Stok fotoğraf API anahtarı yok; CC0 kaynaklarla devam edilir.
3. Chrome bağlanmaz. Behance ve Pinterest oturum açmadan gezilir.
   - Behance bu ortamdan yapılan otomatik isteklere 403 veriyor; engel aşılmaz.
4. MEYEM'den girdi henüz yok (vizyon cümlesi, hedef rakamları, fotoğraflar, logo izni, kimlik kılavuzu). Sunum mevcut gerçeklerle kurulur; sunuma yer tutucu ya da uyarı konmaz.
5. Yeni sunum dosyası açılır; v7 karşılaştırma için kalır.
6. Her faz sonunda commit ve bu dala push izni var. Faz 1 ve Faz 2 sonunda en fazla 10 satırlık özet verilir. Faz 3'te 3 örnek slayt tek temas sayfasında gösterilir ve onay beklenir.

## 7. v7 tasarım sistemi (referans için)

- **Renkler:**
  - INK `#00244D`, INK2 `#2C4868`
  - WINE `#77183A`, WINE_D `#580721`, WINE_L `#832D4C`
  - ROSE `#AA6E84`, BLUSH `#DAC1CA`, BLUE `#3E5E86`
  - Kâğıt tonları: A `#F8F4EC`, B `#F4E8EB`, C `#E9EFF6`, D `#FBFAF6`
- **Yazı aileleri:** Faz 3'te en fazla 2 aileye inilecek. Tümü latin-ext içerir ve Türkçe karakterleri destekler.
- **Guilloche kütüphanesi `pipeline/gx.py`:**
  - Hipotrokoid rozet, dantel rozet, dalgalı halka demeti, örgülü sinüs bandı.
  - `textPath` ile mikro yazı halkası.
  - Yaprak rozet veri görseli, yay göstergesi, iris gradyanı.
  - Arka planlar 1920×1080 tasarlanır, DSF 2'de 3840×2160 JPG (q90) olarak pişirilir.
- **Fotoğraf işlemleri `pipeline/photos.py`:** kırpma, kemer ve daire maskesi, madalyon, pul, gölge, ton ayarı.

## 8. Slides artifact kuralları

- **Yapı:**
  - `project/deck.json`: v5, `lists: css`, `format.shared: ["project/deck.css"]`, `faces` (Google Fonts adresleri), `sections`, `order`.
  - `project/deck.css`.
  - Her slayt `project/slides/<id>.html` dosyasında. Dosyada tek bir `<section>` olur ve son çocuğu konuşma notu `<aside>`dır.
- **Görseller:** asset olarak yüklenir ve `/_blob/<id>` ile çağrılır. `data:` URI kullanılmaz. Kimlikler `data/assets.json` dosyasında.
- **Sınırlar:**
  - Slayt başına en fazla 200 öğe; bir div içinde en fazla 24 sabitlenmiş çocuk.
  - Yazı boyu en az 24 px. `z-index` yok.
  - Durağan dönmede `transform-origin` düşer.
  - Satır içi biçimde yalnızca renk, kalın, italik ve altı çizili kullanılır; satır içinde yazı ailesi değişmez.
  - Kutular 128 px kenar boşluğunun içinde kalır. Altbilgi `bottom:64px`.
- **Yayın (v7'de kullanılan biçim):**
  - `Artifact publish` çağrısı:
    - `url` = sunum
    - `root` = `<pipeline>/out`
    - `file_path` = `<pipeline>/out/project/deck.json`
    - `files` = `{"project/slides/kapak.html": "project/slides/kapak.html", …, "project/deck.css": "project/deck.css"}`
  - Bir yolu `null` ile eşlemek o dosyayı siler.
  - Var olan sunumu güncellemeden önce `Artifact list scope:files url=…` çalıştırılır. Bu ucuzdur; yapılmazsa yayın reddedilir.
- **Varlık yükleme:**
  - `asset:true` ve `file_paths` ile, çağrı başına en fazla 25 dosya.
  - Sonra `list scope:assets` ile SHA-256 kontrolü yapılır.
- **Yeni dosya açılırsa:** eski varlıklar `from_url` ve `asset_ids` ile sunucu tarafında kopyalanır (çağrı başına en fazla 10). Yeniden indirip yüklemeye gerek yok.

## 9. Boru hattı (pipeline)

```bash
cd meyem-sunum/pipeline
pip install -r ../requirements.txt         # pillow, numpy, qrcode
python3 fetch_fonts.py                     # fonts/fonts.css: pişirme ve QA için
python3 d_build.py publish                 # out/project/ üretir, /_blob/ bağlantılarıyla (v7 ile birebir aynı çıktı doğrulandı)
python3 d_build.py preview [id,...]        # arka planları art/ içine pişirir; yerel önizleme için assets/ klasörü gerekir
NODE_PATH=/opt/node-tools/node_modules node qa2.js $PWD/out $PWD/out/qa [id,...]   # taşma, kenar, <24px, çakışma + ekran görüntüsü
python3 sheet.py out/qa out/qa/sheet out 8 # temas sayfası
```

**Dosyalar:**
- **Guilloche ve fotoğraf işleme:** `gx.py` guilloche ve SVG pişirme, `photos.py` fotoğraf işlemleri.
- **Slayt kurma:**
  - `d_common.py`: CSS ve yardımcılar (`P`, `IMG`, `TITLE`, `FOOT`, `SEC`), ayrıca `url_for`.
  - `d_slides1-3.py`: v1 slaytları. `belge`, `yerinde`, `tesvik` ve `referans` hâlâ bunlardan geliyor.
  - `d_slides4.py`: v2 slaytlarının üzerine yazılanlar ve `ORDER_V2`.
  - `d_build.py`: derleme.
- **Varlık üretimi:** `make_photos.py`, `make_photos2.py`, `make_stickers.py`.
  - Girdileri depoda yok (indirilen fotoğraflar, site görselleri, broşür kırpımları). v7 varlıkları zaten yüklü.
  - Yeniden üretmek gerekirse kaynaklar `data/gorsel_kaynaklari.md` dosyasında.
  - Varsayılan klasörler: `pipeline/web/full/px_<id>.jpg`, `pipeline/web/full/ss_<id>.jpg`, `pipeline/web/rp/<ad>.jpg`, `pipeline/site/home/home-<ad>.jpg`, `kaynak/mdeck/assets/...`
- **Kontrol:** `qa2.js`, `shoot2.js` (Playwright ile ekran görüntüsü), `sheet.py`.
- **Tarama:** `browse.js <url> <çıktı> [kaydırma] [bekleme]`, `px.js "<sorgu>" <json>` (PxHere), `ss.js "<sorgu>" <json>` (StockSnap, yalnızca kendi CDN'i).
- **Yollar:**
  - Kod çalışma klasörünü kendi konumundan bulur.
  - `MEYEM_WORK` ve `MEYEM_SRC` ortam değişkenleri bu klasörleri değiştirir.
  - Çıktı klasörleri `.gitignore` içinde.

**Yerel önizleme için varlık:** gereken görsel `Artifact read url=<sunum> path=<asset id>` ile indirilip `pipeline/assets/<dosya adı>` olarak konur. Dosya adı ve asset id eşleşmesi `data/assets.json` içinde.

## 10. Ortam

- **Bulut ortamı:** “MYK araştırma”, ağ sınırsız.
- **Playwright ve Chromium:** hazır kurulu. `playwright install` çalıştırılmaz.
- **Kullanıcının bilgisayarı ve Chrome'u:** bu bulut oturumundan erişilemez. Claude in Chrome araçları yok ve paylaşılmış klasör yok.
- **Geçici klasör (scratchpad):** yeni oturuma taşınmaz. Kalıcı olması gereken her şey bu klasöre yazılıp commit edilir.
- **Depo erişimi:** oturum depo seçilmeden açılırsa klon salt okunur olur ve push 403 alır. Yeni oturum `burayacoder/VFX-AI-Toolkit` seçili açılmalı.

## 11. Token disiplini

- Bu dosyadaki bilgi ve kararlar geçerli. Geçmiş yeniden araştırılmaz, öz eleştiri yeniden yazılmaz.
- Görsel kontrol temas sayfasıyla ve DSF 1'de yapılır; aynı slayt tekrar tekrar açılmaz.
- Büyük dosyalar bütün okunmaz, `grep` ile ilgili bölüm alınır.
- Her faz sonunda çıktı bu klasöre yazılır, commit edilir ve push edilir. Kullanıcı istediği an yeni bir oturumda kaldığı yerden devam edebilir.
- Kullanıcıya ara adımlar anlatılmaz; yalnızca sonuç, karar ve soru yazılır.
