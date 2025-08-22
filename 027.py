# ステップ数を指定し、そこから到達不可能なマス目を計算する

num = 10
a, b = 3, 5
kaidan_lst = [0] * num

# aとbと最後尾
if 1 <= a <= num:
    kaidan_lst[a - 1] = 1
if 1 <= b <= num:
    kaidan_lst[b - 1] = 1
kaidan_lst[-1] = 1

# 倍数
for i in range(num):
    if (i + 1) % a == 0:
        kaidan_lst[i] = 1
    if (i + 1) % b == 0:
        kaidan_lst[i] = 1

# 足し算
# 0であれば、そのaかb座標分前に1が無いか探す
for i in range(num):
    if kaidan_lst[i] == 0:
        if (0 <= i - a <= num -1) and (kaidan_lst[i - a] == 1):  # 範囲内と1の確認
            kaidan_lst[i] = 1
        if (0 <= i - b <= num -1) and (kaidan_lst[i - b] == 1):
            kaidan_lst[i] = 1
# print(kaidan_lst)

count = kaidan_lst.count(0)
print("lst:", kaidan_lst)
print("0count:", count)
