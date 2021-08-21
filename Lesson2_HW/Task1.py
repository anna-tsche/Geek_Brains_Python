class RandomClass:
    pass


random_list = [42, 42.0, "String", None, True, [1, 1, 2, 3, 5, 8, 13],
               (1, 1, 2, 3, 5, 8, 13), {"Yes": 1, "No": 0}, RandomClass, RandomClass()]


def check_type(input_list):
    for element in input_list:
        print(type(element))


check_type(random_list)
