

n, m = map(int, input().split())
lis = [input() for _ in range(n)]
see = [input() for _ in range(m)]


def bsearch(a, x):
    lo = 0
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


ans = []
see.sort()
for target in lis:
    # target이 see에 있으면 듣보잡 -> 출력
    ret = bsearch(see, target)
    if ret == -1:
        continue
    ans.append(target)

print(len(ans))
for each in sorted(ans):
    print(each)
