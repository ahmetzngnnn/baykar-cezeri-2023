# ASHİNA — Otonom Uçan Araç Sistemi

**BAYKAR Teknoloji — CEZERİ 2023 Yarışması** kapsamında geliştirilen otonom hava aracı yazılım projesi.

Hedef: GPS/GNSS destekli otonom navigasyon, güvenli iniş ve acil müdahale senaryolarında görev sürdürme yeteneği.

---

## İçindekiler

```
ASHİNA_UÇAN_ARABA/
├── Yazılım/            ← Python tabanlı otonom uçuş yazılımı
├── RAPORLAR/           ← Sistem dokümanları, tablolar, akademik makaleler
└── Adsız tasarım/      ← UI/UX arayüz mockup'ları ve logo
```

---

## Sistem Mimarisi

```
┌─────────────────────────────────────────────────────────┐
│                  OTONOM UÇUŞ SİSTEMİ                     │
│                                                          │
│  ┌────────────────┐    ┌──────────────────────────────┐  │
│  │ Sensör Katmanı │    │     İşleme Katmanı           │  │
│  │                │    │  (Python + ROS + cezeri_lib) │  │
│  │  GPS / INS     ├───►│                              │  │
│  │  IMU           │    │  ┌──────────┐ ┌───────────┐  │  │
│  │  Lidar / Radar │    │  │ NAV      │ │ GNSS      │  │  │
│  │  Barometer     │    │  │ Modülü   │ │ Güvenlik  │  │  │
│  └────────────────┘    │  └────┬─────┘ └─────┬─────┘  │  │
│                        │       │              │         │  │
│                        │  ┌────▼──────────────▼─────┐  │  │
│                        │  │    Karar Motoru          │  │  │
│                        │  │  PID + Nöral Ağ          │  │  │
│                        │  └────────────┬─────────────┘  │  │
│                        └───────────────┼─────────────┘  │
│                                        │                 │
│  ┌─────────────┐   ┌──────────────────▼──────────────┐  │
│  │ Rota Plan.  │   │      Kontrol Çıktısı              │  │
│  │ A* / Graf   ├──►│  Uçuş / İniş / Görev Devamı     │  │
│  └─────────────┘   └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## Yazılım Modülleri

### Aktif Modüller

| Dosya | İşlev |
|-------|-------|
| `sistemDöküman.py` | `NAV` sınıfı: enlem/boylam takibi, `hedefyon()` ve `hedefmesafe()` hesaplamaları |
| `GNSSSpofing.py` | GNSS spoofing tespiti, irtifa izleme, iniş bölgesi doğrulama |
| `hastaneler.py` | Hipotenuş mesafe hesabıyla en yakın hastane bulma algoritması |
| `kütüphaneler.py` | Ortak bağımlılık importları (`cezeri_lib`, `rospy`, `math`, `numpy`) |

### Planlanan Modüller

| Dosya | Planlanan İşlev |
|-------|----------------|
| `main.py` | Uygulama giriş noktası |
| `sistem.py` | Sistem orkestrasyon katmanı |
| `uçuş.py` | Uçuş modu kontrolü |
| `iniş.py` | Otonom iniş prosedürü |
| `IMUdata.py` | IMU sensör füzyon işleme |
| `sensorsecim.py` | Aktif sensör seçim algoritması |
| `uçuş_yasaklı_bolge.py` | No-fly zone tespiti ve yönlendirme |
| `trafik.py` | Hava trafik çatışma önleme |
| `GNSSArızaİnis.py` | GNSS kayıp durumunda acil iniş |
| `GNSSARızaGörevDevam.py` | GNSS kayıp durumunda INS ile görev devamı |
| `gitmesi gerekenyönHesaplama.py` | Anlık hedef yön vektörü |
| `gittigiyön.py` | Gerçekleşen iz kaydı |

---

## Navigasyon Sistemi (`sistemDöküman.py`)

```python
class NAV:
    # Araç konumunu enlem/boylam cinsinden tutar
    # ve hedef noktaya göre yön / mesafe hesaplar

def hedefyon(enlem1, boylam1, enlem2, boylam2) -> float:
    # Mevcut konum → hedef arasındaki yön açısını döndürür (derece)

def hedefmesafe(enlem1, boylam1, enlem2, boylam2) -> float:
    # İki koordinat arası düzlemsel mesafeyi döndürür (metre)
```

---

## GNSS Güvenlik Modülü (`GNSSSpofing.py`)

GNSS sinyalinin spoofed (sahte) olup olmadığını tespit eder:

- Ölçülen irtifa ile beklenen irtifa karşılaştırması
- Ani konum sıçramalarının izlenmesi
- Spoofing tespitinde güvenli iniş bölgesi doğrulama

```python
# Sahte sinyal tespiti → acil iniş protokolü tetiklenir
if gnss_spoof_detected():
    initiate_safe_landing()
```

---

## Acil Müdahale — En Yakın Hastane (`hastaneler.py`)

Araç mevcut konumundan veritabanındaki tüm hastanelere mesafe hesaplar,
en yakın tesisi bulur ve rotayı günceller.

```python
def en_yakin_hastane(arac_enlem, arac_boylam, hastane_listesi):
    # Haversine değil, hızlı hipotenuş tahmini
    # Yarışma senaryosu için yeterli doğruluk
    return min(hastane_listesi, key=lambda h: mesafe(arac, h))
```

---

## Teknoloji Yığını

| Katman | Teknoloji |
|--------|-----------|
| **Dil** | Python 3.x |
| **Robot Middleware** | ROS (Robot Operating System) |
| **Araç Framework** | `cezeri_lib` (CEZERİ yarışma kütüphanesi) |
| **Nümerik İşlem** | NumPy |
| **Matematiksel Navigasyon** | `math.atan2`, `math.sqrt`, `math.degrees` |
| **Diyagram** | draw.io |

---

## Kurulum

```bash
# ROS ortamını kaynak göster
source /opt/ros/<distro>/setup.bash

# Cezeri kütüphanelerini kur (yarışma ortamı)
pip install cezeri_lib numpy

# Çalıştır
python Yazılım/main.py
```

---

## Raporlar ve Dokümanlar

| Dosya | İçerik |
|-------|--------|
| `RAPORLAR/2024_Kablosuz_Haberleşme_Yarışması_...docx` | Sistem gereksinim dokümanı |
| `RAPORLAR/BÜRKÜT-ÖTRrrr.pdf` | Sistem tasarım raporu |
| `RAPORLAR/elestiri_2024.docx` | Teknik değerlendirme ve kritikler |
| `RAPORLAR/döküman/` | 20+ akademik makale (İHA, otonom navigasyon, BMS) |
| `Yazılım/Untitled Diagram.drawio` | Sistem mimarisi diyagramı (draw.io) |
| `Yazılım/otonom uçuş sistem tasarımı/` | Sistem tasarımı görseli |

### Referans Alınan Akademik Çalışmalar

- Otonom hava araçları navigasyon ve kontrol sistemleri
- GNSS güvenilirliği ve spoofing önleme
- İnsansız hava araçlarının askeri ve sivil uygulamaları
- Elektrikli araç batarya yönetim sistemleri
- Otonom sistem simülatörü tasarımı
- Güdüm ve otopilot algoritmaları

---

## Arayüz Tasarımları

`Adsız tasarım/` klasöründe yer alan mockup'lar:

| Ekran | Açıklama |
|-------|---------|
| `görevPlanlayıcı.png` | Harita üzerinde waypoint tabanlı görev planlama |
| `ucusveri.png` | Gerçek zamanlı uçuş telemetrisi |
| `ayarlar.png` | Sistem parametreleri ve kalibrasyon |

---

## Yarışma Bağlamı

**CEZERİ**, BAYKAR Teknoloji tarafından düzenlenen öğrenci otonom araç yarışmasıdır.
Bu proje, otonom uçan araç kategorisinde yarışmak üzere ASHİNA takımı tarafından geliştirilmiştir.

Temel yarışma senaryoları:
- Belirlenmiş waypoint'ler arasında otonom navigasyon
- GNSS arızasında görev sürekliliği (INS fallback)
- Acil tıbbi müdahale (en yakın hastane yönlendirmesi)
- No-fly zone farkındalığı ve dinamik yeniden yönlendirme
