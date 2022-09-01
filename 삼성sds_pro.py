def add_color(c):
    global color, color_kind
    color[c] += 1
    if color[c] == 1:
        color_kind += 1


def remove_color(c):
    global color, color_kind
    color[c] -= 1
    if color[c] == 0:
        color_kind -= 1
        assert color_kind >= 0


def solution(n, k, flags):
    global color, color_kind

    # validation check
    if len(set(flags)) < k:
        return False

    answer = [0] * n
    color = [0] * (n+1)
    color_kind = 0

    left = right = 0
    for i, curr_c in enumerate(flags):

        # 1-1) 조건이 만족되었다면, 최적화
        while color_kind == k:
            c = flags[left]
            if color[c] == 1:  # 더 이상 구간 좁힐 수 없음
                break
            remove_color(c)
            left += 1

        # 1-2) 안 되었다면, 조건 만족시킬 때까지 추가
        while color_kind != k:
            c = flags[right]
            add_color(c)
            right += 1

        # # 구간 이동
        # if i != 0 and not (left <= i < right):  # 뽑아야하는 현재 깃발이 현재 구간안에 없다면
        #     # if flags[right] == flags[left]: # 추가할 다음 깃발이 삭제할 깃발과 같은 색이라면
        #     remove_color(curr_c)
        #     left += 1
        #     add_color(curr_c)        # -> 다음 깃발 추가하고 구간 늘림
        #     right += 1

        answer[i] = right - left    # 뽑은 깃발 개수 == 구간 길이

    print(answer)
    return sum(answer)


flags = [1, 2, 3, 1, 2, 3, 1, 2]
k = 3
flags = [2, 3, 2, 1, 4, 1, 2, 4]
k = 4
flags = [1]
k = 1
flags = [1, 2]
k = 1
n = len(flags)
res = solution(n, k, flags)

print(res)
