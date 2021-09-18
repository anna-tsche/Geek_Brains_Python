# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

class Clothing:

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def fabric_usage(self) -> float:
        pass


class Coat(Clothing):

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    @property
    def fabric_usage(self):
        return round(self.size/6.5 + 0.5, 2)


class Suit(Clothing):

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.height = height

    @property
    def fabric_usage(self):
        return round(2*self.height + 0.3, 2)


coat_1 = Coat("Пальто", 10)
suit_1 = Suit("Рабочий костюм", 160)

print(coat_1.fabric_usage)
print(suit_1.fabric_usage)
