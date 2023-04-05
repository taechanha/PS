# 10:35

# 0: 빈 칸
# 1: 베이스캠프

# 처음에는 모든 사람이 격자 밖
# m분에 m번 사람이 베이스 캠프에서 편의점으로 출발

# 1분 동안 아래 작업 진행
# 1. 본인 편의점으로, 최단거리로, 한 칸 이동, 최단거리가 여러 개라면 위, 왼, 오른, 아래 우선순위
# 2. 편의점에 도착 시, 해당 편의점에서 멈춤!!. 이 칸은 이동 불가
# 3. 현재 시간이 t분이고 t <= m을 만족하면, t번 사람은 자신의 편의점과 최단거리의 베이스캠프로 들어감! (순간이동)
    # 여러 개면, 그 베이스캠프 중 행이 가장 작은 것, 행이 같으면 열이 가장 작은 것 
    # 이때부터 해당 베이스캠프 이동 불가

from collections import deque

def move_shortest(is_basecamp, r, c, tr=None, tc=None):
    dist = 0
    Q = deque([(r, c, dist)])
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    cnts = []
    while Q:
        r, c, dist = Q.popleft()
        if is_basecamp:
            if board[r][c] == 1:
                cnts.append([dist, r, c])
        else:
            if (r, c) == (tr, tc):
                return dist + 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n): continue
            if visited[nr][nc]: continue
            if board[nr][nc] == BLOCKED: continue
            Q.append((nr, nc, dist+1))
            visited[nr][nc] = True
    return cnts

def goto_basecamp(cr, cc):
    bases = move_shortest(True, cr, cc)
    
    bases.sort(key=lambda x: (x[0], x[1], x[2]))
    
    if DEBUG: print(bases)
    
    assert len(bases) >= 1
    
    return bases[0][1:]

class Person:
    def __init__(self, r, c, done):
        self.r = r
        self.c = c
        self.done = done
        
    def move(self, tr, tc):
        # 위, 왼, 오른, 아래 우선순위
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        idx, shortest = None, float('inf')
        for i, (dr, dc) in enumerate(dirs):
            nr, nc = self.r + dr, self.c + dc
            if not (0 <= nr < n and 0 <= nc < n): continue
            if board[nr][nc] == BLOCKED: continue
            
            cnt = move_shortest(False, nr, nc, tr, tc)
            if type(cnt) == list: continue
            
            if shortest > cnt:
                shortest = cnt
                idx = i
        
        # move
        self.r, self.c = self.r + dirs[idx][0], self.c + dirs[idx][1]
        
        # 편의점 도착
        global to_block
        if (self.r, self.c) == (tr, tc):
            to_block.append((tr, tc))
            self.done = True
    
    def __str__(self):
        return str((self.r, self.c, self.done))

DEBUG = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
convs = [None]
board_people = [None]
BLOCKED = 'blocked'
for _ in range(m):
    r, c = map(lambda x: int(x)-1, input().split())
    convs.append((r, c))
    
t = 0
while True:
    t += 1
    population = len(board_people)
    to_block = []
    
    # terminate condition
    cnt = sum(1 for i in range(1, population) if board_people[i].done == True)
    if cnt == m:
        print(t-1)
        break
    
    # 격자에 사람들이 있다면, 그 사람들 이동
    if not (population == 1):
        for i in range(1, population):
            person = board_people[i]
            
            if person.done: continue
            
            tr, tc = convs[i] # i's conv position
            person.move(tr, tc)
    
    
    # t분 사람 베이스캠프로 점프
    if t > m:
        continue
    cr, cc = convs[t] # t번째 사람의 최단거리 편의점 위치
    tr, tc = goto_basecamp(cr, cc)
    board[tr][tc] = BLOCKED # 블락 처리
    person = Person(tr, tc, None)
    board_people.append(person)
    
    if DEBUG: [print(x, end=" ") for x in board_people[1:]]
    
    for r, c in to_block:
        board[r][c] = BLOCKED
    