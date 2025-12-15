# Isparta Köyler Arası Aşı Rota Optimizasyonu (ACO)

Bu projede, Isparta ili kırsalında bulunan 15 köyde çocuklara aşı
yapmakla görevli bir Sağlık Bakanlığı ekibinin izlemesi gereken
en kısa rota belirlenmiştir.

Problem, Gezgin Satıcı Problemi (TSP) olarak modellenmiş ve
Ant Colony Optimization (ACO) algoritması kullanılarak çözülmüştür.

## Problem Tanımı
Ekip, Isparta İl Merkezi'nden çıkıp tüm köyleri yalnızca bir kez
ziyaret ettikten sonra tekrar merkeze dönmek zorundadır.
Amaç, toplam yol mesafesini minimize etmektir.

## Kullanılan Yöntemler
- Google Maps Geocoding API
- Haversine Mesafe Hesabı
- Ant Colony Optimization (ACO)
- Yakınsama Analizi
- Harita Üzerinde Rota Görselleştirme

## Proje İçeriği
- Gerçek coğrafi veriler Google Maps API ile alınmıştır
- Köyler arası mesafeler Haversine formülü ile hesaplanmıştır
- En kısa kapalı tur ACO algoritması ile elde edilmiştir
- Yakınsama grafikleri ve iyileştirme oranları analiz edilmiştir

## Kurulum ve Çalıştırma
1. Google Maps API key alın
2. `.env` veya `.streamlit/secrets.toml` dosyasına API key ekleyin
3. Notebook dosyasını açıp hücreleri sırayla çalıştırın

## Güvenlik
API anahtarları güvenlik nedeniyle GitHub reposuna eklenmemiştir.

## Not
Bu proje akademik amaçla hazırlanmıştır.
