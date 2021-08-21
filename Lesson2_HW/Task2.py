#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
generated_list = []
temp_input = input("Пожалуйста, введите целое число, чтобы добавить в список. Чтобы закончить, введите \stop >>> ")
while temp_input != "\stop":
    try:
        generated_list.append(int(temp_input))
        print(temp_input)
        temp_input = input("Пожалуйста, введите еще одно целое число. Чтобы закончить, введите \stop >>> ")
    except:
        temp_input = input("Пожалуйста, введите целое число. Чтобы закончить, введите \stop >>> ")

for i in range(len(generated_list)):
    if (i+1) % 2 == 0:
        generated_list[i - 1], generated_list[i] = generated_list[i], generated_list[i - 1]


print(generated_list)