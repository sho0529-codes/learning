num, c = 13, 5  # 列数と含まれる数値の個数
k = 7  # 行数
lst = [[0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

# def search_num(num):
#     ans = []
#     for i in range(k):
#         if lst[i][num - 1] == 1:
#             ans.append(i + 1)
#     return ans

# def nuri(kari, lst):
#     for i in range(num):
#         if lst[i] == 1:
#             kari[i] += 1
#     return kari

def keisan():
    covered = [0] * num
    used_rows = [False] * k  # もう出てきたとこ
    step_count = 0

    while True:
        # 0の列（まだ持ってない）を数える
        uncovered = [i for i in range(num) if covered[i] == 0]
        if not uncovered:
            break  # 終了判定

        # 各行が何個の列をカバーできるか
        best_row = -1
        best_score = -1
        for i in range(k):
            if used_rows[i]:
                continue
            score = sum([1 for j in uncovered if lst[i][j] == 1])
            if score > best_score:
                best_score = score
                best_row = i

        if best_score == 0:
            return -1  # 不可能は-1を返すように

        # スコアが良いものを選択
        used_rows[best_row] = True
        for j in range(num):
            if lst[best_row][j] == 1:
                covered[j] = 1
        step_count += 1

    return step_count

print(keisan())