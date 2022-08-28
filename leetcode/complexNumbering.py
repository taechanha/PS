def dfs(G, i, j):

    stack = [[i, j]]
    count_visits = 0

    while stack:
        i, j = stack.pop()

        visited[i][j] = 1
        count_visits += 1

        if G[i][j] == 0:
            break

        for index in range(4):
            x = i + dx[index]
            y = j + dy[index]

            if not (0 <= x < n and 0 <= y < n):
                continue

            if visited[x][y] == 1:
                continue

            if G[x][y] == 1:
                if [x, y] not in stack:
                    stack.append([x, y])

    return count_visits


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
res = []
# 아래, 위, 왼쪽, 오른쪽.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0 or visited[i][j] == 1:
            continue
        count_visits = dfs(arr, i, j)
        if count_visits:
            res.append(count_visits)

res.sort()
print(len(res))
for complex in res:
    print(complex)
