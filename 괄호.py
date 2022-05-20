t = int(input())
while t:
    t -= 1
    
    open = 0
    si = input()
    for each in si:
        if each == '(':
            open += 1
        else:
            if open > 0:
                open -= 1
            else:
                open = True # special case handling -> print("NO")
                break
            
    if open > 0:
        print("NO")
    else:
        print("YES")

# (())())     -> x
# (((()())()  -> x 
# (()())((())) -> o
