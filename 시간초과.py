# 4:40 ~ 4:56

import math

n = int(input())
dp = [-1] * 1_000_001
mapping = {'O(N)': lambda x: x,
           'O(N^2)': lambda x: pow(x, 2),
           'O(N^3)': lambda x: pow(x, 3),
           'O(2^N)': lambda x: pow(2, x),
           'O(N!)': lambda x: math.factorial(x)
           }
# O(f(si[1])) * si[2] <= 100_000_000 * si[3] => may pass
ans = []
for _ in range(n):
    a, b, c, d = input().split()
    b, c, d = int(b), int(c), int(d)
    if mapping[a](b) * c <= 100_000_000 * d:
        ans.append("May Pass.")
    else:
        ans.append("TLE!")
for row in ans:
    print(row)
