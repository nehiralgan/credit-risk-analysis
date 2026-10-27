import pandas as pd
import sqlite3

# 1. Temizlenmiş veriyi oku
df = pd.read_csv('cleaned_credit_risk.csv')

# 2. SQLite veritabanı oluştur ve bağlan (klasörde credit_risk.db oluşacak)
conn = sqlite3.connect('credit_risk.db')

# 3. DataFrame'i doğrudan SQL tablosuna dönüştür
df.to_sql('loan_data', conn, if_exists='replace', index=False)
print("Veri başarıyla SQL veritabanına (loan_data tablosuna) aktarıldı!")

# 4. SQL Sorgusu: Ev durumuna göre batık kredi analizi
query = """
SELECT 
    person_home_ownership AS Ev_Durumu,
    COUNT(*) AS Toplam_Musteri,
    SUM(loan_status) AS Batik_Kredi_Sayisi,
    ROUND((CAST(SUM(loan_status) AS FLOAT) / COUNT(*)) * 100, 2) AS Batik_Orani_Yuzde
FROM 
    loan_data
GROUP BY 
    person_home_ownership
ORDER BY 
    Batik_Orani_Yuzde DESC;
"""

# 5. Sorguyu veritabanında çalıştır ve ekrana yazdır
risk_raporu = pd.read_sql_query(query, conn)
print("\n--- EV DURUMUNA GÖRE KREDİ RİSK RAPORU ---")
print(risk_raporu)

# 6. Veritabanı bağlantısını kapat
conn.close()