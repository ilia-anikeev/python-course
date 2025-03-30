import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from typing import Union, List


class FileSaverMixin:
    def save(self, filename: str):
        with open(filename, 'w') as file:
            file.write(str(self))


class PrettyPrinterMixin:
    def __str__(self):
        return np.array_str(self._matrix, precision=2)


class NumPyMatrix(NDArrayOperatorsMixin, FileSaverMixin, PrettyPrinterMixin):
    def __init__(self, matrix_data: List[List[Union[int, float]]]):
        if not matrix_data or len(matrix_data) == 0:
            raise ValueError("Матрица должна содержать хотя бы один элемент")
        self._rows = len(matrix_data)
        self._cols = len(matrix_data[0]) if self._rows > 0 else 0
        for row in matrix_data:
            if len(row) != self._cols:
                raise ValueError("Все строки матрицы должны иметь одинаковую длину")
        self._matrix = np.array(matrix_data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = []
        for input in inputs:
            if isinstance(input, NumPyMatrix):
                args.append(input._matrix)
            else:
                args.append(input)
        result = getattr(ufunc, method)(*args, **kwargs)
        return NumPyMatrix(result.tolist()) if isinstance(result, np.ndarray) else result

    @property
    def matrix(self) -> np.ndarray:
        return self._matrix

    @matrix.setter
    def matrix(self, new_matrix):
        new_obj = NumPyMatrix(new_matrix)
        self._matrix = new_obj.matrix
        self._rows = new_obj.rows
        self._cols = new_obj.cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols
