# 5:52 ~

def dfs(i, score):
    global max_score
    if i == n:
        return score
    if i in memo:
        return memo[i]
    group = []
    max_score = 0
    for j in range(i, n):
        group.append(stu[j])
        next_score = score + max(group) - min(group)
        max_score = max(max_score, dfs(j+1, next_score))

    memo[i] = max_score
    return max_score


n = int(input())
stu = list(map(int, input().split()))
dy = [0] * n
for i in range(n):
    for j in range(i, -1, -1):
        dy[i] = max(dy[i], stu[i]-stu[j])  # + dy[i]

print(dy)
