class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    tmp = []
    p = head
    while p != None:
        tmp.append(p.val)
        p = p.next

    return check(tmp)


def check(elems):
    for i in range(len(elems)//2):
        if elems[i] != elems[-i-1]:
            return False
    return True


# Runner method

# rev = None
# slow = fast = head
# while fast and fast.next:
#     fast = fast.next.next
#     rev, rev.next, slow = slow, rev, slow.next
# if fast:
#     slow = slow.next
#
# while rev and rev.val == slow.val:
#     slow, rev = slow.next, rev.next
# return not rev
