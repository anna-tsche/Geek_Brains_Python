# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

def get_wares_data():
    name = input("Пожалуйста, введите название товара >>> ")
    price = input("Пожалуйста, введите цену товара >>> ")
    quantity = input("Пожалуйста, введите количество товара >>> ")
    units = input("Пожалуйста, введите единицу измерения товара >>> ")
    return {
        "название": name,
        "цена": price,
        "количество": quantity,
        "eд": units
    }


resulting_list = []
current_index = 1
command = ''

while command != "stop":
    command = input("Введите add чтобы добавить товар или stop чтобы получить отчет >>> ")
    if command == "add":
        resulting_list.append((current_index, get_wares_data()))
        current_index += 1
    if command == "stop":
        print(resulting_list)
        analytics = {
            "название": [],
            "цена": [],
            "количество": [],
            "eд": []
        }
        for item in resulting_list:
            current_data = item[1]
            analytics["название"].append(current_data["название"])
            analytics["цена"].append(current_data["цена"])
            analytics["количество"].append(current_data["количество"])
            analytics["eд"].append(current_data["eд"])
        print(analytics)


