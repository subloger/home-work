import cProfile
import random


# Задание № 1   ************************************************

def print_code():
    rand_list = []
    for i in range(10000):
        rand_list.append(random.randint(1, 10))

    min_list = min(rand_list)
    max_list = max(rand_list)

    for j in range(len(rand_list)):
        if rand_list[j] == min_list:
            rand_list[j] = max_list
        elif rand_list[j] == max_list:
            rand_list[j] = min_list


cProfile.run('print_code()')

# при изменении количества итераций в первом цикле в 10 раз, время выполнения алгоритма
# увеличивается также в 10 раз, из этого можно предположить, что алгоритм обладает
# линейной сложностью

# 65974 function calls in 0.021 seconds   - при 10000  итераций
# 659499 function calls in 0.202 seconds  - при 100000 итераций
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.202    0.202 <string>:1(<module>)
#    100000    0.050    0.000    0.115    0.000 random.py:200(randrange)
#    100000    0.027    0.000    0.142    0.000 random.py:244(randint)
#    100000    0.046    0.000    0.065    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.049    0.049    0.201    0.201 sample.py:6(print_code)
#         1    0.000    0.000    0.202    0.202 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.min}
#    100000    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    159492    0.012    0.000    0.012    0.000 {method 'getrandbits' of '_random.Random' objects}


# Задание № 2   ************************************************

num_list = []
prime_list = []
num = int(input('Введите число - '))


def list_num():
    for i in range(2, 10000):
        num_list.append(i)


def prime_lst():
    n = 2
    while len(prime_list) != num:
        for j in range(2, len(num_list)):
            if n * j in num_list:
                num_list.remove(n * j)
        n += 1
        if num_list[n-3] != 0:
            prime_list.append(num_list[n-3])
            print(len(prime_list))
        if len(prime_list) == num:
            print(f'{num} = {prime_list[-1]}')
            break


def main():
    list_num()
    prime_lst()


cProfile.run('main()')

# 15009 function calls in 0.627 seconds   1 число
# 17982 function calls in 1.518 seconds   10 число
# 19374 function calls in 3.818 seconds   100 число
# 24774 function calls in 20.872 seconds  1000 число
#
#   Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   20.711   20.711 <string>:1(<module>)
#      1    0.001    0.001    0.002    0.002 sample.py:10(list_num)
#      1   20.468   20.468   20.709   20.709 sample.py:15(prime_lst)
#      1    0.000    0.000   20.711   20.711 sample.py:30(main)
#      1    0.000    0.000   20.711   20.711 {built-in method builtins.exec}
#   4000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   1001    0.022    0.000    0.022    0.000 {built-in method builtins.print}
#  10998    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   # 8769    0.217    0.000    0.217    0.000 {method 'remove' of 'list' objects}


num_1 = int(input('Введите число - '))
list_num_1 = []
prime_list_1 = []


def prime_num():
    n = 2
    while True:
        list_num_1.append(n)
        for i in list_num_1:
            if n % i == 0:
                prime_list_1.append(n)
                if prime_list_1.count(i) > 1:
                    while i in prime_list_1:
                        prime_list_1.remove(i)
        if len(prime_list_1) == num_1:
            print(prime_list_1[-1])
            break
        n += 1


cProfile.run('prime_num()')

# 9 function calls in 0.000 seconds  - нахождение 1 числа
# 273 function calls in 0.000 seconds  - нахождение 10 числа
# 9847 function calls in 0.015 seconds  - нахождение 100 числа
# 207972 function calls in 2.716 seconds  - нахождение 1000 числа
# 3565599 function calls in 532.232 seconds - нахождение 10000 числа

#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000  532.232  532.232 <string>:1(<module>)
#       1  342.166  342.166  532.232  532.232 sample.py:10(prime_num)
#       1    0.000    0.000  532.232  532.232 {built-in method builtins.exec}
#  104728    0.061    0.000    0.061    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
# 1226774    0.221    0.000    0.221    0.000 {method 'append' of 'list' objects}
# 1122046  101.854    0.000  101.854    0.000 {method 'count' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1112046   87.931    0.000   87.931    0.000 {method 'remove' of 'list' objects}
