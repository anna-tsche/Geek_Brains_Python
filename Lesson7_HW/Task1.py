# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, matrix: list[list]):
        self.matrix = matrix

        self.matrix_row_number = len(matrix)

        self.matrix_column_number = set((len(row)) for row in self.matrix)
        if len(self.matrix_column_number) != 1:
            raise TypeError("Объект не является матрицей.")

        self.matrix_size = (self.matrix_row_number, self.matrix_column_number.pop())

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other: "Matrix"):
        if self.matrix_size != other.matrix_size:
            raise ValueError("Матрицы разных размеров невозможно сложить.")
        else:
            resulting_matrix = []
            for number in zip(self.matrix, other.matrix):
                resulting_matrix.append([sum([j, k]) for j, k in zip(*number)])
            return Matrix(resulting_matrix)


my_matrix = Matrix([[1, 1, 0], [0, 0, 0], [1, 1, 1]])
my_second_matrix = Matrix([[0, 0, 1], [1, 1, 1], [0, 0, 0]])
print(f"Исходная матрица:"
      f"\n{my_matrix}\n"
      f"Матрица для сложения:"
      f"\n{my_second_matrix}")

print(f"Результат сложения матриц:"
      f"\n{(my_matrix+my_second_matrix)}")
