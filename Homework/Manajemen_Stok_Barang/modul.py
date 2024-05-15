database = {}

def add():
    name = input("Enter name: ")
    age = input("Enter age: ")
    database[name] = age
    print(f"Data {name} telah ditambahkan")
    print(database)

def delete():
    name = input("Enter name: ")
    if name in database:
        del database[name]
        print(f"Data {name} telah dihapus")
        print(database)
    else:
        print(f"Data {name} tidak ditemukan")
        print(database)

def search():
    name = input("Enter name: ")
    if name in database:
        print(f"Data {name} ditemukan")
        print(database)
    else:
        print(f"Data {name} tidak ditemukan")
        print(database)

def update():
    name = input("Enter name: ")
    if name in database:
        age = input("Enter age: ")
        database[name] = age
        print(f"Data {name} telah diupdate")
        print(database)
    else:
        print(f"Data {name} tidak ditemukan")
        print(database)

def show():
    print(database)
def MSB():
    while True:
        print("1. Add")
        print("2. Delete")
        print("3. Search")
        print("4. Update")
        print("5. Show")
        print("6. Exit")
        pilihan = int(input("Masukan pilihan: "))
        if pilihan == 1:
            add()
        elif pilihan == 2:
            delete()
        elif pilihan == 3:
            search()
        elif pilihan == 4:
            update()
        elif pilihan == 5:
            show()
        elif pilihan == 6:
            break
        else:
            print("Pilihan tidak tersedia")
            print("Silahkan masukan pilihan yang tersedia")
            print()

    print("Terimakasih telah menggunakan program ini")
MSB()