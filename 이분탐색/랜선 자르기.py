
def D(L):
    global lines, N
    ret = 0
    # L: 자를 길이
    for line in lines:
        ret += line // L
    return ret >= N

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

l = 1
r = pow(2, 31)
while l <= r:
    mid = (l + r) // 2
    if D(mid): # i <= mid인 경우는 모두 필요한 N개의 랜선을 모두 얻을 수 있음. 
        ans = mid # 따라서 i > mid인 경우를 탐색하기 위해 l = mid + 1로 설정.
        l = mid + 1
    else:
        r = mid - 1
print(ans)