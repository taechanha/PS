# def fib(n):
#     global cnt0, cnt1
#     if n == 0:
#         cnt0 += 1
#         return 0

#     elif n == 1:
#         cnt1 += 1
#         return 1

#     else:
#         return fib(n-1) + fib(n-2)


# T = int(input())
# while T:
#     T -= 1
#     cnt0 = 0
#     cnt1 = 0
#     n = int(input())
#     fib(n)
#     print(cnt0, cnt1)

T = int(input())
a = [0] * 41
b = [0] * 41
a[0] = 1
for i in range(1, 41):
    a[i], b[i] = b[i-1], a[i-1] + b[i-1]
while T:
    T -= 1
    n = int(input())
    print(a[n], b[n])
