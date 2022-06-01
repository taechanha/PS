
# 12:40 ~
# 2:20 ~ 참고해서 풀었음 - sword를 가지고 있을 때와 아닐 때를 분리해서 풀면 됨

from collections import deque
import sys
input = sys.stdin.readline


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(r, c):
    global n, m, t, dr, dc
    Q = deque([(r, c, 0)])  # (r, c, has_sword?)
    dist = [[None] * m for _ in range(n)]
    dist[r][c] = 0
    min_dist = float('inf')
    while Q:
        r, c, has_sword = Q.popleft()
        # where the princess is
        if (r, c) == (n-1, m-1):
            min_dist = min(min_dist, dist[r][c])
            continue
        if dist[r][c] >= t:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if dist[nr][nc] != None and dist[nr][nc] < dist[r][c] + 1:
                continue
            if board[nr][nc] == 2:
                has_sword = 1
            if board[nr][nc] == 1 and not has_sword:
                continue
            # print(dist[nr][nc], dist[nr][nc], dist[r][c])
            Q.append((nr, nc, has_sword))
            dist[nr][nc] = dist[r][c] + 1
    # for row in dist:
        # print(row)
    return min_dist


min_dist = bfs(0, 0)
print("Fail") if min_dist == float('inf') else print(min_dist)


# visit[ny][nx][find] 이 부분이 포인트

#  static int BFS(){

#         Queue<Point> Q = new LinkedList<>();
#         int result = 100000000;
#         visit[1][1][0] = true;

#         Q.add(new Point(1,1, 0, 0));

#         while(!Q.isEmpty()){
#             Point p = Q.poll();
#             int y = p.y;
#             int x = p.x;
#             int move = p.move;
#             int find = p.find;

#             if(y == r && x == c)
#                 result = Math.min(result, move);

#             for(int a=0; a<4; a++){
#                 int ny = y+Y[a];
#                 int nx = x+X[a];
#                 int nMove = move + 1;

#                 if(ny < 1 || nx < 1 || ny > r || nx > c || visit[ny][nx][find] || nMove > t) continue;
#                 if(find == 0 && map[ny][nx] == 1) continue;

#                 visit[ny][nx][find] = true;
#                 Q.add(new Point(ny, nx, find, nMove));

#                 if(map[ny][nx] == 2){
#                     visit[ny][nx][1] = true;
#                     Q.add(new Point(ny, nx, 1, nMove));
#                 }
#             }
#         }
#         return result;
#     }