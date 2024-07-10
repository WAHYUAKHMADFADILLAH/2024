'''
Langkah 1: 
Mendefinisikan tiga kategori mainan yang berbeda:
boneka, mobil, dan bola.
Masing-masing kategori memiliki tiga elemen.

Langkah 2:
Mendefinisikan tiga kelompok utama
(Kotak A, Kotak B, Kotak C)
di mana mainan akan dibagi.

Langkah 3:
Mengelompokkan mainan ke dalam tiga kotak dengan aturan
bahwa setiap kotak harus berisi satu mainan dari setiap kategori.

Langkah 4: 
Menampilkan hasil pembagian sehingga bisa dilihat bahwa 
setiap kotak memenuhi aturan yang ditetapkan.
'''
# Mainan

boneka = ["Boneka1", "Boneka2", "Boneka3"]
mobil = ["Mobil1", "Mobil2", "Mobil3"]
bola = ["Bola1", "Bola2", "Bola3"]

# Kotak
kotak = {
    "Kotak A": [],
    "Kotak B": [],
    "Kotak C": []
}

# Membagi mainan ke dalam kotak
kotak["Kotak A"] = [boneka[0], mobil[0], bola[0]]
kotak["Kotak B"] = [boneka[1], mobil[1], bola[1]]
kotak["Kotak C"] = [boneka[2], mobil[2], bola[2]]

# Menampilkan hasil
for k, v in kotak.items():
    print(f"{k}: {', '.join(v)}")
