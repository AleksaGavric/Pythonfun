from math import sqrt


def F(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) // (2 ** n * sqrt(5)))


def fib():
    a, b = 0, 1
    while a < 50:
        yield a
        a, b = b, a + b


for index, fibonacci_number in enumerate(fib()):
    print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
    if index == 10:
        break
