# 2:13 ~ 2:43

# 6 6
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2

n, m = map(int, input().split())
INF = float('inf')

G = [[INF] * n for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u][v] = 1

# floyd warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

# for row in G:
#     print(row)

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        # 들어오는 수 + 나가는 수 == 전체 학생 수인 i 존재하면, ans += 1
        if (G[i][j], G[j][i]) != (INF, INF):
            cnt += 1
    if cnt == n - 1:
        # print(i)
        ans += 1

print(ans)
