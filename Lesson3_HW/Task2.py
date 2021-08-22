# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(name="не указано", surname="не указана", birth_year="не указан", city="не указан", email="не указан",
              phone_number="не указан"):
    return f'Имя: {name}' \
           f'\nФамилия: {surname}' \
           f'\nГод рождения: {birth_year}' \
           f'\nГород проживания: {city}' \
           f'\nEmail: {email} ' \
           f'\nТелефон: {phone_number}'


name_input = input("Пожалуйста, введите свое имя >>> ")
surname_input = input("Пожалуйста, введите свою фамилию >>> ")
birth_year_input = input("Пожалуйста, введите свой год рождения >>> ")
city_input = input("Пожалуйста, введите свой город проживания >>> ")
email_input = input("Пожалуйста, введите свой email >>> ")
phone_number_input = input("Пожалуйста, введите свой номер телефона >>> ")

print(user_info(name=name_input, city=city_input, surname=surname_input, birth_year=birth_year_input, email=email_input,
                phone_number=phone_number_input))
