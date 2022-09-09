import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

scores = []

answer = 0

for i in range(n):
  scores.append(list(map(int, input().split())))

scores.sort(key=lambda x: (-x[1]))


for i in range(k):
  answer += scores[i][0]

scores.sort(key=lambda x:(-x[0]))
count = 0

for i in scores:
  if count == m:
    break
  count += 1
  answer += i[0]
  
print(answer)