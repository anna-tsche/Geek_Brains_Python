# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*arguments):
    my_set = sorted(list(*arguments), reverse=True)
    return my_set[0] + my_set[1]


arguments_for_check = (1, 8, 2)
print(my_func(arguments_for_check))
