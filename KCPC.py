t = int(input())
ans = []
while t:
    t -= 1
    n_team, n_problem, my_team, n_entry = map(int, input().split())
    data = {}
    for i in range(1, n_team+1):
        data[i] = {}
        data[i]['n_submit'] = 0
        data[i]['submit_time'] = float('inf')
        data[i]['submits'] = {}
        for j in range(1, n_problem+1):
            data[i]['submits'][j] = 0
    for i in range(1, n_entry+1):
        team, problem, score = map(int, input().split())
        data[team]['n_submit'] += 1
        data[team]['submit_time'] = i
        data[team]['submits'][problem] = max(
            data[team]['submits'][problem], score)
    info = []
    for k, v in data.items():
        n_submit = data[k]['n_submit']
        submit_time = data[k]['submit_time']
        score_sum = 0
        for p, s in data[k]['submits'].items():
            score_sum += data[k]['submits'][p]
        info.append((k, n_submit, submit_time, score_sum))

    info.sort(key=lambda x: [-x[3], x[1], x[2]])
    for i in range(len(info)):
        if info[i][0] == my_team:
            print(i+1)
