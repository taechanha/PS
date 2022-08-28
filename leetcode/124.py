def solution(n):
    if n == 0:
        return '0'
    nums = []
    nums2 = []
    l24 = [1, 2, 4]

    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
        # if r == 0:
        nums2.append(str(l24[r-1]))
        # else:
        # nums2.append(str(l24[r-1]))

    return [''.join(reversed(nums)), ''.join(reversed(nums2))]


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(solution(i))
