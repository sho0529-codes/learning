# 文字列がアナグラムとして成り立つかどうか

text1 = "LISTEN"
text2 = "SILENT"
text3 = "STONE"
text4 = "STOVE"

text1_sorted = sorted(text1)
text2_sorted = sorted(text2)
text3_sorted = sorted(text3)
text4_sorted = sorted(text4)

print(text1, text2, text1_sorted, text2_sorted, text1_sorted == text2_sorted)
print(text1, text3, text3_sorted, text4_sorted, text1_sorted == text3_sorted)