# main.py

from Modulno3 import RestoranQueue

def main():
    restoran_queue = RestoranQueue()

    while True:
        print("\nSistem Antrian Restoran")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ").strip()

        if pilihan == '1':
            pesanan = input("Masukkan nama pesanan: ").strip()
            restoran_queue.enqueue(pesanan)
        elif pilihan == '2':
            restoran_queue.dequeue()
        elif pilihan == '3':
            restoran_queue.display_queue()
        elif pilihan == '4':
            print("Arigatona!!.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
