import hashlib
import string
import random

# Задание № 1   ********************************************************

s = ''
for i in range(10):
    s = s + random.choice(string.ascii_lowercase)
print(f'Строка - {s}')

result = []
sub_str = 0
n = 1
while n != len(s)+1:
    for j in range(len(s)):
        if len(s[j: j + n]) == n:
            hash_1 = hashlib.sha1(s[j: j + n].encode('utf-8')).hexdigest()
            result.append(hash_1)
        hash_2 = hashlib.sha1(s[j: j + n].encode('utf-8')).hexdigest()
        if hash_1 == hash_2:
            sub_str += 1
    n += 1
print(f'\nЗакодированные подстроки\n{result}\n')
print(f'Количество подстрок {sub_str}')


# Задание № 2   ********************************************************
# Второе задание не смог сделать, принцип работы алгоритма Хафмана понятен,
# но вот с реализацией не справился. Может если подольше повозиться то все получиться.

str_1 = 'Hello World'

# создание списка значений и вхождений
list_1 = []
for i in range(len(str_1)):
    list_1.append([str_1[i], str_1.count(str_1[i])])

# удаление дубликатов
n = 0
for j in range(len(list_1)):
    if list_1.count(list_1[n]) > 1:
        list_1.remove(list_1[n])
    else:
        n += 1

# сортировка списка
m = 1
sort_list = []
while len(sort_list) != len(list_1):
    for n in range(len(list_1)):
        if m == list_1[n][1]:
            sort_list.append(list_1[n])
    m += 1

len_sort = len(sort_list)

# создание структуры дерева (не смог сделать сортировку по сумме приоритетов)
while len(sort_list) != 1:
    a = sort_list[0]
    b = sort_list[1]
    sort_list.append([a, b])
    sort_list.remove(sort_list[0])
    sort_list.remove(sort_list[0])

tree_list = sort_list[0].copy()

# кодирование символов (здесь можно закодировать только 8 разных символов)
a = 0
b = 0
c = 0
code_list = {}
while len(code_list) != len_sort:
    if tree_list[a][b][c][0] not in code_list.keys():
        code_list[tree_list[a][b][c][0]] = f'{a}{b}{c}0'
    elif c == 0:
        c = 1
    elif b == 0:
        b = 1
        c = 0
    elif a == 0:
        a = 1
        b = 0
        c = 0

# вывод таблицы кодировки и закодированного сообщения
message = ''
for i in str_1:
    print(f'{i} - {code_list[i]}')
    message += f'{code_list[i]} '
print(f'message - {message}')