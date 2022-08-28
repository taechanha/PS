def countHighlyProfitableMonths(stockPrices, k):
    # Write your code here
    if len(stockPrices) < k:
        return 0
    if len(stockPrices) == k:  # 잘못 작성
        return 1

    count = 0
    for i in range(len(stockPrices) - k + 1):
        if stockPrices[i] < stockPrices[i + 1]:
            for j in range(i + 1, i + k):
                if stockPrices[j] <= stockPrices[j - 1]:
                    break
            else:
                count += 1
    return count
print(countHighlyProfitableMonths([1, 2, 3, 3, 4, 5], 3))

# def countHighlyProfitableMonths(stockPrices, k):
#     if len(stockPrices) < k:
#         return 0

#     count = 0
#     i = 0
#     # for i in range(len(stockPrices) - k + 1):
#     while i < len(stockPrices) - k + 1:
#         for j in range(i+1, i+k):
#             if stockPrices[j] <= stockPrices[j-1]:
#                 break

#         else:
#             count += 1
#             i += k
#     return count


# print(countHighlyProfitableMonths([1, 2, 3, 3, 4, 5], 3))

# import heapq


def lastStoneWeight(weights):
    store = []
    for weight in weights:
        heapq.heappush(store, -weight)
    while len(store) > 1:
        diff = heapq.heappop(store) - heapq.heappop(store)
        if diff < 0:
            heapq.heappush(store, diff)
    if len(store) == 0:
        return 0
    return -store[0]


lastStoneWeight([1, 6, 5, 2, 9, 17, 4, 7, 6])

import requests
import json


def getRelevantFoodOutlets(city, maxCost):
    url = "https://jsonmock.hackerrank.com/api/food_outlets?city={}&page=1".format(
        city)
    response = requests.get(url)
    data = json.loads(response.text)
    total_pages = data['total_pages']
    food_outlets = []
    for page in range(1, total_pages+1):
        url = "https://jsonmock.hackerrank.com/api/food_outlets?city={}&page={}".format(
            city, page)
        response = requests.get(url)
        data = json.loads(response.text)
        for item in data['data']:
            if item['estimated_cost'] <= maxCost:
                food_outlets.append(item['name'])
    return food_outlets


print(getRelevantFoodOutlets("Houston", 200))


# def countHighlyProfitableMonths(stockPrices, k):
#     # Write your code here
#     count = 0
#     for i in range(len(stockPrices)-k+1):
#         if all(stockPrices[i+j] > stockPrices[i+j+1] for j in range(k-1)):
#             count += 1
#     return count
