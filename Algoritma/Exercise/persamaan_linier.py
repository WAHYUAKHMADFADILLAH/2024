print('='*15,'Persamaan Linier','='*15)
# Persamaan Linier
a = 2
b = 3

x = -b/a
print(f'Nilai x yang meemenuhi persamaan 2x + 3 = 0 adalah x = {x}')

# fungsi linier
print('='*15,'fungsi Linier','='*15)
def fungsi_linier (x, m ,c):
	return m*x+c
m = 3
c = 2
x = 1
hasil  = fungsi_linier(x, m, c)
print(f'f({x}) = {m}*{x} + {c} = {hasil}')

print('='*15,'fungsi affine','='*15)
def fungsi_affine(x, m ,c):
	return m*x+c
m = 4
c = 1
x = 2
hasil  = fungsi_affine(x, m, c)
print(f'f({x}) = {m}*{x} + {c} = {hasil}')

print('='*15,'ocntoh penggunaan model','='*15)
import numpy as np 
# Data contoh: suhu (x) dan penjualan es krim (y)
x = np.array([10,20,30 ,40 ,50])
y = np.array([15,25,35 ,45 ,55])
# Menghitung koefisien regresi linier
m , c = np.polyfit(x, y ,1)
# Fungsi model_linier(x):
def model_linier(x):
	return m * x + c
# contoh Penggunaan model
suhu = 30 
penjualan = model_linier(suhu)
print(f'penjualan es krim  saat suhu {suhu} derajat adalah {penjualan}')
