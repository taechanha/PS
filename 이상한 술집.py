# 6:30 ~

def D(ml):
    cnt = 0
    for pot in pots:
        cnt += pot // ml

    return cnt >= friend_n


pot_n, friend_n = map(int, input().split())
pots = [int(input()) for _ in range(pot_n)]
min_, max_ = min(pots), max(pots)

l, r = 1, max_
while l <= r:
    mid = (l + r) // 2
    if D(mid):  # mid ml 만큼을 배분할 수 있다면
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
