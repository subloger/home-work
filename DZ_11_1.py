class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_num(cls, date):
        date_num = date.replace('.', ' ').replace(',', ' ').replace('/', ' ')
        date_num = date_num.split(' ')
        date_num = list(map(int, date_num))
        return print(f'День: {date_num[0]:>02} Месяц: {date_num[1]:>02} Год: {date_num[2]}')

    @staticmethod
    def date_valid(date):
        date = date.replace('.', ' ').replace(',', ' ')
        date = date.split(' ')
        while True:
            if int(date[0]) >= 32:
                print(f'Ошибка в дате - "{date[0]}"')
                break
            if int(date[1]) >= 13:
                print(f'Ошибка в дате - "{date[1]}"')
                break
            if int(date[2]) >= 9999:
                print(f'Ошибка в дате - "{date[2]}"')
                break
            else:
                break
        return print(f'Дата: {date[0]:>02}-{date[1]:>02}-{date[2]}')


Date.date_num('1.12.1235')
Date.date_valid('15.3.1235')
