import numpy as np

# Sistem persamaan:
# 2x + 3y = 6
# 4x - y = 5

# Koefisien matriks
A = np.array([[2, 3], [4, -1]])

# Vektor konstanta
B = np.array([6, 5])

# Menyelesaikan sistem persamaan
solusi = np.linalg.solve(A, B)

print(f"Nilai x dan y yang memenuhi sistem persamaan adalah x = {solusi[0]}, y = {solusi[1]}")


# https://notepad.pw/kodealin