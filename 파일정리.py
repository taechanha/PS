# 파일 확장자 별로 정리
# 사전 순 정렬, Key = 확장자 (not 개수)
from collections import defaultdict

n = int(input())
ext2cnt = defaultdict(int)

for _ in range(n):
    fname = input()
    idx = fname.index('.')
    ext = fname[idx + 1:]
    ext2cnt[ext] += 1

for key in sorted(ext2cnt):
    print(key, ext2cnt[key])
