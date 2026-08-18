# 🐍 Python Fundamentals & Data Science Practice

Bu depo, Python programlama temellerinden başlayarak veri analitiği pratiklerine ve kural tabanlı makine öğrenmesi/segmentasyon uygulamalarına kadar uzanan alıştırmaları ve projeleri içermektedir.

---

## 📁 İçerik ve Dosya Yapısı

### 1. `case_study_hafta_1.py`
Temel Python yapıları, veri tipleri, fonksiyonlar ve list comprehension pratikleri:
* **Veri Yapıları:** String, Integer, Float, Complex, List, Tuple, Set ve Dictionary işlemleri.
* **Fonksiyonlar & Koşullar:** Listeler üzerinde tek/çift sayı filtreleme ve özel fonksiyon tanımlamaları.
* **Döngüler & İterasyon:** `enumerate()` ve `zip()` fonksiyonlarının pratik senaryolarda kullanımı.
* **Küme (Set) Operasyonları:** Alt/üst küme kontrolü (`issuperset`), kesişim (`intersection`) ve fark (`difference`).
* **Comprehensions:** Koşullu List Comprehension ile veri manipülasyonu ve filtreleme alıştırmaları.

---

### 2. `case_study_hafta_2.py`
Pandas & Seaborn kütüphaneleri ile veri analizi ve kural tabanlı müşteri segmentasyonu projesi:

#### 📊 Keşifçi Veri Analizi (EDA) Pratikleri
* **Titanic Veri Seti:** 
  * Eksik değer tespiti ve doldurma (medyan/mod ile imputasyon).
  * Koşullu seçimler, tip dönüşümleri (`category`) ve değişken silme/ekleme (`apply`, `lambda`, `np.where`).
  * `groupby` ve `agg` ile çok boyutlu özet istatistikler.
* **Tips Veri Seti:** 
  * Kategorik kırılımlara göre harcama/bahşiş analizleri.
  * Filtreleme ve sıralama (`sort_values`) işlemleri.

#### 🎯 Proje: Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
* **İş Problemi:** Uluslararası bir oyun şirketinin kullanıcı demografik bilgilerini (Ülke, Cihaz, Cinsiyet, Yaş) kullanarak seviye tabanlı (*level-based*) müşteri personaları oluşturmak ve yeni müşterilerin şirkete sağlayabileceği ortalama getiriyi tahmin etmek.
* **Adımlar:**
  1. Veri setini keşfetme ve özetleme.
  2. `COUNTRY`, `SOURCE`, `SEX` ve `AGE` kırılımında ortalama kazançları hesaplama.
  3. `AGE` değişkenini `pd.cut` ile kategorik aralıklara dönüştürme.
  4. Yeni seviye tabanlı müşterileri (`customers_level_based`) tanımlama.
  5. `pd.qcut` kullanarak müşterileri harcama potansiyellerine göre segmentlere (A, B, C, D) ayırma.
  6. Yeni gelebilecek kurgusal kullanıcılar için persona eşleştirmesi ile getiri ve segment tahmini yapma.

---

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler

* **Python 3.x**
* **Pandas**
* **NumPy**
* **Seaborn**

---

