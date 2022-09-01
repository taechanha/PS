
def power(x, k, s):
    if k == 0:
        return 1
    res = power(x, k >> 1, s)
    res = res * res % s
    if x & 1:
        res = res * x % s
    return res


T = int(input())

for i in range(1, T+1):
    answer = None
    a, b, k = map(int, input().split())
    # 4, 9, 1 -> 2^1*min(a,b)%(a+b) = 2*4%(13) = 8
    k = k % (a+b)
    kth_num = (power(2, k, a+b) * min(a, b)) % (a+b)
    answer = min((a+b) - kth_num, kth_num)
    print(f"#{i} {answer}")
