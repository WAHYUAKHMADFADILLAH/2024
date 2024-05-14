nama = str(input('masukan nama karyawan : '))
jabatan = str(input('masukan jabatan [Design / Programmer / Resouce] : '))
status = str(input('maukan status perkawinan [Y/T] : '))
if jabatan == 'Design':
	gajipokok = 5000000
elif jabatan == 'Programmer':
	gajipokok = 10000000
elif jabatan == 'Resouce':
	gajipokok = 5000000
else:
	print('tidak ada jabatan di database')
	exit()
if status == 'Y':
	tunjangan = 0.2 * gajipokok
else:
	tunjangan = 0

gajikotor = gajipokok + tunjangan
pajak = 0.1 * gajikotor
totalpendapatan = gajipokok - pajak
print(f'{nama} : ')
print(f'{jabatan} : ')
print(f'{status} : ')
print(f'jumlah gaji kotor = {gajikotor:,}')
print(f'jumlah tunjaangan keluarga = {tunjangan:,}')
print(f'jumlah pajak = {pajak:,}')
print(f'jumlah total pendapatan{totalpendapatan:,}')
