# restoran_queue.py

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
