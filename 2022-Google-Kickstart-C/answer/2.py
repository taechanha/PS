from sys import stdin
def input(): return stdin.readline().strip()


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


t = read_int()
for case_num in range(1, t + 1):
    n, x, y = read_ints()
    s = n * (n + 1) // 2
    if s % (x + y) != 0:
        print(f'Case #{case_num}: IMPOSSIBLE')
    else:
        print(f'Case #{case_num}: POSSIBLE')
        a = s // (x + y) * x
        b = set()
        i = 1
        while i <= n:
            b.add(i)
            i *= 2
        used = set()
        for j in range(3, n + 1):
            if j in b:
                continue
            if j <= a:
                used.add(j)
                a -= j
            else:
                break
        for j in range(20):
            if (a & (1 << j)) != 0:
                used.add(1 << j)
        ans = sorted(list(used))
        print(len(ans))
        print(' '.join(map(str, ans)))
