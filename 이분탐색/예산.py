N = int(input())
req = list(map(int, input().split()))
M = int(input())

def D(B): # B for Budget
    global req, M
    ret = 0
    for r in req:
        ret += min(B, r)
    return ret <= M


l = 0
r = max(req)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if D(mid):  # 예상 배정 총액이 M 이하인가? -> 더 높여보자
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
