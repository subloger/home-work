
def gen(n):
    nums_gen = (num for num in range(1, n, 2))
    yield nums_gen


print(*next(gen(int(input('Введите число - ')))))
