# mapの使い方

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(nums)

nums = map(float, nums)  # typeがmapになる
print(list(nums), type(nums))  # リスト化はできる