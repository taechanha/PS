
# records = ["john share", "mary comment", "jay share", "check notification", "check notification", "sally comment", "james share",
#    "check notification", "lee share", "laura share", "will share", "check notification", "alice comment", "check notification"]

records = ["john share", "mary share", "jay share", "james comment", "lee share", "check notification",
           "sally comment", "laura comment", "check notification", "will share", "ruby share", "check notification"]


def actionizer(notification):
    # A shared your post -> 4, 1
    # A and B shared your post -> 6, 3
    # A and N others shared your post -> 7, 4
    tokens = notification.split()
    if len(tokens) == 4:
        action = tokens[1]
        case = 1
    elif len(tokens) == 6:
        action = tokens[3]
        case = 2
    elif len(tokens) == 7:
        action = tokens[4]
        case = 3
    elif len(tokens) == 5:  # A commented on your post -> 5, 1
        action = tokens[1]
        case = 4
    elif len(tokens) == 7:  # A and B commented on your post -> 7, 3
        action = tokens[3]
        case = 5
    else:  # len(tokens) == 8:                  # A and N others commented on your post -> 8, 4
        action = tokens[4]
        case = 6
    return case, action


def updateMessage():
    if len(notification) < 2:
        return -1

    for i in range(len(notification) - 1):
        case1, action1 = actionizer(notification[i])
        case2, action2 = actionizer(notification[i+1])  # back
        if action1 == action2:
            back = notification.pop()
            front = notification.pop()  # 순서 조심
            A = front.split()[0]
            B = back.split()[0]
            # print(case1, case2)
            string = 'nothing yet'
            if case1 == 1 and case2 == 1 or case1 == 4 and case2 == 4:
                if action1 == "shared":
                    string = f'{A} and {B} shared your post'
                else:
                    string = f'{A} and {B} commented on your post'
            elif case1 == 2 and case2 == 1 or case1 == 5 and case2 == 4:
                if action1 == "shared":
                    string = f'{A} and {2} shared your post'
                else:
                    string = f'{A} and {2} commented on your post'
            else:  # case1 == 3 and case2 == 1 or case1 == 6 and case2 == 4:
                tokens = front.split()
                A = tokens[0]
                N = int(tokens[2]) + 1
                if action1 == "shared":
                    string = f'{A} and {B} shared your post'
                else:
                    string = f'{A} and {B} commented on your post'

            notification.append(string)


def updateStore():
    if len(store) < 2:
        return -1

    for i in range(len(store) - 1):
        case1, action1 = actionizer(store[i])
        case2, action2 = actionizer(store[i+1])  # back
        if action1 == action2:
            back = store.pop()
            front = store.pop()  # 순서 조심
            A = front.split()[0]
            B = back.split()[0]
            # print(case1, case2)
            string = 'nothing yet'
            if case1 == 1 and case2 == 1 or case1 == 4 and case2 == 4:
                if action1 == "shared":
                    string = f'{A} and {B} shared your post'
                else:
                    string = f'{A} and {B} commented on your post'
            elif case1 == 2 and case2 == 1 or case1 == 5 and case2 == 4:
                if action1 == "shared":
                    string = f'{A} and {2} shared your post'
                else:
                    string = f'{A} and {2} commented on your post'
            else:  # case1 == 3 and case2 == 1 or case1 == 6 and case2 == 4:
                tokens = front.split()
                A = tokens[0]
                N = int(tokens[2]) + 1
                if action1 == "shared":
                    string = f'{A} and {B} shared your post'
                else:
                    string = f'{A} and {B} commented on your post'

            store.append(string)


notification = []
store = []

for each in records:
    user, action = each.split()
    if action == "share":
        string = f'{user} shared your post'
        notification.append(string)
    elif action == "comment":
        string = f'{user} commented on your post'
        notification.append(string)
    elif action == "notification":
        store.append(notification.pop())

    updateMessage()
    updateStore()
    # print(notification)

print(store)

# 1) 1)
# A shared ~                -> 1
# 2) 1)
#   A and B shared ~        -> 3
#   C shared ~
# 3) 1)
#   A and N other shared ~  -> 4
#   B shared ~


# noti
# A shared ~               # 1
# A and B shared ~         # 2
# A and N others shared ~  # 3

# store
# A shared ~               # 1
# A and B shared ~         # 2
# A and N others shared ~  # 3
