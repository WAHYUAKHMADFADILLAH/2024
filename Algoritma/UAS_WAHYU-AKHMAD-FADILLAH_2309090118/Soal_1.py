def main():
    mahasiswa = []
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({'NIM': nim, 'Nama': nama})
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ")
        if tambah_lagi != 'ya':
            break
    for idx, mhs in enumerate(mahasiswa, start=1):
        print(f"{idx}. NIM: {mhs['NIM']}, Nama: {mhs['Nama']}")
    
    print("sangkyouh!.")
main()
