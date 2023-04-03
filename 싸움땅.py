# n x n
# 초기 플레이어 위치에는 총 없음
# 각 플레이어 능력치 모두 다름
# 플레이어 초기 능력치, 총의 공격력, 플레이어 번호

# 라운드
# 1. 플레이어 현재 바라보고 있는 방향으로 한 칸 이동
# 2. 격자 벗어나면 정반대로 방향 바꿔서 한 칸 이동
# 3. 이동한 곳에 플레이어 없으면 그 위치 총 확인 후, 놓여있는 총들과 가지고 있는 총 중 가장 공격력이 쎈 것을 고르고, 나머지는 아래에 놓음
# 4. 있으면, 싸움 (초기 능력치 + 총 공격력의 합, 같으면 초기 능력치가 더 큰 플레이어가 이김)
# 5. 이긴 플레이어는 합의 차이만큼 포인트 획득
# 6. 진 플레이어는 총을 아래에 놓고, 원래 가고 있던 방향으로 한 칸 이동.
# 7. 그곳에 다른 플레이어가 있거나 격자 범위 밖인 경우 빈 칸이 보일 때까지 오른쪽으로 90도 씩 회전하여 이동 (없으면 제자리)
# 8. (2) 이동한 곳에 총이 있으면 가장 공격력 높은 총 고르고 나머지는 아래에 놓음
# 9. 이긴 플레이어도 마찬가지로 그 위치에서 가장 공격력 높은 총 고름
# 10. 이 과정을 n번 플레이어 모두 수행하면 1라운드
# 11. k라운드 거친 후 각 플레이어의 번호 순으로 담긴 포인트들의 배열 리턴

def in_bound(r, c):
    return (0 <= r < n and 0 <= c < n)

def move(p):
    # r, c, d, s
    r, c, d, s, gun = players[p]
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    # 격자 벗어난 경우
    if not in_bound(nr, nc):
       # 아래로 넘어간 경우
       if nr == n:
           nr, d = n-2, rev_dirs[d]
       # 위로
       elif nr < 0:
           nr, d = 1, rev_dirs[d]
       # 왼쪽으로
       elif nc < 0:
           nc, d = 1, rev_dirs[d]
       # 오른쪽으로
       elif nc == n:
           nc, d = n-2, rev_dirs[d]
    
    players[p] = (nr, nc, d, s, gun)
    return

def exist_another(i, r1, c1):
    for i2, (r2, c2, _, __, ___) in enumerate(players):
        if i == i2: 
            continue
        if (r1, c1) == (r2, c2):
            return True, i2
    return False, None

def give_point(winner, loser):
    r1, c1, d1, s1, gun1 = players[winner]
    r2, c2, d2, s2, gun2 = players[loser]
    
    diff = (s1 + gun1) - (s2 + gun2)
    points[winner] += diff
    
def get_gun(p):
    r, c, d, s, gun = players[p]
    
    guns = board[r][c]
    max_gun, max_idx = board[r][c][0], 0
    for i, each_gun in enumerate(guns):
        if each_gun > max_gun:
            max_gun = each_gun
            max_idx = i
    
    if max_gun > gun:
        board[r][c].pop(max_idx)
        board[r][c].append(gun)
        players[p] = (r, c, d, s, max_gun)

# idx, idx
def fight(p1, p2):
    r1, c1, d1, s1, gun1 = players[p1]
    r2, c2, d2, s2, gun2 = players[p2]
    
    power1, power2 = s1 + gun1, s2 + gun2
    winner, loser = None, None
    if power1 == power2:
        if s1 > s2:
            winner, loser = p1, p2
        else:
            winner, loser = p2, p1
    elif power1 > power2:
        winner, loser = p1, p2
    else:
        winner, loser = p2, p1
        
    give_point(winner, loser)
    
    r, c, d, s, gun = players[loser]
    board[r][c].append(gun)
    players[loser] = (r, c, d, s, 0)
    loser_move(loser)
    
    return winner, loser
    

def loser_move(p):
    r, c, d, s, gun = players[p]
    moved = False
    for i in range(4):    
        # 가던 방향으로 한 칸 이동
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        # 격자 밖이거나 다른 플레이어 없을 때 까지 90도 회전 후 이동 시도
        if not in_bound(nr, nc):
            d = deg90_dirs[d]
            continue
        exist, idx = exist_another(p, nr, nc)
        if exist:
            d = deg90_dirs[d]
            continue
        
        r, c = nr, nc
        moved = True
        break
     
    players[p] = (r, c, d, s, gun)
    if moved:
        get_gun(p)

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
points = [0] * m
players = []
# 위 오른쪽 아래 왼쪽
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
rev_dirs = {0: 2, 2: 0, 1: 3, 3: 1}
deg90_dirs = {0: 1, 1: 2, 2: 3, 3: 0}
for _ in range(m):
    r, c, d, s = map(int, input().split())
    players.append((r-1, c-1, d, s, 0))

# 전처리: 모든 칸이 리스트
for i in range(n):
    for j in range(n):
        board[i][j] = [board[i][j]]

# k번 반복
for i in range(k):
    # 각 플레이어마다 이동
    for p in range(m):
        
        # 이동 (격자 밖 처리 포함)
        move(p)
        curr_r, curr_c, _, __, ___ = players[p]
        
        # 다른 플레이어 존재한다면
        exist, another = exist_another(p, curr_r, curr_c)
        if exist:
            # 싸움
            winner, loser = fight(p, another)
            get_gun(winner)
        else:
            # 아니면 총 획득
            get_gun(p)
        

print(' '.join(map(lambda x: str(x), points)))

