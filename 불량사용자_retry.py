def is_matched(origin, hidden):
    # mustbe same(length of both)
    if len(origin) != len(hidden):
        return False

    for oc, hc in zip(origin, hidden):
        if hc == '*':
            continue
        if oc != hc:
            return False
    return True


def dfs(i, j, chosen):
    if i == len(u) or j == len(b):
        if j == len(b) and chosen not in ans:
            ans.append(chosen)
        return
    else:
        if is_matched(u[i], b[j]):
            chosen += u[i] + " "
        dfs(i+1, j+1, chosen)

        dfs(i+1, j, chosen)
        dfs(i, j+1, chosen)


u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
ans = []

res = dfs(0, 0, "")
print(res)

print(ans)

# frodo crodo abc123 frodoc
# fradi frodo abc123 frodoc
# fradi crodo abc123 frodoc
