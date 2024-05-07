a = 12.5
aint = int(a)  
afloat = float(a)

print(aint)
print(type(aint))
print(afloat)
print(type(afloat))

hasil = aint + afloat
print(hasil)

umur = 12#int(input('masukan umur : '))

if umur >= 18:
    print("Anda sudah dewasa")
    if umur == 18:
        print("Anda sudah berumur 18 tahun")
    else:
        print("Anda belum berumur 18 tahun")
else:
    print("Anda masih di bawah umur")
    
    
for i in range(0,2):
    print(i)

def tambah(a,b):
    return a+b
def mod(a,b):
    return a%b
def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        
def calc():
    print('pilihan')
    print('1.penjumlahan')
    print('2.mod')
    print('3.keluar')
    print('3.keluar')
    pilihan = int(input('pilihan : '))
    if pilihan == 1:
        a = int(input('masukan angka pertama : ' ))
        b = int(input('masukan angka kedua : '))
        print('hasil penjumlahan : ',tambah(a,b))
        lagi = input('apakah anda ingin mengulang (y/n) : ')
        if lagi == 'y':
            calc()
        else:
            print('terimakasih')
            exit()
    elif pilihan == 2:
        a = int(input('masukan angka pertama : ' ))
        b = int(input('masukan angka kedua : '))
        print('hasil mod : ',mod(a,b))
        lagi = input('apakah anda ingin mengulang (y/n) : ')
        if lagi == 'y':
            calc()
        else:
            print('terimakasih')
            exit()
    elif pilihan == 3:
        print('terimakasih')
        exit()
calc()      