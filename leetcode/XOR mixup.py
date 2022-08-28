
t = int(input())
ans = []
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        res = 0
        for j in range(n):
            if j == i:
                continue
            res ^= a[j]
        if res == a[i]:
            ans.append(res)
            break
for row in ans:
    print(row)
