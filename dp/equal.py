def steps(number):
    remainder = [0, 1, 1, 2, 2]
    return number // 5 + remainder[number % 5]

T=int(input())
for loop in range(T):
    N = int(input())
    if N==0:
        input()
        print(0)
        continue
    distribution = list(map(int, input().split()))
    distribution.sort()
    minimum = distribution[0]
    totalsteps = [0,1,1,2,2]
    for i in range(5):
        for element in distribution[1:]:
            totalsteps[i] += steps(element-minimum+i)
    print(min(totalsteps))
                    