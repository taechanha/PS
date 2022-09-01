# 2:36 ~ 3:24 (hard) 

# 1. 3 2 1
# 2. 1 3 4 2

N = int(input())
books = [int(input()) for _ in range(N)]
target = N
answer = 0
for i in range(N-1, -1, -1):
    # 현재 값이 찾으려고 하는 값이라면, 찾았으니 찾으려고 하는 값을 변경
    if books[i] == target:
        target -= 1
    # 현재 값이 찾으려고 하는 값이 아니라면, 위치를 옮겨야하니 카운트
    else:
        answer += 1
 
print(answer)