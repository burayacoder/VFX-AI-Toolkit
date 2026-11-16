# v7 görsellerinin kaynakları ve lisansları

Varlık kimlikleri `assets.json` dosyasında (dosya adı → `/_blob/<id>`). Tüm stok görseller CC0 lisanslı.

| Varlık | Kaynak | Lisans |
|---|---|---|
| cover_photo | MEYEM web sitesi ana sayfa görseli (home-hero) | MEYEM |
| close_photo | MEYEM web sitesi “meyem-academy” görseli | MEYEM |
| soz_a1 | https://pxhere.com/en/photo/1142060 | CC0 |
| soz_a2 | https://stocksnap.io/photo/work-business-WQ2JMRIIQB | CC0 |
| soz_a3 | https://stocksnap.io/photo/construction-plans-69YZFGFBSY | CC0 |
| tile_insaat | https://pxhere.com/en/photo/1087305 | CC0 |
| tile_metal | Openverse, rawpixel “Welder work” (`welder_5`) | CC0 |
| tile_makine | https://pxhere.com/en/photo/771478 | CC0 |
| tile_enerji | https://pxhere.com/en/photo/1324058 | CC0 |
| tile_tasima | Openverse, rawpixel “forklift operator shuttles pallet loaded” (`forklift_operator_warehouse_0`) | CC0 |
| tile_gida | MEYEM web sitesi görseli (h-000 kırpımı) | MEYEM |
| tile_ticaret | https://pxhere.com/en/photo/449062 | CC0 |
| tile_yonetim | https://pxhere.com/en/photo/868210 | CC0 |
| tile_bilisim | https://stocksnap.io/photo/engineer-fiber-6Z663NNH9K | CC0 |
| step_d1 | MEYEM web sitesi “denetim-hizmetleri” görseli | MEYEM |
| step_d2 | https://pxhere.com/en/photo/596254 | CC0 |
| step_d3 | https://pxhere.com/en/photo/680669 | CC0 |
| step_d4 | https://pxhere.com/en/photo/685238 | CC0 |
| step_d5 | MEYEM mühür logosu | MEYEM |
| model_a | https://pxhere.com/en/photo/1246944 | CC0 |
| model_b | MEYEM web sitesi akademi görseli | MEYEM |
| logo_seal, logo_myk, logo_turkak | MEYEM broşürü ve web sitesi | MEYEM ve kurum logoları |
| cert_myk | MEYEM belge örneği; ad bulanıklaştırıldı | MEYEM |
| onsite_big | MEYEM web sitesi “myk-mesleki-yeterlilik” görseli | MEYEM |
| arch_building | MEYEM broşürü bina fotoğrafı | MEYEM |
| wall | Önceki sunum varlığı (MEYEM görselleri) | MEYEM |
| sticker_myk, sticker_yerinde | `make_stickers.py` ile üretildi | Özgün |
| qr_meyem | `qrcode` ile üretildi | Özgün |
| bk_* | `gx.py` guilloche arka planları, pişirildi | Özgün |

Ek kaynak notları:
- PxHere tam boy dosyası, fotoğraf sayfasındaki indirme bağlantısından alınır.
- StockSnap aramasında sponsorlu Shutterstock sonuçları kullanılmaz.
- Unsplash, Pexels ve Pixabay yalnızca resmi API anahtarıyla kullanılır. Anahtar `request_credential` formuyla istenir.

## v10 fotoğrafları (Kasım 2026)

Sonnet sunumunun (v7) fotoğrafları anlatıyla örtüşen CC0 ya da kamu malı görsellerle yenilendi. Seçim ve kırpım odağı `data/v10_foto_secim.json`, üretim `pipeline/make_photos10.py` dosyasında.

| Varlık | Kaynak | Lisans | Konu |
|---|---|---|---|
| cover_photo | https://www.flickr.com/photos/62518311@N00/428896110 | CC0 (flickr) | Obreros: baret, yelek, eldiven ve gözlüklü ekip |
| close_photo | https://www.flickr.com/photos/49208525@N08/7162907121 | Kamu malı (PDM) (flickr) | U.S. Fish and Wildlife Service: baretli, yelekli, gözlüklü çalışan |
| soz_a1 | https://pxhere.com/en/photo/1324058 | CC0 (PxHere) | work,man,person,people,hand,building |
| soz_a2 | https://www.rawpixel.com/image/5928007/photo-image-public-domain-wood-person | CC0 (rawpixel) | İş eldivenli eller ölçü işaretliyor |
| soz_a3 | https://pxhere.com/en/photo/1575627 | CC0 (PxHere) | architect,architecture,adult,architectural,blank,blue |
| tile_insaat | https://pxhere.com/en/photo/749546 | CC0 (PxHere) | building,asphalt,construction,worker,woman,hammer |
| tile_metal | https://pxhere.com/en/photo/897748 | CC0 (PxHere) | spark,work,man,steel,construction,repair |
| tile_makine | https://www.flickr.com/photos/39955793@N07/46953747894 | Kamu malı (PDM) (flickr) | 190428-N-ZM949-1125 |
| tile_enerji | https://pxhere.com/en/photo/1700564 | CC0 (PxHere) | precise,repairman,contracted,client,detect,air conditioner |
| tile_tasima | https://www.flickr.com/photos/41284017@N08/24221252757 | Kamu malı (PDM) (flickr) | USDA: baretli, yelekli forklift operatörü |
| tile_gida | https://www.flickr.com/photos/41284017@N08/34654902823 | Kamu malı (PDM) (flickr) | USDA: Bland Farms soğan ayıklama hattı (filigransız asıl) |
| tile_ticaret | https://www.flickr.com/photos/62518311@N00/96148841 | CC0 (flickr) | Safeway |
| tile_yonetim | https://pxhere.com/en/photo/559565 | CC0 (PxHere) | working,meeting,computer,person,group,people |
| tile_bilisim | https://pxhere.com/en/photo/1241325 | CC0 (PxHere) | technology,server,machine,product,computers,servers |
| onsite_big | https://www.flickr.com/photos/123443813@N05/41186909981 | Kamu malı (PDM) (flickr) | BSEE Inspects New Appomattox Platform |
| step_d1 | https://pxhere.com/en/photo/1096224 | CC0 (PxHere) | writing,hand,meeting,office,desk,sign |
| step_d2 | https://pxhere.com/en/photo/985713 | CC0 (PxHere) | writing,brand,time,range,line,date |
| step_d3 | https://pxhere.com/en/photo/893399 | CC0 (PxHere) | tool,workshop,construction,repair,equipment,industrial |
| step_d4 | https://pxhere.com/en/photo/917715 | CC0 (PxHere) | writing,hand,finger,student,pen,diary |

- PxHere tam boy dosyası sunucu zaman aşımına düştüğü için önbellekteki 800 px sürüm kullanıldı.
- StockSnap bu ortamdan yapılan isteklere 403 verdi; engel aşılmadı.
- 16.11.2026 revizyonu: koruyucu ekipmanı eksik görünen kapak, kapanış, söz (2. kemer) ve forklift fotoğrafları değiştirildi; gıda karosu rawpixel önizlemesindeki soluk filigran yüzünden USDA Flickr aslından yeniden üretildi.
