# 実装方法が不明だったコード
# [0, 0, 1, 1]を[0, 2, 1, 2]のように変換する

# nums = [0, 0, 1, 1, 1]  # [0, 2, 1, 3]にしたい
nums = [0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 5, 5, 5, 4, 5, 4, 3, 2]  # [0, 4, 1, 2, 2, 2, 1, 3, 5, 3, 4, 1, 5, 1, 4, 1, 3, 1, 2, 1]

rule = []
ans = []
for i in range(len(nums)):
    if i == 0:  # i = 0は除外
        rule.append(nums[i])
    elif nums[i - 1] == nums[i]:  # 前と現在の要素が同じ
        rule.append(nums[i])
    else:  # 前と現在の要素が違う
        ans.append(rule[0])  # ruleに入っている値
        ans.append(len(rule))  # ruleに入っている数
        rule = [nums[i]]  # 次の値
ans.append(rule[0])  # ruleに入っている値
ans.append(len(rule))  # ruleに入っている数

print(nums, ans)