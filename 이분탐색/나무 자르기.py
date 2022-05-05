def determination(H):
    global trees, m
    sum = 0
    # H높이로 나무들을 잘랐을 때, M만큼 얻을 수 있으면 True, 없으면 False를 return
    for tree in trees:
        cut = tree-H
        if cut > 0:
            sum += cut
    return sum >= m


def bsearch():
    global m
    L = 0
    R = 2_000_000_000
    ans = 0
    # [L...R] 범위 안에 정답이 존재
    # 이분탐색과 determination 문제를 이용해서 빠르게 answer를 구하자
    while L <= R:
        mid = (L + R) // 2
        if determination(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)


n, m = map(int, input().split())
trees = list(map(int, input().split()))
bsearch()
