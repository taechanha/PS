# import sys
# input = sys.stdin.readline
n, m = map(int, input().split())
name2idx = {}
idx2name = {}

for i in range(1, n+1):
    i, name = str(i), input()
    name2idx[name] = i
    idx2name[i] = name

# t = []
for i in range(1, m+1):
    query = input()
    if query.isdigit():
        print(idx2name[query])
        # t.append(idx2name[query])
    else:
        print(name2idx[query])
        # t.append(name2idx[query])
