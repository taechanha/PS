# 33            45         ?        15
# last time, fix_time, curr_time, interval

# 1. last_time//interval * interval
# 2-1. if last_time := fix_time의 배수:
#           do nothing
# 2-2. else
#           last_time + interval := target time


def solution(events, M):
    from collections import deque
    # settings
    Q = deque()
    curr_m = M
    ans = []

    # 시간 순 정렬
    events.sort(key=lambda x: x.split()[0])

    # 이벤트를 시간 순서대로 순회하면서 수리
    K = 1
    for event in events:
        infos = event.split()
        time = infos[0]

        if len(infos) == 2:  # 대기 표 받은 사람
            Q.append(K)
        else:  # 도중에 나간 사람
            Q.remove(K)

        if time >= curr_m:
            ans.append(Q.popleft())
            curr_m += M

    return ans
