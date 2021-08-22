# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Деление на ноль невозможно:("
    except ValueError:
        return "Вы ввели не число!"


numerator_input = input("Пожалуйста введите числитель для деления >>> ")
denominator_input = input("Пожалуйста введите знаменатель для деления >>> ")

division_result = division(numerator_input, denominator_input)
print(f'Результат деления {division_result}')
