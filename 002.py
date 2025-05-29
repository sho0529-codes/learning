# mapの続き
# 標準入力のとき

a = "0 1 2 3 4 5 6 7 8 9"  # 標準入力を想定

nums = list(map(float, a.split()))  # splitでリスト化、mapで要素をfloat型、mapをリストに
# nums = list(map(int, input().split()))  # いつもはこっちで変換してる

print(nums)