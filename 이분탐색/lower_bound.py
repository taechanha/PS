from bisect import bisect_left, bisect_right


def lower_bound(arr: list[int], target: int):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

# test


# case 1: x is in a
a = [1, 2, 3, 4, 5]
x = 3
ans = 2
assert ans == lower_bound(a, x)
assert bisect_left(a, x) == lower_bound(a, x)

# case 2: x is not in a
a = [1, 2, 2, 4, 5]
x = 3
ans = 3
assert ans == lower_bound(a, x)
assert bisect_left(a, x) == lower_bound(a, x)

# case 3: x is larger than all elements in a
a = [1, 2, 3, 4, 5]
x = 6
ans = 5  # 의도: out of range
assert ans == lower_bound(a, x)
assert bisect_left(a, x) == lower_bound(a, x)

# case 4: x is smaller than all elements in a
a = [1, 2, 3, 4, 5]
x = 0
ans = 0
assert ans == lower_bound(a, x)
assert bisect_left(a, x) == lower_bound(a, x)

# case 5: elements same as x in a appear multiple times
a = [3, 3, 4, 4, 5]
x = 3
ans = 0
assert ans == lower_bound(a, x)
assert bisect_left(a, x) == lower_bound(a, x)
