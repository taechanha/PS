# 자릿수가 올라갈 때마다 하나씩 더 추가된다고 생각하면 되나?
# import time
# n = int(input())
# s = time.time()
# cnt = 0

# for nn in range(1, n + 1):
#     cnt += len(str(nn))

# e = time.time()
# print(cnt, e - s)


import sys
n = int(sys.stdin.readline())
ans, acc = 0, 0
for i in range(1, 11):
    acc = acc*10+9
    if n >= acc:
        ans += (10**(i-1)*9)*i
    else:
        ans += (n-acc//10)*i
        break
print(ans % 1234567)
