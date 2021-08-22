class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __add__(self, other):
        result_list = []
        for n in range(len(self.list_1)):
            list_of_sum = [self.list_1[n][i] + other.list_1[n][i] for i in range(len(self.list_1))]
            result_list.append(list_of_sum)
        str_1 = [' '.join(map(str, result_list[i])) for i in range(len(result_list))]
        return print('\n'.join(str_1))

    def __str__(self):
        str_1 = [' '.join(map(str, self.list_1[i])) for i in range(len(self.list_1))]
        print('\n'.join(str_1))


matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
f'Matrix {matrix_1.__str__()}'
print()
matrix_2 = Matrix([[4, 5, 9], [78, 2, 32], [45, 6, 88]])
matrix_2.__str__()
print()
matrix_1 + matrix_2
