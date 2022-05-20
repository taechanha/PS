def convert_to_abs(t):
    # Ex. '01:00:04.002'
    st = t.split(':')
    h = int(st[0]) * 60 * 60 * 1000
    m = int(st[1]) * 60 * 1000
    s = st[2].split('.')
    sss = int(s[1])           # 002
    s = int(s[0])             # 04
    s *= 1000

    return h + m + s + sss


def get_start_time(end_time, spent_time):
    # Ex. 01:00:02.003 ~ 01:00:04.002 & 2.0s
    st = spent_time[:-1].split('.')

    if len(st) == 2:
        spent_time = int(st[0]) * 1000 + int(st[1])
    else:
        spent_time = int(st[0]) * 1000

    return end_time - spent_time + 1


def solution(lines):

    time_lines = []
    for line in lines:
        line = line.split()
        abs_time = convert_to_abs(line[1])
        start_time = get_start_time(abs_time, line[2])
        time_lines.append((start_time, abs_time))

    start = time_lines[0][0]
    end = time_lines[-1][-1]

    glob_max = 0
    for i in range(len(time_lines)):
        cnt = 0
        base_end_time = time_lines[i][1]

        for j in range(i, len(time_lines)):
            curr_start_time = time_lines[j][0]
            if base_end_time > curr_start_time - 1000:
                cnt += 1
            # if base_end_time + 999 >= curr_start_time:
                # cnt += 1

        glob_max = max(glob_max, cnt)

    return glob_max

    # 왜 이 piece of shit이 제대로 동작하는지 알아봐야겠ㅆㅆㅆㅆㅆㅆㅆ따
    # glob_max = 0
    # for each_sec in range(start, end):
    #     for each_point in range(each_sec, each_sec+1000):
    #         curr_max = 0
    #         cnt = 0
    #         for start_time, end_time in time_lines:
    #             # if start_time > each_point + 999:
    #             #     break
    #             if start_time <= each_point + 999:
    #                 cnt += 1
    #             # if start_time <= each_point <= end_time:
    #                 # cnt += 1
    #             # if start_time - each_point <= 999:
    #                 # cnt += 1
    #         curr_max = max(curr_max, cnt)
    #     glob_max = max(glob_max, curr_max)

    # return glob_max


tc1 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
ans1 = 1
tc2 = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
ans2 = 2
tc3 = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
       "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s",
       "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
       "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
       "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
ans3 = 7
print(solution(tc1))
print(solution(tc2))
print(solution(tc3))
# abs_time = convert_to_abs('01:00:04.002')
# print('abs time: ', abs_time, '\nstart time:',
#   get_start_time(abs_time, '2.0s'))

# 다른 코드 참고 - 기능이 다르진 않은데 더 깔끔해서 복사해놨음


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1
