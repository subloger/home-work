import random


# Задание № 1   *****************************************

print('Операции над числами: \n'
      'сложение "+"\n'
      'вычитание "-"\n'
      'умножение "*"\n'
      'деление "/"\n'
      'выход и программы "0"\n')

while True:
    num_1 = int(input('Введите первое число - '))
    num_2 = int(input('Введите второе число - '))
    operation = input('Введите знак опрерации - ')

    if operation not in '+-*/0':
        print('Введен не верный знак операции!')
        operation = input('Введите знак операции - ')
        if operation in '+-*/0':
            if num_2 == 0 and operation == '/':
                print('На ноль делить нельзя!')
                continue
            elif operation == '+':
                print(f'Результат = {num_1 + num_2}')
            elif operation == '-':
                print(f'Результат = {num_1 - num_2}')
            elif operation == '*':
                print(f'Результат = {num_1 * num_2}')
            elif operation == '/':
                print(f'Результат = {num_1 / num_2}')
            elif operation == '0':
                break
        else:
            print('разрешенные знаки операции  +-*/0')
    else:
        if num_2 == 0 and operation == '/':
            print('На ноль делить нельзя!')
            continue
        elif operation == '+':
            print(f'Результат = {num_1 + num_2}')
        elif operation == '-':
            print(f'Результат = {num_1 - num_2}')
        elif operation == '*':
            print(f'Результат = {num_1 * num_2}')
        elif operation == '/':
            print(f'Результат = {num_1 / num_2}')
        elif operation == '0':
            break


# Задание № 2   *****************************************

number = input('Введите число - ')

even = []
odd = []
number = list(number)
print(number)

for n, i in enumerate(number, 1):
    if int(i) % 2 == 0:
        even.append(int(i))
    else:
        odd.append(int(i))

print(f'Количество четных чисел {len(even)} - {even}\n'
      f'Количество нечетных чисел {len(odd)} - {odd}')


# Задание № 3   *********************************************

num = input('Введите число - ')

num = list(num)
num.reverse()
num = ''.join(num)

print(num)


# Задание № 4   *********************************************

num_n = int(input('Введите число - '))
n = 1
summa = 0

for i in range(num_n):
    summa += n
    n = n / 2

print(f'Сумма = {summa}')


# Задание № 5   *********************************************

list_codes = []
for n, s in enumerate(range(96), 32):
    list_codes.append(f' {n}-{chr(n)} ')
    if len(list_codes) == 10:
        print(*list_codes, sep='')
        list_codes.clear()


# Задание № 6   *********************************************

num_rand = random.randint(1, 100)

for n, i in enumerate(range(10), 0):
    print(f'Осталось попыток - {10 - n}')
    user_num = int(input('Ваш вариант - '))
    if user_num > num_rand:
        print('Загаданное число меньше')
    elif user_num < num_rand:
        print('Загаданное число больше')
    elif user_num == num_rand:
        print(f'Вы угадали за {n + 1} попыток')
        break

print(f'\nЗагаданное число {num_rand}')


# Задание № 7   *********************************************

value = int(input('Введите длинну множества - '))
sum_value = 0

for i in range(value + 1):
    sum_value += i

if sum_value == value * (value + 1) / 2:
    print(f'Равенство выполняется\n 1+2+...+{value} = {value}({value}+1)/2\n'
          f' {sum_value} = {value}*{value + 1}/2\n'
          f' {sum_value} = {value * (value + 1)}/2\n'
          f' {sum_value} = {round(value * (value + 1) / 2)}')


# Задание № 8   *********************************************

in_num = input('Количество чисел - ')
list_num = []

for i in range(int(in_num)):
    list_num.append(input('Введите число - '))

number = int(input('Введите искомую цифру - '))
list_num = ''.join(list_num)
list_num = [int(i) for i in list_num]
print(list_num[:])
print(f'Количество искомых цифр = {list_num.count(number)}')


# Задание № 9   *********************************************

in_num = input('Введите числа через пробел - ')

list_num = in_num.split()
max_sum = 0
for i in range(len(list_num)):
    num = [int(j) for j in list_num[i]]
    if sum(num) > max_sum:
        max_sum = sum(num)
        count = list_num[i]
print(f'Число {count}, его сумма {max_sum}')
