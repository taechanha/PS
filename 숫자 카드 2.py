# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# n = int(input())
# a = list(input().split())
# check = dict()
# for each in a:
#     if each not in check:
#         check[each] = 1
#     else:
#         check[each] += 1

# m = int(input())
# b = list(input().split())

# flag = 0
# for i, each in enumerate(b):
#     if len(b)-1 == i:
#         flag = 1

#     if each in a:
#         print(str(check[each]))
#         if flag == 0:
#             print(" ")
#     else:
#         print(str(0))
#         if flag == 0:
#             print(" ")

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
dic = dict()
for i in a:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
for i in b:
    try:
        print(dic[i], end=" ")
    except:
        print(0, end=" ")
