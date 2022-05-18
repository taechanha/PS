n = int(input())
a = list(map(int, input().split()))
check = dict()
for each in a:
    check[each] = 0

m = int(input())
b = list(map(int, input().split()))
for each in b:
    if each in check:
        print(1)
    else:
        print(0)
