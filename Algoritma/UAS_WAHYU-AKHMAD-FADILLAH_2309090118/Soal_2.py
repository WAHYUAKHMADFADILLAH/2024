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
