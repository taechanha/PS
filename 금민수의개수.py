
def dfs(i, n, chosen):
    if i == n:
        number = int(chosen)
        data.append(number)
        return

    for num in ["4", "7"]:
        dfs(i+1, n, chosen+num)


a, b = map(int, input().split())
data = []
for i in range(1, 10):
    dfs(0, i, "")

cnt = 0
for num in data:
    if a <= num <= b:
        cnt += 1
    elif num > b:
        break

print(cnt)
