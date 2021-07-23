prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

for i in range(len(prices)):                             # задание А
    num = prices[i]
    num = str(num)
    num = num.split('.')
    if len(num) == 2:
        if len(num[1]) == 1:
            num[0] = num[0] + ' руб '
            num[1] = num[1] + '0 коп'
            num = ''.join(num)
            print(num, end=', ')
        else:
            num[0] = num[0] + ' руб '
            num[1] = num[1] + ' коп'
            num = ''.join(num)
            print(num, end=', ')
    else:
        num[0] = num[0] + ' руб '
        zero = '00 коп'
        num.append(zero)
        num = ''.join(num)
        print(num, end=', ')


print()
print()
print('ID списка до сортировки - ', id(prices))          # задание В
prices.sort()
print(prices)
print('ID списка после сортировки - ', id(prices))

print()
prices.sort()                                            # задание С
prices.reverse()
prices_new = prices
print(prices_new)
print()

prices.sort()                                            # задание D
print('Самые дорогие товары - ', prices[-5:])

