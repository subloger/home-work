list_1 = ['в', '"5"', 'часов', '"17"', 'минут', 'температура',
          'воздуха', 'была', '"+5"', 'градусов']
list_2 = []

for i in range(len(list_1)):
    n = list_1[i]
    if n.isdigit() is True or '+' in n:
        if '+' in n:
            n = n.replace('+', '12')
            n = n.replace('1', '+')
            n = n.replace('2', '0')
            list_2.append(n)
        else:
            a = f'{n:>02}'
            list_2.append(a)
    else:
        list_2.append(n)

for i in range(len(list_2)):
    print(list_2[i], end=' ')
