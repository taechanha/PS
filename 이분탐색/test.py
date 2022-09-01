def D(dist):
    global house, c

    n = len(house)
    base, move = 0, 1
    # 순차적으로 2개를 골라, 차이가 dist 이상이면, c -= 1, 베이스 포인터는 j로, j는 한 칸 이동
    # 미만이면, 오른쪽 포인터만 한 칸 이동
    installed = dict()
    while move < n:
        if house[move] - house[base] >= dist:
            installed[base] = 0
            installed[move] = 0
            base = move
            move += 1
        else:
            move += 1

        if len(installed) >= c:
            return True

    return False


house = [1, 2, 4, 8, 9]
c = 3
print(D())
