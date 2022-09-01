n, m = map(int, input().split())

base = set()
for _ in range(n):
    string = input()
    base.add(string)

cnt = 0
for _ in range(m):
    prefix_cand = input()
    for string in base:
        if string.startswith(prefix_cand):
            cnt += 1
            break

print(cnt)
