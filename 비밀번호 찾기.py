import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site2pw = {}

for _ in range(n):
    site, pw = input().split()
    site2pw[site] = pw

for _ in range(m):
    site = input().strip()
    print(site2pw[site])