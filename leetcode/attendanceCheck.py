# 3 ~ N+2
# k sleeping
# Q

# return: # of not attended
import sys
from collections import deque
read = sys.stdin.readline


# def num_not_attended(Qs, Ks, s, e):
#     section = deque(range(s, e+1))
#     for each in Qs:
#         n = 1
#         while each * n <= e:
#             if each * n in section and each * n not in Ks:
#                 section.remove(each * n)
#             n += 1

#     return len(section)

# def get(Qs, Ks, s, e):
#     total = e - s + 1
#     for Q in Qs:
#         total -= e //
#     return 1

# def main():
#     N, K, Q, M = map(int, read().split())
#     Ks = list(map(int, read().split()))
#     Qs = list(map(int, read().split()))
#     Qs = [e for e in Qs if e not in Ks]

#     for i in range(M):
#         s, e = map(int, read().split())
#         # print(num_not_attended(Qs, Ks, s, e))
#     # print(N, K, Q, M, Ks, Qs, s, e)

#     return 1


# if __name__ == '__main__':
#     main()


# N, K, Q, M = map(int, input().split())
# sleepCheck = [False]*(N+3)
# sum = [0]*(N+3)

# # K
# for i in map(int, read().split()):
#     sleepCheck[i] = True

# # Q
# for i in map(int, read().split()):
#     if sleepCheck[i]:
#         continue
#     for k in range(i, N+2, i):
#         if not sleepCheck[k]:
#             sum[k] = 1

# for i in range(3, N+2):
#     sum[i] += sum[i-1]

# for i in range(M):
#     a, b = map(int, input().split())
#     print(b-a+1-(sum[b]-sum[a-1]))

N, K, _, M = map(int, read().split())
sleep = [0]*(N+3)
check = [0]*(N+3)

Ks = list(map(int, read().split()))
Qs = list(map(int, read().split()))

for i in Ks:
    sleep[i] = 1
for i in Qs:
    if sleep[i]:
        continue
    for j in range(i, N+3, i):
        if sleep[j] == 0:
            check[j] = 1

for i in range(3, N+3):
    check[i] += check[i-1]

for _ in range(M):
    s, e = map(int, input().split())  # s부터 e까지 결석한 얘들
    print(e-s+1 - (check[e]-check[s-1]))  # 전체 - (s부터 e까지 출석한 얘들)
