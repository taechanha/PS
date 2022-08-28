# 두 발 같은 곳 X
# 같은 -> 1
# 중앙 -> 2
# 인접 -> 3
# 반대 -> 4
# 최소 힘
#    1
#  2 0 4
#    3

# 1 2 2 4
# (0, 0) → (0, 1) → (2, 1) → (2, 1) → (2, 4)

def dfs(rest, pos, power):
    if rest == []:
        return
    else:
        # choose
        chosen = rest[0]
        rest = rest[1:]
        pos[0] = chosen
        # explore
        dfs(rest, pos, power)


dance = list(map(int, input().split()))
dfs(dance, [0, 0], 0)
