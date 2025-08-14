# リスト内から右、中央、左を取るときのDP

height = 3
width = 4
lst = [[1, 1, 2, 1],
      [2, 1, 1, 2],
      [2, 1, 1, 2]]

for h in range(1, height):
    for w in range(width):
        if 0 < w < width - 1:
            # 真ん中
            lst[h][w] += max(lst[h - 1][w - 1:w + 2])  # スライスは範囲外に触らないらしい
        elif w == 0:
            # 左端
            lst[h][w] += max(lst[h - 1][w:w + 2])
        elif w == width - 1:
            # 右端
            lst[h][w] += max(lst[h - 1][w - 1:w + 1])
print(max(lst[-1]))