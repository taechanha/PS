# 11:11

# 빈 칸: 0, 벽: -1, 제초제: -2, 나무: X(x >= 1)
# 성장: 인접한 네 칸 중 나무가 있는 개수만큼 + (동시)
# 번식: 인접한 네 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에. 각 칸의 나무개수를 번식 가능한 칸의 수로 나눈 값을 번식 가능한 칸에 + (나머지 버림)
#    ** 동시에 진행되어서, 중첩됨
# 제초제: 뿌린 칸을 기준으로 대각선 방향으로 +k칸"까지" 나무 없애고 나무 그루수 획득 (없애는 건 나중에 해야함)
#    - 도중 벽이나 빈 칸 만나면 그 칸 "까지" 제초제 뿌려짐
#    - C년까지는 남아있고 c+1년에 사라짐, 덧뿌려지면 덧뿌려진 제초제로 갱신
# 답: 총 박멸한 나무의 개수

# *** 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.


"""
필요한 연산
1. 인접한 네 칸 조사
2. X칸에서 4 대각선 방향으로 k칸 이동(나무 계산), 자기도 포함
3. 벽인지, 제초제인지, 빈 칸인지, 나무인지
4. 제초제: 동시성 때문에 모든 칸에 대해 계산해놓고, 최대값 구한 후에 빈 칸으로 만들어야함
"""

def is_tree(r, c) -> bool:
    return board[r][c] >= 1

def in_bound(r, c): 
    return (0 <= r < n and 0 <= c < n)

def probeNear(r, c, isGrow):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    tree_cnt = 0
    propagates = []
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not in_bound(nr, nc): continue
        if isGrow:
            if is_tree(nr, nc): tree_cnt += 1
        else:
            if board[nr][nc] == 0:
                propagates.append((nr, nc))
    if isGrow:
        return tree_cnt
    else:
        return propagates

def grow_tree():
    for r in range(n):
        for c in range(n):
            if not is_tree(r, c):
                continue
            tree_cnt = probeNear(r, c, True)
            board[r][c] += tree_cnt

def propagate_tree():
    from collections import defaultdict
    mapping = defaultdict(list)
    for r in range(n):
        for c in range(n):
            if not is_tree(r, c):
                continue
            
            propagates = probeNear(r, c, False)
            amount, tree_cnt = board[r][c], len(propagates)
            
            for nr, nc in propagates:
                mapping[(nr, nc)].append(amount // tree_cnt)
    
    for (nr, nc), tree_adds in mapping.items():
        for amt in tree_adds:
            board[nr][nc] += amt

def kill_tree() -> int:
    global chemical_pos
    max_stump_cnt, candidates = 0, []
    
    for r in range(n):
        for c in range(n):
            if not is_tree(r, c):
                continue
            
            stump_cnt, positions = all_diag_cnt(r, c)
            candidates.append((stump_cnt, r, c, positions))
    
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))
    if not candidates:
        return 0
    
    for r, c in candidates[0][-1]:
        board[r][c] = -2
        chemical_pos[(r, c)] = YEAR
    
    return candidates[0][0]

def all_diag_cnt(r, c):
    stump_cnt = board[r][c]
    positions = [(r, c)]
    dr, dc = [-1, 1, -1, 1], [-1, 1, 1, -1]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        for _ in range(STRIDE):
            if not in_bound(nr, nc): break
            
            # *************************************************************************
            # ****************************** 기억해라 ***********************************
            # *************************************************************************
            if board[nr][nc] == -1: 
                break
            elif board[nr][nc] == -2:
                positions.append((nr, nc))
                break
            elif board[nr][nc] == 0:
                positions.append((nr, nc))
                break
            else:
                stump_cnt += board[nr][nc]
                positions.append((nr, nc))
                nr, nc = nr + dr[i], nc + dc[i]
            # *************************************************************************
            # *************************************************************************
            # *************************************************************************
    
    return stump_cnt, positions

def age_chemical():
    global chemical_pos
    for (r, c) in chemical_pos.keys():
        chemical_pos[(r, c)] -= 1
        if chemical_pos[(r, c)] == 0:
            board[r][c] = 0

n, m, STRIDE, YEAR = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chemical_pos = {}
cnt = 0

for year in range(1, m+1):
    # grow tree
    grow_tree()

    # propagate tree
    propagate_tree()
    
    age_chemical()
    # kill tree
    cnt += kill_tree()

print(cnt)