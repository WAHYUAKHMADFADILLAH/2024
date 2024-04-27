def tanya_makanan_favorit():
    while True:
        nama = input("Halo! Siapa namamu? ")
        # Periksa apakah nama kosong atau tidak sesuai tipe
        if not nama or not isinstance(nama, str):
            print("Mohon masukkan nama yang valid.")
            continue # Mengulangi loop untuk meminta nama kembali
        print(f"Hai {nama.title()}! Saya ingin tahu apa makanan favoritmu.")
        while True:
           makanan_favorit = input("Apa makanan favoritmu? ")
           if not makanan_favorit or not isinstance(makanan_favorit,str):
            print("Mohon masukkan makanan yang valid.")
            continue
           print(f'wah {makanan_favorit} saya juga suka {makanan_favorit} mantap!')
           return nama, makanan_favorit

def olahraga_favorit():
   while True:
      nama_olahraga = input('olahraga apa yang kamu suka ? ')
      if not nama_olahraga or not isinstance(nama_olahraga,str):
         print('nama olahraga tidak valid, masukan ulang!')
         continue
      print(f'wah {nama_olahraga}, menggesankan! aku juga suka {nama_olahraga}.')
      return nama_olahraga

def menanyakan_warna_kesukaan():
   while True:
      warna_kesukaan = input('warna apa yang kamu sukaa?? ')
      if not warna_kesukaan or not isinstance(warna_kesukaan,str):
         continue
      print(f'wah warna favoritmu {warna_kesukaan}, keren bangett!!')
      return warna_kesukaan
 
nama ,makanan_favorit = tanya_makanan_favorit()
nama_olahraga = olahraga_favorit()
warna_favorit = menanyakan_warna_kesukaan()
print('======hasil======')
print(f'nama = {nama.title()}')
print(f'makanan kesukaan = {makanan_favorit}')
print(f'olahraga kesukaan = {nama_olahraga}')
print(f'warna kesukaan = {warna_favorit}')