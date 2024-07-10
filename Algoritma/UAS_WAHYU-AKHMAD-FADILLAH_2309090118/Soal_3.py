class RestoranQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, pesanan):
        self.queue.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
            return None
        pesanan = self.queue.pop(0)
        print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")
        return pesanan

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian pesanan saat ini:")
            for idx, pesanan in enumerate(self.queue, start=1):
                print(f"{idx}. {pesanan}")

# Fungsi utama untuk menjalankan program
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
