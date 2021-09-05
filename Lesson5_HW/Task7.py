# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


import json


companies_dict = {}
average_profit = {}

with open("Task7.txt", "r", encoding="UTF-8") as companies_list:
    profitable_companies = 0
    profitable_companies_profit = 0
    for line in companies_list:
        company, type, revenue, cost = line.split()
        profit = float(revenue) - float(cost)
        if profit > 0:
            profitable_companies += 1
            profitable_companies_profit += profit
        companies_dict[company] = profit
    average_profit["average_profit"] = round(profitable_companies_profit / profitable_companies, 2)

resulting_list = [companies_dict, average_profit]

print(resulting_list)

with open("Task7.json", "w", encoding="UTF-8") as json_write:
    json.dump(resulting_list, json_write)
