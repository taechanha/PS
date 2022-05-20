# def solution(n, k, cmd):
#     cmds = cmd[:]
#     N = n
#     board = list(range(N))
#     cursor = k
#     stack = []

#     for cmd in cmds:
#         cmd = list(cmd.split())
#         if len(cmd) == 1:
#             op = cmd[0]
#             # Z
#             if op == 'Z':
#                 print("Z: ", cursor, board[cursor], board)
#                 idx, item = stack.pop()
#                 if idx < cursor:
#                     cursor += 1
#                 board.insert(idx, item)
#                 print(cursor, board[cursor], board)
#             # C
#             elif op == 'C':
#                 print("C: ", cursor, board[cursor])
#                 stack.append((cursor, board[cursor]))
#                 board.pop(cursor)
#                 if cursor >= len(board):
#                     cursor -= 1
#                 print(cursor, board[cursor])
#                 # exit()
#         else:
#             op, n = cmd[0], int(cmd[1])
#             # D 1
#             if op == 'D':
#                 print("D: ", cursor, board[cursor], n)
#                 cursor += n
#                 print(cursor, board[cursor])
#             # U 1
#             elif op == 'U':
#                 print("U: ", cursor, board[cursor], n)
#                 cursor -= n
#                 print(cursor, board[cursor])

#     # print(board)
#     ans = ['X'] * N
#     for i in board:
#         ans[i] = 'O'
#     return ''.join(ans)

def solution(n, k, cmds):
    class node:
        def __init__(self, idx, up, down) -> None:
            self.idx = idx
            self.up = up
            self.down = down
            self.state = "O"

    def u(k, x):
        for _ in range(x):
            k = table[k].up
        return k

    def d(k, x):
        for _ in range(x):
            k = table[k].down
        return k

    def c(k, x):  # x 필요없는데 파라미터 통일을 위해 넣음
        pick = table[k]
        trash.append(pick)
        pick.state = "X"
        if pick.up != None:
            table[pick.up].down = pick.down
        if pick.down != None:
            table[pick.down].up = pick.up
        return pick.down if pick.down != None else pick.up

    def z(k, x):  # x 필요없는데 파라미터 통일을 위해 넣음
        pick = trash.pop()
        pick.state = "O"
        if pick.up != None:
            table[pick.up].down = pick.idx
        if pick.down != None:
            table[pick.down].up = pick.idx
        return k

    switch = {
        "U": u,
        "D": d,
        "C": c,
        "Z": z,
    }

    table = [node(i, i-1, i+1) for i in range(n)]
    table[0].up = None
    table[n-1].down = None

    trash = []

    for cmd in cmds:
        k = switch[cmd[0]](k, int(cmd[2:]) if cmd[2:] else 0)
        # print("".join([cell.state for cell in table]))

    return "".join([cell.state for cell in table])


cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
n = 8
k = 2
# "OOOO X OOO"
# "OO X O X OOO"
res = solution(n, k, cmd)
print(res)
