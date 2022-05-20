class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.removed = False


def solution(n, k, cmd):
    head = temp = Node()
    for _ in range(n):
        new = Node()
        temp.next = new
        new.prev = temp
        temp = new

    p = head
    while p != None:
        print(p)
        p = p.next

    stack = []
    # linkedList = [Node() for _ in range(n)]
    p = head
    cnt = k
    while cnt != 0:
        p = p.next
        cnt -= 1
    curr_node = p
    # pointer = linkedList[k]
    # init LL
    # for i in range(1, n):
    #     linkedList[i].prev = linkedList[i-1]
    #     linkedList[i-1].next = linkedList[i]

    # process command
    for instruction in cmd:
        si = instruction.split()
        op = si[0]
        if len(si) == 2:
            num = int(si[1])

        if op == 'U':
            cnt = num
            while curr_node.prev and cnt != 0:
                curr_node = curr_node.prev
                cnt -= 1

        elif op == 'D':
            cnt = num
            print()
            while curr_node.next and cnt != 0:
                print(curr_node)
                curr_node = curr_node.next
                cnt -= 1

        elif op == 'C':
            stack.append(curr_node)
            curr_node.removed = True
            prev_node = curr_node.prev
            next_node = curr_node.next

            if prev_node:
                prev_node.next = next_node

            if next_node:
                next_node.prev = prev_node
                curr_node = next_node

            if next_node:
                curr_node = prev_node

        elif op == 'Z':
            node = stack.pop()
            node.removed = False
            prev_node = node.prev
            next_node = node.next
            if prev_node != None:
                prev_node.next = node
            if next_node != None:
                next_node.prev = node

    # set the answer following thru LL
    answer = ''
    p = head
    while p != None:
        if p.removed:
            answer += 'X'
        else:
            answer += 'O'
        p = p.next

    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", ]  # "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
