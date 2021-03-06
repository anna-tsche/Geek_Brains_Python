# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_from_input():
    stop_command = False
    rolling_sum = 0
    while not stop_command:
        user_input = input("Пожалуйста, введите строку чисел, разделенных пробелом. Чтобы закончить, напишите stop >>> ")
        input_list = user_input.split(" ")
        for element in input_list:
            if element != "stop":
                try:
                    rolling_sum += int(element)
                except ValueError:
                    pass
            else:
                stop_command = True
        print(rolling_sum)


sum_from_input()
