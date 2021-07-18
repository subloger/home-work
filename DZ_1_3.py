num = int(input('Ведите число процентов - '))

for i in range(1, num + 1):
    if i == 1 or i > 20 and i % 10 == 1:
        print(i, 'процент')
    elif 2 <= i < 5 or i > 20:
        if 2 <= i % 10 <= 4:
            print(i, 'процента')
        elif i > 20:
            print(i, 'процентов')
    elif 5 <= i <= 20:
        print(i, 'процентов')
