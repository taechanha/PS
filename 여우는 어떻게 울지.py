# 6:32 ~ 7:00

def get_knowns():
    knowns = set()
    while True:
        si = input()
        if si == 'what does the fox say?':
            break
        si = si.split()
        knowns.add(si[2])
    return knowns


def get_answer(sounds, knowns):
    answer = []
    for sound in sounds:
        if not sound in knowns:
            answer.append(sound)
    return answer


t = int(input())
while t:
    t -= 1
    sounds = input().split()
    knowns = get_knowns()
    answer = get_answer(sounds, knowns)
    print(*answer)
