import sys
from collections import defaultdict
d = defaultdict(int)
cnt = 0
while True:
    input_ = sys.stdin.readline()[:-1]
    if input_ == '':
        break
    cnt += 1
    d[input_] += 1

for key in sorted(d):
    fmt = "%.4f" % (100 * d[key]/cnt)
    print(f'{key} {fmt}')
