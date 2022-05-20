n, t = map(int, input().split())
kind = list(reversed([int(input()) for _ in range(n)]))
i = 0
cnt = 0
flag = 0
# t: 4200
# kind = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
while True:

    while kind[i] <= t:
        t -= kind[i]
        cnt += 1
        if t == 0:
            flag = 1
            break
    if flag == 1:
        break
    i += 1
    
if flag == 1:
    print(cnt)