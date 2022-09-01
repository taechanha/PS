# 12:59 ~

n = int(input())
data = []
for _ in range(n):
    color, size = map(int, input().split())
    data.append((color, size))


data.sort(key=lambda x: (x[1]))
prefix_sum = []

for color, size in data:
    

    print(ans)

# 3 8 10 15