
#memasukan dan membaca data
import pandas as pd

data = pd.read_csv("IMDB-Movie-Data.csv", sep=',')

#Ukuran dataset
print('Ukuran Dataset :')
print(data.shape)

print('\nLima Data Pertama:')
print(data.head(5))

#lihat informasi dataset
print("Informasi Dataset:")
data.info()

#periksa nilai unik (variasi data)
print('Jumlah Nilai yang Unik:')
print(data.nunique())

#memeriksa duplikasi
print('Jumlah data duplikat:')
print(data.duplicated().sum())

#periksa missing value
print("\nJumlah Data Kosong:")
print(data.isna().sum())

#persentasi data kosong
print('\nPersetase Data Kosong:')
print((data.isna().sum()/len(data))*100)

#lihat baris yang memiliki data kosong
print('\nData Dengan Revenue Kosong:')
print(data[data['Revenue (Millions)'].isna()].head(10))

print('\nData dengan Metascore Kosong:')
print(data[data['Metascore'].isna()].head(10))

#memahami karakteristik data nya
print('\nStatistik Deskriptif:')
print(data.describe())

#mengisi data kosong di revenue dengan median
median_revenue = data['Revenue (Millions)'].median()
data['Revenue (Millions)'] = data['Revenue (Millions)'].fillna(median_revenue)

#Mengisi data kosong pada metascroe dengan median
median_metascore = data['Metascore'].median()
data['Metascore'] = data['Metascore'].fillna(median_metascore)

#hasil penanganan data kosong
print('Jumlah Missing Value setelah pembersihan:')
print(data.isna().sum())

#Membersihkan spasi di kolom teks
kolom_teks =['Title','Genre','Description','Director','Actors']

for kolom in kolom_teks :
    data[kolom]=data[kolom].str.strip()

print('Pembersihan Spasi berhasil dilakukan.')
print(data[kolom_teks].head())

#menghapus data duplikat
print('Duplikasi sebelum penghapusan:')
print(data.duplicated().sum())

data = data.drop_duplicates()

#memeriksa data setelah penghapusan
print('\nDuplikasi Setelah Penghapusan:')
print(data.duplicated().sum())

print('\nUkuran Dataset setelah Penghapusan:')
print(data.shape)

#Deteksi outlier
#metode IQR pada kolom rating
Q1 =data['Rating'].quantile(0.25)
Q3 =data['Rating'].quantile(0.75)

IQR = Q3-Q1

batas_bawah= Q1-1.5*IQR
batas_atas= Q3+1.5*IQR

#Identifikasi Outlier
kondisi = (data['Rating'] < batas_bawah) | (data['Rating'] > batas_atas)

outlier = data[kondisi]
    
print('Q1:',Q1)
print('Q3:',Q3)
print('IQR:',IQR)

print('Batas bawah:',batas_bawah)
print('Batas Atas:',batas_atas)

print('Jumlah outlier:',len(outlier))

print(outlier[['Title','Rating']])

#memeriksa kembali kondisi dataset
print('1. jumlah missing values:')
print(data.isna().sum())

print('\n2. jumlah data duplikat:')
print(data.duplicated().sum())

print('\n3. ukuran dataset:')
print(data.shape)

print('\n4. Infomasi dataset:')
data.info()

#menyimpan dataset yang sudah dibersihkan
data.to_csv('IMDB-Movie-Data_Cleaned.csv', index=False)
print('Dataset berhasil disimpan.')

#melihat lokasi penyimpanan data bersih
import os

print("Lokasi penyimpanan:")
print(os.getcwd())
