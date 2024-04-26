def tanya_makanan_favorit():
    while True:
        nama = input("Halo! Siapa namamu? ")
        # Periksa apakah nama kosong atau tidak sesuai tipe
        if not nama or not isinstance(nama, str):
            print("Mohon masukkan nama yang valid.")
            continue # Mengulangi loop untuk meminta nama kembali
        print(f"Hai {nama}! Saya ingin tahu apa makanan favoritmu.")
        while True:
           makanan_favorit = input("Apa makanan favoritmu? ")
           if not makanan_favorit or not isinstance(makanan_favorit,str):
            print("Mohon masukkan makanan yang valid.")
            continue
           print(f'wah {makanan_favorit} saya juga suka {makanan_favorit} mantap!')
           break
        break
tanya_makanan_favorit()
