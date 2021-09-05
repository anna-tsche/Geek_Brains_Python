# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


numbers_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("Task4_initial.txt", encoding="UTF-8") as initial_file:
    with open("Task4_new.txt", "x", encoding="UTF-8") as new_file:
        for line in initial_file:
            line = line.split(' ')
            new_file.writelines(numbers_dictionary[line[0]] + " - " + line[-1])
