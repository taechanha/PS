# 2:36 pm ~ 3:50 pm

# n개의 센서, k개의 집중국 설치
# 각 집중국이 m개의 센서를 커버할 때, 각 센서들로의 거리의 합을 최소화하면, 전역적으로 거리 합의 최솟값이 나온다
# 따라서, interval이 큰 경우는 커버하지 않게끔 집중국 설치

n, k = map(int, input().split())
censors = list(map(int, input().split()))

# 1. censor 정렬
censors.sort()

# 2. 인접한 센서 간 거리 차이 계산 - diff

# 3. 차이가 큰 것 k-1개 제거; 현재 설치할 집중국이 아니라 다른 집중국이 커버한다.
