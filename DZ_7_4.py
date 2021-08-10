import os


list_of_files = []
dict_size_of_files = {100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0, 10000000: 0}
error = 0
num_100 = 0
num_1000 = 0
num_10000 = 0
num_100000 = 0

for folder in os.walk(os.getcwd()):
    for i in range(len(folder[2])):
        list_of_files.append(folder[2][i])
        try:
            if os.stat(list_of_files[i]).st_size <= 100:
                num_100 += 1
                dict_size_of_files[100] = num_100
            elif 100 < os.stat(list_of_files[i]).st_size <= 1000:
                num_1000 += 1
                dict_size_of_files[1000] = num_1000
            elif 1000 < os.stat(list_of_files[i]).st_size <= 10000:
                num_10000 += 1
                dict_size_of_files[10000] = num_10000
            elif 10000 < os.stat(list_of_files[i]).st_size <= 100000:
                num_100000 += 1
                dict_size_of_files[100000] = num_100000
            elif 100000 < os.stat(list_of_files[i]).st_size <= 1000000:
                num_100000 += 1
                dict_size_of_files[1000000] = num_100000
            elif 1000000 < os.stat(list_of_files[i]).st_size <= 10000000:
                num_100000 += 1
                dict_size_of_files[10000000] = num_100000
        except FileNotFoundError as e:
            error += 1

print(dict_size_of_files)
print(f'Количество файлов всего: {len(list_of_files)}')
print(f'Файлов размером 100 байт: {dict_size_of_files[100]} шт.')
print(f'Файлов размером 1000 байт: {dict_size_of_files[1000]} шт.')
print(f'Файлов размером 10.000 байт: {dict_size_of_files[10000]} шт.')
print(f'Файлов размером 100.000 байт: {dict_size_of_files[100000]} шт.')
print(f'Файлов размером 1000.000 байт: {dict_size_of_files[1000000]} шт.')
print(f'Файлов размером 10.000.000 байт: {dict_size_of_files[10000000]} шт.')
print(f'Найдено файлов всего: {dict_size_of_files[100] + dict_size_of_files[1000] + dict_size_of_files[10000]}')
print(f'Файлов не найдено: {error}')

