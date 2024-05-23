import numpy as np

# Cek versi numpy
print("Numpy version:", np.__version__)

# Membuat array numpy
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Operasi matematika dasar
print("Tambah 5 ke setiap elemen:", array + 5)
print("Kalikan setiap elemen dengan 2:", array * 2)

# Membuat array 2D (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)

# Operasi pada matrix
print("Transpose matrix:\n", matrix.T)
print("Jumlah elemen di matrix:", np.sum(matrix))
print("Rata-rata elemen di matrix:", np.mean(matrix))

# Menghasilkan array dengan angka acak
random_array = np.random.rand(3, 3)
print("Random array:\n", random_array)

# Menghasilkan array dengan angka dalam range tertentu
range_array = np.arange(0, 10, 2)
print("Range array:", range_array)

# Operasi pada array acak
print("Mean dari random array:", np.mean(random_array))
print("Standard deviation dari random array:", np.std(random_array))
