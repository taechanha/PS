# 8:27 ~ 8:42
from itertools import combinations as C

kinds_top = int(input())
dough_price, top_price = map(int, input().split())
dough_kcal = int(input())
top_kcal = []
for _ in range(kinds_top):
    top_kcal.append(int(input()))

top_kcal.sort(reverse=True)

max_kcal_per_price = dough_kcal // dough_price
prev_kcal = 0

for i, kcal in enumerate(top_kcal):
    kcal_sum = (dough_kcal + prev_kcal + kcal)
    price_sum = (dough_price + (i+1) * top_price)
    kcal_per_price = kcal_sum // price_sum
    max_kcal_per_price = max(max_kcal_per_price, kcal_per_price)
    prev_kcal += kcal


print(max_kcal_per_price)

# for r in range(1, kinds_top+1):
#     for case in C(top_kcal, r):
#         kcal_per_price = (sum(case)+dough_kcal) // (dough_price+(r*top_price))
#         max_kcal_per_price = max(max_kcal_per_price, kcal_per_price)
