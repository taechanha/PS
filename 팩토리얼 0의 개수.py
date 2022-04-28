from math import factorial

n = int(input())

for i, each in enumerate(str(factorial(n))[::-1]):
    if each != '0':
        print(i)
        break
