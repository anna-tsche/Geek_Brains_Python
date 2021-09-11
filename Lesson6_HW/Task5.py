# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print("Вы пишете ручкой.")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print("Вы чертите карандашом.")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print("Вы рисуете фломастером.")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
