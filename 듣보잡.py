from collections import defaultdict

n, m = map(int, input().split())
un_listened_and_seen = defaultdict(int)

for _ in range(n + m):
    si = input()
    un_listened_and_seen[si] += 1

ans = []
for k, v in un_listened_and_seen.items():
    if v >= 2:
        ans.append(k)

print(len(ans))
for each in sorted(ans):
    print(each)
