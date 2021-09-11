from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, parametr):
        self.name = name
        self.parametr = parametr
        print(f'Я - {self.name}. Меня разработали лучшие дизайнеры')

    def __add__(self, other):
        return self.total_cloth + other.total_cloth

    def __str__(self):
        return f'Расход ткани на {self.name} составит {self.total_cloth}'

    @abstractmethod
    def total_cloth(self):
        pass


class Coat(Clothes):
    @property
    def total_cloth(self):
        return round((self.parametr / 6.5 + 0.5), 2)


class Suit(Clothes):
    @property
    def total_cloth(self):
        return round((2 * self.parametr + 0.3) / 100, 2)


cloth_1 = Coat('пальто', 67)
cloth_2 = Suit('костюм', 280)
print(cloth_1)
print(cloth_2)
print(cloth_1 + cloth_2)