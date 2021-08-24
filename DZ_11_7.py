class ComplexNumbers:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def __add__(self, other):
        result = ComplexNumbers(self.num_a + other.num_a, self.num_b + other.num_b)
        return result

    def __mul__(self, other):
        result_1 = ComplexNumbers(self.num_a * other.num_a, self.num_a * other.num_b)
        result_2 = ComplexNumbers(self.num_b * other.num_a, self.num_b * other.num_b)
        result = result_1 + result_2
        return result

    def __str__(self):
        op = '+'
        if self.num_b < 0:
            op = ''
        return f'z = {self.num_a} {op} {self.num_b}i'


cn = ComplexNumbers(5, 7)
cn_2 = ComplexNumbers(2, 5)
print(cn + cn_2)
print(cn * cn_2)
