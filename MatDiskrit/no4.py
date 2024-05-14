import random
nomor_hp = "085157739978"

# Mengambil 6 digit terakhir dari nomor handphone
last_six_digits = nomor_hp[-6:]

# Mengonversi ke dalam bilangan biner
binary_number = bin(int(last_six_digits))[2:]

# Mengonversi ke dalam bilangan heksadesimal
hexadecimal_number = hex(int(last_six_digits))[2:]

# Mengonversi ke dalam bilangan oktal
octal_number = oct(int(last_six_digits))[2:]

# Menampilkan hasil konversi
print("Biner:", binary_number)
print("Heksadesimal:", hexadecimal_number.upper())
print("Oktal:", octal_number)


original_nim = "23090118"

# Membuat 5 NIM baru dengan mengganti 3 huruf terakhir
new_nims = []

for _ in range(5):
    # Mengambil 3 angka acak untuk mengganti 3 huruf terakhir
    random_digits = ''.join(random.choices('0123456789', k=3))
    
    # Menggabungkan NIM asli (8 digit pertama) dengan 3 angka acak
    new_nim = original_nim[:-3] + random_digits
    
    # Menambahkan NIM baru ke dalam list
    new_nims.append(new_nim)

# Menampilkan hasil NIM baru
print("5 NIM baru:")
for nim in new_nims:
    print(nim)
