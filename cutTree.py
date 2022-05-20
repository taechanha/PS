# 4 7
# 20 15 10 17   ->  15

def helper(a):
    if a < 0:
        return 0
    else:
        return a

# 10 20


def decision(s, e):
    mid = (s + e) // 2
    if check(mid) == m:
        return mid
    elif check(mid) > m:
        return decision(mid + 1, e)
    else:
        return decision(s, mid - 1)


def check(cut):
    summed = 0
    for each in arr:
        summed += helper(each - cut)
    return summed


global n, m
n, m = map(int, input().split())
global arr
arr = list(map(int, input().split()))

print(decision(min(arr), max(arr)))
