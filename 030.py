# dpが結局どういう動きしてるのか知りたい
# max()でたまにある最大値が複数の場合を見たい

import random

# 縦横
width = 10
height = 10

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

def max_hantei_lst(lst: list):
    """
    引き数：lst（dp探索が行われたリスト）
    返り値：lst（各行の最大値をAに置き換えたリスト）
    各行の最大値を視覚的に分かりやすく変換する
    複数の最大値がある場合は全てが変換される
    """
    width = len(lst[0])
    height = len(lst)

    for i in range(height):
        max_num = max(lst[i])
        for j in range(width):  # 2つ以上の時見たいから、わざとこの処理
            if lst[i][j] == max_num:
                lst[i][j] = " A "
    
    return lst

lst = random_lst(width, height)
print(show_lst(lst))
lst = dp_lst(lst)
print(show_lst(lst))

print(show_lst(max_hantei_lst(lst)))