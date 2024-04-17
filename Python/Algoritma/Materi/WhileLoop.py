i = 1 
while i <= 10 :
	print('Angka :',i)
	i += 1

total_loop = 0
while True:
	main = input('selesai atau tidak : ').lower()
	if main == 'selesai':
		break
	total_loop += 1
print('Total Perulangan : ',total_loop)

# i = 0
# while i <= 10:
# 	if i == 5:
# 		i += 1
# 		continue
# 	print(i)
# 	i += 1