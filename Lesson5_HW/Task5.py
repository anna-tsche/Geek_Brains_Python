# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def summary():
    try:
        with open("Task5.txt", "w+") as file_for_sum:
            numbers = input("Введите числа через пробел >>> ")
            file_for_sum.writelines(numbers)
            input_sum = 0
            for number in numbers.strip().split():
                input_sum += float(number)
            print(input_sum)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    except ValueError:
        print("Вы вводите не число.")
        summary()


summary()
