# Yeni oturumda devam etme (Opus 5.5)

## Adımlar

1. Claude uygulamasında ya da claude.ai/code adresinde yeni bir oturum aç.
2. Depo olarak `burayacoder/VFX-AI-Toolkit`, ortam olarak **MYK araştırma** seç. Dal seçimi çıkarsa `claude/marmara-mevzuat-sertifikasyon-bi6rnp` seç. Çıkmazsa sorun değil, mesajdaki ilk komut dalı getirir.
3. Model seçiciden **Opus 5.5** seç. Terminalde çalışıyorsan `/model claude-opus-5-5` yaz.
4. Aşağıdaki mesajı yapıştır. Gerekirse 2. ve 4. yanıtı değiştir, sonra gönder.

## Yapıştırılacak mesaj

```
MEYEM vizyon sunumuna kaldığımız yerden devam ediyoruz.

Hazırlık:
1. Çalıştır: git fetch origin claude/marmara-mevzuat-sertifikasyon-bi6rnp && git merge --ff-only FETCH_HEAD
2. CLAUDE.md ve meyem-sunum/README.md dosyalarını oku. Oradaki bilgi, kural ve kararlar geçerli. Geçmişi yeniden araştırma.

Bekleyen sorulara yanıtlarım:
1. Ağ erişimi: sınırsız kalsın.
2. Stok fotoğraf API anahtarı: Hayır, CC0 kaynaklarla devam et.
3. Chrome: Hayır. Behance ve Pinterest'i oturum açmadan gez.
4. MEYEM girdileri: Henüz yok. Mevcut gerçeklerle kur; sunuma yer tutucu ya da uyarı koyma.
5. Dosya: Yeni sunum dosyası aç. v7 karşılaştırma için kalsın.

Çalışma şekli:
- Faz 1'den başla. Faz 1 ve Faz 2 sonunda bana en fazla 10 satırlık özet ver.
- Faz 3'te 3 örnek slaytı tek bir temas sayfasında göster ve onayımı bekle.
- Her faz sonunda çıktıları commit et ve claude/marmara-mevzuat-sertifikasyon-bi6rnp dalına push et. Buna izin veriyorum.
- Ara adımları anlatma. Yalnızca sonuç, karar ve soru yaz.
```

API anahtarı vereceksen 2. yanıtı şöyle yaz: `Evet, Unsplash anahtarı vereceğim; güvenli formu aç.`

## Sonraki fazlarda yeni oturum

Her şey depoda durduğu için her fazdan sonra yeni bir oturum açabilirsin. Aynı mesajı yapıştır, yalnızca “Faz 1'den başla” satırını “Faz 3'ten devam et” gibi değiştir.

## Yeni oturuma taşınanlar ve taşınmayanlar

- **Taşınan:** Bu depo, sunum bağlantısı ve sunuma yüklenmiş tüm görseller.
- **Taşınmayan:** Önceki oturumun geçici klasörü. İndirilmiş fotoğraflar, pişirilmiş arka planlar ve yüklediğin dosyalar (broşür PDF'i, fotoğraflar) burada kaldı. Gerekirse yeni oturumda yeniden yükle.
