def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while progresses[0] < 100:
            for i, (p, s) in enumerate(zip(progresses, speeds)):
                progresses[i] += speeds[i]

        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)

    return answer


prgrs = [93, 30, 55]
speeds = [1, 30, 5]

solution(prgrs, speeds)
