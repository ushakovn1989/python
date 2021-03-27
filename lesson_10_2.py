from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size/6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def fabric_consumption(self):
        return round(2*self.growth + 0.3, 2)


coat = Coat(48)
suit = Suit(1.69)
print(coat.fabric_consumption + suit.fabric_consumption)
