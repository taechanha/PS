# 5:36 ~

from itertools import combinations as C
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
MAX = max(nums)
data = []
for i, num in enumerate(nums):
    data.append((i, num))

data = list((C(data, 2)))

lookup = defaultdict(list)  # sum: [idx1, idx2]

for each in data:
    idx1, num1, idx2, num2 = *each[0], *each[1]
    sum = num1 + num2
    if sum <= MAX:
        lookup[sum].append((idx1, idx2))

ans = 0
for i, num in enumerate(nums):
    if num in lookup:
        # lookup[num].sort(key=lambda x: (x[0], x[1]))
        for each in lookup[num]:
            if each[0] > i:
                break
            if i == each[0] or i == each[1]:
                continue
            ans += 1

print(lookup)
print(ans)
