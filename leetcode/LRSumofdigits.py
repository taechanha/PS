n, m = map(int, input().split())
res = 0

for digit in range(n, m + 1):
    res += sum(list(map(int, str(digit))))

print(res)
