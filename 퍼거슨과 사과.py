# 6:09 ~ 6:23

def uclid(x, y):
    while y:
        x, y = y, x % y
    return x


r, g = map(int, input().split())

ans = []
n = uclid(r, g)
ans.append([n, r//n, g//n])

for i in range(n-1, 0, -1):
    a, b = r % i, g % i
    # print(a, b)
    if a == 0 and b == 0:
        ans.append([i, r//i, g//i])

for row in ans:
    print(*row)
