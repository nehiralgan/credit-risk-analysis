import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi içeri aktar (CSV dosyasının adının doğru olduğundan emin ol)
df = pd.read_csv('credit_risk_dataset.csv')

# İlk 5 satıra ve verinin genel yapısına göz at
print(df.info())

# 100 yaşından büyük olan imkansız satırları filtrele
df = df[df['person_age'] <= 100]

# 60 yıldan fazla çalışma süresi olan imkansız satırları filtrele
df = df[df['person_emp_length'] <= 60]

print(f"Aykırı değerler temizlendikten sonra kalan satır sayısı: {len(df)}")

# Hangi sütunlarda kaç tane boş veri var görelim
print(df.isnull().sum())

# Faiz oranı ve çalışma süresindeki boşlukları medyan ile doldur
df['loan_int_rate'] = df['loan_int_rate'].fillna(df['loan_int_rate'].median())
df['person_emp_length'] = df['person_emp_length'].fillna(df['person_emp_length'].median())

# Boş veri kalmış mı diye teyit et
print("Eksik veri kaldı mı?\n", df.isnull().sum())

# Grafik 1: Kredi ödeyenler (0) ve batıranların (1) sayısal dağılımı
plt.figure(figsize=(6,4))
sns.countplot(x='loan_status', data=df, palette='Set2')
plt.title('Kredi Durumu Dağılımı (0: Ödendi, 1: Batık)')
plt.show()

# Grafik 2: Gelir seviyesinin kredi batırma durumuna etkisi
plt.figure(figsize=(8,5))
sns.boxplot(x='loan_status', y='person_income', data=df, palette='Set2')
plt.title('Kredi Durumuna Göre Gelir Dağılımı')
plt.ylim(0, 150000) # Grafiği netleştirmek için üst gelir limitini sabitledik
plt.show()

# İndeksleri dahil etmeden yeni bir dosya olarak kaydet
df.to_csv('cleaned_credit_risk.csv', index=False)
print("Temizlenmiş veri 'cleaned_credit_risk.csv' olarak kaydedildi!")