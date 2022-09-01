


def solve():
    n, x, y = map(int,input().strip().split())
    all = n * (1+n) // 2
    if all % (x+y) >0:
        print("IMPOSSIBLE")
        return
    now = all * x // (x+y) 
    ans1= []
    for i in range(n,0,-1):
        if now>=i:
            now -= i
            ans1.append(i)
    print("POSSIBLE")
    print(len(ans1))
    for i in ans1:
        print(i,end=" ")
    print("")



t = int(input().strip())
for i in range(1,t+1):
    print(f"Case #{i}: ",end="")
    solve()