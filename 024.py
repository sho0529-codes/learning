# 2 3
# 100 90 180
# 200 200 200

n, m = map(int, input().split())

lst1 = []
for i in range(n):
    lst1.append(list(map(int, input().split())))

lst2 = [[0 for _ in range(n)] for i in range(m)]
for i in range(n):
    for j in range(m):
        lst2[j][i] = lst1[i][j]
# print(lst1)
# print(lst2)

lst3 = []
for i in range(m):
    for j in range(n):
        if lst2[i][j] == max(lst2[i]):
            # print(j)
            lst3.append(j)
            print(lst3)
print(len(set(lst3)))