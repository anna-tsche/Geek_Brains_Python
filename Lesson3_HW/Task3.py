# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*arguments):
    my_set = sorted(list(arguments), reverse=True)
    return my_set[0] + my_set[1]


# Ниже поиск минимального элемента реализован циклом, я хотела написать без использования встроенной фиункции min().
# Это должно быть быстрее, чем решение с сортировкой.
def my_func_alternative(*arguments):
    min_element = arguments[0]
    sum_elements = min_element
    for element in arguments[1:]:
        if element < min_element:
            min_element = element
        sum_elements += element
    return sum_elements - min_element


arg1 = 3
arg2 = 8
arg3 = 12
print(my_func(arg1, arg2, arg3))
print(my_func_alternative(arg1, arg2, arg3))
