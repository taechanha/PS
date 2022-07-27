import string
t = int(input())
i = 0
while i < t:
    i += 1
    
    n = int(input())
    pw = input()
    
    alphas = string.ascii_lowercase
    for alpha in alphas:
        if alpha in pw:
            break
    else:
        pw += alphas[0]
    
    alphas = alphas.upper()
    for alpha in alphas:
        if alpha in pw:
            break
    else:
        pw += alphas[0]
        
    for digit in range(0, 10):
        if str(digit) in pw:
            break
    else:
        pw += '0'
    
    for special in "#@*&":
        if special in pw:
            break
    else:
        pw += '#'
        
    if len(pw) < 7:
        pw += '0' * (7 - len(pw))
    
    print(f'Case #{i}: ', pw)
    