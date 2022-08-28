import re

# check if the email is valid using regex
answer = set()
n = int(input())
for _ in range(n):
    si = input()
    valid = True
    if re.match(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$", si):
        username, domain = si.split('@')
        if len(username) < 1:
            continue
        if len(domain) < 1:
            continue
        # check first or last periods
        if username[0] == '.' or username[-1] == '.':
            continue
        # check consecutive periods
        for i in range(len(username)-1):
            if username[i] == username[i+1] and username[i] == '.':
                valid = False
        if not valid:
            continue
        new_username = ''
        for ch in username:
            if ch != '.':
                new_username += ch
        if not (6 <= len(new_username) <= 30):
            continue
        username = new_username.lower()

        # domain
        domain, part = domain.split('.')
        if domain[0] == '.' or domain[1] == '.':
            continue
        domain = domain.lower()
        part = part.lower()
        if not (3 <= len(domain + part) <= 30):
            continue
        email = username + '@' + domain + '.' + part
        answer.add(email)

# print(answer)
print(len(answer))
