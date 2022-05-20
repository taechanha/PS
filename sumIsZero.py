# def n_cases(a, chosen):
#     if len(chosen) >= 3:
#         if sum(chosen) == 0:
#             global cnt
#             cnt += 1
#     else:
#         for i in range(len(a)):
#             chosen.append(a[i])
#             n_cases(a[i+1:], chosen)
#             chosen.pop()


# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#     nums = {}
#     for each in a:
#         nums[each] = 0

#     cnt = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[a[i]] == 0:
#             del nums[a[i]]
#             target = -(a[i] + a[j])
#             if target in nums:
#                 cnt += 1


#     global cnt
#     cnt = 0

#     if n < 3:
#         print(0)
#         return

#     n_cases(a, [])
#     print(cnt)


# if __name__ == '__main__':
#     main()


import sys
input = sys.stdin.readline

# n, *v = map(int, open(0).read().split())
n = int(input())
v = list(map(int, input().split()))
ans, cnt = 0, [0] * 40001

for i in range(n):
    ans += cnt[20000 - v[i]]
    for j in range(i):
        cnt[20000 + v[i] + v[j]] += 1
print(ans)
