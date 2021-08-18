class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'Manager'
    _income = {'wage': 100, 'bonus': 10}


class Position(Worker):

    def get_full_name(self):
        print(f'ФИО: {Worker.name} {Worker.surname}')

    def get_total_income(self):
        num = Worker._income
        print(f'Доход: {num["wage"] + num["bonus"]}')


f_name = Position()
f_name.get_full_name()
f_name.get_total_income()
