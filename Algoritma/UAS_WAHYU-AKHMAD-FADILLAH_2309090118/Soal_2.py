# saya memiliki data yaitu . nama =  mahasiswa 1 yang nilai algoritma dan struktur data 2 adalah 90 dan matematika numeriknya 80
# dan nama =  mahasiswa 2 yang nilai algoritma dan struktur data 2 adalah 50 dan matematika numeriknya 60
# dan nama =  mahasiswa 3 yang nilai algoritma dan struktur data 2 adalah 65 dan matematika numeriknya 70
# buatlah sebuah array 2 dimensi yang berisi data pada tabel diatas dalam bentuk dataframe lalu, buatlah sebuah program python untuk melakukan operasi berikut: 1. Tampilkan rata rata nilai untuk setiap mata kuliah, 2. Tampilkan rata rata nilai untuk setiap mahasiswa
import pandas as pd
data = [
    ['Mahasiswa 1', 90, 80],
    ['Mahasiswa 2', 50, 60],
    ['Mahasiswa 3', 65, 70]
]
df = pd.DataFrame(data, columns=['Nama', 'Algoritma dan Struktur Data 2', 'Matematika Numerik'])

print("Data Mahasiswa dan Nilai:")
print(df)


rata_rata_matkul = df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean()
print("\nRata-rata Nilai untuk Setiap Mata Kuliah:")
print(rata_rata_matkul)
212
df['Rata-rata Mahasiswa'] = df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean(axis=1)
print("\nData Mahasiswa dengan Rata-rata Nilai:")
print(df[['Nama', 'Rata-rata Mahasiswa']])
