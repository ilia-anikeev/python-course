import numpy as np
from typing import List, Union


class HashableMatrixMixin:
    def __hash__(self) -> int:
        return sum(sum(row) for row in self.matrix_data) * self.columns

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.matrix_data == other.matrix_data


class Matrix(HashableMatrixMixin):
    def __init__(self, matrix_data: List[List[Union[int, float]]]):
        if not matrix_data:
            raise ValueError("Матрица должна содержать хотя бы один элемент")
        self.rows = len(matrix_data)
        self.columns = len(matrix_data[0]) if self.rows > 0 else 0
        for row in matrix_data:
            if len(row) != self.columns:
                raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix_data = matrix_data
        self._cached_matrix_product = {}

    def _check_dimensions(self, other_rows, other_columns):
        if self.rows != other_rows or self.columns != other_columns:
            raise ValueError("Размеры матриц не совпадают")

    def __add__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} не является объектом Matrix")
        self._check_dimensions(other.rows, other.columns)
        result = [[self.matrix_data[i][j] + other.matrix_data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} не является объектом Matrix")
        self._check_dimensions(other.rows, other.columns)
        result = [[self.matrix_data[i][j] * other.matrix_data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other) -> 'Matrix':
        if not isinstance(other, Matrix):
            raise ValueError(f"{other} не является объектом Matrix")
        if self.columns != other.rows:
            raise ValueError(f"Количество столбцов в левой матрице не равно количеству строк в правой матрице: {self.columns} != {other.rows}")
        other_hash = hash(other)
        if other_hash in self._cached_matrix_product:
            return self._cached_matrix_product[other_hash]
        result = Matrix([
            [sum(self.matrix_data[i][k] * other.matrix_data[k][j] for k in range(self.columns))
             for j in range(other.columns)]
            for i in range(self.rows)
        ])
        self._cached_matrix_product[other_hash] = result
        return result

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix_data])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))
