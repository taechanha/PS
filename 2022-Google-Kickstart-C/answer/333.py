def solve():
    n, m = map(int,input().strip().split())
    ants = []
    fall = []
    for i in range(n):
        j,k = map(int,input().strip().split())
        ants.append([j,i+1])
        if k==0:
            fall.append([j,0])
        else:
            fall.append([m-j,1])
    ants = sorted(ants, key = lambda x: x[0] * (n+1) + x[1])
    fall = sorted(fall, key = lambda x: x[0]*(m+1))
    # print(ants)
    # print(fall)
    left = 0
    right = n-1
    ans = []
    for i in range(n):
        if fall[i][1] == 0:
            ans.append([ants[left][1],fall[i][0]])
            left += 1
        else:
            ans.append([ants[right][1],fall[i][0]])
            right -= 1
    ans = sorted(ans, key=lambda x: x[1]*(m+1) + x[0])
    # print(ans)
    for x in ans:
        print(x[0],end=" ")
    print("")





t = int(input().strip())
for i in range(1,t+1):
    print(f"Case #{i}: ",end="")
    solve()