N = int(input())
a = list(input().split())
b = list(input().split())
success = True
try:
    for i in range(N):
        # if a[i] == b[i]:
        #     success = False
        #     break
        j = b.index(a[i])
        if i == j:
            success = False
            break
        else:
            if b[i] != a[j]:
                success = False
                break
except:
    success = False
    
if success:
    print("good")
else:
    print("bad")