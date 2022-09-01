# 5:08 ~

conso = set('bcdfghjklmnpqrstvwxyz')
vowel = set('aeiou')

L, C = map(int, input().split())
string = input().split()

string.sort()


def dfs(i, chosen, consos, vowels):
    if len(chosen) == L:
        if consos >= 2 and vowels >= 1:
            ans.add(chosen)
        return
    if i == C:
        return
    for k in range(i, C):
        if string[k] in vowel:
            dfs(k+1, chosen+string[k], consos, vowels+1)
        elif string[k] in conso:
            dfs(k+1, chosen+string[k], consos+1, vowels)


ans = set()
dfs(0, "", 0, 0)

for row in sorted(list(ans)):
    print(row)
