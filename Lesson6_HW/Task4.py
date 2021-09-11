# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    is_police: bool

    def go(self):
        return f"{self.name} тронулась."

    def stop(self):
        return f"{self.name} остановилась."

    def turn_right(self):
        return f"{self.name} повернула направо."

    def turn_left(self):
        return f"{self.name} повернула налево."

    def show_speed(self):
        return f"Текущая скорость {self.name} составляет {self.speed}."


class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            return f"Текущая скорость {self.name} составляет {self.speed}. {self.name} превышает скорость."
        else:
            return f"Текущая скорость {self.name} составляет {self.speed}."


class SportCar(Car):
    is_police = False


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            return f"Текущая скорость {self.name} составляет {self.speed}. {self.name} превышает скорость."
        else:
            return f"Текущая скорость {self.name} составляет {self.speed}."


class PoliceCar(Car):
    is_police = True


porsche = SportCar(200, "красный", "Porsche")
skoda = TownCar(30, "белый", "Skoda")
kia = WorkCar(80, "красный", "Kia")
mercedes = PoliceCar(130, "черный", "Mercedes")


print(porsche.go())
print(f"Цвет {mercedes.name} - {mercedes.color}.")
print(f"{skoda.name} полицейская машина: {skoda.is_police}.")
print(kia.show_speed())
