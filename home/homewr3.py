class Add:
    def __init__(self, number1):
        self.number1 = number1


    def __add__(self, other):
        return self.number1 + other.number1


class Sub:
    def __init__(self, number1):
        self.number1 = number1


    def __sub__(self, other):
        return self.number1 - other.number1


class Mull:
    def __init__(self, number1):
        self.number1 = number1


    def __mul__(self, other):
        return self.number1 * other.number1


class Truediv:
    def __init__(self, number1):
        self.number1 = number1

    def __truediv__(self, other):
        return round(self.number1 / other.number1, 4)


class Calculator(Add, Sub, Mull, Truediv):
    def __init__(self, number1):
        super().__init__(number1)


# Add.__init__(self, number1, number2)
# Sub.__init__(self, number1, number2)
# Mull.__init__(self, number1, number2)
# Truediv.__init__(self, number1, number2)


first = Calculator(34767)
second = Calculator(34)

print(first / second)
