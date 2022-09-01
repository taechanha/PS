import heapq

T = int(input())

for _ in range(T):
    answer = []
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for i in range(n):
        if i % 2 == 0:
            temp.sort()
            val = temp[len(temp)//2]
            answer.append(val)

    print(*answer)
