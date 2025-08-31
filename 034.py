# ソシャゲのガチャで、意図的にランダムの数値を偏らせる？実装ができるって聞いた
# 1-5の乱数を2つ足して、0-10の乱数という扱いにするらしい
# 1が出なかったから、中の値をいじってみる

import random
import matplotlib.pyplot as plt

random_range = 10
trying = 999999

def two_in_one():
    random_num1 = random.randint(1, random_range // 2)
    # print(random_num1)

    random_num2 = random.randint(1, random_range // 2)
    random_num2 = random_range // 2 - random_num2  # ここの値を反転させたら1が出るが、逆に10が出なくなる
    # print(random_num2)

    return random_num1 + random_num2

def keisan(trying):
    normal_lst = [0 for _ in range(random_range)]
    two_in_one_lst = [0 for _ in range(random_range)]
    for i in range(trying):
        # 普通のほう
        num = random.randint(1, random_range)
        normal_lst[num - 1] += 1
        # 2つ足すほう
        num = two_in_one()
        two_in_one_lst[num - 1] += 1

    return normal_lst, two_in_one_lst

# print(keisan(1000))
normal_lst, two_in_one_lst = keisan(trying)

# グラフ
x = range(1, random_range + 1)
bar_width = 0.5

# 棒のとこ
plt.bar([i - bar_width/2 for i in x], normal_lst, width=bar_width, label='normal')
plt.bar([i + bar_width/2 for i in x], two_in_one_lst, width=bar_width, label='two in one')

# 軸
plt.xlabel('value')
plt.ylabel('count')
plt.title(f'{trying} trying')
plt.xticks(x)
plt.legend()
plt.show()
