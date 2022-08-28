#   N   result
#   5     2
#   6     2
#   5000  5
# 0 1 2 3 4 5 6

# 5000 -> 2500 -> 1250 -> 625 -> 312(+1) -> 156 -> 78 -> 39 -> 19 -> 9 -> 4 -> 2 -> 1 -> 0
#                             1                             1     1    1              1

def solution(n):
    # 625 /= 2 => 312.5
    k = 0
    while n != 1:
        if n % 2 == 1:
            k += 1
        n //= 2
    return k + 1


def solution2(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return solution2(n//2)
    else:
        return solution2(n-1) + 1


print(solution2(5000))
