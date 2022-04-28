n = int(input())
nums = list(map(int, input().split()))
maps = {}
for i in range(len(nums)):
    maps[nums[i]] = 0

maps = {key: i for i, key in enumerate(sorted(maps.keys()))}

for num in nums:
    print(maps[num], end=" ")
