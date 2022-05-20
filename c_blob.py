
n = int(input())

if n == 1:
    print("Yes")
    print(1)
else:
    for i in range(1, n):
        if i * 2 + (n - i - 1) * 4 == n * 5 - 4:
            print("Yes")
            print(i, (n - i - 1))
            break
    else:
        print("No")
