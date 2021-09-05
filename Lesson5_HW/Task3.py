# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


salary_file = open("Task3.txt.", "r", encoding="UTF-8")
salary_lines = salary_file.readlines()
running_total = 0
running_count = 0
low_earners = []
for line in salary_lines:
    line_split = line.split()
    running_total += float(line_split[1])
    running_count += 1
    if float(line_split[1]) < 20000:
        low_earners.append(line_split[0])

print(
    f"Сотрудники с окдадом менее 20 тыс. руб.: {', '.join(low_earners)}. \nСредняя величина дохода сотрудников {round(running_total / running_count, 2)} руб.")
