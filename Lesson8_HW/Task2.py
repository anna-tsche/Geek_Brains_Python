# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class CustomZeroDivisionError(Exception):
    error_message = "Деление на ноль невозможно!"

    def __str__(self):
        return self.error_message


def try_division():
    numerator = int(input("Введите числитель >>> "))
    denominator = int(input("Введите знаменатель >>> "))
    if denominator == 0:
        raise CustomZeroDivisionError
    result = float(numerator / denominator)
    print(f"Результат деления: {numerator} на {denominator}: {result}")


try_division()
