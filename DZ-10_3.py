class Cell:
    value = None

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        sum_1 = self.cell + other.cell
        return sum_1

    def __sub__(self, other):
        sub_1 = self.cell - other.cell
        if sub_1 > 0:
            return sub_1
        else:
            return f'Отрицательное значение'

    def __mul__(self, other):
        mul_1 = self.cell * other.cell
        return mul_1

    def __floordiv__(self, other):
        f_div = self.cell // other.cell
        return f_div

    def make_order(self, value):
        self.value = value
        cell_list = [i for i in range(1, self.cell + 1)]
        n = 0
        str_1 = self.cell // value
        result_list = []
        for i in range(0, str_1 + 1):
            result_list.append(' '.join(map(str, cell_list[n: value + n])))
            n += value
        return print('\n'.join(result_list))


cell_1 = Cell(23)
cell_2 = Cell(6)

print(f'Результат сложения: {cell_1 + cell_2}')
print(f'Результат вычитания: {cell_1 - cell_2}')
print(f'Результат умножения: {cell_1 * cell_2}')
print(f'Результат деления: {cell_1 // cell_2}')
print()
cell_1.make_order(5)
