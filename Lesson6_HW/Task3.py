# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _income = [{"name_surname": "Иван Иванов", "wage": 100, "bonus": 10},
               {"name_surname": "Петр Петров", "wage": 110, "bonus": 0},
               {"name_surname": "Иван Сидоров", "wage": 90, "bonus": 100}]


class Position(Worker):
    def __init__(self, name, surname, position, income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.get_total_income()

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        for employee in Worker._income:
            if employee["name_surname"] == self.get_full_name():
                return employee["wage"] + employee["bonus"]

    @property
    def income(self):
        return self._income


ivanov = Position("Иван", "Иванов", "Стажер")
sidorov = Position("Иван", "Сидоров", "Генеральный директор")


def get_person_info(employee):
    print(f"{employee.get_full_name()}, {employee.position}, зарплата с учетом премии {employee.income}")


get_person_info(ivanov)
get_person_info(sidorov)
