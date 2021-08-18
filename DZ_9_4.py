import random


class Car:
    def __init__(self, color, name, speed, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        list_1 = ['лево', 'право']
        direction = random.choice(list_1)
        print(f'Автомобиль {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed} км')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60} км')
        else:
            print(f'Скорость автомобиля {self.speed} км')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40} км')
        else:
            print(f'Скорость автомобиля {self.speed} км')


class PoliceCar(Car):
    pass


town = TownCar('Red', 'Pontiac', 150)
town.go()
town.turn()
town.show_speed()
town.stop()
