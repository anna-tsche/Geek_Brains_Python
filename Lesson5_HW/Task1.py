# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


file_name = "task1_file.txt"
file_content = open(file_name, "w")
stop_command = False
while not stop_command:
    input_text = input(
        "Введите текст для добавления в файл, для окончания ввода введите пустую строку (нажмите Enter без ввода строки) >>> ")
    if input_text == "":
        stop_command = True
        break
    else:
        file_content.write(f"{input_text}\n")
file_content.close()
