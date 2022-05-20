
def abs_time(time):
    """ HH:MM -> MM """
    h = int(time[0:2]) * 60
    m = int(time[3:])
    return h + m


def preprocess(s):
    avail = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    temp = []
    for i in range(len(s) - 1):
        if s[i] + s[i+1] in avail:
            temp.append(s[i]+s[i+1])
        elif s[i] == '#':
            continue
        else:
            temp.append(s[i])
    temp.append(s[-1])
    return temp
    # 'C#DEFGAB'
    # 1. A
    # 2. A#


def solution(m, musicinfos):
    # data: [180, 210, 'FOO', ['C', 'C#', 'B']
    data = []
    len_max = 0
    glob_max = 0
    answer = ''
    temp = []
    # preprocess -> data
    for minfo in musicinfos:
        minfo = minfo.split(',')
        for i, each in enumerate(minfo):
            minfo[i] = each.strip(' ')

        minfo[0] = abs_time(minfo[0])
        minfo[1] = abs_time(minfo[1])
        minfo[-1] = preprocess(minfo[-1])
        data.append(minfo)

    for i in range(len(data)):
        time_diff = data[i][1] - data[i][0]
        title = data[i][2]
        music = data[i][3]

        adjusted = adjust_music(time_diff, music)

        # compare

        # if len(m) > len(adjusted):
        # m, adjusted = adjusted, m
        m = preprocess(m)
        len_m = len(m)
        found = 0
        # print(m, adjusted)
        # return
        for i in range(len(adjusted) - len_m + 1):
            if m == adjusted[i: i+len_m]:
                found = True

        if found:
            temp.append([time_diff, title])
    # return
    # print(temp)
    if len(temp) == 1:
        return temp[0][1]

    diff_max = 0
    title_max = ''
    for i in range(len(temp) - 1):
        if temp[i][0] > diff_max:
            diff_max = temp[i][0]
            title_max = temp[i][1]

    cnt = 0
    titles = []
    for i in range(len(temp)):
        if diff_max == temp[i][0]:
            cnt += 1
            titles.append(temp[i][1])
    if cnt >= 2:
        return titles[0]
    else:
        return title_max


def adjust_music(time_diff, music):
    """ 30, ['C', 'C#', 'B'] -> ['C', 'C#', 'B' ~ 30 loop] """
    temp = []
    for i in range(time_diff - 1):
        temp.append(music[i % len(music)])
    return temp


# 기억하는 멜로디
m = "ABCDEFG"
# 시작 시간, 종료 시간, 음악 제목, 악보 정보
musicinfos = ["12:00, 12:14, HELLO, CDEFGAB", "13:00, 13:05, WORLD, ABCDEF"]
#answer = "HELLO"

# BASE: ABCDEFG
# CDEFGAB CDEFGAB # l: 14 | overlap: 7(All)
# ABCDEF          # l: 6  | overlap: 6

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00, 03:30, FOO, CC#B", "04:00, 04:08, BAR, CC#BCC#BCC#B"]
#answer = "FOO"

# BASE: CC#B CC#B CC#B CC#B
# CC#B CC#B CC#B CC#B (CC#B CC#B CC#B CC#B CC#B CC#B) # overlap: 12(4 * 3)
# CC#B CC#B CC# (B)                                   # overlap: 8 (2*3 + 2)

m = "ABC"
musicinfos = ["12:00, 12:14, HELLO, C#DEFGAB", "13:00, 13:05, WORLD, ABCDEF"]
#answer = "WORLD"

# BASE: ABC
# C#DEFGAB C#DEFGAB # overlap: 2 [AB] !C#이라 안 되는 것
# ABCDEF            # overlap: 3 [ABC]

# 자, 뭘 판단해야하는 걸까? 어떤 절차를 거쳐야할까?

# 1. 악보 정보를 시작/종료 시간에 맞춰 늘리거나 끊기
# 2. 위 과정에서 C#같은게 걸리적거림. 따라서 문자열을 음 배열로 바꿔야 함
# 3. 위 전처리 과정을 거친 후 나온 '결과'를 BASE(m)과 일일이 비교한 후 가장 긴 놈 골라서 뱉으면 끝?


res = solution(m, musicinfos)
print(res)
