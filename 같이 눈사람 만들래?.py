# 4개 중 2개씩 여러 조합에 대해 각 쌍의 합의 차이가 최소가 되는 경우

n = int(input())
snows = list(map(int, input().split()))
min_diff = float('inf')

snowmans = []  # (i, j sum)

# nC2: n개 중에 눈사람 2개 뽑기
for i in range(n-1):
    for j in range(i+1, n):
        snowmans.append((i, j, snows[i]+snows[j]))

# sort by sum
snowmans.sort(key=lambda x: x[2])

# 눈사람을 크기 순으로 나열했으니, 붙어있는 두 눈사람의 크기 차이가 전체적으로 (가장 적은 크기 차이)
# 조합 시 겹치는 인덱스가 있을 수 있으니, 이 경우를 제외한 첫번째 눈사람과의 차이를 구하고 break
m = len(snowmans)
for i in range(m-1):
    for j in range(i+1, m):
        a, b, c, d = snowmans[i][:2] + snowmans[j][:2]
        if a in (c, d) or b in (c, d):
            continue
        min_diff = min(min_diff, abs(snowmans[i][2] - snowmans[j][2]))
        break

print(min_diff)


# N개 중 4개를 뽑아 2개씩 짝지어 더한 후 그 두 개의 결과 값의 차이가 가장 작은 경우, 그 차이는?

# 어려웠던 점(브루트 포스 제외): 임의로 4개를 뽑는 경우를 어떻게 효율적으로 할지?

# 해결책: 만약 4개가 아니라 2개만 뽑는 경우였다면, 1) 정렬 후 2) 붙어있는 것의 차이가 가장 작다는 점을 이용하면 됨.
#       따라서, 4개 뽑는 경우를 2개 뽑는 경우로 문제를 바꿔풀자! 