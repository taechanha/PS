"Okay"
"No"


def solution():

    a, b, c = map(int, input().split())
    normal = {}
    special = {}
    service = {}
    for _ in range(a):
        food, price = input().split()
        normal[food] = int(price)
    for _ in range(b):
        food, price = input().split()
        special[food] = int(price)
    for _ in range(c):
        food = input()
        service[food] = 0

    normal_pay = 0
    special_pay = 0
    service_ordered = 0
    n = int(input())
    for _ in range(n):
        # 손님 주문
        order = input()
        if order in normal:
            normal_pay += normal[order]

        elif order in special:
            special_pay += special[order]

        elif order in service:
            service_ordered += 1

    # 일반 메뉴 20,000 미만인데 특별 메뉴 주문한 경우
    if normal_pay < 20_000 and special_pay > 0:
        return 'No'
    # 일반 + 특별 50,000 미만인데 서비스 메뉴 주문한 경우
    if normal_pay + special_pay < 50_000 and service_ordered > 0:
        return 'No'
    # 서비스 메뉴를 2개 이상 주문한 경우
    if service_ordered > 1:
        return 'No'

    return 'Okay'


res = solution()
print(res)
