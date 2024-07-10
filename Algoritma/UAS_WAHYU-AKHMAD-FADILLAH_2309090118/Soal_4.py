class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama):
        self.nama = nama

    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"


class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"{super().information()}, Vitamin: {self.vitamin}"

mangga = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")

print(f"Nama: {mangga.nama}")
print(f"Warna: {mangga.warna}")
print(f"Rasa: {mangga.rasa}")
print(f"Vitamin: {mangga.vitamin}")

print("\nInformasi Buah:")
print(mangga.information())

mangga.set_nama("Mangga Manalagi")
mangga.set_warna("Kuning")
mangga.set_rasa("Manis dan Asam")
mangga.set_vitamin("Vitamin A")

print("\nInformasi Buah setelah perubahan:")
print(mangga.information())