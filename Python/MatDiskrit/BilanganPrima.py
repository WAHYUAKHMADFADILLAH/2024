def cek_prima(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def cari_prima_dibawah(batas):
    if batas <= 2:
        return []
    primes = [2]
    for i in range(3, batas, 2):
        if cek_prima(i):
            primes.append(i)
    return primes

batas = 50
print(f"Bilangan prima yang kurang dari {batas}:")
print(cari_prima_dibawah(batas))



# # Mendefinisikan fungsi
# def sapa(nama):
#     print("Halo,", nama)

# # Memanggil fungsi
# sapa("Andi")
# sapa('putra')