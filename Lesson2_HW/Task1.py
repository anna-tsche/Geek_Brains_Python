#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

class RandomClass:
    pass


def function_type():
    pass


random_list = [42, 42.0, 42_1j, "String", None, True, range(0, 3), [1, 1, 2, 3, 5, 8, 13],
               (1, 1, 2, 3, 5, 8, 13), {1, 2, 3, 5, 8, 13}, {"Yes": 1, "No": 0}, function_type, RandomClass,
               Exception(), b'\x00\x00', bytearray(b'\x01\x01\x02\x03\x05\x08\r')]


def check_type(input_list):
    for element in input_list:
        print(type(element))


check_type(random_list)
