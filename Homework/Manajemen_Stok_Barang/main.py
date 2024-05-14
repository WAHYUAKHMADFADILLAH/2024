DB = {}

def TB():
    NB = input('Masukan Nama barang : ')
    SB = input('Masukan Stok barang : ')
    DB[NB]=SB
    print(f"Data barang '{NB}' telah ditambahkan ke stok {SB}. ")
def HB():
    NB = input('masukan barang yang ingin dihapus : ')
    if NB in DB:
        del DB[NB]
        print(f"Data barang '{NB} ")
        