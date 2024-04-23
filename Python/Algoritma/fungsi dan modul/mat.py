def penjumlahan(a,b):
  return a+b
def pengurangan(a,b):
  return a-b
def perkalian(a,b):
  return a*b
def tampilan_main():
  print('pilihan')
  print('1.penjumlahan')
  print('2.pengurangan')
  print('3.perkalian')
  pilihan = input('masukan pihan (1/2/3) : ')
  if pilihan not in ('1','2','3'):
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