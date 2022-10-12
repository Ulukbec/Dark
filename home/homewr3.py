class Calculator:
    num1 = int(input("Вводите цифру :"))
    num2 = int(input("Вводите цифру :"))

    def __init__(self, number_1=num1, number_2=num2):
        self.number1 = number_1
        self.number2 = number_2


class Add(Calculator):
    def __add__(self):
        return self.number1 + self.number2


class Sub(Calculator):
    def __sub__(self):
        return self.number1 - self.number2


class Mull(Calculator):
    def __mul__(self):
        return self.number1 * self.number2


class Truediv(Calculator):
    def __truediv__(self):
        return round(self.number1 / self.number2)


cal = Sub()
print(abs(cal.__sub__()))

add = Add()
print(add.__add__())

mul = Mull()
print(mul.__mul__())

tru = Truediv()
print(tru.__truediv__())
