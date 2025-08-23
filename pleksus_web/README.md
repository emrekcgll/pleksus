# Pleksus Web - Ana Sayfa

Bu modül, Pleksus şirketinin web sitesi için modern ve responsive ana sayfa tasarımını içerir.

## Özellikler

### 🎨 Modern Tasarım
- Gradient arka planlar ve modern renk paleti
- Responsive tasarım (mobil uyumlu)
- Smooth animasyonlar ve geçişler
- Bootstrap 5 tabanlı layout

### 🚀 Ana Bölümler
1. **Hero Section**: Etkileyici başlık ve çağrı butonları
2. **Features**: Öne çıkan özellikler (3 kart)
3. **Stats**: İstatistikler (4 metrik)
4. **CTA**: Çağrı bölümü
5. **Contact**: İletişim formu ve bilgileri

### ⚡ İnteraktif Özellikler
- Smooth scrolling
- Fade-in animasyonları
- Sayaç animasyonları
- Form validasyonu
- Bildirim sistemi
- Scroll progress bar

## Kurulum

1. Modülü Odoo'ya yükleyin
2. Web sitesinde ana sayfa olarak ayarlayın
3. Gerekirse içerikleri özelleştirin

## Dosya Yapısı

```
pleksus_web/
├── controllers/
│   ├── __init__.py
│   └── main.py
├── static/
│   └── src/
│       ├── css/
│       │   └── homepage.css
│       ├── js/
│       │   └── homepage.js
│       └── images/
│           └── hero-illustration.svg
├── views/
│   └── website_templates.xml
├── __init__.py
├── __manifest__.py
└── README.md
```

## Özelleştirme

### Renkler
Ana renkler CSS değişkenleri ile tanımlanmıştır:
- Primary: `#667eea` (mavi)
- Secondary: `#764ba2` (mor)
- Text: `#2c3e50` (koyu gri)

### İçerik
- Metinler `website_templates.xml` dosyasında düzenlenebilir
- Görseller `static/src/images/` klasöründe değiştirilebilir
- Stiller `static/src/css/homepage.css` dosyasında özelleştirilebilir

## Teknik Detaylar

### Kullanılan Teknolojiler
- **HTML5**: Semantic markup
- **CSS3**: Modern styling, gradients, animations
- **JavaScript ES6+**: Modern JavaScript features
- **Bootstrap 5**: Responsive grid system
- **Font Awesome**: İkonlar

### Browser Desteği
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Geliştirme

### Yeni Özellik Ekleme
1. Template'e HTML ekleyin
2. CSS stillerini yazın
3. JavaScript fonksiyonlarını ekleyin
4. Manifest dosyasını güncelleyin

### Test
- Farklı ekran boyutlarında test edin
- Farklı tarayıcılarda kontrol edin
- Form validasyonunu test edin

## Destek

Herhangi bir sorun veya özelleştirme talebi için:
- GitHub Issues kullanın
- E-posta: info@pleksus.com

## Lisans

LGPL-3 lisansı altında dağıtılmaktadır.
