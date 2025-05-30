# ピラミッド型の多次元リスト

def pyramid_list(value):
    ans = [[0, ] * value for i in range(value)]

    for num in range(value // 2 + 1):
        for y in range(num, value - num):
            for x in range(num, value - num):
                ans[y][x] = num + 1

    return ans

print(pyramid_list(5))