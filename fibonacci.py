from math import sqrt


class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibonacci_number = self.a
        self.a, self.b = self.b, self.a + self.b
        return fibonacci_number


class FibonacciFormula:
    @staticmethod
    def calculate(n):
        return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) // (2**n * sqrt(5)))


if __name__ == "__main__":
    fibonacci_gen = FibonacciGenerator()
    fibonacci_formula = FibonacciFormula()

    for index in range(11):
        fibonacci_number = fibonacci_formula.calculate(index)
        print("{i:3}: {f:3}".format(i=index, f=fibonacci_number))
