N, K = map(int, input().split())
apples = list(map(int, input().split()))
apples.sort()
print(sum(apples[-K:]))