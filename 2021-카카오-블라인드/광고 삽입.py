# TODO:
# 01:48:15가 나온다. 어느 구간에서 시간을 구해서 이런 결과가 나왔는지 디버깅해서 알아내야한다.

def log_abs_time(time):
    return [abs_time(time[:8]), abs_time(time[9:])]


def abs_time(time):
    # "01:20:15-01:45:14"
    h = int(time[0:2]) * 60 * 60
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    return h+m+s


def adv_abs_time(adv_time, time):
    # "00:14:15"
    # "01:20:15-01:45:14"
    abs_adv_time = abs_time(adv_time)
    end = time[1]
    return [end-abs_adv_time, end]


def relative_time(abs_time):
    "123124"
    h, abs_time = divmod(abs_time, 3600)
    m, s = divmod(abs_time, 60)
    if h // 10 == 0:
        h = '0' + str(h)
    if m // 10 == 0:
        m = '0' + str(m)
    if s // 10 == 0:
        s = '0' + str(s)
    return str(h) + ':' + str(m) + ':' + str(s)


def solution(play_time, adv_time, logs):
    n = len(logs)
    # 1. 절대 시간으로 변환 [start, end]
    logs_list = []
    for log in logs:
        logs_list.append(log_abs_time(log))

    # 2. logs의 end가 주어지면, adv_time을 가지고 [start, end] 절대 시간 계산
    for abs_logs in logs_list:
        abs_adv_start, abs_adv_end = adv_abs_time(adv_time, abs_logs)
        cnt = 0
        local_max = -1
        for abs_logs in logs_list:
            abs_logs_start, abs_logs_end = abs_logs
            # 3. 겹치는 시간 판단
            if abs_adv_start == abs_logs_start and abs_adv_end == abs_logs_end:
                cnt += abs_adv_end - abs_adv_start
            # adv의 끝점이 logs의 시작점보다 같거나 크고 logs.end보다 작다면, 겹치는 구간은: adv.end - logs.start
            # 반대로, logs의 시작점보다 adv의 시작점이 같거나 크고, logs의 끝점보다 작다면, 겹치는 구간은: logs.end - adv.start
            elif abs_logs_start <= abs_adv_end < abs_logs_end:
                cnt += abs_adv_end - abs_logs_start
            elif abs_logs_start <= abs_adv_start < abs_logs_end:
                cnt += abs_logs_end - abs_adv_start
        if cnt > local_max:
            local_max = cnt
            abs_adv_start_MAX = abs_adv_start

    return relative_time(abs_adv_start_MAX)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
res = solution(play_time, adv_time, logs)
print(res)
