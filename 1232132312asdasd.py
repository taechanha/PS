from collections import defaultdict


def bfs(r, c, visited):
    global n, m, dr, dc, board
    q = [(r, c)]
    visited[r][c] = True
    ret = defaultdict(int)
    while q:
        r, c = q.pop(0)
        ret[board[r][c]] += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == '.':
                continue
            q.append((nr, nc))
            visited[nr][nc] = True
    return ret


def solution(maps):
    global n, m, dr, dc, board
    answer = 0
    # setting
    board = maps
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])

    # 1) 구역 별, 나라 별 영토 개수
    groups = []
    visited = [[False for _ in range(m)] for __ in range(n)]
    for r in range(n):
        for c in range(m):
            if board[r][c] == '.':
                continue
            if visited[r][c]:
                continue
            group_info: dict = bfs(r, c, visited)
            groups.append(group_info)

    # ok

    # 2) 구역 별 승자 정해서 땅 점령
    winners = []
    keys = []
    for group in groups:
        winner, max_cnt = None, 0
        for country, cnt in group.items():
            if cnt > max_cnt:
                winner = country
                max_cnt = cnt
            elif cnt == max_cnt:
                if country < winner:
                    winner = country
                    max_cnt = cnt
        winners.append((winner, max_cnt))

        for country, cnt in group.items():
            if cnt < max_cnt:
                group[winner] += cnt

    print("assad: ", groups)
    # ?
    print(winners)

    # 3) 모든 구역 순회하면서 가장 넓은 영토 점령한 나라 정하기
    answer = []
    for group in groups:
        for country, cnt in group.items():
            answer.append((country, cnt))

    print("ad ", answer)
    return 1


maps = ["AABCA.QA", "AABC..QX", "BBBC.Y..",
        ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]
res = solution(maps)
print("answeR: ", res)
