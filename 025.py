# リスト内から右、中央、左を取るときの全探索
# どこかしらに例外処理の不備があるらしい

height = 3
width = 4
lst = [[1, 1, 2, 1],
      [2, 1, 1, 2],
      [2, 1, 1, 2]]

def keisan(indexs :list):
    """
    引数：各行の座標のリスト
    戻り値：合計値
    引数として各行で選択した座標を受け取り、lstから合計値を出す
    """
    num = 0
    for line in range(height):
        index = indexs[line]
        num += lst[line][index]
    return num

def kumiawase(depth=0, combination=None, combinations=None):
    """
    順序な探索だと例外あってだめ
    総当たりのリストを再起で作る
    """
    if combination is None:
        combination = []
    if combinations is None:
        combinations = []

    if depth == 0:  # 最初
        for w in range(width):
            combination.append(w)
            # depth, combination, combinations = kumiawase(depth + 1, combination, combinations)
            kumiawase(depth + 1, combination, combinations)
            combination.pop()
    elif 0 < depth < height - 1:  # 途中
        for w in [combination[-1] - 1, combination[-1], combination[-1] + 1]:
            if 0 <= w <= width - 1:
                combination.append(w)
                # depth, combination, combinations = kumiawase(depth + 1, combination, combinations)
                kumiawase(depth + 1, combination, combinations)
                combination.pop()
    elif depth == height - 1:  # 最後
        for w in [combination[-1] - 1, combination[-1], combination[-1] + 1]:
            if 0 <= w <= width - 1:
                combination.append(w)
                combinations.append(combination[:])  # コピーのと同じ対策
                combination.pop()

    return combinations

all_paths = kumiawase()  # 全通りの経路
scores = [keisan(path) for path in all_paths]  # 合計値のリスト
max_score = max(scores)
print("max", max_score)


# height, width = map(int, input().split())
# lst = []
# for _ in range(height):
#     lst.append(list(map(int, input().split())))
# ans_lst = []

# # 1行目は最大値
# line1 = lst[0].index(max(lst[0]))
# ans_lst.append(line1)
# # 2行目以降は、heightの回数に従って繰り返し

# for line in range(height - 1):  # 1行目の分は抜いとく
#     if (0 == ans_lst[-1]):
#         line_slice = lst[line + 1][:2]
#         var = line_slice.index(max(line_slice))
#         var = 0 + var
#         ans_lst.append(var)
#     elif (width - 1 == ans_lst[-1]):
#         line_slice = lst[line + 1][-2:]
#         var = line_slice.index(max(line_slice))
#         var = (width - 2) + var
#         ans_lst.append(var)
#     else:
#         line_slice = lst[line + 1][ans_lst[-1] - 1:ans_lst[-1] + 2]
#         var = line_slice.index(max(line_slice))
#         var = (ans_lst[-1] - 1) + var
#         ans_lst.append(var)
# # print(ans_lst)
# ans = 0
# for num, i in enumerate(lst):
#     ans += i[ans_lst[num]]
# print(ans)

# # 2行目は、取れる範囲（スライスかなんかで）の最大値
# # line1 - 1, line1, line1 + 1の範囲内
# # スライスを別で保存して、範囲外を触らんように
# if (0 == line1):
#     line2_slice = lst[1][:2]
#     line2 = line2_slice.index(max(line2_slice))
#     line2 = 0 + line2
# elif (width - 1 == line1):
#     line2_slice = lst[1][-2:]
#     line2 = line2_slice.index(max(line2_slice))
#     line2 = (width - 2) + line2
# else:
#     line2_slice = lst[1][line1 - 1:line1 + 2]
#     line2 = line2_slice.index(max(line2_slice))
#     line2 = (line1 - 1) + line2

# # 3行目は2行目と同じ処理
# if (0 == line2):
#     line3_slice = lst[2][:2]
#     line3 = line3_slice.index(max(line3_slice))
#     line3 = 0 + line3
# elif (width - 1 == line2):
#     line3_slice = lst[2][-2:]
#     line3 = line3_slice.index(max(line3_slice))
#     line3 = (width - 2) + line3
# else:
#     line3_slice = lst[2][line2 - 1:line2 + 2]
#     line3 = line3_slice.index(max(line3_slice))
#     line3 = (line2 - 1) + line3

# print(line1, line2, line3)