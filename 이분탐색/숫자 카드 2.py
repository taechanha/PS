from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
ans = []
for t in b:
    res1 = bisect_left(a, t)
    res2 = bisect_right(a, t)
    ans.append(res2 - res1)

for each in ans:
    print(each, end=" ")