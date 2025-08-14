num1 = [3, 4, 9, 1]
num2 = [8, 6, 2, 5]
num3 = [9, 7, 9, 6]

"""
a + b + c + dのように、演算子は3か所に2択の8通り

+++
++-
+-+
+--
-++
-+-
--+
---
"""

def keisan(num):
    return [num[0] + num[1] + num[2] + num[3],
            num[0] + num[1] + num[2] - num[3],
            num[0] + num[1] - num[2] + num[3], 
            num[0] + num[1] - num[2] - num[3],
            num[0] - num[1] + num[2] + num[3],
            num[0] - num[1] + num[2] - num[3],
            num[0] - num[1] - num[2] + num[3],
            num[0] - num[1] - num[2] - num[3],]

num1 = keisan(num1)
num2 = keisan(num2)
num3 = keisan(num3)
lst = []
for l1 in num1:
    for l2 in num2:
        for l3 in num3:
            if l1 == l2 == l3:
                # print(l1, l2, l3)
                lst.append(l1)
lst = set(lst)
print(sorted(lst))