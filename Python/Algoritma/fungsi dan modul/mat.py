def penjumlahan(a,b):
  return a+b
def pengurangan(a,b):
  return a-b
def perkalian(a,b):
  return a*b
def pembagian(a,b):
  return a/b
def tampilan_main():
  print('pilihan')
  print('1.penjumlahan')
  print('2.pengurangan')
  print('3.perkalian')
  print('4.pembagian')
  pilihan = input('masukan pihan (1/2/3/4) : ')
  if pilihan not in ('1','2','3','4'):
    print('pilihan operator tidak valid')
  else:
   angka1 = int(input('masukan angka pertama : '))
   angka2 = int(input('masukan angka kedua : '))

  if pilihan == '1':
    print('hasil penjumlahan : ',penjumlahan(angka1,angka2))
  elif pilihan == '2' :
    print('hasil penjumlahan : ',pengurangan(angka1,angka2))
  elif pilihan == '3' :
    print('hasil penjumlahan : ',perkalian(angka1,angka2))
  elif pilihan == '4':
    print('hasil pembagian : ',pembagian(angka1,angka2))
    lagi = input('apakah anda ingin mengulang (y/n) : ')
    if lagi == 'y':
      tampilan_main()
    else:
      print('terimakasih')
