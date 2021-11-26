import random


# Задание № 1   *****************************************

list_num = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 100):
    if i % 2 == 0:
        list_num[0] = list_num[0] + 1
    if i % 3 == 0:
        list_num[1] = list_num[1] + 1
    if i % 4 == 0:
        list_num[2] = list_num[2] + 1
    if i % 5 == 0:
        list_num[3] = list_num[3] + 1
    if i % 6 == 0:
        list_num[4] = list_num[4] + 1
    if i % 7 == 0:
        list_num[5] = list_num[5] + 1
    if i % 8 == 0:
        list_num[6] = list_num[6] + 1
    if i % 9 == 0:
        list_num[7] = list_num[7] + 1

print(f'Числу {2} кратны {list_num[0]}\n'
      f'Числу {3} кратны {list_num[1]}\n'
      f'Числу {4} кратны {list_num[2]}\n'
      f'Числу {5} кратны {list_num[3]}\n'
      f'Числу {6} кратны {list_num[4]}\n'
      f'Числу {7} кратны {list_num[5]}\n'
      f'Числу {8} кратны {list_num[6]}\n'
      f'Числу {9} кратны {list_num[7]}\n')


# Задание № 2   *****************************************

list_start = []
list_index = []
for i in range(20):
    list_start.append(random.randint(1, 20))

for n, j in enumerate(list_start):
    if j % 2 == 0:
        list_index.append(n)

print(list_start)
print(list_index)


# Задание № 3   *****************************************

rand_list = []
for i in range(20):
    rand_list.append(random.randint(1, 10))

print(rand_list)
min_list = min(rand_list)
max_list = max(rand_list)

for j in range(len(rand_list)):
    if rand_list[j] == min_list:
        rand_list[j] = max_list
    elif rand_list[j] == max_list:
        rand_list[j] = min_list
print(rand_list)


# Задание № 4   *****************************************

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


# Задание № 5   *****************************************

rand_list = []
for i in range(20):
    rand_list.append(random.randint(-10, 10))

negative_list = [j for j in rand_list if j < 0]

print(rand_list)
print(f'Максимальный отрицательный элемент = {max(negative_list)}\n'
      f'Его позиция {rand_list.index(max(negative_list))}')


# Задание № 6   *****************************************

rand_list = []
for i in range(20):
    rand_list.append(random.randint(1, 100))

summa = sum(rand_list[rand_list.index(min(rand_list)) + 1: rand_list.index(max(rand_list))])

print(rand_list)
print('минимальное значение', min(rand_list))
print('максимальное значение', max(rand_list))
print(rand_list[rand_list.index(min(rand_list)) + 1: rand_list.index(max(rand_list))])
print(f'Сумма всех элементов - {sum(rand_list)}')
print(f'Сумма всех между минимальным и максимальным - {summa}')


# Задание № 7   *****************************************

rand_list = []
for i in range(20):
    rand_list.append(random.randint(1, 20))

rand_list.sort()
print(f'Наименьшими элементами являются - {rand_list[0]} и {rand_list[1]}')


# Задание № 8   *****************************************

matrix = []

for i in range(4):
    matrix.append([random.randint(1, 100) for j in range(4)])

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}\n')

for j in range(4):
    matrix[j].append(sum(matrix[j]))

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}\n')


# Задание № 9   *****************************************

matrix = []
min_elements = []
for i in range(4):
    matrix.append([random.randint(1, 100) for j in range(4)])

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}\n')
elements = []
for j in range(len(matrix)):
    for k in range(4):
        elements.append(matrix[k][j])
    min_elements.append(min(elements[-4:]))

print(f'Минимальные элементы столбцов {min_elements}')
print(f'Максимальный элемент среди минимальных {max(min_elements)}')
