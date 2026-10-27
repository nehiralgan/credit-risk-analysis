# 🏦 Bireysel Kredi Risk ve Müşteri Segmentasyonu Analizi (End-to-End Data Analysis)

## 📌 Proje Özeti
Bu proje, bir finans kuruluşunun (veya bankanın) kredi risk yönetimini optimize etmek amacıyla yapılmış **uçtan uca (end-to-end) bir veri analitiği** çalışmasıdır. Temel amaç, müşterilerin demografik ve finansal geçmişlerine bakarak **kredi batırma (default) riskini** tahmin etmek ve banka yöneticileri için veri odaklı karar almayı sağlayacak interaktif bir raporlama panosu sunmaktır.

Projeyi öne çıkaran en önemli özellik; ham verinin Excel'den alınıp, Python ile temizlenmesi, SQLite ile ilişkisel veritabanına aktarılarak SQL ile sorgulanması ve son olarak Power BI ile görselleştirilerek eksiksiz bir veri ardışık düzeni (data pipeline) kurgulanmasıdır.

## 🛠️ Kullanılan Teknolojiler ve Araçlar
* **Veri Tanıma & Profilleme:** Microsoft Excel (Veri Sözlüğü oluşturma, anomali tespiti)
* **Veri Temizleme & EDA:** Python (Pandas, Matplotlib, Seaborn)
* **Veritabanı Yönetimi & Sorgulama:** SQLite & SQL
* **İş Zekası & Görselleştirme (BI):** Power BI (İnteraktif Yönetici Panosu)

---

## 🚀 Proje Aşamaları (Workflow)

### Faz 1: Veri Profilleme (Excel)
* Kaggle'dan alınan ham `credit_risk_dataset.csv` dosyası incelendi.
* Veri tiplerinin ve sütun anlamlarının yer aldığı bir **Veri Sözlüğü (Data Dictionary)** oluşturuldu.
* Yaş sütunundaki 144 yaş ve çalışma süresindeki 123 yıl gibi veri giriş hataları (fat-finger errors) tespit edildi.

### Faz 2: Veri Temizliği ve Keşifsel Analiz (Python)
* **Outlier Handling:** Excel'de tespit edilen mantıksız yaş (>100) ve çalışma süreleri (>60) filtrelendi.
* **Missing Value Imputation:** Finansal verilerde ortalamayı (mean) saptırmamak adına, faiz oranlarındaki (`loan_int_rate`) ve çalışma sürelerindeki boşluklar **ortanca (median)** değer ile dolduruldu.
* **Encoding & Format Çözümleri:** Excel'in ham CSV'yi kaydederken yaşattığı "Encoding (UTF-8 / Latin-1)" sorunları ve faiz oranlarını otomatik tarihe (örn. Kas.14) çevirme problemleri (Data Corruption) tespit edilip Python seviyesinde ham veri korunarak çözüldü.

### Faz 3: Risk Metriklerinin Hesaplanması (SQL)
* Temizlenen veri bir SQLite veritabanına (`credit_risk.db`) aktarıldı.
* İş problemini çözmek adına SQL sorguları yazılarak çeşitli demografik kırılımlarda batık kredi oranları (Default Rate) hesaplandı. (Örn: Ev sahipliği durumuna göre risk analizi).

### Faz 4: Yönetici Panosu Tasarımı (Power BI)
* Yöneticiler için "Toplam Müşteri, Ortalama Kredi Miktarı, Toplam Batık Kredi" gibi temel KPI kartları oluşturuldu.
* Müşteri risk kümelenmesini (Clustering) görmek için Yaş/Gelir dağılım grafikleri tasarlandı.
* "Kredi Amacı" (Eğitim, Sağlık vb.) bazında panoyu dinamikleştiren interaktif filtreler (Slicer) eklendi.

---

## 📊 Temel İş İçgörüleri (Business Insights)
1. **Ev Sahipliği ve Risk İlişkisi:** SQL analizlerine ve Power BI görselleştirmelerine göre, kirada oturan (RENT) müşterilerin kredisini batırma olasılığı, kendi evi olanlara (OWN) veya ipotekli evi olanlara (MORTGAGE) göre istatistiksel olarak daha yüksektir. Banka, kiracılara kredi verirken skorlama kriterlerini sıkılaştırmalıdır.
2. **Gelir Segmentasyonunda Yığılma:** Dağılım grafiği (Scatter Plot) analizinde, kredisini ödeyemeyen müşterilerin (Kırmızı Noktalar) çok büyük bir kısmının düşük-orta gelir seviyesine sıkıştığı, yüksek gelir gruplarında kredi miktarından bağımsız olarak default oranının dramatik şekilde düştüğü görülmüştür.

---

## 💻 Projeyi Kendi Bilgisayarınızda Çalıştırmak İçin
1. Repoyu klonlayın: `git clone https://github.com/KULLANICI_ADINIZ/credit-risk-analysis.git`
2. Gerekli Python kütüphanelerini yükleyin: `pip install pandas matplotlib seaborn sqlite3`
3. Veri temizleme adımı için `main.py` dosyasını çalıştırın.
4. SQL analizleri ve veritabanı oluşturma için `sql_analizi.py` dosyasını çalıştırın.
5. Sonuçları incelemek için `Dashboard.pbix` (varsa) dosyasını Power BI ile açın.

