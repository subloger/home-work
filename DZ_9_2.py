class Road:

    def __init__(self, depth, le, w):
        self._length = le
        self._width = w
        mass = 25
        print(f'Требуемая масса асфальта '
              f'{round((self._length * self._width * mass * depth) / 1000)} тонн')


road_mass = Road(5, 1000, 20)
