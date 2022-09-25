def chooseTime(times, ystart, yend):
    rcount = 0
    maxcount = time = 0     
    for t in times:
        if t[1] == 'start':
            rcount = rcount + 1
        elif t[1] == 'end':
            rcount = rcount - 1
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
    return maxcount, time

def bestTimeToPartySmart(schedule, start, end): 
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))

    times.sort(key=lambda x: x[0])

    maxcount, time = chooseTime(times, start, end)

    print ('Best time to attend the party is at', time, 'o\'clock', ':', maxcount, \
        'celebrities will be attending!')

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0),
           (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
           (8.0, 10.0), (9.0, 12.0), (9.5, 10.0),   
           (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
start, end = 3, 5

res = bestTimeToPartySmart(sched2, start, end)
print(res)
