database = {}
def add():
    name = input("Masukan Nama Barang : ")
    jum = input("Masukan Jumlah : ")
    database[name] = jum
    print(f"Data {name} telah ditambahkan")
def delete():
    name = input("Nama Data yang ingin dihapus : ")
    if name in database:
        del database[name]
        print(f"Data {name} telah dihapus")
        print('Data : ',database)
    else:
        print(f"Data {name} tidak ditemukan")
        print('Data : ',database)
        delete()
def edit():
    name = input("Masukan nama Data yang ingin di edit : ")
    if name in database:
        jum = input("Ubah jumlah : ")
        database[name] = jum
        print(f"Data {name} telah di edit")
        print('Data : ',database)
    else:
        print(f"Data {name} tidak ditemukan")
        print('Data : ',database)
        edit()
def search():
    name = input("Masukan Nama Data yang ingin dicari : ")
    if name in database:
        print(f"Data {name} ditemukan")
        print('Data : ',database)
    else:
        print(f"Data {name} tidak ditemukan")
        print(database)
        search( )
def jumdatabase():
    print('jumlah Data :' ,len(database))
    print('Data : ',database)
def show():
    print('Data : ',database)
def MSB():
    while True:
        print("========================================")
        print("Menu : ")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. edit")
        print("4. Cari Data")
        print("5. Tampilkan Jumlah Data")
        print("6. Tampilkan Data")
        print("7. Keluar")
        print("========================================")
        pilihan = int(input("Masukan pilihan: "))
        print("========================================")
        if pilihan == 1:
            add()
        elif pilihan == 2:
            delete()
        elif pilihan == 3:
            edit()
        elif pilihan == 4:
            search()
        elif pilihan == 5:
            jumdatabase()
        elif pilihan == 6:
            show()
        elif pilihan == 7:
            yakin = input('apakah yakin ingin keluar [y/n] :')
            if yakin == 'y':
                print("""
                      Terimakasih telah menggunakan program ini
                      Sampai Jumpa lain waktu!!
                      """)
                exit()
            elif yakin == 'n':
                MSB()

def login():
    print('''
   __  ___                    _                               
  /  |/  /___ _ ___  ___ _   (_)___  __ _  ___  ___           
 / /|_/ // _ `// _ \/ _ `/  / // -_)/  ' \/ -_)/ _ \          
/_/  /_/ \_,_//_//_/\_,_/__/ / \__//_/_/_/\__//_//_/          
   ____ __         __   |___/                               __
  / __// /_ ___   / /__  / _ ) ___ _ ____ ___ _ ___  ___ _ / /
 _\ \ / __// _ \ /  '_/ / _  |/ _ `// __// _ `// _ \/ _ `//_/ 
/___/ \__/ \___//_/\_\ /____/ \_,_//_/   \_,_//_//_/\_, /(_)  
                                                   /___/      
''')
    print("Selamat Datang di Manajemen Stok Barang")
    login = input('ingin masuk ke Manajemen stok barang? [y/n] : ')
    if login == 'y':
        MSB()
        print("========================================")
    elif login == 'n':
        print("Sampai Jumpa lain waktu!!")
        exit()
    else:
        print("input salah")
        MSB()