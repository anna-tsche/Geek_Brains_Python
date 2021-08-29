# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle


def iterator_count(starting_number, stop_number):
    for number in count(starting_number):
        if number > stop_number:
            break
        else:
            print(number)


iterator_count(3, 10)
print("\n")

initial_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]


def iterator_cycle(some_list, iterations):
    counter = 0
    for element in cycle(some_list):
        if counter >= iterations:
            break
        else:
            print(element)
            counter += 1


iterator_cycle(initial_list, 16)
