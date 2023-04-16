H, W = map(int, input().split())
board = list(map(int, input().split()))
p1, p2 = 0, len(board)-1
p1_max, p2_max = board[p1], board[p2]
ans = 0

while p1 < p2:
    p1_max = max(p1_max, board[p1])
    p2_max = max(p2_max, board[p2])
    if p1_max <= p2_max:
        ans += p1_max - board[p1]
        p1 += 1
    else:
        ans += p2_max - board[p2]
        p2 -= 1
print(ans)