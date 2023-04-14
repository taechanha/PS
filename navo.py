def solution(R, R_u, R_t, records):
    mem = dict()
    days = set()

    # 순회하면서 각 요일 별로 여태까지의 아이템들을 누적 계산 (idx 아이템이 day까지 총 몇 시간 썼는지)
    for day, idx, time in records:
        days.add(day)
        
        if idx in mem:
            if day in mem[idx]:
                mem[idx][day] += time
            else:
                mem[idx][day] = time
        else:
            mem[idx] = {day: time}
    
    print(mem)
    
    ans = set()
    deletes = []
    for idx in mem.keys():
        r = R
        while r != 0: 
            if r in mem[idx]:
                if mem[idx][r] <= R_u:
                    deletes.append(idx)
                    ans.add(idx)
                    break
            
            r -= 1


    deletes = list(deletes)
    for idx in deletes:
        del mem[idx]
    
    deletes = []
    for idx in mem.keys():
        acc = 0
        for day in mem[idx].keys():
            acc += mem[idx][day]
        
        if acc < R_t:
            deletes.append(idx)
            ans.add(idx)
    
    deletes = list(deletes)
    for idx in deletes:
        del mem[idx]
        
    
    return sorted(list(ans))

n, Q, recent_day, recent_use, total_use = map(int, input().split())
records = []
for _ in range(Q):
    day, idx, time = map(int, input().split())
    records.append((day, idx, time))
    
ans = solution(recent_day, recent_use, total_use, records)
print(ans)

# 4 5 10 20 30
# 8 1 10
# 15 3 40
# 1 2 40
# 4 4 25
# 20 1 20