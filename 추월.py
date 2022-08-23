n = int(input())
M = {}
cars = []
cnt = 0
for i in range(n):
    car = input()
    M[car] = i
    cars.append(car)
for i in range(n):
    car = input()
    if M[car] > i:
        cnt += 1
print(cnt)
