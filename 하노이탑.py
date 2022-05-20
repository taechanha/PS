def hanoi(n, from_, to_, spare):
    if n == 1:
        print(from_, to_)
    else:
        hanoi(n-1, from_, spare, to_)
        hanoi(1, from_, to_, spare)
        hanoi(n-1, spare, to_, from_)


n = int(input())

print(2**n-1)

if n <= 20:
    hanoi(n, 1, 3, 2)
