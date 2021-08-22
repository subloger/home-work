from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def cloth(self):
        pass

    def __add__(self, other):
        result = self.cloth() + other.cloth()
        return result


class Coat(Clothes):
    def cloth(self):
        return (self.param / 6.5) + 0.5


class Suit(Clothes):
    def cloth(self):
        return ((2 * self.param) + 0.3) / 100


coat = Coat(42)
suit = Suit(175)
print(round(coat + suit, 2))
