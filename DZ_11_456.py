import os
import random
from abc import abstractmethod


class Storage:
    quantity = dict({'Printer': 0, 'Scanner': 0, 'Xerox': 0})
    departments = dict({'Accounting': {'Printer': 0, 'Scanner': 0, 'Xerox': 0},
                        'Sales_dep': {'Printer': 0, 'Scanner': 0, 'Xerox': 0}})

    @staticmethod
    def to_storage():
        name = input('Оборудование - ')
        count = int(input('Количество - '))
        if name == 'P':
            print(f'Printer: {count}шт помещен на склад...''\n')
            Storage.quantity['Printer'] += int(count)

        elif name == 'S':
            print(f'Scanner: {count}шт помещен на склад...''\n')
            Storage.quantity['Scanner'] += int(count)

        elif name == 'X':
            print(f'Xerox: {count}шт помещен на склад...''\n')
            Storage.quantity['Xerox'] += int(count)
        else:
            print('Введите правильное обозначение добавляемого оборудования')

    @staticmethod
    def record():
        list_1 = [str(Storage.quantity[num]) for num in Storage.quantity]
        list_2 = [str(Storage.departments['Accounting'][nom]) for nom in Storage.departments['Accounting']]
        list_3 = [str(Storage.departments['Sales_dep'][nom]) for nom in Storage.departments['Sales_dep']]
        str_1 = ','.join(list_1 + list_2 + list_3)
        with open('Storage.txt', 'a', encoding='utf-8') as f:
            str_2 = str_1 + '\n'
            f.writelines(str_2)

        print('Данные о состоянии склада сохранены!')
        print()

    @staticmethod
    def load():
        if os.path.exists('Storage.txt'):
            with open('Storage.txt', 'r', encoding='utf-8') as f:
                str_1 = f.readlines()
                str_2 = str_1[-1]
                str_1 = str_2.replace(',', ' ').split()
                list_1 = list(map(int, str_1))
                Storage.quantity['Printer'] = list_1[0]
                Storage.quantity['Scanner'] = list_1[1]
                Storage.quantity['Xerox'] = list_1[2]
                Storage.departments['Accounting']['Printer'] = list_1[3]
                Storage.departments['Accounting']['Scanner'] = list_1[4]
                Storage.departments['Accounting']['Xerox'] = list_1[5]
                Storage.departments['Sales_dep']['Printer'] = list_1[6]
                Storage.departments['Sales_dep']['Scanner'] = list_1[7]
                Storage.departments['Sales_dep']['Xerox'] = list_1[8]
                print('Данные о состоянии склада загружены!')
                print()
        else:
            print('Нет файла для загрузки! Сначала сохраните состояние склада!')

    @staticmethod
    def show_item():
        print('\n'f'Количество единиц оборудования на складе')
        print('-' * 40)
        print(f'Printer: {Storage.quantity["Printer"]} шт''\n'
              f'Scanner: {Storage.quantity["Scanner"]} шт''\n'
              f'Xerox: {Storage.quantity["Xerox"]} шт')
        print('\n'f'Количество единиц оборудования в отделах')
        print('-' * 40)
        print(f'Бухгалтерия:  Printer - {Storage.departments["Accounting"]["Printer"]} '
              f'Scanner - {Storage.departments["Accounting"]["Scanner"]} '
              f'Xerox - {Storage.departments["Accounting"]["Xerox"]}''\n'
              f'Отдел продаж: Printer - {Storage.departments["Sales_dep"]["Printer"]} '
              f'Scanner - {Storage.departments["Sales_dep"]["Scanner"]} '
              f'Xerox - {Storage.departments["Sales_dep"]["Xerox"]}')

    @staticmethod
    def relocation():
        name = input('Введите отдел для передачи оборудования - ')
        if name == 'A':
            print('Передать бухгалтерии...')
            print('-' * 23)
            p = int(input('Принтер: шт - '))
            s = int(input('Сканнер: шт - '))
            x = int(input('Ксерокс: шт - '))
            print()
            if Storage.quantity['Printer'] > 0:
                Storage.quantity['Printer'] -= int(p)
                Storage.departments['Accounting']['Printer'] += int(p)
            else:
                print(f'На складе закончилось оборудование! Printer: {Storage.quantity["Printer"]}')
            if Storage.quantity['Scanner'] > 0:
                Storage.quantity['Scanner'] -= int(s)
                Storage.departments['Accounting']['Scanner'] += int(s)
            else:
                print(f'На складе закончилось оборудование! Scanner: {Storage.quantity["Scanner"]}')
            if Storage.quantity['Xerox'] > 0:
                Storage.quantity['Xerox'] -= int(x)
                Storage.departments['Accounting']['Xerox'] += int(x)
            else:
                print(f'На складе закончилось оборудование! Xerox: {Storage.quantity["Xerox"]}')
        elif name == 'S':
            print('Передать в отдел закупок...')
            print('-' * 40)
            p = int(input('Принтер: шт - '))
            s = int(input('Сканнер: шт - '))
            x = int(input('Ксерокс: шт - '))
            print()
            if Storage.quantity['Printer'] > 0:
                Storage.quantity['Printer'] -= int(p)
                Storage.departments['Sales_dep']['Printer'] += p
            else:
                print(f'На складе закончилось оборудование! Printer: {Storage.quantity["Printer"]}')
            if Storage.quantity['Printer'] > 0:
                Storage.quantity['Scanner'] -= int(s)
                Storage.departments['Sales_dep']['Scanner'] += s
            else:
                print(f'На складе закончилось оборудование! Scanner: {Storage.quantity["Scanner"]}')
            if Storage.quantity['Printer'] > 0:
                Storage.quantity['Xerox'] -= int(x)
                Storage.departments['Sales_dep']['Xerox'] += x
            else:
                print(f'На складе закончилось оборудование! Xerox: {Storage.quantity["Xerox"]}')
        else:
            print('Введите правильное обозначение отдела!')

    @staticmethod
    def help():
        print(f'Основные команды:''\n'
              f'-----------------''\n'
              f'"help" - справка о командах''\n'
              f'"add"  - добавить оборудование на склад (P - Принтер, S - Сканер, X - Ксерокс)''\n'
              f'"show" - покзать количество оборудования на складе''\n'
              f'"rec"  - запись состояния склада в файл''\n'
              f'"load" - загрузка состояния склада из файла''\n'
              f'"rloc" - перемещение в отделы (A - Бухгалтерия, S - Отдел продаж)''\n'
              f'"stat" - статистика по складу''\n'
              f'"ex"   - выход''\n'
              f'''\n'''
              f'ВНИМАНИЕ!!! Перед началом работы введите команду "load", для загрузки даных склада!''\n'
              f'Перед завершеним работы сохраните данные командой "rec" !')
        print()


class OfficeEquip:
    @abstractmethod
    def __init__(self, company, color):
        self.company = company
        self.color = color


class Printer(OfficeEquip):
    def __init__(self, company, color):
        super().__init__(company, color)

    @staticmethod
    def stat_print():
        color = ['Black', 'White', 'Grey']
        company = 'PrintMagic'
        speed_of_print = [100, 150, 200]
        method_of_print = ['Laser', 'Inkjet']
        count_of_print = Storage.quantity.copy()
        if count_of_print['Printer'] > 0:
            return print('\n'f'Информация о принтерах на складе:''\n'
                         f'---------------------------------''\n'
                         f'количество:                 {count_of_print["Printer"]}''\n'
                         f'производитель:              {company}''\n'
                         f'цвет:                       {random.choice(color)}''\n'
                         f'скорость печати листов/мин: {random.choice(speed_of_print)}''\n'
                         f'категория:                  {random.choice(method_of_print)}')
        else:
            print('На складе нет принтеров!')


class Scanner(OfficeEquip):
    def __init__(self, company, color):
        super().__init__(company, color)

    @staticmethod
    def stat_scan():
        color = ['Black', 'White', 'Grey']
        company = 'ScanMagic'
        dpi = [1000, 1500, 2000]
        count_of_print = Storage.quantity.copy()
        if count_of_print['Scanner'] > 0:
            return print('\n'f'Информация о сканнерах на складе:''\n'
                         f'---------------------------------''\n'
                         f'количество:                 {count_of_print["Scanner"]}''\n'
                         f'производитель:              {company}''\n'
                         f'цвет:                       {random.choice(color)}''\n'
                         f'разрешение точек/дюйм:      {random.choice(dpi)}')
        else:
            print('На складе нет сканнеров!')


class Xerox(OfficeEquip):
    def __init__(self, company, color):
        super().__init__(company, color)

    @staticmethod
    def stat_xerox():
        color = ['Black', 'White', 'Grey']
        company = 'SuperXerox'
        speed_copy = [1000, 1500, 2000]
        count_of_print = Storage.quantity.copy()
        if count_of_print['Xerox'] > 0:
            return print('\n'f'Информация о ксероксах на складе:''\n'
                         f'---------------------------------''\n'
                         f'количество:                      {count_of_print["Xerox"]}''\n'
                         f'производитель:                   {company}''\n'
                         f'цвет:                            {random.choice(color)}''\n'
                         f'скорость копирования листов/мин: {random.choice(speed_copy)}')
        else:
            print('На складе нет ксероксов!')


print('-' * 44)
print('Для ознакомления с коммандами введите "help"')
while True:
    try:
        command = input('|> ')
        if command == 'add':
            Storage.to_storage()
        elif command == 'show':
            Storage.show_item()
        elif command == 'rec':
            Storage.record()
        elif command == 'load':
            Storage.load()
        elif command == 'rloc':
            Storage.relocation()
        elif command == 'stat':
            Printer.stat_print()
            Scanner.stat_scan()
            Xerox.stat_xerox()
        elif command == 'help':
            Storage.help()
        elif command == 'ex':
            break
    except ValueError as e:
        print()
        print('КОЛИЧЕСТВО НАДО ВВОДИТЬ ЦИФРАМИ!!!')
        print()
