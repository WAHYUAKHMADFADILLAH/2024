string1 = 'hello'
string2 = 'world'
int1 = 5
print(string1 + ' ' + string2)
print((string1 + ' ' )* 10)
print(string1 + str(int1))

list_kalimat = ['aku','seorang','kapiten']
kalimat = ' '.join(list_kalimat)
print(kalimat)

list_kalimat = 'aku belum makan'
kalimat = list_kalimat.split()
print(kalimat)

kalimat = list_kalimat.replace('makan','minum')
print(kalimat)
nama = 'putri nur oktaviani' 
print('nama = ', nama)
print('upper = ',nama.upper()) #.upper untuk capslok
print('lower = ',nama.lower()) #.lower untuk un capslok
print('capitalize = ',nama.capitalize())
print('title = ',nama.title())
print('mengambil dari string = ',nama[0:3])

uang = 2308023909
print('uang = ','{:,}'.format(uang))
print('uang = ','{:.2f}'.format(uang))
print('uang = ','{:,.2f}'.format(uang))
print('=='*(13))

print(f'Rp.{uang:,}')
print(f'Rp.{uang:.2f}')
print(f'Rp.{uang:,.2f}')

penilaian = input('Masukan Penilaian [Bagus/Tidak]').title
print(penilaian)