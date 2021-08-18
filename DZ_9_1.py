import time


class TrafficLight:
    _color = 'red'

    def running(self, text_1, text_2, text_3):
        while True:
            print(f'\033[31m{text_1}')
            time.sleep(7)
            print(f'\033[33m{text_2}')
            time.sleep(2)
            print(f'\033[32m{text_3}')
            time.sleep(5)


light = TrafficLight()
light.running('Red', 'Yellow', 'Green')
