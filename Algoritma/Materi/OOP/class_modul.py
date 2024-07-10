class car:
    def __init__(self, merk, color, years):
        self.merk = merk
        self.color = color
        self.years = 2010

car1 = car('Kharisma','Putih','2003')
print(car1.__dict__)

car2 = car('Suzuki','Merah','2040')
print(car2.__dict__)

class Persegi_Panjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2*(self.panjang + self.lebar)

buku = Persegi_Panjang(10,5)
print('Luas buku : ',buku.luas())
print('Keliling buku : ',buku.keliling())

hp = Persegi_Panjang(20,10)
print('Luas hp : ',hp.luas())
print('Keliling hp  : ',hp.keliling())