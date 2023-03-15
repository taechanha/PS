# n x n 격자에 사람들이 흩어져있음
# n <= 300, p <= 200
# 모든 사람들이 특정 위치에 모이고 싶음
# 모든 사람이 매 순간 갈 수 있는 방향은 왼, 오른, 아래만
# 전체가 같이 지시한 한 방향으로만 움직일 수 있음
# 격자 넘어가는 명령은 무시
# 명령을 몇 번 해야 모든 사람들이 한 위치에 모일 수 있는지?
# 
# 시작할 때 모든 사람이 한 행 혹은 한 열에 모여있는 경우는 존재하지 않음

def solution(board):
    n = len(board)
    players = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                players.append((i, j))
    
    # 위로 이동하는 데 필요한 최소 이동 거리
    max_u = 0
    for p in players:
        r, c = p
        max_u = max(max_u, r-1)
    
    # 왼쪽으로 "
    max_l = 0
    for p in players:
        r, c = p
        max_u = max(max_u, c-1)
    # 오른쪽으로
    max_r = 0
    for p in players:
        r, c = p
        max_r = max(max_r, n-1-c)
    
    return max_u + min(max_l, max_r)

board = [[]]
ans = solution(board)
print(ans)