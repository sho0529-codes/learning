# 関数を返り値に持つ関数があるらしい

def adder(x):
    def inner(y):
        return x + y
    return inner

num = adder(100)

print("num:", num)
print("num(10):", num(10))
