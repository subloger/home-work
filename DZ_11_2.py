class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Первое число: 100')

try:
    num = int(input('Введите делитель - '))
    if num == 0:
        raise ZeroDiv("Ошибка: Вы пытаетесь делить на ноль")
except ZeroDiv as e:
    print(e)
else:
    result = 100 / num
    print(round(result, 2))
