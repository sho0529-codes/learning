import math

# フィボナッチ数列とかいうやつ

def fibonacci(n):
    sequence = []
    a, b = 0, 1  # a, b, a + b, b + (a + b)のように続きたい

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# マクローリン展開
def maclaurin(x, n):
    return [x**i / math.factorial(i) for i in range(n)]  # math.factorialは階乗



fib_100 = fibonacci(100)
print(fib_100)

maclaurin_5 = maclaurin(5, 10)
print(maclaurin_5)