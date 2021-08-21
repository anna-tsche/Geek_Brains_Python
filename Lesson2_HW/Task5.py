# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

initial_list = [20, 15, 12, 9, 5, 2]


def input_rating():
    try:
        result = int(input("Пожалуйста, введите рейтинг (целое число) >>> "))
    except:
        print("Вы ввели не число!")
        result = input_rating()
    return result


new_rating = input_rating()
first = 0
last = len(initial_list) - 1

if new_rating > initial_list[0]:
    initial_list.insert(0, new_rating)
else:
    while first <= last:
        pos = 0
        midpoint = (first + last) // 2
        if initial_list[midpoint] == new_rating or first - last == 0:
            pos = midpoint
            initial_list.insert(pos, new_rating) if new_rating > initial_list[midpoint] else initial_list.insert(
                pos + 1, new_rating)
            break
        else:
            if new_rating > initial_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

print(initial_list)
