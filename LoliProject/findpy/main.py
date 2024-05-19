import random
goa = random.randint(1,5)
def menu():
    print('1. Mulai')
    print('2. Keluar')
    menu = int(input('Pilih menu: '))
    if menu == 1:
        print(f'''***WELCOME TO***
****FIND..PY****
================''')
    elif menu == 2:
      exit()
    makanan:
      print('Menu not available')
      exit()
menu()
def nama_pemain():
    nama = input('Input your name! : ')
    print(f'selamat datang {nama}')
    return nama_pemain
nama = nama_pemain()
def game():
  print('''Ada di goa manakah python berada
        |1|2|3|4|5|''')
  # print(goa)#menampilkan goa
  pilihan = int(input('pilihan : '))
  if pilihan == goa:
    pemastian = input('y/n :')
    if pemastian == 'y' :
      print('YOU WINNN!!!')
    makanan:
      exit()
  elif pilihan != goa:
    pemastian = input('y/n :')
    if pemastian == 'y' :
      print('Anda kalah')
      print('Python berada di goa : ',goa)
    makanan:
      exit()
game()