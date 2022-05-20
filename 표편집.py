# cmd
# U X: X칸 위에  있는 행 선택
# D X: X칸 아래에 있는 행 선택
# C: 현재 행 삭제 후 바로 아래 행 선택, 삭제된 행이 마지막이면 바로 윗 행 선택
# Z: 가장 최근에 삭제된 행 복구, 행 선택은 바뀌지 않음

def solution(n, k, cmd):
    table = list(range(n))
    stack = []  # (value)
    pointer: int = k

    for instruction in cmd:
        fl = 0
        si = instruction.split()
        if len(si) == 2:
            # U X, D X
            op = si[0]
            num = si[1]
            if op == 'U':
                pointer -= int(num)
            elif op == 'D':
                pointer += int(num)
        else:
            # C, Z
            op = si[0]
            if op == 'C':
                if pointer == len(table) - 1:
                    fl = -1
                    # pointer -= 1
                elif pointer == 0:
                    fl = 1
                    # pointer += 1
                else:
                    pass  # nothing to do

                item = table.pop(pointer)
                stack.append(item)

                pointer += fl

            elif op == 'Z':
                index = value = stack.pop()
                table.insert(index, value)

                if index <= pointer:
                    pointer += 1

# [0,1,2,3]: initial table
# [0,1]: current table
    ans = ''
    for each in range(n):
        if each not in table:  # optimized version: Dictionary -> not necessary
            ans += 'X'
        else:
            ans += 'O'

    return ans


# n = 8
# k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

ans = solution(n, k, cmd)
print(ans)
