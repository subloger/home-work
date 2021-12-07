import random

# Задание № 1   ***********************************************

list_num = []

for i in range(20):
    list_num.append(random.randint(-100, 100))


def bubbles_sort(value):
    n = 0
    print(f'Исходный массив - {value}')
    while n < len(value):
        m = 0
        for j in range(len(value) - 1):
            if value[j + 1] > value[j]:
                value[j], value[j + 1] = value[j + 1], value[j]
            else:
                m += 1
        if m == len(value) - 1:
            break
        n += 1
        sorted_list = f'Отсортировано за {n} проходов - {value}\n'
    return sorted_list


print(bubbles_sort(list_num))


# Задание № 2   ***********************************************

list_num_start = []

for i in range(20):
    list_num_start.append([random.randint(0, 50)])
print(f'Начальный список - {list_num_start}')

list_num = list_num_start.copy()

for j in range(len(list_num)):
    if list_num[j] <= list_num[j + 1]:
        list_num[j].extend(list_num[j + 1])
        list_num.remove(list_num[j + 1])
    elif list_num[j] >= list_num[j + 1]:
        list_num[j + 1].extend(list_num[j])
        list_num.remove(list_num[j])
    if len(list_num) - 1 == j:
        break
list_num = list_num

list_2 = []
while True:
    list_1 = []
    a = 0
    b = 0
    if len(list_num) > 1:
        while a < len(list_num[0]) and b < len(list_num[1]):
            if list_num[0][a] <= list_num[1][b]:
                list_1.append(list_num[0][a])
                list_num[0].remove(list_num[0][a])
            elif list_num[0][a] >= list_num[1][b]:
                list_1.append(list_num[1][b])
                list_num[1].remove(list_num[1][b])
        if a < len(list_num[0]):
            for i in range(len(list_num[0])):
                list_1.append(list_num[0][i])
        elif b < len(list_num[1]):
            for i in range(len(list_num[1])):
                list_1.append(list_num[1][i])

        list_num.remove(list_num[0])
        list_num.remove(list_num[0])
        list_2.append(list_1)
        if len(list_1) == len(list_num_start):
            print(f'Отсортированный список - {list_1}\n')
            break
    elif len(list_num) == 1:
        for i in range(len(list_2)):
            list_num.insert(i, list_2[i])
    elif len(list_num) == 0:
        for i in range(len(list_2)):
            list_num.append(list_2[i])
        list_2.clear()
    else:
        for i in range(len(list_2)):
            list_num.insert(i, list_2[i])
        list_2.clear()


# Задание № 3   ***********************************************

# Не совсем понял, что значит массив размером 2m + 1
# поэтому решение наверное не правильное
arr = []

for i in range(10):
    arr.append((2 * (random.randint(1, 100))) + 1)
arr_2 = arr.copy()
print(f'Массив {arr}')
while True:
    if len(arr_2) == 2:
        break
    else:
        arr_2.remove(min(arr_2))
        arr_2.remove(max(arr_2))

median = sum(arr_2) / 2

more_median = []
less_median = []
for i in arr:
    if i > median:
        more_median.append(i)
    else:
        less_median.append(i)


print(f'Значения выше медианы {more_median}')
print(f'Медиана {median}')
print(f'Значения ниже медианы {less_median}')
