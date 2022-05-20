n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dict_a = {}
dict_b = {}

for i in range(1, len(a)+1):
    dict_a[a[i-1]] = i

for i in range(1, len(b)+1):
    dict_b[b[i-1]] = dict_a[b[i-1]]


print(dict_a, dict_b)
