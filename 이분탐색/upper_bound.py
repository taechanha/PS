from bisect import bisect_left, bisect_right


def upper_bound(a: list[int], x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


a = [1, 2, 3, 4, 5]
x = 3
ans = 3
assert ans == upper_bound(a, x)
assert bisect_left(a, x) == upper_bound(a, x)
