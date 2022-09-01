n = int(input())
arr = [int(input()) for _ in range(n)]
answer = []

for i in range(len(arr)):
    cnt = 1
    for j in range(i, -1, -1):
        if arr[i] < arr[j]:
            cnt += 1
    answer.append(cnt)

print(answer)
