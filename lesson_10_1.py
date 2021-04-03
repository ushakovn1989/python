class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        values = ('\t'.join(map(str, el)) for el in self.data)
        return '\n'.join(values)

    def __add__(self, other):
        matrix_sum = [
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.data, other.data)]
        return Matrix(matrix_sum)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print('-' * 79)
print(matrix_1 + matrix_2)
