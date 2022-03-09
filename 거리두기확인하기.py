# --------------------- ACCEPTED ---------------

def dfs(i, j):
    stack = [(i, j, 0)]
    visited = [(i, j)]
    while stack:
        r, c, dist = stack.pop()

        if dist == 2:
            if place[r][c] == 'P':
                return 0
            else:
                continue

        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if (nr, nc) in visited:
                continue
            if place[nr][nc] == 'X':
                continue
            if place[nr][nc] == 'P':
                return 0

            stack.append((nr, nc, dist + 1))
            visited.append((nr, nc))


# 우 좌 하 상
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
ans = []
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

for place in places:
    rows = len(place)
    cols = len(place[0])
    outer_fl = 0
    for r in range(rows):
        inner_fl = 0
        for c in range(cols):
            if place[r][c] != 'P':
                continue
            if dfs(r, c) == 0:
                print(place, r, c)
                ans.append(0)
                inner_fl = 1
                break
        if inner_fl == 1:
            outer_fl = 1
            break
    if outer_fl == 0:
        ans.append(1)
print(ans)
