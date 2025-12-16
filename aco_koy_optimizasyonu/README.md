# Isparta Kırsal Aşı Rota Optimizasyonu (ACO)

Bu projede, Isparta ili kırsalında bulunan 15 köyde çocuklara aşı
yapmakla görevli bir Sağlık Bakanlığı ekibinin izlemesi gereken
en kısa rota belirlenmiştir.

Problem, Gezgin Satıcı Problemi (Traveling Salesman Problem - TSP)
olarak modellenmiş ve Ant Colony Optimization (ACO) algoritması
kullanılarak çözülmüştür.

---

## Problem Tanımı

Sağlık Bakanlığı ekibi, Isparta İl Merkezi'nden çıkmakta, belirlenen
15 köyü yalnızca bir kez ziyaret etmekte ve tekrar merkeze dönmektedir.
Amaç, toplam yol mesafesini minimize etmektir.

Bu problem, kombinatoryal optimizasyon problemlerinden biri olan
Gezgin Satıcı Problemi (TSP) kapsamında ele alınmıştır.

---

## Kullanılan Yöntemler

- Google Maps Geocoding API ile köy koordinatlarının elde edilmesi
- Haversine formülü ile köyler arası mesafe matrisi oluşturulması
- Ant Colony Optimization (ACO) algoritması ile en kısa turun bulunması
- Yakınsama (convergence) analizi
- Harita ve grafiklerle görselleştirme

---

## Kullanılan Kütüphaneler

Aşağıda projede kullanılan Python kütüphaneleri ve amaçları verilmiştir:

- **numpy**  
  Sayısal hesaplamalar ve mesafe matrisi işlemleri

- **pandas**  
  Mesafe matrisinin tablo halinde gösterimi

- **matplotlib**  
  Yakınsama (convergence) grafikleri ve analiz görselleştirmeleri

- **googlemaps**  
  Google Maps Geocoding API üzerinden adres → koordinat dönüşümü

- **folium**  
  Rota ve konumların harita üzerinde görselleştirilmesi

- **math**  
  Haversine formülü için trigonometrik hesaplamalar

- **os**  
  Ortam değişkenlerinden (API KEY) güvenli veri okuma

- **typing**  
  Kod okunabilirliği için tip tanımlamaları

---

## Proje Yapısı

```text
aco_koy_optimizasyonu/
│
├── .streamlit/
│   └── secrets.toml        # Streamlit için  anahtar (API key)
│
├── core/
│   ├── ant_algorithm.py    # Ant Colony Optimization (ACO) algoritması
│   ├── haversine.py        # Haversine formülü ile iki koordinasyon arası mesafe hesabı
│   ├── matrix_utils.py    # Mesafe matrisi oluşturma yardımcı fonksiyonları
│   └── __pycache__/        # Python önbellek dosyaları
│
├── data/
│   ├── coordinates.py     # Kampüs duraklarının koordinat bilgileri
│   └── __pycache__/        # Python önbellek dosyaları
│
├── figures/
│   ├── convergence.png    # ACO algoritmasının iterasyon yakınsama grafiği
│   └── rota.html          # Hesaplanan en iyi güzergâhın harita çıktısı
│
├── visual/
│   ├── plotting.py        # Grafik ve görselleştirme işlemleri
│   └── __pycache__/       # Python önbellek dosyaları
│
├── .env                   # Ortam değişkenleri (API anahtarları vb.)
├── config.py              # Genel proje ayarları ve sabitler
├── main.py                # Uygulamanın ana çalıştırma dosyası
├── requirements.txt       # Projede kullanılan Python kütüphaneleri
└── README.md              # Proje açıklamaları ve dokümantasyon
