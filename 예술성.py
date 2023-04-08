# 5:02

# 그룹 정의: 같은 숫자로 인접해있는 경우 동일한 그룹
# 예술 점수: 모든 그룹 쌍의 조화로움의 합
#   - (a에 속한 칸의 개수, b에 속한 칸의 개수) * a 숫자 값 * b 숫자 값 * a와 b가 서로 맞닿아있는 변의 수
#   - 모든 그룹에 대해 구한 후 그 합 -> for 문 사용해서 조합 구함
# 회전
#   - 중앙 십자가: 반 시계 방향으로
#   - 중앙 십자가 제외 나머지 4개의 정사각형: 시계 방향으로
# 이후 예술 점수 구하기

# 답: 이후 3회전까지(+2) 진행 후 예술 점수의 합 (초기, 1, 2, 3 회전 모두 합한 값)
def DEB(board):
    [print(row) for row in board]
    
def rotate_reverse():
    global board
    reversed = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            reversed[r][c] = board[c][n-1-r]
    return reversed


def rotate4(reverse, start_r, start_c):
    temp_arr = [[0 for _ in range(stride)] for _ in range(stride)]

    for i in range(stride):
        for j in range(stride):
            temp_arr[i][j] = board[start_r+i][start_c+j]
    temp_arr = [list(reversed(x)) for x in zip(*temp_arr)]

    for i in range(stride):
        for j in range(stride):
            reverse[start_r+i][start_c+j] = temp_arr[i][j]

    return reverse


def get_groups(board):
    groups = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            group = get_group(i, j, visited)
            groups.append(group)
    return groups

def get_group(r, c, visited):
    def in_range(r, c): return (0 <= r < n and 0 <= c < n)
    
    val = board[r][c]
    stack = [(r, c)]
    visited[r][c] = True
    visits = [(r, c)]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue
            if board[nr][nc] != val: continue
            stack.append((nr, nc))
            visited[nr][nc] = True
            visits.append((nr, nc))
            
    return visits

def get_adj_num_groups(gi, gj):
    adj_pos = set()
    for r, c in gi:
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in gj:
                adj_pos.add((r, c, nr, nc))
    return len(adj_pos)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
stride = n // 2
all_cnt = 0

# 그룹 구하기
groups = get_groups(board)
ng = len(groups)

# 그룹 간 인접 변의 수 구하기
adj_num = dict()
for i in range(ng):
    for j in range(i+1, ng):
        adj_num[(i, j)] = get_adj_num_groups(groups[i], groups[j])


# 그룹 쌍에 대해 조합 구하기
for i in range(ng):
    for j in range(i+1, ng):
        # (a에 속한 칸의 개수, b에 속한 칸의 개수) * a 숫자 값 * b 숫자 값 * a와 b가 서로 맞닿아있는 변의 수
        cnt = (len(groups[i]) + len(groups[j]))
        
        r, c = groups[i][0]
        cnt *= board[r][c]
        r, c = groups[j][0]
        cnt *= board[r][c]
        cnt *= adj_num[(i, j)]

        all_cnt += cnt

# 그룹 정의, 예술 점수 구하기 => 1회전 후 예술 점수
# 이것을 3번 반복해서 모두 더하기
for i in range(3):
    # 십자가 회전
    """ 십자가 골라서 회전시키는 것보다 그냥 카피 후 카피본을 반시계 회전 시킨후, 카피본의 4개 정사각형 부분에 회전시킨 정사각형을 복붙한 후 카피본을 원본으로 사용하면 됨 """
    reverse = rotate_reverse()
    
    # 십자가 제외 나머지 4개 정사각형 회전
    """ n이 주어지면 4개 정사각형 위치 구하는 함수 """
    """ r, c 범위가 주어지면 그 범위에 대해서만 시계 방향 회전하는 함수 & 보드에 복붙까지 """
    for sr, sc in [(0, 0), (0, stride+1), (stride+1, 0), (stride+1, stride+1)]:
        reverse = rotate4(reverse, sr, sc)

    board = reverse
    
    groups = get_groups(board)
    ng = len(groups)

    # 그룹 간 인접 변의 수 구하기
    adj_num = dict()
    for i in range(ng):
        for j in range(i+1, ng):
            adj_num[(i, j)] = get_adj_num_groups(groups[i], groups[j])


    # 그룹 쌍에 대해 조합 구하기
    for i in range(ng):
        for j in range(i+1, ng):
            # (a에 속한 칸의 개수, b에 속한 칸의 개수) * a 숫자 값 * b 숫자 값 * a와 b가 서로 맞닿아있는 변의 수
            cnt = (len(groups[i]) + len(groups[j]))
            
            r, c = groups[i][0]; cnt *= board[r][c]
            r, c = groups[j][0]; cnt *= board[r][c]
            cnt *= adj_num[(i, j)]

            all_cnt += cnt
        

print(all_cnt)