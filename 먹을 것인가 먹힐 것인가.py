





































# t = int(input())

# def lower_bound(a, l, r, x):
#     # A[L...R]에서 X 미만의 수(X보다 작은 수) 중 제일 오른쪽 인덱스를 return 하는 함수
#     # 그런게 없다면 L - 1을 리턴
#     res = l - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if a[mid] < x:
#             res = mid
#             l   = mid + 1
#         else:
#             r = mid - 1
#     return res

# while t:
#     t -= 1

#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     b.sort()
#     cnt = 0

#     # B배열에 대해 이분탐색을 할 예정이니까, 정렬을 해주자.
#     b.sort()
#     ans = 0
#     for x in a:
#         # A[i]를 선택했을 때, B에서는 A[i]보다 작은 게 몇 개나 있는지 count하기
#         ans += lower_bound(b, 0, m-1, x) + 1


