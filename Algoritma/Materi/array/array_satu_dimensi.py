nilai_siswa = [90,80,70,60,50,]
print(nilai_siswa)
print(nilai_siswa[2])

nilai_siswa.append(40)
print(nilai_siswa)

nilai_siswa[0] = 40

nilai_siswa.pop()
print(nilai_siswa)

print(len(nilai_siswa))
print(sum(nilai_siswa))

rata_rata = sum(nilai_siswa)/len(nilai_siswa)

print(max(nilai_siswa))
print(min(nilai_siswa))

nilai_up_average = sum(True for i in nilai_siswa if i > rata_rata)
print('nilai diatas rata-rata : ',nilai_up_average)
