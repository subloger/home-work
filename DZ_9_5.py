class Stationery:
    title = 'pen'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Зауск отрисовки Карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Маркером')


s = Stationery()
s.draw()
p = Pen()
p.draw()
pen = Pen()
pen.draw()
h = Handle()
h.draw()
