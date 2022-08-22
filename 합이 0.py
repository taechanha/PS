# 4:45 ~ 5:11
# re-try

# 10
# 2 -5 2 3 -4 7 -4 0 1 -6

# 정렬 후 투포인터 + 커팅

n = int(input())
members = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = members[i] + members[j] + members[k]
            if sum == 0:
                cnt += 1


print(cnt)


