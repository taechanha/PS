def bsearch(arr, x):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
for x in b:
    ret = bsearch(a, x)
    if ret == -1:
        print(0)
    else:
        print(1)
