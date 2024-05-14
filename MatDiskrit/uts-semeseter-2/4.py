print('4.A')
nomor_handphone = "085157739978"
angka_terakhir = nomor_handphone[-6:]
angka_desimal = int(angka_terakhir)
biner = bin(angka_desimal)
heksa = hex(angka_desimal)
oktal = oct(angka_desimal)
print("Konversi ke dalam biner:", biner)
print("Konversi ke dalam heksadesimal:", heksa)
print("Konversi ke dalam oktal:", oktal)
print('4.B')
nim = [23090118, 23090114, 23090113, 23090112, 23090111]
import random
nim = [f"{n:08d}".replace("011", str(random.randint(0, 999))) for n in nim]
nim_bin = [format(int(n), '016b') for n in nim]
nim_hex = [hex(int(n))[2:] for n in nim]
nim_oct = [oct(int(n))[2:] for n in nim]
print("NIMs (decimal):", nim)
print("NIMs (binary):", nim_bin)
print("NIMs (hexadecimal):", nim_hex)
print("NIMs (octal):", nim_oct)