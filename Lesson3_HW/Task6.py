# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


# Так как из условия непонятно, можно ли использовать в написанной функции встроеннуые функции Python
# для работы со строками, я дополнительным шагом создаю словать с заглавными буквами.
def upper_dict():
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    letter_dictionary_upper = {}
    for letter in english_letters:
        letter_dictionary_upper[letter] = letter.upper()
    return letter_dictionary_upper


dictionary = upper_dict()


def capitalize_word(word):
    try:
        first_letter = dictionary[word[0]]
        other_letters = word[1:]
        new_word = first_letter + other_letters
        return new_word
    except KeyError:
        return "<Вы ввели недопустимый символ.>"


def capitalize_all_words(sentence):
    iterable_list = sentence.split(" ")
    capitalized_list = []
    for word in iterable_list:
        capitalized_list.append(capitalize_word(word))
    return " ".join(capitalized_list)


word_input = input("Введите слово латиницей >>> ").strip()
sentence_input = input("Введите предложение латиницей >>> ").strip()
print(capitalize_word(word_input))
print(capitalize_all_words(sentence_input))
