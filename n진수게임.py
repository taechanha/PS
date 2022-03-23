def ternary(n):
    # 0 -> "0"
    # 1 -> "1"
    # 2 -> "2"
    # 3 -> "10"
    # 4 -> "11"
    # 5 -> "12"
    if n == 0:
        return "0"
    temp = ""
    while n > 0:
        temp = str(n % 3) + temp
        n //= 3
    return temp


def n_ary(n, x):
    # n > 10이면, 10 이상에 대해 ABCDEF를 각각 매핑해야 함. 어떻게?
    d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if x == 0:
        return "0"
    temp = ""
    while x > 0:
        if x % n >= 10:
            temp = d[x % n] + temp
        else:
            temp = str(x % n) + temp
        x //= n
    return temp


def solution(n, t, m, p):
    ans = ""
    num_search_space = t * m  # loose upper bound
    data = ""
    for i in range(num_search_space):
        data += n_ary(n, i)

    start_pointer = p - 1
    while t > 0:
        ans += data[start_pointer]
        start_pointer += m
        t -= 1

    return ans


n = 2
t = 4
m = 2
p = 1

n = 16
t = 16
m = 2
p = 1

n = 16
t = 16
m = 2
p = 2

res = solution(n, t, m, p)
print(str(res) == "0111")
print(str(res) == "02468ACE11111111")
print(str(res) == "13579BDF01234567")
