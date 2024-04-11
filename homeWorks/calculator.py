class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль недопустимо")
        return self.value / other.value


num1 = Calculator(10)
num2 = Calculator(5)

print("Сложение:", num1 + num2)
print("Вычитание:", num1 - num2)
print("Умножение:", num1 * num2)
print("Деление:", num1 / num2)
