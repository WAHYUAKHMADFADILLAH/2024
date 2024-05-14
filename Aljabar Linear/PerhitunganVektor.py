import numpy as np
print('NAMA : WAHYU AKHMAD FADILLAH')
print('NIM  : 23090118')
print('====================================')
VA = [2,4,6,8]
VB = [13, 15, 17, 19]
VC = [[10, 20, 30],[11, 22, 33]]
VD = [[9, 7, 5],[21, 31, 41]]

# vektor
veka = np.array(VA)
vekb = np.array(VB)
vekc = np.array(VC)
vekd = np.array(VD)

print('**A.penjumlahan dan perkalian**')
A1 = veka + vekb
A2 = vekd + vekc
A3 = vekb - veka
A4 = vekc - vekd
print('1. VA + VB = ',str(A1))
print('2. VD + VC = ',str(A2))
print('3. VB - VA = ',str(A3))
print('4. VC - VD = ',str(A4))
print('====================================')
print('**B.perkalian dan pembagian**')
B1 = vekb * veka
B2 = vekc * vekd
B3 = vekb / veka
B4 = vekd / vekc
print('1. VB x VA = ',str(B1))
print('2. VC x VD = ',str(B2))
print('3. VB : VA = ',str(B3))
print('4. VD : VC = ',str(B4))
print('====================================')
print('**C. perkalian titik(dot)**')
C1 = np.dot(vekb,veka)
print("1. dot VB.VA = ",str(C1))
vekc = np.array(VC)
vekd = np.array(VD)
C2 = np.inner(vekc,vekd)
print("1. dot VC.VD = ",str(C2))
# dot_product = np.inner(vekc, vekd)
# print("2. dot VC.VD = " + str(dot_product))
print('====================================')
print("**perkalian skalar**")
SK1 = 2
SK2 = 2.5
SK3 = 0.5
SK4 = 1.5

print('1. skalar VA x 2 =', SK1 * veka)
print('2. skalar VB x 2.5 =', SK2 * vekb)
print('3. skalar VC x 0.5 =', SK2 * vekc)
print('4. skalar VD x 1.5 =', SK2 * vekd)