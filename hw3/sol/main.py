from matrix_lib import Matrix
from numpy_matrix import NumPyMatrix
import numpy as np

# -------- task 1 ---------

np.random.seed(0)
matrix_a = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
matrix_b = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

result_add = matrix_a + matrix_b
result_add.save_to_file('matrix_add.txt')

result_mul = matrix_a * matrix_b
result_mul.save_to_file('matrix_mul.txt')

result_matmul = matrix_a @ matrix_b
result_matmul.save_to_file('matrix_matmul.txt')

# -------- task 2 ---------

np.random.seed(0)
matrix_data = np.random.randint(0, 10, (10, 10)).tolist()
matrix = NumPyMatrix(matrix_data)

result_add = matrix + matrix
result_add.save('matrix_add.txt')

result_mul = matrix * 2
result_mul.save('matrix_mul.txt')

result_matmul = matrix @ matrix
result_matmul.save('matrix_matmul.txt')

# -------- task 3 ---------

np.random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())


C = Matrix([[A.matrix_data[i][j] + 1 if i == j else A.matrix_data[i][j] for j in range(A.columns)] for i in range(A.rows)])
D = B

AB = A @ B
CD = C @ D

A.save_to_file('A.txt')
B.save_to_file('B.txt')
C.save_to_file('C.txt')
D.save_to_file('D.txt')

AB.save_to_file('AB.txt')
CD.save_to_file('CD.txt')

with open('../artifacts/3/hash.txt', 'w') as file:
    file.write(f"Хэш матрицы AB: {hash(AB)}\n")
    file.write(f"Хэш матрицы CD: {hash(CD)}")