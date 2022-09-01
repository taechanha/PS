
mp = {}


def check(tmp, last, now):
    if tmp not in now:
        return False
    for d in now:
        if d in last:
            return True
    return False


def DFS(str_days, day, last):
    if str_days == "":
        return 1
    today = str_days[0]
    sumd = 0
    for now in ['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ABD', 'ACD', 'BCD', 'ABCD']:
        if check(today, last, now):
            if (str_days[1:], day+1, now) in mp:
                sumd = (sumd + mp[(str_days[1:], day+1, now)]) % 1000000007
            else:
                tmpd = DFS(str_days[1:], day+1, now) % 1000000007
                sumd = (sumd + tmpd) % 1000000007
    mp[(str_days, day, last)] = sumd
    return sumd


T: int = int(input())
for test_case in range(1, T + 1):
    day = input()
    answer = DFS(day, 0, "A")
    print(f"#{test_case} {answer}")
