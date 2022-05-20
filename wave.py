# 1. 적절한 딜레이
# 2. 두 파동 더하기
# 3. 가장 작은 진폭분산 리턴

def solution(wave1, wave2):

    if len(wave2) > len(wave1):
        wave1, wave2 = wave2, wave1

    wave1, wave2 = make_same_length(wave1, wave2)

    if is_same_amplitude(wave1) or is_same_amplitude(wave2):
        added = add_two_waves(wave1, wave2)
        return amplitude_variance(added)

    mn = 1e20
    for _ in range(len(wave1)):
        wave1 = (wave1*2)[len(wave1)-1:len(wave1)-1+len(wave1)]
        for _ in range(len(wave2)):
            wave2 = (wave2*2)[len(wave2)-1:len(wave2)-1+len(wave2)]

            added = add_two_waves(wave1, wave2)
            if is_same_amplitude(added):
                return 0
            if mn > amplitude_variance(added):
                mn = amplitude_variance(added)

    return mn


def make_same_length(wave1, wave2):

    wave2 = wave2 * (len(wave1) // len(wave2))
    wave2 += wave2[0:len(wave1) - len(wave2)]

    return wave1, wave2


def amplitude_variance(wave):
    amplitude = get_amplitude(wave)
    return sum(wave[i]**2 for i in range(amplitude))


def add_two_waves(wave1, wave2):
    return [x + y for x, y in zip(wave1, wave2)]


def is_same_amplitude(wave):
    return get_amplitude(wave) == 1


def get_amplitude(wave):
    for i in range(1, len(wave)//2+1):
        if wave[:i] * (len(wave)//i) == wave:
            return i
    return len(wave)


test_cases = [
    [
        [1, 2, 2, 1, 1, 2], [-2, -1]
    ],
    [
        [2, -1, 3], [-1, -1]
    ],
    [
        [0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0]
    ],
    [
        [2, 0, 1, 1, 1, 0], [0, 0, -1]
    ]
]

answers = [2, 9, 0, 1]

for case, answer in zip(test_cases, answers):
    print(answer == solution(case[0], case[1]))
