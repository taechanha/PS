
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]

# [1, 2, 4, 8, 9]
def D(dist):
    global house, c

    n = len(house)
    base, move = 0, 1
    # 순차적으로 2개를 골라, 차이가 dist 이상이면, c -= 1, 베이스 포인터는 j로, j는 한 칸 이동
    # 미만이면, 오른쪽 포인터만 한 칸 이동
    installed = set()
    while move < n:
        if house[move] - house[base] >= dist:
            installed.update({move, base})
            base = move
            move += 1
        else:
            move += 1

        if len(installed) >= c:
            return True

    return False

# 이분탐색 대상: 거리
# 이후, 그 거리가 가능한가?
house.sort()
l, r = 1, max(house)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if D(mid): # 만약 이게 가능하면, i <= mid는 다 가능, 따라서 l = mid + 1로 옮겨줘서, 더 큰 거리 탐색
        ans = mid
        l = mid + 1
    else: # 불가능하다면, i < mid에 대해서 탐색 (더 작은 거리 탐색)
        r = mid - 1

print(ans)