# 全部の要素（列の数）を出現させるのに必要な手数の最低値を求める
# ようわからん、作り直し

# num, c = map(int, input().split())
# k = int(input())
# lst = []
# for i in range(k):
#     x = list(map(int, list(input())))
#     lst.append(x)
# print(num, c, lst)

num, c = 13, 5  # 列数と含まれる数値の個数
k = 7  # 行数
lst = [[0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

def search_num(num):
    ans = []
    for i in range(k):
        if lst[i][num - 1] == 1:
            ans.append(i + 1)
    return ans

def nuri(hantei, line_num):
    for i in range(num):
        if lst[line_num - 1][i] == 1:
            hantei[i] = True
    return hantei

ans_num = [0] * num
ans_line = [False] * k

while True:
    # リスト全体から、それぞれ何がいくつあるか
    count_lst = [0] * num  # 出現回数
    yusen_lst = [[] for _ in range(k)]  # 最低1回かつ最大k回出るとして、0回の想定は別で
    # 優先度計算
    count_lst = [0] * num
    yusen_lst = [[] for _ in range(k)]
    for i in range(k):
        if ans_line[i]:
            continue
        for j in range(num):
            if ans_num[j] == 0:
                count_lst[j] += lst[i][j]

    for i in range(num):
        if count_lst[i] == 0:
            print(i + 1, "不可能")
            exit()
        elif 0 < count_lst[i] <= k:
            yusen_lst[count_lst[i] - 1].append(i + 1)

    for yusens in yusen_lst:
        if not yusens:
            continue
        for yusen in yusens:
            kohos = search_num(yusen)
            hantei_lst = []
            for koho in kohos:
                hantei_line = ans_num[:]
                hantei_lst.append(nuri(hantei_line, koho))

            best_score = -1
            best_index = -1
            for idx, hantei in enumerate(hantei_lst):
                score = sum(hantei)
                if score > best_score:
                    best_score = score
                    best_index = idx

            chosen_line = kohos[best_index]
            ans_line[chosen_line - 1] = True
            for i in range(num):
                if lst[chosen_line - 1][i] == 1:
                    ans_num[i] = 1
            break  # 1列につき1行選んだら break
        break  # 1優先度につき1列処理したら break

    if all(ans_num):
        break

print("最小手数:", sum(ans_line))
print("選んだ行:", [i + 1 for i, used in enumerate(ans_line) if used])