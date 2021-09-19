# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real) - (self.imaginary * other.imaginary),
                             (self.real * other.imaginary) + (self.imaginary * other.real))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


complex_number_1 = ComplexNumber(1, 2)
complex_number_2 = ComplexNumber(-3, -1)

print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)
