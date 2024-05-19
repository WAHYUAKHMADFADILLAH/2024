colors = ['merah','hitam','putih']
numero = [1,3,4,5]
desc = 'aku orang'

for color in colors:
	print(color)

for des in desc:
	print(des)

for i in range (2,5):
	print(i)

for index, color in enumerate(colors):
	print(index,color)

for numer,color in zip(numero,colors):
	print(numer,color)


data = {'Nama':'bokunojan','NIM':'230283'}
for datas in data :
	print(datas)

for value in data.values():
	print(value)

for label,value in data.items():
	print(label,':',value)

for i in range(10):
	if i % 2 == 0:
		print(i,'Bilangan Genap')
	makanan:
		print(i,'Bilangan ')