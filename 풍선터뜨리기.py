N = int(input())

arr = list(map(int, input().split()))
arr_index = [x for x in range(1, N+1)]
ans = []

idx = 0
amt = arr.pop(idx) # amt 는 풍선 속 숫자
ans.append(arr_index.pop(idx))

while len(arr) > 0:
        
    if amt < 0:
        idx = (idx + amt) % len(arr)
    else:
        idx = (idx + amt - 1) % len(arr)
        
    amt = arr.pop(idx)
    ans.append(arr_index.pop(idx))
        
        
print(*ans)