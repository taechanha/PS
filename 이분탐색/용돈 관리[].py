n, m = map(int, input().split())
spend = [int(input()) for _ in range(n)]


def D(W):
    global spend, m

    cnt, budget = 1, W
    for i in range(n):
        if spend[i] < budget:
            budget -= spend[i]
        else:
            budget += W
            budget -= spend[i]
            cnt += 1

    return cnt <= m


l = max(spend)
r = 10**9
ans = 0
while l <= r:
    mid = (l + r) // 2
    if D(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
