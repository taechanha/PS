
# 시작 - 끝 - 스트리밍 끝

# ~ 시작         -> 1차 출석
# 끝 ~ 스트리밍 끝 -> 2차 출석
# 1차, 2차 출석 모두 완료 -> 출석

def validate(name):
    # 알파벳 대소문자와 숫자, 그리고 특수 기호(., _, -)로만 구성된 문자열이며 최대 20글자
    if len(name) > 20:
        return False
    for ch in name:
        if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch.isdigit() or ch == '.' or ch == '_' or ch == '-'):
            return False
    return True


start, end, stream_end = input().split()
attend = {}
while True:
    try:
        enter, name = input().split()
        if validate(name) == False:
            continue
        if enter <= start: # 1차 출석
            attend[name] = 0
        elif end <= enter <= stream_end: # 2차 출석
            if not name in attend:
                continue
            attend[name] = 1
    except EOFError or ValueError:
        break

# answer
count = 0
for name, attended in attend.items():
    if attended:
        count += 1
print(count)
