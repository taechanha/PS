from itertools import combinations as C

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 1. 치킨집이 있을 수 있는 위치의 조합
#   1-1. 치킨집의 위치
chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chickens.append((i, j))
        elif board[i][j] == 1:
            houses.append((i, j))
# 조합
cases = list(C(chickens, m))

# 2. 각 조합에 대해 도시의 치킨 거리 계산
#   2-1. 각 집으로부터 최소 치킨 거리의 합
min_city_dist = float('inf')

def get_dist(hr, hc, cr, cc):
    return abs(hr - cr) + abs(hc - cc)

# O(nCr) -> w: 1700
for case in cases:
    city_dist = 0
    # O(n) -> w: 50
    for hr, hc in houses:
        chicken_dist = float('inf')
        # O(n) -> w: 13
        for cr, cc in case:
            chicken_dist = min(chicken_dist, get_dist(hr, hc, cr, cc))
        city_dist += chicken_dist
    
    min_city_dist = min(min_city_dist, city_dist)

# 3. min_city_dist 출력
print(min_city_dist)

