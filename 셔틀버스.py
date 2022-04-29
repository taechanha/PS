def rel_time(time):
    """ MM -> HH:MM """
    h, m = divmod(time, 60)
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    return str(h) + ":" + str(m)


def abs_time(time):
    """ HH:MM -> MM """
    h = int(time[0:2]) * 60
    m = int(time[3:])
    return h + m


def solution(n, t, m, timetable):
    glob_n = n
    for i, time in enumerate(timetable):
        # 절대시간으로 변환 -> 비교 위해
        timetable[i] = abs_time(time)

    # 그냥 시뮬돌리면 될까?
    # -> n이 1일 때 콘을 투입시키면 됨
    arrive_time = abs_time("09:00")
    while n > 0:
        n -= 1
        rest = logic(arrive_time, timetable, m)
        if type(rest) == tuple:
            return rest[1]
        arrive_time += t

    if rest >= 1:
        if glob_n == 1:
            return "09:00"
        else:
            return rel_time(abs_time("09:00") + (glob_n - 1) * t)

def logic(arrive_time, timetable, m):
    temp = []
    to_delete = []

    for i in range(len(timetable)):
        if timetable[i] <= arrive_time:
            temp.append(timetable[i])
            to_delete.append(i)
            m -= 1
        if m == 0:
            return 1, logic2(temp)  # answer could be found here
    # remove crews who already got on
    for i in to_delete[::-1]:
        timetable.pop(i)
    return m


def logic2(temp):
    for i in range(len(temp)-1):
        if temp[i] < temp[i+1]:
            return rel_time(temp[i])
    return rel_time(temp[0] - 1)


n = 10
t = 60
m = 45
tc = ["08:00", "08:01", "08:02", "08:03"]
tc = ["09:10", "09:09", "08:00"]
tc = ["09:00", "09:00", "09:00", "09:00"]
tc = ["00:01", "00:01", "00:01", "00:01", "00:01"]
tc = ["23:59"]
tc = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
      "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
res = solution(n, t, m, tc)

print(res)


# t는 시간에만 영향 미침

# 1)
# n이 1이면,
# 2)
# m이 모자라면,
# 무조건 맨 앞 시간으로
# m이 풍족하면,
# 맨 뒤에 서도 됨

# 3)
# n이 2이상이면,
# 앞 시간 애들 걸러내고, 나머지 시간들 기준으로 2) 반복하면 될 듯?
