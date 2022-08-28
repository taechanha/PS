

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


a = n_ary(3, 10)
print(a)