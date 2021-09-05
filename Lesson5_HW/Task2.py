# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


working_file = open("Task2.txt", "r")
file_lines = working_file.readlines()
number_of_lines = 0
for line in range(len(file_lines)):
    print(f"В строке номер {line + 1} содержится {len(file_lines[line].split(' '))} слов(о).")
    number_of_lines += 1

print(f"Всего в файле {number_of_lines} строк(и).")

working_file.close()
