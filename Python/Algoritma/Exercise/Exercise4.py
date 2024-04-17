import random
angka_togel = random.randint(1,10)
print(angka_togel)
tebakan = False
percobaan = 0
while True :
  angka_tebakan = int(input('Masukan angka : '))
  if angka_tebakan == angka_togel:
    print('benar')
    break
  elif angka_tebakan >= angka_togel:
    print('Terlalu Duwur Banget :3')
  elif angka_tebakan <= angka_togel:
    print('Terlalu kecil Banget')
  else:
    print('salah')
  percobaan += 1
  print(percobaan)
  exit()

