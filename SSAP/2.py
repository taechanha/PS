# N개의 바구니가 있음, 각 바구니마다 사과가 있을 수도, 없을 수도 있음
# 예를 들어, 5개의 바구니가 있고, 시작할 때는 2, 4번 바구니에만 사과가 있음
#    0 1 0 1 0
#
# 사과를 특정 알고리즘으로 먹는 벌레를 특정 위치에 놓아주려고함
# 알고리즘: 매 순간 자기와 가장 가까운 위치로 이동해서 사과 먹음; 5번이 시작위치면 4번 바구니로 이동해서 사과 먹음 -> 사라짐 -> 2번 이동
#
# 벌레 오류: 가장 가까운 사과 바구니의 거리가 2개이고, 같으면 그 위치에서 죽음; 모든 사과를 먹지 못함
#
# 벌레가 모든 사과를 먹을 수 있는 시작점 중에서 입력 X와 가장 가까운 곳과의 거리 출력
#
#
# N <= 300, 1 <= X <= N

# 17 9
# 1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1
# => 3

def move_to_closest_apple(tmp_baskets, curr):
    global napples

    if tmp_baskets[curr] == 1:
        tmp_baskets[curr] = 0
        napples -= 1
        return curr

    # left
    left_dist = [float('inf'), -1]
    for i, x in enumerate(range(curr, -1, -1)):
        if tmp_baskets[x]:
            left_dist = (curr - x, x)
            break
    # right
    right_dist = [float('inf'), -1]
    for i, x in enumerate(range(curr, len(tmp_baskets))):
        if tmp_baskets[x]:
            right_dist = (x - curr, x)
            break

    if left_dist == [float('inf'), -1] == right_dist:
        return 'clear'

    if left_dist[0] > right_dist[0]:
        dist, x = right_dist
    elif right_dist[0] > left_dist[0]:
        dist, x = left_dist
    else:
        return 'fail'

    tmp_baskets[x] = 0
    napples -= 1
    return x


def solution(baskets, X):
    global napples
    n = len(baskets)
    possibles = []

    # O(n)
    for start in range(n):
        napples = sum(1 for basket in baskets if basket == 1)
        temp_baskets = baskets[:]

        curr = start
        # O(n)
        while napples:
            ret = move_to_closest_apple(temp_baskets, curr)  # O(n)
            if type(ret) == str:
                if ret == 'clear':
                    possibles.append(curr)
                elif ret == 'fail':
                    break
            else:
                curr = ret

        if napples == 0:
            possibles.append(start)

    if not possibles:
        return -1
    return min(abs(pos-X) for pos in possibles)


# baskets = [0, 1, 0, 1, 0]
# x = 4
n, x = map(int, input().split())
baskets = list(map(int, input().split()))
ans = solution(baskets, x-1)
print(ans)
