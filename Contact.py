# 11:43 ~ 11:50

import re

n = int(input())

while n:
    n -= 1
    wave = input()

    pattern = re.compile(r'(100+1+|01)+')

    if pattern.fullmatch(wave):
        print("YES")
    else:
        print("NO")
