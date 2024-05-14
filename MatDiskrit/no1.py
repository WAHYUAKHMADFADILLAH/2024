def hitung_luas_lapangan(p, l):
    luas = p * l
    return luas

panjang_lapangan = float(input("Masukkan panjang lapangan (meter): "))
lebar_lapangan = float(input("Masukkan lebar lapangan (meter): "))

luas_lapangan = hitung_luas_lapangan(panjang_lapangan, lebar_lapangan)

print("Luas lapangan sepak bola adalah", luas_lapangan, "meter persegi")
