import random
import collections
import string

# Задание № 1   ******************************************************

names_company = ['NEON', 'START', 'SQD', 'NEXT']
dict_company = {}
average_sum = collections.defaultdict(list)
above_average = []
below_average = []

for i in names_company:
    list_in = []
    for n in names_company:
        list_in.append(random.randint(5000, 10000))
    dict_company[i] = [j for j in list_in]
    average_sum[i].append(round(sum(dict_company[i]) / 4, 2))

a = sum(dict_company["NEON"]) / 4
b = sum(dict_company["START"]) / 4
c = sum(dict_company["SQD"]) / 4
d = sum(dict_company["NEXT"]) / 4
average = round((a + b + c + d) / 4, 2)
print(f'Средняя прибыль для всех предприятий = {average} руб.')

for item in average_sum.keys():
    if average_sum[item][0] > average:
        above_average.append(item)
    else:
        below_average.append(item)

print(f'\nПрибыль выше среднего у предприятий {above_average}')
print(f'Прибыль ниже среднего у предприятий {below_average}')


# Задание № 2   ******************************************************

sample = string.ascii_uppercase[:6]
digits = string.digits
sam_dig = sample + digits

num_1, num_2 = [], []

for i in range(2):
    num_1.append(random.choice(sam_dig))
    num_2.append(random.choice(sam_dig))

print(f'Число 1 - {num_1},\nЧисло 2 - {num_2}\n')

num_1 = '0X' + ''.join(num_1)
num_2 = '0X' + ''.join(num_2)
result_1 = hex(int(num_1, 16) + int(num_2, 16))
result_2 = hex(int(num_1, 16) * int(num_2, 16))

result_1 = list(result_1[2:])
result_2 = list(result_2[2:])

list_result = collections.namedtuple('LR', ['R1', 'R2'])
lr = list_result(R1=result_1, R2=result_2)

print(f'Результат сложения - {lr.R1}')
print(f'Результат умножения - {lr.R2}')
