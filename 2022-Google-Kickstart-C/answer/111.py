

def calc(n,x):
    ans = []
    for i in range(n):
        if ((x>>i)&1)==1:
            ans.append(2**i)
    return ans

def solve():
    n = int(input().strip())
    s = input().strip()
    n = len(s)
    char1 = False
    char2 = False
    char3 = False
    char0 = False
    for i in range(n):
        if ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
            char0 = True
        if ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
            char1 = True
        if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
            char2 = True
        if s[i] in ['#','@','*','&']:
            char3 = True
    if not char0:
        s = s + '0'
    if not char1:
        s = s + 'a'
    if not char2:
        s = s + 'A'
    if not char3:
        s = s + '#'
    while len(s)<7:
        s = s + '1'
    print(s)



t = int(input().strip())
for i in range(1,t+1):
    print(f"Case #{i}: ",end="")
    solve()