import random
from pympler import asizeof as asi
import string

# версия питон 3.8
# разрядность 64 bit


# Пример № 1   ***************************************

num = str(random.randint(111, 999))
print(f'Значение для расчета = {num}')
num_1 = int(num[0]) + int(num[1]) + int(num[2])
num_2 = int(num[0]) * int(num[1]) * int(num[2])

print(f'Сумма = {num_1},\nПроизведение = {num_2}')

print(f'num = {asi.asizeof(num)}')
print(f'num_1 = {asi.asizeof(num_1)}')
print(f'num_2 = {asi.asizeof(num_2)}')
sum_1 = asi.asizeof(num) + asi.asizeof(num_1) + asi.asizeof(num_2)
print(f'Общее количество зянятой памяти {sum_1} байт')

# Значение для расчета = 659
# Сумма = 20,
# Произведение = 270
# num = 56
# num_1 = 32
# num_2 = 32
# Общее количество зянятой памяти 120 байт

# Значение для расчета = 902
# Сумма = 11,
# Произведение = 0
# num = 56
# num_1 = 32
# num_2 = 24
# Общее количество зянятой памяти 112 байт


# Пример № 2   ***************************************

rand_list = []
for i in range(20):
    rand_list.append(random.randint(1, 10))

val_num = 0
value = 0

for j in range(max(rand_list) + 1):
    summa = rand_list.count(j)
    if summa > val_num:
        value = j
        val_num = summa
    max_num = f'Число {value} встречается {val_num} раз'

print(max_num)
print(rand_list)

print(f'val_num = {asi.asizeof(val_num)}')
print(f'value = {asi.asizeof(value)}')
print(f'max_num = {asi.asizeof(max_num)}')
print(f'rand_list = {asi.asizeof(rand_list)}')
sum_2 = asi.asizeof(val_num) + asi.asizeof(value) + asi.asizeof(max_num) + asi.asizeof(rand_list)
print(f'Общее количество зянятой памяти {sum_2} байт')

# Число 8 встречается 6 раз
# [3, 10, 1, 8, 3, 5, 3, 3, 8, 7, 8, 6, 5, 3, 8, 2, 2, 8, 8, 5]
# val_num = 32
# value = 32
# max_num = 128
# rand_list = 512
# Общее количество зянятой памяти 704 байт

# Число 9 встречается 5 раз
# [4, 4, 5, 4, 3, 1, 7, 9, 6, 9, 2, 9, 1, 1, 9, 7, 7, 8, 9, 7]
# val_num = 32
# value = 32
# max_num = 128
# rand_list = 544
# Общее количество зянятой памяти 736 байт


# Пример № 3   ***************************************

letter_1 = input('Введите первую букву - ')
letter_2 = input('Введите вторую букву - ')

let = string.ascii_lowercase

num_1 = let.find(letter_1) + 1
num_2 = let.find(letter_2) + 1
print(f'{letter_1} - {num_1}, {letter_2} - {num_2}')
print(f'{(num_2 - num_1) - 1} буквы между введенными')

print(f'letter_1 = {asi.asizeof(letter_1)}')
print(f'letter_2 = {asi.asizeof(letter_2)}')
print(f'let = {asi.asizeof(let)}')
print(f'num_1 = {asi.asizeof(num_1)}')
print(f'num_2 = {asi.asizeof(num_2)}')
sum_3 = asi.asizeof(letter_1) + asi.asizeof(letter_2) + asi.asizeof(let) + asi.asizeof(num_1) + asi.asizeof(num_2)
print(f'Общее количество зянятой памяти {sum_3} байт')

# Введите первую букву - a
# Введите вторую букву - f
# a - 1, f - 6
# 4 буквы между введенными
# letter_1 = 56
# letter_2 = 56
# let = 80
# num_1 = 32
# num_2 = 32
# Общее количество зянятой памяти 256 байт

# Введите первую букву - a
# Введите вторую букву - z
# a - 1, z - 26
# 24 буквы между введенными
# letter_1 = 56
# letter_2 = 56
# let = 80
# num_1 = 32
# num_2 = 32
# Общее количество зянятой памяти 256 байт
