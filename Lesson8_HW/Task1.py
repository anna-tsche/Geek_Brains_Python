# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


import datetime


class Date:

    def __init__(self, date_string: str):
        self.date_string = date_string

    def __str__(self):
        return f"Введенная дата: {self.date_string}."

    @classmethod
    def date_split(cls, date_string: str):
        day = int(date_string.split('-')[0])
        month = int(date_string.split('-')[1])
        year = int(date_string.split('-')[2])
        return cls.validation(day, month, year, date_string)

    @staticmethod
    def validation(day, month, year, date_string: str):
        try:
            datetime.date(year, month, day)
            return f"Введенная дата: {date_string} валидна."
        except ValueError:
            return f"Введенная дата: {date_string} не валидна."


date_1 = Date('15-14-2020')
date_2 = Date.date_split('29-02-2021')
date_3 = Date.date_split('15-04-2020')
print(date_1)
print(date_2)
print(date_3)
