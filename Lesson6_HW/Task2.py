# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    _width: float
    _length: float

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_asphalt_mass(self, thickness):
        asphalt_mass = self._length * self._width * 25 * thickness
        return f"Необходимая масса асфальта {asphalt_mass} кг"


road_instance = Road(20, 5000)
print(road_instance.calculate_asphalt_mass(5))