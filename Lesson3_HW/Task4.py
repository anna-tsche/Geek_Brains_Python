# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func_algorithm(x, y):
    temp_power = 1
    for i in range(abs(y)):
        temp_power *= x
    return 1 / temp_power


def my_func_operator(x, y):
    return x ** y


real_number = 17
negative_number = -7

print(my_func_algorithm(real_number, negative_number))
print(my_func_operator(real_number, negative_number))

print(pow(real_number, negative_number))
