from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

n = len(arr)
arr.sort()
min_dist = float('inf')
ans = []
for i in range(n-1):
    # 타겟 -a[i], 탐색공간 (a[i+1:])
    # Ex. -(-99), (-2, -1, 4, 98) -> 98
    x = arr[i]
    ret = bisect_left(a=arr, x=-x, lo=i+1)
    if ret == n:
        y = arr[n-1]
    # elif ret == 0:
    #     # never happen
    #     y = arr[ret]
    else:
        # arr[i]=-2, arr[ret-1]=-1, arr[ret]=6
        if ret >= i+2:
            p = abs(arr[i]+arr[ret-1])
            q = abs(arr[i]+arr[ret])
            if p > q:
                y = arr[ret]
            else:
                y = arr[ret-1]
        else:
            y = arr[ret]

    dist = abs(x+y)

    if min_dist > dist:
        min_dist = dist
        ans = [x, y]

print(' '.join(map(str, ans)))
