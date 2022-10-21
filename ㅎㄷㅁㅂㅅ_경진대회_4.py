def bfs(r, c):
    que = [(r, c, 0)]
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True
    while que:
        r, c, score = que.pop(0) 
        if board[r][c] == 'E': 
            return score 
        if board[r][c] not in ('S', 'E'): 
            local_score = 0 
            for nr_, nc_ in ranges: 
                if not (0 <= nr_ < R and 0 <= nc_ < C): continue 
                if board[nr_][nc_] == 'P': 
                    local_score += 1 
                if board[r][c] == 'Z': 
                    score += local_score 
                elif board[r][c] == 'P': 
                    score += (local_score - 3) 
        cand = [] 
        for i in range(4): 
            nr = r + dr[i] 
            nc = c + dc[i] 
            if not (0 <= nr < R and 0 <= nc < C): 
                continue 
            if visited[nr][nc]: continue 
            
            cand.append((board[nr][nc], nr, nc)) 
        
        cand.sort(key=lambda x: (x[0], x[1], x[2])) 
        
        for _, nr, nc in cand: 
            que.append((nr, nc, score)) 
            visited[nr][nc] = True 

R, C = map(int, input().split()) 
board = [list(input()) for _ in range(R)] 
ranges = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1] 
sr, sc = None, None 
for r in range(R): 
    for c in range(C): 
        if board[r][c] == 'S': 
            sr, sc = r, c 
        if board[r][c] == '0':
            board[r][c] = 'Z' 

score = bfs(sr, sc) 
answer = max(score, 0) 
print(answer)