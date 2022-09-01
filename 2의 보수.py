x = 2  # 011
b = 0  # 000

x = int(input())
res = (x ^ ((2**32)-1)) + 1

res = x ^ res

print(bin(res).count('1'))
