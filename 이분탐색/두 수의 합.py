
n = int(input())
arr = list(map(int, input().split()))
# arr = list(range(1, 100_000))
target = int(input())


def bsearch(a, x, i):
    lo = i
    hi = len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


cnt = 0
arr.sort()
for i in range(n-1):
    t = target - arr[i]
    ret = bsearch(arr, t, i+1) # LEARN: bsearch(arr[i+1:], t)해서 시간초과 났음. 매번 배열 새로 만들어서 넘겨주니까.
    if ret == -1:
        continue
    cnt += 1

print(cnt)
