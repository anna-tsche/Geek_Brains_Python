# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.


class Cell:

    def __init__(self, cell_number: int):
        self.cell_number = cell_number

    def __add__(self, other: "Cell"):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other: "Cell"):
        if self.cell_number - other.cell_number > 0:
            return Cell(self.cell_number - other.cell_number)
        else:
            return "Операция невозможна."

    def __mul__(self, other: "Cell"):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other: "Cell"):
        return Cell(self.cell_number // other.cell_number)

    def make_order(self, number_of_cells_in_row):
        number_of_rows = self.cell_number // number_of_cells_in_row
        residual = self.cell_number % number_of_cells_in_row
        order = ""
        for i in range(number_of_rows):
            order += f"{'*' * number_of_cells_in_row}\n"
        if residual != 0:
            order += f"{'*' * residual}\n"

        return f"Организация ячеек по {number_of_cells_in_row} в ряду:\n{order}"

    def __str__(self):
        return f"Число ячеек {self.cell_number}"


cell_1 = Cell(13)
cell_2 = Cell(17)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_1.make_order(4))
