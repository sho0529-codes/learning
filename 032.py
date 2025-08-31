# maxの数値をinde()で探すときにおこる問題の対処
# 要は、指定範囲内を切り抜いて探し、それを元リストに対応させれば良いはず

import random

# 縦横
width = 5
height = 5

def random_lst(width: int, height: int):
    """
    引き数：width（横幅）、height（高さ）
    返り値：lst（width*heightの2次元リスト）
    与えられた縦横から、ランダム（1から50）に数字を振った2次元リストを返す
    """
    lst = [[random.randint(1, 50) for _ in range(width)] for _ in range(height)]
    return lst

def dp_lst(lst: list):
    """
    引き数：lst
    返り値：lst（dp探索を行ったリスト）
    与えられたリストで上を始点、下を終点とするdp探索
    """
    width = len(lst[0])
    height = len(lst)

    for i in range(1, height):
        for j in range(width):
            # スライスで範囲外にならないように
            if j == 0:  # 左端
                lst[i][j] += max(lst[i - 1][:j + 2])
            elif 0 < j < width - 1:  # 真ん中
                lst[i][j] += max(lst[i - 1][j - 1:j + 2])
            elif j == width - 1:  # 右端
                lst[i][j] += max(lst[i - 1][j - 1:])
    return lst

def show_lst(lst: list):
    """
    引き数：lst
    返り値：char（数値の表示をそろえた文字列）
    与えられたリストを視覚的に見やすいように揃える
    """
    char = ""
    for i in lst:
        for j in i:
            char += " " * (5 - len(str(j))) + str(j)  # 4桁までは揃って表示される
        char += "\n"
    return char

def route_hantei_lst(lst: list):
    """
    引き数：lst（dp探索が行われたリスト）
    返り値：lst（各行の最大値をAに、最大値の経路をBに置き換えたリスト）
    各行の最大値を視覚的に分かりやすく変換する
    複数の最大値がある場合は全てが変換される
    """
    width = len(lst[0])
    height = len(lst)

    # 最大値の置き換え
    for i in range(height):
        max_num = max(lst[i])
        for j in range(width):  # 2つ以上の時見たいから、わざとこの処理
            if lst[i][j] == max_num:
                lst[i][j] = 999
    
    # 問題の場所
    # 最大値の経路の置き換え
    for i in range(height - 1, -1, -1):  # 逆順
        max_num = max(lst[i])
        for j in range(width):  # 2つ以上の時見たいから、わざとこの処理
            if i == height - 1 and (lst[i][j] == max(lst[-1])):
                lst[i][j] = 9999
            elif (height - 1 > i >= 0) and (lst[i + 1][j] == 9999):
                # 差分のリストから座標を指定し、最大値との一致で判定
                if j == 0:  # 左端
                    max_slice_score = max(lst[i][:j + 2])
                elif 0 < j < width - 1:  # 真ん中
                    max_slice_score = max(lst[i][j - 1:j + 2])
                elif j == width - 1:  # 右端
                    max_slice_score = max(lst[i][j - 1:])
                for sabun in [-1, 0, 1]:
                    if (0 <= j + sabun <= width - 1) and (lst[i][j + sabun] == max_slice_score):
                        lst[i][j + sabun] = 9999
                # # スライスの範囲外対策
                # if j == 0:  # 左端
                #     max_index = lst[i].index(max(lst[i][:j + 2]))
                #     lst[i][max_index] = 9999
                # elif 0 < j < width - 1:  # 真ん中
                #     max_index = lst[i].index(max(lst[i][j - 1:j + 2]))
                #     lst[i][max_index] = 9999
                # elif j == width - 1:  # 右端
                #     max_index = lst[i].index(max(lst[i][j - 1:]))
                #     lst[i][max_index] = 9999
    
    # 文字に置き換え
    for i in range(height):
        for j in range(width):
            if lst[i][j] == 999:
                lst[i][j] = " A "
            elif lst[i][j] == 9999:
                lst[i][j] = " B "

    return lst

lst = random_lst(width, height)
print("lst:")
print(show_lst(lst))

lst = dp_lst(lst)
print("dp:")
print(show_lst(lst))

lst = show_lst(route_hantei_lst(lst))
print("route:")
print(lst)