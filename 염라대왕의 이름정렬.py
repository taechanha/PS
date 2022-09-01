T = int(input())
for i in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input())

    data = list(set(data))
    data.sort(key=lambda x: [len(x), x])

    print(f"#{i}")
    for j in range(len(data)):
        print(data[j])
