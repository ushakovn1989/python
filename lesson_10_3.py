class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        difference = self.num_cells - other.num_cells
        if difference > 0:
            return difference
        else:
            return 'The difference is less than zero'

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __floordiv__(self, other):
        return Cell(self.num_cells // other.num_cells)

    def make_order(self, row_cells):
        result = []
        for i in range(1, self.num_cells + 1):
            result.append('*')
            if i % row_cells == 0 and i != self.num_cells:
                result.append('\n')
        return ''.join(result)


cell_1 = Cell(10)
cell_2 = Cell(8)

print(f'sum: {cell_1 + cell_2}', f'dif: {cell_1 - cell_2}')
print(cell_2 - cell_1)
print(f'mul: {(cell_1 * cell_2).num_cells}', f'div: {(cell_1 // cell_2).num_cells}')
print('-' * 79)
print(cell_1.make_order(5))
print('-' * 79)
print(cell_1.make_order(3))
