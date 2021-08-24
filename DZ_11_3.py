class TypeData(Exception):
    def __init__(self, txt):
        self.txt = txt


list_of_num = []
while True:
    try:
        num = input('Введите число - ')
        if num == 'stop':
            print(f'Список занчений: {list_of_num}')
            break
        verify = num.isdigit()
        if verify is False:
            raise TypeData('Введенное значение не является числом')
    except TypeData as err:
        print(err)
    else:
        list_of_num.append(int(num))
